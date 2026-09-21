# AI Projects

> A hands-on collection of agentic AI roadmap projects and focused Python experiments.

This repository is a learning workspace for building practical AI software from the ground up. It will grow from Python fundamentals and data-handling utilities into increasingly capable AI applications—covering prompts, LLM workflows, tools, retrieval, memory, evaluation, and autonomous agents.

Each project lives in its own folder with its own README, setup instructions, and dependencies, so projects can be explored independently.

## What you'll find here

| Area | Focus |
| --- | --- |
| **Agentic AI roadmap** | Step-by-step projects that develop the building blocks of reliable AI agents. |
| **Python side projects** | Small, practical exercises for strengthening programming, data, and software-design skills. |
| **Experiments & learning notes** | Focused prototypes used to understand a concept before applying it in a larger project. |

## Projects

| Project | Type | Description | Status |
| --- | --- | --- | --- |
| [Prompt Stats](./prompt_stats/) | Python / data analysis | Validates a CSV of AI prompts and reports prompt usage by category, model, and length. | Complete |
| More roadmap projects | Agentic AI | New projects will be added as the roadmap progresses. | Coming soon |

## Learning path

The agentic-AI work in this repository is intended to build progressively:

1. **Python foundations** — clean code, file handling, testing, data structures, and APIs.
2. **LLM applications** — prompting, structured outputs, and model integrations.
3. **Tool-using agents** — agents that can choose and call useful functions or services.
4. **Knowledge-aware systems** — retrieval, embeddings, vector search, and grounded responses.
5. **Reliable agent systems** — planning, memory, evaluation, guardrails, and observability.
6. **End-to-end projects** — complete applications that bring these ideas together.

## Repository layout

```text
AI-PROJECTS/
├── prompt_stats/            # Prompt CSV validation and analytics
│   ├── data/                # Project input data
│   ├── prompt_stats/        # Application package
│   ├── tests/               # Automated tests
│   └── README.md            # Project-specific guide
├── <future-project>/        # One self-contained project per folder
└── README.md                # You are here
```

## Getting started

1. Clone this repository.
2. Choose a project folder from the table above.
3. Follow that project's README for its environment, dependencies, and run command.

For example, to run the current project:

```bash
cd prompt_stats
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
python main.py
```

## Project standards

As new projects are added, each one should aim to include:

- a short README explaining the problem, approach, and how to run it;
- a `requirements.txt` or equivalent dependency definition;
- an `.env.example` when environment variables are required—never commit real secrets;
- tests where they provide useful confidence;
- clear, focused commits and a self-contained project folder.

## Tech stack

The core language is **Python**. Individual roadmap projects may introduce libraries and services as they become useful, such as LLM APIs, agent frameworks, vector databases, web tools, and evaluation tooling. Each project README will document its exact stack.

## Why this repository exists

The goal is not only to make demos, but to understand how AI systems work in practice: how they use data and tools, where they fail, and how to make them more useful, testable, and dependable.

---

New projects and improvements are added as the learning journey continues.
