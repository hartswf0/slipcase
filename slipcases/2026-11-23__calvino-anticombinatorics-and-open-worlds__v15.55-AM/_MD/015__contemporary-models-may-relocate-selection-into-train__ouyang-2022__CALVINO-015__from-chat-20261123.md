ZETTEL

ID: CALVINO-015

TITLE:
Contemporary models may relocate selection into training rather than eliminate it.

SOURCE:
Long Ouyang et al. — "Training Language Models to Follow Instructions with Human Feedback" — NeurIPS (2022).

PASSAGE:
[PARAPHRASE]
The researchers collect human-written demonstrations and rankings of model outputs, then use them to train and refine a language model's behavior.

RESEARCH OBJECT:
Human evaluation incorporated into a model's learned generative behavior before an individual user requests an artifact.

LOCAL MOVE:
The paper distinguishes language modeling from following human instructions and demonstrates a procedure for modifying a model through preference feedback.

SOURCE TERMS:
"demonstrations"; "rankings";
"reward model"; "reinforcement learning from human feedback."

WHAT BECAME STRANGE:
The research note's division of labor between a generative model and a human who selects its outputs neglects the human judgments already embedded in some trained models.

QUESTION:
How much of contemporary computational selection occurs before generation, through data selection, annotation, preference modeling, and optimization?

DEEPER QUESTION:
Where should authorship be located when an artifact depends on accumulated evaluations from people who never encounter the eventual user or work?

MECHANISM:
People evaluate candidate behaviors. Their assessments become training data. An optimization procedure changes the model's output distribution.

FORMAL SHIFT:
Human judgments
→ labeled demonstrations and rankings
→ [model optimization]
→ revised generative behavior.

SOURCE FORMALISM:
Supervised fine-tuning.
Reward modeling.
Reinforcement learning from human feedback.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Candidate outputs
→ human preference data
→ learned preference signal
→ modified model parameters
→ subsequent output distribution.

This differs from a human choosing among outputs after generation.

TENSION:
Preference alignment is not equivalent to artistic judgment. A model optimized to follow instructions is not thereby optimized to generate aesthetically consequential exceptions.

MISSING:
A provenance system connecting particular training judgments to particular output characteristics; a defensible account of artistic evaluation across different communities.

BOUNDARY:
This paper establishes one training methodology, not the architecture or training history of all contemporary generative models.

CITATION TRAIL:
Ouyang et al. (2022).
Research on preference learning and reward modeling.
Calvino, "Prose et anticombinatoire."
Studies of distributed creative labor.

TEST:
Compare base and preference-tuned models on the same constrained writing task. Measure conformity, variation, constraint violations, and human evaluations separately.

PLATFORM:
[[Distributed Authorship and Computational Selection]]

LINKS:
[[CALVINO-002]]
[[CALVINO-007]]
[[CALVINO-013]]

BIBTEX:
@inproceedings{ouyang2022training,
  author    = {Ouyang, Long and others},
  title     = {Training Language Models to Follow Instructions with Human Feedback},
  booktitle = {Advances in Neural Information Processing Systems},
  volume    = {35},
  year      = {2022},
  eprint    = {2203.02155},
  archivePrefix = {arXiv},
  url       = {https://arxiv.org/abs/2203.02155}
}
