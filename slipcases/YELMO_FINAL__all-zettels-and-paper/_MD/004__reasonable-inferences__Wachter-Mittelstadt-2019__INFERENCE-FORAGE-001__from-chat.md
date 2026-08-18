ZETTEL

ID: INFERENCE-FORAGE-001

TITLE: CONSENT GOVERNS INPUTS BETTER THAN IT GOVERNS WHAT IS INFERRED

SOURCE: Sandra Wachter and Brent Mittelstadt — “A Right to Reasonable Inferences: Re-Thinking Data Protection Law in the Age of Big Data and AI” — Columbia Business Law Review 2019(2), 494–620 — https://journals.library.columbia.edu/index.php/CBLR/article/view/3424

PASSAGE: [PARAPHRASE] Wachter and Mittelstadt argue that people receive comparatively little control or oversight over inferences drawn about them and propose special protections for “high risk inferences,” including ex-ante justification of the data basis, relevance and normative acceptability, and accuracy and statistical reliability, together with an ex-post means of challenge.

RESEARCH OBJECT: The parent notes repeatedly return to the failure of notice and consent: a person may consent to collection of seemingly ordinary data without being able to anticipate the sensitive information later inferred from it. Wachter and Mittelstadt identify a structural reason. Data-protection mechanisms concentrate protection around the input data and its processing, while the derived inference occupies a weaker position.

LOCAL MOVE: Follow the parent’s sequence “give consent → small amount of data can give more information than it seems → once you have consent you can start learning people’s secrets” into the legal architecture of inferential analytics.

SOURCE TERMS: right to reasonable inferences; high risk inferences; ex-ante justification; ex-post challenge; normatively acceptable basis; relevance; accuracy; statistical reliability; inferential analytics

WHAT BECAME STRANGE: [OUR INFERENCE] Consent to an observation and consent to every proposition that can later be computed from that observation are radically different permissions, yet ordinary data-governance mechanisms can collapse them.

QUESTION: What would it mean to govern not merely whether data may be collected, but which conclusions an actor is entitled to derive from it?

DEEPER QUESTION: Can an inference be objectionable even when every datum used to produce it was lawfully acquired, accurate, and individually innocuous?

MECHANISM: Personal data is legitimately collected → analytics combine or transform those data → a predictive or opinion-like inference is produced → inference is used in an important decision → conventional rights that attached strongly to the input data provide weaker leverage over the derived judgment.

FORMAL SHIFT: FROM: PRIVACY = PERMISSION TO COLLECT / PROCESS DATA. TO: INFERENTIAL GOVERNANCE = JUSTIFICATION OF THE TRANSFORMATION FROM DATA TO JUDGMENT AND OF THE JUDGMENT’S USE.

SOURCE FORMALISM: For high-risk inferences, the proposed right requires ex-ante justification addressing: (1) whether the underlying data constitute a normatively acceptable basis; (2) whether the inference is relevant and normatively acceptable for the intended purpose or decision; and (3) whether the data and inferential methods are accurate and statistically reliable. An ex-post mechanism would allow unreasonable inferences to be challenged.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] CONSENT(INPUT) ≠ JUSTIFICATION(INFERENCE); INPUT DATA → INFERENTIAL METHOD → CLAIM ABOUT PERSON → DECISION → HARM / BENEFIT

TENSION: The proposed right strengthens an individual’s ability to contest consequential inferences. But the parent’s final question concerns public harms from biometric inference, including effects on people who never provided the original data. An individual challenge may therefore solve only part of the problem.

MISSING: A theory of inferential harm when the affected party is a population, category, or person whose own data were never collected; institutional machinery for governing such supraindividual effects.

BOUNDARY: The article analyzes the GDPR and related European data-protection doctrine as it stood in 2019 and proposes a new right. The proposal should not be represented as an enacted general legal right, nor does the article specifically resolve biometric group harms.

CITATION TRAIL: [[PARENT-ZETTEL-ID]] → “CONSENT is BROKEN” / uncertainty about what will be learned from ordinary data → Wachter and Mittelstadt’s accountability gap for high-risk inferences → unresolved edge: who can object when inference operates through similarity between people rather than through an individual’s own disclosed data?

TEST: Select one biometric inference pipeline. For every stage, label INPUT DATA, INFERENTIAL METHOD, OUTPUT CLAIM, DECISION, and AFFECTED PARTY. Apply Wachter and Mittelstadt’s three ex-ante justification requirements. Then identify every harm that remains even if all three requirements are satisfied and the directly observed individual successfully exercises every available personal right.

PLATFORM: BIG DATA / AI INFERENTIAL ANALYTICS / DATA PROTECTION LAW

LINKS: [[PARENT-ZETTEL-ID]]

BIBTEX: @article{wachter2019reasonable, author={Wachter, Sandra and Mittelstadt, Brent}, title={A Right to Reasonable Inferences: Re-Thinking Data Protection Law in the Age of Big Data and AI}, journal={Columbia Business Law Review}, volume={2019}, number={2}, pages={494--620}, year={2019}, doi={10.7916/cblr.v2019i2.3424}, url={https://journals.library.columbia.edu/index.php/CBLR/article/view/3424}}
