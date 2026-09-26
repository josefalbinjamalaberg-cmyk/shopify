/*
  TEST DATA for "Spåra din order" – never used by the live theme.

  Imported by nr-tracking.js only when the section renders data-mode="mock",
  which Liquid only allows on unpublished themes and in the theme editor.

  It implements the same transport as the real backend —
  request(path, payload) → { status, data } — so the page runs exactly the
  code paths it will run against /apps/nordic-tracking: 200 with a tracking
  model, 404 { error: "not_found" }, 429 and 503.

  The rules mirror what the backend must do:
  - Order lookup needs the right order number AND e-mail (case-insensitive).
    A wrong e-mail answers exactly like an unknown order number.
  - Tracking-number lookup never returns order number or products.

  All test orders use the e-mail test@nordicreflection.se.
*/

const TEST_EMAIL = 'test@nordicreflection.se';
const HOUR = 60 * 60 * 1000;

function ago(hours) {
  return new Date(Date.now() - hours * HOUR).toISOString();
}

function inDays(days) {
  const date = new Date(Date.now() + days * 24 * HOUR);
  return date.toISOString().slice(0, 10);
}

function wait(ms, signal) {
  return new Promise((resolve, reject) => {
    const timer = setTimeout(resolve, ms);
    if (signal) {
      signal.addEventListener('abort', () => {
        clearTimeout(timer);
        reject(new DOMException('Aborted', 'AbortError'));
      });
    }
  });
}

function item(asset, fallbackTitle, quantity) {
  const variant = asset && asset.variant && asset.variant !== 'Default Title' ? asset.variant : '';
  return {
    title: (asset && asset.title) || fallbackTitle,
    variantTitle: variant,
    quantity,
    image: (asset && asset.image) || '',
  };
}

const PICKUP_POINT = {
  name: 'DHL Service Point – Pressbyrån Stockholm Centralstation, entréplan vid spår 10',
  address: 'Centralplan 15',
  postalCode: '111 20',
  city: 'Stockholm',
};

/* Events, newest last here – the page sorts them. */
const EVENTS = {
  received: () => ({ timestamp: ago(52), location: 'NordicReflection', description: 'Beställningen har tagits emot' }),
  packed: () => ({ timestamp: ago(30), location: 'NordicReflection, lager', description: 'Paketet är packat' }),
  handedOver: () => ({ timestamp: ago(26), location: 'Stockholm', description: 'Paketet har lämnats till DHL' }),
  terminal: () => ({ timestamp: ago(14), location: 'Jönköping terminal', description: 'Paketet har sorterats på terminal' }),
  onWay: () => ({ timestamp: ago(5), location: 'Stockholm terminal', description: 'Paketet är på väg till utlämningsstället' }),
  arrived: () => ({ timestamp: ago(2), location: 'Stockholm', description: 'Paketet har kommit fram till utlämningsstället' }),
  delivered: () => ({ timestamp: ago(1), location: 'Stockholm', description: 'Paketet har hämtats ut' }),
};

function build(key, assets) {
  const items = [
    item(assets.foamtastic, 'Foamtastic', 1),
    item(assets.alkastrike, 'Alkastrike', 1),
    item(assets.pure, 'Pure Shampoo', 2),
  ];
  const base = { carrier: 'DHL', service: 'DHL Service Point', items };

  switch (key) {
    case 'order_received':
      return { ...base, orderNumber: '#1001', trackingNumber: '', status: 'order_received', service: '', events: [EVENTS.received()] };
    case 'preparing':
      return { ...base, orderNumber: '#1010', trackingNumber: '', status: 'packed', service: '', events: [EVENTS.received(), EVENTS.packed()] };
    case 'packed':
      return {
        ...base,
        orderNumber: '#1002',
        trackingNumber: '1000000002',
        status: 'packed',
        estimatedDelivery: inDays(3),
        events: [EVENTS.received(), EVENTS.packed()],
      };
    case 'in_transit':
      return {
        ...base,
        orderNumber: '#1003',
        trackingNumber: '1234567890',
        status: 'in_transit',
        estimatedDelivery: inDays(1),
        pickupPoint: PICKUP_POINT,
        events: [EVENTS.received(), EVENTS.packed(), EVENTS.handedOver(), EVENTS.terminal(), EVENTS.onWay()],
      };
    case 'ready_for_pickup':
      return {
        ...base,
        orderNumber: '#1004',
        trackingNumber: '1000000004',
        status: 'ready_for_pickup',
        pickupPoint: PICKUP_POINT,
        events: [EVENTS.received(), EVENTS.packed(), EVENTS.handedOver(), EVENTS.terminal(), EVENTS.onWay(), EVENTS.arrived()],
      };
    case 'delivered':
      return {
        ...base,
        orderNumber: '#1005',
        trackingNumber: '1000000005',
        status: 'delivered',
        pickupPoint: PICKUP_POINT,
        events: [
          EVENTS.received(),
          EVENTS.packed(),
          EVENTS.handedOver(),
          EVENTS.terminal(),
          EVENTS.onWay(),
          EVENTS.arrived(),
          EVENTS.delivered(),
        ],
      };
    default:
      return null;
  }
}

/* What each test value does. `delay` simulates network time. */
const ORDERS = {
  1001: { scenario: 'order_received' },
  1002: { scenario: 'packed' },
  1003: { scenario: 'in_transit' },
  1004: { scenario: 'ready_for_pickup' },
  1005: { scenario: 'delivered' },
  1006: { scenario: 'in_transit', delay: 6000 },
  1008: { error: 503 },
  1009: { error: 429 },
  1010: { scenario: 'preparing' },
};

const TRACKING = {
  1000000002: { scenario: 'packed' },
  1234567890: { scenario: 'in_transit' },
  1000000004: { scenario: 'ready_for_pickup' },
  1000000005: { scenario: 'delivered' },
  1000000006: { scenario: 'in_transit', delay: 6000 },
  1000000008: { error: 503 },
  1000000009: { error: 429 },
};

function withoutOrderData(tracking) {
  const { items, orderNumber, ...rest } = tracking;
  return { ...rest, source: 'tracking' };
}

export function createMockTransport({ assets = {} } = {}) {
  return async function request(path, payload, signal) {
    let rule;
    let tracking = null;

    if (path === 'order') {
      const number = String(payload.orderNumber || '').replace(/^#/, '');
      const emailMatches = String(payload.email || '').trim().toLowerCase() === TEST_EMAIL;
      // Unknown order and wrong e-mail are indistinguishable on purpose.
      rule = emailMatches ? ORDERS[number] : undefined;
      if (rule && rule.scenario) tracking = { ...build(rule.scenario, assets), source: 'shopify' };
    } else if (path === 'track') {
      rule = TRACKING[String(payload.trackingNumber || '')];
      if (rule && rule.scenario) tracking = withoutOrderData(build(rule.scenario, assets));
    }

    await wait((rule && rule.delay) || 700, signal);

    if (rule && rule.error === 429) return { status: 429, data: { error: 'rate_limited' } };
    if (rule && rule.error === 503) return { status: 503, data: { error: 'unavailable' } };
    if (!tracking) return { status: 404, data: { error: 'not_found' } };
    return { status: 200, data: { tracking } };
  };
}

/* Buttons in the test panel. */
export const scenarios = [
  { label: 'Beställning mottagen', form: 'order', values: { orderNumber: '#1001', email: TEST_EMAIL } },
  { label: 'Förbereds (inget spårningsnr)', form: 'order', values: { orderNumber: '#1010', email: TEST_EMAIL } },
  { label: 'Packad', form: 'order', values: { orderNumber: '#1002', email: TEST_EMAIL } },
  { label: 'På väg', form: 'order', values: { orderNumber: '#1003', email: TEST_EMAIL } },
  { label: 'Redo att hämtas', form: 'order', values: { orderNumber: '#1004', email: TEST_EMAIL } },
  { label: 'Levererad', form: 'order', values: { orderNumber: '#1005', email: TEST_EMAIL } },
  { label: 'Laddar (långsam)', form: 'order', values: { orderNumber: '#1006', email: TEST_EMAIL } },
  { label: 'Fel e-post', form: 'order', values: { orderNumber: '#1003', email: 'fel@exempel.se' } },
  { label: 'Tillfälligt fel', form: 'order', values: { orderNumber: '#1008', email: TEST_EMAIL } },
  { label: 'För många försök', form: 'order', values: { orderNumber: '#1009', email: TEST_EMAIL } },
  { label: 'Spårningsnr: på väg', form: 'tracking', values: { trackingNumber: '1234567890' } },
  { label: 'Spårningsnr: saknas', form: 'tracking', values: { trackingNumber: '9999999999' } },
];
