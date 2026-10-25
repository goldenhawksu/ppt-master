---
deck_id: aesc_ppt_data_viz
kind: deck
category: brand
summary: AESC branded data insights for CTS, quality, cost, and service-logistics management reviews.
keywords: [aesc, data-insights, quality, operations, management-review]
primary_color: "#2563EB"
canvas_format: ppt169
canvas_width: 1280
canvas_height: 720
canvas_viewbox: "0 0 1280 720"
source_canvas_width: 1280
source_canvas_height: 720
source_viewbox: "0 0 1280 720"
replication_mode: standard
native_structure_mode: structured
page_count: 10
---

# AESC Data Insights Design Specification

## I. Template Overview

| Property | Description |
| --- | --- |
| Template ID | `aesc_ppt_data_viz` |
| Display name | AESC Data Insights |
| Application | CTS, quality, cost, overseas operations, and service-logistics reviews |
| Audience and purpose | Business managers evaluating evidence, implications, and decisions |
| Reading context | Presented discussion plus readable evidence for follow-up review |
| Canvas | 1280 × 720; `viewBox="0 0 1280 720"` |
| Safe body | x = 56–1224; evidence below y = 214; sources at y = 688 |
| Structure | One `aesc_data_viz_master` family and ten distinct Layouts |
| Review status | User-reviewed on 2026-10-25; original cover tones preserved |

Newly authored workspace, not an in-place structural migration of
`templates/layouts/aesc_ppt`. The roster supplies reusable prototypes, not a
mandatory agenda, page count, or sequence for future presentations.

## II. Color Scheme

| Role | Color | Meaning |
| --- | --- | --- |
| Volt Blue | `#2563EB` | Evidence focus, accents, selected series |
| Navy | `#0D1F6E` | Identity headings on light backgrounds |
| Primary ink | `#1A1818` | Titles and primary text |
| Charcoal | `#374151` | Body and key messages |
| Neutral gray | `#6B7280` | Context, secondary series, non-problem decreases |
| Header gray | `#9B9B9B` | Auxiliary metadata |
| Dividers | `#DDDDDD`, `#EEEEEE` | Structural separation |
| White | `#FFFFFF` | Shared Master background |
| Dark ending | `#1C1C1C`, `#DEDEDE` | Ending background and text |
| Eco-Green | `#00C87A` | Source-supported positive meaning |
| Alert Red | `#DC2626` | Explicit risks, warnings, threshold breaches, or problems only |

Red is semantic, never decorative. A decrease is not automatically negative:
lower cost, defects, delay, or complaints may be an improvement. Use neutral
gray or blue unless the source establishes a risk. Do not mechanically apply
green-for-up/red-for-down formatting without checking business meaning.

## III. Typography

The bilingual stack is `Arial, "Helvetica Neue", "Microsoft YaHei", "PingFang SC", sans-serif`.
Choose language-appropriate installed fonts when applying the workspace.

| Role | Size | Treatment |
| --- | --- | --- |
| Cover title | 56 px | Bold white over original photograph |
| Content title | 32 px | Bold ink; evidence-backed conclusion when supported |
| Chapter title | 40 px | Primary ink |
| Key message | 20 px | Charcoal |
| Body | 18–24 px | Ink or charcoal |
| Hero metric | 80 px | Blue; unit and baseline supplied separately |
| Header and source | 12–16 px | Neutral gray |

Bounds are capacity references, not instructions to shrink text arbitrarily.
Rewrite or use a compatible composition when evidence does not fit.

## IV. Signature Design Elements

- Preserve the four-zone AESC header, gray rules, blue title accent, and white evidence field.
- Retain original cover and ending photographs as identity assets.
- Display the cover photograph without overlays, gradients, filters, recoloring,
  or local darkening. Preserve the original bitmap bytes and natural tones;
  do not add a scrim behind the cover title.
- Put the claim above its evidence and keep source, unit, period, and baseline visible when needed.
- Keep the white background Master-owned. Headers, dividers, accents, and imagery belong to Layouts.
- Preserve placeholder types and indices; chart/table slots carry native payloads, not screenshots.

## V. Page Roster

All pages declare Master key `aesc_data_viz_master` / name `AESC Data Insights`.

| SVG | Layout key | Role and principal slots |
| --- | --- | --- |
| `01_cover.svg` | `aesc_cover` | Cover: title, subtitle, presenter, date |
| `02_toc.svg` | `aesc_toc` | Navigation: title and four section/description pairs |
| `03_chapter.svg` | `aesc_chapter` | Chapter: number, title, subtitle |
| `04_content.svg` | `aesc_content` | General evidence: title, key message, editable object body |
| `04a_chart_insight.svg` | `aesc_chart_insight` | Native ranked chart; insight, evidence, action rail |
| `04b_comparison_swing.svg` | `aesc_comparison` | Baseline/proposed evidence and comparison takeaway |
| `04c_hero_number.svg` | `aesc_hero_number` | Metric, baseline, implication, native trend chart |
| `04d_bridge_waterfall.svg` | `aesc_bridge` | Native additive waterfall and bridge takeaway |
| `04e_table_with_trend.svg` | `aesc_table_trend` | Native table, native trend, note, action |
| `05_ending.svg` | `aesc_ending` | Closing: thanks, contact information, date |

Body prototypes also provide page-number and source placeholders. Picker names
and exact bounds, indices, and types are declared in each SVG. The chart/table
payloads are illustrative editable examples, not business facts.

## VI. Assets

| File | Provenance and usage |
| --- | --- |
| `images/cover.jpg` | Byte-preserved from legacy AESC template; cover crop |
| `images/end.jpg` | Byte-preserved from legacy AESC template; dark ending |

The `ΛESC` wordmark follows the legacy textual identity. Provenance does not
establish additional distribution rights. All demonstration chart values and
table rows are synthetic. Replace payloads, titles, units, periods, sources,
and illustrative labels before actual use.

## VII. Placeholder Overrides

Preserve typed native chart/table payloads. For unsupported native schemas use
editable vectors in the general-content object slot or a valid adaptive Layout;
never reinterpret a reused chart/table slot as an object slot.
For Gantt requests, prefer clear ThinkCell-style schedules with readable
milestones and dependencies rather than decorative timeline cards.

## VIII. Data Visualization Grammar

**Trigger**: after this template has been selected, the planning role reads
`${SKILL_DIR}/references/data-viz-grammar/SKILL.md` before choosing data-page
visualizations. Default carries the decisions into its existing §IX object
entries; Quick makes them in active context without creating a Design Spec or
lock. The executing role reads the same reference before chart construction.
Resolve these paths from the retained absolute Skill root, not from a copied
project template. This section is the AESC-specific adaptation of that reference.

**Default — maximize useful evidence, not chart count (may override)**: review
every quantitative claim for a suitable chart. Prefer charts over lists of
numbers when comparison, change, composition, distribution, or attribution
carries the argument. Keep a table for lookup, a hero number for one quantity,
and a diagram for qualitative relationships. Explain an uncharted quantitative
claim in the existing page rationale; never invent values to increase coverage.

| Intent | Available catalog starting points |
| --- | --- |
| Deviation | `horizontal_bar_chart`, `bullet_chart`, `butterfly_chart` |
| Ranking | `horizontal_bar_chart`, `column_chart`, `dumbbell_chart` |
| Distribution | `histogram_chart`, `box_plot_chart`, `pareto_chart` |
| Change over time | `line_chart`, `area_chart`, `column_chart` |
| Part-to-whole | `stacked_bar_chart`, `donut_chart`, `treemap_chart` |
| Magnitude | `horizontal_bar_chart`, `column_chart`, `grouped_bar_chart` |
| Correlation | `scatter_chart`, `bubble_chart` |
| Spatial | A sourced editable map when geography is the argument; otherwise a ranked bar chart |
| Flow | `sankey_chart`, `waterfall_chart`, `funnel_chart` |

These are starting points, not a whitelist or a substitute for the live
`${SKILL_DIR}/templates/charts/charts_index.json` summaries and source grammar's
intent/Skip-if judgments. A waterfall answers additive attribution, not arbitrary
flow; a Pareto answers cumulative contribution, not raw-sample distribution.

**Default — evidence-led page composition (may override)**: start with
`chart_insight_rail` (about 62% chart plus conclusion/evidence/action),
`hero_number`, `comparison_swing`, `bridge_waterfall`, or `table_with_trend`.
These are composition names, not automatically valid PowerPoint Layout keys.
Use the actual compatible Layout keys in §V. Vary neighboring pages when the argument changes;
do not force a chart quota, exact width ratio, or new layout to satisfy variety.

**AESC adaptation**: §II–§IV own identity, typography, and red semantics.
Use Volt Blue to focus the evidence and neutrals for context; green/red need
their defined meaning. The source grammar's palette, 24-character title ceiling,
fixed page repetitions, and blanket card restrictions are reference heuristics,
not overrides of the confirmed communication contract. Write evidence-backed
takeaway titles in the deck's language. Distinguish correlation from causation.
Use actual calendar spacing; missing observations stay missing unless the source
explicitly establishes that no record means zero. Show period, unit, denominator,
baseline/target, and source wherever they affect interpretation.

**Implementation**: keep charts as editable SVG/DrawingML. Prefer a native
PowerPoint Chart plus embedded data when the active profile declares it
native-ready; use `${SKILL_DIR}/references/native-data-interface.md` on its normal
trigger. A chart not representable by the native schema remains editable vector
geometry rather than a screenshot. The independent package does not supply the
95-chart catalog, `visual-grammar-v2`, or PPT gate scripts named in its examples;
use this checkout's live catalog and existing Verify Charts stage instead.

**Verification**: annotate chart groups using the minimal audit attributes in
`${SKILL_DIR}/scripts/docs/aesc-data-viz.md` §2, then run
`python "${SKILL_DIR}/scripts/check_aesc_viz.py" "<project_path>" --require-charts --json`
when the deck contains data charts, before the selected runtime's existing
Verify Charts and final SVG checks. The audit is supplementary: its success
does not certify source truth, geometry, native-payload parity, or visual layout.
The audit contract and limitations are also printed by that script's `--help`;
they remain available when repository documentation is not installed.

The current checkout contains 33 chart catalog entries, not 95. Audit filled
pages only: unfilled prototypes intentionally retain title/source placeholders.
Typed chart/table prototypes use supported native payloads with embedded data.
Unsupported chart forms use editable vectors in compatible object slots rather
than changing the types of reused chart/table slots.
