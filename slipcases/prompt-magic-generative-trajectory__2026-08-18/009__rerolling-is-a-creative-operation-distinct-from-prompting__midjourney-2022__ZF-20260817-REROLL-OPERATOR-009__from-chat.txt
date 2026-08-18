ZETTEL

ID:
ZF-20260817-REROLL-OPERATOR-009

TITLE:
Rerolling Is a Creative Operation Distinct from Prompting

SOURCE:
[PRIMARY ARCHIVE] Midjourney Discord / Office Hours research archive supplied by user.
SOURCE URL: local:_RESOURCES/Midjourney_prompt_magic_archive_2022.md

[AUTHORITATIVE TECHNICAL SOURCE] Midjourney, “Variations.”
https://docs.midjourney.com/hc/en-us/articles/32692978437005-Variations

PASSAGE:
[QUOTE — PRIMARY ARCHIVE] “i find its not so much getting magical prompts as a general prompt and a lot of rolls”

[PARAPHRASE — PRIMARY ARCHIVE] The notes explicitly contrast “magical prompt” production with “V Rolling” and name an accidental, wandering mode of creation.

RESEARCH OBJECT:
Prompt discourse makes language look like the primary creative operation.

The archive gives direct evidence against that assumption.

A practitioner can hold language approximately constant and generate repeatedly until a useful candidate appears.

The creative act then migrates from:

SAYING THE RIGHT THING

toward:

RECOGNIZING THE RIGHT EVENT.

This is not merely inferior prompting.

It is a different control regime.

LOCAL MOVE:
Split:

PROMPT CRAFT

into at least:

SPECIFICATION
SAMPLING
SELECTION
VARIATION
REVISION.

SOURCE TERMS:
roll
V Rolling
variations
wandering
accidental approach
general prompt
exploration

WHAT BECAME STRANGE:
Two practitioners can submit the same prompt and perform radically different amounts of creative work afterward.

A prompt-only account would treat them as equivalent.

A sampling account cannot.

One generates four candidates and stops.
Another generates 400, recognizes a rare anomaly, branches it through variations, rejects 397 outputs, and develops three survivors.

Their textual input may be identical.

Their practice is not.

QUESTION:
Is the prompt really the principal unit of generative authorship, or merely the initialization of a longer search process?

DEEPER QUESTION:
When model outputs are underdetermined, does artistic expertise move from the ability to specify a desired artifact toward the ability to perceive valuable events inside a distribution?

MECHANISM:
GENERAL PROMPT
→ SAMPLE
→ INSPECT
→ REJECT
→ SAMPLE
→ NOTICE ANOMALY
→ VARIATE
→ INSPECT
→ SELECT
→ CONTINUE.

The artist controls the trajectory through acceptance and rejection even when individual image details were not specified in advance.

FORMAL SHIFT:
DESCRIPTION
→ IMAGE

becomes:

DESCRIPTION
→ DISTRIBUTION
→ SAMPLE
→ JUDGMENT
→ BRANCH
→ NEW SAMPLE
→ JUDGMENT
→ ARTIFACT.

SOURCE FORMALISM:
[PARAPHRASE] Midjourney describes its variation controls as mechanisms for producing different versions of an existing generated image, altering details or broader arrangement.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

p = prompt
G(p) = distribution of candidates
xᵢ ~ G(p)
J(xᵢ) = practitioner evaluation

Prompt-dominant model:

ART ≈ G(p)

Search-dominant model:

x₁...xₙ ~ G(p)

x* = argmax J(xᵢ)

then:

x* → variation distribution → selection → ...

Creative agency can therefore enter strongly through J even when p remains weakly specified.

TENSION:
Rerolling can be described either as:

A. mere lottery-ticket generation

or:

B. trained perception navigating an enormous possibility field.

Both remain plausible until selection skill is experimentally separated from brute-force sample count.

MISSING:
Evidence distinguishing:
good taste
good search strategy
large generation budget
and luck.

A practitioner who finds better outputs after 1,000 rolls may be more skilled, merely richer in compute, or both.

BOUNDARY:
Selection does not eliminate prompting.

A prompt changes the distribution from which selection occurs.

The unresolved issue is relative contribution.

CITATION TRAIL:
[[ZF-20260817-VOCABULARY-GAP-002]]
[[ZF-20260817-PROMPT-NOT-COMMAND-004]]
→ archive explicitly distinguishes magical prompting from rolling
→ generation becomes search rather than one-shot expression
→ next edge: quantify authorship across specification and selection

TEST:
Give expert and novice practitioners:

THE SAME PROMPT
THE SAME MODEL
THE SAME PREGENERATED 1,000 OUTPUTS.

Prevent additional prompting.

Ask each to select 10 candidates worth developing.

Then independently evaluate resulting selections.

If experts consistently identify stronger candidates, selection itself is measurable expertise independent of prompt formulation and generation budget.

PLATFORM:
Midjourney
variations
rerolling
generative search

LINKS:
[[ZF-20260817-VOCABULARY-GAP-002]]
[[ZF-20260817-PROMPT-NOT-COMMAND-004]]
[[SELECTION-AS-AUTHORSHIP]]
[[GENERATIVE-SEARCH]]
[[DEFERRED-FORMALIZATION]]

BIBTEX:
@misc{midjourneyVariations,
  author={{Midjourney}},
  title={Variations},
  howpublished={Midjourney Documentation},
  url={https://docs.midjourney.com/hc/en-us/articles/32692978437005-Variations}
}
