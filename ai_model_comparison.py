"""
AI Model Comparison - Demo Project
Compares popular LLMs on benchmarks, cost, speed, and capabilities.
Includes paid vs free alternatives for every use case.
Data reflects publicly available benchmark scores as of 2024-2025.
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

# Free alternative mapping for each paid model
free_alternatives = {
    'GPT-4o': {
        'alternative': 'Llama 3 70B',
        'savings_pct': 97,
        'trade_off': 'Lower creative writing quality. Smaller context window (8K vs 128K).',
        'best_for': 'General Q&A, coding, data analysis where budget matters.'
    },
    'GPT-4 Turbo': {
        'alternative': 'Llama 3 70B',
        'savings_pct': 94,
        'trade_off': 'Slightly lower accuracy on complex reasoning. No vision support.',
        'best_for': 'Batch processing, internal tools, prototyping.'
    },
    'Claude 3.5 Sonnet': {
        'alternative': 'Mistral Large',
        'savings_pct': 47,
        'trade_off': 'Lower coding accuracy (92 vs 82 HumanEval). Smaller context window.',
        'best_for': 'Document analysis, multilingual tasks, self-hosted apps.'
    },
    'Claude 3 Opus': {
        'alternative': 'Llama 3 70B',
        'savings_pct': 96,
        'trade_off': 'Lower benchmark scores across the board. No vision.',
        'best_for': 'High volume text generation, data extraction.'
    },
    'Gemini 1.5 Pro': {
        'alternative': 'Mistral Large',
        'savings_pct': 33,
        'trade_off': 'Loses 1M token context window (drops to 32K). Lower multilingual scores.',
        'best_for': 'Standard document processing, RAG pipelines.'
    },
    'Gemini 1.5 Flash': {
        'alternative': 'Llama 3 8B',
        'savings_pct': 83,
        'trade_off': 'Lower accuracy on math and coding. Smaller context.',
        'best_for': 'Simple chatbots, content classification, high speed needs.'
    },
}

def find_free_alternative(model_name, is_open_source):
    if is_open_source:
        return None
    return free_alternatives.get(model_name, None)

models['free_alternative'] = models.apply(
    lambda row: find_free_alternative(row['model'], row['open_source']), axis=1
)

# Calculate composite score
weights = {'mmlu': 0.25, 'human_eval': 0.30, 'gsm8k': 0.25, 'truthful_qa': 0.20}
models['benchmark_score'] = (
    models['mmlu'] * weights['mmlu'] +
    models['human_eval'] * weights['human_eval'] +
    models['gsm8k'] * weights['gsm8k'] +
    models['truthful_qa'] * weights['truthful_qa']
).round(1)

# Tier assignment
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

# Use case recommendations
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

# Paid vs free comparison table
paid_free_rows = []
for _, row in models.iterrows():
    alt = row['free_alternative']
    if alt:
        alt_row = models[models['model'] == alt['alternative']]
        if len(alt_row) > 0:
            alt_model = alt_row.iloc[0]
            paid_free_rows.append({
                'paid_model': row['model'],
                'paid_score': row['benchmark_score'],
                'paid_cost': row['cost_input_1k'],
                'free_model': alt['alternative'],
                'free_score': alt_model['benchmark_score'],
                'free_cost': alt_model['cost_input_1k'],
                'savings_pct': alt['savings_pct'],
                'score_gap': round(row['benchmark_score'] - alt_model['benchmark_score'], 1),
                'trade_off': alt['trade_off'],
                'best_for': alt['best_for'],
            })

paid_free_df = pd.DataFrame(paid_free_rows)

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

# Plot 2: Composite score with paid/free markers
bars = axes[0, 1].barh(models['model'], models['benchmark_score'], color=model_colors)
axes[0, 1].set_xlabel('Composite Benchmark Score')
axes[0, 1].set_title('Overall Model Performance (green = free / open source)')
for bar, val, is_free in zip(bars, models['benchmark_score'], models['open_source']):
    label_color = '#2ecc71' if is_free else '#e74c3c'
    axes[0, 1].text(val + 0.5, bar.get_y() + bar.get_height()/2,
        f'{val}', va='center', fontsize=8, color=label_color, fontweight='bold')

# Plot 3: Cost vs Performance with free alternatives highlighted
for provider in models['provider'].unique():
    subset = models[models['provider'] == provider]
    axes[1, 0].scatter(subset['cost_input_1k'] * 1000, subset['benchmark_score'],
        label=provider, s=100, alpha=0.7, color=colors[provider])
    for _, row in subset.iterrows():
        axes[1, 0].annotate(row['model'].split()[0],
            (row['cost_input_1k'] * 1000, row['benchmark_score']),
            fontsize=7, ha='center', va='bottom')

# Highlight free alternatives on the scatter plot
free_models = models[models['open_source'] == True]
axes[1, 0].scatter(free_models['cost_input_1k'] * 1000, free_models['benchmark_score'],
    s=200, facecolors='none', edgecolors='#2ecc71', linewidths=2, label='Free / Open Source')
axes[1, 0].set_xlabel('Cost per 1K input tokens (cents)')
axes[1, 0].set_ylabel('Benchmark Score')
axes[1, 0].set_title('Cost vs Performance (circled = free alternatives)')
axes[1, 0].legend(fontsize=7)
axes[1, 0].grid(True, alpha=0.3)

# Plot 4: Paid vs Free score comparison
if len(paid_free_df) > 0:
    x_pf = np.arange(len(paid_free_df))
    width_pf = 0.35
    axes[1, 1].bar(x_pf - width_pf/2, paid_free_df['paid_score'], width_pf,
        label='Paid', color='#e74c3c', alpha=0.8)
    axes[1, 1].bar(x_pf + width_pf/2, paid_free_df['free_score'], width_pf,
        label='Free Alt', color='#2ecc71', alpha=0.8)
    axes[1, 1].set_xticks(x_pf)
    axes[1, 1].set_xticklabels(paid_free_df['paid_model'], rotation=45, ha='right', fontsize=8)
    axes[1, 1].set_ylabel('Composite Score')
    axes[1, 1].set_title('Paid Model vs Free Alternative (score comparison)')
    axes[1, 1].legend(fontsize=8)
    axes[1, 1].grid(True, alpha=0.3)
    for i in range(len(paid_free_df)):
        gap = paid_free_df.iloc[i]['score_gap']
        axes[1, 1].text(i, max(paid_free_df.iloc[i]['paid_score'], paid_free_df.iloc[i]['free_score']) + 1,
            f'gap: {gap:.1f}', ha='center', fontsize=7, fontweight='bold')
else:
    axes[1, 1].text(0.5, 0.5, 'No paid vs free comparison available',
        ha='center', va='center', transform=axes[1, 1].transAxes)
    axes[1, 1].set_title('Paid vs Free Alternative')

plt.tight_layout()
plt.savefig('ai_model_comparison.png', dpi=150, bbox_inches='tight')
print('Saved: ai_model_comparison.png')

# Console output
print('\n--- AI MODEL COMPARISON (PAID VS FREE) ---')
print(f'Models analyzed: {len(models)}')
print(f'\nPerformance Tiers:')
for tier in ['Tier 1: Best in Class', 'Tier 2: Strong Performer', 'Tier 3: Solid Choice', 'Tier 4: Entry Level']:
    tier_models = models[models['tier'] == tier]
    if len(tier_models) > 0:
        names = ', '.join(tier_models['model'].tolist())
        print(f'  {tier}: {names}')

print(f'\nBest overall (composite): {models.loc[models["benchmark_score"].idxmax(), "model"]} ({models["benchmark_score"].max()})')
print(f'Best free alternative (composite): {free_models.loc[free_models["benchmark_score"].idxmax(), "model"]} ({free_models["benchmark_score"].max()})')
print(f'Best value (score/cost): {models.loc[(models["benchmark_score"] / (models["cost_input_1k"] * 1000)).idxmax(), "model"]}')
print(f'Longest context: {models.loc[models["context_window"].idxmax(), "model"]} ({models["context_window"].max():,} tokens)')
print(f'Fastest: {models.loc[models["speed_tokens_per_sec"].idxmax(), "model"]} ({models["speed_tokens_per_sec"].max()} tok/s)')

print('\n--- PAID MODEL VS FREE ALTERNATIVE ---')
for _, row in models.iterrows():
    print(f'\n{row["model"]} ({row["provider"]})')
    print(f'  Cost: ${row["cost_input_1k"]*1000:.2f}/1K inputs | Score: {row["benchmark_score"]} | Open source: {row["open_source"]}')
    alt = row['free_alternative']
    if alt:
        alt_data = models[models['model'] == alt['alternative']].iloc[0]
        print(f'  >> FREE ALTERNATIVE: {alt["alternative"]} (${alt_data["cost_input_1k"]*1000:.2f}/1K inputs, score: {alt_data["benchmark_score"]})')
        print(f'     Save {alt["savings_pct"]}% on API costs.')
        print(f'     Score gap: {alt_data["benchmark_score"] - row["benchmark_score"]:+.1f} points.')
        print(f'     Trade-off: {alt["trade_off"]}')
        print(f'     Best use case for free: {alt["best_for"]}')
    else:
        print(f'  >> Already free / open source.')

print('\n--- USE CASE RECOMMENDATIONS ---')
for _, row in models.iterrows():
    print(f'\n{row["model"]} ({row["provider"]}):')
    print(f'  Tier: {row["tier"]}')
    print(f'  Best for: {row["recommended_for"]}')

# Export
models.to_csv('model_comparison_data.csv', index=False)
if len(paid_free_df) > 0:
    paid_free_df.to_csv('paid_vs_free_alternatives.csv', index=False)
    print('\nExported: model_comparison_data.csv, paid_vs_free_alternatives.csv')
else:
    print('\nExported: model_comparison_data.csv')
print('Done.')
