# Kit PDP system (v2)

One template for every kit. `templates/product.kit.json` is the master; each kit keeps its existing
template suffix (`product.kit-exteriorstart.json`, …) with **identical content**, so no product has to be
re-assigned. Everything kit-specific lives in the kit product's metafields.

## Page structure
| # | Module | File | Source |
|---|---|---|---|
| 01 | Hero: Trustpilot micro-proof → eyebrow → title → who-for → price → köpta separat / du sparar → 3 points → notice → CTA → delivery | `product-information` + blocks `nr-kit-intro`, `nr-kit-pricing`, `buy-buttons`, `nr-kit-trust` | theme settings (Trustpilot, Frakt & leverans); `kit_eyebrow`, `kit_tagline`, `kit_value_points`, `kit_notice(_heading)`; separate value = `snippets/nr-kit-separate-total` |
| 02 | Det här får du | `sections/nr-kit-contents` | `kit_components` (variant refs), product `pdp.type_label`, `kit_component_notes` |
| 03 | Routine | `sections/nr-kit-routine` | `kit_routine` (JSON, verified only); fallback: component groups |
| 04–05 | Varför paketet? + Passar dig som / alternatives | `sections/nr-kit-value` | price vs separate total; `kit_fit_points`; family kits' `kit_alt_question` + `kit_fit_points` |
| 06 | Välj rätt nivå | `sections/nr-kit-family` | `kit_family`; counts, prices and "Allt i X, plus:" computed from component refs |
| 07 | I riktig användning | `sections/nr-kit-proof` | component `custom.result_video`, else first video in `pdp.demo_media` (hidden if none) |
| 08 | Vad kunder säger om NordicReflection | `sections/nr-pdp-trust` | `nr_trustpilot_review`; reviews mentioning a kit component first |
| 10 | Vanliga frågor | `sections/nr-kit-faq` | generated (contents, separate price, how to use, safety from `pdp.safety_note`, delivery from settings) + `kit_faq` |
| 11 | Final CTA | `sections/nr-kit-final` | submits the page's own product form (existing cart/cart drawer) |
Sticky mobile CTA: Horizon's native sticky add-to-cart (`enable_sticky_add_to_cart`).

## Kit metafields (custom.*)
`kit_components` · `kit_family` · `kit_eyebrow` · `kit_tagline` (who it is for) · `kit_value_points` (3) ·
`kit_fit_points` · `kit_card_line` · `kit_alt_question` · `kit_notice` + `kit_notice_heading` ·
`kit_component_notes` (why each component is in THIS kit, same order as components) ·
`kit_routine` (JSON) · `kit_faq` ("Fråga | Svar" per line).

### kit_routine JSON
```json
{ "heading": "Din exteriörrutin", "lead": "…", "numbered": false,
  "stages": [ { "label": "Före handtvätten",
                "tasks": [ { "title": "Asfalt & tjära", "items": [1], "text": "…" } ] } ],
  "note": "…" }
```
`items` = component positions (1-based). Stages are joined with ↓ (verified before/after); tasks inside a stage sit
side by side (no order between them); several items in a task are joined with + (used together).

## Rules
- "Köpta separat" = current price of each component variant × quantity. Never compare-at, never "REA".
- No routine order unless verified; otherwise tasks side by side ("vad varje del löser").
- Brand reviews are always labelled as reviews of NordicReflection, never of the kit.
