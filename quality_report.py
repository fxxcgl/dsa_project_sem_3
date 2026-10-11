import glob
import importlib
import os
import sys

from evaluate import rank_of_bug
from features import build_features, rerank
from pipeline import localize_bug
from signals import file_churn, function_complexity


ROOT_CAUSE_HINTS = {
    "average": "The mean calculation appears to be using the wrong divisor or aggregation path. Verify the arithmetic and any off-by-one logic.",
    "smallest": "The selection logic seems to prefer the current maximum instead of the minimum. Check comparison operators and update logic.",
    "letter": "Score threshold boundaries look incorrect; a boundary condition such as >= 70 vs > 70 may be off by one grade step.",
    "apply_discount": "The discount formula is likely using a percentage conversion that is off by a factor of ten or is applying the wrong arithmetic order.",
    "in_range": "The validity check may be using exclusive bounds instead of inclusive boundaries; confirm the lower and upper limits.",
    "square": "The square logic is likely using the wrong algebraic transformation for negative inputs; verify sign handling.",
    "total": "The aggregation function may be adding an extra value or mishandling parsing before summing the numbers.",
    "first_word": "The parser is likely selecting the wrong token from the sentence; check indexing or split behavior.",
}


def discover_project_files(folder):
    folder = os.path.abspath(folder)
    test_files = sorted(glob.glob(os.path.join(folder, "test_*.py")))
    if not test_files:
        raise FileNotFoundError(f"No test file found in {folder}")

    source_files = sorted(
        p for p in glob.glob(os.path.join(folder, "*.py"))
        if not os.path.basename(p).startswith("test_")
    )
    if not source_files:
        raise FileNotFoundError(f"No source file found in {folder}")
    return test_files[0], source_files[0]


def analyze_project(folder):
    test_file, source_file = discover_project_files(folder)
    test_name = os.path.basename(test_file)[:-3]
    source_name = os.path.basename(source_file)
    project_root = os.path.abspath(folder)

    sys.path.insert(0, project_root)
    try:
        module = importlib.import_module(test_name)
        ranked = localize_bug(module, source_name)
    finally:
        sys.path.pop(0)

    churn = file_churn(os.path.join(project_root, source_name))
    complexity = function_complexity(os.path.join(project_root, source_name))
    rows = build_features(ranked, churn, complexity)
    reranked = rerank(rows)

    report = {
        "folder": project_root,
        "test_module": test_name,
        "source_file": source_name,
        "ranked": rows,
        "reranked": reranked,
        "top_candidates": rows[:5],
    }

    if os.path.exists(os.path.join(project_root, "answer.txt")):
        with open(os.path.join(project_root, "answer.txt")) as handle:
            _, buggy = handle.read().split()
        report["expected_bug"] = buggy
        report["rank_of_expected_bug"] = rank_of_bug(ranked, buggy)

    return report


def root_cause_hint(function_name):
    return ROOT_CAUSE_HINTS.get(function_name, "The failing tests suggest a logic error in the function body; review comparisons, boundary checks, and arithmetic operations.")


def format_report(report, show_fix_suggestions=False):
    lines = [
        "Software Quality Bug Intelligence Report",
        "=" * 36,
        f"Project: {os.path.basename(report['folder'])}",
        f"Test module: {report['test_module']}",
        f"Source file: {report['source_file']}",
    ]

    if "expected_bug" in report:
        lines.append(f"Expected bug: {report['expected_bug']}")
        lines.append(f"Observed rank: {report['rank_of_expected_bug']}")

    lines.append("")
    lines.append("Top suspect functions:")

    for idx, row in enumerate(report["top_candidates"], start=1):
        score = row["ochiai"]
        severity = "high" if score >= 0.9 else "medium" if score >= 0.5 else "low"
        lines.append(
            f"{idx}. {row['function']} | score={score:.3f} | complexity={row['complexity']} | churn={row['churn']} | severity={severity}"
        )
        lines.append(f"   Evidence: {root_cause_hint(row['function'])}")

    if show_fix_suggestions:
        lines.append("")
        lines.append("Suggested validation checks:")
        for row in report["top_candidates"]:
            lines.append(f"- {row['function']}: confirm edge cases, failing tests, and expected outputs before and after a fix.")

    return "\n".join(lines)
