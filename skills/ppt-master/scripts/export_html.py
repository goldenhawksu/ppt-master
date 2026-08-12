#!/usr/bin/env python3
"""
PPT Master - Single-File HTML Export Tool

Embeds every finalized SVG page of a project into one self-contained HTML
deck with slide navigation (prev/next buttons, arrow keys, swipe), page
indicator, and collapsible speaker notes — content identical to the PPT.

Usage:
    python3 scripts/export_html.py <project_path>
    python3 scripts/export_html.py <project_path> -o output.html
    python3 scripts/export_html.py <project_path> --source output --no-notes

Examples:
    python3 scripts/export_html.py projects/<svg_title>_ppt169_YYYYMMDD
    python3 scripts/export_html.py projects/<svg_title>_ppt169_YYYYMMDD -o exports/deck.html

Dependencies:
    None (only uses standard library)

Notes:
    - SVG source defaults to `svg_final/` (post-processed, embed-included),
      falling back to `svg_output/` when the former is empty or missing
    - Speaker notes come from `notes/<NN>_*.md` (fallback: parse `notes/total.md`)
    - Output defaults to `exports/<project_name>_<timestamp>.html`
"""

import sys
import argparse
import html
import re
import time
from datetime import datetime
from pathlib import Path

_XML_DECL_RE = re.compile(r'^\s*<\?xml[^>]*\?>\s*', re.IGNORECASE)
_DOCTYPE_RE = re.compile(r'^\s*<!DOCTYPE[^>]*>\s*', re.IGNORECASE)
_VIEWBOX_RE = re.compile(r'viewBox\s*=\s*"([^"]+)"')
_HEADING_RE = re.compile(r'^(#{1,6})\s*(.+?)\s*$')

_SLIDE_CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body { height: 100%; }
body {
  background: #1f2430;
  color: #e6e6e6;
  font-family: "Microsoft YaHei", "PingFang SC", "Segoe UI", Arial, sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  overflow: hidden;
}
#header {
  width: 100%;
  padding: 10px 18px;
  display: flex;
  align-items: baseline;
  gap: 14px;
  background: #282e3b;
  border-bottom: 1px solid #3a4254;
}
#header h1 { font-size: 15px; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
#header .spacer { flex: 1; }
#header .slide-label { font-size: 13px; color: #9fb0cc; white-space: nowrap; }
#header #fullscreen {
  margin-left: 10px;
  background: none;
  border: 1px solid #3a4254;
  color: #c6d0e0;
  border-radius: 5px;
  padding: 5px 14px;
  font-size: 13px;
  cursor: pointer;
  white-space: nowrap;
}
#header #fullscreen:hover { background: #3a4254; color: #ffffff; }
#deck {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  padding: 14px;
}
.slide { display: none; flex-direction: column; align-items: center; gap: 10px; width: 100%; }
.slide.active { display: flex; }
.slide .slide-body {
  background: #ffffff;
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.45);
  max-width: 96%;
  max-height: 100%;
}
.slide .slide-body svg { display: block; width: 100%; height: 100%; }
.slide .slide-notes {
  width: 100%;
  max-width: 1100px;
  font-size: 13px;
  color: #b9c3d4;
  background: #2b3242;
  border: 1px solid #3a4254;
  border-radius: 6px;
  padding: 8px 12px;
}
.slide .slide-notes summary { cursor: pointer; font-size: 12px; color: #9fb0cc; }
.slide .slide-notes p { margin: 6px 0; line-height: 1.6; }
#controls {
  width: 100%;
  padding: 10px 18px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 18px;
  background: #282e3b;
  border-top: 1px solid #3a4254;
}
#controls button {
  background: #3a8ee0;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 7px 22px;
  font-size: 14px;
  cursor: pointer;
}
#controls button:hover { background: #2f76bd; }
#controls button:disabled { background: #4a5568; cursor: default; }
#controls .page-indicator { font-size: 14px; color: #c6d0e0; min-width: 90px; text-align: center; }
body.fsmode #header, body.fsmode #controls { display: none; }
body.fsmode #deck { padding: 0; }
body.fsmode .slide { gap: 0; height: 100%; }
body.fsmode .slide-notes { display: none; }
body.fsmode .slide-body {
  width: 100%;
  height: 100%;
  max-width: 100%;
  max-height: 100%;
  aspect-ratio: auto;
  box-shadow: none;
  border-radius: 0;
}
#fs-exit {
  display: none;
  position: fixed;
  right: 16px;
  bottom: 16px;
  z-index: 10;
  background: rgba(30, 34, 42, 0.5);
  border: 1px solid rgba(255, 255, 255, 0.25);
  color: #e6e6e6;
  border-radius: 5px;
  padding: 6px 14px;
  font-size: 13px;
  cursor: pointer;
}
#fs-exit:hover { background: rgba(30, 34, 42, 0.85); }
body.fsmode #fs-exit { display: block; }
"""

_SLIDE_JS = """
(function () {
  var slides = Array.prototype.slice.call(document.querySelectorAll('.slide'));
  var indicator = document.getElementById('page-indicator');
  var prevBtn = document.getElementById('prev');
  var nextBtn = document.getElementById('next');
  var current = 0;

  function show(index) {
    if (index < 0 || index >= slides.length) return;
    slides[current].classList.remove('active');
    current = index;
    slides[current].classList.add('active');
    indicator.textContent = (current + 1) + ' / ' + slides.length;
    prevBtn.disabled = current === 0;
    nextBtn.disabled = current === slides.length - 1;
    document.getElementById('slide-label').textContent = slides[current].dataset.title || '';
  }

  prevBtn.addEventListener('click', function () { show(current - 1); });
  nextBtn.addEventListener('click', function () { show(current + 1); });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowLeft' || e.key === 'PageUp') show(current - 1);
    else if (e.key === 'ArrowRight' || e.key === 'PageDown' || e.key === ' ') show(current + 1);
    else if (e.key === 'Home') show(0);
    else if (e.key === 'End') show(slides.length - 1);
  });
  var touchStartX = null;
  document.addEventListener('touchstart', function (e) { touchStartX = e.touches[0].clientX; });
  document.addEventListener('touchend', function (e) {
    if (touchStartX === null) return;
    var dx = e.changedTouches[0].clientX - touchStartX;
    if (Math.abs(dx) > 50) show(dx < 0 ? current + 1 : current - 1);
    touchStartX = null;
  });

  var fullscreenBtn = document.getElementById('fullscreen');
  var fsExitBtn = document.getElementById('fs-exit');
  // 保存各 SVG 原始比例，全屏时拉伸铺满、退出时恢复
  var svgEls = Array.prototype.slice.call(document.querySelectorAll('.slide-body svg'));
  var origRatios = svgEls.map(function (s) {
    return s.getAttribute('preserveAspectRatio') || 'xMidYMid meet';
  });
  function setStretch(on) {
    svgEls.forEach(function (s, i) {
      s.setAttribute('preserveAspectRatio', on ? 'none' : origRatios[i]);
    });
  }
  function isFullscreen() {
    return !!(document.fullscreenElement || document.webkitFullscreenElement);
  }
  function enterFullscreen() {
    var el = document.documentElement;
    (el.requestFullscreen || el.webkitRequestFullscreen).call(el);
  }
  function exitFullscreen() {
    (document.exitFullscreen || document.webkitExitFullscreen).call(document);
  }
  function updateFullscreenState() {
    var fs = isFullscreen();
    document.body.classList.toggle('fsmode', fs);
    setStretch(fs);
    fullscreenBtn.textContent = fs ? '退出全屏' : '全屏';
  }
  fullscreenBtn.addEventListener('click', enterFullscreen);
  fsExitBtn.addEventListener('click', function (e) {
    e.stopPropagation();
    exitFullscreen();
  });
  document.addEventListener('fullscreenchange', updateFullscreenState);
  document.addEventListener('webkitfullscreenchange', updateFullscreenState);

  // 全屏时：点击画面左/右 1/3 区域翻页
  document.addEventListener('click', function (e) {
    if (!isFullscreen()) return;
    var ratio = e.clientX / window.innerWidth;
    if (ratio < 0.3) show(current - 1);
    else if (ratio > 0.7) show(current + 1);
  });

  show(0);
})();
"""


def _clean_svg(raw: str) -> str:
    """Strip XML declaration / DOCTYPE so the SVG embeds cleanly in HTML."""
    cleaned = _XML_DECL_RE.sub('', raw)
    cleaned = _DOCTYPE_RE.sub('', cleaned)
    return cleaned.strip()


def _viewbox_ratio(svg: str) -> float | None:
    """Return the width/height ratio from the SVG viewBox, if present."""
    m = _VIEWBOX_RE.search(svg)
    if not m:
        return None
    parts = m.group(1).split()
    if len(parts) < 4:
        return None
    try:
        w = float(parts[2])
        h = float(parts[3])
    except ValueError:
        return None
    return w / h if h else None


def _find_svg_dir(project_path: Path, source: str) -> Path:
    """Resolve the SVG directory to read pages from."""
    if source == 'final':
        return project_path / 'svg_final'
    if source == 'output':
        return project_path / 'svg_output'
    # auto: prefer finalized, fall back to raw output
    final = project_path / 'svg_final'
    if final.exists() and any(final.glob('*.svg')):
        return final
    return project_path / 'svg_output'


def _load_notes(project_path: Path, stems: list[str]) -> dict[str, str]:
    """Load per-page speaker notes, from per-page files or total.md."""
    notes: dict[str, str] = {}
    notes_dir = project_path / 'notes'
    total_md = notes_dir / 'total.md'

    for stem in stems:
        page_file = notes_dir / f"{stem}.md"
        if page_file.exists():
            try:
                notes[stem] = page_file.read_text(encoding='utf-8').strip()
            except OSError:
                notes[stem] = ''
            continue
        if total_md.exists():
            parsed = _parse_total_md(total_md, stems)
            if stem in parsed:
                notes[stem] = parsed[stem]

    return notes


def _parse_total_md(total_md: Path, stems: list[str]) -> dict[str, str]:
    """Parse total.md, matching each heading to its SVG stem by leading number."""
    stem_by_num: dict[int, str] = {}
    for stem in stems:
        m = re.match(r'^(\d{1,3})', stem)
        if m:
            stem_by_num[int(m.group(1))] = stem

    result: dict[str, str] = {}
    current_num: int | None = None
    lines: list[str] = []
    for line in total_md.read_text(encoding='utf-8').splitlines():
        m = _HEADING_RE.match(line)
        if m:
            if current_num is not None and current_num in stem_by_num:
                result[stem_by_num[current_num]] = '\n'.join(lines).strip()
            num_m = re.match(r'^(\d{1,3})', m.group(2).strip())
            current_num = int(num_m.group(1)) if num_m else None
            lines = []
            continue
        if current_num is not None:
            lines.append(line)
    if current_num is not None and current_num in stem_by_num:
        result[stem_by_num[current_num]] = '\n'.join(lines).strip()
    return result


def _notes_to_html(text: str) -> str:
    """Convert plain-text notes into escaped <p> paragraphs."""
    paragraphs = [html.escape(p.strip()) for p in text.splitlines() if p.strip()]
    return ''.join(f'<p>{p}</p>' for p in paragraphs)


def build_html(
    title: str,
    slides: list[dict],
    *,
    with_notes: bool = True,
) -> str:
    """Assemble the complete self-contained HTML document."""
    sections = []
    for i, slide in enumerate(slides):
        body_style = ''
        if slide['ratio']:
            body_style = f' style="aspect-ratio:{slide["ratio"]:.6f}"'
        notes_html = ''
        if with_notes and slide['notes']:
            notes_html = (
                f'<details class="slide-notes"><summary>演讲者备注</summary>'
                f'{_notes_to_html(slide["notes"])}</details>'
            )
        active = ' active' if i == 0 else ''
        sections.append(
            f'<section class="slide{active}" data-index="{i}" data-title="{html.escape(slide["stem"])}">'
            f'<div class="slide-body"{body_style}>{slide["svg"]}</div>'
            f'{notes_html}'
            f'</section>'
        )

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>{_SLIDE_CSS}</style>
</head>
<body>
<div id="header">
  <h1>{html.escape(title)}</h1>
  <span class="spacer"></span>
  <span id="slide-label" class="slide-label"></span>
  <button id="fullscreen" type="button">全屏</button>
</div>
<div id="deck">
{chr(10).join(sections)}
</div>
<div id="controls">
  <button id="prev" type="button">上一页</button>
  <span id="page-indicator" class="page-indicator">1 / {len(slides)}</span>
  <button id="next" type="button">下一页</button>
</div>
<button id="fs-exit" type="button">退出全屏</button>
<script>{_SLIDE_JS}</script>
</body>
</html>
"""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description='Export a project\'s SVG pages as one self-contained HTML deck.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument('project_path', type=str, help='Project directory path')
    parser.add_argument('-o', '--output', type=str, default=None,
                        help='Output HTML file path (default: exports/<project_name>_<timestamp>.html)')
    parser.add_argument('--source', choices=['final', 'output', 'auto'], default='auto',
                        help='SVG source directory: finalized (default auto → svg_final, fallback svg_output)')
    parser.add_argument('--no-notes', action='store_true', help='Do not embed speaker notes')
    parser.add_argument('--title', type=str, default=None, help='Override the deck title (default: project dir name)')
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    project_path = Path(args.project_path)
    if not project_path.is_dir():
        print(f"Error: project path does not exist: {project_path}", file=sys.stderr)
        return 1

    svg_dir = _find_svg_dir(project_path, args.source)
    svg_files = sorted(svg_dir.glob('*.svg')) if svg_dir.exists() else []
    if not svg_files:
        print(f"Error: no SVG pages found in {svg_dir}", file=sys.stderr)
        return 1

    stems = [p.stem for p in svg_files]
    notes = {} if args.no_notes else _load_notes(project_path, stems)

    slides = []
    for path in svg_files:
        svg = _clean_svg(path.read_text(encoding='utf-8'))
        slides.append({
            'stem': path.stem,
            'svg': svg,
            'ratio': _viewbox_ratio(svg),
            'notes': notes.get(path.stem, ''),
        })

    title = args.title or project_path.name
    document = build_html(title, slides, with_notes=not args.no_notes)

    if args.output:
        output_path = Path(args.output)
    else:
        stamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_path = project_path / 'exports' / f"{project_path.name}_{stamp}.html"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(document, encoding='utf-8')

    print(output_path.resolve())
    print(f"[OK] Exported {len(slides)} slides to {output_path}", file=sys.stderr)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
