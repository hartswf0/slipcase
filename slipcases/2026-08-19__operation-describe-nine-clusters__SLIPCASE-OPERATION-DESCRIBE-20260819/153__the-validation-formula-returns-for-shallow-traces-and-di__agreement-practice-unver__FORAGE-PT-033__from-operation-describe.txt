ZETTEL

ID: FORAGE-PT-033

TITLE: The validation formula returns for shallow traces and diverges for deep ones, so it works exactly where it is least needed

SOURCE: Inter-annotator agreement practice in corpus annotation, where reliability coefficients are computed and reported as a precondition for analysis [UNVERIFIED for specific coefficients and thresholds]; read against PROGRAMS/tah.json validation formula and PROGRAMS/tda.json wink ladder

PASSAGE: [PARAPHRASE] Annotation practice reports agreement coefficients and treats low agreement as evidence that a category is not reliably applicable; agreement is routinely high for surface-level labelling and routinely low for tasks requiring inference about intent, irony or stance. [QUOTE] tah.json: "<action> + <trace> + <social_time> + <rival_readings> [produces] <validated_interpretation>"

RESEARCH OBJECT: A predicted inverse relation between the two parents. If thickness is depth of intentional embedding, and if agreement falls as inference about intent deepens, then validation-by-plurality succeeds on depth-0 traces and fails on depth-3 ones. The formula is best satisfied where nothing interpretive is at stake and returns least where thick description is the point.

LOCAL MOVE: This child joins the plurality requirement to the depth measure and derives a prediction neither parent states: agreement is a decreasing function of embedding depth.

SOURCE TERMS: inter-annotator agreement / reliability / category applicability / rival readings / validated interpretation / embedding depth

WHAT BECAME STRANGE: Low agreement is treated in annotation practice as a defect of the *scheme*. On the depth account it may instead be a *signature of the phenomenon*: a genuinely depth-3 act should produce disagreement, because recovering three nested intentions from a trace underdetermines the reading. Disagreement would then be diagnostic of thickness rather than of bad method — which inverts how reliability is read across the social sciences.

QUESTION: Does inter-reader agreement fall monotonically with the intentional depth required by the item, holding scheme and training constant?

DEEPER QUESTION: If it does, then reliability and thickness are in tension by construction, and any method that selects for high agreement systematically selects *against* the thick cases. That would mean quantitative content analysis has been filtering out precisely the material Geertzian description exists to reach.

MECHANISM: <ITEM AT DEPTH n> -> [READERS RECOVER NESTED INTENTIONS] -> each reader's recovery underdetermined at higher n -> [DISAGREEMENT RISES WITH n] -> <RELIABILITY FALLS AS THICKNESS RISES>

FORMAL SHIFT: <ITEM DEPTH> -> <RECOVERY UNDERDETERMINATION> -> [AGREEMENT COEFFICIENT] -> <RELIABILITY AS AN INVERSE MEASURE OF THICKNESS>

SOURCE FORMALISM: Agreement coefficients exist and are standard; no specific coefficient or threshold is quoted here.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Construct items at depths 0-3 within one scheme. Compute agreement per depth. Prediction: alpha(0) > alpha(1) > alpha(2) > alpha(3). If so, then thickness(item) can be estimated *from* disagreement, giving the corpus a thickness measure that requires no depth annotation at all — only multiple readers.

TENSION: READING A: falling agreement indicates a failing scheme and better training or definitions would restore it. READING B: falling agreement indicates real interpretive underdetermination that no scheme can remove, and forcing agreement at depth would mean coercing readers into a convention rather than measuring an act.

Discriminating evidence: does extended training raise agreement at depth 3 as much as at depth 1? If training closes the shallow gap but not the deep one, Reading B holds.

MISSING: Any depth-stratified agreement study. Any verified coefficient values. Any annotation scheme that reports agreement by inferential depth rather than pooled.

BOUNDARY: Annotation practice covers labelling tasks, not ethnographic description. Whether the same relation holds for open-ended interpretation is an extrapolation.

CITATION TRAIL: [[FORAGE-PT-006]] and [[FORAGE-PT-007]] -> agreement practice -> depth-stratified reliability -> next: irony, stance and implicature annotation, where agreement is known to be low and the items are inherently high-depth.

TEST: One scheme, items stratified by depth 0-3, twelve readers, extended training as a second factor. Report agreement by depth and by training. A persistent deep-item gap converts disagreement into a thickness estimator.

PLATFORM: [[disagreement-as-a-thickness-estimator]]

LINKS: [[FORAGE-PT-006]] [[FORAGE-PT-007]] [[FORAGE-PT-032]] [[FORAGE-PT-034]]

BIBTEX: @misc{agreement_practice_unverified, title={Inter-annotator agreement and category reliability in corpus annotation}, note={[UNVERIFIED] no specific coefficient, threshold or study verified in this forage}, year={2026}}
