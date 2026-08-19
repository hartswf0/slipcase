ZETTEL

ID: FORAGE-PG-001

TITLE: The corpus's first law is an ordering constraint on artifacts, and it has a named failure mode

SOURCE: PROGRAMS/meta.json — <Theory Skeleton>.<constraints>, <Failure Description>.PROGRAM_TEXT_WITHOUT_THEORY, NaurianLoop STEP 10; PROGRAMS/theory.json — <invariants>.invariant 01

PASSAGE: [QUOTE meta.json] "<no-program-text-before-theory>" (constraints); "<program_text> [must-not-outrun] <program_theory>" (STEP 10); failure PROGRAM_TEXT_WITHOUT_THEORY: "<pseudocode> or <rule_machine> [is-produced] before <entities>, <morphisms>, <invariants> are settled ... <code> [cannot-be-justified] <code> [cannot-be-safely-modified] <code> [outpaces] <understanding>". [QUOTE theory.json] "<program_text> must not outrun <program_theory>." and "<program_text> is a residue. <documentation> is a residue."

RESEARCH OBJECT: The load-bearing invariant of the whole corpus: a strict partial order on production (theory before text), stated identically in the meta-program and in its Naur-derived child, each with symptom/damage/correction attached.

LOCAL MOVE: Isolate the one invariant that appears in both the governing program and a child program, and check that it satisfies the corpus's own "no invariant without teeth" rule (it does: the failure mode PROGRAM_TEXT_WITHOUT_THEORY is its violation form).

SOURCE TERMS: program_text; program_theory; residue; patch_rot; PROGRAM_TEXT_WITHOUT_THEORY; Naurian Loop STEP 10; <no-program-text-before-theory>

WHAT BECAME STRANGE: The corpus itself is program text (19 JSON files). If theory.json is right that text is "residue," then the entire PROGRAMS/ directory is residue of a theory that lives only in the operator — and the meta-program cannot verify from inside the files whether the ordering constraint was actually honored during their own generation.

QUESTION: Is "text must not outrun theory" checkable from artifacts alone, or only from the temporal process of production?

DEEPER QUESTION: If possession of theory is what makes text alive (theory.json's <living_program> := <program_text> + <team_that_possesses_program_theory>), can a corpus of formalized theories certify its own aliveness, or does every certificate just add more residue?

MECHANISM: Ordering constraint enforced procedurally: the Naurian Loop holds program text until step 10 of 12; the meta-program's GENERATE directive executes steps in sequence and gates the draft at the ExplanationGate before registration.

FORMAL SHIFT: From quality predicate on code ("good code") to a temporal precedence relation between two artifact classes (theory ≺ text), violation of which is detectable as a named pathology (patch_rot, unjustifiable code).

SOURCE FORMALISM: XML-ish operator notation: <entity> [morphism] <entity>; failure triples {symptom, damage, correction}; 12-step loop with staged outputs.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Let G = (A, ≺) be a DAG over artifact events, with t(theory_i) < t(text_i) required for each system i. The invariant is history-dependent: no predicate P(text, theory) on final states decides it, since identical final corpora arise from compliant and non-compliant histories. Compliance is only witnessed by process logs — which the corpus stores as Chronicle entries, making the Chronicle the invariant's real evidence base.

TENSION: meta.json treats the constraint as enforceable ("[hold] <program_text> until Step 10"), but theory.json's own epistemology says theory is tacit possession that artifacts cannot carry — so the enforcement point (an artifact inspection gate) can never observe the thing it guards. Rival reading: the gate is not verification but ritual, valuable because it slows production (compare agential.json requirement 08 "responsible_slowing").

MISSING: Any audit record showing a case where program text was actually rejected for outrunning theory. The corpus defines the failure mode but records no firing of it.

BOUNDARY: Holds for artifacts produced by the Naurian Loop; says nothing about texts produced first and theorized retroactively (which is how several child theories describing pre-existing papers must in fact have been made).

CITATION TRAIL: Naur, "Programming as Theory Building" (1985) → theory.json core_claim → meta.json LAW 1 / constraint set → CLAUDE.md Constitutional LAW 1.

TEST: Take one child theory file, delete its Theory Skeleton, regenerate it from the Program Text section alone, and diff against the original: if the skeleton is recoverable from the text, the text carried the theory (contradicting "residue"); if not, "residue" is confirmed operationally.

PLATFORM: Any LLM session running PROGRAMS/CLAUDE.md as system instruction; diff tooling.

LINKS: [[FORAGE-PG-002]], [[FORAGE-PG-003]], [[FORAGE-PG-004]], [[FORAGE-PG-013]]

BIBTEX: @unpublished{meta2026program, title={META — The Program of Programs}, note={PROGRAMS/meta.json, version 1.0, OPERATION-DESCRIBE repository, unpublished}, year={2026}} @unpublished{theory2026naur, title={NAUR\_EHN\_MUSASHI\_SOFTWARE\_PRACTICE\_ENGINE}, note={PROGRAMS/theory.json, OPERATION-DESCRIBE repository, unpublished}, year={2026}} @article{naur1985programming, author={Naur, Peter}, title={Programming as Theory Building}, journal={Microprocessing and Microprogramming}, volume={15}, number={5}, pages={253--261}, year={1985}}
