<!-- GSD -->
# Configuration: AI Model Comparison

All configuration is inline in the Python scripts. There are no external config files, environment variables, or CLI flags.

## `ai_model_comparison.py` — Inline Config Sections

### Model Definitions (lines 10-24)

`models` DataFrame — 10 rows, each with:
- `model`: Display name
- `type`: `'LLM'` or `'Image'` — determines which capability scores apply
- `open_source`: Boolean flag
- `coding`, `content`, `reasoning`, `analysis`, `multilingual`, `image_gen`: Capability scores (0-100)
- `cost_monthly`: Estimated monthly cost in USD
- `speed`: Relative speed score (higher = faster)

### Platform Info (lines 26-87)

`platforms` dictionary — each model maps to:
- `api`: API endpoint URL
- `web`: Web interface URL
- `free_tier`: Boolean — whether a free tier exists
- `self_host`: Boolean — whether self-hosting is possible

### Free Alternative Mappings (lines 89-95)

`free_alternatives` dictionary — maps paid model name to:
- `alt`: Free alternative model name
- `savings`: Cost savings percentage (0-100)
- `gap`: Capability score difference (negative = free model scores lower)

Current mappings:
| Paid Model | Free Alternative | Savings | Gap |
|------------|-----------------|---------|-----|
| GPT-4o | Llama 3 70B | 97% | -8.5 |
| Claude 3.5 Sonnet | Mistral Large | 47% | -7.5 |
| Gemini 1.5 Pro | Mistral Large | 33% | -1.7 |
| DALL-E 3 | Stable Diffusion 3.5 | 100% | -10.0 |
| Midjourney | FLUX.1 | 100% | -2.0 |

### Use Cases (lines 97-106)

`use_cases` dictionary — 8 entries mapping choice number to:
- `label`: Display text
- `key`: DataFrame column name used for scoring

### Budget Tiers (lines 108-112)

`budget_opts` dictionary — 3 tiers:
- `1`: Free / open source only (`max_cost: 1`)
- `2`: Balanced (`max_cost: 100`)
- `3`: Premium (`max_cost: 99999`)

### Chart Colors (lines 236-242)

- `colors`: Maps provider name to hex color (OpenAI, Anthropic, Google, Meta, Mistral, Stability AI, Black Forest Labs, Midjourney)
- `providers_map`: Maps model name to provider name

### Performance Tier Thresholds (line 220)

Hardcoded in `run_static_analysis()`:
```python
('Best in Class', 85, 100), ('Strong Performer', 78, 85),
('Solid Choice', 70, 78), ('Entry Level', 0, 70)
```

## `generate_interactive.py` — Inline Config

### Model Data (lines 6-16)

- `models`: 10 model names (different set: GPT-4 Turbo, Claude 3 Opus, Gemini Flash, Llama 3 8B, Mixtral 8x7B included)
- `providers`: Provider name per model
- `scores`: Composite benchmark scores
- `human`: Coding (HumanEval) scores
- `cost`: Cost per 1K tokens
- `open_src`: Open-source booleans

### Composite Score Weights (line 24-25)

```python
composite = round(m*0.25 + h*0.30 + g*0.25 + t*0.20, 1)
```
Where `m` = MMLU/scores, `h` = HumanEval, `g` = GSM8K, `t` = TruthfulQA. Values for `g` and `t` are hardcoded per model (lines 25).

### Speed Data (line 46)

`speed = [85, 60, 75, 40, 50, 120, 90, 140, 80, 110]` — tokens/sec indexed to match `models`.

## How to Change Configuration

All configuration changes require editing the Python source files directly:
1. Open `ai_model_comparison.py` or `generate_interactive.py`
2. Locate the relevant data structure (DataFrame, dictionary, or list)
3. Edit values and save
4. Re-run the script to apply changes

There are no config files, CLI arguments, or environment variable overrides.
