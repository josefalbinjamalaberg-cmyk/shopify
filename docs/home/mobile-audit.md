# Homepage mobile audit (2026-10-04, live theme 205928595790)

Measured in the local harness (real section code and template, mocked
product data). Real page is longer: the brand-story image is a 1125 × 2436
portrait, which alone renders ~780 px tall at 390 px.

## Current order and height at 390 px

| # | Section | Height | Notes |
|---|---|---|---|
| 1 | Hero (video) | 557 | CTAs are two full-width buttons (secondary as heavy as primary) |
| 2 | Trust strip | 91 | 3 stacked icon+label columns |
| 3 | Hitta rätt paket (kits) | 1 242 | 3 full cards stacked: 1.5 screens before any single product |
| 4 | Bästsäljare | 573 | Theme product cards in a swipe row, long titles shortened by JS |
| 5 | Rätt produkt för rätt smuts (advisor, dark) | 1 230 | Product + add-on row + kit card + comparison link at once |
| 6 | Kundomdömen | 712 | Full review text in a swipe row |
| 7 | Handla efter område | 677 | Portals |
| 8 | Brand story | 1 074 (≈1 580 real) | Tall image, paragraph, 3 principles, button |
| | **Total** | **≈ 6 400 (≈ 6 900 real), 7.6 to 8.2 screens** | |

Flow is KIT → PRODUCTS → PROBLEM: the most complex decision (which kit)
comes before the visitor knows what they need.

## Per section

| Section | Verdict | What |
|---|---|---|
| Hero | KEEP + COMPRESS | Copy stays. Shorter on phones (≈ 470 px), primary button + secondary as text link. Video stays (no verified product-action clip that reads at hero size yet). |
| Trust strip | COMPRESS | One thin line: ★ 4,7/5 · Skickas nästa vardag · Fri frakt över 799 kr. |
| Advisor | REORDER (to #3) + REFINE | First shopping moment. Light background. On phones: chips, one visual, one product, one CTA, then one compact add-on row and a one-line kit link. Comparison link only from tablet up. |
| Kits | REORDER (to #4) + COMPRESS | Phones: one kit at a time, 86 vw scroll-snap cards with the next card peeking; image, role, name, who, count, price, saving, CTA. Component strip only on desktop. |
| Bästsäljare | REFINE | Phones: four compact rows (image, short name, problem line, price, +). Quick add for single-variant products. Desktop: 4 clean columns. No long titles. |
| Kundomdömen | REFINE + COMPRESS | Becomes the dark proof moment. 3 reviews, each a big real phrase (verbatim, only shown if it is in the review), stars, one natural sentence, name. |
| Categories | COMPRESS | Lower aspect ratios on phones so the three portals fit in about one screen. |
| Brand story | COMPRESS | Statement, three one-line principles, text link; image cropped 4:3; long paragraph from tablet up only. |
| Newsletter | KEEP AS IS | The homepage newsletter section is already disabled; capture is the popup + floating "Få 15%" button and the footer. Not changed in this task (popup is a global section). |
| shop_by_problem, demo, guides, results | REMOVE (already disabled) | Stay disabled. |

## Target

New order: Hero → Trust → Advisor → Kits → Bästsäljare → Omdömen →
Områden → Brand story. Goal: 15-25 % shorter on phones, without dropping
products, prices, kits or proof.

## Result (after this pass, harness, 390 px)

| Section | Before | After |
|---|---|---|
| Hero | 557 | 490 |
| Trust | 91 | 42 (one line) |
| Advisor (now #3) | 1 230 | 986 |
| Kits (now #4) | 1 242 | 627 (one kit per swipe) |
| Bästsäljare | 573 | 587 (rows with quick add, no carousel) |
| Omdömen (dark) | 712 | 409 |
| Områden | 677 | 558 |
| Brand story | 1 074 (≈1 580 real) | 559 |
| **Total** | **6 416 (7.6 screens)** | **4 517 (5.4 screens), −30 %** |

At 320, 375, 390 and 430 px: no horizontal scroll, no duplicate ids. Desktop
1366 px: 6 454 → 6 319 px, layout unchanged in kind.
