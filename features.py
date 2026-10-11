def build_features(ranked, churn, complexity):
    rows = []
    for fn, score in ranked:
        rows.append({
            "function": fn,
            "ochiai": score,
            "churn": churn,
            "complexity": complexity.get(fn, 0),
        })
    return rows


def rerank(rows, w=0.1):
    if not rows:
        return []
    top = max(r["complexity"] for r in rows) or 1
    scored = [(r["function"], r["ochiai"] + w * r["complexity"] / top) for r in rows]
    return sorted(scored, key=lambda x: (-x[1], x[0]))