ZETTEL

ID: FORAGE-PT-054

TITLE: If cuts are visible only in contrast, then a single apparatus is unauditable by construction and market concentration is an epistemic condition

SOURCE: [[FORAGE-PT-027]] (the cut is unauditable) developed with differential testing as the comparative method; read against PROGRAMS/agential.json and PROGRAMS/memex.json

PASSAGE: [QUOTE] agential.json: "This [hides] the deeper operation: <system> [makes] <worlds_actionable>" [QUOTE] memex.json: "Can a system show not only <what it says>, but <how its path through the record was built>?"

RESEARCH OBJECT: A political consequence of an epistemic limit. The parent established that a cut leaves no trace inside the system that made it, and that the only purchase is contrast between differently-cut systems. It follows that auditability requires plurality of apparatus. Where one apparatus dominates, there is nothing to contrast it against, and its cut becomes invisible not through secrecy but through the absence of an alternative.

LOCAL MOVE: This child derives the parent's method requirement into a structural claim: the precondition for auditing a cut is competition, which makes concentration an epistemic harm distinct from the economic ones usually cited.

SOURCE TERMS: agential cut / hides / worlds actionable / auditable traversal / differential testing / contrast

WHAT BECAME STRANGE: Transparency and plurality are usually treated as separate goods — one about disclosure, one about markets. Under the contrast argument they are the same good. No amount of disclosure by a single system reveals its cut, because disclosure operates within the space the cut constituted. Only a differently-cut system can show what was excluded, which means competition is a *measuring instrument* before it is an economic arrangement.

QUESTION: How many independently-cut apparatuses are needed before the exclusions of any one become visible, and does the answer depend on how correlated their cuts are?

DEEPER QUESTION: If systems are trained on overlapping data with similar policies, they may be *nominally* plural and effectively single-cut. Then apparent competition provides no contrast, and the measurement fails while the market appears healthy. Cut diversity, not vendor count, would be the quantity that matters — and nobody measures it.

MECHANISM: <APPARATUS A CUTS> -> <OPTION SPACE S_A> -> [AUDIT WITHIN S_A: complete and silent about exclusions] ; <APPARATUS B WITH A DIFFERENT CUT> -> <S_B> -> [COMPARE S_A AND S_B] -> symmetric difference names exclusions -> <CUT VISIBLE ONLY IN CONTRAST>. With only A, the final step is unavailable.

FORMAL SHIFT: <SINGLE-SYSTEM AUDIT> -> <DIFFERENTIAL AUDIT ACROSS CUTS> -> [SYMMETRIC DIFFERENCE OF OPTION SPACES] -> <CONCENTRATION AS AN EPISTEMIC LIMIT>

SOURCE FORMALISM: NONE.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] cut_visibility(A) = union over B of |S_A symmetric-difference S_B|, over available alternatives B. With no B, visibility is zero regardless of A's disclosures. Define cut diversity as the expected symmetric difference across an available population — a quantity that can be small even when the vendor count is large.

TENSION: READING A: plurality is necessary for auditing cuts, so concentration is an epistemic harm and competition policy is an epistemic instrument. READING B: a single apparatus can be audited against a *counterfactual* rather than a rival — held-out data, ablated policies, deliberately widened option sets constructed by the auditor. Then internal counterfactual construction substitutes for external plurality, and monopoly is auditable in principle by a sufficiently equipped auditor.

Reading B has a precondition worth naming: the auditor must be able to construct the wider space, which requires access the operator controls.

MISSING: Any measurement of cut diversity across a real population of systems. Any audit that constructs a counterfactual option space rather than sampling the given one.

BOUNDARY: This derives a consequence from the parent's argument. It does not establish that cuts are in fact correlated across current systems, which is the empirical question that decides whether nominal plurality is real.

CITATION TRAIL: [[FORAGE-PT-027]] [[FORAGE-PT-012]] [[FORAGE-PT-046]] -> differential testing -> cut diversity as the operative quantity -> next: whether audit access regimes grant the counterfactual-construction powers Reading B requires.

TEST: Take one identical query set to several systems and record each option space. Compute pairwise symmetric differences. If they are small relative to the plausible space, nominal plurality is providing little contrast and cut diversity is the number to report, not the vendor count.

PLATFORM: [[cut-diversity]]

LINKS: [[FORAGE-PT-012]] [[FORAGE-PT-027]] [[FORAGE-PT-046]] [[FORAGE-PT-039]]

BIBTEX: @unpublished{agential_program, title={Agential Worlds, Cybernetic Cuts}, note={PROGRAMS/agential.json, read against PROGRAMS/memex.json}, year={2026}}
