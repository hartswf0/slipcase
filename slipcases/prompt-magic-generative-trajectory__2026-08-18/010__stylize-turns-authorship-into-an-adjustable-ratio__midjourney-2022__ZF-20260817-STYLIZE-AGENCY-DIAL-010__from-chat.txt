ZETTEL

ID:
ZF-20260817-STYLIZE-AGENCY-DIAL-010

TITLE:
Stylize Turns Authorship into an Adjustable Ratio

SOURCE:
[PRIMARY ARCHIVE] Midjourney Discord / Office Hours research archive supplied by user.
SOURCE URL: local:_RESOURCES/Midjourney_prompt_magic_archive_2022.md

[AUTHORITATIVE TECHNICAL SOURCES] Midjourney, “Stylize” and “Raw.”
https://docs.midjourney.com/hc/en-us/articles/32196176868109-Stylize
https://docs.midjourney.com/hc/en-us/articles/32634113811853-Raw

PASSAGE:
[QUOTE — PRIMARY ARCHIVE] At the historical maximum stylize setting: “Hands off the wheels, who knows what will happen. It may look nothing like your prompt.”

RESEARCH OBJECT:
The question “Who made the image?” becomes unexpectedly concrete when the interface contains a numerical control for how strongly the system should impose its own aesthetic behavior.

Stylize is not merely an aesthetic setting.

It is an agency allocation mechanism.

The user can deliberately ask the model to become less obedient.

LOCAL MOVE:
Replace the binary:

HUMAN AUTHOR
versus
MACHINE AUTHOR

with an interface-level variable:

DEGREE OF DELEGATED AESTHETIC AUTHORITY.

SOURCE TERMS:
stylize
artistic
less strict
take over
hands off the wheels
Raw
creative touch
prompt adherence

WHAT BECAME STRANGE:
Authorship becomes parameterized.

The practitioner can intentionally choose:

FOLLOW ME MORE

or:

SURPRISE ME MORE.

This makes surrender itself potentially intentional.

The paradox:

LESS CONTROL
can be
A CHOSEN CREATIVE CONTROL.

QUESTION:
When an artist deliberately increases a parameter whose purpose is to let the system drift away from their text, has the resulting deviation escaped their intention or fulfilled it?

DEEPER QUESTION:
Can intentionality include intentionally creating conditions under which one will encounter outcomes one did not and could not intend in detail?

MECHANISM:
Prompt
+ stylization setting
→ altered balance between textual constraint and model-default aesthetic behavior
→ candidate
→ human evaluation.

FORMAL SHIFT:
AUTHORSHIP = SOURCE OF IMAGE CONTENT

becomes:

AUTHORSHIP =
CHOICE OF HOW MUCH DETAIL TO CONTROL
+
CHOICE OF HOW MUCH DETAIL TO DELEGATE
+
RESPONSE TO WHAT RETURNS.

SOURCE FORMALISM:
[PARAPHRASE] Midjourney’s documentation describes Stylize as controlling the degree of artistic flair applied by the model; Raw mode reduces automatic stylistic intervention and can increase user control over a detailed stylistic prompt.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

C_h = human textual constraint
A_m = model aesthetic prior
λ = delegated stylization strength

Then approximately:

OUTPUT ~ G(C_h, λA_m)

Increasing λ does not simply decrease authorship.

It changes the locus of the human act from:

SPECIFY CONTENT

toward:

SPECIFY A DEGREE OF NON-SPECIFICATION.

TENSION:
One theory says:

more control = more authorship.

Another says:

skill can consist in knowing exactly when control destroys possibility.

The archive itself contains both impulses.

MISSING:
A theory of intentional delegation capable of distinguishing:

deliberate openness
from
mere absence of control.

BOUNDARY:
The stylize parameter is not literally a mathematical measure of machine authorship.

It is evidence that the interface exposes a practical continuum between textual adherence and model-led aesthetic behavior.

CITATION TRAIL:
[[ZF-20260817-PROMPT-NOT-COMMAND-004]]
→ prompts condition rather than fully determine
→ archive supplies an explicit “hands off the wheels” control
→ intentionality can operate at the level of delegated uncertainty
→ next edge: authorship as governance of possibility rather than specification of outcome

TEST:
Create matched tasks across several stylization levels.

Before each generation, ask practitioners to predict:

desired degree of surprise
acceptable semantic drift
required visual invariants.

Afterward measure whether experts choose stylization levels that more reliably produce outcomes satisfying their declared higher-order constraints.

If so, reduced local control can coexist with greater higher-order intentional control.

PLATFORM:
Midjourney
Stylize
Raw Mode
generative image interfaces

LINKS:
[[ZF-20260817-PROMPT-NOT-COMMAND-004]]
[[DELEGATED-INTENTIONALITY]]
[[CONTROL-OF-NONCONTROL]]
[[GENERATIVE-AUTHORSHIP]]

BIBTEX:
@misc{midjourneyStylize,
  author={{Midjourney}},
  title={Stylize},
  howpublished={Midjourney Documentation},
  url={https://docs.midjourney.com/hc/en-us/articles/32196176868109-Stylize}
}

@misc{midjourneyRaw,
  author={{Midjourney}},
  title={Raw},
  howpublished={Midjourney Documentation},
  url={https://docs.midjourney.com/hc/en-us/articles/32634113811853-Raw}
}
