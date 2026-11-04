"""Tests of checks/local/customer_study.py: it fails where a protocol hides a declaration and is silent where it does not.

Run: python3 -m unittest discover -s checks
The standard's checks/ folder must be importable: set READER_ERGONOMICS_CHECKS to it, or extract the release in
checks/out/standard (AGENTS.md).
"""
import importlib.util
import os
import sys
import tempfile
import unittest
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parents[1]
CANDIDATES = [os.environ.get("READER_ERGONOMICS_CHECKS", ""), REPOSITORY / "checks" / "out" / "standard" / "checks",
              REPOSITORY.parent / "standard" / "checks", REPOSITORY.parent / "reader-ergonomics" / "checks"]
sys.path.insert(0, str(next(Path(c) for c in CANDIDATES if c and (Path(c) / "framework").is_dir())))
spec = importlib.util.spec_from_file_location("customer_study", REPOSITORY / "checks" / "local" / "customer_study.py")
study = importlib.util.module_from_spec(spec)
spec.loader.exec_module(study)

CONFIG = {"customer_study": {"files": ["studies/*.md"]}}
GOOD = """# Study

## Sample

The frame is the members of one club. N = 12, recruited by the club's own mailing.

## Question order

1. What did you do last time?
2. What did you pay?

## Incentive

None. Nobody pays the respondents.
"""


def run(text: str) -> list:
    with tempfile.TemporaryDirectory() as folder:
        root = Path(folder)
        (root / "studies").mkdir()
        (root / "studies" / "a.md").write_text(text, encoding="utf-8")
        return study.check(root, CONFIG)


class CustomerStudyTest(unittest.TestCase):
    def test_complete_protocol_passes(self):
        self.assertEqual(run(GOOD), [])

    def test_missing_sample_fails(self):
        self.assertTrue(run(GOOD.replace("## Sample", "## Who")))

    def test_sample_without_size_fails(self):
        self.assertTrue(run(GOOD.replace("N = 12, ", "")))

    def test_order_not_numbered_fails(self):
        self.assertTrue(run(GOOD.replace("1. What", "- What").replace("2. What", "- What")))

    def test_missing_incentive_fails(self):
        self.assertTrue(run(GOOD.replace("## Incentive", "## Thanks")))

    def test_incentive_without_payer_fails(self):
        self.assertTrue(run(GOOD.replace("None. Nobody pays the respondents.", "A voucher of 10 euros.")))

    def test_unmatched_file_is_ignored(self):
        with tempfile.TemporaryDirectory() as folder:
            (Path(folder) / "x.md").write_text("# Nothing\n", encoding="utf-8")
            self.assertEqual(study.check(Path(folder), CONFIG), [])


if __name__ == "__main__":
    unittest.main()
