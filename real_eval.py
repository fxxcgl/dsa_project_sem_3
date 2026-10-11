from collect import load_trace
from localize import count_tests, rank_functions
from evaluate import rank_of_bug

results = load_trace("cookiecutter_trace.json")
counts, total_failed = count_tests(results)
ranked = rank_functions(counts, total_failed)

print("tests:", len(results), "failed:", total_failed)
print(ranked[:5])
print("rank:", rank_of_bug(ranked, "generate.py::generate_context"))