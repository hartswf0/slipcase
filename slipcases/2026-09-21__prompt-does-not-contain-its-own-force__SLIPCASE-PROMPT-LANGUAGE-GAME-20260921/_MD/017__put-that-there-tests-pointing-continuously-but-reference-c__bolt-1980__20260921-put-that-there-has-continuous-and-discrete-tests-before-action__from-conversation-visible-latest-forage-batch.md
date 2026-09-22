ZETTEL

ID:
20260921-put-that-there-has-continuous-and-discrete-tests-before-action

TITLE:
Put-That-There Tests Pointing Continuously but Reference Commitment Discretely

SOURCE:
Richard A. Bolt — “‘Put-that-there’: Voice and gesture at the graphics interface” — 1980 — SIGGRAPH ’80. ([media.mit.edu](https://www.media.mit.edu/speech/papers/1980/bolt_SIGGRAPH80_put-that-there.pdf?utm_source=chatgpt.com))

PASSAGE:
[PARAPHRASE] The system shows a continuously moving white “x” cursor corresponding to pointing position. Separately, when a graphical item is addressed, the interface gives immediate visual feedback concerning the selected item. Location is then sampled at the spoken deictic moment such as “there.” ([media.mit.edu](https://www.media.mit.edu/speech/papers/1980/bolt_SIGGRAPH80_put-that-there.pdf?utm_source=chatgpt.com))

RESEARCH OBJECT:
Multiple feedback channels operating at different temporal granularities inside one apparently simple command.

LOCAL MOVE:
The source distinguishes continuously observable sensor state from discrete semantic commitment.

SOURCE TERMS:
cursor
running visual feedback
pointing
there
addressed
feedback
x,y

WHAT BECAME STRANGE:
There is no single “interpretation moment.” One layer is continuously visible before language arrives; another binding occurs when a deictic token is spoken; another consequence appears only after action.

QUESTION:
Should prompt-system traces distinguish continuously varying evidence from discrete commitment events?

DEEPER QUESTION:
Can correspondence be made easier to debug by showing the exact instant at which ambiguous evidence becomes a binding that downstream operations must obey?

MECHANISM:
pointer moves
→ continuous cursor displays sensor estimate

speech unfolds
→ deictic token occurs
→ system samples current cursor
→ discrete coordinate binding committed

object reference resolved
→ selection feedback emitted

routine executes
→ world changes.

FORMAL SHIFT:
<ONE PROMPT / ONE RESPONSE>
→ <CONTINUOUS EVIDENCE + DISCRETE BINDINGS + FINAL EFFECT>
→ [COMMIT AT SPECIFIC TIMES]
→ <TEMPORALLY LAYERED INTERACTION>

SOURCE FORMALISM:
Bolt’s system couples continuously sensed pointing with temporally occurring spoken forms and explicit graphical feedback. ([media.mit.edu](https://www.media.mit.edu/speech/papers/1980/bolt_SIGGRAPH80_put-that-there.pdf?utm_source=chatgpt.com))

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
evidence(t) continuous
commitment_k at t_k discrete
effect_{k+1} depends on commitment_k.

TENSION:
LLM inference often lacks an externally observable instant corresponding to semantic commitment; token-by-token decoding may not map cleanly onto stable interpretation events.

MISSING:
Architectures that expose when provisional model interpretations become executor commitments.

BOUNDARY:
Bolt’s multimodal parser has explicit event synchronization. The same temporal structure should not be presumed in transformer inference.

CITATION TRAIL:
[[20260921-desaturation-is-a-micro-test-of-reference-before-world-change]]
→ continuous cursor plus discrete deictic sampling
→ micro-tests divide further into evidence visualization and commitment visualization.

TEST:
Build a gesture-plus-language builder that records a time-aligned stream of hand pose, recognized words, provisional referents, committed bindings, and world operations. Inject errors at each time layer.

PLATFORM:
[[working-definition-of-prompt]]

LINKS:
[[20260921-desaturation-is-a-micro-test-of-reference-before-world-change]]
[[temporal-binding]]
[[micro-test]]
[[commitment]]

BIBTEX:
@inproceedings{bolt1980put,
  author = {Bolt, Richard A.},
  title = {{``Put-that-there'': Voice and Gesture at the Graphics Interface}},
  booktitle = {Proceedings of SIGGRAPH 1980},
  year = {1980},
  pages = {262--270},
  publisher = {ACM},
  doi = {10.1145/800250.807503}
}
