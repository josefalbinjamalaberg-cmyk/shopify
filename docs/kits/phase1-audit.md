# Kit PDPs – Phase 1 audit

Date: 2026-09-28 · Source: Shopify Admin API + live theme 205360922958. **No edits made.**

## Active kits (8) — verified

All eight are **single-SKU kits** (own variant + own inventory, `hasVariantsThatRequiresComponents: false`) – not
Shopify native bundles. No compare-at price is set on any kit. Components are defined in
`custom.kit_components` (metaobject `nr_kit_component` → exact product **variant** reference + quantity, size, role,
group, purpose). Separate value below = sum of those variants' current prices × quantity.

| Kit | Price | Components (variant ref · qty 1 each) | Separate value | Saving | Media | Template | Biggest page problem | Data confidence |
|---|---|---|---|---|---|---|---|---|
| Exteriör Startkit | 429 kr | DeepDegrease 1000 ml (169) · Alkastrike 500 ml (149) · Pure Shampoo 500 ml (179) | 497 kr | 68 kr | 1 packshot | `kit-exteriorstart` (old, hardcoded) | Saving never shown (old template only shows it if compare-at > price); eyebrow "Färdigt paket"; routine lumps DeepDegrease + Alkastrike as one "Avfetta" step | Price/value **high** · routine order **unverified** |
| Foam Wash Kit | 469 kr | Foamtastic 1000 ml (169) · Foam Cannon (399) | 568 kr | 99 kr | 1 packshot | `kit-foamwash` (old) | No compatibility block near the buy button; saving hidden; foam videos exist on the component PDPs but not used | Value **high** · pressure-washer connection **unknown** |
| Exteriör Komplett Kit | 1 199 kr | DeepDegrease 1000 ml · Alkastrike 500 ml · Foamtastic 1000 ml · Pure Shampoo 500 ml · Revolt 500 ml · Clarity 500 ml · Pristine 500 ml · GlossCoat 500 ml | 1 382 kr | 183 kr | 1 packshot | `kit-exteriorkomplett` (earlier nr-kit system) | Already on the data-driven system, but: 8 products not grouped into jobs; an extra AI-generated review block duplicates the proof section; value point "Fri frakt" hardcoded; 1 image | **High** (sizes match PDP specs except Revolt/GlossCoat, which come only from the kit data) |
| Fälg startkit | 309 kr | Revolt 500 ml (189) · **Mikrofiber Fälgborste** (189) | 378 kr | 69 kr | 1 packshot | `kit-falgstart` (old) | Saving hidden; no "Revolt + borste" story; no link up to Fälg & Däck | **High** – note: the brush is the Mikrofiber Fälgborste, not DeepReach |
| Fälg Och Däck Komplett Kit | 499 kr | Revolt 500 ml · Mikrofiber Fälgborste · Pristine 500 ml (189) · Däckapplikator (40) | 607 kr | 108 kr | 1 packshot | `kit-falgdack` (old) | Saving hidden; wheel vs tyre not split into two mini-systems | **High** |
| Litet interiör Startkit | 259 kr | Core APC (159) · Scrub Pad (39) · Mikrofiberduk **5-pack variant** (119) | 317 kr | 58 kr | 1 packshot | `kit-interiorlitet` (old) | No tier comparison; saving hidden | **High** – Core APC volume not recorded |
| Mellan interiör Startkit | 369 kr | Litet + Detail Brush Duo 2-pack (139) | 456 kr | 87 kr | 1 packshot | `kit-interiormellan` (old) | "What Mellan adds" not shown | **High** |
| Stort interiör Startkit | 549 kr | Mellan + Clarity 500 ml (149) + Glass Towel (69) | 674 kr | 125 kr | 1 packshot | `kit-interiorstort` (old) | "What Stort adds" not shown | **High** |

Not in scope (not active): Grundrutinen, Torkduksset, Glans & skydd (UNLISTED, 0 stock, no media, no component data);
Tvätta, torka & skydda and Exteriör Plus (DRAFT – these two ARE native Shopify bundles).

## Findings that apply to all kits

1. **Two template generations.** 7 kits use old, per-kit templates (~31 KB each) built from generic text blocks,
   `all_products['handle']` component chips and hardcoded copy ("Färdigt paket", "Fri frakt över 799 kr").
   Exteriör Komplett uses the earlier data-driven system (`nr-kit-*` sections/blocks, also `product.kit-test`).
   → Rebuild on that system: one `product.kit` template for all eight.
2. **Saving is invisible on 7 of 8 pages.** The old templates only show a saving when compare-at > price, and
   compare-at is empty (correctly – "köpta separat" is not a previous price). The data-driven
   `nr-kit-separate-total` already calculates from the variant references and matches every figure above.
3. **Hardcoded prices in descriptions** ("Köpt separat: 497 kr …"). They match today but will drift when a
   component price changes. The new page shouldn't need them.
4. **Media:** each kit has exactly one image (the packshot). Real use media exists on component PDPs
   (`pdp.demo_media` – foam, Foam Cannon, wheel brush, Revolt reaction, Pristine, Core APC, washpad, shampoo, GlossCoat)
   and can be reused honestly as "real use" clips. No kit-specific in-use/result photos or routine graphics exist.
5. **Routine order is marked unverified** on all kits (`custom.kit_routine_verified = false`). Without confirmation
   the routine section must show "Vad varje del löser" rather than a numbered sequence (e.g. the order of DeepDegrease vs
   Alkastrike is not documented anywhere).
6. **Foam Cannon compatibility:** only the verified text "used with a pressure washer; connection varies by model –
   check before buying" exists (`custom.kit_notice`, Foam Cannon PDP). No connector/adapter spec exists in Shopify.
7. **Inventory:** kits have their own stock independent of component stock (e.g. Komplett 5 in stock while DeepDegrease
   has 5). Not a page problem, but orders don't decrement component stock.
8. **Trust:** Trustpilot 4.7 (theme setting) + 5 verbatim reviews (`nr_trustpilot_review`) are available and brand-level.
9. **Existing kit data to reuse:** `kit_eyebrow` (already role-based, e.g. "Exteriör · Start"), `kit_tagline`,
   `kit_value_points`, `kit_fit_points`, `kit_family` (3/3/2 correct families), `kit_card_line`, `kit_alt_question`,
   `kit_notice`. Component `purpose` texts are generic in places and should be rewritten per kit ("why it's in THIS kit").
10. Mobile: the live storefront can't be loaded from this environment (proxy); mobile checks will be done in the local
    render harness and then by you in the preview theme.

## Needs your input before phase 3
- A. Confirm the real usage order for Exteriör Start/Komplett (e.g. DeepDegrease spot-treatment → Alkastrike prewash → Pure Shampoo), or keep "Vad varje del löser".
- B. Foam Cannon connection: which connector/adapter does it use (e.g. which pressure-washer brands fit)? Without it the block only says "check the connection".
- C. Revolt, GlossCoat and Core APC volumes: confirm 500 ml / 500 ml / ? .
- D. Titles: tidy "Fälg startkit" → "Fälg Startkit", "Fälg Och Däck Komplett Kit" → "Fälg & Däck Komplett Kit", "Litet/Mellan/Stort interiör Startkit" → "… Interiör Startkit"? (changes product titles, not URLs)
- E. Any kit-specific photos (kit in use / result)? Otherwise the gallery uses the packshot + real component clips.
