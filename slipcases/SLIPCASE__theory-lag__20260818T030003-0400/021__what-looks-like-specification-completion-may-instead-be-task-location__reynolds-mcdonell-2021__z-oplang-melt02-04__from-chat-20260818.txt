ZETTEL

ID:
Z-OPLANG-MELT02-04

TITLE:
What looks like specification completion may instead be task location.

SOURCE:
Laria Reynolds and Kyle McDonell — “Prompt Programming for Large Language Models: Beyond the Few-Shot Paradigm” — 2021 — §§1, 3–4.

SOURCE URL:
https://arxiv.org/abs/2102.07350

PASSAGE:
[PARAPHRASE]
Reynolds and McDonell argue that, in some GPT-3 tasks, few-shot prompting is better understood as locating an already learned task than as teaching the task at runtime.

RESEARCH OBJECT:
<TASK LOCATION> as a rival mechanism to <SPECIFICATION COMPLETION>.

LOCAL MOVE:
The authors interpret successful prompting as eliciting behaviors already available in the model rather than necessarily constructing or teaching those behaviors through the prompt.

SOURCE TERMS:
“task location”
“learned tasks”
“prompt programming”
“direct task specification”
“demonstration”
“proxy”
“natural language”
“desired behavior”

WHAT BECAME STRANGE:
Our current mechanism says:

<human partial specification>
→ <model completes missing specification>
→ <realization>.

But suppose the model already contains a latent behavioral repertoire.

Then:

“Masterful French translator…”

may not complete a specification.

It may locate a region of already learned behavior.

The omitted information was never missing from the operative system.

It was missing only from the visible prompt.

QUESTION:
How can we empirically distinguish specification completion from task location?

DEEPER QUESTION:
Where is the “program” when a tiny expression selects a complex behavior whose operative structure resides largely in learned weights?

MECHANISM A — SPECIFICATION COMPLETION:
<prompt>
supplies partial constraints.

<model>
[infers previously unresolved structure].

MECHANISM B — TASK LOCATION:
<model>
already contains <behavioral repertoire>.

<prompt>
[selects / activates / locates]
<behavioral region>.

The same sparse surface expression can arise from radically different mechanisms.

FORMAL SHIFT:
<PARTIAL SPECIFICATION>
→ [COMPLETE]
→ <BEHAVIOR>

splits into competing readings:

READING A:
<PARTIAL SPEC>
→ [CONSTRUCT COMPLETION]
→ <BEHAVIOR>

READING B:
<CUE>
→ [LOCATE LATENT TASK]
→ <BEHAVIOR>

SOURCE FORMALISM:
Reynolds and McDonell explicitly introduce “task location” as an interpretation of some prompting behavior and distinguish direct specification, demonstration, and proxy methods.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let model M contain latent behavior set:

B = {b1, b2, ..., bn}.

Task-location account:

P [indexes] b_i ∈ B.

Specification-completion account:

P + M [construct] b* whose relevant constraints were not already represented as a stable latent behavior.

The hard problem is deciding what “already represented” means in a distributed model.

TENSION:
“Task location” itself is metaphorical.

Neural models do not necessarily contain clean, enumerable tasks waiting on shelves.

A model may compose behaviors dynamically from distributed representations.

Thus task location and specification completion may not be mutually exclusive.

MISSING:
A discriminating experiment.

The field needs tasks varying independently in:
- familiarity,
- novelty,
- compositional novelty,
- linguistic describability,
- demonstration availability.

BOUNDARY:
Reynolds and McDonell demonstrate task-location behavior only for particular models and tasks.

Their paper does not establish task location as a general theory of prompting.

CITATION TRAIL:
In-context learning.
Representation probing.
Task vectors.
Compositional generalization.
Program synthesis.
Prompt Programming.

TEST:
Construct paired tasks:

A. well-known task strongly represented in training culture;
B. novel arbitrary mapping defined entirely in-context;
C. novel composition of known operations.

Hold prompt length approximately constant.

If sparse prompts succeed mainly on A, task location gains support.

If the system can reliably realize B after constraints are progressively introduced, specification completion gains support.

If C behaves differently from both, split the mechanisms again.

PLATFORM:
[[Interpretive Coupling]]

LINKS:
[[Specification Completion]]
[[Task Location]]
[[Learned Semantics]]

BIBTEX:
@inproceedings{reynolds2021prompt,
  author = {Reynolds, Laria and McDonell, Kyle},
  title = {Prompt Programming for Large Language Models: Beyond the Few-Shot Paradigm},
  booktitle = {Extended Abstracts of the 2021 CHI Conference on Human Factors in Computing Systems},
  year = {2021},
  pages = {1--7}
}
