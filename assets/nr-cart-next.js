/*
  NordicReflection – "Lägg till" for the cart suggestions (snippets/nr-cart-next-step).

  Uses the same path as Horizon's product form: POST /cart/add with the
  cart-items sections, then a CartLinesUpdateEvent carrying the rendered
  sections, so cart-items-component morphs the drawer / cart page and the
  suggestion disappears (or the next one shows) from server-rendered Liquid.

  - One request per button: the button is disabled + aria-busy while it runs,
    repeated clicks are ignored.
  - Exactly the variant and quantity 1 rendered in data-variant-id.
  - On error the cart is left untouched and the message is announced.
  - Custom analytics events via Shopify.analytics.publish (nr_cart_rec_add,
    nr_cart_rec_click); Shopify's own product_added_to_cart is not duplicated.
*/
import { CartLinesUpdateEvent, CartErrorEvent } from '@shopify/events';

const publish = (name, detail) => {
  try {
    window.Shopify?.analytics?.publish?.(`nr_${name}`, detail);
  } catch {
    /* analytics must never break the cart */
  }
};

const sectionIds = () =>
  Array.from(document.querySelectorAll('cart-items-component'))
    .map((element) => element instanceof HTMLElement && element.dataset.sectionId)
    .filter(Boolean)
    .join(',');

const announce = (button, text) => {
  const status = button.closest('.nr-cart-next')?.querySelector('.nr-cart-next__status');
  if (status) status.textContent = text;
};

async function add(button) {
  if (button.disabled || button.getAttribute('aria-busy') === 'true') return;

  const variantId = Number(button.dataset.variantId);
  if (!variantId) return;

  const label = button.textContent;
  button.disabled = true;
  button.setAttribute('aria-busy', 'true');
  button.textContent = 'Lägger till…';

  const deferred = CartLinesUpdateEvent.createPromise();
  button.dispatchEvent(
    new CartLinesUpdateEvent({
      action: 'add',
      context: 'product',
      lines: [{ merchandiseId: String(variantId), quantity: 1 }],
      promise: deferred.promise,
    })
  );

  try {
    const response = await fetch(window.Theme.routes.cart_add_url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
      body: JSON.stringify({ items: [{ id: variantId, quantity: 1 }], sections: sectionIds() }),
    });
    const result = await response.json();
    const cart = await fetch(`${window.Theme.routes.cart_url}.js`, {
      headers: { Accept: 'application/json' },
    }).then((r) => r.json());

    if (result.status) {
      button.dispatchEvent(new CartErrorEvent({ error: result.message || 'Add to cart failed', code: 'INVALID' }));
      deferred.resolve({
        cart: CartLinesUpdateEvent.createCartFromAjaxResponse(cart),
        detail: { didError: true, items: cart.items, source: 'nr-cart-next' },
      });
      announce(button, result.description || result.message || 'Det gick inte att lägga till produkten.');
      button.disabled = false;
      button.removeAttribute('aria-busy');
      button.textContent = label;
      return;
    }

    publish('cart_rec_add', { target: button.dataset.nrProduct || '' });
    announce(button, 'Tillagd i varukorgen.');
    // The re-rendered section replaces this card; no need to reset the button.
    deferred.resolve({
      cart: CartLinesUpdateEvent.createCartFromAjaxResponse(cart),
      detail: { didError: false, items: cart.items, sections: result.sections, source: 'nr-cart-next' },
    });
  } catch (error) {
    deferred.reject(error);
    announce(button, 'Det gick inte att lägga till produkten. Försök igen.');
    button.disabled = false;
    button.removeAttribute('aria-busy');
    button.textContent = label;
  }
}

if (!window.nrCartNextReady) {
  window.nrCartNextReady = true;

  document.addEventListener('click', (event) => {
    const target = event.target instanceof Element ? event.target : null;
    const button = target?.closest('[data-nr-cart-rec-add]');
    if (button instanceof HTMLButtonElement) {
      event.preventDefault();
      add(button);
      return;
    }
    const link = target?.closest('[data-nr-cart-rec-click]');
    if (link instanceof HTMLElement) {
      publish('cart_rec_click', { target: link.dataset.nrProduct || '' });
    }
  });
}
