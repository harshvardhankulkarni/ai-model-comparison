
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

models = ['GPT-4o', 'GPT-4 Turbo', 'Claude 3.5 Sonnet', 'Claude 3 Opus',
          'Gemini 1.5 Pro', 'Gemini 1.5 Flash', 'Llama 3 70B', 'Llama 3 8B',
          'Mistral Large', 'Mixtral 8x7B']
providers = ['OpenAI','OpenAI','Anthropic','Anthropic','Google','Google','Meta','Meta','Mistral','Mistral']
scores = [88.7, 86.5, 89.0, 86.8, 85.9, 79.0, 82.0, 66.0, 84.0, 68.0]
human = [90.2, 87.0, 92.0, 84.1, 84.0, 74.0, 80.0, 56.0, 82.0, 54.0]
cost = [0.005, 0.01, 0.003, 0.015, 0.0035, 0.00035, 0.00065, 0.00006, 0.002, 0.0002]
open_src = [False,False,False,False,False,False,True,True,True,True]

colors = {'OpenAI': '#74aa9c', 'Anthropic': '#d4a574', 'Google': '#8ab4f8',
          'Meta': '#8a9eb0', 'Mistral': '#c9957a'}

fig = make_subplots(rows=2, cols=2,
    subplot_titles=('Benchmark Scores by Model', 'Composite Score',
                    'Cost vs Performance', 'Model Speed Comparison'),
    specs=[[{'type': 'bar'}, {'type': 'bar'}],
           [{'type': 'scatter'}, {'type': 'bar'}]])

composite = [round(m*0.25 + h*0.30 + g*0.25 + t*0.20, 1) for m, h, g, t in
             zip(scores, human, [95.8,92,96,95,91,86,87,72,90,70], [82.5,80,85,83,78,72,75,55,76,60])]

for i, m in enumerate(models):
    fig.add_trace(go.Bar(x=[m], y=[scores[i]], name=m,
                         marker_color=colors[providers[i]],
                         showlegend=False, text=scores[i], textposition='outside'), row=1, col=1)

bar_colors = ['#2ecc71' if os else '#e74c3c' for os in open_src]
fig.add_trace(go.Bar(x=models, y=composite, marker_color=bar_colors,
                     text=composite, textposition='outside', showlegend=False), row=1, col=2)

for p in set(providers):
    idxs = [i for i, x in enumerate(providers) if x == p]
    fig.add_trace(go.Scatter(x=[cost[i]*1000 for i in idxs], y=[composite[i] for i in idxs],
                             mode='markers+text', name=p,
                             text=[models[i] for i in idxs],
                             textposition='top center',
                             marker=dict(size=12, color=colors[p]),
                             hovertemplate='%{text}<br>Cost: $%{x:.2f}/1K<br>Score: %{y:.1f}<extra></extra>'),
                  row=2, col=1)

speeds = [85, 60, 75, 40, 50, 120, 90, 140, 80, 110]
fig.add_trace(go.Bar(x=models, y=speeds, marker_color=[colors[p] for p in providers],
                     text=speeds, textposition='outside', showlegend=False), row=2, col=2)

fig.update_layout(height=750, title_text='AI Model Comparison - Interactive', hovermode='closest')
fig.write_html('ai_model_comparison_interactive.html')
print('Saved: ai_model_comparison_interactive.html')
