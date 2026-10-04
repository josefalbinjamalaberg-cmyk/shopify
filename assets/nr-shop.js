/**
 * NordicReflection collections (sections/nr-shop, sections/nr-kit-hub).
 * Progressive enhancement only: every chip, pill, sort and filter is a
 * normal link or GET form to Shopify's own filter/sort URL. This file
 *  - swaps the results in place (section rendering API) and keeps the URL
 *    in sync with history.pushState, so back/forward, reload and sharing
 *    behave exactly like the native page;
 *  - shows the live result count in the filter drawer ("Visa 6 produkter");
 *  - adds quick add (Ajax Cart API + Shopify's CartLinesUpdateEvent, the same
 *    path as the theme's product forms);
 *  - runs the Färdiga paket area tabs (hash in the URL);
 *  - publishes analytics through Shopify.analytics.publish (nr_<event>).
 */
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

function publish(name, detail = {}) {
  try {
    window.Shopify?.analytics?.publish?.(`nr_${name}`, detail);
  } catch {
    /* analytics must never break the page */
  }
}

const shopRoot = () => document.querySelector('[data-nr-shop]');
const collectionHandle = () =>
  document.querySelector('[data-nr-shop], [data-nr-kit-hub]')?.dataset.collection || '';
const activeIntent = () =>
  document.querySelector('.nr-shop-intents .nr-chip[aria-current="true"]')?.dataset.nrIntent || '';

/* ---------- In-place results ---------- */
let controller = null;

function sectionUrl(url) {
  const root = shopRoot();
  const u = new URL(url, window.location.origin);
  u.searchParams.set('section_id', root.dataset.sectionId);
  return u.toString();
}

async function fetchSection(url) {
  controller?.abort();
  controller = new AbortController();
  const response = await fetch(sectionUrl(url), { signal: controller.signal, credentials: 'same-origin' });
  if (!response.ok) throw new Error(`section ${response.status}`);
  const html = await response.text();
  return new DOMParser().parseFromString(html, 'text/html');
}

async function navigate(url, { push = true } = {}) {
  const root = shopRoot();
  if (!root) {
    window.location.href = url;
    return;
  }
  const target = root.querySelector('[data-nr-shop-root]');
  target.querySelector('.nr-shop-grid')?.classList.add('is-loading');
  try {
    const doc = await fetchSection(url);
    const fresh = doc.querySelector('[data-nr-shop-root]');
    if (!fresh) throw new Error('no results root');
    target.replaceWith(fresh);
    if (push) history.pushState({ nrShop: true }, '', url);
    revealSelectedChip();
  } catch (error) {
    if (error.name === 'AbortError') return;
    window.location.href = url;
  }
}

function revealSelectedChip() {
  const chip = document.querySelector('.nr-shop-intents .nr-chip[aria-current="true"]');
  const row = chip?.closest('.nr-chips');
  if (!chip || !row || row.scrollWidth <= row.clientWidth) return;
  const left = chip.parentElement.offsetLeft - 16;
  row.scrollTo({ left: Math.max(0, left), behavior: reduceMotion ? 'auto' : 'smooth' });
}

function urlFromForm(form) {
  const url = new URL(form.action, window.location.origin);
  const data = new FormData(form);
  for (const [key, value] of data.entries()) {
    if (value !== '') url.searchParams.append(key, value);
  }
  return url.pathname + (url.search || '');
}

document.addEventListener('click', (event) => {
  const link = event.target.closest('[data-nr-shop] [data-nr-shop-link]');
  if (!link || event.metaKey || event.ctrlKey || event.shiftKey || event.button !== 0) return;
  event.preventDefault();
  const collection = collectionHandle();
  if (link.dataset.nrIntent !== undefined) {
    publish('collection_intent_select', { collection, intent: link.dataset.nrIntent });
  } else if (link.hasAttribute('data-nr-clear')) {
    publish('collection_filter_clear', { collection });
  }
  link.closest('dialog')?.close();
  navigate(link.href);
});

window.addEventListener('popstate', () => {
  if (shopRoot()) navigate(window.location.href, { push: false });
});

document.addEventListener('change', (event) => {
  const select = event.target.closest('[data-nr-shop-sort] select');
  if (select) {
    publish('collection_sort', { collection: collectionHandle(), sort: select.value });
    navigate(urlFromForm(select.form));
    return;
  }
  const input = event.target.closest('[data-nr-drawer-form] input[type="checkbox"]');
  if (input) {
    publish('collection_filter_select', {
      collection: collectionHandle(),
      filter: input.name,
      value: input.closest('label')?.querySelector('.nr-shop-check__label')?.textContent.trim() || input.value,
      selected: input.checked,
    });
    updateDrawerCount(input.form);
  }
});

/* ---------- Drawer ---------- */
async function updateDrawerCount(form) {
  const button = form.querySelector('[data-nr-drawer-apply]');
  if (!button) return;
  try {
    const doc = await fetchSection(urlFromForm(form));
    const count = Number(doc.querySelector('[data-nr-count]')?.dataset.nrCount);
    if (Number.isFinite(count)) {
      button.textContent = count === 0 ? 'Inga produkter' : count === 1 ? 'Visa 1 produkt' : `Visa ${count} produkter`;
      button.disabled = count === 0;
    }
  } catch {
    /* keep the last label; submitting still works */
  }
}

document.addEventListener('click', (event) => {
  const open = event.target.closest('[data-nr-drawer-open]');
  if (open) {
    const dialog = document.getElementById(open.getAttribute('aria-controls'));
    if (dialog?.showModal) {
      dialog.showModal();
      open.setAttribute('aria-expanded', 'true');
      dialog.addEventListener(
        'close',
        () => {
          open.setAttribute('aria-expanded', 'false');
          open.focus();
        },
        { once: true }
      );
    }
    return;
  }
  if (event.target.closest('[data-nr-drawer-close]')) {
    event.target.closest('dialog')?.close();
    return;
  }
  // Tap on the backdrop closes the sheet.
  if (event.target.matches?.('dialog[data-nr-drawer]')) event.target.close();
});

document.addEventListener('submit', (event) => {
  const form = event.target.closest('[data-nr-drawer-form]');
  if (!form || !shopRoot()) return;
  event.preventDefault();
  form.closest('dialog')?.close();
  navigate(urlFromForm(form));
});

/* ---------- Quick add ---------- */
const cartRoot = () => (window.Shopify?.routes?.root || '/').replace(/\/?$/, '/');

async function announceCartChange(source, variantId, cart) {
  try {
    const { CartLinesUpdateEvent } = await import('@shopify/events');
    const deferred = CartLinesUpdateEvent.createPromise();
    source.dispatchEvent(
      new CartLinesUpdateEvent({
        action: 'add',
        context: 'product',
        lines: [{ merchandiseId: String(variantId), quantity: 1 }],
        promise: deferred.promise,
      })
    );
    deferred.resolve({
      cart: CartLinesUpdateEvent.createCartFromAjaxResponse(cart),
      detail: { items: cart.items, source: 'nr-collection', itemCount: 1, didError: false },
    });
  } catch {
    /* theme without @shopify/events: the item is still in the cart */
  }
}

document.addEventListener('click', async (event) => {
  const button = event.target.closest('[data-nr-shop] [data-nr-quick-add]');
  if (!button || button.disabled) return;
  const card = button.closest('[data-nr-card]');
  const status = card?.querySelector('[data-nr-quick-add-status]');
  const label = button.getAttribute('aria-label') || '';
  button.disabled = true;
  if (status) status.textContent = '';
  try {
    const response = await fetch(`${cartRoot()}cart/add.js`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
      credentials: 'same-origin',
      body: JSON.stringify({ items: [{ id: Number(button.dataset.nrQuickAdd), quantity: 1 }] }),
    });
    const result = await response.json();
    if (!response.ok || result.status) throw new Error(result.description || 'add failed');
    button.classList.add('is-added');
    if (status) status.innerHTML = `I varukorgen. <a href="${cartRoot()}cart">Till varukorgen</a>`;
    publish('collection_quick_add', {
      collection: collectionHandle(),
      intent: activeIntent(),
      product: button.dataset.nrProduct || '',
      position: Number(button.dataset.position) || 0,
    });
    const cart = await fetch(`${cartRoot()}cart.js`, { headers: { Accept: 'application/json' } })
      .then((r) => (r.ok ? r.json() : null))
      .catch(() => null);
    if (cart) announceCartChange(button, button.dataset.nrQuickAdd, cart);
    setTimeout(() => {
      button.classList.remove('is-added');
      button.setAttribute('aria-label', label);
      button.disabled = false;
    }, 2400);
  } catch {
    button.disabled = false;
    if (status) status.textContent = 'Det gick inte att lägga till. Försök igen eller öppna produkten.';
  }
});

/* ---------- Analytics: view, product and kit clicks ---------- */
document.addEventListener('click', (event) => {
  const product = event.target.closest('[data-nr-shop-product]');
  if (product) {
    publish('collection_product_click', {
      collection: collectionHandle(),
      intent: activeIntent(),
      product: product.dataset.nrShopProduct,
      position: Number(product.dataset.position) || product.dataset.position || 0,
    });
  }
  const kit = event.target.closest('[data-nr-kit-click]');
  if (kit) {
    publish('collection_kit_click', { collection: collectionHandle(), product: kit.dataset.nrKitClick });
  }
});

if (collectionHandle()) {
  publish('collection_view', { collection: collectionHandle(), intent: activeIntent() });
  revealSelectedChip();
}

/* ---------- Färdiga paket: area tabs (hash in the URL) ---------- */
function initKitTabs() {
  const list = document.querySelector('[data-nr-kit-tabs]');
  if (!list) return;
  const tabs = [...list.querySelectorAll('[role="tab"]')];

  const select = (tab, { focus = false, updateHash = true } = {}) => {
    tabs.forEach((t) => {
      const on = t === tab;
      t.setAttribute('aria-selected', String(on));
      t.tabIndex = on ? 0 : -1;
      const panel = document.getElementById(t.getAttribute('aria-controls'));
      if (!panel) return;
      panel.hidden = !on;
      if (on && !reduceMotion) {
        panel.classList.remove('is-entering');
        void panel.offsetWidth;
        panel.classList.add('is-entering');
      }
    });
    if (focus) tab.focus();
    if (updateHash && tab.dataset.hash) history.replaceState(null, '', `#${tab.dataset.hash}`);
  };

  tabs.forEach((tab) =>
    tab.addEventListener('click', () => {
      select(tab);
      publish('collection_intent_select', { collection: collectionHandle(), intent: tab.textContent.trim() });
    })
  );

  list.addEventListener('keydown', (event) => {
    const i = tabs.indexOf(document.activeElement);
    if (i < 0) return;
    let next = null;
    if (event.key === 'ArrowRight') next = tabs[(i + 1) % tabs.length];
    if (event.key === 'ArrowLeft') next = tabs[(i - 1 + tabs.length) % tabs.length];
    if (event.key === 'Home') next = tabs[0];
    if (event.key === 'End') next = tabs[tabs.length - 1];
    if (!next) return;
    event.preventDefault();
    select(next, { focus: true });
  });

  const fromHash = () => {
    const hash = decodeURIComponent(window.location.hash.slice(1));
    const tab = tabs.find((t) => t.dataset.hash === hash);
    if (tab) select(tab, { updateHash: false });
  };
  fromHash();
  window.addEventListener('hashchange', fromHash);
}

initKitTabs();
