---
deck_id: aesc_ppt
kind: deck
category: brand
summary: AESC corporate management reviews for CTS, quality, cost, and service logistics, supporting evidence-led decisions and follow-up reading.
keywords: [aesc, corporate, management-review, quality, operations]
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
page_count: 5
---

# AESC-PPT Design Specification

## I. Template Overview

| Property | Description |
| --- | --- |
| Template ID | `aesc_ppt` |
| Display name | AESC Corporate Template |
| Recurring family | CTS, overseas operations, quality performance, service logistics, and business management reviews |
| Audience and purpose | Business managers assessing evidence, alternatives, and follow-up actions |
| Delivery | Presented discussion with readable sources for subsequent review |
| Visual voice | Clean, professional, data-first, bilingual-capable |
| Theme | White interior pages, photographic cover, dark photographic closing |
| Structure | One `aesc_corporate_master` family; five newly authored Layout prototypes |
| Review | Delegated prototype review completed on 2026-10-25; five roles and 33 text carriers checked |

The user confirmed rebuilding the legacy AESC system while retaining the
`aesc_ppt` name and registering it in the library. This workspace is newly
authored from the legacy SVG evidence, not an in-place metadata conversion.
It preserves the five basic page roles without importing the ten-page roster
of the independently registered `aesc_ppt_data_viz` workspace.

The source's chapter examples describe management-report situations, not
mandatory chapters or a fixed agenda. Downstream planning decides the number,
order, and application of these prototypes from the confirmed communication
contract. Neither the five prototypes nor the five-item TOC prescribe deck length.

## II. Color Scheme

| Role | Color | Application |
| --- | --- | --- |
| Volt Blue | `#2563EB` | Accents, chapter numerals, evidence focus |
| Navy | `#0D1F6E` | Large headings on light fields where needed |
| Main text | `#1A1818` | Titles and primary body text |
| Charcoal | `#374151` | Key messages and secondary emphasis |
| Body text | `#3A3838` | Descriptions and prose |
| Header gray | `#9B9B9B` | Header metadata and source line |
| Neutral gray | `#6B7280` | Context and non-problem decreases |
| Dividers | `#DDDDDD`, `#EEEEEE` | Header divisions and content rules |
| White | `#FFFFFF` | Master background and cover text |
| Ending dark | `#1C1C1C` | Photographic ending's dark identity field |
| Ending text | `#DEDEDE`, `#888888` | Closing title and subdued details |
| Eco-Green | `#00C87A` | Source-supported positive meaning |
| Alert Red | `#DC2626` | Explicit risks, warnings, or threshold breaches |

Use the AESC semantic-red decision at the shared adaptation owner in §VIII.
The inherited reduced-opacity TOC numerals are secondary to their black titles;
blue and neutral context carry the primary evidence hierarchy.

## III. Typography

Bilingual stack: `Arial, "Helvetica Neue", "Microsoft YaHei", "PingFang SC", sans-serif`.
Use language-appropriate installed faces when applying the template.

| Role | Size | Appearance |
| --- | --- | --- |
| Cover title | 56 px | Bold, white over the original photograph |
| Cover subtitle | 24 px | White |
| Cover author | 28 px | Bold primary ink |
| Chapter numeral | 52 px | Bold blue |
| Chapter title | 40 px | Bold primary ink |
| Content title | 32 px | Bold primary ink |
| TOC title / item | 28 / 22 px | Bold primary ink |
| Key message / chapter description | 20 px | Charcoal or body text |
| TOC description | 16 px | Body text |
| Header | 16 / 13 px | Brand / auxiliary metadata |
| Source | 12 px | Header gray |
| Closing | 36 / 20 / 14 / 12 px | Thanks / brand / contact / date |

Choose concise evidence-backed titles. Carrier boxes are reusable text frames,
not a promise that arbitrary content fits; rewrite or adapt the layout instead
of shrinking type without regard to reading conditions.

## IV. Signature Design Elements

- Retain the original four-zone header: brand at x = 24, domain at x = 480,
  classification at x = 880, page field at the right. Dividers stand at
  x = 320, 640, and 1120; the lower rule is y = 38.
- The cover photograph occupies x = 0, y = 44, width = 1280, height = 534.
  Preserve its original bitmap bytes and natural tones. Do not add an overlay,
  gradient, filter, recoloring, or local darkening behind the title. The existing
  centered aspect-fill frame is retained; it is not a bitmap edit.
- Keep the cover title and subtitle left-aligned over the photograph and the
  author/date in the white lower strip. The brand remains editable for
  language-appropriate `ΛESC` or `远景动力` wording.
- Keep five TOC rows with pale blue numerals, black titles, short descriptions,
  and restrained horizontal rules. This is a reusable five-item prototype,
  not a fixed number of sections for future reports.
- Keep the chapter's tall blue bar at x = 56 and its left-aligned numeral,
  title, and description. It provides a breathing page between dense evidence.
- The content prototype retains title baseline y = 84, key-message baseline
  y = 128, divider y = 148, and the 1168 × 502 evidence frame at x = 56, y = 154.
  Its source baseline is y = 700. The former centered content guide and duplicate
  footer page number are not authored content and are omitted.
- General body/object carriers start upper-left. Centered closing slots and the
  centered page field at x = 1200 are deliberate short focal/field exceptions. Fixed
  header metadata retains its centered alignment.
- The shared white background belongs to the Master; page chrome and photographs
  belong to Layouts. Slide placeholders carry variable text. No source native
  hierarchy is claimed: the legacy SVGs supplied visual evidence only.

## V. Page Roster

Every prototype declares Master `aesc_corporate_master` / name `AESC Corporate`.
Each Layout has exactly one complete prototype. Header brand and page-number
slots are present on the three interior-page layouts.

| SVG | Layout key | Reusable role and slots |
| --- | --- | --- |
| `01_cover.svg` | `aesc_corporate_cover` | Cover: editable brand, title, subtitle, author, date |
| `02_toc.svg` | `aesc_corporate_toc` | Navigation: brand, page number, TOC title, five indexed title/description pairs |
| `03_chapter.svg` | `aesc_corporate_chapter` | Chapter: brand, page number, chapter number, title, description |
| `04_content.svg` | `aesc_corporate_content` | Flexible evidence: brand, page number, claim title, key message, object area, source |
| `05_ending.svg` | `aesc_corporate_ending` | Closing: thanks, editable brand, contact, date |

The body frame is a flexible evidence area, not a KPI-card prescription. It
can support a selected chart, lookup table, process, comparison, or qualitative
diagram according to the actual argument. Native chart/table implementations
use compatible typed slots in a valid adaptive Layout when required; preserve
the type and index of any reused Layout slot.

## VI. Assets

| Workspace asset | Source and preserved treatment |
| --- | --- |
| `images/cover.jpg` | Original `templates/layouts/aesc_ppt/cover.jpg`; byte-identical copy, no tone processing |
| `images/end.jpg` | Original `templates/layouts/aesc_ppt/end.jpg`; byte-identical copy, original centered aspect-fill frame |

Use only these two adopted identity photographs. No business facts, project
images, invented chart values, or unrelated generated assets are bundled.
The textual brand remains editable; provenance does not grant additional
asset distribution rights. The legacy source folder remains unchanged evidence.

## VII. Placeholder Overrides

Use the inherited indexed `{{TOC_ITEM_N_TITLE}}` / `{{TOC_ITEM_N_DESC}}` family
for N = 1–5. `{{BRAND_LABEL}}` is editable identity wording, with `ΛESC` and
`远景动力` as the source examples; `{{CHAPTER_DESC}}` is the chapter lead-in.
All actual slot types, indices, frames, and carrier baselines are declared in
the SVGs. ThinkCell-style Gantt schedules remain the source preference for
milestone-driven action plans, with readable dates, milestones, and dependencies.

## VIII. Data Visualization Grammar

After this Deck is selected, read
`${SKILL_DIR}/templates/decks/aesc_ppt_data_viz/templates/design_spec.md` §VIII
and follow its reference-loading trigger for Default planning/execution and
Quick active context. That section remains the single owner of AESC's
quantitative-evidence preference, source-grammar adaptation, semantic-red rule,
and supplementary audit trigger. Resolve paths from the retained absolute
Skill root, not from this spec's copied project location.

Apply those rules to this workspace's own five prototypes and actual compatible
Layout keys; do not import the other Deck's ten-page roster or assign its keys
to these pages. This base template contains no demonstration chart payloads.
Assess actual quantitative claims in generated pages and audit filled evidence,
not the unfilled template markers.
