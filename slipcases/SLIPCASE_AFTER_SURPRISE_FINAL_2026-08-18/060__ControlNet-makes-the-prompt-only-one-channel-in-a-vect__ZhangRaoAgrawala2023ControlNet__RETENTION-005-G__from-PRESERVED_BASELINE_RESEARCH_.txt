ZETTEL

ID:
RETENTION-005-G

TITLE:
ControlNet makes “the prompt” only one channel in a vector of independently authored controls.

SOURCE:
Lvmin Zhang, Anyi Rao, and Maneesh Agrawala — “Adding Conditional Control to Text-to-Image Diffusion Models” — 2023.

PASSAGE:
[PARAPHRASE]
ControlNet combines text with spatially structured conditions such as edges, depth, segmentation, and pose. Prompt language therefore need not bear the entire burden of specifying an image.

RESEARCH OBJECT:
PROMPT AUTHORSHIP MAY BE ONE COMPONENT OF A MULTIMODAL CONTROL TOPOLOGY.

LOCAL MOVE:
Composition, pose, depth, and semantic description may all enter BEFORE generation through different control channels.

SOURCE TERMS:
conditional control
edges
depth
segmentation
pose
text-to-image
multiple conditions

WHAT BECAME STRANGE:
The legal question “did the prompt control the image?” can be too coarse when text controls style, pose controls gesture, depth controls space, edge maps control contour, and masks control locality.

QUESTION:
Should human authorship be assigned feature-by-feature to the control channel that causally governs each expressive dimension?

DEEPER QUESTION:
Can authorship be represented as a causal decomposition over output features rather than a binary property of the entire generated image?

MECHANISM:
human supplies p=text, e=edge map, d=depth, h=pose, m=mask → conditioned generator → y.

FORMAL SHIFT:
<PROMPT → OUTPUT> → <VECTOR OF HUMAN CONTROL SIGNALS → OUTPUT>

SOURCE FORMALISM:
ControlNet conditions diffusion generation through learned control pathways for spatial inputs.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
y ~ G(p,e,d,h,m,z). Let C_ij be the causal influence of human control channel i on output feature j.

TENSION:
Copyright does not ordinarily allocate microscopic feature ownership through causal matrices.

MISSING:
A legal doctrine for hybrid works where expressive elements are produced through differently controlled channels inside one generation event.

BOUNDARY:
“Prompting” may describe only one surface of an artistic operation distributed across many human-authored conditions.

CITATION TRAIL:
[[RETENTION-005]] → prompt versus downstream modification → ControlNet → spatial controls move modification upstream → authorship becomes channel- and feature-specific.

TEST:
Ablate one conditioning channel at a time while holding all others fixed. Map unstable visible properties to the human intervention that constrained them.

PLATFORM:
[[class-is-not-a-path]]

LINKS:
[[RETENTION-005]]
[[controlnet]]
[[multimodal-control]]
[[feature-level-authorship]]
[[control-topology]]

BIBTEX:
@article{ZhangRaoAgrawala2023ControlNet, author={Zhang, Lvmin and Rao, Anyi and Agrawala, Maneesh}, title={Adding Conditional Control to Text-to-Image Diffusion Models}, journal={arXiv preprint arXiv:2302.05543}, year={2023}}
