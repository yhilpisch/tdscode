<p align="right"><img src="https://hilpisch.com/tds_logo.png" alt="The Data Scientist" width="25%"></p>

# The Data Scientist &mdash; Companion Code Base

Welcome! This repository ships the runnable material that goes hand in hand with the primer and four modules of **The Data Scientist (TDS)**.

Each directory mirrors the structure of the books so you can jump from a chapter or lab into the matching notebook or script without hunting for files.

---

## Repository Layout

The folder structure mirrors the program arc: primer &rarr; Modules&nbsp;1&ndash;4.

```text
0_primer/
  code/       # primer scripts and helpers
  data/       # primer data files when a notebook needs them
  notebooks/  # primer notebooks (Colab‑friendly)
1_data/ ... 4_data/
  code/       # module‑specific helpers and lab scripts
  data/       # book-local datasets and project inputs
  notebooks/  # notebooks aligned with book chapters and labs
tools/
  validate_*.py
README.md     # Learner‑facing overview (this document)
```

### Notebooks (`*/notebooks/`)

These are your guided workbooks. Each one pairs with a chapter or lab so you can move from reading to running code without guessing what to open.

- Designed to run top‑to‑bottom in Google Colab or a local Jupyter environment.
- Use standard Python + data‑science packages (NumPy, pandas, matplotlib, etc.).
- Echo the callouts and exercises from the books and labs.

### Python Scripts (`*/code/`)

Short, composable helpers live here. They back the labs and show the same workflows you rehearse in the notebooks.

- Small, focused utilities (cleaning helpers, plotting scaffolds, baseline model scripts, project scaffolds, dashboard snippets).
- Organised by module so you can map code back to the relevant book and lab quickly.

---

## Working in Google Colab

Colab is the fastest way to get started &mdash; no local setup, just a browser.

### Option 1: Open a Notebook Directly

1. Navigate to the notebook in GitHub (for example `1_data/notebooks/01_core_types.ipynb`).
2. Replace `github.com` in the URL with `colab.research.google.com/github`.
3. Run the notebook from top to bottom; install cells are provided where extra packages are needed.

### Option 2: Clone the Repo in Colab

```python
from pathlib import Path
import subprocess, sys

repo_url = "https://github.com/REPLACE_ME/tdscode.git"
target = Path("/content/tds")

if not target.exists():
    subprocess.run(["git", "clone", repo_url, str(target)], check=True)

sys.path.append(str(target))
print("Repo ready at", target)
```

Once cloned:

- Open any notebook under `/content/tds/0_primer/notebooks` or `/content/tds/1_data/notebooks`, etc.
- Load the datasets under `/content/tds/.../data` and run the scripts under `/content/tds/.../code` as needed (`!python 1_data/code/clean_orders.py`).

---

## Running Locally

Prefer your own machine? This path gives you full control.

```bash
git clone https://github.com/REPLACE_ME/tdscode.git
cd tdscode
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt  # or install base packages manually
```

Then:

- Launch Jupyter (`jupyter lab` or `jupyter notebook`).
- Open the notebook matching your current module and chapter.
- Use the `code/` helpers wherever the books or labs reference a script.

---

## Validation Tools

The companion repo can also include simple quality checks:

- `tools/validate_code.py` &mdash; basic checks for import/compile errors in `*/code/`.
- `tools/validate_notebooks.py` &mdash; smoke tests for notebooks under `*/notebooks/`.

Check `tools/validate_*.py` docstrings for usage examples.

---

Treat this repo as the living lab companion for **The Data Scientist**: when the books and labs evolve, these notebooks and scripts are updated in lockstep. Pull regularly (or re‑clone in Colab) to stay aligned with the latest version of the program.

---

## Disclaimer

This repository and all associated code, notebooks, and documents are provided for instructional and illustrative purposes only.

- The material is not investment, tax, or legal advice, and it is not a substitute for professional judgement in production systems.
- The examples are simplified and may omit checks, safeguards, or hardening steps that would be required in real‑world deployments.
- No warranty of any kind is given, express or implied; use the code at your own risk and always review it before integrating it into your own projects.
- Do not commit secrets (API keys, passwords, tokens) to this repository or to any fork derived from it.

<p align="right"><img src="https://hilpisch.com/tds_logo.png" alt="The Data Scientist" width="25%"></p>
