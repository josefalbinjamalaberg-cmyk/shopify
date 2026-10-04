# Homepage refinement – audit and pass 1 (2026-10-04)

Draft theme **205921845582** (the only free draft: the store is at the
20-theme limit; it is a copy of the live theme from 2026-10-04 plus the kit
PDP prototype). Live theme 205795000654 untouched. Nothing published.

Preview: https://nordicreflection.se/?preview_theme_id=205921845582

## Current homepage (live, verified)

| # | Section | Job | Verdict |
|---|---|---|---|
| 1 | Hero video "Bilvård byggd steg för steg" + Handla bilvård / Hitta ditt tvättkit | Brand + discovery | KEEP headline and CTAs; REFINE video source, mobile height, subtext |
| 2 | Trust row (Trustpilot, leverans, fri frakt) | Trust | REFINE – values were typed text, 3 stacked items on mobile |
| 3 | Hitta rätt paket (Start / Skumtvätt / Komplett) | AOV | KEEP – REFINE saving display and copy |
| 4 | Bästsäljare (4 native product cards) | Product | KEEP – REFINE selection to real sales |
| 5 | Rätt produkt för rätt typ av smuts (3 cards) | Education → product | REFINE into the full problem → product index |
| 6 | Vad våra kunder säger (AI-generated block, pasted reviews) | Trust | REPLACE with metaobject-driven reviews |
| 7 | Utvalda kategorier (Exteriör / Interiör / Tillbehör) | Discovery | KEEP – heading copy |
| 8 | Bilvård ska vara enklare att förstå | Brand | KEEP – principle copy |
| – | Empty `_blocks` section | none | REMOVE |
| – | Disabled: shop-by-problem, demo, guides, results, newsletter | – | leave disabled |

Data: 90-day sales – Revolt 19, Exteriör Komplett Kit 16, Alkastrike 16,
GlossCoat 16, Core APC 10, DeepDegrease 10, Foamtastic 9, Pure Shampoo 8 →
"Bästsäljare" and "Bästsäljande kit" (Komplett) are supported.
All nine homepage products have one variant (quick add can't pick a wrong one).

## Ranked findings

| P | Finding | Change |
|---|---|---|
| P0 | Hero and proof videos used `sources.last` = the HLS playlist (m3u8) declared as video/mp4 → no playback in Chrome/Firefox (poster only) | `snippets/nr-video-sources`: MP4 only, ≤720p phones / ≤1080p desktop |
| P1 | Kit cards: "−X %" and a saving meter read as a sale | Plain "Du sparar X kr" under the price (green as on kit pages) |
| P1 | Kit "who it is for" hidden behind the mobile toggle; long body text | Who-for line visible under the name; body text removed; points describe contents, not price again |
| P1 | Problem section covered 3 of 8 jobs, one was not a problem | Full index: Flygrost och bromsdamm → Revolt, Trafikfilm → Alkastrike, Asfalt och tjära → DeepDegrease, Skumförtvätt → Foamtastic, Handtvätt → Pure Shampoo, Glans och skydd → GlossCoat, Glas → Clarity, Däck och plast → Pristine; whole row links, live price; "Ingen tvätt kräver alla åtta." |
| P1 | Reviews pasted into an AI block (second copy of the Trustpilot data), body clamped mid-sentence, star characters | `sections/nr-home-reviews` from `nr_trustpilot_review` metaobjects + theme Trustpilot settings, full text, duplicate truncated titles hidden, swipe row on phones |
| P1 | Mobile hero 78svh (≈620px): first shopping content below the fold | 66svh, max 560px; trust row compact → kits heading visible on 390 × 844 |
| P1 | Trust row values typed by hand | [rating] [count] [threshold] tokens from theme settings |
| P1 | Mobile quick add is OFF (theme setting `mobile_quick_add`, default) | **Not changed** (global theme setting) – recommended: Theme settings → Product cards → Quick add on mobile |
| P2 | Mobile nav "Rätt produkt i rätt ordning. 8 steg · Från rengöring till finish" | "Rätt produkt för varje jobb. 8 produkter · Använd det bilen behöver" |
| P2 | Hero subtext "en produkt för varje steg" | "rätt produkt för varje jobb" (headline kept) |
| P2 | Category images are HEIC (image/heic) | **Verify in Chrome**; if not shown, re-upload as JPG |
| P2 | Welcome popup + floating "Få 15% rabatt" button on every page + footer "Få 10%" | **Not changed** (promotion). Recommendation: keep popup, hide the floating button on the homepage |
| P3 | Desktop hero overlay 0 % with white text | Check legibility on the real video; add a subtle left gradient if needed |

## Rhythm after pass 1

video hero → white trust line → soft kits → white bestsellers →
**dark** problem index (only dark moment) → white reviews → soft categories →
white brand story.

## QA (local render, real prices/products/reviews, placeholder media)

320, 375, 390, 430, 768, 1366, 1440, 1920 px: no horizontal page scroll
(one found and fixed: screen-reader text in the review swipe row), no
duplicated ids. Not testable here (storefront/CDN blocked): real video
playback, images, header/nav, quick add, cart drawer, Trustpilot link,
Klaviyo popup.

## Restore

`docs/home/backup/` holds the live `index.json` and `header-group.json`.
Section files: previous versions = commit before 3c43fcb.

## Pass 2: campaign advisor, routine builder, kit and category art direction (2026-10-04)

The design read was: preserve-mode redesign of a premium Scandinavian automotive DTC homepage, monochrome with one green "saving" accent, dials 6/4/3. Only three areas changed. Nothing new was added to the page.

### 1. "Rätt produkt för rätt typ av smuts": `sections/nr-home-visual-proof.liquid`

This is now the page's one dark moment.

- **Problem words:** Trafikfilm, Asfalt, Flygrost, Foam, Handtvätt, Skydd, Glas and Däck form an ARIA tablist styled as an underlined index, not pills. On phones it scrolls sideways.
- **Each state changes the whole stage.** The stage shows the real in-use clip in this order:
  1. block video (Revolt: `revoltförstavideo.mov`);
  2. otherwise the product's own `pdp.demo_media` clip;
  3. otherwise a studio composition with the problem word set large behind the bottle (DeepDegrease and Clarity have no clip).
- **Packshot:** always the real image. With a clip it sits on a light plate in front of the footage. `mix-blend-mode: multiply` makes white or transparent packshots read as objects.
- **Story order:** problem, name, one line, three points, price, "Se <produkt> →", routine builder, optional helper link.
- **Motion:** the stage settles and the story rises in 260–300 ms. Under `prefers-reduced-motion` there is no motion.

### 2. Routine builder: `snippets/nr-routine.liquid` + `initRoutines()` in `assets/nr-homepage.js`

It sits inline under the selected product and shows at most two options:
- one add-on with an inline "Lägg till" (Ajax Cart API, announced with Shopify's `CartLinesUpdateEvent`, the same as the theme's product forms);
- one real kit with its price, its separate value and the saving. The separate value comes from `nr-ks-separate`: current component prices minus the active Revolt + brush discount, never compare-at.

The cart is read once (`/cart.js`) when the section approaches, and again after every add:
- An add-on already in the cart is not offered again.
- If the kit is already in the cart, the block hides.
- If Revolt and the brush are both in the cart, the Fälg Startkit row says "De här två finns redan som färdigt kit."
- If the main product is already in the cart, the kit row says the kit contains it.

Nothing is swapped or removed automatically. If an add fails, the shopper sees an inline message and the button re-enables.

| Product | Add-on | Kit (price · separate value · saving) |
|---|---|---|
| Alkastrike | DeepDegrease | Exteriör Startkit 429 · 497 · 68 |
| DeepDegrease | Alkastrike | Exteriör Startkit |
| Revolt | Mikrofiber Fälgborste | Fälg Startkit 309 · 321,30 · 12,30 (after the active 30 % brush discount) |
| Foamtastic | Foam Cannon | Foam Wash Kit 469 · 568 · 99 |
| Pure Shampoo | Washpad | Exteriör Startkit |
| GlossCoat | Mikrofiberduk (1 st, 49 kr) | Exteriör Komplett 1 199 · 1 382 · 183, labelled "Om du ska köpa flera steg" |
| Clarity | Glass Towel | Stort Interiör Startkit 549 · 674 · 125 |
| Pristine | Däckapplikator | Fälg & Däck Komplett 499 · 550,30 · 51,30 |

### 3. Kits: `sections/nr-home-kit-chooser.liquid`

There are three environments instead of three equal cards:
- **Grunden:** light, with a packshot.
- **Foam setup:** the real `foambanner1.mov` loop as the environment.
- **Hela rutinen:** dark, with all eight products on a two-level shelf.

The Komplett panel is the tall right column on desktop. Each kit shows role, name, who it is for, count, price, separate value, saving and CTA. "Visa vad som ingår" opens a horizontal strip of the components (image, name, size, `pdp.type_label`).

### 4. Categories: `sections/nr-home-categories.liquid`

These are now portals: one dominant portal and two stacked, real photos full bleed, and the name, one line and "Utforska →" on a scrim. HEIC originals are served as progressive JPEG.

### System and analytics

- **Shared tokens:** `--nr-save` and `--nr-save-on-dark` in `nr-homepage.css`. One 4 px radius throughout. One section eyebrow (the advisor).
- **Analytics:** `nr-homepage.js` now publishes `nr_*` custom events through `Shopify.analytics.publish`, as the product pages do: `dirt_advisor_select`, `dirt_advisor_product_click`, `routine_addon_click`, `routine_kit_click`, `kit_section_click` and `category_portal_click`.

### QA

QA used the local harness plus a mock `/cart.js` and `/cart/add.js` server (`mock-cart-server.py`). Widths tested: 320, 375, 390, 430, 768, 1024, 1366, 1440 and 1920.

- **Rendering:** all 8 states show the correct product, price, CTA, add-on and kit. There is no horizontal scroll and nothing clips at any width.
- **Cart:** six cart scenarios and the error path pass.
- **Page length:** desktop is 91 px shorter than before. Mobile is 111 px longer (1.8 %); that space holds the whole routine builder.

Screens are in `screens/v2-*.png`.

## Produktguide – "Rätt produkt för rätt typ av smuts" (2026-10-04)

`sections/nr-home-visual-proof.liquid` (editor name **NR: Produktguide**) replaces the dark problem index with a mini product advisor.

- **Chips:** an ARIA tablist with one block per kind of dirt. Arrow keys, Home and End work, and focus rings are visible. On desktop the chips wrap. On phones they scroll sideways in one row with an edge fade, and the selected chip is scrolled into view.
- **Panels:** all panels are rendered on the server from the block's product reference, so name, price, image and URL come from the product and never go stale. Switching only toggles `hidden`, with a 220 ms fade and an 8 px rise; prefers-reduced-motion turns this off. The logic is `initAdvisor()` in `assets/nr-homepage.js`.
- **Layout:** desktop is 55/45, visual and content. Phones show the visual (16:10) and then the content.
- **Content order:** problem → name → value line → 3 points → price → `SE PRODUKTEN →` → next step → optional helper link.
- **Fallbacks per block:** the text falls back to `pdp.value_line`, the points to `pdp.benefits`, and the image to the product image. An optional in-use video replaces the image and keeps the packshot in the corner (Revolt and Foamtastic use real clips).
- **Next step (real products, prices from the reference):**
  - Alkastrike and DeepDegrease → Exteriör Startkit
  - Revolt → Fälg startkit
  - Foamtastic → Foam Wash Kit
  - Pure → Washpad
  - GlossCoat → Mikrofiberduk
  - Clarity → Glass Towel
  - Pristine → Däckapplikator
- **Helper link:** shown only on the two degreaser panels. "Osäker på vilken avfettning du behöver?" links to the comparison anchor `#vilken-avfettning` on that product's page.
- **QA:** `advisor-qa.js` clicks every chip at 320/375/390/430/768/1024/1366/1920. At every width exactly one panel is visible, aria-selected/controls match, the price and next step are correct, nothing overflows, there is no horizontal page scroll, keyboard navigation works and there are no JS errors. Screens are in `screens/advisor-*.png`.
