<!-- GSD -->
# Testing: AI Model Comparison

This is a demo / portfolio project. There are no automated tests.

## Manual Validation Checklist

### 1. CLI Recommender — Test Every Path

Run `python ai_model_comparison.py` and verify:

| Test Case | Input | Expected |
|-----------|-------|----------|
| Code generation, premium budget | [1], [3], n | Top 3 should include Claude 3.5 Sonnet, GPT-4o |
| Image generation, free budget | [3], [1], y | Should show Stable Diffusion 3.5, FLUX.1 |
| Balanced budget, open source required | any, [2], y | Only open-source models under $100/mo |
| All 8 use cases | each of [1]-[8] | Models scored by the corresponding capability column |
| Invalid input | 9, 0, abc | "Invalid. Pick 1-8." for use case; "Invalid. Pick 1-3." for budget |
| No matching models | extreme budget + open source | "No models match your criteria." |

### 2. Free Alternative Display

For each paid model recommendation, verify:
- Free alternative name is shown
- Savings % is correct (matches `free_alternatives` dict)
- Score gap is shown with sign
- Platform info for the free alternative is displayed

### 3. Static Analysis Output

Verify console prints:
- Best overall LLM (Claude 3.5 Sonnet expected)
- Best free LLM (Mistral Large or Llama 3 70B expected)
- All 4 performance tiers printed
- All paid-vs-free mappings printed (5 rows)

### 4. Chart Output

Check `ai_model_comparison.png` after each run:
- Panel 1: Grouped bar chart with all 6 capability dimensions per model
- Panel 2: Horizontal bar chart with composite scores, color-coded by provider
- Panel 3: Scatter plot with free models circled in green
- Panel 4: Text panel with CLI recommender message

### 5. CSV Export

Check `model_comparison_data.csv`:
- 11 rows (header + 10 models)
- 9 columns: model, type, open_source, coding, content, reasoning, analysis, multilingual, image_gen, cost_monthly, speed
- Values match the source `models` DataFrame

### 6. Interactive Chart

Run `python generate_interactive.py` and open `ai_model_comparison_interactive.html`:
- 4 panels render correctly
- Hover tooltips show cost and score values
- Bars have provider-consistent colors

### 7. Edge Cases

- Run twice without cleaning — verify CSV and PNG are overwritten
- Run with missing matplotlib — verify import error is clear
- Test `open_source` toggle with different budget tiers

## Known Limitations

- No unit or integration tests exist
- No CI pipeline
- Test coverage is manual only
