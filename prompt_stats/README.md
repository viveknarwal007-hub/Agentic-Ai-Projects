# prompt_stats

A beginner Python project that reads a CSV file of AI prompts, validates the data, analyzes usage patterns, and prints a clean report.

Built to practise core Python concepts — no external libraries, just pure Python.

---

## What it does

```
prompts.csv
     |
     v
  loader.py     →  reads the CSV file safely
     |
     v
 validator.py   →  finds missing fields and duplicate prompts
     |
     v
  analyzer.py   →  counts prompts by category, model, and average word length
     |
     v
  reporter.py   →  prints a clean summary report
     |
     v
   main.py      →  wires everything together
```

### Sample output

```
------VALIDATION REPORT------
Total Issues Found: 2
Missing Fields:
  - Entry ID 41: prompt is empty.
  - Entry ID 42: model is empty.
Duplicate Prompts:

------ANALYSIS REPORT------
average prompt length: 5.47 words
Prompt Count by Category:
-coding: 11
-machine_learning: 7
-education: 4
...
Prompt Count by Model:
-gpt-5: 16
-gemini: 14
-claude: 12
```

---

## Project structure

```
prompt_stats/
│
├── data/
│   └── prompts.csv          ← input dataset (id, prompt, category, model)
│
├── prompt_stats/            ← the Python package
│   ├── __init__.py
│   ├── models.py            ← PromptEntry class
│   ├── loader.py            ← load_csv()
│   ├── validator.py         ← validate(), find_missing_fields(), find_duplicates()
│   ├── analyzer.py          ← analyze(), count_by_category(), average_word_count()
│   └── reporter.py          ← print_validation_report(), print_analysis_report()
│
├── tests/
│   ├── test_loader.py       ← 4 tests
│   ├── test_validator.py    ← 4 tests
│   └── test_analyzer.py     ← 5 tests
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Getting started

### 1. Clone the repo

```bash
git clone https://github.com/viveknarwal007-hub/Agentic-Ai-Projects.git
cd prompt_stats
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the project

```bash
python main.py
```

### 5. Run the tests

```bash
pytest tests/ -v
```

---

## Python concepts practised

| Concept | Where |
|---------|-------|
| Functions, parameters, return values | Every module |
| Modules & packages | `__init__.py`, all imports |
| File I/O + context manager (`with open`) | `loader.py` |
| CSV handling (`csv.DictReader`) | `loader.py` |
| Exceptions (`FileNotFoundError`, `ValueError`) | `loader.py`, `validator.py` |
| Type hints | Every function signature |
| OOP — class with `__init__` and `__repr__` | `models.py` |
| List & dict comprehensions | `analyzer.py`, `validator.py`, `main.py` |
| Set comprehensions | `main.py` |
| `pytest` unit tests | `tests/` |
| Virtual environment + pip + `requirements.txt` | Project setup |
| Relative imports | `__init__.py` |

---

## Data format

The input CSV (`data/prompts.csv`) expects these columns:

| Column | Type | Description |
|--------|------|-------------|
| `id` | int | Unique row identifier |
| `prompt` | str | The AI prompt text |
| `category` | str | Topic category (e.g. `coding`, `education`) |
| `model` | str | AI model used (e.g. `gemini`, `gpt-5`, `claude`) |

The validator flags rows where `prompt` or `model` is empty, and detects duplicate prompt text.

---

## Requirements

- Python 3.8+
- `pytest` (for running tests only)

No other external libraries required.

