ZETTEL

ID:
RETENTION-005-F

TITLE:
Attend-and-Excite separates an expressive decision written in the prompt from the mechanism that makes the machine obey it.

SOURCE:
Hila Chefer, Yuval Alaluf, Yael Vinker, Lior Wolf, and Daniel Cohen-Or — “Attend-and-Excite: Attention-Based Semantic Guidance for Text-to-Image Diffusion Models” — 2023.

PASSAGE:
[PARAPHRASE]
A concept can be explicitly present in the human text yet fail to become visually operative. Attend-and-Excite strengthens attention to selected subject tokens during inference so the model more faithfully realizes them.

RESEARCH OBJECT:
INTENTION IN THE PROMPT and OPERATIONAL FORCE OF THE PROMPT ARE DIFFERENT VARIABLES.

LOCAL MOVE:
One intervention can occur twice: first as SEMANTIC COMMITMENT, then as ENFORCEMENT OF THAT COMMITMENT.

SOURCE TERMS:
catastrophic neglect
semantic guidance
attention
subject tokens
faithfulness
inference

WHAT BECAME STRANGE:
A human can specify an expressive element perfectly clearly and still fail to control whether it appears. The failure can be in uptake rather than articulation.

QUESTION:
If a user chooses which requested semantic element to strengthen during inference, has authorship moved closer to direct expressive control?

DEEPER QUESTION:
Should prompt authorship be measured by what the human DESCRIBES or by which described distinctions the system makes operationally enforceable?

MECHANISM:
prompt contains c1,c2,c3 → vanilla model may omit c2 → guidance identifies c2 → strengthen cross-attention to c2 → generation shifts toward realizing c2.

FORMAL SHIFT:
<SEMANTIC SPECIFICATION> → [ATTENTION ENFORCEMENT] → <OPERATIVE CONSTRAINT>

SOURCE FORMALISM:
The method modifies cross-attention activations during inference to increase attention to subject tokens.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
Separate Expressed(p,c) from Effective(p,c,M). An intervention can transform Expressed=true, Effective≈false into Expressed=true, Effective≈true.

TENSION:
The enforcement procedure is largely algorithmic once configured, so attribution depends on who selected the targets and controls.

MISSING:
Interfaces in which artists manually choose which semantic commitments receive inference-time enforcement.

BOUNDARY:
A detailed prompt can contain authored expressive decisions without those decisions being causally sufficient to shape the output.

CITATION TRAIL:
[[RETENTION-005]] → semantic element present yet neglected → inference-time enforcement → intention versus operative control.

TEST:
Write a prompt containing five independently verifiable visual commitments. Compare realization with and without user-directed token enforcement.

PLATFORM:
[[class-is-not-a-path]]

LINKS:
[[RETENTION-005]]
[[attend-and-excite]]
[[semantic-commitment]]
[[operative-enforcement]]
[[uptake]]

BIBTEX:
@article{CheferEtAl2023Attend, author={Chefer, Hila and Alaluf, Yuval and Vinker, Yael and Wolf, Lior and Cohen-Or, Daniel}, title={Attend-and-Excite: Attention-Based Semantic Guidance for Text-to-Image Diffusion Models}, journal={arXiv preprint arXiv:2301.13826}, year={2023}}
