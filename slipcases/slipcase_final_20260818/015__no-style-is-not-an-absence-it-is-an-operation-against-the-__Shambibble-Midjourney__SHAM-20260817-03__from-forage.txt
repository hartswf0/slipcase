ZETTEL

ID:
SHAM-20260817-03

TITLE:
2026-08-17 — “No style” is not an absence; it is an operation against the model’s default authorship.

SOURCE:
Shambibble interview transcript — 2022-10-22 — approximately 26:46–28:28. Midjourney — “Raw” and “Stylize” — current documentation consulted 2026-08-17.

SOURCE URL:
[LOCAL UPLOAD — MJ_Interview 3.wh_shambibble_otter_ai.pdf]
https://docs.midjourney.com/hc/en-us/articles/32634113811853-Raw
https://docs.midjourney.com/hc/en-us/articles/32196176868109-Stylize

PASSAGE:
[QUOTE — SHAMBIBBLE]
“I don’t want to train a style, I want to have no style, you know.”

[QUOTE — CURRENT MIDJOURNEY DOCUMENTATION]
“When you switch to Raw, you’re essentially turning off this ‘auto-pilot.’”

RESEARCH OBJECT:
SUPPRESSING MODEL INTERPRETATION IS A POSITIVE CONTROL ACTION.

LOCAL MOVE:
Shambibble’s wish for “no style” is not a demand for blankness. It is a demand to reduce the model’s unsolicited aesthetic prior so that other constraints can become more legible. Current Midjourney exposes this directly through Raw and through Stylize, which adjusts how much interpretive freedom the system takes.

SOURCE TERMS:
“no style”
“Stylize”
“chaos”
“Raw”
“auto-pilot”
“prompt adherence”

WHAT BECAME STRANGE:
The model’s contribution is not neutral background. To call a precise shot, the user may first have to turn down the system’s tendency to make the shot interesting on its own terms.

QUESTION:
What does it mean to ask a generative system not to interpret?

DEEPER QUESTION:
Can “negative authorship” — suppressing default model tendencies — be treated as a general control primitive across image, text, video, and agentic systems?

MECHANISM:
Standard mode contributes model-default aesthetic interpretation. Raw or lower stylization reduces that intervention. User-specified style/details gain relative influence.

FORMAL SHIFT:
PROMPT
+ MODEL HOUSE STYLE
→ OUTPUT

becomes

PROMPT
+ SUPPRESSED HOUSE STYLE
→ MORE USER-DIRECTED OUTPUT

SOURCE FORMALISM:
Midjourney states that Standard mode adds a creative touch and Raw turns off that “auto-pilot”; Stylize controls movement between closer prompt following and freer artistic interpretation.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

CONTROL is partly subtractive.

CALLING THE SHOT = specifying desired features + suppressing unwanted model initiative.

TENSION:
Reducing model interpretation may increase literal fidelity while reducing precisely the productive mismatch and surprise valued elsewhere in the lineage.

MISSING:
A cross-modal account of which defaults can be suppressed: aesthetic style, verbosity, initiative, safety conservatism, camera motion, composition, tone, or planning depth.

BOUNDARY:
Raw does not remove all learned priors or make the system neutral. “No style” is an operational aspiration, not a literal absence of model influence.

CITATION TRAIL:
[[MJ-2022-013]]
→ Shambibble asks for “no style”
→ lower Stylize / higher Chaos as practitioner controls
→ current Raw formalizes suppression of auto-styling
→ user control includes turning model authorship down

TEST:
For one target, generate a matrix across Raw on/off and low/high Stylize. Have raters separately score prompt fidelity, model-recognizable house style, surprise, and usefulness. Test whether suppressing style reveals other constraints without simply reducing quality.

PLATFORM:
Midjourney

LINKS:
[[MJ-2022-013]]
[[SHOT-20260817-01]]
[[SHOT-20260817-09]]

BIBTEX:
@misc{shambibble2022interview,
  title={MJ Interview 3.wh_shambibble},
  year={2022},
  month={10},
  note={Interview transcript, October 22, 2022, 1:26:03}
}
