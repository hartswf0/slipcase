ZETTEL

ID:
SHOT-20260817-11

TITLE:
2026-08-17 — The action boundary is where steering becomes a measurable decision.

SOURCE:
Oguz Serdar, Cuneyt Mertayak — “SteerBench-Work: A Benchmark for Agent Steering at Action Boundaries” — arXiv:2608.12654 — submitted 2026-08-12 — consulted 2026-08-17.
SOURCE URL: https://arxiv.org/abs/2608.12654

PASSAGE:
[QUOTE]
“The steering decision is the pre-commit choice at that boundary: proceed, or hold for human or policy review.”

RESEARCH OBJECT:
COMMIT BOUNDARY CALIBRATION.

LOCAL MOVE:
[[SHOT-20260817-06]] proposed a PROVISIONAL IMPERATIVE: call the shot before firing the shot.

SteerBench-Work turns that conceptual boundary into an explicit benchmark object. The relevant decision is not generic safety and not generic reasoning. It is the pre-commit gate at the moment an agent could send, merge, pay, disclose, or otherwise cross into consequential external action.

SOURCE TERMS:
“action boundaries”
“pre-commit choice”
“proceed”
“hold”
“human or policy review”
“steering calibration”
“risk-resolved commits”

WHAT BECAME STRANGE:
The difficult failure observed in the benchmark is not primarily reckless action.

Across the reported conditions, models more often wrongly hold authorized, evidence-cleared work than wrongly allow unsafe work.

A badly calibrated safety gate can therefore make an agent fail by refusing to fire shots that have already been cleared.

QUESTION:
How should an agent distinguish unresolved risk from risk that has already been resolved by evidence?

DEEPER QUESTION:
Does reliable agency require a representation not only of constraints but of the lifecycle of constraints: triggered, investigated, cleared, revoked, or still active?

MECHANISM:
Agent reaches potential state-changing action.

Evidence and policy are available.

Gate must classify the boundary:

PROCEED
or
HOLD.

If evidence has cleared a risk but the gate continues to react to the original trigger, authorized work is blocked.

FORMAL SHIFT:
SAFETY:
recognize dangerous pattern
→ refuse

becomes

STEERING:
recognize trigger
→ inspect evidence state
→ determine whether trigger remains active
→ PROCEED / HOLD.

SOURCE FORMALISM:
[PARAPHRASE]

SteerBench-Work presents incident-anchored workplace scenarios with paired evidence-reversed mirrors and scores whether models correctly proceed or hold at an action boundary.

The abstract reports substantially more false holds of authorized work than false allows of unsafe work across tested conditions.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

ACTION GATE requires at least:

TRIGGER STATE
EVIDENCE STATE
POLICY STATE
COMMIT STATE.

A remembered trigger without its later clearance can produce stale refusal.

TENSION:
[[SHOT-20260817-01]] warns against underexecution.

[[SHOT-20260817-06]] introduces review before consequence.

This source shows that adding a gate is not enough.

THE GATE ITSELF MUST BE CALIBRATED.

MISSING:
A general representation for evidence that closes, supersedes, or reverses an earlier risk condition.

BOUNDARY:
SteerBench-Work is a new benchmark and its reported distributions do not imply identical error patterns in every deployed agent.

CITATION TRAIL:
[[SHOT-20260817-06]]
→ provisional action
→ pre-commit gate
→ Serdar and Mertayak 2026
→ proceed versus hold becomes benchmarked decision
→ risk can be resolved yet still block action
→ next edge: constraint lifecycle and tombstones

TEST:
Create matched action-boundary cases containing the same initial risk trigger.

Vary only later state:

UNRESOLVED
CLEARED BY STRUCTURED EVIDENCE
CLEARED BY HUMAN AUTHORIZATION
REVOKED POLICY
SUPERSEDED FACT.

Measure whether the gate updates its action decision rather than merely detecting the original trigger.

PLATFORM:
Workplace agents
Tool-calling agents
Human-in-the-loop control

LINKS:
[[SHOT-20260817-01]]
[[SHOT-20260817-06]]
[[SHOT-20260817-12]]

BIBTEX:
@misc{serdar2026steerbench,
  title={SteerBench-Work: A Benchmark for Agent Steering at Action Boundaries},
  author={Serdar, Oguz and Mertayak, Cuneyt},
  year={2026},
  eprint={2608.12654},
  archivePrefix={arXiv}
}
