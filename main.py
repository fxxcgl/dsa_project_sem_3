import argparse

from quality_report import analyze_project, format_report


def main():
    parser = argparse.ArgumentParser(description="Bug localization and software quality analysis demo.")
    parser.add_argument("--project", default="sample", help="Folder containing a Python test module and source file to inspect.")
    parser.add_argument("--show-fixes", action="store_true", help="Print suggested validation steps for the top suspects.")
    parser.add_argument("--json", action="store_true", help="Print the raw report as JSON.")
    args = parser.parse_args()

    report = analyze_project(args.project)
    if args.json:
        import json
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(format_report(report, show_fix_suggestions=args.show_fixes))


if __name__ == "__main__":
    main()