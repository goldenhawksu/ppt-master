---
template_id: aesc_ppt
category: brand
summary: AESC corporate management reviews for CTS, quality, cost, and service logistics — storyline-led, evidence-first decks that turn data into decisions and follow-up actions.
keywords: [aesc, corporate, management-review, storytelling, data-insights, quality, operations]
primary_color: "#2563EB"
canvas_format: ppt169
replication_mode: standard
use_cases: CTS 业务汇报、海外项目分析、质量表现报告、售后物流方案、战略规划
design_tone: Clean, data-dense, professional, evidence-led, bilingual-capable (default English)
placeholders:
  01_cover: ["{{BRAND_LABEL}}", "{{TITLE}}", "{{SUBTITLE}}", "{{AUTHOR}}", "{{DATE}}"]
  02_toc: ["{{BRAND_LABEL}}", "{{PAGE_NUM}}", "{{TOC_ITEM_1_TITLE}}", "{{TOC_ITEM_1_DESC}}", "{{TOC_ITEM_2_TITLE}}", "{{TOC_ITEM_2_DESC}}", "{{TOC_ITEM_3_TITLE}}", "{{TOC_ITEM_3_DESC}}", "{{TOC_ITEM_4_TITLE}}", "{{TOC_ITEM_4_DESC}}", "{{TOC_ITEM_5_TITLE}}", "{{TOC_ITEM_5_DESC}}"]
  02_chapter: ["{{BRAND_LABEL}}", "{{PAGE_NUM}}", "{{CHAPTER_NUM}}", "{{CHAPTER_TITLE}}", "{{CHAPTER_DESC}}"]
  03_content: ["{{BRAND_LABEL}}", "{{PAGE_NUM}}", "{{PAGE_TITLE}}", "{{KEY_MESSAGE}}", "{{CONTENT_AREA}}", "{{SOURCE}}"]
  03a_content_chart_insight: ["{{PAGE_TITLE}}", "{{KEY_MESSAGE}}", "{{INSIGHT}}", "{{EVIDENCE}}", "{{ACTION}}", "{{SOURCE}}"]
  03b_content_comparison: ["{{PAGE_TITLE}}", "{{KEY_MESSAGE}}", "{{BASELINE_LABEL}}", "{{PROPOSED_LABEL}}", "{{BASELINE_EVIDENCE}}", "{{PROPOSED_EVIDENCE}}", "{{COMPARISON_TAKEAWAY}}", "{{SOURCE}}"]
  03c_content_hero_number: ["{{PAGE_TITLE}}", "{{KEY_MESSAGE}}", "{{METRIC_LABEL}}", "{{VALUE}}", "{{BASELINE}}", "{{IMPLICATION}}", "{{SOURCE}}"]
  03d_content_bridge: ["{{PAGE_TITLE}}", "{{KEY_MESSAGE}}", "{{BRIDGE_TAKEAWAY}}", "{{SOURCE}}"]
  03e_content_table_trend: ["{{PAGE_TITLE}}", "{{KEY_MESSAGE}}", "{{TABLE_NOTE}}", "{{ACTION}}", "{{SOURCE}}"]
  04_ending: ["{{THANK_YOU}}", "{{BRAND_LABEL}}", "{{CONTACT_INFO}}", "{{DATE}}"]
---

# AESC-PPT Design Specification

## I. Template Overview

| Property | Description |
| --- | --- |
| Template ID | `aesc_ppt` — the single AESC template. Saying "aesc_ppt模板" / "aesc_ppt template" selects it (see SKILL.md Step 3) |
| Display name | AESC (远景动力) Corporate Template |
| Recurring family | CTS business reports, overseas project analysis, quality performance, service logistics, cost, and strategy reviews |
| Audience and purpose | Business managers assessing evidence, alternatives, and follow-up actions; the deck argues toward a decision |
| Visual voice | Clean, data-dense, professional, bilingual-capable (default English, brand label `ΛESC`; `远景动力` for Chinese decks) |
| Theme | White interior pages, photographic cover, dark photographic ending |
| Canvas | 1280 × 720; margins 56 left/right, evidence body y = 154–680 |

At a glance: a four-zone grey header, a blue bar-and-underline claim title, a one-line implication beneath it, and one dominant piece of evidence per page with a compact conclusion / action beside it.

This is the consolidated AESC template: the corporate page shell, the six-stage reporting story, the semantic-red policy, and the evidence-led data-visualization and icon grammar live here. No other AESC template remains in the library.

The page roster supplies reusable prototypes, not a mandatory agenda, page count, or sequence. The five-item TOC and the storyline in §VIII do not prescribe deck length.

## II. Color Scheme

| Role | Color | Application |
| --- | --- | --- |
| Volt Blue | `#2563EB` | Title accents, section markers, the series / bar / number in focus |
| Navy | `#0D1F6E` | Large headings on light fields where needed |
| Main text | `#1A1818` | Titles and primary body text |
| Charcoal | `#374151` | Key messages, secondary emphasis, totals and context series |
| Body text | `#3A3838` | Descriptions and prose |
| Header gray | `#9B9B9B` | Header metadata and source line |
| Neutral gray | `#6B7280` | Context and baseline series; decreases that are not problems |
| Dividers | `#DDDDDD`, `#EEEEEE` | Header divisions and content rules |
| White | `#FFFFFF` | Page background; cover text |
| Ending dark | `#1C1C1C` | Dark identity field of the photographic ending |
| Ending text | `#DEDEDE`, `#888888` | Closing title and subdued details |
| Eco-Green | `#00C87A` | Source-supported positive meaning only (target met, verified improvement) |
| Alert Red | `#DC2626` | **Semantic only** — see below |

**Semantic red (binding)**: `#DC2626` is the only red permitted, and only for an explicit risk label, warning callout, named-threshold breach, chart anomaly annotation, unresolved-blocker banner, or a deviation the deck itself calls a problem. Never use red (or `#EF4444`, `#B91C1C`, …) for headers, accent bars, dividers, card borders, bullets, icon fills, tinted panels, or decoration. Blue focuses the evidence; neutrals carry context.

"Down" is not "bad": lower cost, defects, delay, or complaints can be an improvement. Decide with one question — *is the value explicitly flagged as a risk, an issue, or below a named threshold?* Yes → `#DC2626`; no → `#6B7280` (direction only, no alarm) with a trend icon. Example: spare-parts cost +12% within the annual cap → gray; first-time-fix rate 63% against an 80% SLA → red. This overrides the generic consultant convention "red = down, green = up".

## III. Typography

Bilingual stack (all template SVGs): `Arial, "Helvetica Neue", "Microsoft YaHei", "PingFang SC", sans-serif`. Executor may switch to a language-specific stack to match the deck (EN: `Arial, "Helvetica Neue", "Segoe UI", sans-serif`; CN: `"方正兰亭黑_GBK", "Microsoft YaHei", "PingFang SC", Arial, sans-serif`).

| Role | Size | Appearance |
| --- | --- | --- |
| Cover title / subtitle / author | 56 / 24 / 28 px | Bold white / white / bold primary ink, title and subtitle over the photograph |
| Chapter numeral / title / description | 52 / 40 / 20 px | Bold blue / bold primary ink / body |
| TOC title / item / description | 28 / 22 / 16 px | Bold primary ink; description in body text |
| Content title | 32 px | Bold primary ink; an evidence-backed claim on analytical pages |
| Key message | 20 px | Charcoal |
| Insight / takeaway | 24–28 px | Bold Volt Blue |
| Hero metric | 80 px | Bold Volt Blue; unit and baseline set separately |
| Chart labels / values | 16 / 18 px | Charcoal; values bold |
| Header | 16 / 13 px | Brand / auxiliary metadata |
| Source | 12 px | Header gray |
| Ending | 36 / 20 / 14 / 12 px | Thanks / brand / contact / date |

Rewrite or change the composition instead of shrinking type below reading size.

## IV. Signature Design Elements

- **Four-zone header** on every interior page: brand at x = 24, domain at x = 480, classification at x = 880, page field at x = 1200; dividers at x = 320, 640, 1120 (y 10–28); lower rule y = 38.
- **Shared title block**: blue bar (x = 56, y = 55, 5 × 38), title baseline y = 84 with a blue 200 px underline at y = 98, key-message baseline y = 128, divider y = 148, evidence body from y = 154, source baseline y = 700.
- **Cover**: photograph at x = 0, y = 44, 1280 × 534, shown in its original tones — no overlay, gradient, filter, or recoloring. Title and subtitle left-aligned over the photograph; author and date in the white lower strip.
- **TOC and chapter**: five TOC rows with pale-blue numerals and restrained rules; the chapter page's tall blue bar (x = 56) is a breathing page between dense evidence.
- **Evidence pages**: claim above evidence; the main visual explains the relationship; a compact conclusion / action sits beside it.
- **AESC "A" arch mark** (`M-54 98 L0 0 L54 98 L40 98 L0 20 L-40 98 Z`, 100 × 98 base) may appear as a watermark with `fill-opacity`, positioned by `transform="translate(cx,cy) scale(s)"`.

## V. Page Roster

| SVG | Role and when to use |
| --- | --- |
| `01_cover.svg` | Cover: brand, title, subtitle, author, date over the fixed photograph |
| `02_toc.svg` | Navigation: up to five title / description rows. Delete unused rows rather than leaving placeholders |
| `02_chapter.svg` | Chapter divider: numeral, title, lead-in description |
| `03_content.svg` | Flexible fallback: claim title, key message, free 1168 × 502 body. Use for process / swimlane, Gantt or milestone timeline, SWOT, SMART action table, resource request, or any custom editable chart |
| `03a_content_chart_insight.svg` | One dominant chart (~62% width) with a conclusion / evidence / action rail. Default page for a ranked, trended, or composed quantitative claim |
| `03b_content_comparison.svg` | Baseline vs proposed (or option A vs B) in two aligned columns with one comparison takeaway. Alternatives, before / after |
| `03c_content_hero_number.svg` | One decision-grade metric with its baseline, implication, and the trend that supports it |
| `03d_content_bridge.svg` | Additive waterfall from a start total to an end total with an attribution takeaway. Cost, delay, or yield bridges |
| `03e_content_table_trend.svg` | Exact-lookup table with direction icons, a context trend, a note, and one action |
| `04_ending.svg` | Closing: thanks, brand, contact, date over the fixed dark photograph |

The chart, table, and numbers in `03a`–`03e` are synthetic illustrations (marked "Illustrative"), not AESC business facts. Replace payloads, titles, units, periods, and sources before use; replace the sample chart with the chart type that fits the relationship (§IX), keeping the layout zones.

## VI. Assets

| File | Usage |
| --- | --- |
| `cover.jpg` | Cover full-bleed photograph (cinematic landscape + AESC "A"); byte-identical to the original |
| `end.jpg` | Ending full-bleed dark photograph (AESC "A" watermark); centered aspect-fill |

**Image lock**: cover pages always reference `cover.jpg` and ending pages `end.jpg`. The pipeline never replaces them with AI-generated or web-sourced images; a custom cover or ending image must be supplied by the user. No business facts or invented chart values are bundled.

## VII. Placeholder Overrides

Contract declared in the `placeholders:` frontmatter. Indexed `{{TOC_ITEM_N_TITLE}}` / `{{TOC_ITEM_N_DESC}}` for N = 1–5. `{{BRAND_LABEL}}` is editable identity wording (`ΛESC` / `远景动力`); `{{CHAPTER_DESC}}` is the chapter lead-in; `{{KEY_MESSAGE}}` is the implication line under the claim title. Evidence pages add `{{INSIGHT}}`, `{{EVIDENCE}}`, `{{ACTION}}`, `{{BASELINE_LABEL}}`, `{{PROPOSED_LABEL}}`, `{{BASELINE_EVIDENCE}}`, `{{PROPOSED_EVIDENCE}}`, `{{COMPARISON_TAKEAWAY}}`, `{{METRIC_LABEL}}`, `{{VALUE}}`, `{{BASELINE}}`, `{{IMPLICATION}}`, `{{BRIDGE_TAKEAWAY}}`, `{{TABLE_NOTE}}`.

Milestone-driven action plans prefer a clear ThinkCell-style Gantt (`gantt_chart`) with readable dates, milestones, and dependencies over decorative timeline cards.

## VIII. Business Reporting Story Framework

**Trigger**: AESC management reviews (CTS 业务汇报、海外项目分析、质量表现报告、售后物流方案). Strategist carries the selected evidence and message into the Content Outline (design_spec §IX); Executor realizes the visual relationships. Chart selection follows §IX of this file; icon use follows §X.

### A. Narrative Arc

The deck is not "show what we did" — it helps management see why the business needs to change, where the problem sits, what foundation already exists, what to do next, and what support is needed. Default to this six-stage arc; merge, reorder, or drop stages when the confirmed audience, purpose, and page count call for it, but keep actions and resource requests identifiable even when they share a page.

| # | Management question | Evidence to carry forward | Default TOC wording |
| --- | --- | --- | --- |
| 1 | Scope and baseline — 这个业务管什么？现有基础是什么？ | Reporting boundary, operational scale, existing capability, reference period | 管理范围与基础能力 |
| 2 | Gap and priority — 哪里有问题？有多严重？ | Actual vs comparable baseline; affected region, customer, process | 执行侧痛点与现状差距 |
| 3 | Explanation — 为什么会这样？抓手在哪里？ | Factor contributions, observed handoffs, case evidence; separate hypothesis from verified cause | 问题根因分析 |
| 4 | Alternatives — 怎么解决？如何取舍？ | Comparable options, assumptions, trade-offs, expected effects | 改进方案设计 |
| 5 | Execution — 谁来做、何时完成？ | Deliverable, owner, acceptance measure, deadline, dependencies | 行动计划 |
| 6 | Decision required — 需要什么支持？回报是什么？ | Requested support, cost, benefit horizon, uncertainty, consequence of delay | 资源诉求与预期收益 |

Stages 5 and 6 stay separate: an action plan says what will be done; a resource request says what support makes it possible and what it returns.

### B. Visual Reasoning Patterns

Pick the form from the relationship the reader must understand, not from a chart whitelist.

| Stage | Question | Preferred prototype and visual | Adapt when the fit fails |
| --- | --- | --- | --- |
| 1 Baseline | What is the scope and capability? | `03c` hero number + trend; `03e` overview table; a regional map when geography is the argument | Aligned rows for membership; a decorative ring does not establish order or share |
| 2 Gap | Where, and by how much? | `03a` ranked / grouped / stacked bar with the exception highlighted; heatmap for region × step | `03e` table when exact lookup is the task |
| 3 Explanation | What drives the gap? | `03d` waterfall for additive attribution; Pareto for cumulative contribution; annotated chart + case retrospective in `03` | State the driver as a hypothesis until verified |
| 4 Alternatives | How do options differ? | `03b` parallel columns on a shared scale; scatter of cost vs benefit | Labeled comparison table for unlike measures; independent workstreams get no arrows |
| 5 Execution | Who does what, when? | `gantt_chart` with milestones and dependencies; swimlane when ≥ 2 functions hand off; SMART action table | Milestone timeline when only event dates exist; mark pending dates instead of inventing durations |
| 6 Decision | What do we need, and what returns? | Budget breakdown table; ROI bar (investment vs return) | Keep uncertainty and delay consequence visible |

Every analytical page in stages 2–4 carries at least one chart, diagram, or structured visual; a bullet list is never the sole evidence. A repeated grid of unrelated KPI cards is not the default composition.

### C. Evidence Completeness and Traceability

| Evidence status | What the page and its trace retain |
| --- | --- |
| Observed actual | Source document/system, sheet or page locator, cut-off date, inclusion/exclusion rules |
| Derived value | Source inputs, formula, aggregation or weighting, rounding; label as calculated |
| Target or benchmark | Who set it, applicable population/period, whether its definition matches the actual |
| Forecast or scenario | Explicit label, assumptions, horizon, range or sensitivity when supported |
| Missing or conflicting | Name the missing field or conflicting definitions; keep the conclusion provisional |
| Qualitative observation | Case, interview, inspection, or process record; label an unverified explanation a hypothesis |

**Source authority**: actual results come from approved source facts only. Template demonstration values are not AESC data. Preserve missing values as missing; a target, estimated benefit, or assumption is not an observed result.

**Reconciliation**: recompute totals, shares, changes, and target attainment from retained inputs; headline metrics, charts, tables, and annotations must agree. Distinguish percentage change from percentage-point change; explain rounding residuals, excluded categories, and differing denominators. Put a concise, locatable source in the footer; "internal data" is insufficient. Longer calculations go to speaker notes or an appendix page.

### D. From Evidence to Message and Action

**Claim title**: analytical pages carry an evidence-backed takeaway; a cover, agenda, or divider keeps a functional title. The key-message line adds the implication or decision rather than repeating the title. Pattern: `[value] vs [benchmark] — [management implication]`.

**Worked example (hypothetical)**: inputs "on-time delivery 400/500 in Q1, 430/500 in Q2, target 90%" → derived 80% → 86%, +6 pp, still 4 pp below target → compare both rates against a shared target marker with counts labeled → claim "On-time delivery improved 6 pp; the target gap is still 4 pp" → implication: the data does not show which intervention caused it → action tied to owner, acceptance measure, deadline, or marked pending.

**Per-row action (SMART)**: specific deliverable, measurable acceptance criterion, accountable function, feasible resource basis, deadline. Tie each resource request to the action it enables and its expected benefit. Pending owners, approvals, budgets, or dates stay visibly pending; never manufacture commitments to complete a table.

### E. Page Readback

| Readback question | Repair when unclear |
| --- | --- |
| Can the reader state the decision or finding? | Refocus the title; remove competing claims |
| Does the visual itself reveal the comparison or relationship? | Align shared dimensions, expose a baseline, or change form |
| Can the reader reproduce the critical number? | Restore inputs, formula, locator |
| Does the visual imply only what the source establishes? | Remove unsupported arrows, causal labels, areas, progress percentages |
| Is the important exception visible beside the aggregate? | Add the breakdown and its implication |
| Is the evidence legible at viewing size? | Rephrase or move secondary detail to a follow-up page |

## IX. Evidence-Led Data Visualization

**Principle — maximize useful evidence, not chart count.** Review every quantitative claim for the chart that makes the argument visible fastest. Prefer a chart over a list of numbers when comparison, change, composition, distribution, or attribution carries the argument; keep a table for lookup, a hero number for one quantity, a diagram for qualitative relationships. Explain an uncharted quantitative claim in the page rationale; never invent values to raise coverage.

Strategist records the chosen chart per page in `page_charts` (spec_lock); Executor adapts the matching `templates/charts/` SVG inside the evidence prototype's zones. Consult `templates/charts/charts_index.json` and each entry's "Skip if" rule before choosing; the table below is a starting point, not a whitelist.

| Intent | Starting points (`templates/charts/`) | Prototype |
| --- | --- | --- |
| Ranking / magnitude | `horizontal_bar_chart`, `bar_chart`, `dumbbell_chart` | `03a` |
| Deviation vs target | `bullet_chart`, `butterfly_chart`, `progress_bar_chart` | `03a` |
| Change over time | `line_chart`, `area_chart`, `dual_axis_line_chart` | `03c`, `03a` |
| Part-to-whole | `stacked_bar_chart`, `donut_chart`, `treemap_chart` | `03a` |
| Regional / multi-series comparison | `grouped_bar_chart`, `heatmap_chart` | `03a`, `03b` |
| Distribution / concentration | `box_plot_chart`, `pareto_chart` | `03a` |
| Correlation / cost-benefit | `scatter_chart`, `bubble_chart`, `quadrant_bubble_scatter` | `03a` |
| Additive attribution | `waterfall_chart` | `03d` |
| Flow / conversion | `sankey_chart`, `funnel_chart` | `03` |
| Schedule | `gantt_chart`, `project_schedule_table`, `timeline` | `03` |
| Exact lookup | `basic_table`, `consulting_table`, `comparison_table` | `03e` |

A waterfall answers additive attribution, not arbitrary flow; a Pareto answers cumulative contribution; a pie / donut is for 3–5 parts that sum to a meaningful whole.

**Persuasion rules**

- One dominant chart per page; the claim title states what the chart proves.
- Blue is the series, bar, or point the claim is about; everything else is Neutral Gray / Charcoal. Do not use a rainbow palette.
- Label values directly; drop gridlines and legends the labels make redundant. Sort ranked bars by value. Bars start at zero; use actual calendar spacing on time axes.
- Show period, unit, denominator, baseline / target, and source wherever they affect interpretation. Distinguish correlation from causation.
- Annotate the exception (the breach, the outlier, the step that moves the total) with a short callout; use `#DC2626` only when §II allows it.
- Keep missing observations missing unless the source says no record means zero.
- Charts stay editable SVG geometry, never a screenshot. Run `verify-charts` on decks with data charts before post-processing.

Vary neighboring pages when the argument changes; do not force a chart quota or width ratio for variety.

## X. Icons as Evidence Marks

An icon earns its place only when it carries meaning a number or word would carry slower: a direction, a state, a category, or a step. Data and chart stay primary; the icon is the quick-read tag beside them. Never use icons as bullets or decoration, and never to stand in for a quantity.

- **One library**: `chunk-filled` (compact solid silhouettes that stay crisp when projected and match the data-dense tone). Lock it as the deck's icon library; when an exact icon is missing, take the nearest object within it, or let a chart, number, or typography carry the meaning. Reference as `data-icon="chunk-filled/<name>"`.
- **Where an icon is persuasive**: trend direction beside a KPI or delta; status of a risk or target (met / at risk / breached); category identity in a comparison or component breakdown; step type in a process or handoff; action owner or deliverable type in an action table; the conclusion / evidence / action headings of a chart-insight rail.
- **Size and color**: 24–32 px inline with 16–22 px text, 40–48 px as a category anchor; at most one icon per unit and roughly six per page. Volt Blue by default, Neutral Gray for context, Eco-Green and Alert Red only with their §II meaning. Red is never for a mere decrease: use `arrow-trend-down` in `#6B7280`.

Curated starting pool (all verified in `chunk-filled`; pick the drawable object, not the abstract concept):

| Meaning | Icon objects |
| --- | --- |
| Trend up / down | `arrow-trend-up`, `arrow-trend-down` |
| Risk, warning, breach | `triangle-exclamation`, `circle-exclamation` |
| Met, verified, approved | `circle-checkmark`, `badge-check`, `shield-check` |
| Target, goal, KPI gap | `target-arrow`, `gauge-high`, `gauge-low` |
| Time, schedule, delay | `clock`, `calendar`, `hourglass-half-top`, `stopwatch` |
| Logistics, delivery | `truck`, `ship`, `plane`, `box`, `route` |
| Operations, manufacturing | `factory`, `wrench`, `toolbox`, `cog`, `battery-full`, `bolt` |
| Cost, budget | `dollar`, `coin`, `wallet`, `receipt` |
| Region, site | `globe`, `map-pin`, `building` |
| People, owner | `users`, `user` |
| Insight, idea | `lightbulb` |
| Chart type cue | `chart-bar`, `chart-line`, `chart-pie` |
| Feedback loop | `arrows-rotate-clockwise` |
| Milestone, deliverable | `flag`, `clipboard`, `list-ordered` |

The pool is a recall aid, not a whitelist; any `chunk-filled` object that carries the page's meaning is valid.
