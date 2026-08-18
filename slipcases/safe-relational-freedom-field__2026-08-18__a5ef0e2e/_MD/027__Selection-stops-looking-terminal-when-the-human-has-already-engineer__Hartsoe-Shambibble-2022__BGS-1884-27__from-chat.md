ZETTEL

ID:
BGS-1884-27

TITLE:
Selection stops looking terminal when the human has already engineered what the machine is allowed to vary

SOURCE:
Shambibble — interview with Watson Hartsoe — October 22, 2022 — 1:04:50–1:07:08. fileciteturn3file0L149-L179

PASSAGE:
[PARAPHRASE]
After finding a way to make Midjourney render very short text, Shambibble describes repeatedly rolling outputs until the words resolve correctly. Once the text stabilizes, continued rolls begin producing different font treatments of those same words. fileciteturn3file0L159-L175

RESEARCH OBJECT:
[[BGS-1884-12]] split compositional selection from terminal selection.

This source reveals a third case:

selection from a deliberately engineered family whose invariant expressive content has already been constrained by the human.

LOCAL MOVE:
The practitioner first forces a difficult invariant—specific text—then samples variation in the remaining dimensions.

SOURCE TERMS:
select
spell it right
rolls
resolving
different ways to render
horror font
spins

WHAT BECAME STRANGE:
“Choose one of several complete outputs” sounds like terminal selection only if the candidate set is treated as given.

But the candidate set itself may be the product of sustained human constraint.

QUESTION:
When does selection from generated wholes inherit authorship from the human-authored constraints that produced the candidate family?

DEEPER QUESTION:
Should copyright inspect the selected object alone, or the architecture of the distribution from which it was selected?

MECHANISM:
human fixes invariant:
specific words

generator varies:
typography
texture
shape
stylistic treatment

human samples repeatedly
→ selects preferred realization.

FORMAL SHIFT:
<UNCONSTRAINED WHOLES>
→ <HUMAN-CONSTRAINED FAMILY>
→ [GENERATE VARIANTS]
→ <SELECT MEMBER>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Terminal-selection model:

{W₁,W₂,...Wₙ} → choose Wₖ

Constrained-family model:

Human defines invariant I
and permitted variance V

Generator samples:

Wᵢ ∈ F(I,V)

Then human selects:

F(I,V) → Wₖ

The unresolved question is whether authorship attaches partly to F.

TENSION:
If every individual font treatment is supplied by the generator, the user may still fail to author the selected treatment.

But describing the act as “mere selection” erases the prior work that constructed the family being searched.

MISSING:
A distinction between:

selection over arbitrary outputs

and

selection over a human-shaped generative family.

BOUNDARY:
The interview shows practical constraint and repeated selection. It does not establish that the remaining generated variations are legally attributable to the user.

CITATION TRAIL:
[[BGS-1884-12]]
[[BGS-1884-19]]
→ repeated short-text generation
→ invariant + variable family
→ reconsider terminal selection at the distribution level

TEST:
Create two candidate sets of equal size:

A. randomly generated images later searched for a desired result
B. images sampled from a tightly constrained human-built family

Have evaluators inspect only the final selection, then inspect the production history.

Determine what authorship-relevant difference appears only at the family level.

PLATFORM:
[[Authorship of Candidate Families]]

LINKS:
[[BGS-1884-12]]
[[BGS-1884-19]]
[[Granularity of Choice]]
[[Constrained Search]]
[[Distributional Authorship]]

BIBTEX:
@misc{HartsoeShambibble2022,
  author = {Hartsoe, Watson and Shambibble},
  title = {Interview on Midjourney Prompt Craft},
  year = {2022},
  month = {10},
  note = {Interview conducted October 22, 2022}
}
