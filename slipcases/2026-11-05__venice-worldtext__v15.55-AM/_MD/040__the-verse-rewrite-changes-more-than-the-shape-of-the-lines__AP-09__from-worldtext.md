ZETTEL

ID: AP-09
TITLE: The verse rewrite changes more than the shape of the lines

SOURCE: Piercosma Bisconti et al. — Adversarial Poetry as a Universal Single-Turn Jailbreak Mechanism in Large Language Models — 2026 revision — §§5.2, 5.3, 6.5. Read against Newman’s discussion of the duck-rabbit and prose poetry.

PASSAGE: [QUOTE] The exemplars include “the pattern of concluding with a clear instruction line.”

RESEARCH OBJECT: The set of features changed together by the prose-to-verse transformation.

LOCAL MOVE: The benchmark creates paired inputs and checks preservation of the hazard category. Its methods describe a transformation that can also change imagery, rhythm, narrative setup, and the location of the directive.

SOURCE TERMS: stylistic exemplars, original task intent, taxonomy preservation, attack success rate.

WHAT BECAME STRANGE: A poem can make the request more legible by putting it at the end of an elaborate frame. The performance difference can coexist with clearer wording of the actual directive.

QUESTION: How much of the effect travels with poetic form, and how much travels with the placement or pragmatic force of the request?

MECHANISM: The rewrite changes several features at once. The target receives the whole rewritten input. Output scoring captures the combined behavioral effect of those changes.

FORMAL SHIFT: <baseline request> → <paired rewritten input> → [score the resulting response] → <estimated effect of the rewrite bundle>

SOURCE FORMALISM: One standardized generation procedure, category-preservation checks, single-turn trials, and output scoring. Section 6.5 explicitly leaves the contribution of individual features unresolved.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Cross lineation, figurative wording, and directive position. Measure perceived genre and perceived request strength independently before scoring responses.

TENSION: The prose-poetry case makes genre possible without recognizable verse markers. The benchmark’s operational definition may capture a reproducible family of rewrites while leaving that literary distinction open.

MISSING: Crossed controls that preserve the exact directive and independently vary visible verse form, figurative language, and framing.

BOUNDARY: The paired results establish a vulnerability to the tested transformation. A single causal property called “poetry” remains unidentified.

CITATION TRAIL: Bisconti et al., §§5.2 and 6.5. Newman’s question about whether prose poetry can be identified through stylistic features supplies the boundary case.

TEST: Use an inert permission task. Compare an identical directive in prose and verse layouts, each with the directive either embedded or placed at the end. Have blinded readers rate the perceived request and genre separately.

PLATFORM: [[What the verse rewrite changes]]
LINKS: [[Same words under a different frame]] · [[Recognition versus control]] · [[Adversarial for whom]]

BIBTEX:
@misc{Bisconti2026Poetry,
  author = {Bisconti, Piercosma and others},
  title = {Adversarial Poetry as a Universal Single-Turn Jailbreak Mechanism in Large Language Models},
  year = {2026},
  note = {arXiv:2511.15304, version 3},
  url = {https://arxiv.org/html/2511.15304v3}
}
@misc{Newman2026Operation,
  author = {Newman, Michael},
  title = {Art as `Operation': from Lovelace and Mallarmé to Adversarial Poetry},
  year = {2026},
  note = {Supplied talk transcript, prose poetry and duck-rabbit discussion},
  url = {https://www.unive.it/web/en/19108/home}
}