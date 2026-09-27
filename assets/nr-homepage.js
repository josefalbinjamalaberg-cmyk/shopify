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

  /* ---------- Hero video: pause when off-screen, respect reduced motion ---------- */
  function initHeroVideo() {
    initAll('[data-nr-hero-video]', (video) => {
      if (prefersReducedMotion) {
        video.removeAttribute('autoplay');
        video.pause();
        return;
      }

      if (!('IntersectionObserver' in window)) return;

      const observer = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              video.play().catch(() => {});
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
    initHeroVideo();
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
