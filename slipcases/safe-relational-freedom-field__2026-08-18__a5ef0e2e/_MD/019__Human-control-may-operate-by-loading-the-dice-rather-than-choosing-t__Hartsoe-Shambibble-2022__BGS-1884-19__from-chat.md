ZETTEL

ID:
BGS-1884-19

TITLE:
Human control may operate by loading the dice rather than choosing the result

SOURCE:
Shambibble — interview with Watson Hartsoe — October 22, 2022 — 57:24–1:03:53. fileciteturn3file1L197-L231

PASSAGE:
[QUOTE]
“There’s very few surefire solutions to something in Midjourney, there’s things that will give you—that will load your dice, and give you a better shot at what you want. But there’s very little that will just always always work.” fileciteturn3file1L203-L207

RESEARCH OBJECT:
The practice supplies a form of control that the deterministic vocabulary of “conception → execution” handles badly.

The practitioner does not command a state.

The practitioner changes the odds of states.

LOCAL MOVE:
Shambibble refuses to describe prompt techniques as reliable commands. He treats overlapping, repetition, weighting, and decomposition as interventions that increase the probability of desired outcomes.

SOURCE TERMS:
load your dice
better shot
suresfire solutions
overlapping
weighting
influence
hopefully

WHAT BECAME STRANGE:
[[BGS-1884-13]] asked whether a human could author a possibility space.

This source makes that possibility concrete but stranger:

the human may not even determine the boundary of the possible space.

The human may only deform its probability distribution.

QUESTION:
Can probabilistic steering count as expressive control when the author cannot determine which state will be realized?

DEEPER QUESTION:
Does copyright’s notion of control secretly assume pointwise causation when generative practice actually operates through distributional causation?

MECHANISM:
possible outputs S
→ prompt operation
→ probability mass over S changes
→ sample occurs
→ human evaluates result

The operation changes likelihood without selecting the realized state.

FORMAL SHIFT:
<OUTPUT SPACE>
→ <PROBABILITY DISTRIBUTION>
→ [PROMPT OPERATION SHIFTS PROBABILITIES]
→ <STOCHASTIC REALIZATION>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Before intervention:

P(W | S)

After human operation h:

P(W | S, h)

Authorial effect may therefore be:

ΔP_h(W) =
P(W | S, h) - P(W | S)

rather than:

h → W

TENSION:
[[BGS-1884-13]] preserved the possibility that authorship might reside in controlling a possibility space.

But “loading the dice” is weaker than specifying that space.

The system may still determine every local expressive realization even while the human significantly changes their probabilities.

MISSING:
A distinction between:

probabilistic influence
probabilistic control
constraint
determination
selection

BOUNDARY:
The interview establishes a practitioner’s operational description of Midjourney in 2022. It does not establish how copyright law should classify distributional steering.

CITATION TRAIL:
[[BGS-1884-13]]
[[BGS-1884-18]]
→ Shambibble’s “load your dice”
→ distinguish deterministic control from distributional control
→ test whether legal authorship can attach to distribution-shaping operations

TEST:
Hold the model and seed protocol constant.

For one target feature, compare:

no intervention
prompt term
repeated term
multi-prompt separation
weighting

Run each condition many times.

Measure whether the human operation reliably changes the distribution of the target feature without reliably determining any individual result.

PLATFORM:
[[Distributional Authorship]]

LINKS:
[[BGS-1884-13]]
[[BGS-1884-18]]
[[Authored Possibility Spaces]]
[[Control Semantics]]
[[Probabilistic Steering]]

BIBTEX:
@misc{HartsoeShambibble2022,
  author = {Hartsoe, Watson and Shambibble},
  title = {Interview on Midjourney Prompt Craft},
  year = {2022},
  month = {10},
  note = {Interview conducted October 22, 2022}
}
