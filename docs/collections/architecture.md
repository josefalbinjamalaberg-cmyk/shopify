# Collection pages – architecture (Exteriör first)

Preview theme: **205369311566 "Collections – Exteriör (preview)"** (duplicate of the live theme).
Preview URL: `https://nordicreflection.se/collections/exterior?view=exterior&preview_theme_id=205369311566`

## Principle
Native Shopify all the way: Search & Discovery filters on product metafields, Shopify's own filter
URLs (reload / share / back button work), Shopify's manual collection order as "Rekommenderat",
Horizon's own filter drawer, sorting, pagination, product card, quick add and cart drawer.
No filtering library, no client-side catalogue, no title matching.

## Data model (Shopify)
| What | Where |
|---|---|
| Customer-facing filter values | Metaobject `nr_filter_value` (`label` = customer copy, `key` = internal, `group`) – 26 entries |
| Exteriör: "Vad vill du lösa?" | `nrc.intent_exterior` (list → nr_filter_value) |
| Interiör: "Vad vill du göra?" | `nrc.intent_interior` |
| Tillbehör: "Vad behöver du?" | `nrc.intent_accessories` |
| Secondary (Tillbehör/Interiör) | `nrc.product_kind` (→ nr_filter_value) |
| Card copy | `nrc.card_name`, `nrc.card_line`, optional `nrc.card_label` (kit tiers) |

One metafield per shopping context, so products that live in two collections (Scrub Pad, Detail Brush,
Mikrofiberduk, Glass Towel, Clarity) never leak the other page's chips. Source of truth for every value:
`docs/collections/content-source.py`. First value in an intent list = the small label on the card.

## Theme
- `sections/nr-collection.liquid` – one section, logic per template via settings:
  `primary_filter` (chips), `chip_order` (metaobject handles), `secondary_filters`, `card_intent`,
  help link, tip line, small CTA, cross-links. Only the listed filters are passed to Horizon's
  filters block, so the store's other filters never appear on these pages.
- Chips = links to native filter URLs, single choice per row (a chip replaces the current value;
  tapping the selected chip or "Visa alla" removes it). Multi-select stays available in the
  mobile drawer (OR within a filter, AND across filters – Shopify's native logic).
- `blocks/nr-card-info.liquid` – label → name → one line (hidden in 2-col mobile) → price → button.
  Single variant = "Lägg till" (Horizon quick add → cart drawer); options = "Välj alternativ" (quick-add modal);
  sold out = disabled "Slutsåld".
- `assets/nr-collection.js` – upgrades filter links to Horizon's in-place section render, re-renders
  on back/forward (Horizon doesn't), keeps the selected chip in view, publishes `nr_collection_view`,
  `nr_collection_filter_select`, `nr_collection_filter_clear`, `nr_collection_sort`,
  `nr_collection_product_click`, `nr_collection_quick_add` via `Shopify.analytics.publish`.
- Horizon edits (small, theme-wide): `blocks/_product-card.liquid` allows `nr-card-info`;
  `snippets/sorting.liquid` shows Rekommenderat / Pris: lågt → högt / Pris: högt → lågt / Nyast;
  `locales/sv.json`: "Filtrera", "Visa N produkter", "N produkter", "Välj alternativ".
- PDP comparison block: anchors `#jamfor` (all) and one from the heading → `#vilken-avfettning`
  on Alkastrike/DeepDegrease.

## Search & Discovery – steps for the store owner (once)
1. Shopify admin → **Appar** → **Search & Discovery** → **Filter**.
2. **Lägg till filter** → source **Vad vill du lösa? (Exteriör)** → change the label to **Vad vill du lösa?** → **Spara**.
3. **Lägg till filter** → **Vad vill du göra? (Interiör)** → label **Vad vill du göra?** → **Spara**.
4. **Lägg till filter** → **Vad behöver du? (Tillbehör)** → label **Vad behöver du?** → **Spara**.
5. **Lägg till filter** → **Produkttyp** → keep the label → **Spara**.
6. Keep that order in the filter list (drag if needed). Existing filters (price, availability…) can stay;
   they are not shown on these three pages.

Until step 2 is done the Exteriör page shows no chips (the theme editor shows a note instead).

## Go-live (after the preview is approved and the theme is published)
Set the Exteriör collection's theme template to `collection.exterior` (Admin → Produkter → Kollektioner →
Exteriör → Temamall). Interiör and Tillbehör follow in phases 4–5 with their own templates.
