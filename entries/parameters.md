# Parameters

*The fundamental unit of measurement for the size — and, very approximately, the capability — of a modern AI model.*

---

## In one sentence

**A parameter is a single number inside a neural network whose value was determined during training, and a model's "parameter count" — the figure usually quoted alongside its name (Gemma 4 *26B*, Llama 3.3 *70B*) — is the total number of those numbers, typically running from a few hundred million on the small end to a trillion or more on the frontier.**

## Why this term exists

Modern language models are, mechanically, very large mathematical functions. The function takes input tokens and produces output tokens, and the recipe for getting from input to output is *a long sequence of weighted-sum operations*. Each weighted sum has a multiplier — a *parameter* — that says *how much* this particular input matters to this particular output.

Training is the process of finding good values for those multipliers. Trillions of training examples flow through the model, each one nudging the parameter values slightly to make the model's outputs match the desired outputs better. When training finishes, the parameter values are frozen. The "frozen blob of numbers" is the model.

The number of parameters, then, is a structural property of the model — it tells you how big the function is, how much memory it takes to load, and (very roughly) how much capacity it has to represent useful patterns.

## What it actually does — concretely

A working language model is a stack of mathematical operations called *layers*. Inside each layer are matrices of numbers — the parameters — that get multiplied with the input to produce the layer's output. The output of one layer becomes the input of the next.

If a model has 26 billion parameters, that means there are 26 billion individual numbers stored on disk and loaded into memory when the model runs. Each one is typically a 16-bit or 32-bit floating-point number; with the common 4-bit quantization, each parameter is squeezed down to 4 bits of storage. The math:

- 26 billion parameters × 4 bits each = 104 billion bits = 13 GB
- 70 billion parameters × 4 bits each = 280 billion bits = 35 GB
- 405 billion parameters × 4 bits each = 1,620 billion bits = 200 GB (will not fit on most home hardware)

That is why parameter count is the first specification anyone looks at when picking a local model. It tells you whether the model will *fit*.

## A small but important warning about parameters as a quality measure

It is tempting to assume *more parameters = better model*. This is broadly true at the frontier (a 405B model knows more than a 7B model from the same family), but the relationship is loose and full of exceptions:

- A *30B Mixture-of-Experts (MoE)* model may outperform a *70B dense* model on many tasks despite having fewer total parameters, because only a fraction of its weights activate per token (see the [Ollama](ollama.md) entry for the M5 Max benchmark where *Gemma 4 26B MoE* ran at 96 tok/s versus *Gemma 4 31B dense* at 25 tok/s on the same hardware).
- A well-trained 13B model can beat a poorly-trained 70B model on most tasks. *Training data quality and method dominate parameter count* once you are above a few billion.
- A model fine-tuned for a specific domain often beats a much larger general-purpose model on that domain.

The headline parameter count is the rough size of the model. It is *not* the rough quality of the model. Confusing the two is a common rookie mistake — and a common vendor-marketing trick.

## Working example from this machine

The four local models benchmarked on this MacBook on May 2, 2026, ordered by parameter count:

| Model | Parameters | Architecture | Size on disk (Q4) | Tok/sec |
|-------|----------:|--------------|-------------:|------:|
| Gemma 4 26B | 26 billion | MoE (sparse) | 17 GB | 96.5 |
| Gemma 3 27B | 27 billion | Dense | 17 GB | 29.0 |
| Gemma 4 31B | 31 billion | Dense | 19 GB | 24.6 |
| Qwen 2.5 32B | 32 billion | Dense | 19 GB | 25.7 |

Notice that the smallest-parameter model — Gemma 4 26B — outruns all the larger ones by a factor of nearly 4×. Architecture (sparse vs. dense) matters more than raw parameter count for inference speed. This is the same lesson stated above, made concrete.

## Why this matters in a teaching context

For an MBA classroom, parameter count is a useful entry point into a deeper management lesson: **headline metrics are usually less informative than the supporting structure that produced them.**

The same pattern shows up in:

- Revenue figures (where the *quality* of the revenue — recurring vs. one-time — matters more than the number)
- Headcount (where the *roles* matter more than the total)
- Patent counts (where the *value* of the patents matters more than the count)

A management student who internalizes the pattern *"the headline number is a starting point, not an answer"* will be a more rigorous strategist. AI parameter counts are a particularly clean teaching example because the gap between headline and reality can be demonstrated in twenty minutes of benchmarking.

## Trade-offs

- **Bigger = more capable, all else equal.** All else is rarely equal.
- **Bigger = slower and more expensive to run.** Real, predictable, linear in most cases.
- **Bigger = harder to deploy locally.** A 405B model needs a server-class machine or a multi-GPU rig. A 7B model runs on a Mac Mini.
- **Parameter count tells you nothing about training data quality, alignment quality, or domain fit.** These often dominate.

## Related and adjacent terms

- *Quantization* — the practice of squeezing each parameter into fewer bits (typically 4) to make the model fit.
- *Mixture of Experts (MoE)* — an architecture where most parameters stay inactive on any given token, allowing larger total parameter counts at lower per-token cost.
- *Dense model* — the conventional architecture where all parameters activate on every token.
- *Token* — the unit of input/output. Different from a parameter.

---

*Related entries: [Ollama](ollama.md), [Token burn](token-burn.md), [Fine-tuning](fine-tuning.md), forthcoming Quantization.*
