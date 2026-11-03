ZETTEL

ID: IMG-JEPA-03

TITLE:
Viewpoint can be nuisance in a caption and instruction in a prompt

SOURCE:
Randall Balestriero and Yann LeCun — Proving and Improving the Platonic Representation Hypothesis with JEPAs — 2026 — §2.3

PASSAGE:
[QUOTE] “It is a nuisance only for alignment”

RESEARCH OBJECT:
A variable whose status changes when language moves from describing an image to directing its production.

LOCAL MOVE:
The authors distinguish the state a modality shares with others from observation-specific variation. They explicitly acknowledge that a camera-acting world model would need its viewpoint.

SOURCE TERMS:
State, nuisance, viewpoint, independent nuisances, alignment.

WHAT BECAME STRANGE:
[OUR INFERENCE] An image encoder can benefit from treating two camera angles as equivalent for scene recognition. A prompt critic applying that same equivalence could reward a generator for ignoring an explicit camera instruction.

QUESTION:
Can an imagetext critic recognize the same depicted event across views while remaining sensitive to the requested view?

DEEPER QUESTION:
Who decides which details should survive alignment when the language itself selects what matters visually?

MECHANISM:
The positive-pair rule resamples viewpoint in the source model. A prompt such as “seen directly overhead” instead makes viewpoint a target whose value must affect the rendered image.

FORMAL SHIFT:
<Camera angle> → <nuisance for scene recognition or constraint for generation> → [ignore or discriminate] → <different judgments of the same image pair>

SOURCE FORMALISM:
In §2.3, observations are g_m(z, ν). Good views draw independent nuisance variables ν and ν′; corruptions of one observation share its nuisance.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
Keep separate labels for event identity and prompt-constraint satisfaction. The same image pair may match on one and differ on the other.

TENSION:
A critic that strongly preserves camera geometry may mistake a viewpoint change for an event change. A critic that suppresses it may miss a visible prompt violation.

MISSING:
Instruction-conditioned evidence about which differences the critic should ignore.

BOUNDARY:
The paper’s nuisance analysis describes an alignment objective. Applying it to prompt compliance is an inference about a different task.

CITATION TRAIL:
§2.3’s explicit camera-acting example and §3.3’s tests of video frames as image views.

TEST:
Render the same dispute overhead and at eye level. Use both versions with “a dispute before elders,” then score both against “a dispute before elders seen directly overhead.” A critic passes if it preserves event identity in the first comparison and detects the wrong view in the second.

PLATFORM:
[[Operative Ekphrasis]]

LINKS:
[[Cinepromptography]]
[[Conditional Fidelity]]
[[Scene Identity]]

BIBTEX:
@misc{balestriero2026platonic,
  author = {Balestriero, Randall and LeCun, Yann},
  title = {Proving and Improving the Platonic Representation Hypothesis with {JEPAs}},
  year = {2026},
  eprint = {2610.39302},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/html/2610.39302v1}
}