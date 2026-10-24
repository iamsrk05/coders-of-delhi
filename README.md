# Coders of Delhi

A pure-Python learning project for cleaning JSON data and recommending friends
and pages. This repository is a scaffold: the project logic, tests, and data
are for you to add as you work through the course.

## Project layout

```text
coders-of-delhi/
├── data/
│   ├── raw/              Original JSON input; keep it unchanged
│   └── processed/        Cleaned output generated later
├── docs/
│   └── implementation-plan.md
├── src/
│   └── coders_of_delhi/
│       ├── __init__.py
│       ├── clean_data.py
│       ├── recommend_friends.py
│       └── recommend_pages.py
├── tests/
│   └── README.md
├── .gitignore
└── pyproject.toml
```

The three source files match the three project tasks. `data/raw` is for the
original course JSON files. `data/processed` is for output you generate while
cleaning. `tests` is for checks you write as each task is completed. The plan
in `docs` gives a suggested order without supplying solutions.

## Getting started

1. Put the course's original JSON file or files in `data/raw/`.
2. Inspect their keys and record the actual data format in your own notes.
3. Start with `src/coders_of_delhi/clean_data.py`. Decide what counts as
   invalid, duplicate, or incomplete data before writing cleaning code.
4. Add small tests for those rules, then work on friend recommendations and
   page recommendations in that order.

Use Python 3.8 or newer. The project uses the Python standard library for its
runtime code. When you are ready to write tests, install the optional test
dependency from this folder with `python -m pip install -e ".[dev]"`, then run
`python -m pytest`. No tests are present in the scaffold yet.

## GitHub use

This project has its own Git repository, separate from the Python learning
workspace. Its initial commit contains the scaffold only; implementation and
course data can be added in later commits.
