ZETTEL

ID: FORAGE-PT-010

TITLE: Four of the five things an utterance becomes build structure; one of them changes structure, and prompts do not mark which is which

SOURCE: PROGRAMS/tenne.json — EXECUTABLE_SEMANTICS, source "From Word Models to World Models"

PASSAGE: [QUOTE] "The program must model how <utterance> [becomes] <condition>, <query>, <definition>, <revision>, or <world_model>." [QUOTE] "<LLM> [is] <translator> <probabilistic_program> [is ..." [QUOTE] "<language> [selects-or-builds] <world_model> <world_model> [supports] <inference> <inference> [returns] <belief>, <answer>, <prediction>, <simulation>, or <failure_trace>"

RESEARCH OBJECT: A five-way typology of what an utterance becomes, in which revision is categorically unlike the other four. Condition, query, definition and world_model add to a state. Revision *mutates* an existing state — it is the only destructive operation, and natural language does not mark destructiveness.

LOCAL MOVE: The theory splits translation from inference: the model converts language into program elements, and the program does the reasoning. That relocates competence away from the language surface entirely.

SOURCE TERMS: condition / query / definition / revision / world_model / translator / probabilistic program / failure_trace

WHAT BECAME STRANGE: In every programming language, mutation is syntactically distinguished from declaration. In prompts it is not. "The door is locked" can be a definition (a new fact) or a revision (overwriting that the door was open), and nothing in the utterance says which. Every multi-turn interaction is therefore running unmarked mutations.

QUESTION: Can utterance type be predicted from surface form before execution, or does typing require the prior state?

DEEPER QUESTION: If revision is unmarked, then contradiction in a long interaction is not a model failure — it is an unresolved mutation. That reclassifies a large class of "hallucination" as a state-management bug with a different owner.

MECHANISM: <UTTERANCE> -> [TRANSLATE TO PROGRAM ELEMENT] -> element is additive or destructive -> [EXECUTE AGAINST STATE] -> <BELIEF / ANSWER / PREDICTION / SIMULATION / FAILURE TRACE>

FORMAL SHIFT: <SENTENCE> -> <TYPED PROGRAM ELEMENT> -> [EXECUTION AGAINST STATE] -> <RESULT OR FAILURE TRACE>

SOURCE FORMALISM: The five utterance products; the five inference returns, including failure_trace as a first-class result.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] type: Utterance -> {CONDITION, QUERY, DEFINITION, REVISION, MODEL}. Partition into ADDITIVE = {CONDITION, DEFINITION, MODEL, QUERY} and DESTRUCTIVE = {REVISION}. Predict: error rate rises with the proportion of unmarked DESTRUCTIVE utterances in a session.

TENSION: READING A: typing is recoverable from context, so unmarked mutation is not a real problem. READING B: it is recoverable only if the prior state is unambiguous, which in long interactions it is not — so the ambiguity compounds.

MISSING: Any classifier for the five types. Any measurement of how often revision is misread as definition.

BOUNDARY: The theory is a design proposal for language-to-program pipelines; it does not claim current systems implement this typing.

CITATION TRAIL: Probabilistic programming semantics; belief revision (AGM) as the existing formal treatment of the destructive case. [[FORAGE-PT-004]] [[FORAGE-PT-008]]

TEST: Label 200 turns from real multi-turn sessions with the five types. Measure how often REVISION turns are followed by contradictions. If contradictions cluster after unmarked revisions, a large slice of hallucination is mis-typed mutation.

PLATFORM: [[unmarked-mutation]]

LINKS: [[FORAGE-PT-008]] [[FORAGE-PT-004]] [[FORAGE-PT-009]]

BIBTEX: @unpublished{tenne_program, title={EXECUTABLE_SEMANTICS}, note={PROGRAMS/tenne.json, source "From Word Models to World Models"}, year={2026}}
