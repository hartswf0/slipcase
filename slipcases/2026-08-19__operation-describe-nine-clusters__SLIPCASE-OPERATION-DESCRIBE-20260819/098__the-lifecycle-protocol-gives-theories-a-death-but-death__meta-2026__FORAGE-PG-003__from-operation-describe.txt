ZETTEL

ID: FORAGE-PG-003

TITLE: The lifecycle protocol gives theories a death, but death is operator-judged while decay is rule-detected

SOURCE: PROGRAMS/meta.json — <Operational Description>.THE LIFECYCLE PROTOCOL; <states>; <Failure Description>.DEAD_LETTER_THEORY; <Residual Human Theory>.irreducible_remainder

PASSAGE: [QUOTE] "<registered_theory> [enters] <theory-decaying> when: - its <source_text> lineage has been superseded - its <core_distinction> has been absorbed by another theory - it has not been deployed in N cycles - its <failure_modes> no longer fire on current artifacts"; "<registered_theory> [enters] <theory-dead> when: - <operator> [judges] it no longer teaches anything that cannot be better taught by another theory in the corpus - its <invariants> are violated by the corpus itself"; and from the remainder: "<whether-a-theory-is-dead-or-dormant> requires lived judgment."

RESEARCH OBJECT: A two-tier mortality model for theories: decay has four mechanical, checkable triggers; death has two triggers of which one is pure operator judgment and the other — "invariants violated by the corpus itself" — is a reflexive condition the corpus can trip on its own.

LOCAL MOVE: Separate the lifecycle's decidable transitions from its judgment-gated transitions and notice that the corpus already satisfies a death condition (see FORAGE-PG-004: four children violate the mandatory-residual invariant, i.e., corpus invariants are violated by the corpus itself).

SOURCE TERMS: theory-decaying; theory-dead; theory-revived; theory-retired; dead-letter; deployment_history; N cycles; DEAD_LETTER_THEORY

WHAT BECAME STRANGE: "Failure modes no longer fire" is a decay trigger — meaning a theory whose diagnostics never find anything is dying, not succeeding. Health is measured by continued firing of pathology detectors. A theory that fixed its domain so well that its failures went extinct would be indistinguishable, in this model, from one that lost contact with its artifacts.

QUESTION: What is N? The decay trigger "not deployed in N cycles" is stated with a free variable that no section binds.

DEEPER QUESTION: Can the death condition "invariants violated by the corpus itself" apply to meta.json? If meta violates its own invariants (it hosts children without residual sections, contra its own must-have list), the rule demands meta enter theory-dead — but only meta defines the lifecycle in which that death would be recorded.

MECHANISM: State machine over {registered, deployed, decaying, dead, revived, retired} with mechanical decay detection (CorpusAuditor, AUDIT directive A1–A3) feeding operator adjudication (keep/deploy/merge/split/retire).

FORMAL SHIFT: From corpus-as-library (texts accumulate) to corpus-as-ecology (theories must be deployed to live, can starve, die, and be revived by new artifacts) — with an explicit immune system (CorpusAuditor "as <the immune system>").

SOURCE FORMALISM: Named states plus transition conditions in operator notation; AUDIT pseudocode classifying dead-letter-risk / decay-risk / redundancy-risk / obsolescence-risk.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Lifecycle = labeled transition system L = (S, Σ_mech ∪ Σ_judg, →). Reachability of <theory-dead> is not decidable within L because one transition's guard is an oracle call (operator). But reachability of <theory-decaying> is decidable given deployment logs; hence the auditable claim "theory X is decaying" is a fact, while "theory X is dead" is a ruling. The corpus conflates these in prose but separates them perfectly in mechanism.

TENSION: DEAD_LETTER_THEORY says an undeployed theory "sits-in-corpus as <decoration>" and must be retired or deployed — yet no deployment_history exists anywhere in the repository for any child, so by the corpus's own audit logic all 19 children are dead-letter risks. Rival reading: deployment happens in live sessions and is simply unrecorded, i.e., the ChronicleWriter module is specified but was never run — which is itself the PROGRAM_TEXT_WITHOUT_THEORY pattern inverted (theory without process).

MISSING: Binding for N; any Chronicle of an actual lifecycle event; criteria distinguishing "dormant" from "dead" beyond the confession that this requires lived judgment.

BOUNDARY: Governs registered theories only; a draft that fails the registration gate has no lifecycle state at all (it is not "dead," it never lived).

CITATION TRAIL: meta.json LIFECYCLE ← AUDIT directive ← CLAUDE.md AUDIT section ("Dead Letters: theories never deployed").

TEST: Execute AUDIT as specified against the actual corpus: expected output flags every child as <dead-letter-risk> (no deployment history) and flags {tda, dac, theory, haunted} for invariant violation (missing residual sections). If an implementation returns "all healthy," it is not implementing A1–A2.

PLATFORM: LLM session under PROGRAMS/CLAUDE.md; file inspection suffices.

LINKS: [[FORAGE-PG-004]], [[FORAGE-PG-001]], [[FORAGE-PG-005]], [[FORAGE-PG-012]]

BIBTEX: @unpublished{meta2026program, title={META — The Program of Programs}, note={PROGRAMS/meta.json, version 1.0, OPERATION-DESCRIBE repository, unpublished}, year={2026}}
