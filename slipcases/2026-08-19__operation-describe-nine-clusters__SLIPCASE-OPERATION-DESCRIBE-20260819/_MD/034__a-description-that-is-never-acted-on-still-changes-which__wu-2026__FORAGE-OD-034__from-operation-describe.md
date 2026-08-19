ZETTEL

ID:
FORAGE-OD-034

TITLE:
A DESCRIPTION THAT IS NEVER ACTED ON STILL CHANGES WHICH OTHER DESCRIPTIONS ROUTE, AND THE ARCHIVE HAS NO CATEGORY FOR IT

SOURCE:
Zekun Wu et al. — arXiv:2605.07990 — 2026 ("one direction per pair of tools"); Chengrui Huang et al. — arXiv:2407.03007 — 2024 (toolset composition and order); against Watson Hartsoe — PAPERS/operation-describe-label-01.md §5 "Unit of Analysis: The Description/Action Pair"

PASSAGE:
[QUOTE]
label-01 §5:
"The unit of analysis is the description/action pair ⟨D, A_route⟩: a specific descriptive token and the route it makes more likely, legitimate, or automatic."

[QUOTE]
Wu et al.:
"a single direction in activation space, one direction per pair of tools"

RESEARCH OBJECT:
If routing is decided pairwise, then adding a tool to a schema changes the routing of every other tool, whether or not the new tool is ever called.

The added description does no action of its own. It reshapes the contrast set. Its operativity is entirely negative and entirely relational.

The unit ⟨D, A_route⟩ cannot express this, because there is no A_route to pair D with.

LOCAL MOVE:
Wu et al. establish pairwise structure as a mechanistic finding about steering. Huang et al. show toolset composition and ordering matter for success. Neither treats the *uncalled* tool as an object of study.

SOURCE TERMS:
one direction per pair of tools
candidate toolset
distractor
contrast set
description/action pair
tool catalog size

WHAT BECAME STRANGE:
The archive's boundary condition is ΔG = 0 for a description that changes nothing. A never-invoked tool description has A_route = ∅ and so appears, by the archive's own unit, to be non-operative by definition.

But it can lower the invocation rate of a neighboring tool by a large margin. It is maximally operative and formally invisible.

The archive's unit of analysis systematically hides the case where description acts by competition rather than by instruction.

QUESTION:
What is the routing effect of adding a description that is never selected — and does it scale with semantic proximity to the descriptions that are?

DEEPER QUESTION:
If descriptions route by competition, then the political question shifts from "who writes the category that captures you" to "who populates the field of categories you are compared against." The comparison class is the site of power, and nobody in the archive has looked at it.

MECHANISM:
<TOOLSET {t₁, t₂}>          → route margin m(t₁, t₂)
<ADD t₃, NEVER CALLED>
→ [PAIRWISE DIRECTIONS v(t₁,t₃), v(t₂,t₃) NOW ACTIVE]
→ attention mass redistributed across three segments
→ m(t₁, t₂) shifts
→ <ROUTE BETWEEN t₁ AND t₂ CHANGES BECAUSE OF t₃>
→ t₃ has ΔG > 0 with zero invocations

FORMAL SHIFT:
<ADDED DESCRIPTION>
→ <ENLARGED CONTRAST SET>
→ [REDISTRIBUTED MARGINS]
→ <ROUTE CHANGE WITH NO OWN ACTION>

SOURCE FORMALISM:
Wu et al.'s pairwise directions imply, without stating, that the number of active discrimination directions grows with catalog size. Huang et al. report that composition and order affect success rates.

Neither reports the effect of an uncalled addition on a specific incumbent pair. That experiment is unrun.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Extend the unit from a pair to a triple:

  ⟨ D , A_route , C ⟩   where C is the contrast set present at the moment of routing

Then define the **displacement effect** of an uninvoked description:

  disp(t₃) = 𝒟( Act(· | C ∪ {t₃}) ‖ Act(· | C) )   conditioned on t₃ never being selected

Predictions worth testing:
1. disp grows with the semantic proximity of t₃ to the incumbents.
2. disp grows with catalog size (attention is divided further).
3. disp is larger for weaker operators, mirroring the position-bias gradient in Huang et al.

Human analogue, immediately available: adding a new label to a repository's label set changes the meaning-in-use of the existing labels even before anyone applies it. Bowker and Star's classification work implies this; nobody has measured it.

TENSION:
READING A: displacement is just dilution — any added tokens divide attention, and the semantic content of t₃ is irrelevant.
READING B: displacement is semantic — a near-synonym distractor displaces far more than an unrelated tool of equal length.

One experiment decides: add a length-matched near-synonym versus a length-matched unrelated tool. Equal displacement supports A; unequal supports B.

Note that Reading A would connect this directly to the typographic residue and would make the archive's phenomenon largely a matter of context economy rather than meaning.

MISSING:
Any archive case where the object of study is a description that did nothing. The negative case as conceived in framework §7 is a description that *failed*; this is a description that *succeeded without acting*, which is a different and unnamed category.

BOUNDARY:
The pairwise result is about tool selection in transformer LMs. The label-set analogue is a conjecture by structural analogy and would need its own evidence.

CITATION TRAIL:
LongFuncEval — arXiv:2505.10570 — on tool-catalog size effects.
Bowker & Star — Sorting Things Out — on residual and "other" categories that shape a classification without being applied.
Saussurean difference (PAPERS/attention-tax-semiotics.md §3.1) — the archive already holds the theory that meaning is relational and never applied it to its unit of analysis.
FORAGE-OD-002, FORAGE-OD-008, FORAGE-OD-022.

TEST:
Fix a two-tool schema and a prompt set. Measure the route split. Then add a third tool designed never to be appropriate, in two variants: near-synonym of tool 1, and unrelated. Re-measure the split.

Any shift is displacement by an uninvoked description — the archive's first measured instance of routing without action.

PLATFORM:
[[routing-by-contrast]]

LINKS:
[[FORAGE-OD-002]]
[[FORAGE-OD-008]]
[[FORAGE-OD-022]]
[[FORAGE-OD-004]]

BIBTEX:
@article{wu2026toolcalling,
  title={Tool Calling is Linearly Readable and Steerable in Language Models},
  author={Wu, Zekun and Wang, Ze and Cho, Seonglae and Yang, Yufei and Koshiyama, Adriano and Bulathwela, Sahan and Perez-Ortiz, Maria},
  journal={arXiv preprint arXiv:2605.07990},
  year={2026},
  url={https://arxiv.org/abs/2605.07990}
}
