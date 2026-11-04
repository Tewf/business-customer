"""Customer study: a study protocol declares its sample, its question order and its incentive before the first interview.

A file matched by `[customer_study] files` of checks/config.toml must hold three sections, each with a heading that
starts with its name:
- `Sample`: a size as `N = <number>` and the words frame and recruit (who is asked, and how they are reached);
- `Question order`: a numbered list of at least two questions, in the order they are asked;
- `Incentive`: a sentence that either says none or gives an amount, a prize or a delivery, and says who pays it.

A run with no error guarantees: no protocol leaves out the three things that bend an answer before it is given. It does
not guarantee the sample is representative, the order unbiased or the incentive compatible (judgment). Time O(text).
"""
from __future__ import annotations

import fnmatch
import re
from pathlib import Path

from framework.check_api import Finding, files_in_scope

NAME = "customer-study"
EXACT = True

HEADING = re.compile(r"^#{1,6}\s+(.*?)\s*$")
SIZE = re.compile(r"\bN\s*=\s*\d+", re.IGNORECASE)
NUMBERED = re.compile(r"^\s*\d+[.)]\s+\S")
INCENTIVE = re.compile(r"\bnone\b|\bno incentive\b|\d|\bprize\b|\bdeposit\b|\bdelivery\b|\bvoucher\b", re.IGNORECASE)
PAYER = re.compile(r"\bpaid by\b|\bpays\b|\bfunded by\b|\bnobody\b|\bnone\b", re.IGNORECASE)


def sections(text: str) -> dict[str, tuple[int, list[str]]]:
    """Each heading's lowercase title mapped to its first line number and its body lines."""
    found: dict[str, tuple[int, list[str]]] = {}
    current = None
    for number, line in enumerate(text.splitlines(), 1):
        match = HEADING.match(line)
        if match:
            current = match.group(1).lower()
            found[current] = (number, [])
        elif current:
            found[current][1].append(line)
    return found


def section(found: dict, name: str):
    """The (line, body) of the first heading starting with name, or None."""
    for title, value in found.items():
        if title.startswith(name):
            return value
    return None


def check(root: Path, config: dict) -> list[Finding]:
    """One finding per missing or empty declaration, in each file the config names."""
    patterns = config.get("customer_study", {}).get("files", [])
    findings = []
    for path in files_in_scope(root, config, {".md"}):
        if not any(fnmatch.fnmatch(path, pattern) for pattern in patterns):
            continue
        found = sections((root / path).read_text(encoding="utf-8", errors="replace"))

        def fail(line: int, message: str) -> None:
            findings.append(Finding(NAME, path, line, message))

        sample = section(found, "sample")
        if sample is None:
            fail(1, "no Sample section: say who is asked, how many, and how they are reached")
        else:
            body = "\n".join(sample[1])
            if not SIZE.search(body):
                fail(sample[0], "the Sample section gives no size as N = <number>")
            if not (re.search(r"\bframe\b", body, re.I) and re.search(r"\brecruit", body, re.I)):
                fail(sample[0], "the Sample section names no frame and no recruitment")
        order = section(found, "question order")
        if order is None:
            fail(1, "no Question order section: list the questions in the order they are asked")
        elif sum(1 for line in order[1] if NUMBERED.match(line)) < 2:
            fail(order[0], "the Question order section is not a numbered list of at least two questions")
        incentive = section(found, "incentive")
        if incentive is None:
            fail(1, "no Incentive section: say what a respondent gets, or that nothing is given")
        else:
            body = "\n".join(incentive[1])
            if not INCENTIVE.search(body) or not PAYER.search(body):
                fail(incentive[0], "the Incentive section says neither what is given (or none) nor who pays it")
    return findings
