import json

with open('frontend/benchmarks_data.json', 'r', encoding='utf-8') as f:
    benchmarks_data = json.load(f)

with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

print("Synchronized app.js and frontend/app.js successfully!")
