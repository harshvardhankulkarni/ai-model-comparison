<!-- GSD -->

# AI Model Comparison — Architecture

## Context and Goals

Compares 10 AI models across benchmarks, cost, speed, and context window. Features an interactive CLI recommender and paid-vs-free alternative mapping. Portfolio demo showcasing data analysis with structured comparison data.

## Data Flow

```
Model Definitions (10 models with scores, costs, platforms)
  → Interactive CLI (3 questions: task, budget, open-source preference)
  → Multi-factor scoring engine
  → Top 3 recommendations with paid/free alternatives
  → Static 4-panel benchmark visualization
  → Interactive Plotly HTML comparison chart
  → CSV export (model data, paid-vs-free mapping)
```

## Components

| File | Role |
|------|------|
| `ai_model_comparison.py` | Main script: model definitions, CLI interaction, scoring engine, recommendations, static chart |
| `generate_interactive.py` | Generates interactive Plotly HTML comparison |
| `ai_model_comparison.ipynb` | Jupyter notebook for exploratory analysis |
| `model_comparison_data.csv` | Full model data with scores and costs |
| `paid_vs_free_alternatives.csv` | Paid-to-free model mapping |
| `ai_model_comparison.png` | Static 4-panel benchmark comparison |
| `ai_model_comparison_interactive.html` | Interactive Plotly chart |

## Model Scope

| Category | Models |
|----------|--------|
| Flagship LLMs | GPT-4o, GPT-4 Turbo, Claude 3.5 Sonnet, Claude 3 Opus |
| Alternative LLMs | Gemini 1.5 Pro, Gemini 1.5 Flash, Llama 3 70B, Llama 3 8B, Mistral Large |
| Image Generation | DALL-E 3, Stable Diffusion, Midjourney, FLUX.1 |
| Compact | Claude 3 Haiku |

## Design Decisions

| Decision | Rationale |
|----------|-----------|
| CLI-based interaction | Simple, scriptable, no web UI needed for demo |
| 3-question input | Covers key decision factors without overwhelming users |
| Paid vs free mapping | Practical cost-saving recommendations |
| Static + interactive charts | Quick reference and detailed exploration |
| Subjective capability scores | Benchmark scores aggregated for simplified comparison |

## Trade-offs

- Model data becomes outdated as new versions release
- Capability scores are subjective aggregations
- Limited to 10 models — many alternatives not covered
- No real-time pricing (cost data is static)
- CLI only — no web or API interface for recommendations

## File Organization

```
ai-model-comparison/
├── ai_model_comparison.py
├── generate_interactive.py
├── ai_model_comparison.ipynb
├── ai_model_comparison.png
├── ai_model_comparison_interactive.html
├── model_comparison_data.csv
├── paid_vs_free_alternatives.csv
├── index.html
└── docs/
    ├── ARCHITECTURE.md
    ├── GETTING-STARTED.md
    ├── DEVELOPMENT.md
    ├── TESTING.md
    └── CONFIGURATION.md
```
