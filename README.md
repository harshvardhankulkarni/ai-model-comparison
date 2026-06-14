<!-- GSD -->
# AI Model Comparison — Demo Project

Compare 10 AI models (LLMs + image generators) across benchmark scores, monthly cost, speed, and capability dimensions. Features an interactive CLI recommender that asks your use case, budget, and open-source preference — then recommends top 3 models with paid/free alternatives and platform access info.

**GitHub Pages:** https://harshvardhankulkarni.github.io/ai-model-comparison/

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.8+ | Runtime |
| Pandas 2.0+ | Data structuring and ranking |
| NumPy 1.24+ | Numerical operations |
| Matplotlib 3.7+ | Static multi-panel charts |
| Plotly | Interactive HTML charts |

## Quick Start

```bash
git clone https://github.com/harshvardhankulkarni/ai-model-comparison.git
cd ai-model-comparison
pip install pandas numpy matplotlib plotly
python ai_model_comparison.py
```

The CLI asks 3 questions — answer them and get ranked recommendations with platform info. A static 4-panel chart and CSV export are generated automatically.

## Interactive Chart

```bash
python generate_interactive.py
```

Produces `ai_model_comparison_interactive.html` — an interactive Plotly dashboard with benchmark scores, composite scores, cost-vs-performance scatter, and speed comparison.

## Project Structure

```
ai-model-comparison/
  ai_model_comparison.py          Main script: CLI recommender + static analysis + chart
  generate_interactive.py         Plotly interactive HTML chart generator
  ai_model_comparison.ipynb       Jupyter Notebook
  model_comparison_data.csv       Model data with scores and costs
  paid_vs_free_alternatives.csv   Paid-to-free mapping
  ai_model_comparison.png         Static 4-panel chart
  ai_model_comparison_interactive.html  Interactive Plotly chart
  index.html                      GitHub Pages landing page
  README.md                       This file
  docs/
    ARCHITECTURE.md               Design and methodology
    GETTING-STARTED.md            First run guide
    DEVELOPMENT.md                Extending the project
    TESTING.md                    Manual validation
    CONFIGURATION.md              Inline config reference
    runbook.md                    Operations guide
```

## Features

- **Interactive CLI Recommender** — 8 use cases, 3 budget tiers, open-source toggle; weighted recommendation engine
- **Paid vs Free Alternatives** — Every paid model maps to a free alternative with savings % and capability gap
- **Static 4-Panel Chart** — Capability scores, overall capability, cost vs capability scatter
- **Interactive Plotly Chart** — Benchmark scores, composite scores, cost vs performance, speed comparison
- **CSV Export** — `model_comparison_data.csv` for external use

## Demo / Portfolio Note

This is a demo and portfolio project. Model scores are estimates based on public benchmarks as of 2024-2025. The tool is not production-grade — it does not pull live benchmark data. See `docs/ARCHITECTURE.md` for design decisions and trade-offs.
