# AESC-PPT Design Specification

## I. Template Overview

| Property | Description |
| --- | --- |
| **Template Name** | AESC-PPT |
| **Display Name** | AESC (远景动力) Corporate Template |
| **Template ID** | `aesc_ppt` |
| **Use Cases** | CTS 业务汇报、海外项目分析、质量表现报告、售后物流方案、战略规划 |
| **Design Tone** | Clean, data-dense, professional, dual-language (default English) |
| **Theme Mode** | Hybrid (white content pages + photo cover + dark photo ending) |
| **Default Language** | English (brand label: `ΛESC`)；中文演示时替换为 `远景动力` |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| **Format** | Standard 16:9 |
| **Dimensions** | 1280 × 720 px |
| **viewBox** | `0 0 1280 720` |
| **Safe Margins** | 56px left/right, 46px top, 40px bottom |
| **Content Area** | x: 56–1224, y: 150–680 |

## III. Color Scheme

| Role | Color | Usage |
| --- | --- | --- |
| **Volt Blue** | `#2563EB` | Title underlines, accent bars, section markers |
| **Navy Title** | `#0D1F6E` | Cover titles, large headings (over light backgrounds) |
| **Eco-Green** | `#00C87A` | Positive indicators, growth markers |
| **Deep Charcoal** | `#374151` | Subtitles, key message line, secondary text |
| **Main Text** | `#1A1818` | Primary headings, body text |
| **Body Text** | `#3A3838` | Body copy, descriptions |
| **Header Gray** | `#9B9B9B` | Header auxiliary text (domain, classification) |
| **Divider** | `#DDDDDD` | Header dividers, borders |
| **Light Divider** | `#EEEEEE` | Content dividers |
| **Pure White** | `#FFFFFF` | Content/chapter/TOC page background |
| **Ending Black** | `#1C1C1C` | Ending page background (from end.jpg) |
| **Ending Text** | `#DEDEDE` | Ending page "Thanks" text |
| **Ending Subdued** | `#888888` | Ending page contact info, date |

## IV. Typography System

| Level | Usage | Size | Weight | Color |
| --- | --- | --- | --- | --- |
| **Display** | Cover title | 56px | Bold | `#FFFFFF` (over image) / `#0D1F6E` (over light bg) |
| **Cover Subtitle** | Cover subtitle | 24px | Regular | `#FFFFFF` |
| **H1** | Content title | 32px | Bold | `#1A1818` |
| **H2** | Chapter title / TOC "Contents" | 28–40px | Bold | `#1A1818` |
| **H3** | Section head / TOC item title | 22–24px | Bold | `#1A1818` |
| **Key Message** | Content key message line | 20px | Regular | `#374151` |
| **Body** | Paragraph / TOC description | 16–20px | Regular | `#3A3838` |
| **Caption** | Metadata / source / footer | 12–14px | Regular | `#3A3838` / `#9B9B9B` |
| **Header** | Header text | 13–16px | Bold/Regular | `#1A1818` / `#9B9B9B` |

**Font Stack (EN)**: `Arial, "Helvetica Neue", "Segoe UI", sans-serif`
**Font Stack (CN)**: `"方正兰亭黑_GBK", "Microsoft YaHei", "PingFang SC", Arial, sans-serif`
**Font Stack (Bilingual — Template Default)**: `Arial, "Helvetica Neue", "Microsoft YaHei", "PingFang SC", sans-serif`

> All template SVG files use the Bilingual font stack to ensure correct rendering for both English and Chinese content. Executor may override with the language-specific stack based on actual content language.

## V. Header Specification

All content pages share a unified 4-zone header bar:

```
Height: 38px │ Background: #FFFFFF │ Bottom border: stroke #DDDDDD 1px

Zones (separated by vertical dividers at x = 320, 640, 1120):
┌──────────────┬──────────────┬──────────────────────────────┬─────────┐
│ {{BRAND_     │ aesc-group   │ document level :            │ {{PAGE  │
│  LABEL}}     │ .com         │ confidential                │  _NUM}} │
│ 16px Bold    │ 13px Regular │ 13px Regular                │ 13px R  │
│  #1A1818     │  #9B9B9B     │  #9B9B9B                    │ #9B9B9B │
│  x=24        │  x=480       │  x=880                      │ x=1200  │
│  y=24        │  y=24        │  y=24                       │ y=24    │
└──────────────┴──────────────┴──────────────────────────────┴─────────┘
Vertical dividers: y1=10 → y2=28, stroke #DDDDDD, 1px
```

## VI. Page Types

### 1. Cover Page (`01_cover.svg`)
- White top strip (44px) with brand label
- Full-width background image (`cover.jpg`, 1280×534 zone)
- Dark left gradient overlay for title readability
- Large blue title + white subtitle over image
- White bottom strip (142px) with author + date

### 2. Table of Contents (`02_toc.svg`)
- Standard 4-zone header
- White background, no pattern
- "Contents" title with blue accent underline
- Up to 5 indexed items with blue numerals

### 3. Chapter Page (`02_chapter.svg`)
- Standard 4-zone header
- White background, no pattern
- Left blue accent bar (5px wide)
- Chapter number + title + description

### 4. Content Page (`03_content.svg`)
- Standard 4-zone header
- Pure white background, no pattern or decoration
- Blue left accent bar (5px wide) + title + underline
- Key message line (20px, Deep Charcoal)
- Open content area (1168 × 502 px)
- Footer with source (left) + page number (right)

### 5. Ending Page (`04_ending.svg`)
- Full-bleed dark background (`end.jpg`)
- Centered "Thanks" text (light gray)
- Brand label at bottom (white)
- Optional contact information

## VII. Layout Modes

| Mode | Recommendation |
| --- | --- |
| **Data Dashboard** | Use full-width body with 3-4 KPI cards + chart area |
| **Comparison** | Use split columns (560+560, gap 24px) |
| **Process / Flow** | Use horizontal flow with 3-6 stages, full width |
| **Table** | Use full-width body area, max height ~400px |
| **KPI + Detail** | Top row of data cards (3-4) + bottom detail area |

## VIII. Spacing Specification

| Property | Value |
| --- | --- |
| **Base Unit** | 8px |
| **Card Gap** | 20px |
| **Title to Body** | 44px |
| **Header Height** | 38px |
| **Footer Offset** | 40px from bottom |

## IX. SVG Technical Constraints

1. `viewBox` = `0 0 1280 720` — no exceptions
2. Banned: `mask`, `<style>`, `class`, `foreignObject`, `textPath`, animation tags, `rgba()`, `<g opacity>`, `<symbol>`+`<use>`
3. `clipPath` is **conditionally allowed** on `<image>` elements only (for circular/rounded image crops); the referenced `<clipPath>` must live in `<defs>` and contain a single shape child
4. Use plain hex colors with `fill-opacity` / `stroke-opacity`
5. Image references use relative paths (e.g. `cover.jpg`, `end.jpg`)
6. No inline CSS — all styling via SVG attributes

## X. Placeholder Specification

| Placeholder | Pages | Description |
| --- | --- | --- |
| `{{BRAND_LABEL}}` | All | Brand name (default: `ΛESC`；中文: `远景动力`) |
| `{{TITLE}}` | Cover | Cover main title |
| `{{SUBTITLE}}` | Cover | Cover subtitle |
| `{{DATE}}` | Cover, Ending | Date (cover: bottom left; ending: bottom center) |
| `{{AUTHOR}}` | Cover | Presenter / organization |
| `{{CHAPTER_NUM}}` | Chapter | Chapter number |
| `{{CHAPTER_TITLE}}` | Chapter | Chapter title |
| `{{CHAPTER_DESC}}` | Chapter | Chapter description |
| `{{PAGE_TITLE}}` | TOC, Content | Page title |
| `{{KEY_MESSAGE}}` | Content | Key message line |
| `{{CONTENT_AREA}}` | Content | Flexible content body |
| `{{SOURCE}}` | Content | Source attribution |
| `{{PAGE_NUM}}` | Content, Chapter | Page number |
| `{{TOC_ITEM_1_TITLE}}` | TOC | TOC item 1 title |
| `{{TOC_ITEM_1_DESC}}` | TOC | TOC item 1 description |
| `{{TOC_ITEM_2_TITLE}}` | TOC | TOC item 2 title |
| `{{TOC_ITEM_2_DESC}}` | TOC | TOC item 2 description |
| `{{TOC_ITEM_3_TITLE}}` | TOC | TOC item 3 title |
| `{{TOC_ITEM_3_DESC}}` | TOC | TOC item 3 description |
| `{{TOC_ITEM_4_TITLE}}` | TOC | TOC item 4 title |
| `{{TOC_ITEM_4_DESC}}` | TOC | TOC item 4 description |
| `{{TOC_ITEM_5_TITLE}}` | TOC | TOC item 5 title |
| `{{TOC_ITEM_5_DESC}}` | TOC | TOC item 5 description |
| `{{THANK_YOU}}` | Ending | Thank-you message |
| `{{CONTACT_INFO}}` | Ending | Contact info line |

## XI. Asset Specification

| Asset | Purpose |
| --- | --- |
| `cover.jpg` | Cover page full-bleed background (cinematic landscape + AESC "A") |
| `end.jpg` | Ending page full-bleed background (dark + AESC "A" watermark) |

Both assets are required. Place them in the template directory alongside the SVG files.

> **Image lock**: `cover.jpg` and `end.jpg` are **fixed template assets**. Cover pages MUST always reference `cover.jpg`; ending pages MUST always reference `end.jpg`. The pipeline must NOT replace or override them with AI-generated images, web-sourced images, or other generated content. If a deck needs a custom cover or ending image, the user must supply the replacement file themselves — the pipeline never auto-generates a substitute for these two assets.

## XII. AESC "A" Arch Logo

The AESC logo is a geometric arch (letter "A" without crossbar). SVG path template (100×98 base, scale as needed):

```
M-54 98 L0 0 L54 98 L40 98 L0 20 L-40 98 Z
```

Usage: Apply `transform="translate(cx,cy) scale(s)"` for positioning and sizing. Use `fill-opacity` for watermark effects.

## XIII. Business Reporting Story Framework

> This section is **mandatory** for business reporting decks (CTS 业务汇报、海外项目分析、质量表现报告、售后物流方案). It governs how the Strategist constructs the Content Outline (Section IX of the design_spec output) and how the Executor designs each page's visual hierarchy.

### A. Narrative Arc（汇报故事线）

The deck must follow a six-chapter arc. This is not "show what we did" — it is "help management understand: why the business needs improvement, where the problems are, what foundation already exists, what to do next, and what support is needed."

| Chapter | Story Stage | Management Reader Expects |
| --- | --- | --- |
| **Ch 1** | 业务背景 / 管理现状 — Scope & Baseline | 这个业务管什么？我们目前有哪些管理能力和基础？ |
| **Ch 2** | 执行痛点 — Execution Pain Points | 哪里有问题？严重程度如何？数据说明什么？ |
| **Ch 3** | 问题分析 — Root Cause Analysis | 为什么会这样？根因是什么？管理抓手在哪里？ |
| **Ch 4** | 解决方案 — Solution Design | 怎么解决？方案是否可行？多个方案如何取舍？ |
| **Ch 5** | 行动计划 — Action Plan | 谁来做？做什么？什么时候完成？当前进展如何？ |
| **Ch 6** | 资源诉求 — Resource Request | 需要哪些跨部门支持或资源投入？预期回报是什么？ |

**Recommended TOC structure** (Strategist should default to this for aesc_ppt decks):

```
1. 管理范围与基础能力
2. 执行侧痛点与现状差距
3. 问题根因分析
4. 改进方案设计
5. 行动计划
6. 资源诉求与预期收益
```

### B. Visualization Guide per Chapter（各章节图表选型）

The aesc_ppt template is **data-first**. Every conclusion page in Ch 2 / Ch 3 / Ch 4 must carry a chart or structured visual. Pure bullet-point pages are not permitted in these chapters.

| Chapter | Preferred Chart Types | Notes |
| --- | --- | --- |
| **Ch 1** 管理现状 | KPI Dashboard cards (3–4), overview table, regional coverage map | Establish scope and capability baseline |
| **Ch 2** 执行痛点 | Stacked / grouped bar chart, horizontal bar (ranking), heatmap table | Quantify gaps across regions / process steps |
| **Ch 3** 问题分析 | SWOT matrix (2×2), cost waterfall chart, event retrospective frame | Waterfall chart: shows cost deltas by factor; use for cost gap attribution |
| **Ch 4** 解决方案 | Two-column comparison table (option A vs B), process flowchart, cost-benefit scatter plot | If scatter plot is unclear, replace with a two-column table (投入 vs 产出) |
| **Ch 5** 行动计划 | Gantt-style timeline, swimlane flowchart (cross-department), SMART action table | Swimlane for processes involving ≥ 2 departments |
| **Ch 6** 资源诉求 | Budget breakdown table, ROI comparison bar chart | Keep this chapter separate from Ch 5 — do not merge |

**Chart selection decision rules:**

- 各区域对比 → grouped / stacked bar chart
- 各环节成本构成 / 成本增减因素 → waterfall chart
- 跨部门流程 → swimlane / flowchart
- 典型问题复盘 → event retrospective (事件性复盘框架)
- 方案投入产出比较 → scatter plot; if data is sparse or two dimensions are insufficient to tell the story, use a two-column table instead
- 管理抓手识别 → annotated chart with callout boxes (not plain bullets)

### C. Content Quality Gates（内容质量原则）

The Strategist **must** enforce these rules when drafting the Content Outline, and the Executor must enforce them when writing page titles and key message lines.

1. **Assertion page titles** — every page title must be a conclusive statement, not a label.
   - ❌ `海外仓成本分析` → ✅ `亚太区仓储成本超标 18%，是三区域中差距最大的`
   - ❌ `行动计划` → ✅ `三项优先行动将在 Q3 落地，责任人已确定`

2. **Data-backed conclusions** — every management conclusion requires three elements: the value itself + a comparison benchmark + the implication.
   - Pattern: `[数值] 相比 [基准], 说明 [管理含义]`

3. **SMART action items** — every row in the action plan table must satisfy:
   - **S**pecific — 具体说明做什么
   - **M**easurable — 有可量化的完成标准
   - **A**ssignable — 明确负责人（姓名或职能）
   - **R**ealistic — 当前资源条件下可执行
   - **T**ime-bound — 有明确截止时间

4. **Action Plan ≠ Resource Request** — Ch 5 and Ch 6 must be separate chapters. Do not merge resource asks into the action plan page.

5. **图文结合 (visual + text integration)** — Ch 2 / Ch 3 / Ch 4 pages: each data conclusion page must have at least one chart, diagram, or structured visual. Plain text bullet lists are not acceptable as the sole content element on these pages.

### D. Example Narrative: Overseas Warehouse Logistics Reporting

This is the reference narrative for a 海外仓储物流汇报 deck. Use it to validate outline structure and logic flow.

```
Ch 1 — 管理范围与基础能力
  • 当前海外仓管理区域与仓点数量（KPI dashboard）
  • 已建立的制度、流程、系统（结构化表格）
  • 当前具备的管理能力概览

Ch 2 — 执行侧痛点与现状差距
  • 各区域执行难度对比（堆积柱状图）
  • 效率低的关键环节及量化数据（横向条形图）
  • 反复发生的问题类型统计（分类汇总表）

Ch 3 — 问题根因分析
  • SWOT 分析：管理体系的优势、劣势、机会、威胁
  • 成本瀑布图：识别各区域成本差异的驱动因素
  • 事件性复盘：1–2 个典型案例的经验教训

Ch 4 — 改进方案设计
  • 方案对比：两列表格（方案A vs 方案B）
  • 改进后流程图（泳道图 or flowchart）

Ch 5 — 行动计划
  • 甘特式时间线（按季度展示关键里程碑）
  • SMART 行动表（责任人 / 完成标准 / 截止时间）

Ch 6 — 资源诉求与预期收益
  • 所需资源拆解（预算 + 人力 + 跨部门协同）
  • ROI 预期：投入 vs 预计收益对比
```
