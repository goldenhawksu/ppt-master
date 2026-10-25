#!/usr/bin/env python3
"""AESC SVG 审计器的最小回归用例。"""

from __future__ import annotations

import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPTS_DIR = Path(__file__).resolve().parents[1]
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from check_aesc_viz import INTENTS, audit, main


class CheckAescVizTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.svg_root = self.root / "svg_output"
        self.svg_root.mkdir()
        self.page = self.svg_root / "01_chart.svg"
        self.valid_svg = '''<svg xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 1280 720" data-viz-page-type="chart_insight_rail">
            <text id="cost-takeaway" x="56" y="100">Cost fell 18%</text>
            <g id="cost" data-viz-intent="ranking" data-viz-chart="horizontal_bar_chart">
            <rect x="100" y="200" width="360" height="32" fill="#2563EB"/>
            </g><text id="cost-source" x="56" y="670">Source: demo ledger; USD; Q3</text>
            </svg>'''
        self.page.write_text(self.valid_svg, encoding="utf-8")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def _report(self, svg: str) -> dict:
        self.page.write_text(svg, encoding="utf-8")
        return audit(self.root, require_charts=True)

    def test_valid_project_reports_one_chart(self) -> None:
        report = audit(self.root, require_charts=True)
        self.assertEqual(report["summary"], {
            "pages": 1, "chart_pages": 1, "charts": 1, "errors": 0, "warnings": 0,
        })

    def test_all_nine_intents_are_accepted(self) -> None:
        for intent in INTENTS:
            with self.subTest(intent=intent):
                report = self._report(self.valid_svg.replace('intent="ranking"', f'intent="{intent}"'))
                self.assertEqual(report["summary"]["errors"], 0)

    def test_missing_visible_source_fails(self) -> None:
        report = self._report(self.valid_svg.replace('id="cost-source"', 'id="unrelated"'))
        self.assertGreater(report["summary"]["errors"], 0)

    def test_hidden_source_fails(self) -> None:
        for attribute in ('display="none"', 'opacity="0"', 'visibility="hidden"', 'style="display:none"'):
            with self.subTest(attribute=attribute):
                report = self._report(self.valid_svg.replace('id="cost-source"', f'id="cost-source" {attribute}'))
                self.assertGreater(report["summary"]["errors"], 0)

    def test_source_in_defs_fails(self) -> None:
        report = self._report(self.valid_svg.replace('<text id="cost-source"', '<defs><text id="cost-source"').replace('Q3</text>', 'Q3</text></defs>'))
        self.assertGreater(report["summary"]["errors"], 0)

    def test_placeholder_source_fails(self) -> None:
        report = self._report(self.valid_svg.replace('Source: demo ledger; USD; Q3', '{{SOURCE}}'))
        self.assertGreater(report["summary"]["errors"], 0)

    def test_duplicate_ids_fail(self) -> None:
        report = self._report(self.valid_svg.replace('</svg>', '<text id="cost-source">Duplicate</text></svg>'))
        self.assertGreater(report["summary"]["errors"], 0)

    def test_unknown_intent_and_catalog_key_fail(self) -> None:
        report = self._report(self.valid_svg.replace('ranking', 'unknown').replace('horizontal_bar_chart', 'missing_chart'))
        self.assertEqual(report["summary"]["errors"], 2)

    def test_custom_chart_requires_reason(self) -> None:
        custom = self.valid_svg.replace('horizontal_bar_chart', 'custom/slope')
        self.assertGreater(self._report(custom)["summary"]["errors"], 0)
        custom = custom.replace('data-viz-chart=', 'data-viz-reason="Two-period rank movement" data-viz-chart=')
        self.assertEqual(self._report(custom)["summary"]["errors"], 0)

    def test_bitmap_only_chart_fails(self) -> None:
        report = self._report(self.valid_svg.replace('<rect x="100" y="200" width="360" height="32" fill="#2563EB"/>', '<image href="chart.png"/>'))
        self.assertGreater(report["summary"]["errors"], 0)

    def test_native_chart_cannot_escape_annotations(self) -> None:
        report = self._report(self.valid_svg.replace('data-viz-intent="ranking"', 'data-pptx-replace-with="chart"'))
        self.assertEqual(report["summary"]["charts"], 1)
        self.assertGreater(report["summary"]["errors"], 0)

    def test_plot_marker_cannot_escape_annotations(self) -> None:
        svg = self.valid_svg.replace('data-viz-intent="ranking"', '')
        svg = svg.replace('</svg>', '<!-- chart-plot-area: object=cost | x=100 --></svg>')
        report = self._report(svg)
        self.assertEqual(report["summary"]["charts"], 1)
        self.assertGreater(report["summary"]["errors"], 0)

    def test_orphan_plot_marker_fails(self) -> None:
        report = self._report(self.valid_svg.replace('</svg>', '<!-- chart-plot-area: object=missing | x=100 --></svg>'))
        self.assertGreater(report["summary"]["errors"], 0)

    def test_shared_page_text_can_be_referenced(self) -> None:
        svg = self.valid_svg.replace('id="cost-source"', 'id="shared-source"')
        svg = svg.replace('data-viz-intent=', 'data-viz-source="shared-source" data-viz-intent=')
        self.assertEqual(self._report(svg)["summary"]["errors"], 0)

    def test_malformed_xml_and_non_svg_fail(self) -> None:
        for svg in ('<svg>', '<html/>'):
            with self.subTest(svg=svg):
                self.assertGreater(self._report(svg)["summary"]["errors"], 0)

    def test_three_repeated_page_types_warn(self) -> None:
        for name in ('02_chart.svg', '03_chart.svg'):
            (self.svg_root / name).write_text(self.valid_svg, encoding="utf-8")
        self.assertEqual(audit(self.root)["summary"]["warnings"], 1)

    def test_chartless_deck_is_optional_not_a_false_required_pass(self) -> None:
        self.page.write_text('<svg xmlns="http://www.w3.org/2000/svg"/>', encoding="utf-8")
        self.assertEqual(audit(self.root)["summary"]["errors"], 0)
        self.assertGreater(audit(self.root, require_charts=True)["summary"]["errors"], 0)

    def test_empty_target_fails(self) -> None:
        self.assertGreater(audit(self.root / "missing")["summary"]["errors"], 0)

    def test_cli_json_has_no_file_side_effects(self) -> None:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            status = main([str(self.root), '--require-charts', '--json'])
        self.assertEqual(status, 0)
        self.assertEqual(json.loads(output.getvalue())["summary"]["charts"], 1)
        self.assertEqual(sorted(path.name for path in self.root.iterdir()), ['svg_output'])

    def test_help_does_not_read_or_write_target(self) -> None:
        with contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaises(SystemExit) as raised:
                main(['--help'])
        self.assertEqual(raised.exception.code, 0)


if __name__ == "__main__":
    unittest.main()
