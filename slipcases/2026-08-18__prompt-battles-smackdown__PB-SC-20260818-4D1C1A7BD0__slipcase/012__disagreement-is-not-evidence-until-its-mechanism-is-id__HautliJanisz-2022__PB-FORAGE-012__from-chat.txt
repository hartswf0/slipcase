ZETTEL

ID:
PB-FORAGE-012

TITLE:
Disagreement is not evidence until its mechanism is identified.

SOURCE:
Annette Hautli-Janisz, Ella Schad, and Chris Reed — Disagreement Space in Argument Analysis — 2022 — Proceedings of the 1st Workshop on Perspectivist Approaches to NLP @LREC2022, pp. 1–9.

PASSAGE:
[PARAPHRASE]
Hautli-Janisz and colleagues reject the assumption that subjective annotation should always be aggregated into one gold label. But they also refuse to romanticize every disagreement: their analysis distinguishes annotation errors, fuzziness, and ambiguity as different sources of disagreement.

RESEARCH OBJECT:
[[PB-FORAGE-006]] proposed that judge disagreement might itself be data.

This source forces a correction.

“Disagreement” is still too coarse a research object.

Some disagreement reveals multiple plausible interpretations.

Some reveals fuzzy boundaries.

Some is simply error.

LOCAL MOVE:
Replace:

AGREEMENT versus DISAGREEMENT

with:

WHAT GENERATED THIS DISAGREEMENT?

SOURCE TERMS:
non-aggregated annotation
gold standards
disagreement space
annotation errors
fuzziness
ambiguity
subjective task

WHAT BECAME STRANGE:
A low inter-rater agreement score collapses several incompatible phenomena into one number.

Two judges can disagree because:

one misunderstood the rule
the criterion has a fuzzy boundary
the object genuinely supports competing interpretations
the judges are attending to different objects entirely.

Treating all four as “pluralism” is as destructive as treating all four as “noise.”

QUESTION:
What taxonomy of judge disagreement is specific to Prompt Battles?

DEEPER QUESTION:
Can the battle discover that the FLAG itself is ambiguous by examining the structure of judge disagreement?

MECHANISM:
A judgment difference is observed.

Its rationale is inspected.

The difference is attributed provisionally to a generating mechanism.

Different mechanisms require different responses:

ERROR
→ repair instruction or judgment

FUZZINESS
→ model graded boundary

AMBIGUITY
→ preserve multiple readings.

FORMAL SHIFT:
<JUDGE LABELS>
→ <OBSERVED DISAGREEMENT>
→ [DIAGNOSE DISAGREEMENT MECHANISM]
→ <ERROR / FUZZINESS / AMBIGUITY / OTHER>
→ <DIFFERENT EPISTEMIC RESPONSE>

SOURCE FORMALISM:
The paper structures a “disagreement space” using categories including:

annotation errors
fuzziness
ambiguity.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

For judges i and j:

J_i(x) ≠ J_j(x)

does not itself imply meaningful perspectival difference.

Introduce latent disagreement cause:

D_ij ∈ {
error,
boundary_fuzziness,
interpretive_ambiguity,
criterion_conflict,
unknown
}

The object of analysis becomes:

P(D_ij | rationales, revisions, judge histories)

rather than only inter-rater agreement.

TENSION:
Standardization removes disagreements that may be caused by confusion.

But clarification can also erase legitimate interpretive multiplicity by teaching judges which reading the benchmark designer prefers.

The procedure used to “clean” disagreement can manufacture consensus.

MISSING:
Judge rationales collected before reconciliation.

Without pre-reconciliation explanations, the evidence needed to distinguish error from ambiguity may be destroyed by the consensus process itself.

BOUNDARY:
Hautli-Janisz et al. study argument annotation rather than AI battle judging.

Their disagreement categories should be treated as a starting taxonomy, not automatically transplanted as complete.

CITATION TRAIL:
[[PB-FORAGE-006]]
→ Hautli-Janisz, Schad, and Reed
→ Aroyo and Welty on CrowdTruth
→ perspectivist annotation
→ derive Prompt Battle-specific disagreement mechanisms.

TEST:
For one battle, require every judge to submit:

score
confidence
short rationale
what evidence would reverse the judgment

before seeing other judgments.

Where judges disagree, conduct a second pass after clarification.

Classify each disagreement by what happens:

disappears after factual correction
→ probable error

moves gradually with threshold discussion
→ probable fuzziness

survives complete factual agreement
→ candidate interpretive ambiguity.

Do not aggregate until this classification is complete.

PLATFORM:
[[Disagreement as Research Object]]

LINKS:
[[PB-FORAGE-006]]
[[Disagreement Space]]
[[Judge Rationales]]
[[Ambiguous Flag]]

BIBTEX:
@inproceedings{hautli2022disagreement,
  title={Disagreement Space in Argument Analysis},
  author={Hautli-Janisz, Annette and Schad, Ella and Reed, Chris},
  booktitle={Proceedings of the 1st Workshop on Perspectivist Approaches to NLP @LREC2022},
  pages={1--9},
  year={2022},
  publisher={European Language Resources Association}
}
