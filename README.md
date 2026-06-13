# AI Model Comparison - Demo Project

Compares 10 popular large language models across benchmarks, cost, speed, and context window. Provides use case recommendations for each model.

This is a demo project using publicly available benchmark data (MMLU, HumanEval, GSM8K, TruthfulQA) as of 2024-2025.

## Models Compared

| Model | Provider | Size | Open Source |
|-------|----------|------|-------------|
| GPT-4o | OpenAI | Unknown | No |
| GPT-4 Turbo | OpenAI | Unknown | No |
| Claude 3.5 Sonnet | Anthropic | Unknown | No |
| Claude 3 Opus | Anthropic | Unknown | No |
| Gemini 1.5 Pro | Google | Unknown | No |
| Gemini 1.5 Flash | Google | Unknown | No |
| Llama 3 70B | Meta | 70B | Yes |
| Llama 3 8B | Meta | 8B | Yes |
| Mistral Large | Mistral | Unknown | Yes |
| Mixtral 8x7B | Mistral | 47B | Yes |

## Metrics Compared

- **MMLU**: Massively Multitask Language Understanding (0-100%)
- **HumanEval**: Python code generation accuracy (0-100%)
- **GSM8K**: Grade school math problem solving (0-100%)
- **TruthfulQA**: Truthfulness and factuality (0-100%)
- **Context Window**: Maximum tokens per input
- **Cost**: USD per 1K input/output tokens
- **Speed**: Tokens per second

## Results

- **Best overall**: Claude 3.5 Sonnet (composite score 90.6)
- **Best value**: Llama 3 8B (near-zero cost, 56% of top performance)
- **Longest context**: Gemini 1.5 Pro (1M tokens)
- **Fastest**: Llama 3 8B (140 tok/s)
- **Best for coding**: Claude 3.5 Sonnet (HumanEval 92.0%)

## Use Case Recommendations

| Need | Recommended Model | Why |
|------|------------------|-----|
| Maximum accuracy | Claude 3.5 Sonnet / GPT-4o | Highest composite scores |
| Long document analysis | Gemini 1.5 Pro | 1M token context window |
| Cost sensitive, high volume | Gemini 1.5 Flash / Llama 3 8B | Lowest cost per token |
| Self hosted, data privacy | Llama 3 70B / Mistral Large | Open source, self deployable |
| Code generation | Claude 3.5 Sonnet | Best HumanEval score (92%) |
| Fast, simple tasks | Mixtral 8x7B / Llama 3 8B | High speed, low latency |

## How to Run

```bash
pip install pandas matplotlib numpy
python ai_model_comparison.py
```

Output: `ai_model_comparison.png` (4-panel chart) and `model_comparison_data.csv` (full dataset).

## Tech Stack

Python, Pandas, NumPy, Matplotlib

## License

MIT
