# Graph Report - shopify  (2026-09-27)

## Corpus Check
- 143 files · ~257,620 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 117 file(s) not represented in the graph (top: .liquid 58, .csv 53, .css 6)

## Summary
- 2513 nodes · 3274 edges · 187 communities (145 shown, 42 thin omitted)
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 31 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `83f4d350`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- NrOrderTracking
- scripts/core.py
- validate_data.py
- gray
- nr-tracking-mock.js
- NordicReflection Prisanalys: Fardiga paket
- init
- CLAUDE.md
- sys
- slide_search_core.py
- Tailwind CSS Utility Reference
- pathlib
- design_system.py
- Brand Guidelines v1.0
- Design
- Canvas Design System
- spacing
- Form & Input Components
- Tailwind CSS Responsive Design
- Typography Specifications
- Logo Usage Rules
- Component Specifications
- shadcn/ui Accessibility Patterns
- TestTailwindConfigGenerator
- html-token-validator.py
- Asset Approval Checklist
- Logo AI Prompt Engineering
- .generate
- Color Palette Management
- CIP Deliverable Guide
- States and Variants
- UI Styling Skill
- Workflow
- Design System
- Tailwind CSS Customization
- TailwindConfigGenerator
- Appendix B - Canonical Sources (read these before reinventing)
- generate-slide.py
- test_design_system_mode.py
- Routing by Task Type
- Asset Organization Guide
- Primary Color Meanings
- Core Logo Types
- cip/core.py
- BM25
- fetch-background.py
- color
- Brand Consistency Checklist
- CIP Mockup Prompt Engineering
- Color Semantics
- Design Principles
- Design Principles
- fontSize
- TestShadcnInstaller
- extract-colors.cjs
- CIP Design Reference
- Icon Design Reference
- Copywriting Formulas
- Copywriting Formulas
- test_data_contracts.py
- _palette_is_dark
- CatalogRefreshTest
- Banner Design - Multi-Format Creative Banner System
- Messaging Framework
- Brand Voice Framework
- validate-asset.cjs
- Layout Patterns
- Tailwind Integration
- Layout Patterns
- TestWebStackFreshness
- cip/generate.py
- update.md
- Logo Design Reference
- Token Architecture
- design-tokens-starter.json
- _select_palette_for_mode
- TestDomainDetection
- TestSearchDomains
- 4. DESIGN ENGINEERING DIRECTIVES (Bias Correction)
- csv
- Primitive Tokens
- embed-tokens.cjs
- validate-tokens.cjs
- card
- ShadcnInstaller
- .check_shadcn_config
- .generate_config_string
- render-html.py
- Core Visual Elements
- inject-brand-context.cjs
- CIP Design Style Guide
- primitive
- TestGeneratedConfigIsValidJs
- TestNativeDesktopStackFreshness
- Quick Reference
- 10. REFERENCE VOCABULARY (Pattern Names the Agent Should Know)
- tasteskill: Anti-Slop Frontend Skill
- ._base_config
- sync-brand-to-tokens.cjs
- Brand
- Slide Strategies
- Component Tokens
- generate-tokens.cjs
- Standard PDP system – Phase 1 audit
- button
- Slide Strategies
- test_style_taxonomy.py
- BM25
- .test_add_all_components_success
- DesignSystemGenerator
- 9. AI TELLS (Forbidden Patterns)
- cip/search.py
- input
- radius
- UI/UX Pro Max - Design Intelligence
- 11. REDESIGN PROTOCOL
- 3. DEFAULT ARCHITECTURE & CONVENTIONS
- 6. PERFORMANCE & ACCESSIBILITY GUARDRAILS
- logo/search.py
- Slides Reference
- HTML Slide Template
- HTML Slide Template
- TestThresholdGate
- Query Contract
- shadow
- Slides
- TestTokenizer
- split_values
- read_rows
- TestLandingAndStackContract
- Pre-Delivery Checklist
- Prerequisites
- 0. BRIEF INFERENCE (Read the Room Before Anything Else)
- 12. THE BLOCK LIBRARY (Contract - Implementations Land Here Iteratively)
- 5. CONTEXT-AWARE PROACTIVITY
- 8. DARK MODE PROTOCOL
- Brand Guidelines Template
- $type
- radius
- lg
- TestBm25CoreBehavior
- Common Rules for Professional UI
- Example Workflow
- 7. DIAL DEFINITIONS (Technical Reference)
- padding-y
- xl
- md
- none
- TestFixtureValidation
- Tips for Better Results
- destructive
- destructive-foreground
- muted
- primary-foreground
- ring
- secondary-foreground
- .temp_project
- slides-create.md
- create.md
- .test_add_components_no_config
- .test_add_components_already_installed
- .test_add_components_dry_run
- .test_add_all_components_dry_run
- .test_list_installed_empty
- .test_init_default_project_root
- .test_get_installed_components_empty
- .test_add_components_no_components
- .test_add_fonts
- .test_add_breakpoints
- .test_recommend_plugins
- .test_generate_typescript_config
- .test_add_spacing
- .test_generate_javascript_config
- .test_validate_config_no_content
- .test_validate_config_empty_theme
- .test_recommend_plugins_nextjs
- .test_generate_config_with_colors
- .test_write_config_invalid_path
- .test_validate_config_valid
- .test_full_configuration_typescript
- .test_default_content_paths_react
- .test_full_configuration_javascript
- .test_add_colors
- .test_default_content_paths_nextjs
- test_text_layout_resilience.py
- TestGeneratedCatalogContract
- publish

## God Nodes (most connected - your core abstractions)
1. `TailwindConfigGenerator` - 58 edges
2. `TestTailwindConfigGenerator` - 35 edges
3. `DesignSystemGenerator` - 35 edges
4. `ShadcnInstaller` - 34 edges
5. `TestShadcnInstaller` - 26 edges
6. `NrOrderTracking` - 20 edges
7. `UI Styling Skill` - 17 edges
8. `tasteskill: Anti-Slop Frontend Skill` - 16 edges
9. `color` - 15 edges
10. `search()` - 15 edges

## Surprising Connections (you probably didn't know these)
- `Base Color Presets` --references--> `init()`  [INFERRED]
  .claude/skills/ui-styling/references/shadcn-theming.md → assets/nr-homepage.js
- `Style Variants` --references--> `init()`  [INFERRED]
  .claude/skills/ui-styling/references/shadcn-theming.md → assets/nr-homepage.js
- `TestShadcnInstaller` --uses--> `ShadcnInstaller`  [INFERRED]
  .claude/skills/ui-styling/scripts/tests/test_shadcn_add.py → .claude/skills/ui-styling/scripts/shadcn_add.py
- `TestGeneratedConfigIsValidJs` --uses--> `TailwindConfigGenerator`  [INFERRED]
  .claude/skills/ui-styling/scripts/tests/test_tailwind_config_gen.py → .claude/skills/ui-styling/scripts/tailwind_config_gen.py
- `TestTailwindConfigGenerator` --uses--> `TailwindConfigGenerator`  [INFERRED]
  .claude/skills/ui-styling/scripts/tests/test_tailwind_config_gen.py → .claude/skills/ui-styling/scripts/tailwind_config_gen.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Bundle price ladder proposal across families** — docs_nordicreflection_prisanalys_paket_good_better_best_ladder, docs_nordicreflection_prisanalys_paket_interior_bundle_family, docs_nordicreflection_prisanalys_paket_rim_bundle_family, docs_nordicreflection_prisanalys_paket_exterior_bundle_family, docs_nordicreflection_prisanalys_paket_exterior_mid_bundle_proposal [EXTRACTED 1.00]

## Communities (187 total, 42 thin omitted)

### Community 0 - "NrOrderTracking"
Cohesion: 0.12
Nodes (19): COPY, createHttpTransport(), createService(), call(), dateTimeParts, dhlTrackingUrl(), el(), formatDate() (+11 more)

### Community 1 - "scripts/core.py"
Cohesion: 0.06
Nodes (60): BM25, _contains_phrase(), detect_domain(), _domain_keywords(), _exact_match_diagnostic(), _exact_row_identity(), _exact_stack_identifier(), _file_signature() (+52 more)

### Community 2 - "validate_data.py"
Cohesion: 0.06
Nodes (52): ambiguous_python_import_1a7aff1e4e66, ambiguous_python_import_862968582d30, Semantic quality contracts for the core UI/UX datasets., read_rows(), TestAccessibilityGuidance, TestChartsTypographyAndIcons, TestCurrentReactGuidance, TestSemanticColors (+44 more)

### Community 3 - "gray"
Cohesion: 0.05
Nodes (53): $type, $value, $type, $value, $type, $value, $type, $value (+45 more)

### Community 4 - "nr-tracking-mock.js"
Cohesion: 0.08
Nodes (27): build(), createMockTransport(), EVENTS, inDays(), item(), ORDERS, PICKUP_POINT, scenarios (+19 more)

### Community 5 - "NordicReflection Prisanalys: Fardiga paket"
Cohesion: 0.25
Nodes (15): NordicReflection Prisanalys: Fardiga paket, Automatic upgrade line in bundle comparison, Cost data gaps in Shopify, Decisions needed, Exterior bundle family (Startkit / Komplett Kit), Exterior mid bundle proposal (Startkit + Foamtastic + GlossCoat, 719 kr), Foam Wash Kit, Bra / Battre / Bast price ladder (+7 more)

### Community 6 - "init"
Cohesion: 0.10
Nodes (27): init(), initAll(), initKitToggles(), initResultSlider(), initReveal(), initShortTitles(), initVideos(), initWashSteps() (+19 more)

### Community 8 - "sys"
Cohesion: 0.09
Nodes (32): apply_color(), apply_viewbox_size(), extract_svgs(), generate_batch(), generate_icon(), generate_sizes(), load_env(), main() (+24 more)

### Community 9 - "slide_search_core.py"
Cohesion: 0.08
Nodes (38): format_context(), format_result(), main(), Format a single search result for display, Slide Search CLI - Search slide design databases for strategies, layouts, copy,…, Format contextual recommendations for display., BM25, calculate_pattern_break() (+30 more)

### Community 10 - "Tailwind CSS Utility Reference"
Cohesion: 0.05
Nodes (43): Arbitrary Values, Aspect Ratio, Background Colors, Border Color, Border Radius, Border Style, Border Width, Borders (+35 more)

### Community 11 - "pathlib"
Cohesion: 0.10
Nodes (22): Regression test for sync-brand-to-tokens.cjs. The color parser required a…, main(), Slide Token Validator (Legacy Wrapper) Now delegates to html-token-validator.py…, Delegate to unified html-token-validator.py with --type slides., Path, Regression tests for validate-tokens.cjs. The validator used to skip any line…, A hardcoded hex on the same line as a var() token is still a violation., A line that references only tokens produces no false positives. (+14 more)

### Community 12 - "design_system.py"
Cohesion: 0.06
Nodes (41): ambiguous_python_import_27651e179b1f, ambiguous_python_import_2f0c067c00e5, ambiguous_python_import_dace3b29cbf4, ambiguous_python_import_fcb3bee7b643, argparse, ansi_ljust(), _detect_page_type(), format_ascii_box() (+33 more)

### Community 13 - "Brand Guidelines v1.0"
Cohesion: 0.05
Nodes (37): 1. Color Palette, 2. Typography, 3. Logo Usage, 4. Voice & Tone, 5. Imagery Guidelines, 6. Design Components, Accessibility, AI Image Generation (+29 more)

### Community 14 - "Design"
Cohesion: 0.06
Nodes (35): Banner Design (Built-in), Banner: Design Rules, Banner: Quick Size Reference, Banner: Top Art Styles, Banner: Workflow, CIP Design (Built-in), CIP: Generate Brief, CIP: Generate Mockups (+27 more)

### Community 15 - "Canvas Design System"
Cohesion: 0.06
Nodes (35): 1. Visual Communication First, 2. Minimal Text Integration, 3. Expert Craftsmanship, 4. Systematic Patterns, Analog Meditation, Approach, Canvas Boundaries, Canvas Design System (+27 more)

### Community 16 - "spacing"
Cohesion: 0.06
Nodes (34): $type, $value, $type, $value, $type, $value, $type, $value (+26 more)

### Community 17 - "Form & Input Components"
Cohesion: 0.06
Nodes (32): Accordion, Alert, Alert Dialog, Avatar, Badge, Button, Card, Checkbox (+24 more)

### Community 18 - "Tailwind CSS Responsive Design"
Cohesion: 0.06
Nodes (32): 1. Mobile-First Design, 2. Consistent Breakpoint Usage, 3. Test at Breakpoint Boundaries, 4. Use Container for Content Width, 5. Progressive Enhancement, 6. Avoid Too Many Breakpoints, Best Practices, Breakpoint System (+24 more)

### Community 19 - "Typography Specifications"
Cohesion: 0.06
Nodes (30): Accessibility, Base System, Best Practices, Clean & Modern, Common Font Pairings, Contrast Requirements, CSS Implementation, Editorial (+22 more)

### Community 20 - "Logo Usage Rules"
Cohesion: 0.07
Nodes (28): Absolute Don'ts, Approved Backgrounds, Before Using Logo, Clear Space, Co-branding, Color Rules, Color Usage, Color Variants (+20 more)

### Community 21 - "Component Specifications"
Cohesion: 0.07
Nodes (28): Alert, Anatomy, Anatomy, Anatomy, Anatomy, Anatomy, Badge, Button (+20 more)

### Community 22 - "shadcn/ui Accessibility Patterns"
Cohesion: 0.07
Nodes (28): Accordion, Alert, ARIA Labels, Checkbox and Radio, Color Contrast, Command Palette Navigation, Component-Specific Patterns, Dialog/Modal Navigation (+20 more)

### Community 23 - "TestTailwindConfigGenerator"
Cohesion: 0.07
Nodes (15): Test adding colors multiple times., Test adding full color palette., Test TailwindConfigGenerator class., Test that adding same plugin twice doesn't duplicate., Test generating config with plugins., Test writing configuration to file., Test initialization for JavaScript config., Test that written config contains expected content. (+7 more)

### Community 24 - "html-token-validator.py"
Cohesion: 0.12
Nodes (25): get_context(), is_allowed_exception(), is_allowed_rgba(), is_inside_block(), load_css_variables(), main(), print_result(), print_summary() (+17 more)

### Community 25 - "Asset Approval Checklist"
Cohesion: 0.08
Nodes (25): Accessibility, Archival, Asset Approval Checklist, Automation Support, Color Compliance, Common Issues & Fixes, Content Accessibility, Content Quality (+17 more)

### Community 26 - "Logo AI Prompt Engineering"
Cohesion: 0.08
Nodes (25): Common Pitfalls, Core Prompt Structure, Detailed Brief, Eco/Sustainable, Effective Keywords by Style, Fashion Brand, Healthcare, Industry-Specific Prompts (+17 more)

### Community 27 - ".generate"
Cohesion: 0.14
Nodes (8): Execute searches across multiple domains., Find matching reasoning rule for a category., Apply reasoning rules to search results., Select best matching result based on priority keywords., Extract results list from search result dict., Generate complete design system recommendation. variance/motion/density are…, Bucket a 1-10 dial value into its tier config. Returns None if value is None., _resolve_dial()

### Community 28 - "Color Palette Management"
Cohesion: 0.08
Nodes (24): Accessibility Requirements, Brand Compliance Validation, Checking Contrast, Color Documentation Format, Color Extraction, Color Palette Examples, Color Palette Management, Color System Structure (+16 more)

### Community 29 - "CIP Deliverable Guide"
Cohesion: 0.08
Nodes (24): Apparel, Business Card, Car/Sedan, CIP Deliverable Guide, Core Identity, Digital Assets, Email Signature, Envelope (+16 more)

### Community 30 - "States and Variants"
Cohesion: 0.08
Nodes (24): Accessibility, Accessibility Requirements, ARIA States, Color Contrast, Color Variants, Disabled States, Error Messages, Error States (+16 more)

### Community 31 - "UI Styling Skill"
Cohesion: 0.08
Nodes (24): Accessibility Patterns, Alternative: Tailwind-Only Setup, Best Practices, Common Patterns, Component Layer: shadcn/ui, Component Library Guide, Component + Styling Setup, Core Stack (+16 more)

### Community 32 - "Workflow"
Cohesion: 0.08
Nodes (23): Art Direction Styles (Reuse from Banner), Color & Contrast, Design Best Practices, HTML Design Rules, HTML Template Structure, Option A: Chrome Headless CLI (Recommended — zero dependencies), Option B: chrome-devtools skill, Option C: Playwright script (+15 more)

### Community 33 - "Design System"
Cohesion: 0.09
Nodes (22): Best Practices, Chart.js Integration, Command, Component Spec Pattern, Contextual Decision Flow, Decision System CSVs, Design System, Integration (+14 more)

### Community 34 - "Tailwind CSS Customization"
Cohesion: 0.09
Nodes (22): @apply Directive, Best Practices, Color Customization, Complete Tailwind Config, Configuration Examples, Content Configuration, Custom Color Palette, Custom Font Sizes (+14 more)

### Community 35 - "TailwindConfigGenerator"
Cohesion: 0.10
Nodes (12): main(), Add custom font families. Args: fonts: Dict of font_type: [font_names] e.g.,…, Add custom spacing values. Args: spacing: Dict of name: value e.g., {'18':…, Add custom breakpoints. Args: breakpoints: Dict of name: width e.g., {'3xl':…, Add plugin requirements. Args: plugins: List of plugin names e.g.,…, Get plugin recommendations based on configuration. Returns: List of recommended…, Generate Tailwind CSS configuration files., Validate configuration. Returns: Tuple of (valid, message) (+4 more)

### Community 36 - "Appendix B - Canonical Sources (read these before reinventing)"
Cohesion: 0.09
Nodes (21): APPENDICES - Real Source-Backed Reference Material, Appendix A - Install Commands per Design System, Appendix B - Canonical Sources (read these before reinventing), Appendix C - Apple Liquid Glass: Honest Web Approximation, Apple Liquid Glass (Apple platforms only), Atlassian, Bootstrap, Carbon (+13 more)

### Community 37 - "generate-slide.py"
Cohesion: 0.13
Nodes (21): _e(), generate_chart_slide(), generate_cta_slide(), generate_deck(), generate_metrics_slide(), generate_problem_slide(), generate_solution_slide(), generate_testimonial_slide() (+13 more)

### Community 38 - "test_design_system_mode.py"
Cohesion: 0.14
Nodes (11): _filter_anti_patterns_for_mode(), _query_wants_dark(), True when a styles.csv row describes itself as dark-first., True when the query explicitly asks for a dark theme., Resolve the mode the rest of the output has to agree with., Drop "avoid dark mode" advice once dark mode is the resolved answer., _resolve_color_mode(), _style_is_dark_primary() (+3 more)

### Community 39 - "Routing by Task Type"
Cohesion: 0.10
Nodes (19): Banner Design Tasks, Brand Identity Tasks, Component Creation, Corporate Identity Program Tasks, Design Routing Guide, Design System Migration, Icon Design Tasks, Implementation Tasks (+11 more)

### Community 40 - "Asset Organization Guide"
Cohesion: 0.11
Nodes (18): Asset Entry (manifest.json), Asset Organization Guide, By Campaign, By Status, By Type, Cleanup Workflow, Components, Directory Structure (+10 more)

### Community 41 - "Primary Color Meanings"
Cohesion: 0.11
Nodes (18): Accessibility Considerations, Analogous, Black, Blue, Color Combinations by Industry, Color Harmony Types, Complementary, Green (+10 more)

### Community 42 - "Core Logo Types"
Cohesion: 0.11
Nodes (18): 1. Wordmark (Logotype), 2. Lettermark (Monogram), 3. Pictorial Mark (Brand Mark), 4. Abstract Mark, 5. Mascot, 6. Emblem, 7. Combination Mark, Aesthetic Styles (+10 more)

### Community 43 - "cip/core.py"
Cohesion: 0.10
Nodes (27): detect_domain(), get_cip_brief(), _load_csv(), Load CSV and return list of dicts, Core search function using BM25, Auto-detect the most relevant domain from query, Main search function with auto-domain detection, Search across all domains and combine results (+19 more)

### Community 44 - "BM25"
Cohesion: 0.28
Nodes (5): BM25, BM25 ranking algorithm for text search, Lowercase, split, remove punctuation, filter short words, Build BM25 index from documents, Score all documents against query

### Community 45 - "fetch-background.py"
Cohesion: 0.16
Nodes (18): generate_css_for_background(), get_background_image(), get_curated_images(), get_overlay_css(), get_pexels_search_url(), load_backgrounds_config(), load_brand_colors(), main() (+10 more)

### Community 46 - "color"
Cohesion: 0.11
Nodes (19): $type, $value, background, foreground, muted-foreground, primary, primary-hover, secondary (+11 more)

### Community 47 - "Brand Consistency Checklist"
Cohesion: 0.11
Nodes (17): Audit Frequency, Brand Consistency Checklist, Channel Audit, Collateral, Colors, Common Issues, Email, Imagery (+9 more)

### Community 48 - "CIP Mockup Prompt Engineering"
Cohesion: 0.11
Nodes (17): Apparel (Polo/T-Shirt), Base Prompt Structure, Business Card, CIP Mockup Prompt Engineering, Context Modifiers, Corporate Minimal, Deliverable-Specific Modifiers, Letterhead (+9 more)

### Community 49 - "Color Semantics"
Cohesion: 0.11
Nodes (17): Accent, Applying Semantic Tokens, Background & Foreground, Border & Ring, Color Semantics, Dark Mode Overrides, Destructive, Interactive States (+9 more)

### Community 50 - "Design Principles"
Cohesion: 0.12
Nodes (15): 22 Art Direction Styles, Banner Sizes & Art Direction Styles Reference, Complete Banner Sizes, CTA Rules, Design Principles, Pinterest Research Queries, Print, Print Specs (+7 more)

### Community 51 - "Design Principles"
Cohesion: 0.12
Nodes (15): 22 Art Direction Styles, Banner Sizes & Art Direction Styles Reference, Complete Banner Sizes, CTA Rules, Design Principles, Pinterest Research Queries, Print, Print Specs (+7 more)

### Community 52 - "fontSize"
Cohesion: 0.12
Nodes (16): $type, $value, $type, $value, $type, $value, $type, $value (+8 more)

### Community 53 - "TestShadcnInstaller"
Cohesion: 0.12
Nodes (9): Test adding components with overwrite flag., Test ShadcnInstaller class., Test listing installed components without config., Test listing installed components when they exist., Test initialization with custom project root., Test initialization with dry run mode., Test checking for existing shadcn config., Test getting installed components when files exist. (+1 more)

### Community 54 - "extract-colors.cjs"
Cohesion: 0.20
Nodes (12): calculateCompliance(), colorDistance(), displayPalette(), extractHexColors(), findNearestBrandColor(), fs, generateImageMagickCommand(), hexToRgb() (+4 more)

### Community 55 - "CIP Design Reference"
Cohesion: 0.13
Nodes (14): CIP Brief (Start Here), CIP Design Reference, Commands, Deliverable Categories, Design Styles, Detailed References, Generate Mockups, HTML Presentation Features (+6 more)

### Community 56 - "Icon Design Reference"
Cohesion: 0.13
Nodes (14): Available Styles, CLI Options, Commands, Generate Batch Variations, Generate Multiple Sizes, Generate Single Icon, Icon Categories, Icon Design Reference (+6 more)

### Community 57 - "Copywriting Formulas"
Cohesion: 0.13
Nodes (14): AIDA (Attention-Interest-Desire-Action), Before-After-Bridge, Contrast Patterns, Copywriting Formulas, Core Formulas, Cost of Inaction, FAB (Features-Advantages-Benefits), Formula-to-Slide Mapping (+6 more)

### Community 58 - "Copywriting Formulas"
Cohesion: 0.13
Nodes (14): AIDA (Attention-Interest-Desire-Action), Before-After-Bridge, Contrast Patterns, Copywriting Formulas, Core Formulas, Cost of Inaction, FAB (Features-Advantages-Benefits), Formula-to-Slide Mapping (+6 more)

### Community 59 - "test_data_contracts.py"
Cohesion: 0.20
Nodes (10): ambiguous_python_import_b9171ee6cb4c, apply_decision_rules(), _object_without_duplicates(), parse_decision_rules(), Return deterministic mutations and an audit trail; never execute data., Closed, non-executable grammar for design-system decision rules., Parse the canonical condition -> action-array representation., _validate_action() (+2 more)

### Community 60 - "_palette_is_dark"
Cohesion: 0.18
Nodes (7): _palette_is_dark(), WCAG relative luminance of a #RRGGBB string, or None if unparseable., True when a colors.csv row's Background is a dark surface., _relative_luminance(), The exact reproduction from issue #428., TestEndToEndCoherence, TestLuminance

### Community 62 - "Banner Design - Multi-Format Creative Banner System"
Cohesion: 0.14
Nodes (13): Art Direction Styles (Top 10), Banner Design - Multi-Format Creative Banner System, Banner Size Quick Reference, Design Rules, Prerequisites, Security, Step 1: Gather Requirements (AskUserQuestion), Step 2: Research & Art Direction (+5 more)

### Community 63 - "Messaging Framework"
Cohesion: 0.14
Nodes (13): Core Statements, Elevator Pitches, Framework Structure, Message Architecture, Message by Audience, Message Testing, Messaging Framework, Mission Statement (+5 more)

### Community 64 - "Brand Voice Framework"
Cohesion: 0.14
Nodes (13): Brand Voice Framework, Character Spectrum, Emotion Spectrum, Language Spectrum, Step 1: Define Personality Traits, Step 2: Create Voice Chart, Step 3: Context Adaptation, Tone Spectrum (+5 more)

### Community 65 - "validate-asset.cjs"
Cohesion: 0.25
Nodes (13): checkManifest(), formatBytes(), formatOutput(), fs, main(), parseFilename(), path, RULES (+5 more)

### Community 66 - "Layout Patterns"
Cohesion: 0.14
Nodes (13): Card Styles, Component Variants, CSS Structures, Feature Grid (3 columns), Layout Decision Flow, Layout Patterns, Layout Selection by Use Case, Metric Styles (+5 more)

### Community 67 - "Tailwind Integration"
Cohesion: 0.14
Nodes (13): Animation Tokens, Base Layer, Button Example, Component Classes, CSS Variables Setup, Dark Mode Toggle, HSL Format Benefits, shadcn/ui Alignment (+5 more)

### Community 68 - "Layout Patterns"
Cohesion: 0.14
Nodes (13): Card Styles, Component Variants, CSS Structures, Feature Grid (3 columns), Layout Decision Flow, Layout Patterns, Layout Selection by Use Case, Metric Styles (+5 more)

### Community 70 - "cip/generate.py"
Cohesion: 0.19
Nodes (15): ambiguous_python_import_766077957567, build_cip_prompt(), check_logo_required(), generate_cip_set(), generate_with_nano_banana(), load_env(), load_logo_image(), main() (+7 more)

### Community 71 - "update.md"
Cohesion: 0.15
Nodes (12): Color Presets, Examples, Files Modified, Important, Overview, Skills Used, Step 1: Gather Brand Input, Step 2: Update Brand Guidelines (+4 more)

### Community 72 - "Logo Design Reference"
Cohesion: 0.15
Nodes (12): Available Styles, Color Psychology, Commands, Design Brief (Start Here), Detailed References, Generate Logo, Industry Defaults, Logo Design Reference (+4 more)

### Community 73 - "Token Architecture"
Cohesion: 0.15
Nodes (12): Categories, Dark Mode, File Organization, Layer 1: Primitive Tokens, Layer 2: Semantic Tokens, Layer 3: Component Tokens, Layer Overview, Migration from Flat Tokens (+4 more)

### Community 74 - "design-tokens-starter.json"
Cohesion: 0.15
Nodes (12): component, $type, $value, dark, semantic, $schema, $type, $value (+4 more)

### Community 75 - "_select_palette_for_mode"
Cohesion: 0.22
Nodes (7): _contrast_ratio(), _derive_dark_palette(), WCAG contrast ratio for two hex colors, or None if either is invalid., Keep product brand tokens while deriving accessible dark surfaces., Pick the highest-ranked palette matching the resolved mode. Only the dark case…, _select_palette_for_mode(), TestPaletteSelection

### Community 78 - "4. DESIGN ENGINEERING DIRECTIVES (Bias Correction)"
Cohesion: 0.17
Nodes (12): 4.10 Quotes & Testimonials, 4.11 Page Theme Lock (Light / Dark Mode Consistency), 4.1 Typography, 4.2 Color Calibration, 4.3 Layout Diversification, 4.4 Materiality, Shadows, Cards, 4.5 Interactive UI States, 4.6 Data & Form Patterns (+4 more)

### Community 79 - "csv"
Cohesion: 0.12
Nodes (12): ambiguous_python_import_4aa1a5da4b7d, ambiguous_python_import_9c9aff68267f, Offline contract tests for deterministic upstream catalog refreshes., Freshness and migration contracts for native, desktop, and 3D stacks., Unit tests for metric math and relevance fixture validation., TestMetricMath, Freshness and generation-isolation contracts for web stack guidance., csv (+4 more)

### Community 80 - "Primitive Tokens"
Cohesion: 0.17
Nodes (11): Border Radius, Color Scales, Gray Scale, Motion / Duration, Primary Colors (Blue), Primitive Tokens, Shadows, Spacing Scale (+3 more)

### Community 81 - "embed-tokens.cjs"
Cohesion: 0.17
Nodes (9): args, fs, minimal, MINIMAL_TOKENS, path, projectRoot, tokensPath, wrapStyle (+1 more)

### Community 82 - "validate-tokens.cjs"
Cohesion: 0.24
Nodes (11): extensions, formatReport(), fs, getFiles(), main(), parseArgs(), path, patterns (+3 more)

### Community 83 - "card"
Cohesion: 0.20
Nodes (12): $type, $value, bg, bg, padding, shadow, card, bg (+4 more)

### Community 84 - "ShadcnInstaller"
Cohesion: 0.17
Nodes (8): main(), Path, Handle shadcn/ui component installation., Initialize installer. Args: project_root: Project root directory (default:…, ShadcnInstaller, Test adding all components without config., Test checking for non-existent shadcn config., Test getting installed components without config.

### Community 85 - ".check_shadcn_config"
Cohesion: 0.21
Nodes (6): Add all available shadcn/ui components. Args: overwrite: If True, overwrite…, List installed components. Returns: Tuple of (success, message with component…, Check if shadcn is initialized in project. Returns: True if components.json…, Get list of already installed components. Returns: List of installed component…, Read shadcn version from project package.json; fall back to a pinned default., Add shadcn/ui components. Args: components: List of component names to add…

### Community 86 - ".generate_config_string"
Cohesion: 0.20
Nodes (6): Generate configuration file content. Returns: Configuration file as string, Generate TypeScript configuration., Generate JavaScript configuration., Format plugins array for config. Validates each plugin name against a strict…, Add indentation to JSON string., Write configuration to file. Returns: Tuple of (success, message)

### Community 87 - "render-html.py"
Cohesion: 0.24
Nodes (10): ambiguous_python_import_4bbefc92923a, base64, generate_html(), get_deliverable_info(), get_image_base64(), main(), Convert image to base64 for embedding in HTML, Extract deliverable type from filename and get info (+2 more)

### Community 88 - "Core Visual Elements"
Cohesion: 0.18
Nodes (10): Color Palette, Colors, Core Visual Elements, Logo, Logo, Quick Checks, Typography, Typography (+2 more)

### Community 89 - "inject-brand-context.cjs"
Cohesion: 0.31
Nodes (10): extractColorsFromTable(), extractCoreAttributes(), extractHexColors(), extractImageStyle(), extractTypography(), extractVoice(), fs, generatePromptAddition() (+2 more)

### Community 90 - "CIP Design Style Guide"
Cohesion: 0.18
Nodes (10): Bold Dynamic, CIP Design Style Guide, Classic Traditional, Color Psychology, Corporate Minimal, Fresh Modern, Luxury Premium, Modern Tech (+2 more)

### Community 91 - "primitive"
Cohesion: 0.18
Nodes (11): fast, normal, slow, $type, $value, $type, $value, primitive (+3 more)

### Community 92 - "TestGeneratedConfigIsValidJs"
Cohesion: 0.25
Nodes (7): Reduce a generated TS/JS config to a bare assignable object so it can be handed…, Regression guard for the missing-comma bug between the ``theme`` block and…, The property preceding ``plugins`` must end with a comma (pure-Python check, so…, The emitted config parses as valid JS via ``node --check``., _strip_to_object(), TestGeneratedConfigIsValidJs, parametrize

### Community 94 - "Quick Reference"
Cohesion: 0.18
Nodes (11): 10. Charts & Data (LOW), 1. Accessibility (CRITICAL), 2. Touch & Interaction (CRITICAL), 3. Performance (HIGH), 4. Style Selection (HIGH), 5. Layout & Responsive (HIGH), 6. Typography & Color (MEDIUM), 7. Animation (MEDIUM) (+3 more)

### Community 95 - "10. REFERENCE VOCABULARY (Pattern Names the Agent Should Know)"
Cohesion: 0.20
Nodes (10): 10. REFERENCE VOCABULARY (Pattern Names the Agent Should Know), Animation Library Choice, Cards & Containers, Galleries & Media, Hero Paradigms, Layout & Grids, Micro-Interactions & Effects, Navigation & Menus (+2 more)

### Community 96 - "tasteskill: Anti-Slop Frontend Skill"
Cohesion: 0.20
Nodes (10): 13. OUT OF SCOPE, 14. FINAL PRE-FLIGHT CHECK, 1.A Dial Inference (design read → dial values), 1.B Use-Case Presets, 1.C How the Dials Drive Output, 1. THE THREE DIALS (Core Configuration), 2.A When to reach for a real design system (use official packages), 2.B When the brief is an aesthetic, not a system (+2 more)

### Community 97 - "._base_config"
Cohesion: 0.22
Nodes (6): Any, Path, Initialize generator. Args: typescript: If True, generate .ts config, else .js…, Determine default output path., Create base configuration structure., Get default content paths for framework.

### Community 98 - "sync-brand-to-tokens.cjs"
Cohesion: 0.29
Nodes (9): adjustBrightness(), { execFileSync }, extractColorsFromMarkdown(), fs, generateColorScale(), main(), path, updateDesignTokens() (+1 more)

### Community 99 - "Brand"
Cohesion: 0.20
Nodes (9): Brand, Brand Sync Workflow, Quick Start, References, Routing, Scripts, Subcommands, Templates (+1 more)

### Community 100 - "Slide Strategies"
Cohesion: 0.20
Nodes (9): Common Structures, Duarte Sparkline Pattern, Matching Strategy to Context, Product Demo (6 slides), Sales Pitch (9 slides), Search Commands, Slide Strategies, Strategy Selection (+1 more)

### Community 101 - "Component Tokens"
Cohesion: 0.20
Nodes (9): Alert Tokens, Badge Tokens, Button Tokens, Card Tokens, Component Tokens, Dialog/Modal Tokens, Input Tokens, Table Tokens (+1 more)

### Community 102 - "generate-tokens.cjs"
Cohesion: 0.36
Nodes (9): flattenTokens(), fs, generateCSS(), generateTailwind(), main(), parseArgs(), path, resolveReference() (+1 more)

### Community 103 - "Standard PDP system – Phase 1 audit"
Cohesion: 0.20
Nodes (9): 1. Scope, 2. Page-by-page table, 3. Cross-cutting findings, 4. Recommendation audit, 5. Proposed mappings (validated against catalogue and kit contents), 6. Media inventory and production backlog, 7. Missing or conflicting product information (needs owner confirmation), 8. Decisions needed before Phase 3 (+1 more)

### Community 104 - "button"
Cohesion: 0.20
Nodes (10): fg, font-size, hover-bg, button, $type, $value, $type, $value (+2 more)

### Community 105 - "Slide Strategies"
Cohesion: 0.20
Nodes (9): Common Structures, Duarte Sparkline Pattern, Matching Strategy to Context, Product Demo (6 slides), Sales Pitch (9 slides), Search Commands, Slide Strategies, Strategy Selection (+1 more)

### Community 106 - "test_style_taxonomy.py"
Cohesion: 0.17
Nodes (4): ambiguous_python_import_c894f1325619, Regression tests for the public style taxonomy and search contract., read_rows(), TestStyleTaxonomy

### Community 107 - "BM25"
Cohesion: 0.28
Nodes (5): BM25, BM25 ranking algorithm for text search, Lowercase, split, remove punctuation, filter short words, Build BM25 index from documents, Score all documents against query

### Community 108 - ".test_add_all_components_success"
Cohesion: 0.22
Nodes (5): Test successful component addition., Test component addition with subprocess error., Test component addition when npx is not found., Test successful addition of all components., patch

### Community 109 - "DesignSystemGenerator"
Cohesion: 0.23
Nodes (4): DesignSystemGenerator, Generates design system recommendations from aggregated searches., Load reasoning rules from CSV., TestReasoningMatch

### Community 110 - "9. AI TELLS (Forbidden Patterns)"
Cohesion: 0.25
Nodes (8): 9.A Visual & CSS, 9. AI TELLS (Forbidden Patterns), 9.B Typography, 9.C Layout & Spacing, 9.D Content & Data ("Jane Doe" Effect), 9.E External Resources & Components, 9.F Production-Test Tells (banned outright), 9.G EM-DASH BAN (the single most-violated Tell)

### Community 111 - "cip/search.py"
Cohesion: 0.32
Nodes (7): ambiguous_python_import_e82323b3f9ad, format_brief(), format_results(), main(), Format search results for display, CIP Design Search CLI - Search corporate identity design guidelines, Format CIP brief for display

### Community 112 - "input"
Cohesion: 0.29
Nodes (8): padding-x, input, $type, $value, focus-ring, padding-x, $type, $value

### Community 113 - "radius"
Cohesion: 0.29
Nodes (8): $type, $value, $type, $value, radius, default, full, default

### Community 114 - "UI/UX Pro Max - Design Intelligence"
Cohesion: 0.25
Nodes (7): How to Use, Primary Use Cases, Recommended, Rule Categories by Priority, Skip, UI/UX Pro Max - Design Intelligence, When to Apply

### Community 115 - "11. REDESIGN PROTOCOL"
Cohesion: 0.29
Nodes (7): 11.A Detect the Mode (first action), 11.B Audit Before Touching, 11.C Preservation Rules, 11.D Modernisation Levers (priority order), 11.E Decision Tree: Targeted Evolution vs Full Redesign, 11.F What Never Changes Silently, 11. REDESIGN PROTOCOL

### Community 116 - "3. DEFAULT ARCHITECTURE & CONVENTIONS"
Cohesion: 0.29
Nodes (7): 3.A Stack, 3.B State, 3.C Icons, 3.D Emoji Policy, 3. DEFAULT ARCHITECTURE & CONVENTIONS, 3.E Responsiveness & Layout Mechanics, 3.F Dependency Verification (mandatory)

### Community 117 - "6. PERFORMANCE & ACCESSIBILITY GUARDRAILS"
Cohesion: 0.29
Nodes (7): 6.A Hardware Acceleration, 6.B Reduced Motion (mandatory), 6.C Dark Mode (mandatory for any consumer-facing page), 6.D Core Web Vitals Targets, 6.E DOM Cost, 6.F Z-Index Restraint, 6. PERFORMANCE & ACCESSIBILITY GUARDRAILS

### Community 118 - "logo/search.py"
Cohesion: 0.29
Nodes (6): ambiguous_python_import_7e842b6a8c63, format_output(), generate_design_brief(), Format results for Claude consumption (token-optimized), Logo Design Search - CLI for searching logo design guidelines Usage: python…, Generate a comprehensive logo design brief based on query

### Community 119 - "Slides Reference"
Cohesion: 0.29
Nodes (6): Key Features, Knowledge Base, Slides Reference, Usage, When to Use, Workflow

### Community 120 - "HTML Slide Template"
Cohesion: 0.29
Nodes (6): Animation Classes, Background Images, Base Structure, Chart.js Integration, CSS Variables Reference, HTML Slide Template

### Community 121 - "HTML Slide Template"
Cohesion: 0.29
Nodes (6): Animation Classes, Background Images, Base Structure, Chart.js Integration, CSS Variables Reference, HTML Slide Template

### Community 123 - "Query Contract"
Cohesion: 0.29
Nodes (7): Query Contract, Step 1: Analyze User Requirements, Step 2: Generate Design System (new projects/pages), Step 2b: Persist Design System (Master + Overrides Pattern), Step 2c: Design Dials (optional), Step 3: Supplement with Detailed Searches (as needed), Step 4: Stack Guidelines

### Community 124 - "shadow"
Cohesion: 0.47
Nodes (6): sm, shadow, sm, sm, $type, $value

### Community 125 - "Slides"
Cohesion: 0.33
Nodes (5): References (Knowledge Base), Routing, Slides, Subcommands, When to Use

### Community 127 - "split_values"
Cohesion: 0.47
Nodes (3): split_values(), style_identities(), TestStyleIdentityContract

### Community 130 - "Pre-Delivery Checklist"
Cohesion: 0.33
Nodes (6): Accessibility, Interaction, Layout, Light/Dark Mode, Pre-Delivery Checklist, Visual Quality

### Community 131 - "Prerequisites"
Cohesion: 0.33
Nodes (6): Available Domains, Available Stacks, How to Use This Skill, Output Formats, Prerequisites, Search Reference

### Community 132 - "0. BRIEF INFERENCE (Read the Room Before Anything Else)"
Cohesion: 0.40
Nodes (5): 0.A Read these signals first, 0.B Output a one-line "Design Read" before generating, 0. BRIEF INFERENCE (Read the Room Before Anything Else), 0.C If the brief is ambiguous, ask one question, do not guess, 0.D Anti-Default Discipline

### Community 133 - "12. THE BLOCK LIBRARY (Contract - Implementations Land Here Iteratively)"
Cohesion: 0.40
Nodes (5): 12.A File Location, 12.B Required Frontmatter, 12.C Required Body Sections, 12.D Block-Library Discipline, 12. THE BLOCK LIBRARY (Contract - Implementations Land Here Iteratively)

### Community 134 - "5. CONTEXT-AWARE PROACTIVITY"
Cohesion: 0.40
Nodes (5): 5.A Sticky-Stack - Canonical Skeleton, 5.B Horizontal-Pan - Canonical Skeleton, 5.C Scroll-Reveal Stagger - Canonical Skeleton (lighter alternative), 5. CONTEXT-AWARE PROACTIVITY, 5.D Forbidden Animation Patterns

### Community 135 - "8. DARK MODE PROTOCOL"
Cohesion: 0.40
Nodes (5): 8.A Token Strategy (pick one, stick to it), 8.B Do Not Prescribe Specific Colors Here, 8.C Default Mode, 8.D Test in Both Modes Before Finishing, 8. DARK MODE PROTOCOL

### Community 136 - "Brand Guidelines Template"
Cohesion: 0.40
Nodes (4): Brand Guidelines Template, Document Structure, Extractable Fields, Usage

### Community 137 - "$type"
Cohesion: 0.60
Nodes (5): $type, $value, border, border, border

### Community 138 - "radius"
Cohesion: 0.60
Nodes (5): radius, radius, radius, $type, $value

### Community 139 - "lg"
Cohesion: 0.60
Nodes (5): lg, $type, $value, lg, lg

### Community 141 - "Common Rules for Professional UI"
Cohesion: 0.40
Nodes (5): Common Rules for Professional UI, Icons & Visual Elements, Interaction (App), Layout & Spacing, Light/Dark Mode Contrast

### Community 142 - "Example Workflow"
Cohesion: 0.40
Nodes (5): Example Workflow, Step 1: Analyze Requirements, Step 2: Generate Design System, Step 3: Supplement with Detailed Searches (as needed), Step 4: Stack Guidelines

### Community 143 - "7. DIAL DEFINITIONS (Technical Reference)"
Cohesion: 0.50
Nodes (4): 7. DIAL DEFINITIONS (Technical Reference), DESIGN_VARIANCE (Level 1-10), MOTION_INTENSITY (Level 1-10), VISUAL_DENSITY (Level 1-10)

### Community 144 - "padding-y"
Cohesion: 0.67
Nodes (4): padding-y, padding-y, $type, $value

### Community 145 - "xl"
Cohesion: 0.67
Nodes (4): xl, xl, $type, $value

### Community 146 - "md"
Cohesion: 0.67
Nodes (4): $type, $value, md, md

### Community 147 - "none"
Cohesion: 0.67
Nodes (4): $type, $value, none, none

### Community 149 - "Tips for Better Results"
Cohesion: 0.50
Nodes (4): Common Sticking Points, Pre-Delivery Checklist, Query Strategy, Tips for Better Results

### Community 150 - "destructive"
Cohesion: 0.67
Nodes (3): destructive, $type, $value

### Community 151 - "destructive-foreground"
Cohesion: 0.67
Nodes (3): destructive-foreground, $type, $value

### Community 152 - "muted"
Cohesion: 0.67
Nodes (3): muted, $type, $value

### Community 153 - "primary-foreground"
Cohesion: 0.67
Nodes (3): primary-foreground, $type, $value

### Community 154 - "ring"
Cohesion: 0.67
Nodes (3): ring, $type, $value

### Community 155 - "secondary-foreground"
Cohesion: 0.67
Nodes (3): secondary-foreground, $type, $value

### Community 184 - "test_text_layout_resilience.py"
Cohesion: 0.18
Nodes (5): ambiguous_python_import_bfd22ae4b7aa, Canonical regression contracts for resilient UI text layouts., read_rows(), TestTextLayoutDataContracts, TestTextLayoutRetrieval

## Knowledge Gaps
- **1040 isolated node(s):** `fs`, `path`, `fs`, `path`, `fs` (+1035 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1498 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **42 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `TailwindConfigGenerator` connect `TailwindConfigGenerator` to `pathlib`, `TestTailwindConfigGenerator`, `.test_add_fonts`, `.test_add_breakpoints`, `.test_recommend_plugins`, `.test_generate_typescript_config`, `.test_add_spacing`, `.test_generate_javascript_config`, `.test_validate_config_no_content`, `.test_validate_config_empty_theme`, `.test_recommend_plugins_nextjs`, `.test_generate_config_with_colors`, `.test_write_config_invalid_path`, `.test_validate_config_valid`, `.test_full_configuration_typescript`, `.test_default_content_paths_react`, `.test_full_configuration_javascript`, `.test_add_colors`, `.test_default_content_paths_nextjs`, `.generate_config_string`, `TestGeneratedConfigIsValidJs`, `._base_config`?**
  _High betweenness centrality (0.020) - this node is a cross-community bridge._
- **Why does `ShadcnInstaller` connect `ShadcnInstaller` to `.test_add_components_already_installed`, `.test_add_components_dry_run`, `.test_add_all_components_dry_run`, `.test_list_installed_empty`, `.test_init_default_project_root`, `.test_get_installed_components_empty`, `.test_add_components_no_components`, `pathlib`, `.test_add_all_components_success`, `TestShadcnInstaller`, `.check_shadcn_config`, `.test_add_components_no_config`?**
  _High betweenness centrality (0.020) - this node is a cross-community bridge._
- **Why does `DesignSystemGenerator` connect `DesignSystemGenerator` to `read_rows`, `test_design_system_mode.py`, `.generate`, `_select_palette_for_mode`, `design_system.py`, `test_data_contracts.py`, `_palette_is_dark`?**
  _High betweenness centrality (0.011) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `TailwindConfigGenerator` (e.g. with `TestGeneratedConfigIsValidJs` and `TestTailwindConfigGenerator`) actually correct?**
  _`TailwindConfigGenerator` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `DesignSystemGenerator` (e.g. with `TestReasoningMatch` and `TestReasoningContract`) actually correct?**
  _`DesignSystemGenerator` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `fs`, `path`, `fs` to the rest of the system?**
  _1040 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `NrOrderTracking` be split into smaller, more focused modules?**
  _Cohesion score 0.12280701754385964 - nodes in this community are weakly interconnected._