ZETTEL

ID:
Z-RF-20260817-011

TITLE:
ELIZA’s apparent conversational agency can be decomposed into small symbolic operations.

SOURCE:
Joseph Weizenbaum — “ELIZA—A Computer Program for the Study of Natural Language Communication Between Man and Machine” — Communications of the ACM 9(1) — January 1966 — pp. 36–45 — DOI 10.1145/365153.365168.

PASSAGE:
[PARAPHRASE]
ELIZA scans input for keywords, uses those keywords to select decomposition rules, and generates responses through associated reassembly rules. The paper treats keyword identification, minimal context, transformation choice, and responses without keywords as explicit technical problems.

RESEARCH OBJECT:
Conversational plausibility can emerge from an inspectable chain of shallow operations without a corresponding unified conversational understanding.

LOCAL MOVE:
This pushes [[Z-AIACS-012]] beneath the psychological label “interpretive repair” into source machinery that can actually be manipulated.

SOURCE TERMS:
“keywords”
“decomposition rules”
“reassembly rules”
“minimal context”
“transformation”
“script”

WHAT BECAME STRANGE:
The spectator may infer one speaking agent from a sequence assembled by several independent rule-selection operations.

QUESTION:
Which minimal ELIZA mechanisms contribute most strongly to a user’s perception that there is one coherent interlocutor behind the responses?

DEEPER QUESTION:
How little computational continuity is required before human interpretation supplies the rest?

MECHANISM:
input sentence
→ keyword scan
→ keyword precedence
→ select decomposition rule
→ decompose input
→ choose reassembly rule
→ construct response
→ user interprets response as conversational continuation

FORMAL SHIFT:
<USER UTTERANCE>
→ <KEYWORD / RULE REPRESENTATION>
→ [DECOMPOSE + REASSEMBLE]
→ <APPARENT CONVERSATIONAL RESPONSE>

SOURCE FORMALISM:
A keyword indexes associated decomposition and reassembly rules. Decomposition patterns divide the input into components; reassembly rules reuse selected components to construct a reply. Keyword ranking limits which rule family is attempted.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

PERCEIVED_AGENT =
ELIZA_RULE_OUTPUT
+
HUMAN_CONTINUITY_INFERENCE

The research variable is not whether the program “understands.”
It is how changes to rule machinery alter the second term.

TENSION:
[[Z-AIACS-012]] treats machine incoherence as eliciting human repair. ELIZA shows that plausibility is not simply “nonsense versus sense”; it can be engineered locally through keyword choice, minimal-context decomposition, substitutions, and reassembly while global understanding remains absent.

MISSING:
Controlled evidence linking particular ELIZA mechanisms to measured changes in attributed understanding, personality, memory, or intentionality.

BOUNDARY:
Weizenbaum’s implementation demonstrates a symbolic mechanism for ELIZA. It does not prove that contemporary generative dialogue systems produce perceived agency through the same machinery.

CITATION TRAIL:
[[Z-AIACS-012]]
→ Weizenbaum 1966
→ keyword/decomposition/reassembly machinery
→ decompose apparent agency into executable operations
→ experimentally ablate operations and measure interpretation

TEST:
Run matched ELIZA variants with keyword ranking, pronoun transformation, memory behavior, decomposition specificity, or reassembly diversity independently removed. Ask users to rate coherence, understanding, personality, intentionality, and conversational continuity after each variant.

PLATFORM:
[[Meaning Repair]]

LINKS:
[[Z-AIACS-012]]
[[ELIZA]]
[[Agency Attribution]]
[[Interpretive Repair]]
[[Executable Plausibility]]

BIBTEX:
@article{Weizenbaum1966ELIZA,
  author = {Joseph Weizenbaum},
  title = {ELIZA---A Computer Program for the Study of Natural Language Communication Between Man and Machine},
  journal = {Communications of the ACM},
  volume = {9},
  number = {1},
  year = {1966},
  pages = {36--45},
  doi = {10.1145/365153.365168}
}
