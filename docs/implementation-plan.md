# Implementation plan

## 1. Understand the input

Inspect the course JSON and note its top-level structure, fields, identifiers,
and links between people and pages. Keep the original file in `data/raw/`.

## 2. Clean the data

Write down the cleaning rules you intend to use. Implement them in
`clean_data.py`, add focused tests, and save results in `data/processed/`.

## 3. Recommend friends

Decide how to rank people who are not already friends. Implement and test that
rule in `recommend_friends.py` using the cleaned data.

## 4. Recommend pages

Decide how to rank pages a person does not already follow. Implement and test
that rule in `recommend_pages.py`.

## 5. Document your decisions

Record the actual input format, cleaning rules, recommendation rules, and how
to run your finished project in the main README as your work progresses.
