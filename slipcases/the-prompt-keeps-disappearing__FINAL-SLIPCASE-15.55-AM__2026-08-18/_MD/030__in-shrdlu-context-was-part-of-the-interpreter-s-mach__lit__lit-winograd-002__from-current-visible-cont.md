ZETTEL

ID:
LIT-WINOGRAD-002

TITLE:
In SHRDLU, context was part of the interpreter’s machinery, not extra information appended after linguistic meaning.

SOURCE:
Terry Winograd — “A Procedural Model of Language Understanding” — 1973 — pp. 153, 167ff.

PASSAGE:
[PARAPHRASE]
Winograd rejects analysis of sentences in isolation. Language occurs in a setting comprising the physical situation, discourse topic, prior discourse, participants’ knowledge of the world, and their ideas about one another. SHRDLU therefore maintains both world state and discourse-relevant information.

RESEARCH OBJECT:
Context as computationally active state.

LOCAL MOVE:
“Context” is decomposed into resources used during interpretation rather than treated as an amorphous surrounding background.

SOURCE TERMS:
context
setting
physical situation
topic of discourse
knowledge
world model
current state

WHAT BECAME STRANGE:
“The prompt contains context” and “the prompt occurs in context” are different architectural claims.

QUESTION:
Which parts of contemporary prompt interpretation are carried by the prompt string, which by conversation state, which by interface state, and which by model parameters?

DEEPER QUESTION:
Has the context window collapsed distinctions that earlier systems kept architecturally separate?

MECHANISM:
Current linguistic material is interpreted against prior discourse, represented world state, and procedures/knowledge already available to the system.

FORMAL SHIFT:
<UTTERANCE>
→ <UTTERANCE + DISCOURSE STATE + WORLD STATE + KNOWLEDGE>
→ [INTERPRET]
→ <RESOLVED MEANING / ACTION>

SOURCE FORMALISM:
A maintained symbolic blocks-world database plus procedures and discourse-sensitive interpretation.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
INTERPRET(u) =
f(u, discourse_history, represented_world, procedural_knowledge)

TENSION:
LLM “context” is not straightforwardly the same object. Much relevant structure may be latent in parameters rather than stored as explicit predicates or discourse records.

MISSING:
A vocabulary that distinguishes:
TEXTUAL CONTEXT
INTERACTION STATE
WORLD STATE
MODEL KNOWLEDGE
TOOL STATE
USER-SIDE SITUATION.

BOUNDARY:
Winograd’s architecture does not establish how transformer models interpret context. It shows that context-sensitive computational language interpretation has a much older technical genealogy.

CITATION TRAIL:
Bar-Hillel on indexical expressions.
Winograd — Understanding Natural Language.
Suchman — Plans and Situated Actions.
Clark & Wilkes-Gibbs — collaborative reference.

TEST:
Take one successful multimodal prompt and reconstruct which variables would have required explicit representation in SHRDLU. The residual may identify what contemporary models newly make implicit.

PLATFORM:
[[PROMPT LEANS ON A WORLD]]

LINKS:
[[STATEFUL LANGUAGE]]
[[CONTEXT IS NOT ONE THING]]
[[SHRDLU GENEALOGY]]

BIBTEX:
@incollection{winograd1973procedural,
  author = {Terry Winograd},
  title = {A Procedural Model of Language Understanding},
  booktitle = {Computer Models of Thought and Language},
  editor = {Roger C. Schank and Kenneth M. Colby},
  publisher = {W. H. Freeman},
  address = {San Francisco},
  pages = {152--186},
  year = {1973}
}