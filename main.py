import sys
sys.path.insert(0, "sample")

import test_calc
from collect import run_all_tests
from localize import count_tests, rank_functions
from signals import file_churn, function_complexity
from features import build_features

results = run_all_tests(test_calc, "calc.py")
counts, total_failed = count_tests(results)
ranked = rank_functions(counts, total_failed)

churn = file_churn("sample/calc.py")
complexity = function_complexity("sample/calc.py")

for row in build_features(ranked, churn, complexity):
    print(row)