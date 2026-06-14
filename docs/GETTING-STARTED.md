<!-- GSD -->
# Getting Started: AI Model Comparison

## Prerequisites

- Python 3.8 or higher
- pip package manager

## Installation

```bash
git clone https://github.com/harshvardhankulkarni/ai-model-comparison.git
cd ai-model-comparison
pip install pandas numpy matplotlib
```

For the interactive Plotly chart:

```bash
pip install plotly
```

## First Run

```bash
python ai_model_comparison.py
```

The CLI prompts you through 3 questions:

1. **What do you want to do?** — Pick from 8 use cases:
   - `[1]` Code generation
   - `[2]` Content creation
   - `[3]` Image generation
   - `[4]` Data analysis & reporting
   - `[5]` Document analysis & summarization
   - `[6]` Math & reasoning tasks
   - `[7]` Translation & multilingual
   - `[8]` General Q&A / chatbot

2. **Budget preference?** — Pick from 3 tiers:
   - `[1]` Free / open source only (max cost: $1/mo)
   - `[2]` Balanced (max cost: $100/mo)
   - `[3]` Premium (unlimited)

3. **Need open source / self-hostable?** — `y` or `n`

## Expected Output

After answering, the CLI shows:

- **Top 3 recommendations** — Each with model name, type, score, monthly cost, platform info (API, web, free tier, self-hostable)
- **Free alternative** — For paid recommendations, shows the best free replacement with savings % and capability gap
- **All models ranked** — Complete ranked list with scores and costs
- **Static benchmark comparison** — Best overall LLM, best free LLM, performance tiers, and paid-vs-free table
- **Chart saved** — `ai_model_comparison.png` (4-panel matplotlib figure)
- **CSV exported** — `model_comparison_data.csv`

## Interactive Chart Version

```bash
python generate_interactive.py
```

Produces `ai_model_comparison_interactive.html`. Open in any browser for an interactive Plotly dashboard with 4 panels: benchmark scores, composite score, cost vs performance, speed comparison.

## Expected Outputs

| File | Description |
|------|-------------|
| `ai_model_comparison.png` | Static 4-panel chart (capability scores, overall capability, cost vs capability, recommender note) |
| `model_comparison_data.csv` | All 10 models with capability scores, cost, speed, and open-source flag |
| `ai_model_comparison_interactive.html` | Interactive Plotly chart (from `generate_interactive.py`) |
