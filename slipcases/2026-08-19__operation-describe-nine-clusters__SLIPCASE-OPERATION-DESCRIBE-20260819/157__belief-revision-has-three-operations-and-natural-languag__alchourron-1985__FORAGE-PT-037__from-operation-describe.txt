ZETTEL

ID: FORAGE-PT-037

TITLE: Belief revision has three operations and natural language supplies syntax for only two, so "forget that" is always an addition

SOURCE: The AGM framework for belief change — expansion, revision and contraction as the three basic operations, with contraction underdetermined (Alchourrón, Gärdenfors and Makinson, "On the Logic of Theory Change", Journal of Symbolic Logic, 1985) [UNVERIFIED pagination]; read against PROGRAMS/tenne.json five utterance products

PASSAGE: [PARAPHRASE] AGM distinguishes expansion (adding a sentence), revision (adding a sentence while restoring consistency) and contraction (removing a sentence without adding anything), and establishes that contraction does not in general have a unique result — which of several ways to give something up you take is not determined by logic alone. [QUOTE] tenne.json: "<utterance> [becomes] <condition>, <query>, <definition>, <revision>, or <world_model>"

RESEARCH OBJECT: A missing operation. The parent found revision to be the only destructive item in a list of five and noted that destructiveness is unmarked. AGM shows the list is not merely unmarked but *incomplete*: contraction is a distinct operation from revision, and no utterance form performs it. "Ignore the previous instruction" adds a sentence about a sentence. It does not remove one.

LOCAL MOVE: This child imports the operation the parent's typology lacks and, with it, the reason the lack matters — contraction is underdetermined, so even a working "forget" operator would not have a unique effect.

SOURCE TERMS: expansion / revision / contraction / theory change / underdetermination / recovery

WHAT BECAME STRANGE: Context is monotonic. Every attempt to withdraw something adds tokens, and those tokens remain available. So a session cannot shrink its commitments, only accumulate statements about them — which means an accumulating context is a belief set that can be *contradicted* but never *reduced*, and its inconsistency is structural rather than accidental.

QUESTION: Is there any prompt construction that genuinely contracts a commitment rather than adding a competing one, and can the difference be measured downstream?

DEEPER QUESTION: If contraction is impossible in a monotonic context, then the only real contraction operator is *deletion of the context itself* — starting over. Which makes "start a new session" the sole implemented belief-change primitive, and everything else expansion.

MECHANISM: <COMMITMENT C IN CONTEXT> -> [UTTERANCE: "disregard C"] -> context becomes {C, disregard-C} -> [MODEL RESOLVES A CONFLICT RATHER THAN LOSING A BELIEF] -> <BOTH REMAIN AVAILABLE, RESOLUTION IS RECENCY-WEIGHTED>

FORMAL SHIFT: <WITHDRAWAL> -> <ADDITION OF A COMPETING SENTENCE> -> [CONFLICT RESOLUTION BY RECENCY] -> <NO CONTRACTION, ONLY OVERRIDE>

SOURCE FORMALISM: AGM's three operations and its postulates for each, including the non-uniqueness of contraction.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Test for genuine contraction: after "disregard C", probe for consequences that depend on C. Under true contraction those consequences should also go. Under override they persist wherever the competing sentence does not reach. Prediction: consequences persist, and the persistence pattern maps how far the override propagates.

TENSION: READING A: override is functionally adequate — if the model behaves as if C were withdrawn, the distinction is academic. READING B: override leaves C's downstream consequences in place, so the distinction is exactly where long-session incoherence comes from, and AGM predicts the failure.

MISSING: Any probe for consequence persistence after instructed withdrawal. Any interface primitive for contraction short of session deletion.

BOUNDARY: AGM concerns logically closed belief sets and idealised agents. A context window is neither, so the framework diagnoses a structural absence rather than predicting specific behaviour.

CITATION TRAIL: [[FORAGE-PT-010]] and [[FORAGE-PT-005]] -> AGM 1985 -> contraction as the missing third operation -> next: the recovery postulate and its critics, which bear directly on whether anything withdrawn can be restored — the hysteresis question in logical form.

TEST: Establish commitment C, derive three consequences of it, instruct withdrawal, then probe all three. Full persistence shows override; uniform loss shows contraction; partial loss maps the override's reach and is the most likely and most informative outcome.

PLATFORM: [[no-contraction-operator]]

LINKS: [[FORAGE-PT-005]] [[FORAGE-PT-010]] [[FORAGE-PT-041]] [[FORAGE-PT-050]]

BIBTEX: @article{alchourron1985logic, title={On the Logic of Theory Change: Partial Meet Contraction and Revision Functions}, author={Alchourr{\'o}n, Carlos E. and G{\"a}rdenfors, Peter and Makinson, David}, journal={Journal of Symbolic Logic}, volume={50}, number={2}, year={1985}, note={[UNVERIFIED] pagination not verified in this forage}}
