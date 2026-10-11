import sys
import os
import json

def trace_functions(test_func, source_file):
    called = set()
    passed = True

    def profiler(frame, event, arg):
        if event == "call":
            code = frame.f_code
            if os.path.basename(code.co_filename) == source_file:
                called.add(code.co_name)

    sys.setprofile(profiler)
    try:
        test_func()
    except AssertionError:
        passed = False
    finally:
        sys.setprofile(None)
    return called, passed
def run_all_tests(test_module, source_file):
    results = []
    for name in dir(test_module):
        if name.startswith("test_"):
            func = getattr(test_module, name)
            results.append(trace_functions(func, source_file))
    return results

def load_trace(path):
    with open(path) as f:
        data = json.load(f)
    out = []
    for v in data.values():
        funcs = {f for f in v["functions"] if "::<" not in f}
        out.append((funcs, v["passed"]))
    return out

if __name__ == "__main__":
    sys.path.insert(0, "sample")
    import test_calc
    print(trace_functions(test_calc.test_describe, "calc.py"))
    print(trace_functions(test_calc.test_add, "calc.py"))