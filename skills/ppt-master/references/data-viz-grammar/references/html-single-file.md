# HTML 单文件看板 / 报表 —— 规则版落地

> html 是最容易退回“卡片网格 + 投影 + 多色”的介质：框架默认样式就在鼓励它。
> 本文件把 `data-viz-grammar` §3 翻成 CSS/HTML 的具体写法。

## 1. 页龴结构（默认 `chart_insight_rail`）

```
标题区   : 结论句 (clamp(22px, 2.2vw, 30px), 600) + 副标（口径/时段, 13px, #767676）+ 发丝分割线
主区     : 图 62–68% + 右栏 30–34%（结论 / 证据 / 动作）
底部     : 来源行（12–13px, #767676, 左对齐）
```

禁止：顶部一排 4 个 KPI 卡片。如果确实有 4 个同等重要的数，用 `hero_number` 式布局：
一个大数（48–64px）占 2 列，其余三个用“数 + 一句解释 + 小趋势线”列表，**不包卡片**。

## 2. 反卡片 CSS（直接抄）

```css
:root{
  --ink:#1A1A1A; --graphite:#4D4D4D; --mid:#767676;
  --hair:#DAD7D0; --wash:#F5F3EE; --accent:#2C5C7E;
  --neg:#A8442F; --pos:#3F6F5E;
}
body{background:#fff;color:var(--ink);font:15px/1.65 "Microsoft YaHei",system-ui,sans-serif}
.panel{box-shadow:none;border:none;border-radius:0;padding:0}
.grid{border-top:1px solid var(--hair)}          /* 分区靠发丝线，不靠边框盒 */
.kpi{border-left:2px solid var(--hair);padding-left:14px}   /* 一组数字靠左发丝线分组 */
.kpi b{font-size:44px;font-weight:600;letter-spacing:-.02em}
.note{font-size:12px;color:var(--mid)}
.src{font-size:12px;color:var(--mid);border-top:1px solid var(--hair);padding-top:8px}
```

写代码时的硬检查：`grep -n "box-shadow\|border-radius: *[5-9]" page.html` 应为空。

## 3. 图表怎么嵌

优先 **内联 SVG**（可打印、可截图、不依赖 CDN）：
- 坐标系：只画横向基线，不画 Y 轴线与刻度短线；网格线 `stroke:#DAD7D0;stroke-width:1`
- 文字：`<text>` 直接标系列名与数值，不用 `<div class=legend>` 色块图例
- 强调：只有论点指向的元素用 `--accent`，其余 `#8E8B84` / `#767676`
- 字号：`<text font-size="12">` 为下限，轴标题 12、数值 12–13、图内主数字 15–18

当用 ECharts / Chart.js 时（仅限交互看板）：
```js
color:['#2C5C7E','#8E8B84','#DAD7D0'],
legend:{show:false},                 // 用 series.endLabel 直接标注
grid:{left:48,right:96,top:24,bottom:36,containLabel:true},
shadowBlur:0, shadowColor:'transparent',
xAxis:{axisLine:{lineStyle:{color:'#DAD7D0'}},splitLine:{show:false},axisTick:{show:false}},
yAxis:{axisLine:{show:false},splitLine:{lineStyle:{color:'#DAD7D0'}},axisTick:{show:false}},
series:[{type:'line',symbol:'none',lineStyle:{width:2},endLabel:{show:true,formatter:'{a} {c}'}}]
```

## 4. 字号与可读性（用户反复报“字太小”）

| 元素 | 最小 | 建议 |
|---|---|---|
| 页标题 | 22px | 26–30px |
| 分区标题 | 15px | 16–18px |
| 正文 | 14px | 15–16px |
| 图表轴/数值/注释 | 12px | 12–13px |
| 来源行 | 12px | 12–13px |

- 不要用 `rem` 配 10px 根字号来“缩全局”：会造成整页小于 12px。`html{font-size:100%}` 起步。
- 宽度自适应时用 `clamp()`，不要用 `transform:scale()` 缩小页面。
- 打印场景加 `@media print{ @page{size:A4 landscape;margin:10mm} }`。

## 5. 自检

```bash
python <data-viz-grammar>/scripts/check_html_viz.py page.html          # 逐项报错
python <data-viz-grammar>/scripts/check_html_viz.py page.html --strict # warning 也算失败
```

它会查：投影 / 圆角卡片 / 饱和色数量 / 最小字号 / 来源行 / 名词短语标题 / 卡片网格。
人工仍需看两点：**标题数字与图内数字是否一致**、**文字有没有压图**。
