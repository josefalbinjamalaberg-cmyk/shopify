/*
  NordicReflection – standard product page system (lightweight, no dependencies).

  1. Analytics: elements with data-nr-event publish a custom event through
     Shopify's customer-events API (Shopify.analytics.publish), so any
     pixel (GA4, Meta, TikTok…) can subscribe without a second tracking
     implementation. Standard events (product_viewed, product_added_to_cart)
     are already sent by Shopify and are NOT duplicated here.
     Custom events: kit_upgrade_click, cross_sell_click, trustpilot_click,
     video_play, gallery_interaction, sticky_atc_click.
  2. Subtle section entrance (opacity + 12px, ~320 ms), only when the user
     hasn't asked for reduced motion and only for sections below the fold.
*/

const publish = (name, detail = {}) => {
  try {
    window.Shopify?.analytics?.publish?.(`nr_${name}`, detail);
  } catch {
    /* analytics must never break the page */
  }
};

const productHandle = document.querySelector('[data-nr-pdp-product]')?.dataset.nrPdpProduct || '';

document.addEventListener('click', (event) => {
  const tracked = event.target.closest('[data-nr-event]');
  if (tracked) {
    publish(tracked.dataset.nrEvent, {
      product: productHandle,
      target: tracked.dataset.nrProduct || '',
      source: tracked.dataset.nrSource || '',
    });
  }
  if (event.target.closest('.sticky-add-to-cart__button')) {
    publish('sticky_atc_click', { product: productHandle });
  }
});

document.addEventListener(
  'play',
  (event) => {
    if (event.target instanceof HTMLVideoElement && event.target.closest('.nr-pdp-demo')) {
      publish('video_play', { product: productHandle, source: 'demo' });
    }
  },
  true
);

let galleryTracked = false;
const gallery = document.querySelector('media-gallery, .product-media-gallery, [data-media-gallery]');
gallery?.addEventListener(
  'pointerdown',
  () => {
    if (galleryTracked) return;
    galleryTracked = true;
    publish('gallery_interaction', { product: productHandle });
  },
  { passive: true }
);

if (window.matchMedia('(prefers-reduced-motion: no-preference)').matches && 'IntersectionObserver' in window) {
  const sections = [...document.querySelectorAll('.nr-pdp-section')].filter(
    (section) => section.getBoundingClientRect().top > window.innerHeight
  );
  const observer = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        entry.target.classList.add('is-revealed');
        entry.target.classList.remove('is-revealing');
        observer.unobserve(entry.target);
      }
    },
    { rootMargin: '0px 0px -10% 0px' }
  );
  for (const section of sections) {
    section.classList.add('is-revealing');
    observer.observe(section);
  }
}
