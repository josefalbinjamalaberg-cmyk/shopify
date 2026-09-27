# Graph Report - shopify  (2026-09-27)

## Corpus Check
- Corpus is ~36,558 words - fits in a single context window. You may not need a graph.

## Summary
- 113 nodes · 202 edges · 8 communities
- Extraction: 97% EXTRACTED · 2% INFERRED · 1% AMBIGUOUS · INFERRED: 4 edges (avg confidence: 0.85)
- Token cost: 77,227 input · 0 output

## Community Hubs (Navigation)
- Tracking UI Component
- Tracking Backend Contract
- Design Taste Skill
- Tracking Service Layer
- Tracking Mock Data
- Bundle Pricing Analysis
- Homepage Interactions
- Graphify Integration

## God Nodes (most connected - your core abstractions)
1. `NrOrderTracking` - 18 edges
2. `NordicReflection Prisanalys: Fardiga paket` - 12 edges
3. `design-taste-frontend Skill (tasteskill)` - 11 edges
4. `Spara din order - backend contract` - 11 edges
5. `el()` - 8 edges
6. `normalizeTracking()` - 7 edges
7. `POST /apps/nordic-tracking/order` - 7 edges
8. `init()` - 6 edges
9. `text()` - 6 edges
10. `initAll()` - 5 edges

## Surprising Connections (you probably didn't know these)
- `Upgrade communicated in kronor, percent secondary` --semantically_similar_to--> `Anti-Default Discipline`  [AMBIGUOUS] [semantically similar]
  docs/NordicReflection-prisanalys-paket.pdf → .agents/skills/design-taste-frontend/SKILL.md
- `Order Tracking Page (/pages/spara-din-order)` --conceptually_related_to--> `Shopify Polaris`  [AMBIGUOUS]
  docs/tracking/README.md → .agents/skills/design-taste-frontend/SKILL.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Order tracking theme file set** — docs_tracking_readme_nr_order_tracking_section, assets_nr_tracking, assets_nr_tracking_mock, docs_tracking_readme_nr_tracking_css, docs_tracking_readme_page_template [EXTRACTED 1.00]
- **Bundle price ladder proposal across families** — docs_nordicreflection_prisanalys_paket_good_better_best_ladder, docs_nordicreflection_prisanalys_paket_interior_bundle_family, docs_nordicreflection_prisanalys_paket_rim_bundle_family, docs_nordicreflection_prisanalys_paket_exterior_bundle_family, docs_nordicreflection_prisanalys_paket_exterior_mid_bundle_proposal [EXTRACTED 1.00]
- **Design read to dials to design system pipeline** — _agents_skills_design_taste_frontend_skill_brief_inference, _agents_skills_design_taste_frontend_skill_three_dials, _agents_skills_design_taste_frontend_skill_design_system_map, _agents_skills_design_taste_frontend_skill_preflight_check [INFERRED 0.85]

## Communities (8 total, 0 thin omitted)

### Community 0 - "Tracking UI Component"
Cohesion: 0.22
Nodes (5): createHttpTransport(), el(), formatDateTime(), NrOrderTracking, svgIcon()

### Community 1 - "Tracking Backend Contract"
Cohesion: 0.14
Nodes (20): Spara din order - backend contract, Backend security checklist, DHL Shipment Tracking Unified API, Normalized tracking model, assets/nr-tracking.css, POST /apps/nordic-tracking/order, Order enumeration protection (identical not_found), templates/page.spara-din-order.json (+12 more)

### Community 2 - "Design Taste Skill"
Cohesion: 0.16
Nodes (16): design-taste-frontend Skill (tasteskill), AI Tells (Forbidden Patterns), Anti-Default Discipline, Block Library Contract, Brief Inference / Design Read, Brief to Design System Map, Em-Dash Ban, Layout Discipline Hard Rules (+8 more)

### Community 3 - "Tracking Service Layer"
Cohesion: 0.24
Nodes (14): COPY, createService(), call(), dateTimeParts, dhlTrackingUrl(), formatDate(), formatOrderNumber(), isoDate() (+6 more)

### Community 4 - "Tracking Mock Data"
Cohesion: 0.18
Nodes (13): build(), createMockTransport(), EVENTS, inDays(), item(), ORDERS, PICKUP_POINT, scenarios (+5 more)

### Community 5 - "Bundle Pricing Analysis"
Cohesion: 0.27
Nodes (14): NordicReflection Prisanalys: Fardiga paket, Automatic upgrade line in bundle comparison, Cost data gaps in Shopify, Decisions needed, Exterior bundle family (Startkit / Komplett Kit), Exterior mid bundle proposal (Startkit + Foamtastic + GlossCoat, 719 kr), Foam Wash Kit, Bra / Battre / Bast price ladder (+6 more)

### Community 6 - "Homepage Interactions"
Cohesion: 0.67
Nodes (6): init(), initAll(), initHeroVideo(), initResultSlider(), initReveal(), initWashSteps()

### Community 7 - "Graphify Integration"
Cohesion: 1.00
Nodes (3): CLAUDE.md project instructions, graphify Knowledge Graph (graphify-out), Run graphify update after code changes

## Ambiguous Edges - Review These
- `Anti-Default Discipline` → `Upgrade communicated in kronor, percent secondary`  [AMBIGUOUS]
  docs/NordicReflection-prisanalys-paket.pdf · relation: semantically_similar_to
- `Shopify Polaris` → `Order Tracking Page (/pages/spara-din-order)`  [AMBIGUOUS]
  docs/tracking/README.md · relation: conceptually_related_to

## Knowledge Gaps
- **15 isolated node(s):** `PICKUP_POINT`, `EVENTS`, `ORDERS`, `TRACKING`, `scenarios` (+10 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 22 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Anti-Default Discipline` and `Upgrade communicated in kronor, percent secondary`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._
- **What is the exact relationship between `Shopify Polaris` and `Order Tracking Page (/pages/spara-din-order)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `Spara din order - backend contract` connect `Tracking Backend Contract` to `Design Taste Skill`, `Tracking Service Layer`, `Tracking Mock Data`?**
  _High betweenness centrality (0.517) - this node is a cross-community bridge._
- **Why does `Order Tracking Page (/pages/spara-din-order)` connect `Design Taste Skill` to `Tracking Backend Contract`?**
  _High betweenness centrality (0.341) - this node is a cross-community bridge._
- **What connects `PICKUP_POINT`, `EVENTS`, `ORDERS` to the rest of the system?**
  _15 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Tracking Backend Contract` be split into smaller, more focused modules?**
  _Cohesion score 0.1380952380952381 - nodes in this community are weakly interconnected._