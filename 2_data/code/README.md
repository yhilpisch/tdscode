# Module 2 Code Assets

The Data Scientist — Book 2 · Python Data Analysis, Visualization, and Storytelling  
(c) Dr. Yves J. Hilpisch  
AI-Powered by GPT 5.x

These scripts mirror the book chapters and the companion notebooks. The
Titanic material uses the aggregated `Class`/`Sex`/`Age`/`Survived`/`Freq`
table shipped in `data/Titanic.csv`, so the cleaning and plotting helpers treat
`Freq` as a weight.

## Chapter coverage

- `numpy_vectorization.py` — NumPy arrays, vectorization, and loop comparison.
- `clean_orders.py` — cleaning and preparing the small orders dataset.
- `eda_plot.py` — exploratory plotting helper for a numeric column.
- `titanic_clean.py` — cleans the aggregated Titanic table and saves
  `data/titanic_clean.csv`.
- `titanic_eda.py` — plots weighted survival-rate bar charts from the cleaned
  Titanic table.
- `generate_figures.py` — figure helper used by the book build.
- `sql_demo.py` — small SQLite setup for SQL and pandas side-by-side examples.

## Run from the book root

```bash
python code/numpy_vectorization.py
python code/clean_orders.py
python code/eda_plot.py
python code/titanic_clean.py
python code/titanic_eda.py
python code/sql_demo.py
```

Outputs stay in `figures/`, `data/`, or console as appropriate.
