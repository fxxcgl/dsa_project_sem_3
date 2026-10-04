from collect import run_all_tests
from localize import count_tests, rank_functions

def localize_bug(test_module, source_file):
    results = run_all_tests(test_module, source_file)
    counts, total_failed = count_tests(results)
    return rank_functions(counts, total_failed)

if __name__ == "__main__":
    import sys
    sys.path.insert(0, "sample")
    import test_calc
    print(localize_bug(test_calc, "calc.py"))