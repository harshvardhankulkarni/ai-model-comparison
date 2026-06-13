# Runbook: AI Model Comparison

## When to Use This Runbook

- Running the model comparison for the first time.
- Adding new models or benchmarks.
- Generating a report for a technology decision.

## Prerequisites

- Python 3.8+ installed.
- pip installed.

## Procedure

### Step 1: Install Dependencies

```bash
pip install pandas numpy matplotlib
```

### Step 2: Run the Comparison

```bash
cd path/to/ai-model-comparison
python ai_model_comparison.py
```

### Step 3: Verify Output

Check for these files:

- `ai_model_comparison.png` - 4-panel comparison chart.
- `model_comparison_data.csv` - 10 rows with all scores, tiers, and recommendations.

### Step 4: Read the Rankings

The console output shows:

- Performance tiers (which models are best in class).
- Best overall model by composite score.
- Best value model (score per dollar).
- Longest context window.
- Fastest model.

### Step 5: Check Use Case Recommendations

Each model includes a `recommended_for` field. Use this to match models to your needs.

## Adding a New Model

### Step 1: Add Data

Add a new row to the `models` dictionary:

```python
{
    'model': 'Claude 3 Haiku',
    'provider': 'Anthropic',
    'release_date': '2024-03',
    'mmlu': 75.0,
    'human_eval': 73.0,
    'gsm8k': 83.0,
    'truthful_qa': 76.0,
    'context_window': 200000,
    'cost_input_1k': 0.00025,
    'cost_output_1k': 0.00125,
    'speed_tokens_per_sec': 120,
    'open_source': False,
}
```

### Step 2: Add Provider Color

Add the provider to the `colors` dictionary:

```python
colors = {'OpenAI': '#74aa9c', 'Anthropic': '#d4a574', ...}
```

### Step 3: Re-run

```bash
python ai_model_comparison.py
```

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| Missing model in output | Not in DataFrame | Check the model name is in the list |
| Wrong tier | Threshold changed | Reset `assign_tier()` to original values |
| Chart missing provider color | Provider not in colors dict | Add provider to `colors` dictionary |
| Negative cost values | Data entry error | Cost values must be positive |
| Recommendation empty | No rules matched | Add more conditions to `recommend_use_case()` |

## Customization

### Change Benchmark Weights

```python
weights = {
    'mmlu': 0.20,
    'human_eval': 0.35,  # Increased coding weight
    'gsm8k': 0.20,
    'truthful_qa': 0.25,  # Increased factuality weight
}
```

### Change Tier Thresholds

```python
def assign_tier(score):
    if score >= 85:      # Lowered from 88
        return 'Tier 1'
    elif score >= 75:    # Lowered from 80
        return 'Tier 2'
    ...
```

## Escalation

Open a GitHub issue with:

- Model scores and source URLs (when adding new models).
- Expected vs actual ranking.
- Python version.
