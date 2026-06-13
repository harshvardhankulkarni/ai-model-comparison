# AI Model Comparison - Demo Project

Compare 10 popular large language models across benchmarks, cost, speed, and context window. Provides use case recommendations for each model.

Data reflects publicly available benchmark scores as of 2024-2025.

## Tech Stack

- Python 3.8+
- Pandas 2.0+ - Data structuring and ranking
- NumPy 1.24+ - Numerical operations
- Matplotlib 3.7+ - Multi-panel visualizations

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

```bash
git clone https://github.com/harshvardhankulkarni/ai-model-comparison.git
cd ai-model-comparison
pip install pandas numpy matplotlib
```

### Running

```bash
python ai_model_comparison.py
```

Expected output:

```
--- AI MODEL COMPARISON (DEMO) ---
Models analyzed: 10
Best overall (composite): Claude 3.5 Sonnet (90.8)
Best value (score/cost): Llama 3 8B
Longest context: Gemini 1.5 Pro (1,000,000 tokens)
...
Exported: model_comparison_data.csv
Done.
```

### Output Files

| File | Description |
|------|-------------|
| ai_model_comparison.png | 4-panel comparison chart |
| model_comparison_data.csv | All models with scores, costs, and recommendations |

## Models Compared

| Model | Provider | Size | Open Source | Release |
|-------|----------|------|-------------|---------|
| GPT-4o | OpenAI | Unknown | No | May 2024 |
| GPT-4 Turbo | OpenAI | Unknown | No | Nov 2023 |
| Claude 3.5 Sonnet | Anthropic | Unknown | No | Jun 2024 |
| Claude 3 Opus | Anthropic | Unknown | No | Mar 2024 |
| Gemini 1.5 Pro | Google | Unknown | No | Feb 2024 |
| Gemini 1.5 Flash | Google | Unknown | No | Feb 2024 |
| Llama 3 70B | Meta | 70B | Yes | Apr 2024 |
| Llama 3 8B | Meta | 8B | Yes | Apr 2024 |
| Mistral Large | Mistral | Unknown | Yes | Feb 2024 |
| Mixtral 8x7B | Mistral | 47B | Yes | Dec 2023 |

## Benchmarks

| Metric | What it measures | Weight |
|--------|-----------------|--------|
| MMLU | Multitask language understanding (57 subjects) | 25% |
| HumanEval | Python code generation accuracy | 30% |
| GSM8K | Grade school math problem solving | 25% |
| TruthfulQA | Factuality and truthfulness | 20% |

## How It Works

1. Model data is defined as a DataFrame with benchmark scores, cost, speed, and context window.
2. A composite benchmark score is calculated using weighted averages.
3. Models are grouped into performance tiers based on composite scores.
4. Use case recommendations are generated based on model strengths.
5. Four visualizations compare models across dimensions.

## Results Summary

- **Best overall**: Claude 3.5 Sonnet (90.8 composite).
- **Best value**: Llama 3 8B (near-zero cost, 56% of top performance).
- **Longest context**: Gemini 1.5 Pro (1M tokens).
- **Fastest**: Llama 3 8B (140 tok/s).
- **Best for coding**: Claude 3.5 Sonnet (HumanEval 92.0%).

## Project Structure

```
ai-model-comparison/
  ai_model_comparison.py   Main comparison script
  README.md                This file
  docs/
    architecture.md         Design and methodology
    runbook.md              Operations guide
```

## Configuration

Edit these sections in the script:

- `weights` dictionary - Change benchmark importance.
- `assign_tier()` thresholds - Adjust performance tier boundaries.
- `recommend_use_case()` logic - Add or change recommendation rules.

## License

MIT
