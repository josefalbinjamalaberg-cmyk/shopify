# Varukorg – ett tydligt nästa steg (2026-10-02)

Draft theme **205725663566** only (checked `role: UNPUBLISHED` before and after).
Nothing published; no app settings, product relations, discounts, shipping or
gift thresholds changed; no app installed.

Preview: https://nordicreflection.se/?preview_theme_id=205725663566 (add a
product → cart drawer) and https://nordicreflection.se/cart?preview_theme_id=205725663566

## What existed

| Part | Finding |
|---|---|
| Cart UI | Horizon cart drawer (`snippets/cart-drawer.liquid`, `cart_type: drawer`) – identical to the live theme. No recommendation code in the theme's cart files. |
| Cart page | `templates/cart.json` had a generic `product-list` section (collection **all**, first 4 products) – not related to the cart. |
| App | App embed **Section Store – block-cart** enabled; its content/logic is configured inside the app (global). Not visible through the theme. Most likely source of the earlier "Revolt → Däckapplikator" observation – **unverified** (storefront not reachable from here). |
| Product relations | No Search & Discovery complementary/related products on any product. `pdp.accessories` exists per product (used by the PDP). |
| Kit contents | `custom.kit_components` registered on all 8 kits (verified). The unlisted "Grundrutinen – Komplett tvättpaket" (0 in stock) has none. |
| Automatic discounts | One: **"revolt + mikrofiber"** – buy Revolt → 30 % off Mikrofiber Fälgborste, combines with nothing. Revolt 189 + borste 132,30 = 321,30 kr vs Fälg startkit 309 kr (verified). |
| Updates on cart change | Horizon re-renders `cart-items-component` (Section Rendering API) on every `CartLinesUpdateEvent` – anything rendered inside it updates automatically. |

## Change (minimal)

- `snippets/nr-cart-next-step.liquid` (new) – max two suggestions, first one is primary.
- `assets/nr-cart-next.js` (new) – "Lägg till": `/cart/add` + `CartLinesUpdateEvent`, busy state, no double adds, errors announced; custom events `nr_cart_rec_add` / `nr_cart_rec_click`.
- `snippets/cart-drawer.liquid` – renders the snippet between the items and the summary.
- `sections/main-cart.liquid` – same on the cart page (items column).
- `templates/cart.json` – generic "all products" list disabled (`"disabled": true`).

### Relations (theme-local, ranked)

| In cart (product or kit component) | Suggestion | Reason shown | Button |
|---|---|---|---|
| Revolt (loose) | **Fälg startkit** link instead of the brush | Revolt + Mikrofiber Fälgborste i ett paket … | Se paketet |
| Revolt (only inside a kit, e.g. Exteriör komplett) | Mikrofiber Fälgborste (189 kr – the discount needs a loose Revolt) | Kom åt smutsen på fälgen – även mellan ekrarna. | Lägg till |
| Pure Shampoo | Washpad | Mjuk mikrofiber för handtvätten med Pure Shampoo. | Lägg till |
| Clarity | Glass Towel | En glasduk till din glasrengöring. | Lägg till |
| Pristine | Däckapplikator | Applicera Pristine jämnt på däcksidan. | Lägg till |
| Core APC | Scrub Pad | Arbeta in Core APC i textil, plast och vinyl. | Lägg till |
| Foamtastic | Foam Cannon | … Kontrollera anslutningen före köp. | Se produkt (no direct add – connection not verified) |

Not suggested: spray equipment for chemicals (no verified chemical compatibility),
anything already in the cart, a component of a kit in the cart, an equivalent
(DeepReach Wheel Brush covers the wheel-brush task), sold-out products.
Multi-variant products would get "Välj alternativ" (none in the current list).

### Revolt + borste price

The brush is never offered next to a loose Revolt, so no pre-discount price
(189 kr) is shown for something that would cost 132,30 kr. Instead:
- Revolt alone → link to Fälg startkit with its current price (309 kr). Revolt stays in the cart.
- Revolt + borste already in the cart → kit shown only if its price is lower than what the
  cart actually charges for the two lines (`final_price`, after automatic discounts):
  "… i varukorgen kostar de nu 321,30 kr".
- Direct kit swap (replace lines) is **not** implemented – next step, see below.

## Open items

1. **Section Store "block-cart" embed** – still enabled in the draft. Shopify ignores
   embed on/off changes made through the file API. To see only the new suggestions,
   switch it off in the theme editor of the draft theme (App embeds). That is a
   per-theme setting; the app's own configuration stays untouched.
2. Direct kit swap (Revolt → Fälg startkit in one click) – separate step.
3. Real storefront/cart/checkout tests – not possible from here (storefront blocked).

## Restore

`docs/cart/backup/*.theme-205725663566.2026-10-02` – upload back the four files
(cart-drawer, main-cart, cart.json; settings_data unchanged) and delete
`snippets/nr-cart-next-step.liquid` and `assets/nr-cart-next.js`.
