ZETTEL

ID: FORAGE-PT-044

TITLE: Constraint trades output-set entropy for pointwise surprisal, and Oulipo optimises the second while the folk theory measures the first

SOURCE: PROGRAMS/haunted.json AXIOM_03; the information-theoretic distinction between the entropy of a distribution and the surprisal of an individual outcome [standard, no specific source claimed]

PASSAGE: [QUOTE] haunted.json: "AXIOM_03 := <constraint> [does_not_merely_limit] <generation> <constraint> [enables] <generation> <constraint> [excludes] <generation>"

RESEARCH OBJECT: Two quantities that the parent's tension named informally and that information theory separates exactly. Entropy is a property of the distribution: how varied the set of outputs is. Surprisal is a property of an outcome: how improbable this particular output was. Constraint reduces the first and can raise the second, because it forces sampling into low-probability regions that remain admissible.

LOCAL MOVE: This child gives the parent's unresolved tension a formal separation, converting "variety versus surprise" from a verbal distinction into two measurable quantities with opposite predicted responses.

SOURCE TERMS: constraint / enables / excludes / finite symbolic inventory / rules of combination

WHAT BECAME STRANGE: Both sides of the Calvino debate can now be right simultaneously, and the debate turns out to have been about which quantity to care about. The generative-practice folk theory measures entropy and correctly reports that constraint reduces it. Oulipo cares about surprisal and correctly reports that constraint raises it. Nobody was wrong; the two camps were measuring different things and each thought the other was denying its evidence.

QUESTION: Does surprisal rise monotonically with constraint while entropy falls, and where do the two curves cross for a given generator?

DEEPER QUESTION: If the crossing point is where "interesting" output lives — enough variety to be non-repetitive, enough improbability to be non-obvious — then aesthetic judgements about generated work are estimating a crossing point, and the crossing point is computable. That is either a useful design target or the reduction of taste to a curve intersection, and which it is depends on whether the crossing tracks human preference.

MECHANISM: <ZERO CONSTRAINT> -> sampling near the mode -> high entropy across the set but low surprisal per item -> [ADD CONSTRAINT] -> admissible region excludes the mode -> items become individually improbable while the set narrows -> [HEAVY CONSTRAINT] -> region collapses -> both fall

FORMAL SHIFT: <CONSTRAINT> -> <TWO INFORMATION QUANTITIES> -> [MEASURE BOTH ACROSS A SWEEP] -> <CROSSING POINT>

SOURCE FORMALISM: The three axioms. No information-theoretic apparatus is present in the source.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] For constraint count k: H(k) = entropy over N sampled outputs; S(k) = mean pointwise surprisal of those outputs under the unconstrained distribution. Prediction: H decreasing, S increasing, and the parent's inverted-U in "variety" appears only if variety is operationalised as a product or a threshold on both.

TENSION: READING A: the parent's inverted-U is real once variety is properly defined as requiring both quantities. READING B: there is no inverted-U in either quantity taken alone, and the parent's prediction was an artifact of conflating them — in which case Calvino's axiom is about surprisal only and says nothing about variety at all.

MISSING: Any joint measurement. Any evidence that human preference tracks a crossing point rather than one quantity.

BOUNDARY: These are properties of sampling distributions. Whether they correspond to what Calvino meant by constraint enabling generation is an interpretation the source does not authorise.

CITATION TRAIL: [[FORAGE-PT-017]] -> the entropy/surprisal split -> joint sweep -> next: human preference ratings across the same sweep, which decide whether the crossing point has any aesthetic content.

TEST: Sweep k = 0,1,2,4,8 on one generation task, N samples per level. Compute H(k) and S(k) under a fixed reference model, and collect human interest ratings. If ratings peak near the crossing, the curve has content; if ratings track S alone, constraint is about improbability and variety was never the point.

PLATFORM: [[entropy-against-surprisal]]

LINKS: [[FORAGE-PT-017]] [[FORAGE-PT-031]] [[FORAGE-PT-053]]

BIBTEX: @unpublished{haunted_program, title={Haunted Machine Criticism Engine}, note={PROGRAMS/haunted.json, after Calvino}, year={2026}}
