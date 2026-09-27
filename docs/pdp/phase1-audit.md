# Standard PDP system – Phase 1 audit

Audited 2026-09-27 against the live theme **205344604494 "Navigation + footer (preview)"** (MAIN) and live Shopify product data. No edits were made.

Sources:
- the 21 live product templates (checksums matched live);
- product data, SEO, variants, media and metafields for every active product;
- the kit contents (`custom.kit_components`, `custom.separate_components`);
- uploaded video files.

Not verified:
- **Images and video content.** The sandbox cannot reach cdn.shopify.com, so media was not viewed; findings come from file names, counts, dimensions and where each file is used.
- **The Trustpilot page** could not be reached. The rating used below (4.7/5, 34 reviews) is the figure already on the kit PDPs and in the footer, and it must be re-checked before launch.

## 1. Scope

31 active products:
- **23 standard products:** 9 chemicals, 14 accessories. These are in scope.
- **8 kits:** they use the Kit PDP system (`product.kit-*`) and are out of scope.

| # | Product | Handle | Group | Price | Template |
|---|---|---|---|---|---|
| 1 | Revolt – Flygrostborttagare | revolt-flygrostborttagare | Chemical | 189 kr | product.revolt |
| 2 | Alkastrike – Alkalisk Avfettning | alkastrike-alkalisk-avfettning | Chemical | 149 kr | product.alkastrike |
| 3 | Foamtastic – Snow Foam för effektiv förtvätt | foamtastic-hogkoncentrerat-snow-foam | Chemical | 169 kr | product.foamtastic |
| 4 | DeepDegrease – Kallavfettning | deepdegrease-kallavfettning | Chemical | 169 kr | product.deepdegrease |
| 5 | Pure Shampoo – Bilschampo | pure-shampoo-ph-neutralt-bilschampo | Chemical | 179 kr | product.pureshampoo |
| 6 | GlossCoat – Sprayförsegling | glosscoat-hydrofobisk-sprayforsegling | Chemical | 189 kr | product.glosscoat |
| 7 | Clarity – Glasrengöring | clarity-glasrengoring | Chemical | 149 kr | product.clarity |
| 8 | Pristine - Däck- & Plastförnyare | pristine-dack-plastfornyare | Chemical | 189 kr | product.pristine |
| 9 | Core APC – Allrengöring (APC) | core-apc-allrengoring | Chemical | 159 kr | product.coreapc |
| 10 | Foam Cannon | foam-lance-skumlans | Tool | 399 kr | product.foamlance |
| 11 | Tryckspruta | tryckspruta-2l-kemikalieresistent | Tool | 299 kr | product.tryckspruta |
| 12 | Tvätthink | tvatthink-20l-grit-guard | Tool | 299 kr | product.tvatthink |
| 13 | Washpad | wash-pad-mikrofiber | Accessory | 149 kr | product.washpad |
| 14 | Scrub Pad | scrub-pad-interior | Accessory | 39 kr | product.scrubpad |
| 15 | Däckapplikator | dackapplikator | Accessory | 40 kr | product.dackapplikator |
| 16 | Mikrofiber Fälgborste | mikrofiber-falgborste | Tool | 189 kr | product.falgborste |
| 17 | DeepReach Wheel Brush | deepreach-wheel-brush | Tool | 169 kr | **product (default)** |
| 18 | Detail Brush Duo – 2-pack | detail-brush | Tool | 139 kr | **product (default)** |
| 19 | Torkduk 70x90 - 1400 GSM | torkduk-70x90-1400gsm | Towel | 329 kr | product.torkduk-70x90 |
| 20 | Torkduk 50x80 - 1400 GSM | torkduk-50x80-1400gsm | Towel | 229 kr | product.torkduk-50x80 |
| 21 | Torkduk 40x40 - 1400 GSM | torkduk-40x40-1400gsm | Towel | 149 kr | product.torkduk-40x40 |
| 22 | Mikrofiberduk (1 / 5 / 10) | mikrofiberduk | Towel | 49 / 119 / 199 kr | product.mikrofiberduk |
| 23 | Glass Towel – Glasduk | glass-towel-glasduk | Towel | 69 kr | **product (default)** |

Pricing:
- No product has a compare-at price, and no page shows sale styling.
- All prices come from the Shopify price block.
- No incorrect prices were found.

The 8 kits and their prices:
- Fälg startkit 309 kr
- Fälg Och Däck Komplett Kit 499 kr
- Foam Wash Kit 469 kr
- Exteriör Startkit 429 kr
- Exteriör Komplett Kit 1 199 kr
- Litet interiör Startkit 259 kr
- Mellan interiör Startkit 369 kr
- Stort interiör Startkit 549 kr

## 2. Page-by-page table

"Hero" is the value line shown under the title today (the `short_value_proposition` metafield, or the template fallback). "Media" lists gallery images, plus videos placed in page sections. No product has a video inside its gallery.

| Product | Hero message today | Media | Recommendations today | Kit shown today | Major problems | Data confidence |
|---|---|---|---|---|---|---|
| Revolt | "Löser upp flygrost och bromsdamm på fälgen så att det enkelt kan spolas bort." | 3 img (2 named `ChatGPT_Image_…`) + 2 section videos (revolthemsida, revoltförstavideo) + 1 image (IMG_0441) in a disabled section | Cross-sell: Mikrofiber Fälgborste. Recommended section disabled | None | **Contradictions.** The visible FAQ says the product turns purple; the FAQ JSON-LD says no colour reaction is confirmed; the description says purple. The description and SEO say "pH-neutral" and "lack, fälgar"; the page says pH 6–8 and wheels only. Active ingredient and pH sit in the hero. The same sentence appears 3× above the fold. Two gallery images look AI-generated. DeepReach Wheel Brush, Pristine and Fälg startkit are not linked | **Low**: core claims conflict |
| Alkastrike | "Löser trafikfilm, insekter och organisk smuts före kontaktvätten." | 1 img + 1 section video (alkaliskhemsida). `result_video` metafield set but the section is disabled | Cross-sell: Tryckspruta; 4 tiles (Tryckspruta, DeepDegrease, Foamtastic, Pure) | None | **No FAQ at all** (section disabled). No surfaces or tech info. Dilution "upp till 1:25" exists only in SEO/description and is never shown. 8 of 15 sections disabled. No DeepDegrease comparison on this side | Medium |
| Foamtastic | "Tjockt, vidhäftande skum som löser upp smuts innan handtvätten." | 2 img + 2 section videos (foamhemsida, foambanner1) | Cross-sell: "Komplettera med **Foam Lance**", which points at a product titled **Foam Cannon** | None (Foam Wash Kit exists) | Cross-sell heading does not match the product's title. The FAQ says "Ingen specifik spädningsgrad är angiven på denna sida" (dilution unknown). No "Foamtastic vs Pure Shampoo" comparison. Foam Wash Kit not offered | Medium |
| DeepDegrease | "Löser upp asfalt, tjära och petroleumbaserad smuts – före handtvätten." | 1 img, **no video** | Comparison block → Alkastrike; tiles: Alkastrike, Mikrofiberduk, Torkduk 50x80, Tryckspruta | None | Recommends Tryckspruta for a solvent product without verified solvent compatibility. Recommends a 1400 GSM drying towel for wiping off tar. Safety (H226) block in the hero. "Motorrum och hjulhus" use not verified. The comparison is only on this page, not on Alkastrike | Medium |
| Pure Shampoo | "Skonsamt mot vax och keramiska lackskydd – ändå kraftfullt mot smuts och vägfilm." | 1 img + 1 section video (schampoooooo). Unused: pureschampoo.mov, schampootest.mov | Cross-sell: "Tvätthink **20 L Grit Guard**" (product title is "Tvätthink") | None | **Says "pH-neutralt (pH 8–9)"**, a contradiction (pH 8–9 is mildly alkaline). pH is in the hero. The FAQ points to an "Avsedda användningsområden" section that is disabled. The FAQ JSON-LD has 4 questions against 8 visible. Washpad and Torkduk not linked | **Low** on the pH claim |
| GlossCoat | "Djup glans. Kraftig vattenavrinning. På några minuter." | 1 img + 2 section videos (glosscoattttt, avrinning) | Cross-sell: Mikrofiberduk. Recommended disabled | None | Hero bullets are chemistry-first ("✓ Hydrofobisk effekt"). Durability ("slitstarkt skydd") is not verified. The FAQ points to a disabled surfaces section. 2 metafield definitions have whole marketing sentences as keys (junk). Only kit containing it: Exteriör Komplett | Medium |
| Clarity | "Kristallklart glas utan ränder – med en ren och vattenavvisande finish." | 1 img, **no video** | 4 tiles: Mikrofiberduk, Torkduk 40x40, Core APC, GlossCoat. **Glass Towel is not recommended** | None | **No "how to use"** (section disabled); usage areas disabled. Water-repellent claim appears only in category and value prop, not in the description. "Säker på tonade rutor" is only in SEO. The FAQ points to disabled sections. FAQ JSON-LD differs from the visible FAQ (3 vs 6 questions) | **Low** on claims |
| Pristine | "Djupare färg. Jämn finish. Aldrig överdrivet blank." | 1 img + 1 section video (pristine) + before/after slider (IMG_0389/IMG_0391) | Kit block titled "**Wheel & Tyre Kit**" pointing at "Fälg Och Däck Komplett Kit"; cross-sell: Däckapplikator | Yes (hardcoded name) | Kit block heading does not match the kit's title, and component products are hardcoded 4× in settings. The UV-protection claim is not verified. pH 6–7 (from the SDS) sits in the FAQ, which is fine | Medium |
| Core APC | Full product title shown as H2; value line: "Koncentrerad allrengöring för smuts, fett och fläckar – invändigt och utvändigt." | 1 img + 1 section video (coreapc) | Cross-sell: "Scrub Pad **Interior**" (title is "Scrub Pad") | None (3 interior kits contain it) | **Judge.me product rating badge in the hero** (5.0 from 2 reviews): real data, but it breaks the "brand-level trust only" rule. Kits describe it as interior-only; the PDP claims interior, exterior and engine bay. No dilution values | Medium |
| Foam Cannon | "Tjockt, jämnt skum som minskar risken för tvättrepor redan i förtvätten." | 1 img, **no video** | None | None (Foam Wash Kit exists) | **No pressure-washer compatibility, connection or adapter info anywhere.** The one FAQ answer says "kontrollera anslutningen". Naming is mixed: title "Foam Cannon"; handle, SEO and hero say "Foam lance / skumlans". No Foamtastic link | **Low** (critical info missing) |
| Tryckspruta | "Snabb och jämn applicering av bilvårdsprodukter med utbytbara munstycken." | 1 img, no video | None | None | Which chemicals it may hold is unverified (it is recommended for solvent-based DeepDegrease). No pressure or usage info. Title "Tryckspruta"; 2 L appears only in the handle, SEO and description | Medium |
| Tvätthink | "Håll smutsen på botten – inte i tvätthandsken." | 1 img + 1 section video (hinkgridlockfinal) | Recommended disabled | None | 20 L only in the handle and SEO; no dimensions. No link to Pure Shampoo or Washpad | Medium |
| Washpad | "Mjuk premium-mikrofiber som skyddar lacken vid varje handtvätt." | 2 img + 1 section video (washpad) | None | None | Name varies ("Washpad" vs "Wash Pad"). No size. No link to Pure Shampoo or Tvätthink | Medium |
| Scrub Pad | "Effektiv rengöring av ingrodd smuts på läder, plast, vinyl, gummi och textil." | 3 img, no video | Tiles: Core APC, Mikrofiberduk | None (interior kits contain it) | Leather is claimed here, but Core APC's surfaces do not list leather. No size or material | Medium |
| Däckapplikator | "Jämn och kontrollerad applicering utan onödigt kladd." | 1 img, no video | Tiles: Pristine, Mikrofiberduk | None (Fälg & Däck Komplett contains it) | Fine; kit not offered | High |
| Mikrofiber Fälgborste | "Skonsam och effektiv rengöring även mellan ekrar och bakom fälgen." | 1 img + 1 section video (fälgborste mikrofiber) | None | None (Fälg startkit contains it) | No Revolt link, no kit | High (size 36 × 4.5 cm verified in the description) |
| DeepReach Wheel Brush | Product title only (default template) | 1 img | Shopify auto "Passar bra ihop med" | None | **Default Horizon template:** apparel accordions "Material / Skötselråd / Passform", "Fri retur" claim, no value line. No dimensions. No SEO title or description | Low |
| Detail Brush Duo | Product title only (default template) | 1 img | Shopify auto | None (Mellan/Stort interiör contain it) | Default template (same issues as DeepReach). No dimensions or bristle material. No SEO | Low |
| Torkduk 70x90 | "Torkar hela bilen snabbt och skonsamt utan ränder." | 2 img, **2nd image (IMG_9793.jpg) is the same file as on Torkduk 50x80**. No video | Tiles: GlossCoat, Clarity, Pure, Torkduk 40x40 | None | **GSM conflict:** title says 1400 GSM; description says "hela 1300 GSM". The Clarity tile copy "Randfritt glas med samma mjuka mikrofiber" doesn't fit Clarity. The GlossCoat tile "Applicera enkelt med torkduken" (applying sealant with a drying towel) is not verified | **Low** (GSM) |
| Torkduk 50x80 | "…" (similar template) | 2 img (shares IMG_9793.jpg with 70x90) | Same 4 tiles and copy as 70x90 | None | Shared image may show the wrong size. Same tile-copy problems | Medium |
| Torkduk 40x40 | "Precision för lack, glas och detaljer – utan repor." | 2 img (IMG_9792) | Same pattern | None | Same tile-copy problems. "Utan repor" is an absolute claim | Medium |
| Mikrofiberduk | "Mångsidig mikrofiberduk för hela bilvården." | 4 img, no video | 4 tiles: Clarity, Core APC, GlossCoat, Pure | None (interior kits contain the 5-pack) | Variant names are bare "1 / 5 / 10" (no "-pack"). No size or GSM | Medium |
| Glass Towel | Product title only (default template) | 1 img | Shopify auto | None (Stort interiör contains it) | Default template. Not linked from Clarity even though the description pairs it with Clarity. No size or GSM. No SEO | Low |

## 3. Cross-cutting findings

**Architecture**
- **21 hand-built templates** (48–131 KB each, about 1.7 MB in total). Each one repeats the same sections with hardcoded copy in theme JSON, and 3 products fall back to the stock Horizon template.
  - 5–8 disabled leftover sections per chemical template (`result_video`, `before_after`, `why_*`, `tech_specs`, `recommended`, `final_cta`, `system`, `surfaces`).
  - Unused templates: `product.instant-*` (×3), `product.instant-backup-product`, `product.zztest`, `product.kit-test`, and `product.kit` (a duplicate of `product.kit-exteriorkomplett`).
- **Product data is not the source of truth.** Titles in hero, cross-sell headings and kit headings are typed by hand, separately from the referenced product. The existing product-reference fields prove this is how the wrong-name bugs happen:
  - "Komplettera med **Foam Lance**" → the product is **Foam Cannon**
  - "Tvätthink **20 L Grit Guard**" → **Tvätthink**
  - "Scrub Pad **Interior**" → **Scrub Pad**
  - "**Wheel & Tyre Kit**" → **Fälg Och Däck Komplett Kit**
  - Pristine's kit block stores its 4 component products by hand in settings, although `custom.kit_components` already holds them.
- **Metafields exist but are mostly empty.**
  - Only 2 of 23 products have `short_value_proposition` (Alkastrike, Pure Shampoo) and 9 have `product_category`; the templates carry fallback copy instead.
  - `dilution_*`, `dwell_time`, `suitable_surfaces`, `safety_notes`, `storage`, `safety_data_sheet`, `product_label`: set on at most one product (Core APC has `suitable_surfaces`).
  - Two junk definitions (`custom.glosscoat_ar_en_snabb_…`, `custom.revolt_ar_en_ph_neutral_…`) should be deleted.
- **Kit contents:** 7 of 8 kits store their contents in `custom.kit_components` (variant references). Only Exteriör Komplett Kit has `custom.separate_components`. Kit upgrades can be computed from `kit_components` (the approach used in the mega menu).

**Trust**
- **No PDP has Trustpilot proof.**
- **Judge.me product ratings exist:** Revolt 5.0 (1), Pristine 5.0 (1), Core APC 5.0 (2). Core APC shows the Judge.me badge in its hero. That is real data, but it is product-level and inconsistent with the rest. **Decision needed** (see §8).
- **Reusable Trustpilot content** already exists in the kit templates (`ai_gen_block_f9f7e7d`): 4.7/5, 34 reviews, several verbatim reviews.
  - One review mentions "flygrostborttagare" and "alkalisk avfettning", so it can be prioritised on Revolt and Alkastrike.
  - The rating and count must be re-checked against Trustpilot before launch.

**Shipping and returns**
- The same copy is hardcoded in all 20 custom templates: "Standardfrakt 49 kr. Fri frakt över 799 kr.", "Normal leveranstid 1–3 arbetsdagar. Order skickas normalt senast nästa vardag.", "14 dagars ångerrätt". The hero also carries "Snabb leverans från Sverige / Säkra betalningsalternativ / 14 dagars ångerrätt".
- The default template (DeepReach, Detail Brush, Glass Towel) says **"Fri retur"**. That is not stated anywhere else and is probably wrong.
- There is no single global source for the 799 kr threshold. The header announcement, footer and kits each hold their own copy.

**Technical info appears too early**
- Revolt: active ingredient and pH in the hero.
- Pure Shampoo: pH in the hero.
- GlossCoat: "Hydrofobisk effekt".
- DeepDegrease: H226 in the hero. It must stay on the page, but lower, with a short notice kept near the buy button.
- Category labels such as "Kallavfettning (lösningsmedelsbaserad)".

**Duplicated content**
- Every chemical hero shows value line, short description and 3–4 bullets that restate the same sentence before the price.
- Delivery info appears twice: the hero row and a full section.
- The FAQ often repeats the hero ("Vad är X?").

**FAQ problems**
- **Structured data disagrees with visible text:**
  - Revolt: colour reaction yes vs no.
  - Clarity: different question sets.
  - Pure Shampoo: 4 vs 8 questions.
- **Visible FAQs point at sections that are switched off:**
  - Pure Shampoo and GlossCoat: "Avsedda användningsområden ovan".
  - Clarity: "avsnittet om invändigt och utvändigt glas ovan" and "produktbeskrivningen ovan".
- Alkastrike has no FAQ.

**Layout inconsistencies**
- The "NordicReflection" eyebrow appears on some products only.
- Core APC uses the full product title; others use a short name.
- Info blocks appear only on Clarity, DeepDegrease and GlossCoat.
- Two of the kit-upgrade styles differ.
- Every PDP has sticky add-to-cart enabled and a carousel gallery with dots on mobile.

**Product names are inconsistent**
- "Pristine - " (hyphen) vs "–" elsewhere.
- "Fälg Och Däck Komplett Kit" capitalisation.
- "Washpad" vs "Wash Pad".
- "Foam Cannon" vs "Foam Lance".
- `productType` is empty on all standard products.

**Missing alt text**
- 19 of 23 standard products have empty alt text on all their gallery images.

## 4. Recommendation audit

| Product | Today | Problem |
|---|---|---|
| Revolt | Mikrofiber Fälgborste | Misses DeepReach Wheel Brush, Pristine, Däckapplikator and Fälg startkit |
| Alkastrike | Tryckspruta (twice: cross-sell and tile), DeepDegrease, Foamtastic, Pure | Duplicate Tryckspruta; four tiles is too many |
| Foamtastic | "Foam Lance" (= Foam Cannon) | Name mismatch; Pure Shampoo and Foam Wash Kit missing |
| DeepDegrease | Alkastrike, Mikrofiberduk, Torkduk 50x80, Tryckspruta | Sprayer and drying towel not appropriate or not verified for a solvent product |
| Pure Shampoo | Tvätthink | Name mismatch; Washpad and Torkduk missing |
| GlossCoat | Mikrofiberduk | OK; could add Torkduk 40x40 (it already mentions buffing sealants) |
| Clarity | Mikrofiberduk, Torkduk 40x40, Core APC, GlossCoat | **Glass Towel missing**; Core APC and GlossCoat not relevant |
| Pristine | Däckapplikator + "Wheel & Tyre Kit" | Kit name mismatch; kit components hardcoded |
| Core APC | Scrub Pad | Name mismatch; Detail Brush and Mikrofiberduk missing |
| Foam Cannon | – | Foamtastic missing (critical: the pair only works together) |
| Tryckspruta | – | Alkastrike missing |
| Tvätthink | – | Pure Shampoo and Washpad missing |
| Washpad | – | Pure Shampoo and Tvätthink missing |
| Torkdukar ×3 | GlossCoat, Clarity, Pure, other towel | Tile copy wrong for Clarity; GlossCoat claim unverified |
| Mikrofiberduk | Clarity, Core APC, GlossCoat, Pure | Generic |
| Default-template trio | Shopify automatic recommendations | Uncurated |

## 5. Proposed mappings (validated against catalogue and kit contents)

The kit saving is computed from current prices: the sum of the components' variant prices minus the kit price. Do not hardcode these numbers. Where no kit fits, none is shown.

| Product | Primary kit upgrade | Kit saving today | Accessories (max 3) |
|---|---|---|---|
| Revolt | Fälg startkit (Revolt + Mikrofiber Fälgborste) | 378 → 309, saves 69 kr | DeepReach Wheel Brush · Pristine · Däckapplikator |
| Alkastrike | Exteriör Startkit (DeepDegrease + Alkastrike + Pure) | 497 → 429, saves 68 kr | Tryckspruta · DeepDegrease · Foamtastic |
| Foamtastic | Foam Wash Kit (Foamtastic + Foam Cannon) | 568 → 469, saves 99 kr | Foam Cannon · Pure Shampoo |
| DeepDegrease | Exteriör Startkit | saves 68 kr | Alkastrike · Mikrofiberduk (not Torkduk; Tryckspruta only if solvent-safe) |
| Pure Shampoo | Exteriör Startkit | saves 68 kr | Washpad · Tvätthink · Torkduk 70x90 |
| GlossCoat | Exteriör Komplett Kit (only kit containing it) | 1 382 → 1 199, saves 183 kr | Mikrofiberduk · Torkduk 40x40 · Pure Shampoo |
| Clarity | Stort interiör Startkit (contains Clarity + Glass Towel) | 674 → 549, saves 125 kr | **Glass Towel** · Mikrofiberduk |
| Pristine | Fälg Och Däck Komplett Kit | 607 → 499, saves 108 kr | Däckapplikator · Revolt |
| Core APC | Litet interiör Startkit (Core APC + Scrub Pad + Mikrofiberduk 5-pack); Mellan as an alternative | 317 → 259, saves 58 kr | Scrub Pad · Detail Brush Duo · Mikrofiberduk |
| Foam Cannon | Foam Wash Kit | saves 99 kr | Foamtastic |
| Mikrofiber Fälgborste | Fälg startkit | saves 69 kr | Revolt · DeepReach Wheel Brush |
| Däckapplikator | Fälg Och Däck Komplett Kit | saves 108 kr | Pristine |
| Scrub Pad | Litet interiör Startkit | saves 58 kr | Core APC · Detail Brush Duo |
| Detail Brush Duo | Mellan interiör Startkit | 456 → 369, saves 87 kr | Core APC · Scrub Pad |
| Glass Towel | Stort interiör Startkit | saves 125 kr | Clarity |
| Mikrofiberduk | Litet interiör Startkit (contains the 5-pack) | saves 58 kr | Core APC · Clarity · GlossCoat |
| DeepReach Wheel Brush | none (not in any kit) | – | Revolt · Mikrofiber Fälgborste |
| Tryckspruta | none | – | Alkastrike (+ Core APC if confirmed) |
| Tvätthink | none | – | Pure Shampoo · Washpad |
| Washpad | none | – | Pure Shampoo · Tvätthink · Torkduk 70x90 |
| Torkduk 70x90 / 50x80 | none | – | Pure Shampoo · Torkduk 40x40 |
| Torkduk 40x40 | none | – | GlossCoat · Torkduk 70x90 |

## 6. Media inventory and production backlog

Gallery images are counted per product. "Section video" means a video file placed in a page section (outside the gallery). None of the media was viewed (CDN blocked), so descriptions come from file names only.

| Product | Images | Video | Most important missing media | Priority | Most important missing copy |
|---|---|---|---|---|---|
| Revolt | 3 (2 AI-named) | revolthemsida 29 s, revoltförstavideo 9 s | Visible reaction on a dirty wheel → rinse → clean wheel, in the gallery (if the existing videos show it, move them into the gallery) | **P0** | Confirmed colour-reaction statement; confirmed surfaces (wheels only vs paint); dwell time |
| Alkastrike | 1 | alkaliskhemsida 20 s | Lower panel with traffic film → apply → rinse | P1 | Verified dilution table (only "upp till 1:25" known); dwell time; surfaces |
| Foamtastic | 2 | foamhemsida 32 s, foambanner1 13 s | Car fully covered in foam, close-up of thickness, rinse | **P0** (may already exist in foamhemsida) | Dilution/dosage in cannon bottle |
| DeepDegrease | 1 | none | Tar spots on a lower panel → dissolve → wipe | **P0** | Dwell time; verified surfaces; whether a sprayer may hold it |
| Pure Shampoo | 1 | schampoooooo 47 s (+ unused pureschampoo 48 s, schampootest 1 s) | Washpad in bucket → lather on paint → rinse | P1 | Correct pH wording; dosage per bucket |
| GlossCoat | 1 | glosscoattttt 35 s, avrinning 8 s | Water behaviour (beading/sheeting) on a finished panel | **P0** (avrinning may already cover it) | Durability; verified surfaces; cure time |
| Clarity | 1 | none | Glass application → wipe → clear reflection | P1 | Tinted-glass safety confirmation; water-repellent claim (keep or remove) |
| Pristine | 1 | pristine 17 s + before/after stills | Before/after in the gallery | **P0** (stills exist) | UV claim verification |
| Core APC | 1 | coreapc 25 s | Dirty interior surface → spray → agitate → wipe (50/50) | P1 | Dilution per use; leather yes/no |
| Foam Cannon | 1 | none | Cannon on a pressure washer, connector close-up, foaming | **P0** | **Connector/thread type, included adapters, bottle volume, compatible washer brands** |
| Tryckspruta | 1 | none | Spraying a wheel/panel; nozzle modes | P1 | Chemical compatibility (solvent?), max pressure, seals |
| Tvätthink | 1 | hinkgridlockfinal 23 s | Two-bucket set-up in use | P2 | Dimensions; lid yes/no |
| Washpad | 2 | washpad 29 s | In hand on paint | P1 | Size |
| Scrub Pad | 3 | none | Interior use on a seat or plastic | P1 | Size, material, leather compatibility |
| Däckapplikator | 1 | none | Applying Pristine to a tyre | P1 | Size |
| Mikrofiber Fälgborste | 1 | fälgborste mikrofiber 28 s | (video exists) Reach behind spokes | P2 | – |
| DeepReach Wheel Brush | 1 | none | In a wheel barrel; length vs wheel | P1 | **Dimensions**, bristle material |
| Detail Brush Duo | 1 | none | Vents and emblems | P1 | Dimensions, bristle material |
| Torkduk 70x90 | 2 (one shared) | none | Drying a whole panel; absorption demo | P1 | **Correct GSM (1400 vs 1300)**; material |
| Torkduk 50x80 | 2 (one shared) | none | Own lifestyle image (not shared) | P1 | Material |
| Torkduk 40x40 | 2 | none | Buffing a detail | P2 | – |
| Mikrofiberduk | 4 | none | Texture close-up, pack sizes | P2 | Size, GSM |
| Glass Towel | 1 | none | On glass with Clarity; texture | P1 | Size, GSM |

Also P2: a rotating studio bottle video for each chemical.

## 7. Missing or conflicting product information (needs owner confirmation)

1. **Revolt colour reaction.** The visible FAQ and description say it turns purple; the FAQ JSON-LD says no reaction is confirmed. Which is true?
2. **Revolt pH and surfaces.** Description and SEO say "pH-neutral" and "lack, fälgar och andra exteriöra ytor"; the page says pH 6–8 and wheels only.
3. **Pure Shampoo pH.** It is called "pH-neutralt" and "pH 8–9" at the same time. Which statement is correct?
4. **Torkduk 70x90 GSM.** Title says 1400; description says 1300.
5. **Foam Cannon.** Connection and thread type, adapters included, bottle volume, and pressure-washer compatibility.
6. **Tryckspruta.** Is it approved for solvent-based DeepDegrease? Is it approved for Core APC?
7. **Dilutions.** Needed for Alkastrike (light/normal/heavy), Foamtastic (cannon), Pure Shampoo (per bucket) and Core APC (per use). All `dilution_*` metafields are empty.
8. **Dwell times.** Needed for Revolt, Alkastrike, DeepDegrease, Foamtastic and Core APC. None are verified.
9. **Volumes.** Revolt, Alkastrike, Pure Shampoo, Clarity and Pristine are 500 ml; Foamtastic and DeepDegrease are 1000 ml. This comes only from kit metaobjects and is not shown on the PDPs. GlossCoat and Core APC volumes are unknown.
10. **Clarity.** "Vattenavvisande finish" and "säker på tonade rutor": keep only if verified.
11. **Pristine.** The UV-protection claim.
12. **GlossCoat.** Durability, surfaces (plastic, rubber, wheels?) and cure time.
13. **Core APC.** Leather yes/no; exterior and engine-bay use (kits say interior only).
14. **Shipping policy.** Is it still 49 kr standard, free over 799 kr, 1–3 working days, shipped by the next working day? Is "Fri retur" on the default template false?
15. **Dimensions and material** for DeepReach, Detail Brush Duo, Glass Towel, Mikrofiberduk, Washpad, Scrub Pad, Tvätthink and Däckapplikator.
16. **Revolt gallery images named `ChatGPT_Image_…`.** Are these AI-generated product scenes? If they depict results, they must not be used as proof.

## 8. Decisions needed before Phase 3

- **Judge.me product ratings** (Revolt 1, Pristine 1, Core APC 2 reviews). Option (a): hide them on PDPs for now, and keep the slot for a future product-review module. Option (b): show them clearly as product reviews in that slot. They are real, but Core APC currently shows them in the hero next to where brand Trustpilot proof will sit.
- **Trustpilot count.** Is 34 reviews still current, and is 4.7 still current?
