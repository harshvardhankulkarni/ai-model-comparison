<!-- GSD -->
# Development: AI Model Comparison

## Project Structure

```
ai-model-comparison/
  ai_model_comparison.py       Main CLI — edit this for most changes
  generate_interactive.py      Plotly chart — independent of main script
  ai_model_comparison.ipynb    Jupyter notebook
  model_comparison_data.csv    CSV output (regenerated on each run)
  paid_vs_free_alternatives.csv  Extended alternative mappings
  ai_model_comparison.png      Chart output
  ai_model_comparison_interactive.html  Interactive output
  index.html                   GitHub Pages site
  docs/                        Documentation
```

## How to Add a New Model

### In `ai_model_comparison.py`

1. **Add model data** — Insert a row in the `models` DataFrame (line 10-24):
   ```python
   'NewModel': {
       'type': 'LLM',                    # 'LLM' or 'Image'
       'open_source': True,              # or False
       'coding': 85,                     # 0-100 capability scores
       'content': 80,
       'reasoning': 82,
       'analysis': 78,
       'multilingual': 75,
       'image_gen': 0,                   # 0 for LLMs
       'cost_monthly': 40,               # estimated $/mo
       'speed': 95,                      # relative speed score
   }
   ```

2. **Add platform info** — Insert entry in `platforms` dictionary (line 26-87):
   ```python
   'NewModel': {
       'api': 'Provider API (url)',
       'web': 'Web interface (url)',
       'free_tier': False,
       'self_host': False,
   }
   ```

3. **Add provider color** — Add entry in the `colors` dictionary (line 236) and `providers_map` (line 239) for chart color coding.

4. **Add free alternative mapping** — If the model is paid and has a free alternative, add to `free_alternatives` dict (line 89-95):
   ```python
   'NewModel': {'alt': 'FreeModel', 'savings': 80, 'gap': -12.0}
   ```

### In `generate_interactive.py`

The interactive script has its own model list (line 6-13). Add a new entry to `models`, `providers`, `scores`, `human`, `cost`, and `open_src` arrays.

## How to Modify Scoring Criteria

### Recommendation score formula (main script)

In `recommend()` (line 126):
```python
filtered['score'] = primary_score + filtered['reasoning'] * 0.3 + filtered['speed'] / 200
```

Adjust the weights or add new components:
```python
filtered['score'] = primary_score * 1.0 + filtered['reasoning'] * 0.2 + filtered['speed'] / 150 + filtered['cost_monthly'] * -0.02
```

### LLM benchmark formula (static analysis)

In `run_static_analysis()` (line 208-211):
```python
llm_only['benchmark'] = (
    llm_only['coding'] * 0.25 + llm_only['reasoning'] * 0.30 +
    llm_only['content'] * 0.25 + llm_only['multilingual'] * 0.20
)
```

### Composite score formula (chart)

In `run_static_analysis()` (line 259-261):
```python
base_scores = (models['coding'] * 0.2 + models['content'] * 0.2 +
               models['reasoning'] * 0.2 + models['analysis'] * 0.2 +
               models['multilingual'] * 0.1 + models['image_gen'] * 0.1)
```

## How to Update Paid-vs-Free Mappings

Edit the `free_alternatives` dictionary in `ai_model_comparison.py` (line 89-95). Each entry requires:
- `alt`: name of the free alternative model (must exist in the `models` DataFrame)
- `savings`: percentage cost saved (0-100)
- `gap`: capability score difference (negative means the free model scores lower)

Also update `paid_vs_free_alternatives.csv` for the extended dataset with trade-off descriptions.

## How to Modify Performance Tier Thresholds

In `run_static_analysis()` (line 220-224):
```python
for tier_name, lo, hi in [('Best in Class', 85, 100), ('Strong Performer', 78, 85),
                           ('Solid Choice', 70, 78), ('Entry Level', 0, 70)]:
```

Adjust `lo` and `hi` values for each tier.

## How to Add a New Use Case

In `use_cases` dictionary (line 97-106), add a new entry:
```python
'9': {'label': 'Your new use case', 'key': 'coding'},
```

The key must match a column name in the `models` DataFrame (one of: `coding`, `content`, `image_gen`, `analysis`, `reasoning`, `multilingual`).
