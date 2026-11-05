ZETTEL

ID: BAJOHR-07
TITLE: An action can look right while leaving the object unchanged
SOURCE: OpenAI — “Video Generation Models as World Simulators,” 2024, Discussion. Read against Bajohr’s use of Sora in the Venice talk, 2025.

PASSAGE: [PARAPHRASE] OpenAI reports that eating can fail to produce the expected change in the food’s state. The same report presents scaling as a promising route toward capable simulators.

RESEARCH OBJECT: The persistence of an action’s consequence through a change of view.
LOCAL MOVE: The report’s failure case gives Bajohr’s general contrast between statistical regularity and causality an observable target.
SOURCE TERMS: Changes in object state, simulator, physical interaction.
WHAT BECAME STRANGE: An eating gesture can be convincing enough to identify even when the food offers no durable evidence that eating happened.
QUESTION: What happens when a later shot depends on an earlier action’s material consequence?
MECHANISM: A bite should alter the same object. That alteration should survive occlusion, a camera move, and the object’s return to view.
FORMAL SHIFT: <whole object plus action> → <changed object> → [preserve identity and state across views] → <reappearance consistent with the action>.
SOURCE FORMALISM: The report documents the failure class. It supplies no explicit object-state update rule for this case.
OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Score action recognizability, immediate state change, and persistence after reappearance as separate outcomes.
TENSION: A. The model maintains an object state across the sequence. B. Each moment is visually plausible while the relation between moments is fragile.
MISSING: A matched no-action condition and systematic variation of occlusion and camera movement.
BOUNDARY: An output test can establish persistence under the tested conditions. Identifying the internal representation requires further evidence.
CITATION TRAIL: The report’s eating, shattering, and spontaneous-object examples. Compare the intervention method in Li et al., arXiv:2210.13382, within its bounded Othello setting.
TEST: Compare clips in which a person bites a marked apple or only raises it to their lips, hides it behind a cup, then reveals the same side. Score whether the mark and bite state persist together.
PLATFORM: [[Evidence for operative world models]]
LINKS: [[BAJOHR-03]] [[BAJOHR-04]]

BIBTEX:
@misc{openai2024worldsimulators,
  author = {{OpenAI}},
  title = {Video Generation Models as World Simulators},
  year = {2024},
  url = {https://openai.com/index/video-generation-models-as-world-simulators/}
}
