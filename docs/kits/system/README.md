# NordicReflection Kit PDP system (nr-ks) – step 1–5

Draft theme **205921845582** "Kit PDP-system – Exteriör Startkit (prototyp)",
duplicated from the live theme on 2026-10-04. Nothing published.

Preview (prototype): https://nordicreflection.se/products/litet-exterior-startkit?preview_theme_id=205921845582

## Step 1 – Audit (verified in Shopify 2026-10-04)

All eight kits are **standalone SKUs** with their own inventory
(`tracksInventory: true`, no Shopify Bundles, `requiresComponents: false`).
Components are stored as product references: `custom.kit_components` →
`nr_kit_component` metaobjects → one ProductVariant each (+ quantity, size,
role, group, purpose). Cart = one line item per kit. No compare-at prices.
Kit stock is NOT linked to component stock (fulfillment unchanged).

| Kit | Family | Tier | Price | Components | Bought separately | Saving | Media | Structural problem (live) | Data |
|---|---|---|---|---|---|---|---|---|---|
| Exteriör Startkit | Exteriör | Start | 429 kr | DeepDegrease 1000 ml, Alkastrike 500 ml, Pure Shampoo 500 ml | 497 kr | 68 kr | 1 packshot; clips via Alkastrike, Pure | Product cards, no system story, no family comparison incl. Foam/Komplett | High |
| Foam Wash Kit | Exteriör | Foam | 469 kr | Foamtastic 1000 ml, Foam Cannon | 568 kr | 99 kr | 1 packshot; 2 Foamtastic clips | Pressure-washer connection data missing | High (price) / **missing compatibility** |
| Exteriör Komplett Kit | Exteriör | Komplett | 1 199 kr | DeepDegrease, Alkastrike, Foamtastic, Pure Shampoo, Revolt, Clarity, Pristine, GlossCoat | 1 382 kr | 183 kr | 1 packshot; clips on 6 of 8 components | 8 equal cards, chemicals-only not obvious; stock 4 | High |
| Fälg Startkit | Fälgar | Fälg | 309 kr | Revolt 500 ml, Mikrofiber Fälgborste | 321,30 kr* | 12,30 kr | 1 packshot; Revolt (2) + brush clips | Real saving small because of an automatic discount | High |
| Fälg & Däck Komplett Kit | Fälg & däck | Fälg + däck | 499 kr | + Pristine 500 ml, Däckapplikator | 550,30 kr* | 51,30 kr | 1 packshot; Revolt, Pristine clips | Product title casing "Fälg Och Däck"; product type empty | High |
| Litet Interiör Startkit | Interiör | Bas | 259 kr | Core APC 500 ml, Scrub Pad, Mikrofiberduk 5-pack | 317 kr | 58 kr | 1 packshot; Core APC clip (presentation) | Upgrade path to Detalj/Komplett not visual | High |
| Mellan Interiör Startkit | Interiör | Detalj | 369 kr | + Detail Brush Duo 2-pack | 456 kr | 87 kr | 1 packshot | Brush stock 7 | High |
| Stort Interiör Startkit | Interiör | Komplett | 549 kr | + Clarity 500 ml, Glass Towel | 674 kr | 125 kr | 1 packshot | – | High |

\* Active automatic discount "revolt + mikrofiber" (buy Revolt → 30 % off the
brush) lowers the one-by-one price by 56,70 kr → stored once in
`custom.kit_separate_adjust` on the two wheel kits.

## Step 2 – Design system

Builds on the standard PDP (`assets/nr-pdp.css`): same tokens, trust line,
delivery line, brand reviews, 58/42 hero, section entrance. Kit layer:
`assets/nr-kitsys.css`.

| Token / component | Spec |
|---|---|
| Colour | ink #111, muted #5f5f5f, faint #8a8a8a (large numbers only), line rgba(17,17,17,.12), soft #f5f5f2, accent #1f6b3a (saving, "Ditt val", checks – nothing else) |
| Shape | sharp (radius 0) everywhere; buttons keep the theme radius |
| Type | theme fonts only. Hero name clamp(36–52px)/-0.03em; section H2 clamp(28–44px); step numbers clamp(40–68px) faint; labels 12px/600/0.14em uppercase |
| Spacing | section 56px mobile / 104px desktop; gutter 20/40; head → content 30/50px |
| Dividers | 1px ink above a group, 1px line between rows – never both on every row |
| Price | 28–34px/600 → "Köpta separat: X" muted 15px → "Du sparar X" accent 15px/600 |
| CTA | native buy button, label "Lägg paketet i varukorgen", min-height 56px; express checkout below |
| Media | product images on soft #f5f5f2, object-fit contain (never cropped); 4:5 sequence, 1:1 rows, 4:3 tiers; clips 4:5 |
| Motion | one 320ms fade/12px rise per section (nr-pdp.js), 200ms hover; none under reduced motion |
| Mobile | single column; proof clips in a native scroll-snap row; final CTA without the repeated packshot; Horizon sticky add-to-cart (hidden while the cart drawer is open – nr-pdp.css) |

### Page architecture (shared, content per kit)

| # | Section | File | Data |
|---|---|---|---|
| 1 | Decision zone | `blocks/nr-ks-intro` + native buy buttons + `nr-pdp-delivery` | kit_name, block copy, price, `nr-ks-separate` |
| 2 | Det här får du | `sections/nr-ks-contents` | kit_components (sequence ≤3, grouped rows ≥4 by component group) |
| 3 | System / rutin | `sections/nr-ks-system` | stage blocks with product references |
| 4 | Varför paketet? | `sections/nr-ks-value` | `nr-ks-separate`, kit price |
| 5 | Passar dig som + escape route | `sections/nr-ks-fit` | section copy, link to alternative kit |
| 6 | Kitfamiljen | `sections/nr-ks-tiers` | kit_family, kit_tier, kit_tier_summary, components ("Allt i X, plus …") |
| 7 | Riktiga produkter | `sections/nr-ks-proof` | first clip in each chosen product's pdp.demo_media; hidden without clips |
| 8 | Brand trust | `sections/nr-pdp-trust` (shared) | nr_trustpilot_review metaobjects; reviews mentioning kit components first |
| 9 | Bra att veta | `sections/nr-ks-details` | generated contents, safety notes, delivery + FAQ blocks per kit |
| 10 | Final CTA | `sections/nr-ks-final` | forwards to the hero add-to-cart |

### Single source of truth

- Every component = ONE variant reference; name, image, link, size, role
  come from it. No separate arrays for name/image/link/price.
- Separate value + saving: `snippets/nr-ks-separate` only (component
  variant prices × qty − `kit_separate_adjust`). Never compare-at.
- Shipping/delivery: theme settings (Frakt & leverans).
- Trustpilot: theme settings (rating shown as "NordicReflection … på Trustpilot", always brand level).

### New metafields (product, `custom`) – not read by the live theme

`kit_name`, `kit_tier`, `kit_tier_summary`, `kit_separate_adjust` – set on all
eight kits. Existing keys are only read.

## Step 3–4 – Exteriör Startkit prototype + QA

Local render (real prices, components, copy and reviews; placeholder images
because the CDN and storefront are not reachable from this environment) at
320, 375, 390, 430, 768, 1024, 1366 and 1920 px: no horizontal page scroll,
no duplicated ids, no clipped text, price/separate/saving = 429 / 497 / 68 kr
everywhere. Screenshots: `docs/kits/system/screens/`.

Not testable here (please check in the preview): real images/video, Horizon
sticky bar, cart drawer, add-to-cart, checkout, Trustpilot link.

## Data gaps / missing content

1. Only one image per kit (packshot). Missing: components-visible shot,
   in-use, result, routine visual, short kit video.
2. No clip for DeepDegrease, Scrub Pad, Mikrofiberduk, Detail Brush, Clarity,
   Glass Towel, Däckapplikator, Foam Cannon.
3. Foam Cannon connection / pressure-washer compatibility not documented
   (blocker for the Foam Wash page).
4. Trustpilot 4,7 / 34 omdömen is a theme setting – confirm it is current.
5. `kit_component_notes` is index-matched to the component list; reordering
   components requires reordering the notes.

## Restore

Draft only. Live theme 205795000654 unchanged. Delete the draft theme or
ignore it; the four new metafields are unused by the live theme.
