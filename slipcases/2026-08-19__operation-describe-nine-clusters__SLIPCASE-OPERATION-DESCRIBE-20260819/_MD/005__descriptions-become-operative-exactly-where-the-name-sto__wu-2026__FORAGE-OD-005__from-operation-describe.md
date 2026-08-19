ZETTEL

ID:
FORAGE-OD-005

TITLE:
DESCRIPTIONS BECOME OPERATIVE EXACTLY WHERE THE NAME STOPS BEING READABLE — CROSS-LINGUAL SELECTION RISES FROM 60% TO 93%

SOURCE:
Zekun Wu et al. — Tool Calling is Linearly Readable and Steerable in Language Models — arXiv:2605.07990 — 2026

PASSAGE:
[QUOTE]
"they also raise cross-lingual classification from 60% to 93%."

RESEARCH OBJECT:
The same paper that shows descriptions add "at most a few points" in the monolingual case shows a 33-point gain when the operator must route across a language boundary.

That is not a contradiction. It is the boundary condition the archive has been unable to state for two years of due-diligence documents.

LOCAL MOVE:
Wu et al. mention the cross-lingual result almost in passing, as evidence that descriptions are "optional for most use cases." They do not notice that they have located the precise condition under which descriptions stop being optional.

SOURCE TERMS:
cross-lingual classification
60% to 93%
short tool descriptions
name-only steering
optional

WHAT BECAME STRANGE:
"When is a description NOT operative?" — the question the archive itself calls the biggest missing due-diligence question — has an answer with a number attached, and the answer is not philosophical.

A description is non-operative when the label already carries the route for that operator. It becomes operative in proportion to the *illegibility of the name to the operator*.

QUESTION:
Can operativity be predicted from a measurable property of the name–operator relation, such as the name's tokenization or its frequency in the operator's training distribution?

DEEPER QUESTION:
If operativity is a function of the operator's prior competence with the label, then operative description is not a theory of language. It is a theory of *unequal legibility* — and its politics is about who gets a legible name.

MECHANISM:
<NAME> legible to operator
→ route already determined
→ description adds ≈ 0
→ ΔG ≈ 0

<NAME> illegible to operator (foreign language, novel API, opaque identifier, internal code)
→ route underdetermined
→ [DESCRIPTION SUPPLIES THE DISCRIMINATION]
→ large ΔG
→ description is the valve

FORMAL SHIFT:
<NAME LEGIBILITY>
→ <ROUTE UNDERDETERMINATION>
→ [DESCRIPTION AS REPAIR]
→ <RECOVERED ROUTE>

SOURCE FORMALISM:
Reported: cross-lingual classification 60% → 93% with short descriptions added; monolingual instruction-tuned 4B+ at 93–100% without descriptions.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Define name legibility for operator O:
  L(name, O) ∈ [0,1]

Conjecture (the Legibility Complement):
  ΔG(description) ≈ k · (1 − L(name, O))

Predictions:
1. ΔG is near zero for high-legibility names.
2. ΔG is maximal for opaque identifiers.
3. ΔG can be *engineered* by degrading the name — which makes the experiment cheap and ethical.

This turns the dissertation's central boundary into a dose–response curve.

TENSION:
This reframing weakens the dissertation's universalist ambition ("natural language is directly compiled into executable machine action") while strengthening its defensibility. The archive must choose which it wants.

It also raises the possibility that thick prompting is *not* a general method but a compensation strategy whose returns collapse as naming improves.

MISSING:
An operationalization of L. Candidates: token count of the name, subword fragmentation, corpus frequency, cross-lingual embedding distance. None are in the archive.

Also missing: the human-side analogue. Is a GitHub label's operativity likewise a complement of its legibility to the contributor?

BOUNDARY:
The 60→93 figure is a single reported result in a single paper on function calling. It supports the *shape* of the conjecture, not its magnitude, and certainly not its transfer to human institutional routing.

CITATION TRAIL:
Cross-lingual transfer in instruction-tuned models.
Bowker & Star, Sorting Things Out — on who gets a legible category.
James C. Scott, Seeing Like a State — legibility as the state's operation (already in the archive as PAPERS/cyber-02.md §6 "Legibility and Metis").
PAPERS/operation-describe-label-00.md §0 (the question this answers).

TEST:
Systematically degrade the name while holding the description fixed: full name → abbreviation → hash → foreign-language name. Measure selection accuracy at each step, with and without description.

If the description's contribution grows monotonically as the name degrades, the Legibility Complement holds and the archive has its boundary condition, with a curve.

PLATFORM:
[[names-route-descriptions-repair]]

LINKS:
[[FORAGE-OD-004]]
[[FORAGE-OD-006]]
[[FORAGE-OD-014]]
[[FORAGE-OD-029]]

BIBTEX:
@article{wu2026toolcalling,
  title={Tool Calling is Linearly Readable and Steerable in Language Models},
  author={Wu, Zekun and Wang, Ze and Cho, Seonglae and Yang, Yufei and Koshiyama, Adriano and Bulathwela, Sahan and Perez-Ortiz, Maria},
  journal={arXiv preprint arXiv:2605.07990},
  year={2026},
  url={https://arxiv.org/abs/2605.07990}
}
