ZETTEL

ID:
SHAM-20260817-02

TITLE:
2026-08-17 — The seed is an experimental control, not a memory of an image.

SOURCE:
Shambibble interview transcript — 2022-10-22 — 43:24–44:52. Midjourney — “Seeds” — current documentation consulted 2026-08-17.

SOURCE URL:
[LOCAL UPLOAD — MJ_Interview 3.wh_shambibble_otter_ai.pdf]
https://docs.midjourney.com/hc/en-us/articles/32604356340877-Seeds

PASSAGE:
[QUOTE — SHAMBIBBLE]
“these days, I’m not even if I’m testing something, I’m not satisfied until I run it with the same seed four times.”

[QUOTE — CURRENT MIDJOURNEY DOCUMENTATION]
“Lock a seed when testing different elements in your prompts. It’s like having a control in an experiment.”

RESEARCH OBJECT:
LOCAL REPRODUCIBILITY UNDER STOCHASTIC EXECUTION.

LOCAL MOVE:
[[MJ-2022-004]] proposed same-seed ablation. Shambibble complicates his own method: a single same-seed run had stopped being persuasive enough, so he repeated it four times. Current Midjourney documentation explicitly describes seeds as experimental controls while warning that they should not be relied upon for identical results across prompting sessions.

SOURCE TERMS:
“same seed four times”
“random”
“indeterminate”
“control in an experiment”
“not always predictable”

WHAT BECAME STRANGE:
The seed is not a reproducibility token in the strong software sense. It is a temporary device for reducing one source of variance while other model and session variables remain live.

QUESTION:
What is the minimum experimental record required to make a prompt-effect claim reproducible enough to teach?

DEEPER QUESTION:
Should prompt knowledge be versioned like experimental protocols rather than stored as decontextualized recipes?

MECHANISM:
Hold seed fixed. Repeat multiple generations. Vary one prompt component. Compare distributions rather than one favored output. Record model version and settings.

FORMAL SHIFT:
SAME-SEED ANECDOTE
→ REPEATED SAME-SEED TRIALS
→ LOCAL EFFECT CLAIM
→ VERSION/SESSION BOUNDARY

SOURCE FORMALISM:
Midjourney currently describes seeds as useful for testing and experimentation but cautions that prompts, model versions, settings, and sessions can change outcomes.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

A prompt claim should minimally carry: {model version, prompt, parameters, seed, repetition count, observed effect}.

TENSION:
Stable-looking examples encourage false confidence. Yet demanding full statistical rigor for every creative use would destroy the exploratory practice Shambibble explicitly defends.

MISSING:
Community norms for how many trials count as sufficient evidence for different kinds of prompt claims.

BOUNDARY:
A seed reduces some randomness; it does not isolate every causal variable in generation.

CITATION TRAIL:
[[MJ-2022-004]]
→ same-seed ablation
→ Shambibble raises repetition requirement
→ current seed documentation calls seed an experimental control
→ reproducibility becomes local and versioned

TEST:
For five claimed prompt operators, run 1, 4, 16, and 64 repetitions under fixed seed/settings where supported. Compare whether conclusions based on one image survive distributional sampling. Repeat after a model-version change.

PLATFORM:
Midjourney
Prompt testing

LINKS:
[[MJ-2022-004]]
[[MJ-2022-005]]
[[MJ-2022-009]]
[[SHOT-20260817-07]]

BIBTEX:
@misc{shambibble2022interview,
  title={MJ Interview 3.wh_shambibble},
  year={2022},
  month={10},
  note={Interview transcript, October 22, 2022, 1:26:03}
}
