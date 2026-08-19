ZETTEL

ID: FORAGE-PT-047

TITLE: Paraphrase sensitivity is already a measurement of carry-over, and it is evidence for the third profile

SOURCE: Robustness-to-paraphrase and prompt-sensitivity results in language-model evaluation — performance varying across semantically equivalent phrasings of the same item [UNVERIFIED for specific studies and effect sizes]; read against [[FORAGE-PT-020]]

PASSAGE: [PARAPHRASE] A recurring finding in evaluation work is that scores change when items are rephrased without altering their content, and that the ranking of systems can move with the phrasing — reported in benchmark-sensitivity and prompt-format studies. [QUOTE] rcp.json: "<concept-possession> [is] <operational-mastery-across-an-indefinite-task-field>"

RESEARCH OBJECT: An existing measurement of the quantity the parent said nobody measures. Carry-over across occasions is what a disposition delivers: if you possess a concept, a rephrasing of the same problem is the same problem. Paraphrase sensitivity is therefore not a robustness nuisance — it is a direct estimate of rho, the correlation of success across presentations of one underlying item.

LOCAL MOVE: This child finds that the corpus's missing measurement has been running for years in a literature that reads its own results as an engineering defect rather than as evidence about possession.

SOURCE TERMS: paraphrase robustness / prompt sensitivity / format sensitivity / benchmark variance / equivalent items

WHAT BECAME STRANGE: Two communities have the same number and opposite interpretations. Evaluation research treats phrasing variance as noise to be averaged away, and reports mean performance. On the possession account the variance *is* the signal, and averaging destroys exactly the quantity that distinguishes a disposition from a sequence of achievements.

QUESTION: What is the item-level success correlation across semantically equivalent paraphrases, reported as a correlation rather than as a mean and a spread?

DEEPER QUESTION: If rho is low while mean accuracy is high, the third profile is instantiated at scale and the field has been reporting the wrong statistic for years. That would mean benchmark leaderboards measure achievement rates and are structurally blind to possession.

MECHANISM: <ITEM I> -> [PRESENTED AS PARAPHRASE p1] -> success or failure ; <SAME I> -> [PARAPHRASE p2] -> success or failure -> [CORRELATE OUTCOMES ACROSS PARAPHRASES OF THE SAME ITEM] -> <rho: high means disposition, low means per-presentation achievement>

FORMAL SHIFT: <MEAN ACCURACY> -> <ITEM-LEVEL CROSS-PARAPHRASE CORRELATION> -> [REPORT rho] -> <POSSESSION VERSUS ACHIEVEMENT DISTINGUISHED>

SOURCE FORMALISM: NONE verified; the paradigms exist but no specific statistic or study is quoted.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] For items i and paraphrases p, let x_ip be success. rho = correlation of x_ip1 with x_ip2 across i. Then: POSSESSOR high mean, high rho; ACHIEVER-WITHOUT-POSSESSION high mean, low rho; BLUFFER low mean, low rho. Existing evaluations report only the mean and therefore cannot separate the first two.

TENSION: READING A: low rho indicates the capacity is not general, so paraphrase variance measures absence of possession. READING B: low rho indicates the *interface* is brittle while the capacity is intact — the model knows the thing and fails to find it under some phrasings, which is a retrieval problem rather than a possession problem.

Reading B has a decisive test: if a hint that does not add information restores performance under the failing paraphrase, the capacity was present and unretrieved.

MISSING: Verified studies and effect sizes. Any evaluation that reports item-level cross-paraphrase correlation. Any hint-restoration condition of the kind Reading B requires.

BOUNDARY: Nothing here establishes any system's profile. It establishes that the discriminating statistic is computable from data already collected and is not reported.

CITATION TRAIL: [[FORAGE-PT-020]] and [[FORAGE-PT-001]] -> paraphrase-robustness literature (retrieve and verify) -> rho as the discriminating statistic -> next: hint-restoration designs, which separate absent capacity from unretrieved capacity.

TEST: Re-analyse any existing multi-paraphrase evaluation at item level and report rho alongside the mean. Then add the hint-restoration arm. High mean with low rho and successful hint restoration would show the field has been measuring achievement while claiming to measure competence.

PLATFORM: [[rho-is-the-missing-statistic]]

LINKS: [[FORAGE-PT-001]] [[FORAGE-PT-020]] [[FORAGE-PT-028]]

BIBTEX: @misc{paraphrase_sensitivity_unverified, title={Paraphrase and prompt-format sensitivity in language-model evaluation}, note={[UNVERIFIED] no specific study or effect size verified in this forage}, year={2026}}
