# Collection pages: four shopping experiences, one system

Audit: `audit-2026-10-04.md`. Screens: `screens/`. Local harness:
`harness.py` + `mock-server.py` + `interaction-qa.js`.

## Templates (one per collection question)

| Collection | Template | Question | Shopping shortcut | Editorial moment |
|---|---|---|---|---|
| Exteriör | `collection.exterior` | What problem do I need to solve? | "Vad behöver bilen?" chips (`nrc.intent_exterior`) | after product 4: "Osäker på avfettning?" Alkastrike vs DeepDegrease → PDP comparison; after the grid: "Vill du slippa välja?" Exteriör Komplett Kit |
| Interiör | `collection.interior` | What am I cleaning? | "Vad ska du rengöra?" chips (`nrc.intent_interior`) | after product 4: kit ladder Bas 259 → Detalj 369 → Komplett 549 (what each adds, saving); kits leave the grid unless "Färdiga paket" is chosen |
| Tillbehör | `collection.accessories` | What job do I need a tool for? | "Vad ska du göra?" chips (`nrc.intent_accessories`) + Filtrera: Produkttyp (`nrc.product_kind`) | after the cloths (product 12, or after the towels when "Torkning" is chosen): "Vilken torkduk passar dig?" 70×90 / 50×80 / 40×40; one "Passar med" line per card (`nrc.pairs_with`) |
| Färdiga paket | `collection.kits` | How complete a solution? | area tabs Exteriör / Fälg & däck / Interiör (URL hash) | each family side by side: role, name, who, contents or "Allt i X, plus …", count, Paketpris, Köpta separat, Du sparar |
| Alla produkter + others | `collection` (default) | Browse everything | category links + Filtrera: Produkttyp | none |

Shared pieces: `sections/nr-shop.liquid`, `sections/nr-kit-hub.liquid`,
`snippets/nr-shop-card.liquid`, `snippets/nr-shop-module.liquid`,
`snippets/nr-kit-adds.liquid`, `assets/nr-shop.css`, `assets/nr-shop.js`
(tokens and buttons from `assets/nr-homepage.css`).

Native all the way: chips, active pills, "Rensa alla", the drawer and the
sort are links / GET forms to Shopify's own filter and sort URLs (reload,
back, sharing, canonical behaviour unchanged). `nr-shop.js` only swaps the
results in place (section rendering + pushState), shows the drawer's live
count, adds quick add (Ajax Cart API + `CartLinesUpdateEvent`) and the kit
tabs, and publishes `nr_collection_view`, `nr_collection_intent_select`,
`nr_collection_filter_select`, `nr_collection_filter_clear`,
`nr_collection_sort`, `nr_collection_product_click`,
`nr_collection_quick_add`, `nr_collection_kit_click` (collection, intent,
product, position). Horizon's `collection-component` still sends the
standard `collection_viewed` event.

"Rekommenderat" = the collection's manual order (Admin). Sort options:
Rekommenderat, Bästsäljande (Shopify's real sales order), Nyast, Pris lågt
till högt, Pris högt till lågt.

## Data (Shopify)

- `nr_filter_value` metaobjects: customer label + internal key (e.g. label
  "Flygrost & bromsdamm", key `iron`).
- Product metafields `nrc.*`: `card_name`, `card_line`, `card_label`,
  `intent_exterior`, `intent_interior`, `intent_accessories`, `product_kind`,
  `pairs_with` (new). Source of truth: `content-source.py`.

## Search & Discovery: once, by hand (the API cannot do this)

Until these filters exist the pages work as plain, well-designed lists, but
the chips and Filtrera have nothing to filter with (the theme editor shows a
note where the chips go).

1. Shopify admin → **Appar** → **Search & Discovery** → **Filter**.
2. **Lägg till filter** → in the list choose **Vad vill du lösa? (Exteriör)** →
   Etikett: **Vad behöver bilen?** → **Spara**.
3. **Lägg till filter** → **Vad vill du göra? (Interiör)** → Etikett:
   **Vad ska du rengöra?** → **Spara**.
4. **Lägg till filter** → **Vad behöver du? (Tillbehör)** → Etikett:
   **Vad ska du göra?** → **Spara**.
5. **Lägg till filter** → **Produkttyp** (the one from "Produkttyp" metafield,
   values Dukar, Borstar …) → Etikett: **Produkttyp** → **Spara**.
6. Leave the store's other filters as they are; these pages only show the
   filters named in their template.

## Go-live (after you have approved and published the theme)

Admin → **Produkter** → **Kollektioner** → open each → **Temamall** (right
column) → choose → **Spara**:

| Collection | Template |
|---|---|
| Exteriör | `exterior` |
| Interiör | `interior` |
| Tillbehör | `accessories` |
| Färdiga paket | `kits` |

`/collections/all` and every collection without a template use the new
default automatically. Preview before that, on the preview theme:
`/collections/exterior?view=exterior&preview_theme_id=<id>` (same for
`interior`, `accessories`, `fardiga-paket?view=kits`).

The mega menu is untouched: clicking EXTERIÖR still opens
`/collections/exterior`, the chevron still opens the submenu.

## Open data points (not changed)

- Torkduk 70×90: title says 1400 GSM, description says 1300 GSM.
- `packages` ("Färdiga paket", 0 products) duplicates `fardiga-paket`;
  consider deleting or redirecting it.
- Three unlisted kits (Grundrutinen 699, Glans & Skydd 489, Torkduksset 649)
  sit in Färdiga paket but are hidden by Shopify; not part of the families.
- Revolt's 2nd/3rd images are AI renders, so no second-image hover is used.
