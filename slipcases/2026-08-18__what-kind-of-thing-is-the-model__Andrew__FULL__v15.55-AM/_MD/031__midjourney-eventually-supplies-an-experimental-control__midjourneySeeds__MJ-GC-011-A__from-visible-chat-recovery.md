ZETTEL

ID:
MJ-GC-011-A

TITLE:
Midjourney eventually supplies an experimental “control,” but then warns that the control itself is unstable.

SOURCE:
Midjourney — “Seeds” — official documentation.
URL: https://docs.midjourney.com/hc/en-us/articles/32604356340877-Seeds

PASSAGE:
[PARAPHRASE]
Midjourney's current documentation explicitly recommends locking a seed when comparing prompt changes because it holds the initial noise starting point more nearly constant. Yet the same documentation warns that seeds may behave unexpectedly across prompting sessions, can lose consistency under small model or setting changes, and should not be treated as a durable way to preserve appearance.

RESEARCH OBJECT:
UNSTABLE-EXPERIMENTAL-CONTROL.

LOCAL MOVE:
[[MJ-GC-011]] attributed prompt superstition partly to difficulty isolating variables.

Midjourney's own later interface contains machinery intended to make variable isolation easier:
the seed.

But this does not simply solve the epistemic problem.

The platform describes a control whose reliability itself has boundaries.

The experimental situation becomes stranger:

the system provides the user with something analogous to a laboratory control,
while warning that the control is not necessarily stable across time, settings, or sessions.

SOURCE TERMS:
“seed”
“testing”
“experimenting”
“control”
“initial”
“random noise”
“not always predictable”
“not always consistent”

WHAT BECAME STRANGE:
The user is asked to perform experiments inside an apparatus whose supposedly fixed background conditions can themselves drift.

This is not ordinary prompt superstition.

It is experimental knowledge under PLATFORM INSTABILITY.

QUESTION:
What kind of causal knowledge can users establish when the mechanism used to hold conditions constant is only locally reliable?

DEEPER QUESTION:
Does prompt engineering require a different epistemology from ordinary reproducible experimentation—one built around temporary invariants rather than durable ones?

MECHANISM:
WITHOUT FIXED SEED:
PROMPT_A
→ NOISE_1
→ OUTPUT_A

PROMPT_B
→ NOISE_2
→ OUTPUT_B

Difference confounds:
PROMPT CHANGE + INITIAL NOISE CHANGE.

WITH FIXED SEED:
PROMPT_A
→ NOISE_S
→ OUTPUT_A

PROMPT_B
→ NOISE_S
→ OUTPUT_B

Prompt difference becomes easier to inspect.

BUT:

MODEL VERSION / SETTINGS / SESSION CONDITIONS
→ seed behavior may shift
→ experimental equivalence degrades.

FORMAL SHIFT:
FROM:
STOCHASTIC SYSTEM
→ impossible variable isolation
→ superstition

TO:
LOCAL CONTROL
→ improved comparison
→ CONTROL DRIFT
→ bounded causal inference.

SOURCE FORMALISM:
Midjourney documents the parameter:

--seed #

with an integer seed value.

[PARAPHRASE]
The seed establishes the initial noise used to begin generation. The documentation recommends locking it for prompt-element testing but explicitly limits its reliability as a consistency mechanism.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Within experimental window W:

CONTROL(seed=S, W) ≈ stable.

Across W₁ → W₂:

CONTROL(seed=S) may not remain invariant.

Therefore:

CAUSAL CLAIM(prompt term)
must include
MODEL_VERSION
SETTINGS
MODE
TIME / SESSION CONDITIONS
and SEED.

TENSION:
The seed makes the interviewee's demand for better experiments more executable.

But current documentation is not evidence that the same experimental affordance or behavior existed in the model version discussed in the interview.

MISSING:
Historical Midjourney documentation establishing exactly how seeds behaved at the date of the interview.

BOUNDARY:
Current V8.X seed behavior must not be projected backward onto earlier Midjourney versions.

CITATION TRAIL:
[[MJ-GC-011]]
→ superstition because variables cannot be isolated
→ official Midjourney seed documentation
→ seed introduced/used as experimental control
→ documentation simultaneously limits reproducibility
→ prompt experimentation becomes bounded experimentalism.

TEST:
For one suspected “magic” term:

1. lock prompt, version, settings, mode, and seed;
2. vary only the term;
3. repeat across multiple seeds;
4. repeat after a new session;
5. repeat after a model-version change.

Classify effects as:
SEED-LOCAL,
SESSION-STABLE,
VERSION-STABLE,
or NON-REPLICATING.

PLATFORM:
Midjourney

LINKS:
[[MJ-GC-011]]
[[MJ-GC-010]]
[[MJ-GC-009]]
[[MJ-GC-013]]

BIBTEX:
@misc{midjourneySeeds,
  author={{Midjourney}},
  title={Seeds},
  howpublished={Midjourney Documentation},
  url={https://docs.midjourney.com/hc/en-us/articles/32604356340877-Seeds},
  urldate={2026-08-17}
}
