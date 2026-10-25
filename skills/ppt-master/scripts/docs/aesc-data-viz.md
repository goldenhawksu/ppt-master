# AESC Data Visualization Audit

## 1. Scope and Invocation

`check_aesc_viz.py` is a supplementary, read-only SVG audit. AESC's chart
preference and adaptation rules are owned by
`templates/decks/aesc_ppt_data_viz/templates/design_spec.md` §VIII, not by this tool. It does not activate a runtime, select a template,
create a Design Spec, modify a lock, or certify native PPTX export.

```powershell
python "<absolute Skill root>/scripts/check_aesc_viz.py" "<project root>" --require-charts --json
```

Accepted targets are a project with `svg_output/`, a directory of authored
slide SVGs, or one SVG file. The shared slide-roster discovery excludes
non-slide SVG resources. `--json` prints one JSON document to stdout without
creating files. Exit codes: `0` for no errors, `1` for audit errors, `2` for
argument, catalog, or I/O setup errors. Warnings do not change the exit code.
Without `--require-charts`, a chartless deck is legitimate; it is not evidence
that every data page has been reviewed.

Run before the active runtime's existing Verify Charts and final SVG gates.
This tool is invoked by the template instructions, not automatically by the
exporter; a standalone export does not enforce it.

## 2. Minimal Authoring Contract

Annotate the existing semantic chart group; do not create a second group for
the audit or change the native payload schema. These attributes are authoring
metadata, not visible slide content.

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720"
     data-viz-page-type="chart_insight_rail">
  <text id="cost-takeaway" x="56" y="100" font-size="32">Cost fell 18%</text>
  <g id="cost" data-viz-intent="ranking" data-viz-chart="horizontal_bar_chart">
    <rect x="100" y="200" width="360" height="32" fill="#2563EB"/>
    <rect x="100" y="260" width="240" height="32" fill="#6B7280"/>
  </g>
  <text id="cost-source" x="56" y="670" font-size="12">Source: reviewed ledger; USD; 2026 Q3</text>
</svg>
```

| Field | Contract |
| --- | --- |
| Chart `id` | Existing unique semantic object key |
| `data-viz-intent` | `deviation`, `ranking`, `distribution`, `change_over_time`, `part_to_whole`, `magnitude`, `correlation`, `spatial`, or `flow` |
| `data-viz-chart` | A live `charts_index.json` key; or `custom/<name>` with nonblank `data-viz-reason` for a justified editable custom chart |
| Takeaway text | A visible SVG `text` with default ID `<object>-takeaway`; `data-viz-title` may reference a different text ID |
| Source text | A visible SVG `text` with default ID `<object>-source`; `data-viz-source` may reference a different text ID; shared page sources may be referenced by several charts |
| Root `data-viz-page-type` | Optional rhythm hint: `chart_insight_rail`, `hero_number`, `comparison_swing`, `bridge_waterfall`, or `table_with_trend` |

Discovery includes annotated chart groups, native Chart replacement groups,
and groups named by scoped `chart-plot-area: object=...` comments. Missing
annotations on discovered charts are errors. A lone legacy unscoped marker
without any annotated chart group is an error requiring object identification.
Qualitative diagrams, ordinary lookup tables, and standalone metrics do not
need to masquerade as chart groups.

The tool checks unique IDs, supported intent values, catalog membership,
nonempty and non-placeholder takeaway/source text, common hidden XML
properties, and at least one editable primitive inside each chart. It warns
about weak takeaway cues, missing page-type hints, and three neighboring pages
sharing the same declared page type. A custom chart is not excluded merely
because this checkout has no matching catalog asset.

## 3. Evidence Boundaries

- Catalog membership does not establish intent/chart suitability; review the
  actual analytical question, the source grammar's Skip-if, and catalog summary.
- An arbitrary unannotated SVG chart with no coordinate/native marker cannot
  be reliably distinguished from a diagram. The audit cannot calculate the
  denominator of all quantitative claims or prove complete chart coverage.
- Presence of source text does not prove its truth, precision, or accessibility.
  Nonempty `text` and common visibility flags are checked, not clipping,
  off-canvas positioning, contrast, paint inheritance, or rendered legibility.
- An editable primitive does not prove correct geometry or encoding. Keep
  Verify Charts, native-payload parity checks, missing-data review, waterfall
  closure, source reconciliation, and visual review at their existing owners.
- This does not convert the legacy AESC source package into a structured
  workspace. Current template validation and Create Template confirmation
  remain required before publishing a replacement.

## 4. Vendored Reference Provenance

The five files under `references/data-viz-grammar/` come from the user-supplied
independent ZIP. Only carriage returns were normalized and a final newline
was supplied where needed; source wording and script behavior were retained.
They are bundled references, not a claim that a global host skill was installed.
The source declares MIT licensing and `author: hermes`; its attribution remains
in the vendored Skill. HTML/Excel/matplotlib companions are conditional resources,
not PPT runtime dependencies.

Archive SHA-256:
`abe951966dc976a0a8588cb87f3cd980fc131828949529fd516ee17feea84332`.

| Original path | Original SHA-256 prefix |
| --- | --- |
| `data-viz-grammar/SKILL.md` | `a1369202715bd24c` |
| `data-viz-grammar/references/excel-chart.md` | `054fe47eb7d6402c` |
| `data-viz-grammar/references/html-single-file.md` | `5a9791b790c3b132` |
| `data-viz-grammar/references/matplotlib.md` | `fa0ca370e4cd7785` |
| `data-viz-grammar/scripts/check_html_viz.py` | `ffa7d2e528d033a1` |

The independent ZIP supplies no `check_viz_wiring.py`, `check_chart_lib.py`,
`check_deck_viz.py`, editorial-era index, or `visual-grammar-v2/`. Commands and
links for those names in the historical reference describe its source system,
not capabilities installed by this integration. The AESC adaptation points to
the local catalog and current PPT verification stages instead.
