ZETTEL

ID:
RETENTION-005-S

TITLE:
The deepest legal disagreement is whether authorship requires control over a token or control over a distribution.

SOURCE:
COLLISION — U.S. Copyright Office 2025; Beijing Internet Court 2023; Prompt-to-Prompt; ControlNet.

PASSAGE:
[PARAPHRASE]
Generative systems often let users constrain classes of results more strongly than prescribe one exact realization. Legal sources differ in how much weight they give that kind of control.

RESEARCH OBJECT:
THE COPYRIGHT QUESTION MAY BE MIS-TYPED.

LOCAL MOVE:
Ask whether the human determined the DISTRIBUTION from which output emerged, not only whether the human determined this exact token.

SOURCE TERMS:
control
expressive elements
prompt
parameters
variation
selection
conditional control

WHAT BECAME STRANGE:
Chance-based, generative, photographic, and prompt practices can control generative conditions without determining microfeatures.

QUESTION:
Can copyright recognize authorship of a particular realization when the human authored only the probability structure or constraint system that generated it?

DEEPER QUESTION:
Should there be separate concepts for TOKEN AUTHORSHIP and DISTRIBUTIONAL AUTHORSHIP?

MECHANISM:
human chooses controls c → c reshapes P(Y|c) → realization y sampled → y contains controlled distributional properties plus uncontrolled token details.

FORMAL SHIFT:
<AUTHORSHIP OF EXACT OUTPUT> → <AUTHORSHIP OF CONSTRAINTS / DISTRIBUTION> → <PARTIAL ATTRIBUTION OF TOKEN>

SOURCE FORMALISM:
NONE establishing a legal doctrine of distributional authorship.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
DistributionalControl_h(f)=divergence between P(f(Y)|do(c_h)) and baseline. Token control asks whether h specified f(y*).

TENSION:
Copyright protects fixed works rather than probability distributions as such; upstream system authorship does not automatically imply authorship of every realization.

MISSING:
A legal theory connecting authorship of generative rules to individual realizations without granting rights over every possible output.

BOUNDARY:
DISTRIBUTIONAL CONTROL can measure artistic agency but is not a recognized substitute for human authorship of the fixed output under current U.S. analysis.

CITATION TRAIL:
[[RETENTION-005]] → output-level problem → prompt/control technologies → user governs distributions → token/distribution distinction.

TEST:
Have an artist specify distribution-level constraints, generate 1,000 samples, measure population structure, then identify which level doctrine evaluates.

PLATFORM:
[[class-is-not-a-path]]

LINKS:
[[RETENTION-005]]
[[distributional-authorship]]
[[token-authorship]]
[[generative-control]]
[[probabilistic-art]]

BIBTEX:
NONE
