/**
 * NordicReflection homepage interactions.
 * Progressive enhancement only — every component works without this file.
 * Loaded once (module, defer) from sections/nr-home-hero.liquid, so it
 * never ships on pages without homepage components.
 */
(() => {
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

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

  /* ---------- Kit cards: collapsible details on small screens ---------- */
  function initKitToggles() {
    initAll('[data-nr-kit-toggle]', (toggle) => {
      const card = toggle.closest('.nr-kit');
      const label = toggle.querySelector('[data-nr-kit-toggle-label]');
      if (!card) return;
      card.classList.add('is-collapsible');
      toggle.hidden = false;
      toggle.addEventListener('click', () => {
        const open = !card.classList.contains('is-open');
        card.classList.toggle('is-open', open);
        toggle.setAttribute('aria-expanded', String(open));
        if (label) label.textContent = open ? 'Dölj detaljer' : 'Visa vad som ingår';
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
          panel.addEventListener('animationend', () => panel.classList.remove('is-entering'), { once: true });
        }
      };

      tabs.forEach((tab) => tab.addEventListener('click', () => select(tab)));

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
      });

      // Theme editor: selecting a block shows its panel.
      root.addEventListener('shopify:block:select', (event) => {
        const tab = tabs.find((t) => panelFor(t) === event.target);
        if (tab) select(tab);
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
