#!/usr/bin/env python3
"""
PPT Master - AESC 图表审计

检查 SVG 图表的意图、可见论点、可见来源及可编辑图元，输出可追溯审计。
这是补充检查，不验证数据真伪、坐标计算、视觉排版或原生图表载荷。

Usage:
    python scripts/check_aesc_viz.py <project_or_svg> --require-charts --json

Examples:
    python scripts/check_aesc_viz.py projects/demo/svg_output --json

Dependencies:
    仅使用标准库及随 Skill 分发的模块。
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from xml.etree import ElementTree as ET

from console_encoding import configure_utf8_stdio
from slide_roster import discover_slide_svgs


configure_utf8_stdio()

INTENTS = {
    "deviation", "ranking", "distribution", "change_over_time",
    "part_to_whole", "magnitude", "correlation", "spatial", "flow",
}
PAGE_TYPES = {
    "chart_insight_rail", "hero_number", "comparison_swing",
    "bridge_waterfall", "table_with_trend",
}
DRAWING_TAGS = {"rect", "path", "line", "polyline", "polygon", "circle", "ellipse"}
CLAIM_CUE = re.compile(
    r"\d|升|降|超|低|倍|最|首|差|转|增长|减少|集中|贡献|"
    r"\b(up|down|higher|lower|grew|fell|exceed\w*|lead\w*|largest|smallest)\b",
    re.IGNORECASE,
)
SCOPED_MARKER = re.compile(r"chart-plot-area:\s*object=([^\s|]+)")


def _tag(element: ET.Element) -> str:
    return element.tag.rsplit("}", 1)[-1]


def _visible(element: ET.Element, parents: dict) -> bool:
    current = element
    while current is not None:
        if _tag(current) in {"defs", "metadata", "clipPath"}:
            return False
        style = current.get("style", "").replace(" ", "").lower()
        if current.get("display") == "none" or "display:none" in style:
            return False
        if current.get("visibility") in {"hidden", "collapse"} or "visibility:hidden" in style:
            return False
        if current.get("opacity") in {"0", "0.0"} or re.search(r"(?:^|;)opacity:0(?:\.0+)?(?:;|$)", style):
            return False
        current = parents.get(current)
    return True


def _text(element: ET.Element | None, parents: dict) -> str:
    if element is None or _tag(element) != "text" or not _visible(element, parents):
        return ""
    return " ".join("".join(element.itertext()).split())


def check_page(path: Path, chart_keys: set[str]) -> dict:
    result = {"file": str(path), "charts": [], "errors": [], "warnings": []}
    try:
        raw = path.read_text(encoding="utf-8-sig")
        root = ET.fromstring(raw)
    except (OSError, UnicodeError, ET.ParseError) as exc:
        result["errors"].append(f"无法读取 SVG：{exc}")
        return result
    if _tag(root) != "svg":
        result["errors"].append("根元素必须是 SVG")
        return result
    parents = {child: parent for parent in root.iter() for child in parent}
    elements = {}
    for element in root.iter():
        identifier = element.get("id")
        if identifier:
            if identifier in elements:
                result["errors"].append(f"重复对象 ID：{identifier}")
            elements[identifier] = element
    scoped_keys = set(SCOPED_MARKER.findall(raw))
    groups = [element for element in root.iter() if _tag(element) == "g" and (
        "data-viz-intent" in element.attrib
        or element.get("data-pptx-replace-with") == "chart"
        or element.get("id") in scoped_keys
    )]
    for missing in sorted(scoped_keys - {group.get("id") for group in groups}):
        result["errors"].append(f"图表坐标标记没有对应分组：{missing}")
    if "chart-plot-area:" in raw and not scoped_keys and not groups:
        result["errors"].append("旧式无对象键图表需要补充 data-viz-intent 审计分组")
    result["page_type"] = root.get("data-viz-page-type", "")
    if groups and result["page_type"] not in PAGE_TYPES:
        result["warnings"].append("建议声明有效的 data-viz-page-type，以便检查相邻页节奏")
    for group in groups:
        identifier = group.get("id", "")
        intent = group.get("data-viz-intent", "")
        chart = group.get("data-viz-chart", "")
        takeaway = _text(elements.get(group.get("data-viz-title", f"{identifier}-takeaway")), parents)
        source = _text(elements.get(group.get("data-viz-source", f"{identifier}-source")), parents)
        result["charts"].append({
            "object": identifier, "intent": intent, "chart": chart,
            "takeaway": takeaway, "source": source,
        })
        if not identifier:
            result["errors"].append("图表分组缺少 id")
        if intent not in INTENTS:
            result["errors"].append(f"{identifier}: 缺少或无效的九类意图：{intent!r}")
        if chart not in chart_keys:
            if not (chart.startswith("custom/") and group.get("data-viz-reason", "").strip()):
                result["errors"].append(f"{identifier}: 图种不在当前目录中；自绘图使用 custom/<name> 并注明 data-viz-reason")
        if not takeaway:
            result["errors"].append(f"{identifier}: 缺少可见论点文本")
        elif not CLAIM_CUE.search(takeaway):
            result["warnings"].append(f"{identifier}: 标题可能只是主题名词，请人工核实论点")
        if not source:
            result["errors"].append(f"{identifier}: 缺少可见来源文本")
        for label, text in (("论点", takeaway), ("来源", source)):
            if "{{" in text or "}}" in text:
                result["errors"].append(f"{identifier}: {label}仍是占位符")
        drawings = [element for element in group.iter() if _tag(element) in DRAWING_TAGS and _visible(element, parents)]
        if not drawings:
            result["errors"].append(f"{identifier}: 缺少可编辑图元；不能只放截图或元数据")
    return result


def audit(target: Path, *, require_charts: bool = False) -> dict:
    catalog_path = Path(__file__).resolve().parents[1] / "templates" / "charts" / "charts_index.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    chart_keys = set(catalog["charts"])
    target = target.resolve()
    svg_root = target / "svg_output" if (target / "svg_output").is_dir() else target
    if target.is_file():
        files = [target] if target.suffix.lower() == ".svg" else []
    else:
        files = discover_slide_svgs(svg_root) if svg_root.is_dir() else []
    pages = [check_page(path, chart_keys) for path in files]
    errors = [] if files else ["目标中没有 SVG 页面"]
    chart_count = sum(len(page["charts"]) for page in pages)
    if require_charts and not chart_count:
        errors.append("要求至少一个数据图表，但没有找到已标注图表")
    for index in range(2, len(pages)):
        page_type = pages[index].get("page_type")
        if page_type and all(page.get("page_type") == page_type for page in pages[index - 2:index]):
            pages[index]["warnings"].append("连续三页采用相同页型，请人工判断是否需要变化")
    return {
        "schema": "ppt-master.aesc-viz-audit.v1", "target": str(target),
        "summary": {
            "pages": len(pages), "chart_pages": sum(bool(page["charts"]) for page in pages),
            "charts": chart_count,
            "errors": len(errors) + sum(len(page["errors"]) for page in pages),
            "warnings": sum(len(page["warnings"]) for page in pages),
        },
        "errors": errors, "pages": pages,
        "limitations": [
            "未标注、没有坐标标记或原生替换标记的图表不能可靠发现，不能用本报告推断全量覆盖率。",
            "来源、意图与图种适配、坐标、缺失值、色彩语义和视觉可读性仍须其他门禁及人工复核。",
        ],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "图表分组：id、data-viz-intent（九类意图）、data-viz-chart（当前图表目录键）。\n"
            "可见 text 默认 ID：<对象键>-takeaway、<对象键>-source；可通过 data-viz-title/source 引用。\n"
            "自绘图：data-viz-chart=custom/<name>，附 data-viz-reason。\n"
            "SVG 根可声明 data-viz-page-type；机器检查不能替代 Verify Charts 和最终 SVG 门禁。"
        ),
    )
    parser.add_argument("target", type=Path, help="项目根、svg_output 目录或单页 SVG")
    parser.add_argument("--require-charts", action="store_true", help="未发现图表时返回失败")
    parser.add_argument("--json", action="store_true", help="将完整 JSON 报告写到标准输出，不写文件")
    args = parser.parse_args(argv)
    try:
        report = audit(args.target, require_charts=args.require_charts)
    except (OSError, ValueError, KeyError) as exc:
        parser.exit(2, f"检查失败：{exc}\n")
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(json.dumps(report["summary"], ensure_ascii=False))
        for message in report["errors"]:
            print(f"[ERROR] {message}")
        for page in report["pages"]:
            for severity in ("errors", "warnings"):
                for message in page[severity]:
                    print(f"[{severity.upper()}] {Path(page['file']).name}: {message}")
    return 1 if report["summary"]["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
