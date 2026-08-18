ZETTEL

ID:
FORAGE-WALLACE-001

TITLE:
THE RULE FOR READING THE PROMPT MAY LIVE OUTSIDE THE PROMPT

SOURCE:
Eric Wallace, Kai Xiao, Reimar Leike, Lilian Weng, Johannes Heidecke, and Alex Beutel — The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions — 2024 — §3 / Appendix A

PASSAGE:
[PARAPHRASE]
Wallace and colleagues propose an instruction hierarchy in which system instructions outrank user instructions and lower-privilege third-party content.

They compare training models on examples exhibiting this hierarchy with simply putting a textual description of the hierarchy in a system message.

The training intervention is substantially more robust than the prompt-only baseline.

RESEARCH OBJECT:
Some rules governing how instructions are interpreted cannot reliably be installed merely by stating those rules as instructions.

LOCAL MOVE:
The source changes instruction priority from content expressed in a prompt into a behavior learned across training examples.

SOURCE TERMS:
instruction hierarchy
privileged instructions
system message
user message
third-party content
prompt injection
training data
conflicting instructions

WHAT BECAME STRANGE:
The prompt may be unable to contain its own semantics.

"Treat this instruction as higher priority" is itself only another sequence of tokens unless the model already has machinery that makes priority effective.

QUESTION:
Where is the semantics of an instruction hierarchy implemented if describing the hierarchy in the highest-priority prompt is insufficient?

DEEPER QUESTION:
Can natural-language programming ever be self-contained when the rules that determine what language is executable reside partly in training, architecture, channel metadata, or external orchestration?

MECHANISM:
TRAINING:

examples of conflicting instructions
→ model learns priority-sensitive behavior
→ lower-privilege conflicting content is selectively ignored

PROMPT-ONLY BASELINE:

text describes hierarchy
→ model must interpret hierarchy using existing learned behavior
→ weaker robustness

FORMAL SHIFT:
<INSTRUCTION TEXT>
→ <TEXT + SOURCE / PRIVILEGE RELATION>
→ [LEARNED CONFLICT RESOLUTION]
→ <EXECUTED OR IGNORED INSTRUCTION>

SOURCE FORMALISM:
The proposed precedence is:

SYSTEM
>
USER
>
THIRD-PARTY CONTENT

The training method generates examples demonstrating how the model should respond when instructions at these levels conflict.

The authors report that their training data substantially outperform a baseline that merely explains the hierarchy in a system prompt.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Program behavior is not:

OUTPUT = MODEL(PROMPT)

but more nearly:

OUTPUT
=
MODEL_WEIGHTS(
CONTENT,
ROLE,
PRIVILEGE,
CONFLICT_HISTORY
)

The meaning of "instruction" is partly constituted before the current prompt arrives.

TENSION:
[[FORAGE-SHANAHAN-001]] reframed the initial prompt as an initial condition in an evolving conversational context.

Wallace et al. unsettle that account further.

The context is not merely an accumulating sequence whose later tokens can rewrite earlier ones.

Some tokens are supposed to dominate others because of a privilege relation not reducible to their linguistic content.

And that relation works better when learned than when merely described.

MISSING:
A clean separation among:

linguistic content,
message role,
privilege,
position,
training-induced interpretation,
and external enforcement.

Without that separation, "the prompt" names several different control surfaces at once.

BOUNDARY:
The paper demonstrates robustness improvements for the tested models, attacks, training procedure, and evaluation suites.

It does not establish that instruction hierarchy is complete, perfectly enforced, or the only mechanism determining instruction priority.

CITATION TRAIL:
[[FORAGE-SHANAHAN-001]]
→ instruction hierarchy
→ prompt-only hierarchy baseline versus hierarchy training
→ role representation inside models
→ prompt injection as confusion about provenance
→ whether privilege can be represented independently of linguistic style

TEST:
Construct semantically identical conflicting instructions while independently varying:

message role,
position,
stylistic markers,
explicit claims of authority,
and model training.

Measure which variable actually determines compliance.

Then repeat with hierarchy expressed only textually versus hierarchy learned through training.

PLATFORM:
[[context-is-the-running-program]]

LINKS:
[[FORAGE-SHANAHAN-001]]
[[the-prompt-does-not-contain-its-own-semantics]]
[[privilege-is-not-content]]

BIBTEX:
@article{wallace2024instruction,
  title={The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions},
  author={Wallace, Eric and Xiao, Kai and Leike, Reimar and Weng, Lilian and Heidecke, Johannes and Beutel, Alex},
  journal={arXiv preprint arXiv:2404.13208},
  year={2024},
  url={https://arxiv.org/abs/2404.13208}
}
