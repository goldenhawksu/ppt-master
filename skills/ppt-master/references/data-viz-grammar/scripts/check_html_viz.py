#!/usr/bin/env python3
"""HTML visualization audit — the page-level gate for single-file dashboards / reports.

Same intent as ppt-master's check_deck_viz.py, but for HTML instead of SVG:
catches card grids, drop shadows, accent-colour sprawl, sub-12px type, missing source
lines and noun-phrase titles. Heuristic by design (no browser needed, no deps).

Usage:
    python scripts/check_html_viz.py page.html
    python scripts/check_html_viz.py page.html --profile dashboard   # interactive board: <=6 saturated
    python scripts/check_html_viz.py page.html --strict              # warnings fail too
Exit 1 on ERROR (or on WARN with --strict).
"""
import argparse, os, re, sys

NAMED_NEUTRAL = {"white", "black", "transparent", "inherit", "none", "currentcolor"}
SOURCE_WORDS = ("数据来源", "来源：", "来源:", "口径", "资料来源", "Data source")
DIRECTION = ("升", "降", "超", "低", "高", "倍", "最", "首", "差", "转", "增", "减", "跌", "涨", "+", "-", "%")
PROFILES = {"editorial": (3, 5), "dashboard": (6, 9)}     # (warn_above, error_above)


def _rgb(h):
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    try:
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    except ValueError:
        return None


def is_neutral(colour):
    c = colour.strip().lower()
    if c in NAMED_NEUTRAL:
        return True
    if c.startswith("rgb"):
        nums = re.findall(r"\d+", c)
        if len(nums) >= 3:
            r, g, b = (int(n) for n in nums[:3])
        else:
            return True
    elif c.startswith("#"):
        rgb = _rgb(c)
        if rgb is None:
            return True
        r, g, b = rgb
    else:
        return True
    mx, mn = max(r, g, b), min(r, g, b)
    if mx == 0:
        return True
    if (mx - mn) / mx < 0.25:      # grey-ish
        return True
    if mn > 230:                    # near-white tint
        return True
    return False


def text_of(html):
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html, flags=re.S | re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"&nbsp;?", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def audit(path, profile="editorial"):
    raw = open(path, encoding="utf-8", errors="ignore").read()
    errs, warns = [], []
    body = re.sub(r"<script[^>]*>.*?</script>", " ", raw, flags=re.S | re.I)

    # 1) drop shadows (editorial grammar bans them; a hover shadow on a button is tolerable)
    shadows = [m for m in re.finditer(r"box-shadow\s*:\s*([^;}]+)", body, re.I)
               if m.group(1).strip().strip('"\' ').lower() not in ("none", "", "0")]
    if shadows:
        _msg = (f"{len(shadows)} box-shadow(s) — editorial grammar carries no shadows "
                f"(first: {shadows[0].group(1).strip()[:40]})" if profile == "editorial"
                else f"{len(shadows)} box-shadow(s) — fine for overlays/popovers, not for card grids")
        (errs if profile == "editorial" else warns).append(_msg)

    # 2) rounded containers used as cards
    radii = [float(v) for v in re.findall(r"border-radius\s*:\s*(\d+(?:\.\d+)?)px", body, re.I)]
    cards = [r for r in radii if r > 4]
    if len(cards) >= 3:
        warns.append(f"{len(cards)} rounded corners >4px — card-grid look; a card row needs 4 genuinely parallel points")

    # 3) accent colour budget
    colours = re.findall(r"#[0-9a-fA-F]{3,8}\b", body) + re.findall(r"rgba?\([^)]+\)", body)
    accent = {}
    for c in colours:
        if is_neutral(c):
            continue
        key = c.lower()
        accent[key] = accent.get(key, 0) + 1
    warn_above, err_above = PROFILES[profile]
    if len(accent) > err_above:
        errs.append(f"{len(accent)} saturated colours — cap is 1 accent + 1 semantic (profile={profile}); top: {sorted(accent, key=accent.get, reverse=True)[:6]}")
    elif len(accent) > warn_above:
        warns.append(f"{len(accent)} saturated colours — confirm each carries semantics: {sorted(accent, key=accent.get, reverse=True)[:6]}")

    # 4) font floor
    sizes = [float(v) for v in re.findall(r"font-size\s*:\s*(\d+(?:\.\d+)?)px", body, re.I)]
    if sizes and min(sizes) < 12:
        errs.append(f"smallest font-size {min(sizes):g}px < 12px (the '字太小' failure)")
    elif sizes and min(sizes) < 13:
        warns.append(f"smallest font-size {min(sizes):g}px — 12px is the floor, 13-14 reads better on projectors")

    # 5) source / scope line — only for pages that actually present data
    #    (a checklist or a discussion doc has nothing to source; demanding one there trains people to ignore the gate)
    charts = len(re.findall(r"<svg", raw, re.I)) + len(re.findall(r"<canvas", raw, re.I))
    tables = len(re.findall(r"<table", raw, re.I))
    txt = text_of(raw)
    has_source = any(w in txt for w in SOURCE_WORDS)
    if not has_source and (charts or tables):
        if charts + tables >= 2:
            errs.append(f"no source line (数据来源 / 口径) — this page shows {charts} chart(s) + {tables} table(s)")
        else:
            warns.append("no source line (数据来源 / 口径) — one data block still needs its 口径")

    # 6) title = conclusion, not a noun phrase
    m = re.search(r"<h1[^>]*>(.*?)</h1>", raw, re.S | re.I) or re.search(r"<title[^>]*>(.*?)</title>", raw, re.S | re.I)
    title = text_of(m.group(1)) if m else ""
    if not title:
        warns.append("no <h1>/<title> — the page has no stated argument")
    elif not any(d in title for d in DIRECTION) and not re.search(r"\d", title):
        msg = f"title has no number or direction word (noun phrase?): {title[:40]!r}"
        if profile == "dashboard":
            warns.append(msg + " — OK for a dashboard's product title; each panel still needs a conclusion heading")
        else:
            errs.append(msg)

    # 7) decorative gradients / 3D-ish text
    if len(re.findall(r"linear-gradient", body, re.I)) >= 3:
        warns.append(f"{len(re.findall('linear-gradient', body, re.I))} gradient fills — decoration competing with the data")
    if re.search(r"text-shadow\s*:", body, re.I):
        warns.append("text-shadow present — remove on data text")

    # 8) chart-ish volume
    svg_n = len(re.findall(r"<svg", raw, re.I))
    canvas_n = len(re.findall(r"<canvas", raw, re.I))
    if svg_n == 0 and canvas_n == 0 and tables:
        warns.append("tables but no <svg>/<canvas> — if a trend/comparison is buried in a table, chart it")

    stats = {"svg": svg_n, "canvas": canvas_n, "accent": len(accent), "min_font": min(sizes) if sizes else None,
             "title": title[:60]}
    return errs, warns, stats


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--strict", action="store_true", help="warnings fail too")
    ap.add_argument("--profile", choices=list(PROFILES), default="editorial",
                    help="editorial = 1 accent + 1 semantic; dashboard = interactive board, <=6 saturated")
    args = ap.parse_args()
    if not os.path.isfile(args.path):
        print("no such file:", args.path)
        return 1

    errs, warns, st = audit(args.path, args.profile)
    print(f"{os.path.basename(args.path)}  [{args.profile}]  svg={st['svg']} canvas={st['canvas']} "
          f"accent={st['accent']} min-font={st['min_font']}")
    print(f"  title: {st['title']!r}")
    for e in errs:
        print("  E", e)
    for w in warns:
        print("  W", w)
    print(f"\n{len(errs)} error(s) · {len(warns)} warning(s)")
    if errs or (args.strict and warns):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
