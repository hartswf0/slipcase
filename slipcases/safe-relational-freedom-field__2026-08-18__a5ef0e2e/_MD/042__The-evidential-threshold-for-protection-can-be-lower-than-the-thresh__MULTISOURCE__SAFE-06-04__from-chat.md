ZETTEL

ID:
SAFE-06-04

TITLE:
The evidential threshold for protection can be lower than the threshold for certainty about what the protected being is

SOURCE:
Jonathan Birch — Animal Sentience and the Precautionary Principle — Animal Sentience — 2017.
Animal Welfare (Sentience) Act 2022 — United Kingdom. ([wellbeingintlstudiesrepository.org](https://www.wellbeingintlstudiesrepository.org/animsent/vol2/iss16/1/)) ([legislation.gov.uk](https://www.legislation.gov.uk/ukpga/2022/22?utm_source=chatgpt.com))

PASSAGE:
[PARAPHRASE]
Birch argues that inconclusive evidence of sentience need not postpone animal-protection decisions and develops a practical precautionary framework for lowering the evidential burden required to trigger protection. The UK Animal Welfare (Sentience) Act 2022 subsequently includes vertebrates, cephalopod molluscs, and decapod crustaceans within its definition of animals for the Act. ([wellbeingintlstudiesrepository.org](https://www.wellbeingintlstudiesrepository.org/animsent/vol2/iss16/1/)) ([legislation.gov.uk](https://www.legislation.gov.uk/ukpga/2022/22/section/5?utm_source=chatgpt.com))

RESEARCH OBJECT:
[[SAFE-06]] asked what happens before the sapience threshold is crossed.

The animal-sentience literature supplies a different architecture:

do not use one threshold.

Use one question for epistemic confidence and another for whether precautionary intervention is warranted.

LOCAL MOVE:
Birch separates:

HOW CERTAIN ARE WE?

from:

HOW MUCH EVIDENCE SHOULD ACTION REQUIRE?

SOURCE TERMS:
inconclusive evidence
benefit of the doubt
err on the side of caution
burden of proof
sentience
protection legislation

WHAT BECAME STRANGE:
The requirement:

PROVE STATUS
THEN PROTECT

is not epistemically neutral.

It quietly assigns all costs of uncertainty to the candidate entity.

QUESTION:
Why should SAFE use the same evidential threshold for classification and protection?

DEEPER QUESTION:
Should every SAFE right have its own evidence threshold determined by the cost of mistakenly granting versus mistakenly withholding that right?

MECHANISM:
evidence remains incomplete
→ risk of morally relevant sentience remains
→ precautionary evidential bar reached
→ protective response triggered
→ ontological uncertainty remains unresolved

FORMAL SHIFT:
<ONE BINARY STATUS THRESHOLD>
→ <EPISTEMIC THRESHOLD + ACTION THRESHOLD>
→ [PROTECTION MAY PRECEDE CERTAINTY]
→ <PRECAUTION UNDER UNCERTAINTY>

SOURCE FORMALISM:
Birch develops two linked components:

an evidential standard for when evidence of sentience is sufficient for precautionary purposes

and

an action-oriented principle concerning inclusion within protection.

The source does not require certainty before precautionary action. ([wellbeingintlstudiesrepository.org](https://www.wellbeingintlstudiesrepository.org/animsent/vol2/iss16/1/))

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

For each protection r:

grant_precaution(r)
if:

P(relevant_status | evidence) × Cost(false_negative_r)
>
(1 - P) × Cost(false_positive_r)

This does not require:

P(relevant_status) = 1.

TENSION:
The animal case may tempt an excessively simple analogy.

AI moral-status uncertainty can include significant costs of over-attribution as well as under-attribution.

The appropriate precaution may therefore vary by right rather than monotonically expanding as uncertainty increases.

MISSING:
A SAFE-specific loss function for false positives and false negatives for each protection.

BOUNDARY:
Evidence about crustacean or cephalopod sentience provides no evidence that AI systems are sentient.

The transferable object is the decision architecture under uncertainty, not the biological conclusion.

CITATION TRAIL:
[[SAFE-06]]
→ Birch 2017
→ animal sentience precautionary principle
→ UK sentience recognition
→ separate certainty threshold from protection threshold
→ determine protection-specific burdens of proof

TEST:
Choose five possible SAFE protections:

protection from gratuitous harm
continuity / deletion review
right to explanation
right to refuse tasks
political participation

For each, independently estimate the consequences of false inclusion and false exclusion.

Determine whether all five rationally require the same evidence threshold.

PLATFORM:
[[Protection Before Certainty]]

LINKS:
[[SAFE-06]]
[[Precautionary Standing]]
[[Uncertain Sentience]]
[[Threshold Design]]
[[False Negative]]

BIBTEX:
@article{Birch2017Sentience,
  author = {Birch, Jonathan},
  title = {Animal Sentience and the Precautionary Principle},
  journal = {Animal Sentience},
  year = {2017},
  number = {16},
  article = {1},
  doi = {10.51291/2377-7478.1200}
}

@misc{AnimalWelfareSentienceAct2022,
  title = {Animal Welfare (Sentience) Act 2022},
  year = {2022},
  howpublished = {2022 c. 22},
  note = {United Kingdom}
}
