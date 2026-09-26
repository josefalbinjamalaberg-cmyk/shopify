/*
  REFERENCE ONLY – server-side code, never part of the theme.

  Turns a DHL Shipment Tracking – Unified API response into the tracking
  model the page expects (see README.md). Field names follow DHL's public
  documentation for GET https://api-eu.dhl.com/track/shipments; verify them
  against real responses once API access is approved.

  The API key (DHL-API-Key header) lives in the server's environment only.
*/

const STATUS_BY_CODE = {
  'pre-transit': 'packed',
  transit: 'in_transit',
  delivered: 'delivered',
  failure: 'in_transit',
  unknown: 'in_transit',
};

// DHL descriptions are often English; map the ones we see to Swedish copy.
// Extend this list from real data. Unmapped texts fall back to a neutral line.
const DESCRIPTIONS_SV = [
  [/ready for (pick ?up|collection)|available for pick ?up/i, 'Paketet har kommit fram till utlämningsstället'],
  [/delivered|picked up by (the )?recipient/i, 'Paketet har levererats'],
  [/out for delivery/i, 'Paketet är ute för leverans'],
  [/arrived at .*(terminal|facility|hub)|processed at/i, 'Paketet har sorterats på terminal'],
  [/departed|in transit|on its way/i, 'Paketet är på väg'],
  [/received|picked up|accepted/i, 'Paketet har lämnats till DHL'],
  [/electronic(ally)? (notified|announced)|shipment information received/i, 'DHL har fått information om paketet'],
];

function toSwedish(description) {
  const text = String(description || '');
  for (const [pattern, sv] of DESCRIPTIONS_SV) if (pattern.test(text)) return sv;
  return text ? 'Ny händelse i leveransen' : '';
}

function locality(location) {
  const address = location && location.address;
  return (address && (address.addressLocality || address.postalCode)) || '';
}

function isReadyForPickup(shipment) {
  const latest = shipment.status || {};
  return /ready for (pick ?up|collection)|available for pick ?up/i.test(
    `${latest.status || ''} ${latest.description || ''}`
  );
}

/**
 * @param {object} dhlResponse  Parsed JSON from DHL.
 * @param {object} [order]      Only for the verified order flow:
 *                              { orderNumber, items: [{ title, variantTitle, quantity, image }] }
 */
export function normalizeDhl(dhlResponse, order) {
  const shipment = dhlResponse && Array.isArray(dhlResponse.shipments) ? dhlResponse.shipments[0] : null;
  if (!shipment) return null;

  const code = shipment.status && shipment.status.statusCode;
  let status = STATUS_BY_CODE[code] || 'in_transit';
  if (status !== 'delivered' && isReadyForPickup(shipment)) status = 'ready_for_pickup';

  const events = (shipment.events || []).map((event) => ({
    timestamp: event.timestamp,
    location: locality(event.location),
    description: toSwedish(event.description || event.status),
  }));

  const pickup = shipment.details && shipment.details.receiver && shipment.details.receiver.servicePoint;

  const model = {
    source: order ? 'shopify' : 'tracking',
    trackingNumber: shipment.id,
    carrier: 'DHL',
    service: (shipment.details && shipment.details.product && shipment.details.product.productName) || '',
    status,
    statusLabel: '',
    estimatedDelivery: shipment.estimatedTimeOfDelivery || '',
    lastUpdated: (shipment.status && shipment.status.timestamp) || (events[0] && events[0].timestamp) || '',
    latestEvent: events[0] || null,
    pickupPoint: pickup
      ? {
          name: pickup.name || '',
          address: (pickup.address && pickup.address.streetAddress) || '',
          postalCode: (pickup.address && pickup.address.postalCode) || '',
          city: (pickup.address && pickup.address.addressLocality) || '',
        }
      : null,
    events,
  };

  // Order data only for the verified order-number + e-mail flow.
  if (order) {
    model.orderNumber = order.orderNumber;
    model.items = order.items;
  }
  return model;
}
