ZETTEL

ID: FORAGE-PG-004

TITLE: Four child theories lack the mandatory Residual Human Theory section — the corpus violates its own registration gate

SOURCE: PROGRAMS/meta.json — <invariants> ("every-child-theory must-have ... residual_human_theory") and REGISTER STEP R1 requirement 7; PROGRAMS/tda.json (ends at FINAL_THEOREM); PROGRAMS/dac.json (ends at FINAL_INVARIANT); PROGRAMS/theory.json (ends at final_law); PROGRAMS/haunted.json (ends at FINAL_INVARIANT)

PASSAGE: [QUOTE meta.json] "<every-child-theory> [must-have] { <CoreThesis>, <entities>, <morphisms>, <states>, <invariants>, <constraints>, <failure_modes>, <change_tests>, <assumption_ledger>, <program_text>, <theory_code_mapping>, <residual_human_theory> }" and registration gate item 7: "<residual_human_theory> is non-empty". [PARAPHRASE] Full-text search of tda.json, dac.json, theory.json, and haunted.json finds no Residual Human Theory section; each ends instead with a final theorem/invariant/law. haunted.json additionally lacks change tests and an assumption ledger. (theory.json names <residual_human_judgment> as an entity but has no section declaring what it cannot formalize.)

RESEARCH OBJECT: A verifiable structural fact: the constitutional requirement that "every theory must state what it cannot do" (CLAUDE.md LAW 5) is unmet by 4 of 19 registered children, and the meta-program's own death condition ("its <invariants> are violated by the corpus itself") is thereby armed.

LOCAL MOVE: Mechanical schema audit of all 19 children against meta's must-have list — doing the CorpusAuditor's job once, since no audit record exists.

SOURCE TERMS: residual_human_theory; registration_gate; LAW 5; no theory claims completeness; must-state what-it-cannot-do

WHAT BECAME STRANGE: The four non-confessing theories are precisely the four that end in triumphant closures ("FINAL_THEOREM", "FINAL_INVARIANT", "final_law"). Where the confession is missing, its place is taken by a proclamation — exactly the rhetorical form the residual section exists to prevent (meta's maintainer_warning: the forbidden move is declaring the program complete).

QUESTION: Were tda, dac, theory, haunted registered before the gate existed (schema drift), or registered through the gate in violation of it (gate never actually run)?

DEEPER QUESTION: Is the residual section performative rather than informative — i.e., does writing "what I cannot formalize" do governance work regardless of content, such that its absence changes how a theory can be wielded (a theory without stated limits invites deployment beyond them)?

MECHANISM: Registration gate as 8-point checklist (R1) that provably did not fire, or fired without enforcement, for at least four files; enforcement depends on the same operator the gate is meant to discipline.

FORMAL SHIFT: From "incompleteness as philosophical humility" to incompleteness-declaration as a required schema field with a validator — which makes humility auditable and its absence a detectable fault.

SOURCE FORMALISM: meta.json invariant list and REGISTER pseudocode; child files' XML-ish section structure.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Let R(c) = 1 if child c contains a non-empty residual section. Corpus compliance = Σ R(c)/19 = 15/19 ≈ 0.79. Under meta's own transition rules this sets corpus state = invariant-violating, which satisfies death condition 2 for the violated theories or (reflexively) for meta. The corpus is thus formally in a state its own state machine names, but which no file acknowledges.

TENSION: Rival reading 1: these four predate the meta-program (schema evolution), so the violation is an unrun migration, not hypocrisy — supported by their divergent top-level formats (haunted.json is not even XML-wrapped; it is bare operator notation with a stray ":contentReference[oaicite:0]{index=0}" generation artifact). Rival reading 2: the violation is meaningful content — the four closures (culture-as-public-world, accountable-design, victory-law, haunted-machine) resist the residual form because each already internalizes limitation into its thesis, making a separate confession feel redundant to their author. Reading 2 is charitable but fails LAW 5's letter.

MISSING: Registration records; a schema validator; residual sections for tda, dac, theory, haunted (each is writable today — the material exists inside their own failure modes).

BOUNDARY: This audit covers section presence, not section quality; the 15 present residual sections vary from deep (mmt, argue) to perfunctory, which the gate's "non-empty" criterion cannot distinguish.

CITATION TRAIL: meta.json invariants → CLAUDE.md Registration Gate table → the four child files' terminal sections → haunted.json's oaicite token (evidence of LLM-assisted generation left in source).

TEST: Write the four missing residual sections and submit each through REGISTER R1; separately, run AUDIT and check it reports the violation. A passing corpus requires either four edits or four retirements; no third option exists under the stated rules.

PLATFORM: Text editing plus an LLM session under PROGRAMS/CLAUDE.md acting as RegistrationGate.

LINKS: [[FORAGE-PG-003]], [[FORAGE-PG-013]], [[FORAGE-PG-001]], [[FORAGE-PG-014]]

BIBTEX: @unpublished{meta2026program, title={META — The Program of Programs}, note={PROGRAMS/meta.json, OPERATION-DESCRIBE repository, unpublished}, year={2026}} @unpublished{tda2026thick, title={Thick Description program theory}, note={PROGRAMS/tda.json, OPERATION-DESCRIBE repository, unpublished}, year={2026}} @unpublished{haunted2026machine, title={Haunted Machine Criticism Engine}, note={PROGRAMS/haunted.json, OPERATION-DESCRIBE repository, unpublished}, year={2026}}
