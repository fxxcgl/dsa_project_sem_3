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