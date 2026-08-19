ZETTEL

ID: FORAGE-PT-001

TITLE: "Indefinite" is the load-bearing word in concept possession, and it makes possession unverifiable by any finite test

SOURCE: PROGRAMS/rcp.json — RYLEAN_CONCEPT_POSSESSION_ENGINE, <CORE_CLAIM> — source: Gilbert Ryle, "Thinking Thoughts and Having Concepts"

PASSAGE: [QUOTE] "<concept> [is-not] <inner-object> ... <concept> [is] <factor-in-use> <concept-possession> [is] <operational-mastery-across-an-indefinite-task-field>" [QUOTE] "Replace the question 'What inner item is present?' with: 'What can the <actor> now do, recognize, infer, explain, correct, and transfer?'"

RESEARCH OBJECT: The word indefinite. Possession is defined over a task field that cannot be enumerated. Every benchmark is finite. Therefore no benchmark can establish concept possession — not because benchmarks are bad but because of the definition.

LOCAL MOVE: Ryle moves the concept out of the head and into a capability profile, replacing an ontological question with an operational one. The theory keeps the operational reading and inherits its unverifiability.

SOURCE TERMS: factor-in-use / concept-possession / operational mastery / indefinite task field / do, recognize, infer, explain, correct, transfer

WHAT BECAME STRANGE: The six verbs are individually testable and their conjunction over an indefinite field is not. So the theory is operational at the item level and metaphysical at the claim level.

QUESTION: Can possession be evidenced by anything other than transfer to task types absent from the training and evaluation distribution?

DEEPER QUESTION: If not, is concept possession an asymptotic property that can only ever be *disconfirmed* — one failed transfer refutes it, no number of successes confirms it?

MECHANISM: <CONCEPT CLAIM> -> [SAMPLE TASKS FROM FIELD] -> success on sample -> [FIELD IS INDEFINITE] -> no generalization licensed -> <POSSESSION UNDECIDED>

FORMAL SHIFT: <INNER ITEM> -> <CAPABILITY PROFILE> -> [OPEN-ENDED TRANSFER] -> <UNFALSIFIABLE-BY-CONFIRMATION CLAIM>

SOURCE FORMALISM: The six-verb battery (do / recognize / infer / explain / correct / transfer) and rcp's own pseudo-program evaluate_concept_possession.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] possession(A,C) iff for all t in T_C: succeeds(A,t), where T_C is not recursively enumerable. Any test set S subset T_C gives only: not-possession if any failure in S; nothing if all succeed.

TENSION: READING A: "indefinite" means unbounded but samplable, so possession is estimable with confidence intervals. READING B: it means not enumerable, so sampling licenses no inference about the unsampled remainder. Ryle's own examples (mastery shown by handling the *unforeseen* case) favour B.

MISSING: Any procedure for constructing genuinely out-of-field tasks. Without it, "transfer" is the sixth verb in name only.

BOUNDARY: This says nothing about whether machines have concepts. It says the criterion as written cannot answer the question in the affirmative for any actor, human included.

CITATION TRAIL: Ryle — "Thinking Thoughts and Having Concepts"; The Concept of Mind on dispositions vs occurrences. Generalization-gap literature. [[FORAGE-PT-020]]

TEST: Build an adversarial transfer battery: task types in a claimed concept family that could not appear in any training or eval corpus (novel notations, invented domains). Score. A single systematic failure decides against possession; success decides nothing — and that asymmetry is the finding.

PLATFORM: [[possession-is-disconfirmable-only]]

LINKS: [[FORAGE-PT-002]] [[FORAGE-PT-004]] [[FORAGE-PT-020]]

BIBTEX: @unpublished{rcp_program, title={RYLEAN_CONCEPT_POSSESSION_ENGINE}, note={PROGRAMS/rcp.json, program theory after Ryle, "Thinking Thoughts and Having Concepts"}, year={2026}}
