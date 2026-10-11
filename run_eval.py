import sys
import os
import glob
import importlib
from pipeline import localize_bug
from evaluate import rank_of_bug, top_k, mrr
from signals import function_complexity
from features import build_features, rerank

def load_bug(folder):
    with open(os.path.join(folder, "answer.txt")) as f:
        source, buggy = f.read().split()
    test_file = glob.glob(os.path.join(folder, "test_*.py"))[0]
    test_name = os.path.basename(test_file)[:-3]
    return test_name, source, buggy

folders = ["sample"] + sorted(glob.glob("bugs/*"))
ranks, ranks2 = [], []

for folder in folders:
    test_name, source, buggy = load_bug(folder)
    sys.path.insert(0, folder)
    module = importlib.import_module(test_name)
    ranked = localize_bug(module, source)
    r = rank_of_bug(ranked, buggy)
    ranks.append(r)
    rows = build_features(ranked, 0, function_complexity(f"{folder}/{source}"))
    ranks2.append(rank_of_bug(rerank(rows), buggy))
    print(folder, buggy, "rank:", r)
    sys.path.pop(0)

print("Top-1:", top_k(ranks, 1))
print("Top-5:", top_k(ranks, 5))
print("MRR:", mrr(ranks))
print("Combined Top-1:", top_k(ranks2, 1))
print("Combined MRR:", mrr(ranks2))