ZETTEL

ID:
PROMPT-ONTOLOGY-005

TITLE:
Software engineering needs the prompt to be an artifact exactly where execution makes it non-self-contained.

SOURCE:
Hugo Villamizar, Jannik Fischbach, Alexander Korn, Andreas Vogelsang, and Daniel Mendez — “Prompts as Software Engineering Artifacts: A Research Agenda and Preliminary Findings” — 2025 — SOURCE URL: https://arxiv.org/abs/2509.17548

PASSAGE:
[PARAPHRASE] Villamizar et al. position prompts as potential software-engineering artifacts whose evolution, traceability, reuse, development, and maintenance deserve systematic study. They invoke an artifact conception centered on a self-contained work result with physical representation, syntax, semantics, and context-specific purpose.

RESEARCH OBJECT:
ARTIFACT IDENTITY AND CAUSAL IDENTITY DIVERGE.

A prompt can be an excellent maintenance artifact while being an incomplete unit of causal explanation.

LOCAL MOVE:
Separate VERSIONABLE OBJECT from OPERATIVE EVENT.

SOURCE TERMS:
software engineering artifact
self-contained work result
evolution
traceability
reuse
prompt management

WHAT BECAME STRANGE:
The practical properties that make something manageable as a software artifact—boundedness, representation, versioning—are precisely the properties lost when the prompt is thickened to include everything that makes its behavior reproducible.

QUESTION:
What is being versioned when a prompt file is unchanged but the model, system message, retrieval, or execution policy changes?

DEEPER QUESTION:
Can software engineering maintain a prompt without falsely implying that the maintained artifact is the complete behavioral unit?

MECHANISM:
Repositories stabilize text/templates as artifacts; runtime systems instantiate them inside changing environments. Version histories record the former more reliably than the latter.

FORMAL SHIFT:
FROM:
PROMPT-VERSION = BEHAVIORAL-VERSION

TO:
PROMPT-ARTIFACT VERSION
≠ necessarily
EXECUTION-CONDITION VERSION.

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let A be archived prompt artifact and E(A,r) its execution under runtime r.

A1 = A2 does not imply E(A1,r1) ≡ E(A2,r2).

TENSION:
Rejecting artifact status would make prompt maintenance harder without solving the causal problem. The useful move is not to abolish prompt artifacts but to stop asking artifact identity to carry causal identity automatically.

MISSING:
Version-control primitives that jointly track prompt text, runtime assembly, model/version, hidden system instructions where available, retrieval state, tools, and evaluation/selection.

BOUNDARY:
The source frames prompts as potential artifacts and a research agenda; it does not claim prompt text alone is a complete causal specification.

CITATION TRAIL:
[[WORKWORDS-PROMPT-001]]
→ prompt programming
→ prompt as maintainable software artifact
→ self-containedness collides with situated execution
→ distinguish maintenance identity from causal identity.

TEST:
Take a production prompt repository over model migrations. Compute byte-level prompt stability and behavioral stability separately. Identify cases where artifact identity persists across behavioral discontinuity and cases where artifact diffs produce no meaningful behavioral change.

PLATFORM:
Software engineering; LLM-integrated workflows.

LINKS:
[[WORKWORDS-PROMPT-001]] [[PROMPT-ONTOLOGY-003]]

BIBTEX:
@article{Villamizar2025PromptsArtifacts,
  title={Prompts as Software Engineering Artifacts: A Research Agenda and Preliminary Findings},
  author={Villamizar, Hugo and Fischbach, Jannik and Korn, Alexander and Vogelsang, Andreas and Mendez, Daniel},
  journal={arXiv preprint arXiv:2509.17548},
  year={2025},
  url={https://arxiv.org/abs/2509.17548}
}
