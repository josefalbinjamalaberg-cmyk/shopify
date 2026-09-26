# Spåra din order – backend-kontrakt

Temat (sidan `/pages/spara-din-order`) är klart och körs i dag på testdata.
Det här dokumentet beskriver vad servern bakom `/apps/nordic-tracking` måste
göra för att sidan ska fungera med riktig data – utan att temat byggs om.

## Filer i temat

| Fil | Roll |
| --- | --- |
| `sections/nr-order-tracking.liquid` | Sidans markup, formulär, texter (redigerbara i temaredigeraren) |
| `assets/nr-tracking.js` | Validering, POST-anrop, statushantering, rendering |
| `assets/nr-tracking-mock.js` | Testdata. Laddas bara i opublicerat tema/temaredigeraren |
| `assets/nr-tracking.css` | Utseende |
| `templates/page.spara-din-order.json` | Sidmall |

Inga nycklar eller hemligheter finns i temat. All kommunikation med Shopify
Admin API och DHL sker på servern.

## Testläge vs. riktig spårning

Sektionens inställning **Datakälla** (`data_source`):

- `live` – POST till `endpoint_base` (standard `/apps/nordic-tracking`).
- `mock` – testdata, men **bara** när sidan renderas av ett opublicerat tema
  eller i temaredigeraren (`theme.role` / `request.design_mode`). I publicerat
  tema ignoreras `mock` helt: testpanelen renderas inte och
  `nr-tracking-mock.js` laddas aldrig.

Innan publicering: sätt Datakälla till `live` i mallen ändå, så att det är
tydligt i admin.

## Endpoints

Båda ska ligga bakom en **Shopify App Proxy** (`/apps/nordic-tracking/*`) så att
anropen går till butikens egen domän och Shopify signerar dem (`signature`
query-parametern ska verifieras på servern).

### `POST /apps/nordic-tracking/order`

```json
{ "orderNumber": "#1047", "email": "namn@email.se" }
```

Servern ska:

1. Rate-limita (se nedan) **innan** något slås upp.
2. Normalisera ordernumret (ta bort `#` och blanksteg) och slå upp ordern via
   Admin GraphQL: `orders(first: 1, query: "name:#1047")`.
3. Jämföra e-post **skiftlägesokänsligt** och i konstant tid
   (`crypto.timingSafeEqual` på normaliserade värden/hashar) mot `order.email`
   (och ev. `customer.email`).
4. Om ordern inte finns **eller** e-posten inte matchar: svara exakt likadant –
   `404 {"error":"not_found"}` – med samma ungefärliga svarstid. Avslöja aldrig
   att ett ordernummer finns.
5. Vid match: läsa fulfillments (`trackingInfo { number company url }`), hämta
   DHL-status för spårningsnumret, normalisera (se modell) och returnera
   `200 {"tracking": {...}}` med `source: "shopify"`.
6. Returnera bara det som behövs: ordernummer, status, händelser,
   utlämningsställe och produkter (titel, variant, antal, bild-URL). **Aldrig**
   namn, adress, telefon, e-post, pris, betalning eller kund-id.

Rimliga regler: visa inte arkiverade/avbrutna ordrar (svara `not_found`),
begränsa till ordrar yngre än t.ex. 6 månader.

### `POST /apps/nordic-tracking/track`

```json
{ "trackingNumber": "1234567890" }
```

- Slå **bara** upp hos DHL. Koppla aldrig spårningsnumret till en Shopify-order
  i svaret.
- Svaret ska ha `source: "tracking"` och får inte innehålla `orderNumber` eller
  `items`. (Frontend rensar dem även om de skulle komma med.)
- Okänt nummer: `404 {"error":"not_found"}`.

### Svarskoder som frontend hanterar

| Kod | Body | Visas för kunden |
| --- | --- | --- |
| 200 | `{"tracking": {...}}` | Resultat |
| 404 / 400 | `{"error":"not_found"}` (JSON) | "Vi kunde inte hitta …" |
| 429 | valfri | "För många försök. Vänta en stund och försök igen." |
| övrigt, HTML-svar, timeout (15 s), nätverksfel | – | "Spårningen är tillfälligt otillgänglig …" |

Obs: en 404 **utan** JSON (t.ex. om app-proxyn inte är installerad) tolkas som
"tillfälligt otillgänglig", inte som "hittades inte".

## Normaliserad modell (det enda frontend tar emot)

```json
{
  "source": "shopify",
  "orderNumber": "#1047",
  "trackingNumber": "1234567890",
  "carrier": "DHL",
  "service": "DHL Service Point",
  "status": "in_transit",
  "statusLabel": "",
  "estimatedDelivery": "2026-09-29",
  "lastUpdated": "2026-09-26T14:42:00Z",
  "latestEvent": { "timestamp": "…", "location": "Stockholm", "description": "Paketet är på väg" },
  "pickupPoint": { "name": "…", "address": "…", "postalCode": "111 20", "city": "Stockholm" },
  "items": [{ "title": "…", "variantTitle": "500 ml", "quantity": 1, "image": "https://cdn.shopify.com/…" }],
  "events": [{ "timestamp": "2026-09-26T14:42:00Z", "location": "Stockholm", "description": "…" }]
}
```

- `status` måste vara en av: `order_received`, `packed`, `in_transit`,
  `ready_for_pickup`, `delivered`. Annat värde → "tillfälligt otillgänglig".
- `statusLabel` (valfri) ersätter standardrubriken. Lämna tom för att använda
  sidans egna svenska rubriker.
- Tidsstämplar i ISO 8601. Sidan visar dem i Europe/Stockholm
  ("26 september · 16:42"). `estimatedDelivery` kan vara `YYYY-MM-DD`.
- `description`/`location` ska vara **svensk kundtext**. Översätt DHL:s
  händelser på servern.
- Saknas spårningsnummer och status är `order_received`/`packed` visar sidan
  "Din order förbereds".
- Tomma fält döljs automatiskt.

### Mappning Shopify/DHL → status (förslag)

| Källa | status |
| --- | --- |
| Order betald, ingen fulfillment | `order_received` |
| Fulfillment skapad, DHL har ingen händelse än / "pre-transit" | `packed` |
| DHL `statusCode: transit` | `in_transit` |
| DHL händelse "ready for pickup" / ankommen till service point | `ready_for_pickup` |
| DHL `statusCode: delivered` | `delivered` |
| DHL `failure` / okänt | `in_transit` + förklarande händelsetext (eller egen status i framtiden) |

Se `reference-normalizer.js` för ett exempel mot DHL Shipment Tracking –
Unified API (`GET https://api-eu.dhl.com/track/shipments?trackingNumber=…`,
header `DHL-API-Key`). Nyckeln ska ligga i serverns miljövariabler.

## Säkerhet – checklista för backend

- [ ] App-proxyns HMAC-signatur verifieras på varje anrop.
- [ ] Bara POST accepteras; e-post finns aldrig i URL eller loggas i klartext.
- [ ] Rate limiting per IP **och** per ordernummer, t.ex. 10 försök / 15 min
      per IP och 5 / 15 min per ordernummer → `429`.
- [ ] Missbruksskydd: exponentiell fördröjning efter misslyckade försök,
      möjlighet att lägga till Turnstile/hCaptcha efter X fel.
- [ ] Samma svar och svarstid för "finns inte" och "fel e-post".
- [ ] Minsta möjliga data i svaret (se ovan). Inga Shopify-id:n.
- [ ] Tracking-flödet returnerar aldrig orderdata.
- [ ] `Cache-Control: no-store` på alla svar.
- [ ] DHL- och Admin API-nycklar enbart i serverns hemlighetshantering.
- [ ] Timeout mot DHL (< 10 s) och cache av DHL-svar (t.ex. 5 min per nummer)
      för att hålla nere anropen och DHL:s kvot.
