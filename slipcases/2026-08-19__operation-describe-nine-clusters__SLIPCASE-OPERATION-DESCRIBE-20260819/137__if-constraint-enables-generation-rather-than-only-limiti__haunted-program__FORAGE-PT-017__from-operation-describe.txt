ZETTEL

ID: FORAGE-PT-017

TITLE: If constraint enables generation rather than only limiting it, then removing constraints should *reduce* output variety — which is testable and counterintuitive

SOURCE: PROGRAMS/haunted.json — Haunted Machine Criticism Engine, AXIOM_01 to AXIOM_03, after Italo Calvino

PASSAGE: [QUOTE] "AXIOM_01 := <literature> [is_not] <self_expression_first> <literature> [is] <operation_before_expression>" [QUOTE] "AXIOM_02 := <narrative> [emerges_from] <finite_symbolic_inventory> [under] <rules_of_combination>" [QUOTE] "AXIOM_03 := <constraint> [does_not_merely_limit] <generation> <constraint> [enables] <generation> <constraint> [excludes] <generation>"

RESEARCH OBJECT: The two-sided operation in AXIOM_03. Constraint is asserted to do three things at once — not-merely-limit, enable, exclude — which yields a non-monotonic prediction: variety should be low at zero constraint, peak at some intermediate level, and fall again as exclusion dominates.

LOCAL MOVE: It puts operation before expression, making the finite inventory plus combination rules the primary object and authorial voice a downstream effect.

SOURCE TERMS: operation before expression / finite symbolic inventory / rules of combination / enables / excludes / constraint

WHAT BECAME STRANGE: The folk theory in generative practice is that constraints trade away variety for control — a monotone tradeoff. Calvino's axiom denies the monotonicity. If it is right, an unconstrained generator is not maximally various but maximally *average*: with nothing to push against, it settles into the highest-probability region.

QUESTION: Does output variety peak at intermediate constraint, and where is the peak for a given generator?

DEEPER QUESTION: If the curve is an inverted U, then the same shape governs thick prompting, the six-layer rubric, and Oulipian form — and "how much constraint" becomes one empirical question with one answer per generator rather than a matter of taste.

MECHANISM: <FINITE INVENTORY> + <ZERO CONSTRAINT> -> sampling collapses toward the mode -> low variety; <INVENTORY> + <MODERATE CONSTRAINT> -> forced into low-probability regions that are still licensed -> high variety; <INVENTORY> + <HEAVY CONSTRAINT> -> admissible set shrinks -> low variety

FORMAL SHIFT: <CONSTRAINT COUNT> -> <ADMISSIBLE REGION AND SAMPLING PRESSURE> -> [GENERATE] -> <INVERTED-U VARIETY>

SOURCE FORMALISM: The three axioms; finite inventory plus combination rules as the generative model.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] For constraint count k, variety V(k) = mean pairwise distance among N outputs. Prediction: V has an interior maximum. Folk theory predicts V monotonically decreasing. One sweep distinguishes them.

TENSION: READING A: constraint genuinely enables — the Oulipo evidence is that form produces what freedom does not. READING B: what constraint enables is *surprise to the reader*, not variety in the output set; those are different quantities and the axiom conflates them.

MISSING: Any variety measurement. Any distinction in the theory between variety across outputs and surprise within one output.

BOUNDARY: Calvino argues from literary practice, not from sampling behaviour. The inverted-U is our prediction from his axiom, not his claim.

CITATION TRAIL: Calvino, "Cybernetics and Ghosts," in The Uses of Literature. Oulipo constraint practice. Propp's morphology as a finite inventory with combination rules. [[FORAGE-PT-007]] [[FORAGE-PT-026]]

TEST: Sweep constraint count k = 0,1,2,4,8 on a fixed generation task, N samples each, measure pairwise distance. An interior maximum supports Calvino and gives thick prompting its optimum. Monotone decrease refutes AXIOM_03 as stated for this substrate.

PLATFORM: [[constraint-has-an-optimum]]

LINKS: [[FORAGE-PT-007]] [[FORAGE-PT-016]] [[FORAGE-PT-026]]

BIBTEX: @unpublished{haunted_program, title={Haunted Machine Criticism Engine}, note={PROGRAMS/haunted.json, after Calvino}, year={2026}}
