import sys
import importlib
from pipeline import localize_bug
from evaluate import rank_of_bug, top_k, mrr
from signals import function_complexity
from features import build_features, rerank

# (folder, test module, source file, known buggy function)
BUGS = [
    ("sample", "test_calc", "calc.py", "average"),
    ("bugs/bug1", "test_textutil", "textutil.py", "first_word"),
    ("bugs/bug2", "test_mathutil", "mathutil.py", "square"),
    ("bugs/bug3", "test_csvsum", "csvsum.py", "total"),
]

ranks = []
ranks2 = []
for folder, test_name, source, buggy in BUGS:
    sys.path.insert(0, folder)
    module = importlib.import_module(test_name)
    ranked = localize_bug(module, source)
    rows = build_features(ranked, 0, function_complexity(f"{folder}/{source}"))
    ranks2.append(rank_of_bug(rerank(rows), buggy))
    r = rank_of_bug(ranked, buggy)
    ranks.append(r)
    print(folder, buggy, "rank:", r)
    sys.path.pop(0)

print("Top-1:", top_k(ranks, 1))
print("Top-5:", top_k(ranks, 5))
print("MRR:", mrr(ranks))
print("Combined Top-1:", top_k(ranks2, 1))
print("Combined MRR:", mrr(ranks2))