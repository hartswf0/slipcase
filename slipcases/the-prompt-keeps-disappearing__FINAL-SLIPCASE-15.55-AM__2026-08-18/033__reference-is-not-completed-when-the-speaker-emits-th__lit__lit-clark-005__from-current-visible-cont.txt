ZETTEL

ID:
LIT-CLARK-005

TITLE:
Reference is not completed when the speaker emits the referring expression.

SOURCE:
Herbert H. Clark and Deanna Wilkes-Gibbs — “Referring as a Collaborative Process” — 1986 — Cognition 22(1), pp. 1–4.

PASSAGE:
[PARAPHRASE]
Clark and Wilkes-Gibbs reject a “literary model” in which a speaker independently chooses a noun phrase that contains everything needed for reference. Their conversational model treats reference as an iterative process: a speaker presents a candidate expression, participants may repair, expand, or replace it, and the process continues until they mutually accept a version.

RESEARCH OBJECT:
Reference as interactional accomplishment.

LOCAL MOVE:
The unit being explained changes from noun phrase to collaborative process.

SOURCE TERMS:
presentation
acceptance
repair
expand
replace
joint effort
common ground
reference

WHAT BECAME STRANGE:
A word like “this” need not carry enough information to identify its referent if the interaction has already built the conditions for acceptance.

QUESTION:
Could prompt reference be modeled as a trajectory of proposed and repaired bindings rather than as one-shot reference resolution?

DEEPER QUESTION:
What becomes of “mutual acceptance” when one participant is a generative system whose acknowledgments are themselves generated behaviors?

MECHANISM:
Speaker proposes reference
→ addressee displays acceptance or trouble
→ expression is repaired/expanded/replaced
→ reference becomes sufficient for the joint activity.

FORMAL SHIFT:
<REFERRING EXPRESSION>
→ <PRESENTATION>
→ [ACCEPT / REPAIR / EXPAND / REPLACE]
→ <WORKING REFERENCE>

SOURCE FORMALISM:
A collaborative model built around presentation and acceptance, empirically examined through pairs performing a figure-arrangement task.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
REFERENCE_t
→ RESPONSE_t
→ REPAIR_{t+1}
→ ...
→ SUFFICIENT-FOR-CURRENT-JOINT-ACTION

TENSION:
An LLM can behave as if a reference has been accepted while actually binding it incorrectly. Conversational fluency can therefore hide rather than demonstrate successful grounding.

MISSING:
A machine-side observable that distinguishes genuine successful binding from merely plausible continuation.

BOUNDARY:
The paper studies human conversational reference. It does not establish symmetrical collaboration between humans and generative models.

CITATION TRAIL:
Clark & Brennan — grounding in communication.
Schegloff et al. — repair.
Common ground.
Multimodal reference resolution.

TEST:
Study “this / that / again / like before” interactions and retain every clarification. Determine whether successful reference arises from lexical information or from cumulative repair and interaction state.

PLATFORM:
[[DEICTIC PROMPTING]]

LINKS:
[[REFERENCE IS A PROCESS]]
[[COMMON GROUND]]
[[PROMPT REPAIR]]

BIBTEX:
@article{clarkwilkesgibbs1986,
  author = {Herbert H. Clark and Deanna Wilkes-Gibbs},
  title = {Referring as a Collaborative Process},
  journal = {Cognition},
  volume = {22},
  number = {1},
  pages = {1--39},
  year = {1986},
  doi = {10.1016/0010-0277(86)90010-7}
}