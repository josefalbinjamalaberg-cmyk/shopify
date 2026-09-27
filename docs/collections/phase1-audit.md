# Collection pages – Phase 1 audit (Exteriör, Interiör, Tillbehör)

Audit date: 2026-09-27. Source: Shopify Admin API + live theme `205360922958` ("PDP-system – Revolt", MAIN).
Nothing was modified.

## 1. Collections

| Collection | Handle | Type | Sort order | Products | Description | SEO title/desc | Image | Template |
|---|---|---|---|---|---|---|---|---|
| Exteriör | `exterior` | Manual (no rules) | **BEST_SELLING** | 8 | empty | empty | none | `collection.json` (default) |
| Interiör | `interior` | Manual | **BEST_SELLING** | 3 | empty | empty | none | default |
| Tillbehör | `accessories` | Manual | **BEST_SELLING** | 14 | empty | empty | none | default |

Other collections found (not in scope, noted only): `dack-falg` (3), `fardiga-paket` (11, MANUAL), `packages` (0 – empty duplicate of Färdiga paket), `frontpage` (0), example-products (0).

## 2. Products per collection (current order = best selling)

All products below: ACTIVE, one variant unless stated, in stock, no compare-at price, `templateSuffix: standard`, vendor `nordicreflection`, **empty productType**, **no tags** (except Detail Brush: `interior`).

### Exteriör (8) – chemicals only, all single size
| # | Product | Price | Images | Stock |
|---|---|---|---|---|
| 1 | Revolt – Flygrostborttagare | 189 | 3 | 100 |
| 2 | GlossCoat – Sprayförsegling | 189 | 1 | 15 |
| 3 | Alkastrike – Alkalisk Avfettning | 149 | 1 | 100 |
| 4 | DeepDegrease – Kallavfettning | 169 | 1 | 5 |
| 5 | Pure Shampoo – Bilschampo | 179 | 1 | 11 |
| 6 | Foamtastic – Snow Foam för effektiv förtvätt | 169 | 2 | 13 |
| 7 | Pristine - Däck- & Plastförnyare | 189 | 1 | 15 |
| 8 | Clarity – Glasrengöring | 149 | 1 | 17 |

No kits, no Foam Cannon, no multiple sizes → **a size filter is not justified today**.

### Interiör (3)
| Product | Price | Images |
|---|---|---|
| Core APC – Allrengöring (APC) | 159 | 1 |
| Scrub Pad | 39 | 3 |
| Detail Brush Duo – 2-pack | 139 | 1 |

**Only 3 products.** Clarity, Glass Towel, Mikrofiberduk and the three interior kits are *not* in this collection, so the requested intents GLAS, TORKA AV and FÄRDIGA PAKET would return nothing today.

### Tillbehör (14)
Foam Cannon 399 · Tvätthink 299 · Däckapplikator 40 · Scrub Pad 39 · Torkduk 70x90 329 · Torkduk 40x40 149 · Torkduk 50x80 229 · Mikrofiber Fälgborste 189 · Glass Towel 69 · Detail Brush Duo 139 · **Mikrofiberduk 49–199 (3 variants)** · Washpad 149 · Tryckspruta 299 · DeepReach Wheel Brush 169.

Mikrofiberduk is the only multi-variant product → must use "Välj alternativ", not direct add.

### Interior kits (in Färdiga paket, verified contents via `custom.kit_components`)
| Kit | Price | Contents |
|---|---|---|
| Litet interiör Startkit | 259 | Core APC · Scrub Pad · Mikrofiberduk 5-pack |
| Mellan interiör Startkit | 369 | Litet + Detail Brush Duo |
| Stort interiör Startkit | 549 | Mellan + Clarity 500 ml + Glass Towel |

→ Honest tier labels: Litet "Grundrutin", Mellan "+ detaljborstar", Stort "+ glas". The suggested "Ny på interiörtvätt? Core APC + Scrub Pad + Mikrofiber → Litet Startkit" **matches the real contents.**

## 3. Theme (collection template)

One template for all collections: `templates/collection.json`.

- Sections: `main-collection` + an empty `_blocks` section. **No collection title / H1 / description block is rendered** (SEO + orientation gap).
- `filters` block: **`enable_filtering: false`, `enable_sorting: false`**, grid density off. Customers currently cannot filter or sort.
- Infinite scroll on (24/page) – fine at this catalogue size.
- Grid: `product_card_size: medium` desktop, `mobile_product_card_size: small` (= 2 columns on mobile).
- Product card: image (`image_ratio: adapt` → **inconsistent aspect ratios**), full Shopify title (e.g. "Foamtastic – Snow Foam för effektiv förtvätt"), price. No descriptor / use-case line.
- Quick add: `quick_add` on (theme default) → desktop hover only; `mobile_quick_add` off → **no quick add on mobile**. Cart type drawer, auto-open on.
- Badges: only Sold out / Sale (native). None active today (all in stock, no compare-at).
- Card hover effect: none; no second-image hover.
- No collection-specific custom sections.

## 4. Search & Discovery

Filter configuration of the Search & Discovery app is **not readable or writable through the Admin API**. Since theme filtering is disabled, whatever is configured there has no visible effect today. Enabling native filters requires the store owner to add them once in *Search & Discovery → Filters* (a 2-minute manual step – I'll give exact instructions in Phase 2).

## 5. Data available for filtering

| Data | Status |
|---|---|
| Tags | effectively none |
| productType | empty on every individual product |
| `custom.product_category` | chemicals only, free text, not filter-ready |
| `pdp.value_line`, `pdp.type_label`, `pdp.problems` | all 23 products – good source for card descriptor copy, **not** for filtering |
| Metafield definitions usable as storefront filters | **none** exist yet |
| Kit contents (`custom.kit_components`) | complete for all kits |
| Trustpilot (theme settings `nr_trustpilot_*`) | available for one page-level trust line |

## 6. Proposed data model (for approval in Phase 2)

Native Shopify filtering (Search & Discovery) with **metaobject-reference metafields**, so the internal key and the customer label are separate and the URL is the native `?filter.p.m.…` URL (back button, reload and sharing work, no JS-only state).

**Metaobject `nr_intent`**: `label` (customer copy, e.g. "Trafikfilm & vägsmuts"), `key` (internal, e.g. `traffic_film`).

**Product metafields** – one per shopping context, so a product in two collections (Scrub Pad, Detail Brush) never leaks the wrong chips into the other page:

| Metafield | Type | Used on |
|---|---|---|
| `nr.intent_exterior` | list.metaobject_reference → nr_intent | Exteriör |
| `nr.intent_interior` | list.metaobject_reference | Interiör |
| `nr.intent_accessories` | list.metaobject_reference | Tillbehör |
| `nr.wash_stage` | list.metaobject_reference (optional) | Exteriör secondary |
| `nr.product_kind` | metaobject_reference (Kem/Pad/Borste/Duk/Paket/Spruta/Hink/Applikator) | Tillbehör secondary |
| `nr.card_name` | single_line_text | short card name ("Revolt") |
| `nr.card_line` | single_line_text | ≤ 35 chars card descriptor ("Flygrost & bromsdamm") |

Each collection gets its own template (`collection.exterior/interior/accessories.json`) that decides which of those filters is shown; the others stay hidden on that page. Native logic = OR within a filter, AND across filters, which is what we want (e.g. two intents together widen the result, never empty it).

### Draft mapping (verified against PDP content – to be confirmed)
**Exteriör**: Trafikfilm & vägsmuts → Alkastrike · Asfalt & tjära → DeepDegrease · Flygrost & bromsdamm → Revolt · Foam / förtvätt → Foamtastic · Handtvätt → Pure Shampoo · Skydd & glans → GlossCoat · Glas → Clarity · Däck & plast → Pristine. (1 product per chip today – so a secondary "Steg i tvätten" filter adds little; I'll propose it off by default.)

**Interiör** (requires adding products to the collection): Rengöra ytor → Core APC · Ingrodd smuts → Core APC, Scrub Pad · Detaljer & springor → Detail Brush Duo, Mikrofiberduk · Glas → Clarity, Glass Towel · Torka av → Mikrofiberduk · Färdiga paket → Litet/Mellan/Stort.

**Tillbehör**: Förtvätt & applicering → Foam Cannon, Tryckspruta · Handtvätt → Washpad, Tvätthink · Fälgar & däck → Mikrofiber Fälgborste, DeepReach, Däckapplikator · Torkning → Torkduk 70x90, 50x80 · Interiör → Scrub Pad, Detail Brush Duo, Mikrofiberduk · Glas → Glass Towel · Detaljering → Torkduk 40x40, Mikrofiberduk, Detail Brush Duo. Product-type secondary: Skumkanon/spruta (2) · Borste (3) · Pad (2) · Duk (5) · Hink (1) · Applikator (1). A separate towel "Användning" filter is unnecessary – the intents already cover drying / glass / detail.

## 7. Issues found

1. No H1/title or intro on collection pages.
2. Filtering and sorting disabled.
3. Default order = best selling (not intentional merchandising) → switch to MANUAL with the proposed order.
4. Interiör holds only 3 products; glass, wipe and kit intents impossible until products are added.
5. Mixed image aspect ratios (`adapt`).
6. Long titles dominate cards; no "what does it do" line.
7. No quick add on mobile.
8. No filter-ready product data (no tags, types or filterable metafields).
9. Collection descriptions and SEO fields empty.
10. Empty duplicate collection `packages` ("Färdiga paket") – may confuse search/SEO.
11. No page to link "Osäker på vilken avfettning du behöver?" to – the Alkastrike/DeepDegrease PDP comparison block is the closest real target.

## 8. Decisions needed before Phase 2

- A. Add Clarity, Glass Towel, Mikrofiberduk and the three interior kits to **Interiör**?
- B. Switch the three collections to **manual order** (proposed Exteriör order: Revolt, Alkastrike, DeepDegrease, Foamtastic, Pure Shampoo, GlossCoat, Clarity, Pristine)?
- C. Kits on Exteriör: keep them out of the grid and show one small "Vill du slippa välja? → Färdiga paket" link below it?
- D. OK that you add the filters once in Search & Discovery (I can't do it via API)?
