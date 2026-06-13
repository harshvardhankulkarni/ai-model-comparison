"""
AI Model Comparison - Demo Project
Compares popular LLMs on benchmarks, cost, speed, and capabilities.
Data reflects publicly available benchmark scores as of 2025-2026.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

models = pd.DataFrame({
    'model': [
        'GPT-4o', 'GPT-4 Turbo', 'Claude 3.5 Sonnet', 'Claude 3 Opus',
        'Gemini 1.5 Pro', 'Gemini 1.5 Flash', 'Llama 3 70B', 'Llama 3 8B',
        'Mistral Large', 'Mixtral 8x7B'
    ],
    'provider': ['OpenAI', 'OpenAI', 'Anthropic', 'Anthropic',
                  'Google', 'Google', 'Meta', 'Meta',
                  'Mistral', 'Mistral'],
    'release_date': ['2024-05', '2023-11', '2024-06', '2024-03',
                     '2024-02', '2024-02', '2024-04', '2024-04',
                     '2024-02', '2023-12'],
    'mmlu': [88.7, 86.5, 89.0, 86.8, 85.9, 79.0, 82.0, 66.0, 84.0, 68.0],
    'human_eval': [90.2, 87.0, 92.0, 84.1, 84.0, 74.0, 80.0, 56.0, 82.0, 54.0],
    'gsm8k': [95.8, 92.0, 96.0, 95.0, 91.0, 86.0, 87.0, 72.0, 90.0, 70.0],
    'truthful_qa': [82.5, 80.0, 85.0, 83.0, 78.0, 72.0, 75.0, 55.0, 76.0, 60.0],
    'context_window': [128000, 128000, 200000, 200000, 1000000, 1000000, 8192, 8192, 32000, 32000],
    'cost_input_1k': [0.0050, 0.0100, 0.0030, 0.0150, 0.0035, 0.00035, 0.00065, 0.00006, 0.0020, 0.0002],
    'cost_output_1k': [0.0150, 0.0300, 0.0150, 0.0750, 0.0105, 0.00105, 0.00087, 0.00008, 0.0060, 0.0006],
    'speed_tokens_per_sec': [85, 60, 75, 40, 50, 120, 90, 140, 80, 110],
    'open_source': [False, False, False, False, False, False, True, True, True, True],
})

# Calculate composite score (weighted average of benchmarks)
weights = {'mmlu': 0.25, 'human_eval': 0.30, 'gsm8k': 0.25, 'truthful_qa': 0.20}
models['benchmark_score'] = (
    models['mmlu'] * weights['mmlu'] +
    models['human_eval'] * weights['human_eval'] +
    models['gsm8k'] * weights['gsm8k'] +
    models['truthful_qa'] * weights['truthful_qa']
).round(1)

# Categorize by tier
def assign_tier(score):
    if score >= 88:
        return 'Tier 1: Best in Class'
    elif score >= 80:
        return 'Tier 2: Strong Performer'
    elif score >= 70:
        return 'Tier 3: Solid Choice'
    else:
        return 'Tier 4: Entry Level'

models['tier'] = models['benchmark_score'].apply(assign_tier)

# Categorize best use case
def recommend_use_case(row):
    reasons = []
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
    return ' | '.join(reasons)

models['recommended_for'] = models.apply(recommend_use_case, axis=1)

# Visualization
fig, axes = plt.subplots(2, 2, figsize=(15, 11))
colors = {'OpenAI': '#74aa9c', 'Anthropic': '#d4a574', 'Google': '#8ab4f8',
          'Meta': '#8a9eb0', 'Mistral': '#c9957a'}
model_colors = [colors[p] for p in models['provider']]

# Plot 1: Benchmark scores grouped by provider
x = np.arange(len(models))
width = 0.2
metrics = ['mmlu', 'human_eval', 'gsm8k', 'truthful_qa']
for i, metric in enumerate(metrics):
    offsets = (i - 1.5) * width
    axes[0, 0].bar(x + offsets, models[metric], width, label=metric.replace('_', ' ').title())
axes[0, 0].set_xticks(x)
axes[0, 0].set_xticklabels(models['model'], rotation=45, ha='right', fontsize=8)
axes[0, 0].set_ylabel('Score (%)')
axes[0, 0].set_title('Benchmark Scores by Model')
axes[0, 0].legend(fontsize=8)
axes[0, 0].set_ylim(40, 100)
axes[0, 0].grid(True, alpha=0.3)

# Plot 2: Composite score
bars = axes[0, 1].barh(models['model'], models['benchmark_score'], color=model_colors)
axes[0, 1].set_xlabel('Composite Benchmark Score')
axes[0, 1].set_title('Overall Model Performance')
for bar, val in zip(bars, models['benchmark_score']):
    axes[0, 1].text(val + 0.5, bar.get_y() + bar.get_height()/2,
        f'{val}', va='center', fontsize=8)

# Plot 3: Cost vs Performance scatter
for provider in models['provider'].unique():
    subset = models[models['provider'] == provider]
    axes[1, 0].scatter(subset['cost_input_1k'] * 1000, subset['benchmark_score'],
        label=provider, s=100, alpha=0.7, color=colors[provider])
    for _, row in subset.iterrows():
        axes[1, 0].annotate(row['model'].split()[0],
            (row['cost_input_1k'] * 1000, row['benchmark_score']),
            fontsize=7, ha='center', va='bottom')
axes[1, 0].set_xlabel('Cost per 1K input tokens (cents)')
axes[1, 0].set_ylabel('Benchmark Score')
axes[1, 0].set_title('Cost vs Performance')
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3)

# Plot 4: Context window comparison
bars2 = axes[1, 1].bar(models['model'], models['context_window'] / 1000, color=model_colors)
axes[1, 1].set_xticklabels(models['model'], rotation=45, ha='right', fontsize=8)
axes[1, 1].set_ylabel('Context Window (K tokens)')
axes[1, 1].set_title('Context Window Size')
for bar, val in zip(bars2, models['context_window']):
    axes[1, 1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
        f'{val/1000:.0f}K', ha='center', fontsize=7)

plt.tight_layout()
plt.savefig('ai_model_comparison.png', dpi=150, bbox_inches='tight')
print('Saved: ai_model_comparison.png')

# Print results
print('\n--- AI MODEL COMPARISON (DEMO) ---')
print(f'Models analyzed: {len(models)}')
print(f'\nPerformance Tiers:')
for tier in ['Tier 1: Best in Class', 'Tier 2: Strong Performer', 'Tier 3: Solid Choice', 'Tier 4: Entry Level']:
    tier_models = models[models['tier'] == tier]
    if len(tier_models) > 0:
        names = ', '.join(tier_models['model'].tolist())
        print(f'  {tier}: {names}')

print(f'\nBest overall (composite): {models.loc[models["benchmark_score"].idxmax(), "model"]} ({models["benchmark_score"].max()})')
print(f'Best value (score/cost): {models.loc[(models["benchmark_score"] / (models["cost_input_1k"] * 1000)).idxmax(), "model"]}')
print(f'Longest context: {models.loc[models["context_window"].idxmax(), "model"]} ({models["context_window"].max():,} tokens)')
print(f'Fastest: {models.loc[models["speed_tokens_per_sec"].idxmax(), "model"]} ({models["speed_tokens_per_sec"].max()} tok/s)')

print('\n--- USE CASE RECOMMENDATIONS ---')
for _, row in models.iterrows():
    print(f'\n{row["model"]} ({row["provider"]}):')
    print(f'  Tier: {row["tier"]}')
    print(f'  Best for: {row["recommended_for"]}')
    print(f'  Open source: {row["open_source"]}')

models.to_csv('model_comparison_data.csv', index=False)
print('\nExported: model_comparison_data.csv')
print('Done.')
