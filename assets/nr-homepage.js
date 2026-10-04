/**
 * NordicReflection homepage interactions.
 * Progressive enhancement only — every component works without this file.
 * Loaded once (module, defer) from sections/nr-home-hero.liquid, so it
 * never ships on pages without homepage components.
 */
(() => {
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Analytics ----------
     Same architecture as the product pages (assets/nr-pdp.js): custom
     events go through Shopify's customer-events API as nr_<name>, so any
     connected pixel can subscribe. Elements carry data-nr-event (+ optional
     data-nr-product / data-nr-source); clicks inside homepage components
     are published here. Never throws. */
  function publish(name, detail = {}) {
    try {
      window.Shopify?.analytics?.publish?.(`nr_${name}`, detail);
    } catch {
      /* analytics must never break the page */
    }
  }

  if (!window.nrHomeEventsBound) {
    window.nrHomeEventsBound = true;
    document.addEventListener('click', (event) => {
      const tracked = event.target.closest('[data-nr-scope] [data-nr-event]');
      if (!tracked) return;
      publish(tracked.dataset.nrEvent, {
        target: tracked.dataset.nrProduct || '',
        source: tracked.dataset.nrSource || '',
      });
    });
  }

  /**
   * Runs `init` for every element matching `selector`, isolating failures
   * so one broken component can't take down the rest of the page.
   */
  function initAll(selector, init) {
    document.querySelectorAll(selector).forEach((el) => {
      if (el.dataset.nrInitialized) return;
      try {
        init(el);
        el.dataset.nrInitialized = 'true';
      } catch (error) {
        console.error(`[nr-homepage] Failed to init "${selector}"`, error);
      }
    });
  }

  /* ---------- Reveal-on-scroll ---------- */
  function initReveal() {
    if (prefersReducedMotion) return;

    const targets = document.querySelectorAll('[data-nr-reveal]:not(.is-visible)');
    if (!targets.length) return;

    // Stagger containers: each direct child gets its position so the CSS
    // can delay it (see [data-nr-reveal='stagger'] in nr-homepage.css).
    targets.forEach((el) => {
      if (el.dataset.nrReveal !== 'stagger') return;
      // Skip inline <style>/<script> siblings some theme blocks render.
      [...el.children]
        .filter((child) => !['STYLE', 'SCRIPT', 'LINK'].includes(child.tagName))
        .forEach((child, index) => child.style.setProperty('--nr-i', index));
    });

    if (!('IntersectionObserver' in window)) {
      targets.forEach((el) => el.classList.add('is-visible'));
      return;
    }

    const observer = new IntersectionObserver(
      (entries, obs) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add('is-visible');
          obs.unobserve(entry.target);
        });
      },
      { rootMargin: '0px 0px -10% 0px', threshold: 0.1 }
    );

    targets.forEach((el) => observer.observe(el));
  }

  /* ---------- Wash-step keyboard/focus parity with hover ---------- */
  function initWashSteps() {
    initAll('[data-nr-wash-step]', (card) => {
      const media = card.querySelector('[data-nr-wash-step-media]');
      if (!media) return;
      card.addEventListener('focusin', () => card.classList.add('is-active'));
      card.addEventListener('focusout', () => card.classList.remove('is-active'));
    });
  }

  /* ---------- Background videos: pause control, off-screen pause, reduced motion ----------
     Every <video data-nr-video> may have a [data-nr-video-toggle] button in
     the same container. The visitor's choice wins: once they pause, the
     video stays paused even when it scrolls back into view. */
  function initVideos() {
    initAll('[data-nr-video]', (video) => {
      const toggle = video.parentElement && video.parentElement.querySelector('[data-nr-video-toggle]')
        || video.closest('.nr-hero')?.querySelector('[data-nr-video-toggle]');
      let userPaused = prefersReducedMotion;

      const sync = () => {
        if (!toggle) return;
        const paused = video.paused;
        toggle.classList.toggle('is-paused', paused);
        toggle.setAttribute('aria-label', paused ? 'Spela videon' : 'Pausa videon');
      };

      if (prefersReducedMotion) {
        video.removeAttribute('autoplay');
        video.pause();
      }

      if (toggle) {
        toggle.hidden = false;
        toggle.addEventListener('click', () => {
          if (video.paused) {
            userPaused = false;
            video.play().catch(() => {});
          } else {
            userPaused = true;
            video.pause();
          }
        });
        video.addEventListener('play', sync);
        video.addEventListener('pause', sync);
        sync();
      }

      if (!('IntersectionObserver' in window)) return;
      const observer = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              if (!userPaused) video.play().catch(() => {});
            } else {
              video.pause();
            }
          });
        },
        { threshold: 0.25 }
      );
      observer.observe(video);
    });
  }

  /* ---------- Bestseller cards: short product names ----------
     Product titles read "Name – long descriptor". On the homepage cards the
     use-case line already describes the product, so the visible name stops
     at the dash; the card link keeps the full title as its accessible name. */
  function initShortTitles() {
    document.querySelectorAll('.nr-featured-products__grid [role="heading"]').forEach((heading) => {
      if (heading.dataset.nrShort) return;
      const full = heading.textContent.trim();
      const short = full.split(/\s[–-]\s/)[0];
      if (short && short !== full) {
        heading.textContent = short;
        heading.title = full;
      }
      heading.dataset.nrShort = 'true';
    });
  }

  /* ---------- Kits: "Visa vad som ingår" component strip ----------
     Without JS every strip stays visible; with JS it opens on request. */
  function initKitToggles() {
    initAll('[data-nr-kitx-toggle]', (toggle) => {
      const strip = document.getElementById(toggle.getAttribute('aria-controls'));
      const label = toggle.querySelector('[data-nr-kitx-toggle-label]');
      const card = toggle.closest('.nr-kitx');
      if (!strip || !card) return;
      [...strip.children].forEach((part, index) => part.style.setProperty('--i', index));
      card.setAttribute('data-nr-kitx-ready', '');
      toggle.hidden = false;
      toggle.addEventListener('click', () => {
        const open = !strip.classList.contains('is-open');
        strip.classList.toggle('is-open', open);
        toggle.setAttribute('aria-expanded', String(open));
        if (label) label.textContent = open ? 'Dölj innehållet' : 'Visa vad som ingår';
      });
    });
  }

  /* ---------- Product advisor: chips as ARIA tabs ----------
     All panels are server-rendered; switching only toggles `hidden`, so
     prices and links are never stale. Arrow keys/Home/End move between
     chips (automatic activation – panels are local, nothing is fetched).
     Videos in hidden panels pause on their own: initVideos' observer sees
     them leave the viewport when the panel is hidden. */
  function initAdvisor() {
    initAll('[data-nr-advisor]', (root) => {
      const tablist = root.querySelector('[data-nr-advisor-tabs]');
      const tabs = [...root.querySelectorAll('[data-nr-advisor-tab]')];
      if (!tablist || tabs.length < 2) return;

      const panelFor = (tab) => document.getElementById(tab.getAttribute('aria-controls'));

      // Keep the chosen chip in view inside the scrollable row (phones)
      // without scrolling the page vertically.
      const reveal = (tab) => {
        if (tablist.scrollWidth <= tablist.clientWidth) return;
        const pad = 16;
        const left = tab.offsetLeft - tablist.offsetLeft;
        const right = left + tab.offsetWidth;
        if (left - pad < tablist.scrollLeft) {
          tablist.scrollTo({ left: left - pad, behavior: prefersReducedMotion ? 'auto' : 'smooth' });
        } else if (right + pad > tablist.scrollLeft + tablist.clientWidth) {
          tablist.scrollTo({
            left: right + pad - tablist.clientWidth,
            behavior: prefersReducedMotion ? 'auto' : 'smooth',
          });
        }
      };

      const select = (next, { focus = false } = {}) => {
        const current = tabs.find((tab) => tab.getAttribute('aria-selected') === 'true');
        if (focus) next.focus({ preventScroll: true });
        reveal(next);
        if (current === next) return;

        tabs.forEach((tab) => {
          const selected = tab === next;
          tab.setAttribute('aria-selected', String(selected));
          tab.tabIndex = selected ? 0 : -1;
          const panel = panelFor(tab);
          if (!panel) return;
          panel.hidden = !selected;
          panel.classList.remove('is-entering');
        });

        const panel = panelFor(next);
        if (panel && !prefersReducedMotion) {
          // Restart the enter animation even on quick repeated switches.
          void panel.offsetWidth;
          panel.classList.add('is-entering');
          clearTimeout(panel.nrEnterTimer);
          panel.nrEnterTimer = setTimeout(() => panel.classList.remove('is-entering'), 400);
        }
      };

      tabs.forEach((tab) =>
        tab.addEventListener('click', () => {
          const changed = tab.getAttribute('aria-selected') !== 'true';
          select(tab);
          if (changed) publish('dirt_advisor_select', { target: tab.dataset.nrProduct || '', source: tab.textContent.trim() });
        })
      );

      tablist.addEventListener('keydown', (event) => {
        const index = tabs.indexOf(document.activeElement);
        if (index < 0) return;
        let target = null;
        if (event.key === 'ArrowRight' || event.key === 'ArrowDown') target = tabs[(index + 1) % tabs.length];
        else if (event.key === 'ArrowLeft' || event.key === 'ArrowUp') target = tabs[(index - 1 + tabs.length) % tabs.length];
        else if (event.key === 'Home') target = tabs[0];
        else if (event.key === 'End') target = tabs[tabs.length - 1];
        if (!target) return;
        event.preventDefault();
        select(target, { focus: true });
        publish('dirt_advisor_select', { target: target.dataset.nrProduct || '', source: target.textContent.trim() });
      });

      // Theme editor: selecting a block shows its panel.
      root.addEventListener('shopify:block:select', (event) => {
        const tab = tabs.find((t) => panelFor(t) === event.target);
        if (tab) select(tab);
      });
    });
  }

  /* ---------- Routine builder (snippets/nr-routine) ----------
     Reads the cart once when a routine block comes near the viewport, and
     again after every add, then sets each block's state:
       add-on in cart            → add-on row hidden (never offered twice)
       kit in cart               → add-on and kit rows hidden
       main + add-on in cart and
       the kit is exactly those  → kit row: "De här två finns redan som färdigt kit."
       main in cart              → kit row notes the kit contains it
     Adding uses the Ajax Cart API and announces the change with Shopify's
     CartLinesUpdateEvent (same as the theme's product forms), so the cart
     icon and cart drawer/app update the way they do for any add. Nothing in
     the cart is removed or swapped automatically. */
  const cartRoot = () => (window.Shopify?.routes?.root || '/').replace(/\/?$/, '/');
  let cartPromise = null;

  function readCart(force = false) {
    if (!cartPromise || force) {
      cartPromise = fetch(`${cartRoot()}cart.js`, { headers: { Accept: 'application/json' }, credentials: 'same-origin' })
        .then((response) => (response.ok ? response.json() : null))
        .catch(() => null);
    }
    return cartPromise;
  }

  function applyRoutineState(root, cart) {
    if (!cart) return;
    const inCart = new Set((cart.items || []).map((item) => String(item.product_id)));
    const main = root.dataset.main;
    const addon = root.querySelector('[data-nr-routine-addon]');
    const kit = root.querySelector('[data-nr-routine-kit]');
    const addonId = addon?.dataset.product;
    const kitIn = kit ? inCart.has(kit.dataset.product) : false;
    const addonJustAdded = addon?.dataset.added === 'true';

    if (addon) addon.hidden = kitIn || (inCart.has(addonId) && !addonJustAdded);

    if (kit) {
      kit.hidden = kitIn;
      const components = (kit.dataset.components || '').split(',').filter(Boolean);
      const isPair =
        components.length === 2 && addonId && components.includes(main) && components.includes(addonId);
      const pairInCart = isPair && inCart.has(main) && inCart.has(addonId);
      const match = kit.querySelector('[data-nr-routine-match]');
      const text = kit.querySelector('[data-nr-routine-kit-text]');
      const hasMain = kit.querySelector('[data-nr-routine-has-main]');
      if (match) match.hidden = !pairInCart;
      if (text) text.hidden = pairInCart;
      if (hasMain) hasMain.hidden = pairInCart || !inCart.has(main) || !components.includes(main);
    }

    root.hidden = (!addon || addon.hidden) && (!kit || kit.hidden);
  }

  function refreshRoutines(cart) {
    document.querySelectorAll('[data-nr-routine]').forEach((root) => applyRoutineState(root, cart));
  }

  async function announceCartChange(source, lines, cart) {
    try {
      const { CartLinesUpdateEvent } = await import('@shopify/events');
      const deferred = CartLinesUpdateEvent.createPromise();
      source.dispatchEvent(
        new CartLinesUpdateEvent({ action: 'add', context: 'product', lines, promise: deferred.promise })
      );
      deferred.resolve({
        cart: CartLinesUpdateEvent.createCartFromAjaxResponse(cart),
        detail: { items: cart.items, source: 'nr-routine', itemCount: 1, didError: false },
      });
    } catch {
      /* Older theme without @shopify/events: the cart page still has the item. */
    }
  }

  function initRoutines() {
    const roots = document.querySelectorAll('[data-nr-routine]');
    if (!roots.length) return;

    const load = () => readCart().then(refreshRoutines);
    if ('IntersectionObserver' in window) {
      const observer = new IntersectionObserver(
        (entries, obs) => {
          if (!entries.some((entry) => entry.isIntersecting)) return;
          obs.disconnect();
          load();
        },
        { rootMargin: '400px 0px' }
      );
      roots.forEach((root) => observer.observe(root.closest('[data-nr-scope]') || root));
    } else {
      load();
    }

    initAll('[data-nr-routine-add]', (button) => {
      const row = button.closest('[data-nr-routine-addon]');
      const label = button.querySelector('[data-nr-routine-add-label]');
      const status = row?.querySelector('[data-nr-routine-status]');

      button.addEventListener('click', async () => {
        if (button.disabled) return;
        button.disabled = true;
        if (label) label.textContent = 'Lägger till…';
        if (status) status.textContent = '';

        try {
          const response = await fetch(`${cartRoot()}cart/add.js`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
            credentials: 'same-origin',
            body: JSON.stringify({ items: [{ id: Number(button.dataset.nrRoutineAdd), quantity: 1 }] }),
          });
          const result = await response.json();
          if (!response.ok || result.status) throw new Error(result.description || result.message || 'add failed');

          row.dataset.added = 'true';
          if (label) label.textContent = 'Tillagd';
          if (status) {
            status.innerHTML = `I varukorgen. <a href="${cartRoot()}cart">Till varukorgen</a>`;
          }
          const cart = await readCart(true);
          if (cart) {
            refreshRoutines(cart);
            announceCartChange(button, [{ merchandiseId: button.dataset.nrRoutineAdd, quantity: 1 }], cart);
          }
        } catch (error) {
          button.disabled = false;
          if (label) label.textContent = 'Lägg till';
          if (status) status.textContent = 'Det gick inte att lägga till just nu. Försök igen eller öppna produkten.';
        }
      });
    });
  }

  /* ---------- Results gallery: simple before/after drag slider ---------- */
  function initResultSlider() {
    initAll('[data-nr-result-slider]', (root) => {
      const range = root.querySelector('[data-nr-result-range]');
      const before = root.querySelector('[data-nr-result-before]');
      if (!range || !before) return;

      const update = () => {
        before.style.clipPath = `inset(0 ${100 - range.value}% 0 0)`;
      };
      range.addEventListener('input', update);
      update();
    });
  }

  function init() {
    initReveal();
    initWashSteps();
    initVideos();
    initKitToggles();
    initAdvisor();
    initRoutines();
    initShortTitles();
    initResultSlider();
  }

  init();

  /* ---------- Shopify Theme Editor support ---------- */
  document.addEventListener('shopify:section:load', (event) => {
    // Re-scan only the newly (re)loaded section so editing one section
    // doesn't re-run animations on the whole page.
    const scope = event.target;
    if (!scope) return init();

    scope.querySelectorAll('[data-nr-initialized]').forEach((el) => {
      delete el.dataset.nrInitialized;
    });
    init();
  });

  document.addEventListener('shopify:section:unload', (event) => {
    // Nothing to tear down explicitly — observers are scoped to elements
    // that are removed from the DOM along with the section.
  });
})();
