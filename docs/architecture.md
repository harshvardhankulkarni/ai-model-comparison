# Architecture: AI Model Comparison

## Context

The AI model landscape changes rapidly. Developers and businesses need a structured way to compare models across benchmarks, cost, and capabilities to make informed decisions.

## Goals

- Compare 10 major LLMs across 4 standardized benchmarks.
- Rank models by a weighted composite score.
- Categorize models into performance tiers.
- Generate use case recommendations for each model.
- Visualize comparisons across multiple dimensions.

## Design

### Data Flow

```
Model DataFrame (10 rows x 14 columns)
  - Identity: model name, provider, release date
  - Benchmarks: MMLU, HumanEval, GSM8K, TruthfulQA
  - Performance: context window, speed
  - Cost: input/output per 1K tokens
  - Metadata: open source flag
        |
        v
Score Calculation
  - Weighted composite = MMLU*0.25 + HumanEval*0.30 + GSM8K*0.25 + TruthfulQA*0.20
        |
        +---> Tier Assignment (4 tiers by score)
        +---> Use Case Recommendation (rule-based)
        |
        v
Visualization (2x2 grid) + CSV Export
```

### Scoring Model

```python
weights = {
    'mmlu': 0.25,        # General knowledge
    'human_eval': 0.30,  # Coding (highest weight)
    'gsm8k': 0.25,       # Math reasoning
    'truthful_qa': 0.20  # Factuality
}
```

Coding is weighted highest because it is the most common practical use case.

### Recommendation Logic

```python
if row['context_window'] >= 100000:
    reasons.append('Long document analysis')
if row['human_eval'] >= 85:
    reasons.append('Complex coding tasks')
if row['cost_input_1k'] <= 0.001:
    reasons.append('High volume, cost sensitive')
if row['open_source']:
    reasons.append('Self hosted, data privacy')
if row['benchmark_score'] >= 88:
    reasons.append('General purpose, maximum accuracy')
```

### Visualization Layout

```
Panel 1: Grouped bar chart - All benchmarks by model (color by provider)
Panel 2: Horizontal bar - Composite score ranking
Panel 3: Scatter plot - Cost vs performance
Panel 4: Bar chart - Context window comparison
```

## Key Decisions

| Decision | Rationale |
|----------|-----------|
| 4 benchmarks only | Covers knowledge, coding, math, and truthfulness. More benchmarks add noise. |
| Weighted composite instead of average | Coding is the highest value use case for most users. |
| Rule-based recommendations | Transparent and explainable. No black-box ML needed. |
| Cost as a separate dimension | Critical for practical decision making. A perfect model is useless if it is too expensive. |

## Trade-offs

- **Static data**: Benchmark scores change as models get updated. The data is a snapshot. A production system would pull from an API.
- **4 benchmarks vs 50+**: MMLU alone has 57 subjects. Adding more benchmarks (HellaSwag, ARC, WinoGrande) would give a more complete picture but reduce readability.
- **Cost vs quality**: The composite score does not include cost. We show cost separately. Some users care more about value (cost-adjusted score).

## Integration Points

- **Input**: Hardcoded DataFrame. Replace with API data from OpenRouter, Artificial Analysis, or Evalplus.
- **Output**: `model_comparison_data.csv` for reports or dashboards.
- **Extending**: Add more models by appending rows. Add more benchmarks by adding columns.

## Dependencies

- Python 3.8+
- pandas, numpy, matplotlib
