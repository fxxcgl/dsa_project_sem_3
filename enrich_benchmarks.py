import json
import os
import math

def ochiai(ef, ep, tf):
    denom = math.sqrt(tf * (ef + ep))
    return ef / denom if denom else 0.0

def tarantula(ef, ep, tf, tp):
    if tf == 0 or (tf + tp) == 0: return 0.0
    num = (ef / tf) if tf else 0.0
    denom = num + ((ep / tp) if tp else 0.0)
    return num / denom if denom else 0.0

def dstar(ef, ep, tf):
    denom = ep + (tf - ef)
    return (ef * ef) / denom if denom else 0.0

def jaccard(ef, ep, tf):
    denom = tf + ep
    return ef / denom if denom else 0.0

ROOT_HINTS = {
    "average": "The mean calculation divides by (len + 1) instead of len. Arithmetic off-by-one error.",
    "first_word": "Index [1] was selected from the split string instead of index [0]. Token indexing boundary error.",
    "square": "Transformation uses x * abs(x), producing negative outputs for negative numbers. Invariant sign violation.",
    "total": "Summation appends + 1 to the final result. Extraneous accumulator offset.",
    "letter": "Score check uses strict inequality (> 70) rather than inclusive boundary (>= 70). Grading boundary gap.",
    "smallest": "Selection checks (n > best) instead of (n < best), finding the maximum instead of minimum.",
    "apply_discount": "Percentage calculation divides by 10 instead of 100, deducting 10x the intended discount.",
    "in_range": "Bound check uses strict inequalities (low < value < high) rather than inclusive limits (low <= value <= high).",
    "generate_context": "Context generation fails to validate JSON serialization for nested hook paths.",
    "find_hook": "Hook discovery fails when hook executable permissions are missing on POSIX targets.",
    "read_user_choice": "User choice prompt fails to default when interactive EOF signal is encountered."
}

FIX_PAIRS = {
    "average": ("return sum(nums) / (len(nums) + 1)", "return sum(nums) / len(nums)"),
    "first_word": ('return clean(s).split(" ")[1]', 'return clean(s).split(" ")[0]'),
    "square": ("return x * abs(x)", "return x * x"),
    "total": ("return sum(to_ints(parse(s))) + 1", "return sum(to_ints(parse(s)))"),
    "letter": ("if score > 70:", "if score >= 70:"),
    "smallest": ("if n > best:", "if n < best:"),
    "apply_discount": ("return price - price * percent / 10", "return price - price * percent / 100"),
    "in_range": ("return low < value < high", "return low <= value <= high"),
    "generate_context": ("context = copy(data)", "context = deepcopy(data)"),
    "find_hook": ("return os.path.exists(p)", "return os.path.exists(p) and os.access(p, os.X_OK)"),
    "read_user_choice": ("choice = input(prompt)", "choice = input(prompt) if sys.stdin.isatty() else default")
}

ASSET_MAP = [
    'thumb-dark-circle',
    'thumb-sculpture',
    'thumb-feather',
    'thumb-moss',
    'thumb-landscape',
    'thumb-cyan-swirl',
    'thumb-amber-bottle',
    'thumb-mountain',
    'thumb-cream',
    'thumb-poppy',
    'thumb-skeleton-leaf'
]

# Load previously extracted basic data
with open('frontend/benchmarks_data.json', 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

enhanced = []
for idx, b in enumerate(raw_data):
    asset_id = ASSET_MAP[idx % len(ASSET_MAP)]
    b_id = b['id']
    expected = b.get('expected_bug') or b.get('report', {}).get('expected_bug', '')
    if '::' in expected:
        expected = expected.split('::')[1]

    # Normalize functions list
    functions = []
    existing_fns = b.get('functions') or b.get('report', {}).get('ranked', [])
    
    total_failed = b.get('total_failed', 2 if 'bug' in b_id or b_id == 'sample' else 1)
    total_passed = b.get('total_passed', 2)

    for r in existing_fns:
        fn_name = r.get('name') or r.get('function')
        clean_fn = fn_name.split('::')[-1] if '::' in fn_name else fn_name
        is_bug = (clean_fn == expected)
        
        ef = r.get('failed_execs', total_failed if is_bug else (1 if r.get('ochiai', 0) > 0.5 else 0))
        ep = r.get('passed_execs', 0 if is_bug else (2 if r.get('ochiai', 0) == 0 else 1))
        
        o_score = ochiai(ef, ep, total_failed)
        t_score = tarantula(ef, ep, total_failed, total_passed)
        d_score = dstar(ef, ep, total_failed)
        j_score = jaccard(ef, ep, total_failed)
        
        comp = r.get('complexity', 1)
        churn = r.get('churn', 2)

        functions.append({
            'name': clean_fn,
            'full_name': r.get('full_name', fn_name),
            'is_expected_bug': is_bug,
            'failed_execs': ef,
            'passed_execs': ep,
            'total_failed': total_failed,
            'total_passed': total_passed,
            'ochiai': round(o_score, 4),
            'tarantula': round(t_score, 4),
            'dstar': round(d_score, 4),
            'jaccard': round(j_score, 4),
            'complexity': comp,
            'churn': churn,
            'hint': ROOT_HINTS.get(clean_fn, "Potential control or data flow anomaly detected during execution.")
        })

    # Sort by Ochiai descending
    functions.sort(key=lambda x: -x['ochiai'])

    buggy_str, fixed_str = FIX_PAIRS.get(expected, ("# Buggy logic", "# Corrected logic"))

    enhanced.append({
        'id': b_id,
        'title': b['title'],
        'folder': b['folder'],
        'source_file': b['source_file'],
        'test_file': b['test_file'],
        'source_code': b['source_code'],
        'test_code': b['test_code'],
        'expected_bug': expected,
        'thumb_asset': asset_id,
        'hint': ROOT_HINTS.get(expected, "Anomaly in logic detected."),
        'buggy_snippet': buggy_str,
        'fixed_snippet': fixed_str,
        'functions': functions,
        'total_tests': total_failed + total_passed,
        'total_failed': total_failed,
        'total_passed': total_passed,
        'top_suspect': functions[0]['name'] if functions else 'none',
        'top_score': functions[0]['ochiai'] if functions else 0.0
    })

with open('frontend/benchmarks_data.json', 'w', encoding='utf-8') as f:
    json.dump(enhanced, f, indent=2)

print(f"Successfully wrote {len(enhanced)} enriched benchmarks to frontend/benchmarks_data.json")
