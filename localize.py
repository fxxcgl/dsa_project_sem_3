from math import sqrt

def ochiai(failed_s, passed_s, total_failed):
    denom = sqrt(total_failed * (failed_s + passed_s))
    return failed_s / denom if denom else 0.0

def count_tests(results):
    counts = {}
    total_failed = 0
    for called, passed in results:
        if not passed:
            total_failed += 1
        for fn in called:
            c = counts.setdefault(fn, {"failed": 0, "passed": 0})
            c["passed" if passed else "failed"] += 1
    return counts, total_failed

def rank_functions(counts, total_failed):
    scores = {}
    for fn, c in counts.items():
        scores[fn] = ochiai(c["failed"], c["passed"], total_failed)
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    results = [
        ({"add"}, True),
        ({"multiply"}, True),
        ({"average"}, False),
        ({"describe", "average"}, False),
    ]
    counts, total_failed = count_tests(results)
    print(rank_functions(counts, total_failed))