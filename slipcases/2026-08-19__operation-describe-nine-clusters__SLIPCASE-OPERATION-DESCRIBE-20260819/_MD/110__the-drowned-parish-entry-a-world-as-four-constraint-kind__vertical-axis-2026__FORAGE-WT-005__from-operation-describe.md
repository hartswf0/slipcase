ZETTEL

ID: FORAGE-WT-005

TITLE: The Drowned Parish entry: a world as four constraint kinds (INVARIANT / COMMITMENT / CULTURAL LOGIC / FAILURE MODE)

SOURCE: worldtext/syntheses/vertical-axis.md — "The Drowned Parish Example", "The Core Argument", "Subject Alignment"

PASSAGE: [QUOTE] "INVARIANT: Fresh water is sacred. Salt water is profane. / INVARIANT: No building may stand taller than the tide-mark. / INVARIANT: The blacksmith works only at low tide (fire and salt don't mix in this theology). / COMMITMENT: Navigation is oral. Maps are forbidden because they 'trap the water.' / CULTURAL LOGIC: Social status is measured by distance from shore. ... / FAILURE MODE: If any generated content introduces a written map, a tall building, or a freshwater well on the beach, the Worldtext is violated."

RESEARCH OBJECT: The minimal worldtext entry format: a world specified not by description but by a stack of typed constraints, each type doing different work — INVARIANT (physical/theological law), COMMITMENT (cultural prohibition with in-world rationale), CULTURAL LOGIC (a status gradient), FAILURE MODE (explicit violation conditions).

LOCAL MOVE: The file replaces the generative-AI norm ("a quaint village nestled in rolling hills") with a spec whose every line forbids something — shifting the unit of worldbuilding from evocation to prohibition, and pre-registering what would count as the generator breaking the world.

SOURCE TERMS: Drowned Parish; INVARIANT; COMMITMENT; CULTURAL LOGIC; FAILURE MODE; residue; Viscosity Trap; instability codes; hostile extraction; "constitutionally governed, self-historicizing, diagnostically instrumented knowledge organism."

WHAT BECAME STRANGE: The FAILURE MODE line makes the world spec self-adjudicating: the entry contains its own test suite. A paragraph of fiction ships with assertions, like code shipping with unit tests.

QUESTION: Do the four constraint kinds have distinct operational semantics (is violating a COMMITMENT weaker than violating an INVARIANT?), or are they rhetorical registers of a single constraint type?

DEEPER QUESTION: The entry claims generated output against it will be "distinctive, constrained, internally coherent, and — crucially — **modifiable**"; is modifiability a property of the constraint *format* (typed, causal-rationale-bearing) rather than of any particular content — i.e., is there a formal criterion for when a world spec is modification-closed?

MECHANISM: Each constraint embeds its own rationale ("fire and salt don't mix in this theology"; maps "trap the water"), which is what makes propagation possible: change the theology and the rationale-bearing constraints self-identify as affected. Rationale-free constraints would be unpropagatable.

FORMAL SHIFT: From world-as-description (renderable) to world-as-constraint-system (checkable): generation becomes constraint satisfaction, and the FAILURE MODE clause turns aesthetic violation into a detectable event.

SOURCE FORMALISM: The four-kind constraint block quoted above is the only formalism; the file also gives the "Instability Codes" table mapping rhetorical markers to diagnoses (e.g. [QUOTE] "'anomaly' | The Vermeer Problem", "'fundamentally flawed' | RAG as knowledge graph, not theory possession") and the Subject Alignment table (WAS/IS subject swap).

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Entry = ⟨I, C, L, F⟩ with I hard constraints (world-inconsistent if violated), C defeasible norms with rationale r(c) linking them to elements of I, L order-inducing functions over entities (status: Entity → ℝ), F decidable violation predicates over generated output. Modifiability(entry) ∝ fraction of constraints carrying rationales that reference other constraints.

TENSION: vertical-axis.md presents the Drowned Parish as proof the method works; worldtext-formal-engine.md §IX admits the propagation it promises cannot yet be automated. The same example is a demo in one file and an open problem in the other. Rival reading of the whole file: its "Counter-Reading" section concedes the piece is itself a performance of the Ritual Loop — persuasion machinery, not measurement.

MISSING: Any second worked example; grammar for the constraint language (what strings are valid INVARIANTs?); precedence rules when INVARIANT and CULTURAL LOGIC conflict; how many constraints a world needs before generation becomes "distinctive."

BOUNDARY: The format targets one audience explicitly — "Generative AI practitioners and simulation architects" who believe "Coherence emerges from scale" — and its claims are calibrated as rhetoric against RAG, not as neutral measurement.

CITATION TRAIL: vertical-axis.md → worldtext-formal-engine.md §IV (Salt Water Test operates on this exact entry) → seven-failure-modes.md Mode 1 (the "quaint village" as Vermeer residue) → cybernetic-ritual-narratology.md (the file's own counter-reading cites the Ritual Loop).

TEST: Generate N continuations against the Drowned Parish block vs. against an untyped prose paraphrase of the same content; count FAILURE MODE violations (written map / tall building / beach well) per condition. The F clause is decidable enough to score by hand.

PLATFORM: Prompt-level; any instruction-following LLM.

LINKS: [[FORAGE-WT-003]], [[FORAGE-WT-004]], [[FORAGE-WT-006]], [[FORAGE-WT-016]]

BIBTEX: @unpublished{vertical-axis-2026, title={The Vertical Axis — Worldtext as Hostile Extraction}, note={worldtext/syntheses/vertical-axis.md, OPERATION-DESCRIBE repository}, year={2026}, month={apr}}
