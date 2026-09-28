/*
  NordicReflection – collection pages (progressive enhancement, no dependencies).

  1. Chips, active-filter pills and "Rensa" are plain links to Shopify's native
     filter URLs – they work without JS. Here they are upgraded to Horizon's own
     in-place update (facets-form-component.updateFiltersByURL → section
     rendering), so the grid, count and chips refresh without a full reload.
  2. Browser back/forward: Horizon pushes filter URLs but does not listen for
     popstate, so the section is re-rendered from the restored URL.
  3. Analytics through Shopify.analytics.publish (customer events), prefixed
     nr_ like the PDP events: collection_view, collection_filter_select,
     collection_filter_clear, collection_sort, collection_product_click,
     collection_quick_add. Standard Shopify events are not duplicated.
*/
import { sectionRenderer } from '@theme/section-renderer';

const ROOT = '[data-nr-collection]';

const publish = (name, detail = {}) => {
  try {
    window.Shopify?.analytics?.publish?.(`nr_${name}`, detail);
  } catch {
    /* analytics must never break the page */
  }
};

const rootOf = (el) => el?.closest?.(ROOT) || document.querySelector(ROOT);
const collectionOf = (el) => rootOf(el)?.dataset.nrCollection || '';

document.addEventListener('click', (event) => {
  const target = event.target instanceof Element ? event.target : null;
  if (!target) return;

  // --- 1. Filter links (chips, pills, clear) ---
  const link = target.closest('[data-nr-filter-link]');
  if (link && rootOf(link)) {
    const collection = collectionOf(link);
    if ('nrClear' in link.dataset || link.dataset.nrValue === 'all') {
      publish('collection_filter_clear', { collection, filter: link.dataset.nrFilter || 'all' });
    } else if ('nrRemove' in link.dataset || link.getAttribute('aria-current') === 'true') {
      publish('collection_filter_clear', { collection, filter: link.dataset.nrFilter, value: link.dataset.nrValue });
    } else {
      publish('collection_filter_select', { collection, filter: link.dataset.nrFilter, value: link.dataset.nrValue });
    }

    if (event.metaKey || event.ctrlKey || event.shiftKey || event.button === 1) return;
    const section = link.closest('.shopify-section');
    const form = section?.querySelector('facets-form-component');
    if (form && typeof form.updateFiltersByURL === 'function') {
      event.preventDefault();
      form.updateFiltersByURL(link.href);
    }
    return;
  }

  // --- 3. Product click / quick add ---
  const item = target.closest(`${ROOT} [data-nr-product]`);
  if (!item) return;
  const product = item.dataset.nrProduct;
  const collection = collectionOf(item);
  if (target.closest('.quick-add__button, .add-to-cart-button')) {
    publish('collection_quick_add', {
      collection,
      product,
      mode: target.closest('.quick-add__button--choose') ? 'choose' : 'add',
    });
  } else if (target.closest('a[href]')) {
    publish('collection_product_click', { collection, product });
  }
});

// Sorting (Horizon renders radios / a select named sort_by)
document.addEventListener('change', (event) => {
  const input = event.target;
  if (!(input instanceof HTMLInputElement || input instanceof HTMLSelectElement)) return;
  if (input.name !== 'sort_by' || !rootOf(input)?.contains(input)) return;
  publish('collection_sort', { collection: collectionOf(input), sort: input.value });
});

// --- 2. Back / forward restores the filtered state ---
window.addEventListener('popstate', () => {
  const root = document.querySelector(ROOT);
  const sectionId = root?.getAttribute('section-id');
  if (!sectionId) return;
  sectionRenderer.renderSection(sectionId, { cache: true }).catch(() => window.location.reload());
});

// Mobile chip row scrolls sideways: keep the selected chip in view (on load and after each re-render)
const revealActiveChip = () => {
  const row = document.querySelector(`${ROOT} .nr-coll-chips`);
  const active = row?.querySelector('[aria-current="true"]');
  if (!row || !active || row.scrollWidth <= row.clientWidth) return;
  const li = active.parentElement;
  row.scrollLeft = Math.max(0, li.offsetLeft - row.offsetLeft - 16);
};

const root = document.querySelector(ROOT);
if (root) {
  revealActiveChip();
  const section = root.closest('.shopify-section') || root;
  let queued = false;
  new MutationObserver(() => {
    if (queued) return;
    queued = true;
    requestAnimationFrame(() => {
      queued = false;
      revealActiveChip();
    });
  }).observe(section, { childList: true, subtree: true, attributes: true, attributeFilter: ['aria-current'] });

  const params = new URLSearchParams(window.location.search);
  const filters = [...params.keys()].filter((key) => key.startsWith('filter.'));
  publish('collection_view', {
    collection: root.dataset.nrCollection,
    filters: filters.map((key) => `${key}=${params.getAll(key).join('|')}`),
    sort: params.get('sort_by') || 'default',
  });
}
