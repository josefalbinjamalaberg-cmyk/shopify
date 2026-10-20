## Skills

This repo ships design skills in `.claude/skills/`. Use them — don't freehand design work:

- Any UI, layout, styling or responsive change in `sections/`, `assets/*.css`, `templates/` or `layout/`: use `design-taste-frontend` and `ui-ux-pro-max` first.
- Copy, tone of voice, product messaging or brand visuals: use `brand`.
- Colors, spacing, typography scales or CSS variables: use `design-system`.
- Banners, hero images or ad/social creatives: use `banner-design`.
- Logos, icons, mockups or broader identity work: use `design`.
- Presentations: use `slides`.

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

These rules apply only when the `graphify` CLI is installed (`command -v graphify`). If it isn't, skip them and use normal search and file reads.

Rules:
- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).
