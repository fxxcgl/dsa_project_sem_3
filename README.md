# Bug Intelligence Demo

This project is a compact Python proof of concept for a software quality and bug-localization workflow. It focuses on one bounded scope: identifying the most likely faulty function from a failing test suite using execution traces, Ochiai scoring, and code signals.

## What the project does

- Runs each test in a project module and captures the functions that were called.
- Counts failed vs passed executions for each function.
- Scores suspicious functions with Ochiai similarity.
- Combines the ranking with simple file churn and function complexity signals.
- Produces an evidence-based report for the likely defect area.

## Included demo data

The repository includes:

- `sample/` – a tiny calculator project with failing tests to demonstrate the workflow.
- `bugs/` – several intentionally buggy mini-projects used as benchmark fixtures.
- `cookiecutter*_trace.json` – trace records for larger real-world bug-localization examples.

## Running the project

```bash
python main.py --project sample
python main.py --project bugs/bug1 --show-fixes
python main.py --project sample --json
```

## Evaluation

```bash
python run_eval.py
```

This prints the rank of the expected buggy function for each demo folder and reports Top-1 and MRR metrics.

## Why this matches the assignment

The project stays within a manageable scope but demonstrates the critical software-quality workflow expected by the assignment:

- defect localization from failing tests,
- evidence-based ranking,
- root-cause explanation,
- validation-oriented reporting,
- measurable evaluation using known buggy functions.
