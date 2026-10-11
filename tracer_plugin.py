import sys
import os
import json
import pytest

ROOT = os.path.normcase(os.path.abspath("cookiecutter"))
records = {}
current = set()

def profiler(frame, event, arg):
    if event == "call":
        path = os.path.normcase(os.path.abspath(frame.f_code.co_filename))
        if path.startswith(ROOT):
            current.add(os.path.basename(path) + "::" + frame.f_code.co_name)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call(item):
    current.clear()
    sys.setprofile(profiler)
    yield
    sys.setprofile(None)
    records[item.nodeid] = {"functions": sorted(current)}

def pytest_runtest_logreport(report):
    if report.when == "call":
        if report.skipped:
            records.pop(report.nodeid, None)
        else:
            records[report.nodeid]["passed"] = report.passed
def pytest_sessionfinish(session):
    with open("trace.json", "w") as f:
        json.dump(records, f)
