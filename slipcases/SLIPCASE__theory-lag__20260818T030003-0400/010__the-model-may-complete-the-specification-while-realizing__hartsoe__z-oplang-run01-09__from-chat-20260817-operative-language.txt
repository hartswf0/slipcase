ZETTEL

ID:
Z-OPLANG-RUN01-09

TITLE:
The model may complete the specification while realizing it.

SOURCE:
Watson Hartsoe — BETWEEN CODE AND POETRY — 2026 — §§13–15. fileciteturn1file0L504-L616
Watson Hartsoe — The Warm Seed — 2026 — fragments 36–38. fileciteturn0file0L466-L492

SOURCE URL:
sandbox:/mnt/data/Pasted%20markdown(20260817-170730).md
sandbox:/mnt/data/Pasted%20markdown(20260817-170018).md

PASSAGE:
[PARAPHRASE]
The dissertation notes describe prompts as expressions capable of reference, constraint, transformation, iteration, and evaluation without deterministic specification. The aphoristic manuscript adds that a prompt can discover what its symbols meant only after the machine responds.

RESEARCH OBJECT:
<SPECIFICATION COMPLETION>.

A generative model may not merely execute an incomplete specification. Its realization can supply concrete commitments that retrospectively reveal what the specification meant.

LOCAL MOVE:
The source initially treats the prompt as defining a region of acceptable possibility. The later aphorism destabilizes the assumption that this region was fully known before generation.

SOURCE TERMS:
“viable prompt”
“region of possibility”
“evaluation”
“context”
“iteration”
“discover”
“failed prompt”

WHAT BECAME STRANGE:
The standard sequence:

<specification>
→ <execution>

assumes that the criterion exists clearly before realization.

Prompting often behaves differently.

A user can say:
“Make the house remember.”

The model must decide what memory looks like.

Those decisions make latent interpretations concrete.

Only then can the user say:
“No—not that kind of remembering.”

The attempted realization has participated in specifying the task.

QUESTION:
Does generative prompting delegate not only execution but part of specification itself?

DEEPER QUESTION:
What becomes of the distinction between programmer and interpreter when interpretation generates commitments that the original specifier had not yet articulated?

MECHANISM:
<human>
[provides] <partial specification>.

<model>
[infers] <unstated commitments> while [realizing] <candidate>.

<candidate>
[externalizes] <one interpretation of specification>.

<human>
[judges] <interpretation>.

<judgment>
[clarifies] <next specification>.

Specification develops through its attempted realizations.

FORMAL SHIFT:
<PARTIAL SPECIFICATION>
→ <INTERPRETIVE COMPLETION>
→ [REALIZE]
→ <EXTERNALIZED INTERPRETATION>
→ [CORRECT]
→ <REFINED SPECIFICATION>

SOURCE FORMALISM:
NONE.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

At t0:

S0 = explicitly stated constraints.

Model supplies latent completion:

C0 = M(S0, context).

Realization:

R0 = realize(S0 + C0).

Human judgment yields:

ΔS = evaluate(R0).

Then:

S1 = S0 + ΔS.

Critically, ΔS may contain criteria not present in S0.

TENSION:
All design can involve discovering requirements through prototypes.

Software specifications also evolve after implementation.

Therefore specification completion is not unique to LLMs.

What may differ is the speed and cheapness with which underspecified representations can be repeatedly externalized into candidate realizations.

MISSING:
A distinction between:
- inference the user already intended but omitted,
- genuinely new model contribution,
- accidental artifact later adopted by the human,
- correction of misunderstanding.

These mechanisms should not be collapsed.

BOUNDARY:
The evidence does not prove that the model understands the intended specification.

It shows that outputs can function as probes that make latent or missing specification visible.

CITATION TRAIL:
Prototype-driven requirements engineering.
Reflective design.
Program synthesis from examples.
Interactive machine learning.
Specification mining.
Design-by-example systems.

TEST:
Ask participants to specify a complex artifact before generation.

Record explicit requirements.

Generate candidates.

After each rejection, record newly stated criteria.

Classify each criterion:
A. already stated,
B. consciously intended but omitted,
C. recognized only after seeing output,
D. adopted from unexpected model behavior.

Measure how much final specification emerges only through realization.

PLATFORM:
[[Deferred Formalization]]

LINKS:
[[Specification Completion]]
[[Prototype as Query]]
[[Failure Becomes Specification]]

BIBTEX:
@unpublished{hartsoe2026betweencodepoetry,
  author = {Hartsoe, Watson},
  title = {Between Code and Poetry: Committee Notes Toward a Prompt-Forward Dissertation},
  year = {2026},
  note = {Unpublished manuscript supplied by the author}
}
