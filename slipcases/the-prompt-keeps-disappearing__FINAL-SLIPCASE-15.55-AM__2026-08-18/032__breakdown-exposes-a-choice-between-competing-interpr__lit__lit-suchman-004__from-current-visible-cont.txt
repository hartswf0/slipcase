ZETTEL

ID:
LIT-SUCHMAN-004

TITLE:
Breakdown exposes a choice between competing interpretations and therefore supplies information unavailable in smooth interaction.

SOURCE:
Lucy A. Suchman — Plans and Situated Actions: The Problem of Human-Machine Communication — 1985 — pp. 107–108.

PASSAGE:
[PARAPHRASE]
In analyzing trouble in human-machine interaction, Suchman notes that an incoherent or inappropriate response creates an interpretive problem. In human interaction, a producer may treat the response as evidence that the listener misheard or misunderstood, or may treat it as intended; repair then depends on that diagnosis.

RESEARCH OBJECT:
Repair as diagnosis of an interactional mismatch.

LOCAL MOVE:
Failure is decomposed into rival hypotheses about what went wrong.

SOURCE TERMS:
trouble
response
misunderstanding
repair
instruction
human-machine communication

WHAT BECAME STRANGE:
“No, again” is not merely another instruction. It is an implicit diagnosis of the previous interaction.

QUESTION:
What hypothesis about the preceding exchange is encoded by each prompt revision?

DEEPER QUESTION:
Could prompt iteration be studied as repair organization rather than optimization?

MECHANISM:
Unexpected response
→ infer source of trouble
→ choose repair strategy
→ reformulate / repeat / redirect
→ test new interpretation.

FORMAL SHIFT:
<EXPECTED RESPONSE ≠ OBSERVED RESPONSE>
→ <DIAGNOSIS OF TROUBLE>
→ [REPAIR]
→ <REVISED INTERACTION>

SOURCE FORMALISM:
Suchman explicitly distinguishes information available to the user, information available to the machine, observable machine behavior, and the system rationale in her interaction tables.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
FAILURE
→ {misheard?, misunderstood?, wrong reference?, wrong state?, wrong intention?}
→ REPAIR

TENSION:
LLM generations can vary stochastically. Not every bad generation provides a stable diagnostic signal about the system’s interpretation.

MISSING:
A repair taxonomy for prompting that separates:
REPETITION
REFORMULATION
CONTEXT ADDITION
REFERENCE REPAIR
CRITERION REVISION
TOOL/STATE REPAIR.

BOUNDARY:
Suchman does not claim that every breakdown is informative, and her analysis of human repair should not be imported as evidence that a model possesses human conversational understanding.

CITATION TRAIL:
Schegloff, Jefferson & Sacks — repair organization.
Clark & Wilkes-Gibbs.
Conversation analysis.
Interactive machine learning.

TEST:
Code real prompt histories by repair type instead of success/failure. Ask whether certain failures systematically reveal hidden assumptions that successful generations leave unarticulated.

PLATFORM:
[[FAILURE AS METHOD]]

LINKS:
[[PROMPT REPAIR]]
[[FAILED PROMPT AS PROBE]]
[[INTERACTIONAL DEBUGGING]]

BIBTEX:
@techreport{suchman1985plans,
  author = {Lucy A. Suchman},
  title = {Plans and Situated Actions: The Problem of Human-Machine Communication},
  institution = {Xerox Palo Alto Research Center},
  number = {ISL-6},
  address = {Palo Alto, CA},
  month = {February},
  year = {1985}
}