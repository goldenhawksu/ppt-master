# matplotlib 出图 —— 规则版落地

> 出成 PNG 嵌 PPT/报幕时，matplotlib 默认样式（全框盒 + 灰色网格 + 图例 + 默认蓝）
> 正是“2020 看板感”的来源。下面是一份可直接复用的 rcParams + 画法。

## 1. rcParams（一次性设定）

```python
import matplotlib as mpl
mpl.rcParams.update({
    "font.family": "Microsoft YaHei",     # Windows 中文字体，避免方块
    "axes.unicode_minus": False,
    "figure.dpi": 200, "savefig.dpi": 200,
    "figure.facecolor": "white", "axes.facecolor": "white",
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.spines.left": False,                    # 只留底轴，或连底轴也去
    "axes.edgecolor": "#DAD7D0", "axes.linewidth": 1,
    "axes.grid": True, "grid.color": "#DAD7D0", "grid.linewidth": 1,
    "grid.alpha": 1.0, "axes.axisbelow": True,
    "axes.tick_params.left": False, "axes.tick_params.bottom": False,
    "axes.labelcolor": "#4D4D4D", "text.color": "#1A1A1A",
    "xtick.color": "#767676", "ytick.color": "#767676",
    "font.size": 12, "axes.titlesize": 15, "xtick.labelsize": 12, "ytick.labelsize": 12,
    "legend.frameon": False,
})
# 只留横向网格
mpl.rcParams["axes.grid.axis"] = "y"
```

关键三条：**去 top/right 脊柱**、**网格只留横向且极淡**、**字号起步 12**。

## 2. 画布大小（嵌 PPT / 一页纸时）

```python
# 一页 1280×720 里图占 62% 宽 → 约 5.5×3.1 in @200dpi = 1100×620 px
fig, ax = plt.subplots(figsize=(5.5, 3.1))
fig.savefig("chart.png", bbox_inches="tight", pad_inches=0.04)
```

- `figsize` 按**目标英寸**给，不要画很大再缩 —— 缩完字号跟着缩，就回到“字太小”问题。
- 嵌 HTML/PPT 用 PNG；印刷或需无损时用 `svg` 或 `pdf`，并 `rcParams['svg.fonttype']='none'` 保留可编辑文字。

## 3. 与语法对齐的画法

| 语法规则 | matplotlib 写法 |
|---|---|
| 直接标注，不用图例 | `ax.text(x[-1]+pad, y[-1], name, va='center')` 或 `ax.annotate` |
| 单一强调色 | 突出项 `color='#2C5C7E'`，其余 `'#8E8B84'` / `'#767676'` |
| 参考线带标签 | `ax.axhline(target, ls='--', lw=1.5, color='#4D4D4D')` + `ax.text(xmax, target, '目标 125', ha='right', va='bottom', fontsize=12)` |
| 最多一个气泡 | `ax.annotate('8月转正', xy=(8,0), xytext=(20,30), textcoords='offset points', arrowprops=dict(arrowstyle='-', lw=0.8, color='#4D4D4D'), fontsize=12)` |
| 柱 >12 根只标首末峰谷 | 逐柱标数时先算 `idx_to_label` 白名单 |
| 坐标不让读者换算 | 直接标单位到标题/轴名（`人均工单（单）`），不要用 1e3 偏移 |
| 大数不用科学计数 | `ax.ticklabel_format(style='plain', axis='y')` + 千分位 formatter |

## 4. 常用图种一行代码要点

```python
# 双向条形（偏离）：零线居中，负值向左
ax.barh(labels, dev, color=["#2C5C7E" if v>=0 else "#A8442F" for v in dev])
ax.axvline(0, color="#4D4D4D", lw=1)

# 斜率图（两名次/两期）
for i,(a,b) in enumerate(zip(v1,v2)):
    ax.plot([0,1],[a,b], color="#2C5C7E" if i==focus else "#B9B5AC", lw=2 if i==focus else 1.2)
    ax.text(1.02, b, name, fontsize=12, va="center")
ax.set_xticks([0,1]); ax.set_xlim(-0.05, 1.35)

# 直方图（柱间无缝）
ax.hist(vals, bins=np.arange(lo, hi+step, step), edgecolor="white", linewidth=0.6, color="#2C5C7E")

# 洛伦兹/帕累托：累计曲线 + 均分线 + 交点标注
ax.plot([0,1],[0,1], ls="--", color="#B9B5AC", lw=1)   # 均分线必须有，否则看不出集中
```

## 5. 交付前

1. `print(min fontsize used)` —— 有任何 < 12 的（标注、tick、图例）就算错。
2. 中文字体：缺字会静默变成方块，**必须眼看一次**（`vision_analyze` 或 `open`）。
3. 裁边用 `bbox_inches='tight'`，不要事后 PIL 裁剪猜边。
4. 嵌进 PPT 前确认图片像素 ≥ 目标尺寸 ×2（防投影模糊）。
