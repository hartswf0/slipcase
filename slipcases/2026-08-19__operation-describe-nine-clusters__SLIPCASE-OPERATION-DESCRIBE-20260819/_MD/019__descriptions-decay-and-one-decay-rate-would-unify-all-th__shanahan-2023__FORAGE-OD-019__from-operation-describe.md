ZETTEL

ID:
FORAGE-OD-019

TITLE:
DESCRIPTIONS DECAY, AND ONE DECAY RATE WOULD UNIFY ALL THREE OF THE ARCHIVE'S CASES

SOURCE:
Murray Shanahan, Kyle McDonell, Laria Reynolds — Role-Play with Large Language Models — Nature 623:493–498 — 2023 — §§2–3, as recorded in SLIPCASE zettel FORAGE-SHANAHAN-001; read against Watson Hartsoe — PAPERS/abc-cineosis-paper.md §6 (third unstable question) — 2026

PASSAGE:
[PARAPHRASE]
Shanahan et al.: a dialogue prompt supplies an initial characterization, but every subsequent exchange becomes additional context that can extend or overwrite that characterization, changing the role the agent performs.

[QUOTE]
SLIPCASE FORAGE-SHANAHAN-001, MISSING field:
"A theory of which parts of context remain load-bearing, which decay, which are overwritten, and what forms of instruction resist conversational drift."

[QUOTE]
abc-cineosis-paper.md §6:
"What does duration and motion (ABC Cineosis) add to the semiotic loop that cannot be observed in text or still image generation?"

RESEARCH OBJECT:
The archive's unit of analysis is the pair ⟨D, A_route⟩. It is not time-indexed.

Every case in the archive is in fact time-indexed, and each has an unstudied decay:

  a system prompt's hold on a role decays over conversational turns
  a video prompt's adherence decays over generated frames
  a repository label's predictive power over action decays over days
  a policy category's fit to its objects decays over releases

One quantity — the half-life of an operative description — would answer the archive's third unstable question and fill the gap the user's own SLIPCASE corpus already recorded as missing.

LOCAL MOVE:
Shanahan et al. are arguing against the persona metaphor. They establish, in passing, that the initial specification is not durable. They do not measure how fast it stops being durable.

The archive, separately, asks what duration adds. Neither notices that the answer to the second is the measurement of the first.

SOURCE TERMS:
dialogue prompt
preamble
context
continuation
superposition of simulacra
conversational drift
duration
temporal collapse
prompt adherence

WHAT BECAME STRANGE:
"Operative" has been treated as a binary predicate — a description either routes or it does not.

Nothing in the archive's own formalism forces that. ΔG is a function of context, and context grows monotonically. So ΔG must be a function of time, and the natural object is not a predicate but a curve.

QUESTION:
What is the functional form of ΔG(t) for a fixed description as the operator's context accumulates — exponential, power-law, or step-wise on specific overwriting events?

DEEPER QUESTION:
If decay is event-driven rather than smooth, then what matters is not elapsed time but the arrival of *competing* descriptions — and the object of study becomes description competition, not description power.

MECHANISM:
<DESCRIPTION D AT t₀>
→ sets initial route margin m₀
→ context accumulates: new turns, new frames, new comments, new labels
→ [EACH ADDITION COMPETES FOR THE SAME ATTENTION BUDGET]
→ m_t declines
→ [SOME ADDITION DIRECTLY CONTRADICTS D]
→ m_t steps to ~0
→ <D NO LONGER ROUTES>

FORMAL SHIFT:
<DESCRIPTION>
→ <TIME-INDEXED ROUTE MARGIN>
→ [DECAY UNDER COMPETING CONTEXT]
→ <HALF-LIFE>

SOURCE FORMALISM:
Shanahan et al. supply the autoregressive frame: P(w_{n+1} | w_1 … w_n), with sampled tokens appended to context. That is sufficient to make decay expected but says nothing about its rate.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

  ΔG(D, t) = route margin attributable to D at step t

  half-life λ(D) = min { t : ΔG(D, t) ≤ ½ ΔG(D, 0) }

Three measurements, one metric, three case studies — which is exactly the comparative structure the archive has been trying to justify:

  λ measured in turns   → the LLM case
  λ measured in frames  → the ABC Cineosis case
  λ measured in days    → the GitHub label case

And a design claim falls out immediately: **the durability of a description is a design variable independent of its initial strength.** A weak, durable description may route more total action than a strong, brittle one. Nothing in the archive can currently say this.

TENSION:
READING A: decay is dilution — a fixed description's influence falls simply because context grows, so λ scales with context length and is not a property of D.
READING B: decay is displacement — λ depends on whether later content *contradicts* D, so λ is a property of the D-and-successor relation, and a well-formed description can be arbitrarily durable.

These predict opposite things: under A, padding with irrelevant text shortens λ; under B, it does not. That is a one-experiment discrimination.

MISSING:
Any longitudinal measurement in the archive. Every entry in its YAML schema is a single loop step. The schema has `next_prompt` but no time axis and no decay field.

Also missing: the human-side λ. Nobody in the archive has asked how long a GitHub label keeps predicting action after application.

BOUNDARY:
Shanahan et al. establish that roles can be overwritten; they do not measure rates and are not about video or labels. λ is proposed here as a research object, not reported as a finding.

CITATION TRAIL:
Shanahan, McDonell, Reynolds — Role-Play with Large Language Models — Nature 2023 — arXiv:2305.16367.
SLIPCASE case "2026 08 18 — what kind of thing is the model" — the user's own corpus, where the same gap is recorded in a different vocabulary.
Prompt-adherence / temporal-consistency metrics in video generation.
Survival analysis, for the right statistical tool.
FORAGE-OD-020, FORAGE-OD-029.

TEST:
Fix a system prompt with a checkable commitment ("always answer in exactly one sentence"). Then run two arms of equal token growth: (a) padding with unrelated text, (b) turns that gradually normalize multi-sentence answers.

Measure the turn at which compliance halves in each arm.

Equal λ supports dilution. Shorter λ in arm (b) supports displacement. Either result gives the archive its first decay curve, and the same protocol transfers directly to frames and to days.

PLATFORM:
[[the-half-life-of-a-description]]

LINKS:
[[FORAGE-OD-020]]
[[FORAGE-OD-029]]
[[FORAGE-OD-006]]
[[FORAGE-OD-012]]

BIBTEX:
@article{shanahan2023roleplay,
  title={Role-Play with Large Language Models},
  author={Shanahan, Murray and McDonell, Kyle and Reynolds, Laria},
  journal={Nature},
  volume={623},
  pages={493--498},
  year={2023},
  url={https://arxiv.org/abs/2305.16367}
}
