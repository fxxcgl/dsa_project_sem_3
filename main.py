import sys
sys.path.insert(0, "sample")

import test_calc
from collect import run_all_tests
from localize import count_tests, rank_functions

results = run_all_tests(test_calc, "calc.py")
counts, total_failed = count_tests(results)
print(rank_functions(counts, total_failed))