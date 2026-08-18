ZETTEL

ID:
BGS-1884-20

TITLE:
An instruction can create by eliminating futures it never explicitly describes

SOURCE:
Shambibble — interview with Watson Hartsoe — October 22, 2022 — 02:10–04:29. fileciteturn3file2L335-L361

PASSAGE:
[PARAPHRASE]
Shambibble links patent practice to an adversarial habit of asking how language will be misinterpreted. To obtain the color orange without producing fruit, he describes adding exclusions such as “no fruit, no sphere, no circle”: the operative work is partly preventing unwanted interpretations rather than positively describing the desired image. fileciteturn3file2L337-L357

RESEARCH OBJECT:
Specification can operate negatively.

The creator does not need to describe the final state if they can progressively eliminate classes of wrong states.

LOCAL MOVE:
The source reframes prompting from description into adversarial constraint management.

SOURCE TERMS:
misinterpreted
double meanings
orange
fruit
negate
stack it up
no sphere
no circle
how is this gonna be screwed up

WHAT BECAME STRANGE:
Sarony’s authorship was narrated through positive acts:

pose this body
place this costume
arrange this light.

Generative direction often works backward:

not that
not there
not like this
remove that association.

QUESTION:
Can a person originate expression by systematically eliminating expressive alternatives rather than selecting the surviving expression directly?

DEEPER QUESTION:
Is authorship sometimes better represented by the structure of rejected possibilities than by a description of the final work?

MECHANISM:
large interpretation space
→ ambiguous instruction
→ unwanted class appears
→ human identifies failure mode
→ exclusion added
→ possibility space contracts
→ system resolves inside surviving region

FORMAL SHIFT:
<AMBIGUOUS POSSIBILITY SPACE>
→ <OBSERVED FAILURE>
→ [NEGATIVE CONSTRAINT]
→ <REDUCED POSSIBILITY SPACE>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let S₀ be possible realizations.

Human exclusions e₁...eₙ produce:

Sₙ =
S₀
\ E₁
\ E₂
...
\ Eₙ

The human may never specify W.

The human authors:

NOT-W₁
NOT-W₂
NOT-W₃
...

until the surviving region becomes consequentially structured.

TENSION:
Copyright normally asks what expression the claimant contributed.

Negative specification instead produces expression indirectly by removing alternatives.

A sufficiently powerful elimination procedure could strongly determine a result without ever describing its positive form.

MISSING:
A threshold at which pruning becomes expressive determination rather than merely communicating preferences.

BOUNDARY:
The source shows that exclusions altered Midjourney behavior in the practitioner’s experience. It does not show that the surviving details were therefore authored by the person supplying the exclusions.

CITATION TRAIL:
[[BGS-1884-18]]
→ adversarial specification in the Shambibble interview
→ authorship through exclusion
→ compare positive direction with negative constraint systems

TEST:
Attempt to reproduce the same target through two workflows:

A. only positive descriptions
B. begin underspecified and use only exclusions after each failure

Compare how tightly each workflow constrains expressive features of the final distribution.

PLATFORM:
[[Authorship by Elimination]]

LINKS:
[[BGS-1884-18]]
[[Control Semantics]]
[[Negative Specification]]
[[Possibility-Space Pruning]]

BIBTEX:
@misc{HartsoeShambibble2022,
  author = {Hartsoe, Watson and Shambibble},
  title = {Interview on Midjourney Prompt Craft},
  year = {2022},
  month = {10},
  note = {Interview conducted October 22, 2022}
}
