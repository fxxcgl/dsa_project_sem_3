def rank_of_bug(ranked, buggy_fn):
    for position, (fn, score) in enumerate(ranked, start=1):
        if fn == buggy_fn:
            return position
    return None
def top_k(ranks, k):
    hits = [r for r in ranks if r is not None and r <= k]
    return len(hits) / len(ranks)

def mrr(ranks):
    total = sum(1 / r for r in ranks if r is not None)
    return total / len(ranks)

if __name__ == "__main__":
    ranks = [1, 2, 1, 6, None]  # 5 bugs
    print(top_k(ranks, 1))
    print(top_k(ranks, 5))
    print(mrr(ranks))