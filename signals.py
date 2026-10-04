import subprocess

def file_churn(path):
    out = subprocess.run(
        ["git", "log", "--oneline", "--", path],
        capture_output=True, text=True
    ).stdout
    return len(out.splitlines())

if __name__ == "__main__":
    print(file_churn("sample/calc.py"))