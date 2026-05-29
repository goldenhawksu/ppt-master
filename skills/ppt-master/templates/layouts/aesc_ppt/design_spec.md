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
