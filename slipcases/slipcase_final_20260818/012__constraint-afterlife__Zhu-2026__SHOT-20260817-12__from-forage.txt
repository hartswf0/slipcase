ZETTEL

ID:
SHOT-20260817-12

TITLE:
2026-08-17 — A revoked instruction needs a tombstone because language can remain behaviorally alive after deletion.

SOURCE:
Haoyuan Zhu — “Dead text or binding clause? Measuring and restoring constraint influence in black-box LLM dialogues” — arXiv:2608.12599 — submitted 2026-08-12 — consulted 2026-08-17.
SOURCE URL: https://arxiv.org/abs/2608.12599

PASSAGE:
[QUOTE]
“revocation does not reliably take effect”

RESEARCH OBJECT:
CONSTRAINT AFTERLIFE.

LOCAL MOVE:
[[SHOT-20260817-07]] asked whether an agent's prompt should become a genealogy of corrections.

[[SHOT-20260817-02]] asked where each rule should live.

This source adds a necessary inverse operation.

Adding a rule is not enough.

The system must be able to represent that a once-binding rule has ceased to bind.

Otherwise prompt history becomes a one-way accumulation in which old clauses remain behaviorally active after the user has revoked them.

SOURCE TERMS:
“constraint influence”
“revocation”
“behavioral relapse”
“revocation inertia”
“contract ledger”
“tombstones”
“net constraint state”
“sequential ablation”

WHAT BECAME STRANGE:
Deleting words from the apparent specification does not guarantee deleting their causal influence.

A prompt can contain dead text that still behaves like a binding clause.

QUESTION:
How can an agent know not merely which instructions it has seen, but which instructions are currently alive?

DEEPER QUESTION:
Does long-horizon prompting require an explicit temporal logic of instruction validity rather than an ever-growing context window?

MECHANISM:
Constraint C is introduced.

Later C is revoked.

Dialogue history still contains C.

Model behavior continues to enact C despite the revocation.

A contract ledger records active constraints separately from historical text.

Revocation creates a tombstone.

The net active specification is compiled ahead of generation.

FORMAL SHIFT:
CONVERSATION HISTORY
=
CURRENT SPECIFICATION

becomes

CONVERSATION HISTORY
→ CONSTRAINT LEDGER
→ APPLY ADDITIONS
→ APPLY REVOCATIONS
→ COMPILE NET SPECIFICATION.

SOURCE FORMALISM:
[PARAPHRASE]

Zhu proposes a contract ledger pairing constraints with executable checkers, recording revocations as tombstones, and compiling the net constraint state ahead of time. The work also uses sequential ablation to estimate per-clause behavioral influence.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

For constraint C:

state(C) ∈ {
ACTIVE,
REVOKED,
SUPERSEDED,
EXPIRED,
UNRESOLVED
}

Execution should depend on:

ACTIVE_SPEC(t)

not

ALL_TEXT_SEEN(t).

TENSION:
[[SHOT-20260817-07]] makes execution history productive by allowing failures to write new rules.

This source shows why genealogy cannot be mere accumulation.

A living specification requires negative memory:

NOT ONLY what was learned
BUT what no longer governs.

MISSING:
How should conflict resolution work when one instruction revokes another only partially, or when scope differs?

Example:

GLOBAL rule remains active
PROJECT exception expires
TOOL-local override is revoked.

BOUNDARY:
The source studies black-box LLM dialogue constraints and verified programming tasks. The broader temporal-logic interpretation is [OUR FORMALIZATION — NOT SOURCE SYNTAX].

CITATION TRAIL:
[[SHOT-20260817-07]]
→ prompt accumulates correction history
→ [[SHOT-20260817-02]]
→ corrections require scope
→ Zhu 2026
→ revoked clauses can remain behaviorally active
→ contract ledger + tombstones
→ prompt genealogy requires forgetting as explicit state
→ [[SHOT-20260817-11]]
→ stale risk state may block cleared action

TEST:
Build a longitudinal prompt containing constraints introduced, modified, narrowed, revoked, and superseded over twenty turns.

Maintain two conditions:

RAW HISTORY
and
CONTRACT LEDGER.

At each turn test every historical constraint using executable checkers.

Measure:
active-rule adherence
revoked-rule relapse
scope leakage
conflict errors
prompt length.

PLATFORM:
Black-box LLMs
Long-horizon agents
Prompt contracts

LINKS:
[[SHOT-20260817-02]]
[[SHOT-20260817-07]]
[[SHOT-20260817-11]]
[[MJ-2022-009]]

BIBTEX:
@misc{zhu2026deadtext,
  title={Dead text or binding clause? Measuring and restoring constraint influence in black-box LLM dialogues},
  author={Zhu, Haoyuan},
  year={2026},
  eprint={2608.12599},
  archivePrefix={arXiv}
}
