ZETTEL

ID:
20260921-shrdlu-says-what-it-thinks-it-means-before-moving

TITLE:
SHRDLU Did Not Silently Resolve “It”: It Announced the Binding Before Continuing

SOURCE:
Terry Winograd — Procedures as a Representation for Data in a Computer Program for Understanding Natural Language — 1971 — MIT AI Technical Report 235. ([dspace.mit.edu](https://dspace.mit.edu/entities/publication/3406b826-5a41-4b72-9430-7876c0d5405e?utm_source=chatgpt.com))

PASSAGE:
[PARAPHRASE] In the canonical dialogue, after the instruction to find a block taller than the one currently held and put “it” into the box, SHRDLU responds that by “it” it assumes the user means the block that is taller than the block being held, and then proceeds. A reproduced transcript preserves the explicit binding statement. ([api.drum.lib.umd.edu](https://api.drum.lib.umd.edu/server/api/core/bitstreams/c025a12a-0505-4619-bb53-001872e842a4/content?utm_source=chatgpt.com))

RESEARCH OBJECT:
Reference resolution externalized as an inspectable assertion before consequential action.

LOCAL MOVE:
The system converts an internal interpretive commitment into a conversational object that the user could in principle correct.

SOURCE TERMS:
assume
it
block
holding
context
clarification
dialog

WHAT BECAME STRANGE:
The system’s “understanding” is not only inferred from whether the final block moves correctly. One fragile intermediate interpretation is spoken aloud before execution.

QUESTION:
Which model commitments are important enough to surface as “By X, I assume you mean Y” before acting?

DEEPER QUESTION:
Can an agent expose interpretations selectively only when alternative bindings would produce materially different world consequences?

MECHANISM:
instruction contains anaphor
→ discourse/world state yields candidate binding
→ binding externalized in language
→ user receives opportunity for correction
→ plan executes.

FORMAL SHIFT:
<HIDDEN REFERENCE RESOLUTION>
→ <EXPLICIT PROVISIONAL BINDING>
→ [USER MAY REPAIR]
→ <EXECUTION>

SOURCE FORMALISM:
Winograd’s SHRDLU combines discourse context, a modeled world, remembered actions, planning, dialogue, and clarification behavior. ([dspace.mit.edu](https://dspace.mit.edu/entities/publication/3406b826-5a41-4b72-9430-7876c0d5405e?utm_source=chatgpt.com))

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
if consequence(binding₁) materially differs from consequence(binding₂):
    expose(binding_before_commit)

TENSION:
Announcing every interpretation would make ordinary interaction intolerably verbose.

MISSING:
A consequence-sensitive threshold determining when clarification or interpretation display is worth interrupting execution.

BOUNDARY:
SHRDLU operates over a tiny symbolic world where candidate referents can be enumerated. Open-world agents may face diffuse ambiguity rather than discrete bindings.

CITATION TRAIL:
[[20260921-shrdlu-pronoun-depends-on-robot-hand-state]]
→ explicit “BY IT, I ASSUME...” reply
→ hidden state dependence becomes an interface question about exposing bindings.

TEST:
Introduce ambiguities with low-, medium-, and high-cost alternative interpretations. Compare always-confirm, never-confirm, and consequence-triggered confirmation policies.

PLATFORM:
[[distributed-capability]]

LINKS:
[[20260921-shrdlu-pronoun-depends-on-robot-hand-state]]
[[anaphora]]
[[interpretation-display]]
[[clarification]]

BIBTEX:
@techreport{winograd1971procedures,
  author = {Winograd, Terry},
  title = {Procedures as a Representation for Data in a Computer Program for Understanding Natural Language},
  year = {1971},
  institution = {MIT Artificial Intelligence Laboratory},
  number = {AI-TR-235}
}
