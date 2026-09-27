# Standard PDP system – architecture (Phase 2)

One template, `templates/product.standard.json`, serves every standard product. Product-specific content comes from **product metafields** (namespace `pdp`) and **product references**, not from per-product templates. Every section hides itself when its data is empty, so a towel automatically gets a shorter page than a chemical. Kits keep their own `product.kit-*` system.

## Page order

| # | Module | File | Data source |
|---|---|---|---|
| 01 | Hero, left: gallery | Horizon `_product-media-gallery` (carousel; "1 / N" counter on mobile) | product media |
| 01 | Hero, right: trust line → name → type → value line | `blocks/nr-pdp-intro.liquid` | title, `pdp.type_label`, `pdp.value_line`, theme settings (Trustpilot) |
| 01 | Price | Horizon `price` (real Shopify price, no fake compare-at) | variant |
| 01 | 3 benefits | `blocks/nr-pdp-benefits.liquid` | `pdp.benefits` |
| 01 | Key facts (accessories: size, compatibility…) | `blocks/nr-pdp-facts.liquid` | `pdp.key_facts` |
| 01 | Variant picker, add to cart | Horizon `variant-picker`, `buy-buttons` (existing AJAX cart) | – |
| 01 | Delivery, returns, payment icons | `blocks/nr-pdp-delivery.liquid` | theme settings *Frakt & leverans* (`free_shipping_threshold`, `delivery_time_text`), `shop.enabled_payment_types` |
| 02 | Kit upgrade | `blocks/nr-pdp-kit-upgrade.liquid` | `pdp.kit_upgrade` → kit's own `custom.kit_components`, price; saving via `snippets/nr-kit-separate-total` |
| 03 | Demo media | `sections/nr-pdp-demo.liquid` | `pdp.demo_media`, `pdp.demo_heading` |
| 04 | When to use + comparison + level-2 quote | `sections/nr-pdp-when.liquid` | `pdp.problems`, `pdp.compare_with`, `pdp.best_for` (on both products), `pdp.compare_heading`, `pdp.compare_note`, metaobject `nr_trustpilot_review` |
| 05 | How to use, dilution, warning | `sections/nr-pdp-how.liquid` | `pdp.steps`, `pdp.dilution`, `pdp.usage_note`, `pdp.safety_note` |
| 06 | In the wash routine | `sections/nr-pdp-routine.liquid` | the section's own 4 stage product lists (one place for the whole store), `pdp.routine_note` |
| 07 | Goes well with (max 3) | `sections/nr-pdp-accessories.liquid` | `pdp.accessories` + `pdp.accessory_reasons` (same order) |
| – | *(future product reviews go here, as their own section)* | – | – |
| 08 | Trustpilot (brand level) | `sections/nr-pdp-trust.liquid` | theme settings *NordicReflection – Trustpilot*, metaobject `nr_trustpilot_review` (reviews mentioning the product first) |
| 09–10 | Technical info, full description (SEO), FAQ + FAQPage JSON-LD | `sections/nr-pdp-details.liquid` | `pdp.specs`, `product.description`, `pdp.faq` |
| – | Sticky add to cart | Horizon `sticky-add-to-cart` (built in) + CSS in `nr-pdp.css` | – |

The final purchase CTA (module 11) is Horizon's sticky add-to-cart bar, so no extra section was added.

**Styles and script**
- `assets/nr-pdp.css` is loaded only by these blocks and sections.
- `assets/nr-pdp.js` (about 2 KB, no dependencies) sends the custom analytics events and adds a subtle entrance animation.

## Product data model

Namespace `pdp`, owner PRODUCT. The 23 definitions are visible under *Settings → Custom data → Products* with the prefix "PDP –".

Multi-line fields use one item per line: `Rubrik | Text`.

| Key | Type | Used by |
|---|---|---|
| preset | single_line (choices: kemikalie, tillbehor, duk, verktyg) | heading variants (e.g. "När ska du använda…" vs "Vad använder du … till?") |
| type_label | single_line | hero |
| value_line | single_line | hero |
| benefits | list.single_line (max 3) | hero |
| key_facts | multi_line | hero (accessories) |
| problems | multi_line | 04 |
| compare_with | product_reference | 04 |
| compare_heading, compare_note | single_line | 04 |
| best_for | list.single_line | 04 (read from both products) |
| demo_heading | single_line | 03 |
| demo_media | list.file_reference | 03 |
| steps, dilution | multi_line | 05 |
| usage_note, safety_note | single_line | 05 |
| routine_note | single_line | 06 |
| kit_upgrade | product_reference | 02 |
| kit_heading | single_line | 02 |
| accessories | list.product_reference (max 3) | 07 |
| accessory_reasons | list.single_line (max 3) | 07 |
| specs, faq | multi_line | 09–10 |

**Metaobject `nr_trustpilot_review`**
- Fields: author, rating, title, body (verbatim), date, mentions (list of products).
- Holds 5 reviews, copied verbatim from the content already used on the kit pages.
- It is the single source for Trustpilot quotes on every PDP.

**Theme settings group "NordicReflection – Trustpilot"**
- `nr_trustpilot_rating` (4.7)
- `nr_trustpilot_count` (34)
- `nr_trustpilot_url`

**Existing group "Frakt & leverans"**
- `free_shipping_threshold` (799)
- `delivery_time_text`

### Rules that prevent wrong pairings

- Every related product, kit or routine product is a Shopify product reference. Name, image, price and URL are always read from that one object; no title or price is typed next to a reference.
- The kit saving is computed from the kit's component variants. The compare-at price is never used.
- Trustpilot is always labelled as reviews of NordicReflection. Judge.me product ratings are not rendered on this template.
- The FAQ structured data is generated from the same `pdp.faq` lines as the visible FAQ.

## Analytics

`nr-pdp.js` publishes custom events via `Shopify.analytics.publish`:
- `nr_kit_upgrade_click`
- `nr_cross_sell_click`
- `nr_trustpilot_click`
- `nr_video_play`
- `nr_gallery_interaction`
- `nr_sticky_atc_click`

`product_viewed` and `product_added_to_cart` are Shopify's standard events and are not duplicated. Any existing GA4, Meta or TikTok pixel can subscribe to the custom events; nothing new was installed.

## Rollout

1. Fill a product's `pdp.*` metafields. They are invisible on live until the product uses the template.
2. Preview it with `?view=standard&preview_theme_id=<theme>`.
3. When the theme containing `product.standard.json` is published, switch the product's template to "standard". The old `product.<name>.json` templates can then be deleted.

**Do not switch a product's template before the theme with `product.standard.json` is live.** The live theme doesn't have the template yet, and the product would fall back to the default template.
