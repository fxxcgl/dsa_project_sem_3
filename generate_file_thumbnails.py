import os

files_meta = [
    {
        'id': 'sample',
        'file': 'calc.py',
        'asset': 'thumb-file-calc',
        'fail': 2,
        'pass': 2,
        'top_bug': 'average()',
        'color': '#3b82f6',
        'lines': ['def add(a, b):', '    return a + b', 'def average(nums):', '    return sum(nums) / len']
    },
    {
        'id': 'bug1',
        'file': 'textutil.py',
        'asset': 'thumb-file-textutil',
        'fail': 2,
        'pass': 2,
        'top_bug': 'first_word()',
        'color': '#8b5cf6',
        'lines': ['def clean(s):', '    return s.strip()', 'def first_word(s):', '    return s.split()[1]']
    },
    {
        'id': 'bug2',
        'file': 'mathutil.py',
        'asset': 'thumb-file-mathutil',
        'fail': 1,
        'pass': 2,
        'top_bug': 'square()',
        'color': '#06b6d4',
        'lines': ['def square(x):', '    return x * abs(x)', 'def cube(x):', '    return x * x * x']
    },
    {
        'id': 'bug3',
        'file': 'csvsum.py',
        'asset': 'thumb-file-csvsum',
        'fail': 1,
        'pass': 2,
        'top_bug': 'total()',
        'color': '#10b981',
        'lines': ['def parse(s):', '    return s.split(",")', 'def total(s):', '    return sum(p) + 1']
    },
    {
        'id': 'bug4',
        'file': 'grades.py',
        'asset': 'thumb-file-grades',
        'fail': 1,
        'pass': 2,
        'top_bug': 'letter()',
        'color': '#f59e0b',
        'lines': ['def letter(score):', '    if score > 70:', '        return "C"', '    return "F"']
    },
    {
        'id': 'bug5',
        'file': 'listutil.py',
        'asset': 'thumb-file-listutil',
        'fail': 1,
        'pass': 2,
        'top_bug': 'smallest()',
        'color': '#ec4899',
        'lines': ['def smallest(nums):', '    best = nums[0]', '    if n > best: best = n', '    return best']
    },
    {
        'id': 'bug6',
        'file': 'discount.py',
        'asset': 'thumb-file-discount',
        'fail': 1,
        'pass': 2,
        'top_bug': 'apply_discount()',
        'color': '#6366f1',
        'lines': ['def apply_discount(p, %):', '    return p - p*% / 10', 'def cart_total(p):', '    return sum(p)']
    },
    {
        'id': 'bug7',
        'file': 'ticketing.py',
        'asset': 'thumb-file-ticketing',
        'fail': 1,
        'pass': 4,
        'top_bug': 'in_range()',
        'color': '#14b8a6',
        'lines': ['def in_range(val, l, h):', '    return l < val < h', 'def valid_age(a):', '    return in_range(...)']
    },
    {
        'id': 'cookiecutter1',
        'file': 'generate.py',
        'asset': 'thumb-file-generate',
        'fail': 1,
        'pass': 27,
        'top_bug': 'generate_context()',
        'color': '#f97316',
        'lines': ['def generate_context():', '    context = copy(d)', '    apply_overwrites(...)', '    return ctx']
    },
    {
        'id': 'cookiecutter2',
        'file': 'hooks.py',
        'asset': 'thumb-file-hooks',
        'fail': 1,
        'pass': 17,
        'top_bug': 'find_hook()',
        'color': '#ef4444',
        'lines': ['def find_hook(name):', '    p = get_hook_path()', '    return os.path.exists', 'def run_hook(p): ...']
    },
    {
        'id': 'cookiecutter3',
        'file': 'prompt.py',
        'asset': 'thumb-file-prompt',
        'fail': 1,
        'pass': 11,
        'top_bug': 'read_user_choice()',
        'color': '#a855f7',
        'lines': ['def read_user_choice():', '    prompt = f"Select:"', '    return input(prompt)', '    # EOF unhandled']
    }
]

os.makedirs('frontend/assets', exist_ok=True)

for m in files_meta:
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <!-- Code File Background -->
  <rect width="200" height="200" rx="14" fill="#0d1117"/>
  
  <!-- Editor Window Header Bar -->
  <rect width="200" height="34" rx="14" fill="#161b22"/>
  <rect y="20" width="200" height="14" fill="#161b22"/>
  
  <!-- Window Control Dots -->
  <circle cx="16" cy="17" r="4.5" fill="#ef4444"/>
  <circle cx="29" cy="17" r="4.5" fill="#eab308"/>
  <circle cx="42" cy="17" r="4.5" fill="#22c55e"/>
  
  <!-- File Extension Badge -->
  <rect x="145" y="9" width="42" height="16" rx="4" fill="{m['color']}" opacity="0.25"/>
  <text x="166" y="21" fill="{m['color']}" font-family="'JetBrains Mono', Consolas, monospace" font-size="10" font-weight="700" text-anchor="middle">.PY</text>

  <!-- Filename Header -->
  <text x="14" y="58" fill="#f0f6fc" font-family="'JetBrains Mono', Consolas, monospace" font-size="14" font-weight="700">{m['file']}</text>
  
  <!-- Subtitle: Suspect Defect Target -->
  <text x="14" y="74" fill="#8b949e" font-family="system-ui, sans-serif" font-size="9" font-weight="600">TARGET: {m['top_bug']}</text>

  <!-- Code Syntax Lines Mockup -->
  <g opacity="0.85">
    <rect x="14" y="90" width="45" height="5" rx="2.5" fill="#ff7b72"/>
    <rect x="64" y="90" width="70" height="5" rx="2.5" fill="#79c0ff"/>
    <rect x="139" y="90" width="25" height="5" rx="2.5" fill="#d2a8ff"/>

    <rect x="24" y="104" width="38" height="5" rx="2.5" fill="#ff7b72"/>
    <rect x="67" y="104" width="85" height="5" rx="2.5" fill="#a5d6ff"/>

    <!-- Highlighted Buggy Line with red glow -->
    <rect x="14" y="117" width="172" height="18" rx="4" fill="#ff4444" opacity="0.18" stroke="#ff4444" stroke-width="1"/>
    <rect x="24" y="123" width="55" height="6" rx="3" fill="#ff7b72"/>
    <rect x="84" y="123" width="75" height="6" rx="3" fill="#ffa657"/>

    <rect x="14" y="144" width="48" height="5" rx="2.5" fill="#ff7b72"/>
    <rect x="67" y="144" width="60" height="5" rx="2.5" fill="#79c0ff"/>
  </g>

  <!-- Bottom Status Footer -->
  <rect x="10" y="162" width="180" height="26" rx="6" fill="#161b22"/>
  
  <!-- Failure Badge -->
  <circle cx="22" cy="175" r="4" fill="#f85149"/>
  <text x="32" y="179" fill="#f85149" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700">{m['fail']} FAIL</text>
  
  <!-- Pass Badge -->
  <text x="140" y="179" fill="#56d364" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="600">{m['pass']} PASS</text>
</svg>"""

    with open(f'frontend/assets/{m["asset"]}.svg', 'w', encoding='utf-8') as f:
        f.write(svg)

print(f"Generated {len(files_meta)} code file thumbnails in frontend/assets/ successfully.")
