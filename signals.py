import subprocess


def file_churn(path):
    try:
        out = subprocess.run(
            ["git", "log", "--oneline", "--", path],
            capture_output=True,
            text=True,
            check=False,
        ).stdout
    except OSError:
        return 0
    return len(out.splitlines())


try:
    from radon.complexity import cc_visit
except ImportError:  # pragma: no cover - optional dependency fallback
    cc_visit = None


def function_complexity(path):
    try:
        with open(path) as f:
            code = f.read()
    except OSError:
        return {}

    if cc_visit is None:
        return {}
    return {b.name: b.complexity for b in cc_visit(code)}


if __name__ == "__main__":
    print(file_churn("sample/calc.py"))
    print(function_complexity("sample/calc.py"))