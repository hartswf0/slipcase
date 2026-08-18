ZETTEL

ID:
LIT-ACE-011

TITLE:
Attempto makes natural language executable by restricting the language before execution rather than by restricting the world.

SOURCE:
Norbert E. Fuchs and Rolf Schwitter — “Attempto Controlled English (ACE)” — 1996 — arXiv cmp-lg/9603003.
SOURCE URL: https://arxiv.org/abs/cmp-lg/9603003

PASSAGE:
[PARAPHRASE]
Fuchs and Schwitter describe ACE as a controlled natural language in which domain specialists can formulate specifications that the Attempto system translates into discourse representation structures and then into Prolog; the resulting knowledge base can be queried and used for execution, simulation, prototyping, and validation.

RESEARCH OBJECT:
LANGUAGE RESTRICTION AS THE SITE WHERE NATURAL-LANGUAGE SPECIFICATION BUYS EXECUTABILITY.

LOCAL MOVE:
ACE makes the price of executability unusually visible. Instead of accepting unrestricted natural language and resolving ambiguity later, the system constrains the admissible English so that translation into formal representations can be systematic.

SOURCE TERMS:
controlled natural language
specifications
discourse representation structure
Prolog
knowledge base
query
execute
simulation
prototyping
validation

WHAT BECAME STRANGE:
Executable natural language does not require natural language to become code-like everywhere. A system can decide where to pay for precision. SHRDLU largely pays by shrinking the world; ACE pays by shrinking the language.

QUESTION:
Is the history of natural-language programming better described by where formal restriction is placed than by how “natural” its language appears?

DEEPER QUESTION:
What changes when restriction is no longer imposed primarily before execution but can be introduced selectively during interaction?

MECHANISM:
Controlled English specification
→ syntactic/semantic interpretation under restricted grammar
→ discourse representation structure
→ Prolog representation / knowledge base
→ query or execution.

FORMAL SHIFT:
<CONTROLLED ENGLISH>
→ <DRS>
→ [TRANSLATE]
→ <PROLOG / EXECUTABLE KNOWLEDGE BASE>

SOURCE FORMALISM:
[PARAPHRASE]
The Attempto pipeline translates ACE specifications through discourse representation structures into Prolog clauses that support formal querying and execution.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
ACE strategy: reduce ambiguity by constraining LANGUAGE before runtime.
SHRDLU strategy: reduce ambiguity by constraining WORLD and ONTOLOGY.

TENSION:
The comparison can be overstated. SHRDLU also constrains language through its parser and ACE also assumes a domain and interpretation machinery. The distinction is one of where the dominant restriction is made most explicit, not a pure binary.

MISSING:
A comparative matrix measuring restrictions on language, ontology, world state, action space, interpretation method, and runtime repair across systems.

BOUNDARY:
ACE does not demonstrate unrestricted natural-language programming, and its controlled grammar should not be treated as equivalent to contemporary probabilistic language-model interpretation.

CITATION TRAIL:
Winograd 1971/1973 → Attempto Controlled English 1995/1996 → semantic parsing → contemporary LLM agents.

TEST:
Describe one identical task in SHRDLU-style English, ACE, and a contemporary tool-using LLM. Inventory every place where ambiguity is removed or tolerated before a state-changing action becomes legal.

PLATFORM:
[[GENEALOGY OF EXECUTABLE NATURAL LANGUAGE]]

LINKS:
[[LIT-WINOGRAD-001]]
[[LIT-WINOGRAD-002]]
[[PROMPT FELICITY CONDITIONS]]
[[RESTRICTION MIGRATION]]

BIBTEX:
@misc{fuchs1996ace,
  author = {Norbert E. Fuchs and Rolf Schwitter},
  title = {Attempto Controlled English (ACE)},
  year = {1996},
  eprint = {cmp-lg/9603003},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/cmp-lg/9603003}
}