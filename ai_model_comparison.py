"""
AI Model Comparison - Demo Project
Interactive CLI: tells you what you want to do, recommends the best model
with paid/free alternatives and platform info.
"""

import pandas as pd
import numpy as np

models = pd.DataFrame({
    'model': ['GPT-4o', 'Claude 3.5 Sonnet', 'Gemini 1.5 Pro', 'Llama 3 70B',
              'Mistral Large', 'DALL-E 3', 'Stable Diffusion 3.5', 'Midjourney',
              'FLUX.1', 'Claude 3 Haiku'],
    'type': ['LLM', 'LLM', 'LLM', 'LLM', 'LLM', 'Image', 'Image', 'Image', 'Image', 'LLM'],
    'open_source': [False, False, False, True, True, False, True, False, True, False],
    'coding': [90, 92, 84, 80, 82, 0, 0, 0, 0, 75],
    'content': [88, 85, 82, 76, 78, 92, 82, 95, 88, 70],
    'reasoning': [89, 91, 86, 83, 84, 0, 0, 0, 0, 78],
    'analysis': [87, 90, 88, 81, 83, 0, 0, 0, 0, 76],
    'multilingual': [85, 82, 91, 78, 80, 0, 0, 0, 0, 72],
    'image_gen': [0, 0, 0, 0, 0, 95, 85, 90, 88, 0],
    'cost_monthly': [200, 150, 120, 30, 80, 50, 0, 60, 0, 30],
    'speed': [85, 75, 50, 90, 80, 30, 60, 20, 55, 120],
})

platforms = {
    'GPT-4o': {
        'api': 'OpenAI API (platform.openai.com)',
        'web': 'ChatGPT (chatgpt.com)',
        'free_tier': False,
        'self_host': False,
    },
    'Claude 3.5 Sonnet': {
        'api': 'Anthropic API (console.anthropic.com)',
        'web': 'Claude (claude.ai)',
        'free_tier': False,
        'self_host': False,
    },
    'Gemini 1.5 Pro': {
        'api': 'Google AI Studio (makersuite.google.com)',
        'web': 'Gemini (gemini.google.com)',
        'free_tier': True,
        'self_host': False,
    },
    'Llama 3 70B': {
        'api': 'Groq (groq.com), Replicate (replicate.com)',
        'web': 'Hugging Face Chat (huggingface.co/chat)',
        'free_tier': True,
        'self_host': True,
    },
    'Mistral Large': {
        'api': 'Mistral API (console.mistral.ai)',
        'web': 'Le Chat (chat.mistral.ai)',
        'free_tier': True,
        'self_host': True,
    },
    'DALL-E 3': {
        'api': 'OpenAI API (platform.openai.com)',
        'web': 'ChatGPT (chatgpt.com)',
        'free_tier': False,
        'self_host': False,
    },
    'Stable Diffusion 3.5': {
        'api': 'Hugging Face Inference, Replicate',
        'web': 'Hugging Face Spaces, Stability AI web',
        'free_tier': True,
        'self_host': True,
    },
    'Midjourney': {
        'api': 'Midjourney API (midjourney.com/api)',
        'web': 'Discord (discord.gg/midjourney)',
        'free_tier': False,
        'self_host': False,
    },
    'FLUX.1': {
        'api': 'Replicate, Hugging Face Inference',
        'web': 'Hugging Face Spaces',
        'free_tier': True,
        'self_host': True,
    },
    'Claude 3 Haiku': {
        'api': 'Anthropic API (console.anthropic.com)',
        'web': 'Claude (claude.ai)',
        'free_tier': False,
        'self_host': False,
    },
}

free_alternatives = {
    'GPT-4o': {'alt': 'Llama 3 70B', 'savings': 97, 'gap': -8.5},
    'Claude 3.5 Sonnet': {'alt': 'Mistral Large', 'savings': 47, 'gap': -7.5},
    'Gemini 1.5 Pro': {'alt': 'Mistral Large', 'savings': 33, 'gap': -1.7},
    'DALL-E 3': {'alt': 'Stable Diffusion 3.5', 'savings': 100, 'gap': -10},
    'Midjourney': {'alt': 'FLUX.1', 'savings': 100, 'gap': -2},
}

use_cases = {
    '1': {'label': 'Code generation / software development', 'key': 'coding'},
    '2': {'label': 'Content creation / copywriting', 'key': 'content'},
    '3': {'label': 'Image generation', 'key': 'image_gen'},
    '4': {'label': 'Data analysis & reporting', 'key': 'analysis'},
    '5': {'label': 'Document analysis & summarization', 'key': 'analysis'},
    '6': {'label': 'Math & reasoning tasks', 'key': 'reasoning'},
    '7': {'label': 'Translation & multilingual', 'key': 'multilingual'},
    '8': {'label': 'General Q&A / chatbot', 'key': 'coding'},
}

budget_opts = {
    '1': {'label': 'Free / open source only (save money)', 'max_cost': 1},
    '2': {'label': 'Balanced (good quality at fair price)', 'max_cost': 100},
    '3': {'label': 'Premium (best quality, cost unlimited)', 'max_cost': 99999},
}


def recommend(use_case_key, budget_max, need_open_source):
    filtered = models.copy()
    if need_open_source:
        filtered = filtered[filtered['open_source'] == True]
    filtered = filtered[filtered['cost_monthly'] <= budget_max]
    if len(filtered) == 0:
        msg = 'open source' if need_open_source else 'budget'
        print(f'  No models match your {msg} criteria.')
        return None
    primary_score = filtered[use_case_key]
    filtered['score'] = primary_score + filtered['reasoning'] * 0.3 + filtered['speed'] / 200
    filtered = filtered.sort_values('score', ascending=False)
    return filtered


def print_platform(model_name):
    p = platforms.get(model_name)
    if not p:
        return
    print(f'    API: {p["api"]}')
    print(f'    Web: {p["web"]}')
    if p['free_tier']:
        print('    Free tier: Yes')
    if p['self_host']:
        print('    Self-hostable: Yes')


def interactive():
    print('\n' + '=' * 60)
    print('  AI MODEL RECOMMENDER')
    print('  Tell me what you need -- I will recommend the best model.')
    print('=' * 60)
    print()
    for k, v in use_cases.items():
        print(f'  [{k}] {v["label"]}')

    while True:
        choice = input('\nWhat do you want to do? (1-8): ').strip()
        if choice in use_cases:
            break
        print('  Invalid. Pick 1-8.')

    use_case = use_cases[choice]
    print(f'\nYou selected: {use_case["label"]}')
    print()

    for k, v in budget_opts.items():
        print(f'  [{k}] {v["label"]}')
    while True:
        bc = input('\nBudget preference? (1-3): ').strip()
        if bc in budget_opts:
            break
        print('  Invalid. Pick 1-3.')

    budget = budget_opts[bc]
    print()

    need_os = input('Need open source / self-hostable? (y/n): ').strip().lower() == 'y'

    result = recommend(use_case['key'], budget['max_cost'], need_os)
    if result is None:
        return

    print('\n' + '-' * 60)
    print('  TOP RECOMMENDATIONS')
    print('-' * 60)
    for i, (_, row) in enumerate(result.head(3).iterrows()):
        tag = 'OPEN SOURCE' if row['open_source'] else 'PAID'
        print(f'\n  #{i+1}: {row["model"]} ({row["type"]}) [{tag}]')
        print(f'    Score: {row["score"]:.1f} | Cost: ${row["cost_monthly"]}/mo')
        print_platform(row['model'])

        alt = free_alternatives.get(row['model'])
        if alt:
            alt_data = models[models['model'] == alt['alt']].iloc[0]
            print(f'    >> Free alternative: {alt["alt"]} (save {alt["savings"]}%, gap: {alt["gap"]:+.1f})')
            print_platform(alt['alt'])

    print('\n  ALL MODELS RANKED:')
    for _, row in result.iterrows():
        tag = 'FREE' if row['open_source'] else 'PAID'
        print(f'    {row["model"]:25s} score: {row["score"]:.1f}  ${row["cost_monthly"]:>3}/mo  [{tag}]')
    print()

    # Also run the static analysis
    run_static_analysis()


def run_static_analysis():
    print('\n' + '=' * 60)
    print('  STATIC BENCHMARK COMPARISON')
    print('=' * 60)
    llm_only = models[models['type'] == 'LLM'].copy()
    llm_only['benchmark'] = (
        llm_only['coding'] * 0.25 + llm_only['reasoning'] * 0.30 +
        llm_only['content'] * 0.25 + llm_only['multilingual'] * 0.20
    ).round(1)
    best = llm_only.loc[llm_only['benchmark'].idxmax()]
    print(f'  Best overall LLM: {best["model"]} ({best["benchmark"]})')
    open_llm = llm_only[llm_only['open_source'] == True]
    if len(open_llm) > 0:
        best_open = open_llm.loc[open_llm['benchmark'].idxmax()]
        print(f'  Best free LLM: {best_open["model"]} ({best_open["benchmark"]})')

    print('\n  Performance Tiers:')
    for tier_name, lo, hi in [('Best in Class', 85, 100), ('Strong Performer', 78, 85),
                               ('Solid Choice', 70, 78), ('Entry Level', 0, 70)]:
        names = llm_only[(llm_only['benchmark'] >= lo) & (llm_only['benchmark'] < hi)]['model'].tolist()
        if names:
            print(f'    {tier_name}: {", ".join(names)}')
    print()

    print('  PAID MODEL VS FREE ALTERNATIVE')
    for _, row in models.iterrows():
        alt = free_alternatives.get(row['model'])
        if alt:
            alt_data = models[models['model'] == alt['alt']].iloc[0]
            print(f'  {row["model"]:20s} -> {alt["alt"]:20s} save {alt["savings"]:>2}%  gap {alt["gap"]:+.1f}')

    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(2, 2, figsize=(15, 11))
    colors = {'OpenAI': '#74aa9c', 'Anthropic': '#d4a574', 'Google': '#8ab4f8',
              'Meta': '#8a9eb0', 'Mistral': '#c9957a', 'Stability AI': '#9b59b6',
              'Black Forest Labs': '#e67e22', 'Midjourney': '#1abc9c'}
    providers_map = {'GPT-4o': 'OpenAI', 'Claude 3.5 Sonnet': 'Anthropic', 'Gemini 1.5 Pro': 'Google',
                     'Llama 3 70B': 'Meta', 'Mistral Large': 'Mistral', 'DALL-E 3': 'OpenAI',
                     'Stable Diffusion 3.5': 'Stability AI', 'Midjourney': 'Midjourney',
                     'FLUX.1': 'Black Forest Labs', 'Claude 3 Haiku': 'Anthropic'}

    x = np.arange(len(models))
    width = 0.2
    metrics = ['coding', 'content', 'reasoning', 'analysis']
    for i, metric in enumerate(metrics):
        axes[0, 0].bar(x + (i - 1.5) * width, models[metric], width,
                       label=metric.replace('_', ' ').title())
    axes[0, 0].set_xticks(x)
    axes[0, 0].set_xticklabels(models['model'], rotation=45, ha='right', fontsize=8)
    axes[0, 0].set_ylabel('Score')
    axes[0, 0].set_title('Capability Scores by Model')
    axes[0, 0].legend(fontsize=8)
    axes[0, 0].set_ylim(0, 100)
    axes[0, 0].grid(True, alpha=0.3)

    model_colors = [colors.get(providers_map.get(m, '#95a5a6')) for m in models['model']]
    base_scores = (models['coding'] * 0.2 + models['content'] * 0.2 +
                   models['reasoning'] * 0.2 + models['analysis'] * 0.2 +
                   models['multilingual'] * 0.1 + models['image_gen'] * 0.1).round(1)
    bars = axes[0, 1].barh(models['model'], base_scores, color=model_colors)
    axes[0, 1].set_xlabel('Composite Capability Score')
    axes[0, 1].set_title('Overall Model Capability')
    for bar, val in zip(bars, base_scores):
        axes[0, 1].text(val + 0.5, bar.get_y() + bar.get_height()/2,
                        f'{val}', va='center', fontsize=8, fontweight='bold')

    for i in range(len(models)):
        axes[1, 0].scatter(models['cost_monthly'].iloc[i], base_scores.iloc[i],
                          s=100, alpha=0.7, color=model_colors[i])
        axes[1, 0].annotate(models['model'].iloc[i].split()[0],
                           (models['cost_monthly'].iloc[i], base_scores.iloc[i]),
                           fontsize=7, ha='center', va='bottom')
    free_m = models[models['open_source'] == True]
    axes[1, 0].scatter(free_m['cost_monthly'], base_scores[free_m.index],
                      s=200, facecolors='none', edgecolors='#2ecc71', linewidths=2,
                      label='Free / Open Source')
    axes[1, 0].set_xlabel('Cost ($/month)')
    axes[1, 0].set_ylabel('Capability Score')
    axes[1, 0].set_title('Cost vs Capability (circled = free)')
    axes[1, 0].legend(fontsize=7)
    axes[1, 0].grid(True, alpha=0.3)

    axes[1, 1].text(0.5, 0.5,
        'Interactive Recommender:\nRun "python ai_model_comparison.py"\nto get personalized suggestions.',
        ha='center', va='center', transform=axes[1, 1].transAxes, fontsize=11)
    axes[1, 1].set_title('Need a recommendation?')

    plt.tight_layout()
    plt.savefig('ai_model_comparison.png', dpi=150, bbox_inches='tight')
    print('\nSaved: ai_model_comparison.png')

    models.to_csv('model_comparison_data.csv', index=False)
    print('Exported: model_comparison_data.csv')
    print('Done.')


if __name__ == '__main__':
    interactive()
