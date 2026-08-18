ZETTEL

ID:
SHAM-20260817-04

TITLE:
2026-08-17 — The recurring-character hack was a missing control surface before identity persistence became a named control.

SOURCE:
Shambibble interview transcript — 2022-10-22 — 07:43–11:04. Midjourney — “Omni Reference” — current documentation consulted 2026-08-17.

SOURCE URL:
[LOCAL UPLOAD — MJ_Interview 3.wh_shambibble_otter_ai.pdf]
https://docs.midjourney.com/hc/en-us/articles/36285124473997-Omni-Reference

PASSAGE:
[QUOTE — SHAMBIBBLE]
“let me take this other prompt that I have and put that face on this other thing, and boom, there you go. You have a recurring character”

[QUOTE — CURRENT MIDJOURNEY DOCUMENTATION]
“Using an Omni Reference allows you to put characters, objects, vehicles, or non-human creatures from a reference image into your Midjourney creations.”

RESEARCH OBJECT:
A WORKAROUND CAN REVEAL A LATENT USER VARIABLE BEFORE THE INTERFACE NAMES IT.

LOCAL MOVE:
[[MJ-2022-007]] and [[MJ-2022-008]] centered on user-discovered capability. The transcript gives the mechanism: image prompt + generic person label + reuse of job ID/seed/prompt + remastering could stabilize identity enough to create a recurring character. Current Midjourney exposes reference identity as a dedicated control with an explicit weight.

SOURCE TERMS:
“recurring character”
“job ID”
“seed”
“remastered”
“Omni Reference”
“Omni Reference Weight”

WHAT BECAME STRANGE:
The hack was not only a clever prompt. It was an informal attempt to hold one latent property constant while varying the rest of the scene.

QUESTION:
Which repeated community hacks are evidence that a generative interface is missing an explicit state variable?

DEEPER QUESTION:
Can prompt archaeology predict future interface primitives by finding properties users repeatedly simulate through cumbersome prompt-and-state recipes?

MECHANISM:
User identifies property P to preserve. Existing interface lacks direct P control. User composes available features to approximate P persistence across generations. Later interface exposes P-like reference control directly.

FORMAL SHIFT:
PROMPT RECIPE
→ SIMULATED STATE PERSISTENCE
→ DEDICATED REFERENCE CONTROL

SOURCE FORMALISM:
Midjourney’s current Omni Reference provides a dedicated reference input and `--ow` weight for controlling how much detail from a reference image appears in new images.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

A workaround is a candidate specification for a missing control surface when users repeatedly expend effort to conserve the same variable across otherwise changing generations.

TENSION:
The modern feature does not establish that the 2022 hack caused its creation. Independent product development can converge on the same user need.

MISSING:
Release notes or developer testimony connecting specific community recurring-character practices to later Character/Omni Reference design.

BOUNDARY:
FUNCTIONAL CONTINUITY IS NOT GENEALOGICAL PROOF.

CITATION TRAIL:
[[MJ-2022-007]]
→ recurring-character experiment
→ job-ID/seed/remaster composition
→ [[MJ-2022-008]] hack-to-button question
→ current Omni Reference identity control
→ missing variable becomes interface state

TEST:
Mine community archives for cumbersome recipes that repeatedly preserve the same property — identity, pose, style, camera, layout, temporal continuity. Track which later become explicit controls. Measure predictive precision of “repeated workaround → future primitive.”

PLATFORM:
Midjourney
Discord

LINKS:
[[MJ-2022-007]]
[[MJ-2022-008]]
[[SHOT-20260817-02]]
[[SHOT-20260817-03]]

BIBTEX:
@misc{shambibble2022interview,
  title={MJ Interview 3.wh_shambibble},
  year={2022},
  month={10},
  note={Interview transcript, October 22, 2022, 1:26:03}
}
