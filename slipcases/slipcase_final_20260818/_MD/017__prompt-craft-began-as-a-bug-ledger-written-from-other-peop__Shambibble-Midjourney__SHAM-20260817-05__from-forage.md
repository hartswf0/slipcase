ZETTEL

ID:
SHAM-20260817-05

TITLE:
2026-08-17 — Prompt craft began as a bug ledger written from other people’s failures.

SOURCE:
Shambibble interview transcript — 2022-10-22 — 00:53–01:53 and 12:22–13:45. Anthropic — “Prompt engineering overview” — current documentation consulted 2026-08-17.

SOURCE URL:
[LOCAL UPLOAD — MJ_Interview 3.wh_shambibble_otter_ai.pdf]
https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

PASSAGE:
[QUOTE — SHAMBIBBLE]
“people would like, come to with specific problems. Like, you know, what, why aren’t Why aren’t I getting a photorealistic picture? When I put photorealistic in it enough people ask that I figure Okay, well, I should put that into an FAQ.”

[QUOTE — SHAMBIBBLE]
“it’s fun, I think to just like, sit there and debug things.”

[QUOTE — CURRENT ANTHROPIC DOCUMENTATION]
“A clear definition of the success criteria for your use case” and “Some ways to empirically test against those criteria.”

RESEARCH OBJECT:
PROMPT KNOWLEDGE EMERGES FROM FAILURE TRIAGE.

LOCAL MOVE:
The transcript’s “manual” does not begin as a theory of good prompts. It accretes because users bring concrete failures and recurring questions. The PromptCraft channel functions like a debugging desk. Contemporary prompt guidance formalizes the same orientation by asking practitioners to define success criteria and empirical tests before optimizing wording.

SOURCE TERMS:
“specific problems”
“FAQ”
“debug things”
“success criteria”
“empirically test”

WHAT BECAME STRANGE:
The natural archive of prompt expertise may be a collection of failure cases and repairs, not a style guide of ideal sentences.

QUESTION:
What would prompt engineering look like if every rule had to name the failure class it repairs?

DEEPER QUESTION:
Can a prompt manual be compiled automatically from recurring failure traces while retaining evidence about where each rule does and does not work?

MECHANISM:
User produces failure F. Community diagnoses F. Repair R is tested. Recurrent F justifies documentation. Documentation becomes a reusable rule. Later versions may invalidate R while F may disappear, persist, or change form.

FORMAL SHIFT:
FAILURE
→ DEBUGGING CONVERSATION
→ REPRODUCIBLE REPAIR
→ FAQ/MANUAL
→ VERSIONED RULE

SOURCE FORMALISM:
Shambibble explicitly describes the manual as growing from repeated concrete user problems and the channel as a place to debug. Anthropic’s current guidance assumes success criteria and empirical tests before prompt engineering.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

PROMPT RULE = {failure signature, intervention, evidence, scope, version}.

A rule without its failure signature is folklore.

TENSION:
A failure-led archive can overfit to visible complaints: users may never report silent failures, and communities may document what is easy to notice rather than what matters most.

MISSING:
The original PromptCraft manual and Discord threads would allow reconstruction of the actual sequence by which rules entered the manual.

BOUNDARY:
The interview is strong evidence for Shambibble’s stated practice, not for the behavior of the entire community.

CITATION TRAIL:
[[MJ-2022-004]]
→ prompt ablation
→ [[MJ-2022-005]] bounded empirical knowledge
→ Shambibble manual emerges from repeated failures
→ current eval-first prompt guidance
→ [[SHOT-20260817-07]] failure becomes specification delta

TEST:
Build a prompt manual where each entry must include: failing example, successful repair, counterexample, model/version, date, and retest. Compare its durability across model updates with a conventional advice manual organized by techniques.

PLATFORM:
Midjourney PromptCraft
Claude prompt engineering
Discord

LINKS:
[[MJ-2022-004]]
[[MJ-2022-005]]
[[SHOT-20260817-07]]
[[SHOT-20260817-09]]

BIBTEX:
@misc{shambibble2022interview,
  title={MJ Interview 3.wh_shambibble},
  year={2022},
  month={10},
  note={Interview transcript, October 22, 2022, 1:26:03}
}
