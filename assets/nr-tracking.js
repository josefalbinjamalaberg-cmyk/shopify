/*
  "Spåra din order" – frontend for sections/nr-order-tracking.liquid.

  Layers (kept separate so the real backend can be plugged in without
  touching the UI):
  1. Transport  – `request(path, payload)` → { status, data }.
                  Live: POST JSON to the app proxy (default /apps/nordic-tracking).
                  Test: nr-tracking-mock.js implements the same function with
                  test data. It is only imported when the section renders
                  data-mode="mock", which Liquid only allows on unpublished
                  themes and in the theme editor.
  2. Service    – turns an HTTP result into { ok, tracking } or { ok: false, error }.
  3. Normaliser – validates/cleans the tracking model (docs/tracking/README.md).
  4. View       – renders with textContent/DOM APIs only (never innerHTML with
                  data), so nothing the server returns can inject markup.

  No credentials of any kind live here. The e-mail address is only ever sent
  in a POST body, never in a URL.
*/

const REQUEST_TIMEOUT_MS = 15000;
const TIME_ZONE = 'Europe/Stockholm';
const LOCALE = 'sv-SE';

const COPY = {
  emptyOrder: 'Fyll i båda fälten för att fortsätta.',
  invalidEmail: 'Ange en giltig e-postadress.',
  emptyTracking: 'Ange ett spårningsnummer för att fortsätta.',
  orderNotFound: 'Vi kunde inte hitta en order med de uppgifterna. Kontrollera informationen och försök igen.',
  trackingNotFound:
    'Vi kunde inte hitta någon leverans med det spårningsnumret. Kontrollera numret och försök igen.',
  unavailable: 'Spårningen är tillfälligt otillgänglig. Försök igen om en stund.',
  rateLimited: 'För många försök. Vänta en stund och försök igen.',
  loading: 'Söker efter din leverans …',
  preparingHeading: 'Din order förbereds',
  preparingText:
    'Vi håller på att packa din beställning. Spårningen aktiveras så snart paketet har lämnat vårt lager.',
};

const STATUSES = {
  order_received: {
    step: 0,
    heading: 'Vi har tagit emot din beställning',
    text: 'Din order är registrerad och förbereds för leverans.',
  },
  packed: {
    step: 1,
    heading: 'Din order är packad',
    text: 'Paketet är packat och väntar på att lämnas över till DHL.',
  },
  in_transit: {
    step: 2,
    heading: 'Ditt paket är på väg',
    text: 'Paketet är på väg till dig.',
  },
  ready_for_pickup: {
    step: 3,
    heading: 'Redo att hämtas',
    text: 'Ditt paket har kommit fram till utlämningsstället och väntar på dig.',
  },
  delivered: {
    step: 3,
    heading: 'Levererad',
    text: 'Ditt paket har levererats.',
  },
};

/* ---------------------------------------------------------------- */
/* 1. Transport                                                      */
/* ---------------------------------------------------------------- */

function createHttpTransport(endpoint) {
  const base = endpoint.replace(/\/+$/, '');

  return async function request(path, payload, signal) {
    const response = await fetch(`${base}/${path}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
      body: JSON.stringify(payload),
      credentials: 'same-origin',
      cache: 'no-store',
      signal,
    });

    let data = null;
    const type = response.headers.get('Content-Type') || '';
    if (type.includes('application/json')) {
      try {
        data = await response.json();
      } catch {
        data = null;
      }
    }
    return { status: response.status, data };
  };
}

/* ---------------------------------------------------------------- */
/* 2. Service                                                        */
/* ---------------------------------------------------------------- */

function createService(request) {
  async function call(path, payload, source) {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), REQUEST_TIMEOUT_MS);

    try {
      const { status, data } = await request(path, payload, controller.signal);

      if (status === 200 && data && data.tracking) {
        const tracking = normalizeTracking(data.tracking, source);
        return tracking ? { ok: true, tracking } : { ok: false, error: 'unavailable' };
      }
      if (status === 429) return { ok: false, error: 'rate_limited' };
      // Only a JSON "not_found" from our own backend means "no match". An HTML
      // 404 (e.g. the app proxy isn't installed) is an outage, not a miss.
      if ((status === 404 || status === 400) && data && data.error === 'not_found') {
        return { ok: false, error: 'not_found' };
      }
      return { ok: false, error: 'unavailable' };
    } catch {
      return { ok: false, error: 'unavailable' };
    } finally {
      clearTimeout(timer);
    }
  }

  return {
    lookupOrder: (orderNumber, email) => call('order', { orderNumber, email }, 'shopify'),
    lookupTracking: (trackingNumber) => call('track', { trackingNumber }, 'tracking'),
  };
}

/* ---------------------------------------------------------------- */
/* 3. Normaliser                                                     */
/* ---------------------------------------------------------------- */

function text(value, max = 200) {
  if (typeof value !== 'string' && typeof value !== 'number') return '';
  return String(value).trim().slice(0, max);
}

function isoDate(value) {
  const string = text(value, 40);
  if (!string) return '';
  return Number.isNaN(Date.parse(string)) ? '' : string;
}

function safeImageUrl(value) {
  const string = text(value, 1000);
  if (!string) return '';
  try {
    const url = new URL(string, window.location.origin);
    return url.protocol === 'https:' || url.origin === window.location.origin ? url.href : '';
  } catch {
    return '';
  }
}

function normalizeEvent(event) {
  if (!event || typeof event !== 'object') return null;
  const description = text(event.description, 300);
  if (!description) return null;
  return {
    timestamp: isoDate(event.timestamp),
    location: text(event.location, 120),
    description,
  };
}

function normalizePickupPoint(point) {
  if (!point) return null;
  if (typeof point === 'string') return { name: text(point, 160), lines: [] };
  if (typeof point !== 'object') return null;
  const postal = [text(point.postalCode, 12), text(point.city, 80)].filter(Boolean).join(' ');
  const lines = [text(point.address, 160), postal].filter(Boolean);
  const name = text(point.name, 160);
  return name || lines.length ? { name, lines } : null;
}

/**
 * Cleans a tracking model coming from the backend (or the test data).
 * `expectedSource` is the flow that asked for it: a tracking-number lookup
 * can never produce order data, whatever the response contains.
 */
function normalizeTracking(raw, expectedSource) {
  if (!raw || typeof raw !== 'object') return null;

  const status = Object.hasOwn(STATUSES, raw.status) ? raw.status : null;
  if (!status) return null;

  const source = expectedSource === 'shopify' && raw.source === 'shopify' ? 'shopify' : 'tracking';

  const events = (Array.isArray(raw.events) ? raw.events : [])
    .slice(0, 50)
    .map(normalizeEvent)
    .filter(Boolean)
    .sort((a, b) => (Date.parse(b.timestamp) || 0) - (Date.parse(a.timestamp) || 0));

  const items =
    source === 'shopify' && Array.isArray(raw.items)
      ? raw.items
          .slice(0, 30)
          .map((item) =>
            item && typeof item === 'object' && text(item.title)
              ? {
                  title: text(item.title),
                  variantTitle: item.variantTitle === 'Default Title' ? '' : text(item.variantTitle),
                  quantity: Math.max(1, Math.min(999, parseInt(item.quantity, 10) || 1)),
                  image: safeImageUrl(item.image),
                }
              : null
          )
          .filter(Boolean)
      : [];

  return {
    source,
    orderNumber: source === 'shopify' ? text(raw.orderNumber, 32) : '',
    trackingNumber: text(raw.trackingNumber, 40),
    carrier: text(raw.carrier, 40) || 'DHL',
    service: text(raw.service, 80),
    status,
    statusLabel: text(raw.statusLabel, 80),
    estimatedDelivery: isoDate(raw.estimatedDelivery) || text(raw.estimatedDelivery, 60),
    lastUpdated: isoDate(raw.lastUpdated) || (events[0] && events[0].timestamp) || '',
    latestEvent: normalizeEvent(raw.latestEvent) || events[0] || null,
    pickupPoint: normalizePickupPoint(raw.pickupPoint),
    items,
    events,
  };
}

/* ---------------------------------------------------------------- */
/* 4. Formatting                                                     */
/* ---------------------------------------------------------------- */

const dateTimeParts = new Intl.DateTimeFormat(LOCALE, {
  timeZone: TIME_ZONE,
  day: 'numeric',
  month: 'long',
  hour: '2-digit',
  minute: '2-digit',
});

/** "26 september · 16:42" */
function formatDateTime(iso) {
  if (!iso) return '';
  const date = new Date(iso);
  if (Number.isNaN(date.getTime())) return '';
  const parts = Object.fromEntries(dateTimeParts.formatToParts(date).map((p) => [p.type, p.value]));
  return `${parts.day} ${parts.month} · ${parts.hour}:${parts.minute}`;
}

/** "måndag 29 september" – date-only values are calendar dates, not instants. */
function formatDate(value) {
  if (!value) return '';
  const dateOnly = /^\d{4}-\d{2}-\d{2}$/.test(value);
  const date = new Date(dateOnly ? `${value}T12:00:00Z` : value);
  if (Number.isNaN(date.getTime())) return value;
  return new Intl.DateTimeFormat(LOCALE, {
    timeZone: dateOnly ? 'UTC' : TIME_ZONE,
    weekday: 'long',
    day: 'numeric',
    month: 'long',
  }).format(date);
}

function formatOrderNumber(value) {
  if (!value) return '';
  return value.startsWith('#') ? value : `#${value}`;
}

/* ---------------------------------------------------------------- */
/* 5. View helpers                                                   */
/* ---------------------------------------------------------------- */

function el(tag, className, content) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (content !== undefined && content !== null && content !== '') node.textContent = content;
  return node;
}

function svgIcon(kind) {
  const ns = 'http://www.w3.org/2000/svg';
  const svg = document.createElementNS(ns, 'svg');
  svg.setAttribute('viewBox', '0 0 16 16');
  svg.setAttribute('aria-hidden', 'true');
  svg.setAttribute('focusable', 'false');
  const path = document.createElementNS(ns, 'path');
  if (kind === 'check') {
    path.setAttribute('d', 'M3.5 8.5l3 3 6-7');
    path.setAttribute('fill', 'none');
    path.setAttribute('stroke', 'currentColor');
    path.setAttribute('stroke-width', '1.8');
    path.setAttribute('stroke-linecap', 'round');
    path.setAttribute('stroke-linejoin', 'round');
  } else if (kind === 'arrow') {
    path.setAttribute('d', 'M4 12L12 4M6 4h6v6');
    path.setAttribute('fill', 'none');
    path.setAttribute('stroke', 'currentColor');
    path.setAttribute('stroke-width', '1.5');
    path.setAttribute('stroke-linecap', 'round');
    path.setAttribute('stroke-linejoin', 'round');
  }
  svg.append(path);
  return svg;
}

function dhlTrackingUrl(trackingNumber) {
  return `https://www.dhl.com/se-sv/home/tracking/tracking-parcel.html?submit=1&tracking-id=${encodeURIComponent(
    trackingNumber
  )}`;
}

/* ---------------------------------------------------------------- */
/* 6. Custom element                                                 */
/* ---------------------------------------------------------------- */

class NrOrderTracking extends HTMLElement {
  async connectedCallback() {
    if (this.initialised) return;
    this.initialised = true;

    this.search = this.querySelector('[data-track-search]');
    this.result = this.querySelector('[data-track-result]');
    this.announcer = this.querySelector('[data-track-announcer]');
    this.forms = {
      order: this.querySelector('[data-track-form="order"]'),
      tracking: this.querySelector('[data-track-form="tracking"]'),
    };

    // Listeners first, so a fast submit never falls back to a native form
    // post; the submit waits for the transport to be ready.
    for (const [kind, form] of Object.entries(this.forms)) {
      if (!form) continue;
      form.addEventListener('submit', (event) => {
        event.preventDefault();
        this.submit(kind);
      });
      form.addEventListener('input', (event) => {
        if (event.target.getAttribute('aria-invalid') === 'true') this.clearError(kind);
      });
    }

    this.mode = 'order';
    this.modeButtons = [...this.querySelectorAll('[data-track-mode]')];
    for (const button of this.modeButtons) {
      button.addEventListener('click', () => this.setMode(button.dataset.trackMode, true));
    }

    this.ready = this.createTransport().then((transport) => {
      this.service = createService(transport);
    });
  }

  async createTransport() {
    const mockSrc = this.dataset.mode === 'mock' ? this.dataset.mockSrc : '';
    if (mockSrc) {
      try {
        const mock = await import(mockSrc);
        const assetsNode = this.querySelector('[data-track-mock-assets]');
        let assets = {};
        try {
          assets = JSON.parse(assetsNode ? assetsNode.textContent : '{}') || {};
        } catch {
          assets = {};
        }
        this.renderDevPanel(mock.scenarios || []);
        return mock.createMockTransport({ assets });
      } catch (error) {
        console.warn('[nr-tracking] Testdata kunde inte laddas', error);
      }
    }
    return createHttpTransport(this.dataset.endpoint || '/apps/nordic-tracking');
  }

  /* ---------- Forms ---------- */

  /** Shows one of the two search forms (order number / tracking number). */
  setMode(kind, focus = false) {
    if (!this.forms[kind]) return;
    this.mode = kind;
    for (const [name, form] of Object.entries(this.forms)) {
      if (form) form.hidden = name !== kind;
    }
    for (const button of this.modeButtons) {
      button.setAttribute('aria-pressed', String(button.dataset.trackMode === kind));
    }
    if (focus) this.forms[kind].querySelector('input').focus();
  }

  field(kind, name) {
    return this.forms[kind].elements.namedItem(name);
  }

  showError(kind, message, invalidFields = []) {
    const form = this.forms[kind];
    const error = form.querySelector('[data-track-form-error]');
    error.textContent = message;
    error.hidden = false;

    const inputs = [...form.querySelectorAll('input')];
    for (const input of inputs) {
      const describedBy = (input.getAttribute('aria-describedby') || '').split(' ').filter(Boolean);
      if (!describedBy.includes(error.id)) describedBy.push(error.id);
      input.setAttribute('aria-describedby', describedBy.join(' '));
      input.setAttribute('aria-invalid', invalidFields.includes(input) ? 'true' : 'false');
    }
    (invalidFields[0] || inputs[0]).focus();
  }

  clearError(kind) {
    const form = this.forms[kind];
    const error = form.querySelector('[data-track-form-error]');
    error.textContent = '';
    error.hidden = true;
    for (const input of form.querySelectorAll('input')) {
      input.removeAttribute('aria-invalid');
      const describedBy = (input.getAttribute('aria-describedby') || '')
        .split(' ')
        .filter((id) => id && id !== error.id);
      input.setAttribute('aria-describedby', describedBy.join(' '));
    }
  }

  async submit(kind) {
    if (this.busy) return;
    this.clearError('order');
    this.clearError('tracking');

    let lookup;
    if (kind === 'order') {
      const orderInput = this.field('order', 'orderNumber');
      const emailInput = this.field('order', 'email');
      const orderNumber = orderInput.value.replace(/\s+/g, '');
      const email = emailInput.value.trim();

      const empty = [orderInput, emailInput].filter((input) => !input.value.trim());
      if (empty.length) return this.showError('order', COPY.emptyOrder, empty);
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        return this.showError('order', COPY.invalidEmail, [emailInput]);
      }
      lookup = () => this.service.lookupOrder(orderNumber, email);
    } else {
      const input = this.field('tracking', 'trackingNumber');
      const trackingNumber = input.value.replace(/\s+/g, '').toUpperCase();
      if (!trackingNumber) return this.showError('tracking', COPY.emptyTracking, [input]);
      lookup = () => this.service.lookupTracking(trackingNumber);
    }

    this.setBusy(true);
    await this.ready;
    const result = await lookup();
    this.setBusy(false);

    if (result.ok) {
      this.renderResult(result.tracking);
      return;
    }

    this.showSearch();
    const messages = {
      not_found: kind === 'order' ? COPY.orderNotFound : COPY.trackingNotFound,
      rate_limited: COPY.rateLimited,
      unavailable: COPY.unavailable,
    };
    this.showError(kind, messages[result.error] || COPY.unavailable);
  }

  setBusy(busy) {
    this.busy = busy;
    for (const form of Object.values(this.forms)) {
      const button = form.querySelector('[type="submit"]');
      button.disabled = busy;
    }
    if (busy) {
      this.search.hidden = true;
      this.result.hidden = false;
      this.result.setAttribute('aria-busy', 'true');
      this.result.replaceChildren(this.renderSkeleton());
      this.announce(COPY.loading);
    } else {
      this.result.removeAttribute('aria-busy');
    }
  }

  showSearch() {
    this.result.hidden = true;
    this.result.replaceChildren();
    this.search.hidden = false;
  }

  announce(message) {
    this.announcer.textContent = '';
    // A fresh text node is what makes screen readers re-announce.
    requestAnimationFrame(() => {
      this.announcer.textContent = message;
    });
  }

  scrollIntoViewIfNeeded(node) {
    const rect = node.getBoundingClientRect();
    const header = parseInt(getComputedStyle(document.documentElement).getPropertyValue('--header-height'), 10) || 80;
    if (rect.top < header || rect.top > window.innerHeight * 0.6) {
      const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      window.scrollTo({ top: window.scrollY + rect.top - header - 16, behavior: reduce ? 'auto' : 'smooth' });
    }
  }

  /* ---------- Dev panel (test mode only) ---------- */

  renderDevPanel(scenarios) {
    const container = this.querySelector('[data-track-dev-buttons]');
    if (!container) return;
    for (const scenario of scenarios) {
      const button = el('button', 'nr-track-dev__button', scenario.label);
      button.type = 'button';
      button.addEventListener('click', () => {
        this.showSearch();
        this.setMode(scenario.form);
        const form = this.forms[scenario.form];
        for (const [name, value] of Object.entries(scenario.values)) {
          form.elements.namedItem(name).value = value;
        }
        form.requestSubmit();
      });
      container.append(button);
    }
  }

  /* ---------- Rendering ---------- */

  renderSkeleton() {
    const wrap = el('div', 'nr-track-skeleton');
    wrap.setAttribute('aria-hidden', 'true');
    wrap.append(
      el('div', 'nr-track-skeleton__line nr-track-skeleton__line--eyebrow'),
      el('div', 'nr-track-skeleton__line nr-track-skeleton__line--title'),
      el('div', 'nr-track-skeleton__line nr-track-skeleton__line--text')
    );
    const steps = el('div', 'nr-track-skeleton__steps');
    for (let i = 0; i < 4; i += 1) steps.append(el('div', 'nr-track-skeleton__step'));
    wrap.append(steps, el('div', 'nr-track-skeleton__card'), el('div', 'nr-track-skeleton__card'));
    return wrap;
  }

  renderResult(tracking) {
    const status = STATUSES[tracking.status];
    const preparing = !tracking.trackingNumber && status.step <= 1;
    const heading = preparing ? COPY.preparingHeading : tracking.statusLabel || status.heading;
    const intro = preparing ? COPY.preparingText : status.text;

    const fragment = document.createDocumentFragment();

    /* Status card: numbers, heading, progress and the latest event */
    const summary = el('section', 'nr-track-summary');
    summary.setAttribute('aria-labelledby', 'NrTrackStatusHeading');

    const header = el('header', 'nr-track-status');
    const numbers = el('p', 'nr-track-status__numbers');
    if (tracking.orderNumber) {
      numbers.append(el('span', null, `Order ${formatOrderNumber(tracking.orderNumber)}`));
    }
    if (tracking.trackingNumber) {
      numbers.append(el('span', null, `Spårningsnummer ${tracking.trackingNumber}`));
    }
    if (numbers.childElementCount) header.append(numbers);

    const title = el('h2', 'nr-track-status__title', heading);
    title.id = 'NrTrackStatusHeading';
    title.tabIndex = -1;
    header.append(title, el('p', 'nr-track-status__text', intro));
    summary.append(header, this.renderProgress(tracking, status));

    const latest = tracking.latestEvent;
    if (latest || tracking.lastUpdated) {
      const row = el('div', 'nr-track-latest');
      const body = el('div', 'nr-track-latest__body');
      body.append(el('p', 'nr-track-latest__eyebrow', 'Senaste händelse'));
      if (latest) body.append(el('p', 'nr-track-latest__description', latest.description));
      const meta = el('p', 'nr-track-latest__meta');
      const when = formatDateTime((latest && latest.timestamp) || tracking.lastUpdated);
      if (when) meta.append(el('span', null, when));
      if (latest && latest.location) meta.append(el('span', null, latest.location));
      if (meta.childElementCount) body.append(meta);
      row.append(body);
      summary.append(row);
    }
    fragment.append(summary);

    /* Details card: delivery info, history and (verified lookups only) order contents */
    const details = el('div', 'nr-track-details');
    const info = this.renderInfo(tracking);
    if (info) details.append(info);
    if (tracking.events.length > 1) details.append(this.renderHistory(tracking.events));
    if (tracking.source === 'shopify' && tracking.items.length) {
      details.append(this.renderItems(tracking.items));
    }
    if (details.childElementCount) fragment.append(details);

    /* Actions: search again + carrier link */
    const actions = el('div', 'nr-track-actions');
    const again = el('button', 'nr-track-actions__again');
    again.type = 'button';
    again.append(el('span', null, '\u2190'), document.createTextNode(' Sök igen'));
    again.firstChild.setAttribute('aria-hidden', 'true');
    again.addEventListener('click', () => {
      this.showSearch();
      this.forms[this.mode].querySelector('input').focus();
    });
    actions.append(again);

    if (tracking.trackingNumber && /dhl/i.test(tracking.carrier)) {
      const link = el('a', 'nr-track-actions__carrier', 'Visa hos DHL');
      link.href = dhlTrackingUrl(tracking.trackingNumber);
      link.target = '_blank';
      link.rel = 'noopener noreferrer';
      link.append(el('span', 'visually-hidden', ' (öppnas i nytt fönster)'), svgIcon('arrow'));
      actions.append(link);
    }
    fragment.append(actions);

    this.result.replaceChildren(fragment);
    this.result.hidden = false;
    this.search.hidden = true;

    this.announce(`${heading}. ${intro}`);
    title.focus({ preventScroll: true });
    this.scrollIntoViewIfNeeded(this.result);
  }

  renderProgress(tracking, status) {
    const lastLabel =
      tracking.status === 'delivered'
        ? 'Levererad'
        : tracking.status === 'ready_for_pickup' || tracking.pickupPoint
        ? 'Redo att hämtas'
        : 'Levererad';
    const labels = ['Beställning mottagen', 'Packad', 'På väg', lastLabel];
    const current = status.step;
    const complete = tracking.status === 'delivered';

    const list = el('ol', 'nr-track-progress');
    list.setAttribute('aria-label', 'Leveransens förlopp');

    labels.forEach((label, index) => {
      let state = 'upcoming';
      if (index < current || (complete && index === current)) state = 'done';
      else if (index === current) state = 'active';

      const item = el('li', `nr-track-progress__step is-${state}`);
      if (state === 'active' || (complete && index === current)) item.setAttribute('aria-current', 'step');

      const marker = el('span', 'nr-track-progress__marker');
      marker.setAttribute('aria-hidden', 'true');
      if (state === 'done') marker.append(svgIcon('check'));
      else marker.append(el('span', 'nr-track-progress__dot'));

      const hidden = { done: 'Klart: ', active: 'Aktuellt steg: ', upcoming: 'Kommande: ' }[state];
      const labelNode = el('span', 'nr-track-progress__label');
      labelNode.append(el('span', 'visually-hidden', hidden), document.createTextNode(label));

      item.append(marker, labelNode);
      list.append(item);
    });
    return list;
  }

  renderBlock(className, headingText, headingId) {
    const section = el('section', `nr-track-block ${className}`);
    section.setAttribute('aria-labelledby', headingId);
    const heading = el('h3', 'nr-track-block__heading', headingText);
    heading.id = headingId;
    section.append(heading);
    return section;
  }

  renderInfo(tracking) {
    const rows = [];
    if (tracking.service) rows.push(['Fraktsätt', tracking.service]);
    if (tracking.estimatedDelivery && tracking.status !== 'delivered') {
      rows.push(['Beräknad leverans', formatDate(tracking.estimatedDelivery)]);
    }
    if (tracking.pickupPoint) rows.push(['Utlämningsställe', tracking.pickupPoint]);
    // The tracking number is already shown at the top of the status card.
    if (!rows.length) return null;

    const section = this.renderBlock('nr-track-info', 'Leverans', 'NrTrackInfoHeading');
    if (tracking.status === 'ready_for_pickup') section.classList.add('nr-track-info--highlight');

    const list = el('dl', 'nr-track-info__list');
    for (const [label, value] of rows) {
      const row = el('div', 'nr-track-info__row');
      row.append(el('dt', null, label));
      const dd = el('dd');
      if (typeof value === 'string') {
        dd.textContent = value;
      } else {
        if (value.name) dd.append(el('span', 'nr-track-info__strong', value.name));
        for (const line of value.lines) dd.append(el('span', null, line));
      }
      row.append(dd);
      list.append(row);
    }
    section.append(list);
    return section;
  }

  renderHistory(events) {
    const VISIBLE = 3;
    const section = this.renderBlock('nr-track-history', 'Leveranshistorik', 'NrTrackHistoryHeading');

    const list = el('ol', 'nr-track-timeline');
    list.id = 'NrTrackTimeline';
    events.forEach((event, index) => {
      const item = el('li', 'nr-track-timeline__item');
      if (index >= VISIBLE) item.hidden = true;
      const when = formatDateTime(event.timestamp);
      if (when) {
        const time = el('time', 'nr-track-timeline__time', when);
        time.dateTime = event.timestamp;
        item.append(time);
      }
      item.append(el('p', 'nr-track-timeline__description', event.description));
      if (event.location) item.append(el('p', 'nr-track-timeline__location', event.location));
      list.append(item);
    });
    section.append(list);

    if (events.length > VISIBLE) {
      const toggle = el('button', 'nr-track-timeline__toggle', `Visa alla ${events.length} händelser`);
      toggle.type = 'button';
      toggle.setAttribute('aria-expanded', 'false');
      toggle.setAttribute('aria-controls', list.id);
      toggle.addEventListener('click', () => {
        const expand = toggle.getAttribute('aria-expanded') !== 'true';
        [...list.children].forEach((item, index) => {
          if (index >= VISIBLE) item.hidden = !expand;
        });
        toggle.setAttribute('aria-expanded', String(expand));
        toggle.textContent = expand ? 'Visa färre' : `Visa alla ${events.length} händelser`;
      });
      section.append(toggle);
    }
    return section;
  }

  renderItems(items) {
    const section = this.renderBlock('nr-track-items', 'Din beställning', 'NrTrackItemsHeading');

    const list = el('ul', 'nr-track-items__list');
    list.setAttribute('role', 'list');
    for (const item of items) {
      const row = el('li', 'nr-track-items__item');
      const media = el('span', 'nr-track-items__media');
      if (item.image) {
        const img = document.createElement('img');
        img.src = item.image;
        img.alt = '';
        img.width = 64;
        img.height = 64;
        img.loading = 'lazy';
        img.decoding = 'async';
        media.append(img);
      }
      const body = el('span', 'nr-track-items__body');
      body.append(el('span', 'nr-track-items__title', item.title));
      if (item.variantTitle) body.append(el('span', 'nr-track-items__variant', item.variantTitle));
      const qty = el('span', 'nr-track-items__qty', `${item.quantity} st`);
      qty.setAttribute('aria-label', `Antal: ${item.quantity}`);
      row.append(media, body, qty);
      list.append(row);
    }
    section.append(list);
    return section;
  }
}

if (!customElements.get('nr-order-tracking')) {
  customElements.define('nr-order-tracking', NrOrderTracking);
}

export { normalizeTracking };
