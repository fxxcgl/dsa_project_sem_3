import subprocess

def file_churn(path):
    out = subprocess.run(
        ["git", "log", "--oneline", "--", path],
        capture_output=True, text=True
    ).stdout
    return len(out.splitlines())

from radon.complexity import cc_visit

def function_complexity(path):
    with open(path) as f:
        code = f.read()
    return {b.name: b.complexity for b in cc_visit(code)}

if __name__ == "__main__":
    print(file_churn("sample/calc.py"))
    print(function_complexity("sample/calc.py"))