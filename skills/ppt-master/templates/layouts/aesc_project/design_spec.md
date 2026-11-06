---
template_id: aesc_project
category: brand
summary: AESC battery storage and engineering project management review template — structured for weekly PMO updates, master Gantt timelines, KPI dashboards, work package status, and logistics tracking.
keywords: [aesc, 远景动力, project-management, pmo, weekly-update, gantt, timeline, bss, work-package]
primary_color: "#3B3B44"
canvas_format: ppt169
replication_mode: fidelity
use_cases: 储能工程项目管理、周度例会汇报、PMO状态看板、甘特排程推进、工作包交付跟踪
design_tone: Rigorous, data-dense, engineering-focused, structured, bilingual-capable (default English ΛESC, Chinese 远景动力)
placeholders:
  01_cover: ["{{TITLE}}", "{{SUBTITLE}}", "{{DATE}}", "{{AUTHOR}}"]
  02_toc: ["{{PAGE_TITLE}}", "{{TOC_ITEM_1_TITLE}}", "{{TOC_ITEM_1_DESC}}", "{{TOC_ITEM_2_TITLE}}", "{{TOC_ITEM_2_DESC}}", "{{TOC_ITEM_3_TITLE}}", "{{TOC_ITEM_3_DESC}}", "{{TOC_ITEM_4_TITLE}}", "{{TOC_ITEM_4_DESC}}", "{{TOC_ITEM_5_TITLE}}", "{{TOC_ITEM_5_DESC}}", "{{PAGE_NUM}}"]
  02_chapter: ["{{CHAPTER_NUM}}", "{{CHAPTER_TITLE}}", "{{CHAPTER_DESC}}", "{{PAGE_NUM}}"]
  03_content: ["{{PAGE_TITLE}}", "{{CONTENT_AREA}}", "{{PAGE_NUM}}"]
  03a_content_overview_kpis: ["{{PAGE_TITLE}}", "{{KPI_1_VAL}}", "{{KPI_1_LABEL}}", "{{KPI_2_VAL}}", "{{KPI_2_LABEL}}", "{{KPI_3_VAL}}", "{{KPI_3_LABEL}}", "{{KPI_4_VAL}}", "{{KPI_4_LABEL}}", "{{KPI_5_VAL}}", "{{KPI_5_LABEL}}", "{{FACT_1_KEY}}", "{{FACT_1_VAL}}", "{{FACT_2_KEY}}", "{{FACT_2_VAL}}", "{{FACT_3_KEY}}", "{{FACT_3_VAL}}", "{{FACT_4_KEY}}", "{{FACT_4_VAL}}", "{{MILESTONE_SUMMARY}}", "{{PAGE_NUM}}"]
  03b_content_org_chart: ["{{PAGE_TITLE}}", "{{TIER_1_TITLE}}", "{{TIER_2_TITLE}}", "{{TIER_3_TITLE}}", "{{ROLE_1}}", "{{NAME_1}}", "{{ROLE_2}}", "{{NAME_2}}", "{{ROLE_3}}", "{{NAME_3}}", "{{ROLE_4}}", "{{NAME_4}}", "{{PAGE_NUM}}"]
  03c_content_master_timeline: ["{{PAGE_TITLE}}", "{{TIMELINE_TITLE}}", "{{PHASE_1_LABEL}}", "{{PHASE_2_LABEL}}", "{{PHASE_3_LABEL}}", "{{PHASE_4_LABEL}}", "{{MILESTONE_1}}", "{{MILESTONE_2}}", "{{MILESTONE_3}}", "{{PAGE_NUM}}"]
  03d_content_wp_status_dashboard: ["{{PAGE_TITLE}}", "{{WP_NAME}}", "{{WP_OWNER}}", "{{WEEK_NUM}}", "{{VARIANCE_DAYS}}", "{{SCHEDULE_STATUS}}", "{{ACTIVITY_1}}", "{{OWNER_1}}", "{{DUE_1}}", "{{STATUS_1}}", "{{ACTIVITY_2}}", "{{OWNER_2}}", "{{DUE_2}}", "{{STATUS_2}}", "{{ACTIVITY_3}}", "{{OWNER_3}}", "{{DUE_3}}", "{{STATUS_3}}", "{{MILESTONE_1}}", "{{MS_BASELINE_1}}", "{{MS_FORECAST_1}}", "{{MS_VAR_1}}", "{{RISK_1_TYPE}}", "{{RISK_1_DESC}}", "{{RISK_1_MITIGATION}}", "{{PAGE_NUM}}"]
  03e_content_production_plan: ["{{PAGE_TITLE}}", "{{PLAN_SUMMARY}}", "{{BATCH_1_NAME}}", "{{BATCH_1_QTY}}", "{{BATCH_1_DATE}}", "{{BATCH_1_STATUS}}", "{{BATCH_2_NAME}}", "{{BATCH_2_QTY}}", "{{BATCH_2_DATE}}", "{{BATCH_2_STATUS}}", "{{PAGE_NUM}}"]
  04_ending: ["{{THANK_YOU}}", "{{BRAND_LABEL}}", "{{CONTACT_INFO}}", "{{DATE}}"]
---

# AESC Project Management Design Specification

## I. Template Overview

| Property | Description |
| --- | --- |
| Template ID | `aesc_project` — the dedicated AESC project management and PMO review template. Saying "使用aesc_project模板" selects it. |
| Display name | AESC (远景动力) Project Management Template |
| Recurring family | BESS energy storage project management, weekly PMO reviews, master timeline tracking, work package updates, factory production & logistics delivery |
| Audience and purpose | Project directors, work package owners, EPC customers, and executive steering committees assessing schedule adherence, risks, and next steps |
| Visual voice | Clean, highly structured, data-dense, engineering-focused, bilingual-capable (English default `ΛESC`, Chinese `远景动力`) |
| Theme | White interior pages with `#3B3B44` dark chrome, corporate green tinted photographic cover, dark photographic ending |
| Canvas | 1280 × 720 px (`ppt169`); content workspace y = 80–656 px |

## II. Color Scheme

| Role | Color | Application |
| --- | --- | --- |
| Dark Chrome | `#3B3B44` | Top accent bar, slide title divider, table banners, footer bar background |
| Project Blue | `#4472C4` | Milestone markers, category headers, active section indicators |
| Status Green | `#00B050` / `#17795E` | ON TRACK status dot, forecast actual progress bars, positive milestones |
| Status Amber | `#FFC000` | AT RISK status dot, cautionary variance alerts |
| Semantic Red | `#ED7D31` / `#DC2626` | BEHIND status dot, delayed timeline alerts, risk severity flags |
| Table Header Fill | `#E6E8EC` / `#44546A` | Sub-headers in activity & milestone tables |
| Neutral Light | `#F3F4F6` / `#F8FAFC` | Tile backgrounds, alternating row fills |
| Dark Text | `#1E293B` / `#22222A` | Primary titles, table content, metadata values |
| Muted Text | `#64748B` / `#5A5D68` | Secondary labels, descriptions, subtitles |

## III. Signature Design Elements

1. **Top Security Chrome**: 5.92px top solid bar in `#3B3B44`, accompanied by top-right confidentiality text: `AESC CONFIDENTIAL`.
2. **Page Title Rule**: Left-aligned 28px bold page title above a 1px divider rule stretching from x=20 to x=1262 at y=79.8.
3. **Bottom Compliance Footer**: 64px dark bottom bar (`#3B3B44`) featuring the white AESC logo on the left, an italicized three-line legal disclosure in the center, and dynamic slide number `{{PAGE_NUM}}` on the right.
4. **Brand Label Language Rule**: When generating English decks, use `ΛESC`; when generating Chinese decks, use `远景动力`. Do not mix English branding into Chinese templates.
5. **Project Management Core Widgets**:
   - Status Indicator Card: 3-light indicator (`BEHIND` / `ON TRACK` / `AHEAD`), schedule variance in days, WP owner, and week code.
   - Dual-track Progress Gantt: Baseline dashed schedule compared against solid forecast/actual bars with diamond milestone markers.
   - Triple Action Table: Activities/Priorities, Upcoming 4-6 Week Milestones, and Risk/Opportunity Mitigation matrix.

## IV. Typography

- Primary Latin: `Calibri, "Segoe UI", Arial, sans-serif`
- Primary Chinese: `"Microsoft YaHei", "PingFang SC", sans-serif`
- Headers: Bold `Helvetica, Arial, sans-serif` (24–44px)
- KPI Big Numbers: Bold `Calibri` (30–32px)
- Body / Tables: `Calibri` (12–14px)

## V. Page Roster

| # | Filename | Purpose | Description |
|---|----------|---------|-------------|
| 01 | `01_cover.svg` | Cover | Project title, subtitle, date, author, AESC logo |
| 02 | `02_toc.svg` | Table of contents | 5 numbered agenda items with titles and summaries |
| 03 | `02_chapter.svg` | Chapter page | Chapter number, title, description on tinted background |
| 04 | `03_content.svg` | General content | Standard header/footer frame with open workspace |
| 05 | `03a_content_overview_kpis.svg` | Overview & KPIs | 5 KPI big-number tiles, project facts table, logistics map slot, timeline summary |
| 06 | `03b_content_org_chart.svg` | Organization chart | 3-tier stakeholder and support team matrix with role cards |
| 07 | `03c_content_master_timeline.svg` | Master Gantt timeline | Multi-phase Gantt chart with calendar header and contract milestones |
| 08 | `03d_content_wp_status_dashboard.svg` | Work package dashboard | Schedule status card (lights/variance/owner), dual-line Gantt, action items, upcoming milestones, risks |
| 09 | `03e_content_production_plan.svg` | Production plan | Matrix table tracking manufacturing batches, FAT, shipment, and ETD status |
| 10 | `04_ending.svg` | Ending page | Thank you message, AESC brand label, contact info |
