from collect import load_trace
from localize import count_tests, rank_functions
from evaluate import best_rank, top_k, mrr

BUGS = [
    ("cookiecutter_trace.json", ["generate.py::generate_context"]),
    ("cookiecutter2_trace.json", ["hooks.py::find_hook", "hooks.py::run_hook"]),
    ("cookiecutter3_trace.json", ["prompt.py::read_user_choice"]),
]

ranks = []
for trace_file, answers in BUGS:
    results = load_trace(trace_file)
    counts, total_failed = count_tests(results)
    ranked = rank_functions(counts, total_failed)
    r = best_rank(ranked, answers)
    ranks.append(r)
    print(trace_file, "tests:", len(results), "failed:", total_failed, "rank:", r)
    print("   top:", [(f, round(s, 3)) for f, s in ranked[:6]])
    for name in [f for f, s in ranked[:6]] + answers:
        print("     ", name, counts.get(name))

print("Top-1:", top_k(ranks, 1))
print("Top-5:", top_k(ranks, 5))
print("MRR:", mrr(ranks))