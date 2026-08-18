ZETTEL

ID:
WORKWORDS-PROMPT-008

TITLE:
A prompt becomes a research object when it is treated as a variable instead of a message.

SOURCE:
Ian Arawjo, Chelse Swoopes, Priyan Vaithilingam, Martin Wattenberg, and Elena L. Glassman — “ChainForge: A Visual Toolkit for Prompt Engineering and LLM Hypothesis Testing” — 2023 — arXiv:2309.09128; subsequently CHI 2024.

PASSAGE:
[PARAPHRASE] ChainForge is designed to compare responses across prompt variations and models rather than treating prompting as isolated conversational turns. The authors frame prompt engineering alongside on-demand hypothesis testing and identify opportunistic exploration, limited evaluation, and iterative refinement as recurring modes of practice.

RESEARCH OBJECT:
THE UNIT OF PROMPT RESEARCH SHOULD NOT BE THE SUCCESSFUL PROMPT.

It should be the DIFFERENCE produced by controlled changes.

A prompt without its alternatives hides the mechanism that made it appear effective.

LOCAL MOVE:
Turn PROMPT RECEIPTS into EXPERIMENTAL RECEIPTS.

Preserve:

prompt,
variant,
model,
parameters,
outputs,
evaluation,
failure,
and revision lineage.

SOURCE TERMS:
ChainForge
prompt variation
model comparison
hypothesis testing
opportunistic exploration
limited evaluation
iterative refinement

WHAT BECAME STRANGE:
Chat interfaces preserve chronology.

Experiments require counterfactual structure.

A scrollback tells us:

what happened next.

It does not automatically tell us:

what changed because one word changed.

QUESTION:
What is the smallest provenance structure that turns prompt practice from anecdotal craft into inspectable experimental knowledge?

DEEPER QUESTION:
Could the history of a creative work be represented not as drafts but as a causal graph of linguistic interventions and resulting worlds?

MECHANISM:
prompt variants
×
models
×
inputs

→ batches of outputs

→ comparison / evaluation

→ hypothesis revision.

FORMAL SHIFT:
FROM:

P1
→ output
→ P2
→ output
→ P3
→ satisfactory output

TO:

{P1,P2,...Pn}
×
{M1,M2,...Mm}
×
{X1,...Xk}

→ response field

→ contrasts.

SOURCE FORMALISM:
ChainForge uses a visual data-flow environment to construct comparisons among prompts, models, and generated responses for prompt engineering and hypothesis testing.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Prompt intervention:

ΔP = P' - P.

Observed world difference:

ΔW = G(P') - G(P).

A useful receipt records:

R = (P, ΔP, M, state, parameters, outputs, ΔW, evaluation).

Without ΔP and comparison outputs, provenance records execution but not causal evidence.

TENSION:
Systematic experimentation can reveal prompt effects.

But creative prompting may depend on serendipity, path dependence, situated judgment, and criteria discovered only after seeing an output.

Experimental rigor can therefore clarify mechanism while simultaneously discarding the changing purposes of the practitioner.

MISSING:
A method that preserves both:

controlled counterfactual comparison

and

the evolving criterion by which the practitioner decides what matters.

BOUNDARY:
ChainForge is designed primarily for LLM experimentation. A world-building or multimodal prompt practice introduces persistent state, images, space, motion, and model-mediated history that a simple prompt-response matrix may not capture.

CITATION TRAIL:
[[DEFAULT-IMAGES-CHI26-E]]
→ default-image study detects relational anomalies across many prompts
→ ChainForge operationalizes prompt comparison and hypothesis testing
→ prompt receipt becomes contrastive rather than archival
→ next edge: causal inference, version control, experimental notebooks, and output-directed programming.

TEST:
For one day of prompting, stop storing prompts as a chronological transcript.

Instead record each revision as:

CLAIM
INTERVENTION
CONTROL
OUTPUT DIFFERENCE
SURPRISE
NEXT QUESTION.

At the end of the day, test whether the resulting graph explains more about how the work changed than the original chat log.

PLATFORM:
ChainForge; LLM experimentation and prompt engineering.

LINKS:
[[DEFAULT-IMAGES-CHI26-E]]

BIBTEX:
@article{Arawjo2023ChainForge,
  author = {Arawjo, Ian and Swoopes, Chelse and Vaithilingam, Priyan and Wattenberg, Martin and Glassman, Elena L.},
  title = {ChainForge: A Visual Toolkit for Prompt Engineering and LLM Hypothesis Testing},
  year = {2023},
  url = {https://arxiv.org/abs/2309.09128}
}
