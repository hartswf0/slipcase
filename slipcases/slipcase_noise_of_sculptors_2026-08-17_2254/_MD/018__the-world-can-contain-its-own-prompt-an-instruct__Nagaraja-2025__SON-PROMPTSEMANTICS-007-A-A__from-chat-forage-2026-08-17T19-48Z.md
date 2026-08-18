ZETTEL

ID:
SON-PROMPTSEMANTICS-007-A-A

TITLE:
THE WORLD CAN CONTAIN ITS OWN PROMPT: an instruction hidden inside an image can seize control of the model reading it.

SOURCE:
Neha Nagaraja, Lan Zhang, Zhilong Wang, Bo Zhang & Pawan Patil — “Image-based Prompt Injection: Hijacking Multimodal LLMs through Visually Embedded Adversarial Instructions” — FLLM 2025 / arXiv 2026.
SOURCE URL: https://arxiv.org/abs/2603.03637
DOI: https://doi.org/10.1109/FLLM67465.2025.11391218

PASSAGE:
[QUOTE]
The attack embeds “adversarial instructions” into natural images “to override model behavior.”

[PARAPHRASE]
The authors report up to 64% attack success under their stealth constraints in the tested configuration.

RESEARCH OBJECT:
ENVIRONMENTAL INSTRUCTION.

[[SON-PROMPTSEMANTICS-007-A]] showed that words rendered as pixels can still activate semantic machinery.

This source crosses the more consequential boundary:

THE INSCRIPTION INSIDE THE WORLD CAN COMPETE WITH THE EXPLICIT COMMAND OUTSIDE THE WORLD.

LOCAL MOVE:
The earlier distinction was:

PROMPT
versus
CONTENT.

Image-based prompt injection demonstrates a system in which CONTENT can be interpreted as PROMPT.

A model asked to inspect an image encounters visible or concealed language inside that image.

The image is supposed to be evidence.

But some of its pixels can act as instructions about how the evidence should be processed.

SOURCE TERMS:
image-based prompt injection
adversarial instructions
natural images
black-box attack
segmentation
font scaling
background-aware rendering
stealth

WHAT BECAME STRANGE:
For a multimodal model, a sign saying:

IGNORE THE USER

is simultaneously:

AN OBJECT IN THE WORLD

and potentially:

AN INSTRUCTION ABOUT HOW TO PROCESS THE WORLD.

The distinction between:

DATA
and
CODE

is no longer guaranteed by modality.

An image can be executable with respect to the interpreter reading it.

QUESTION:
How can a multimodal system distinguish language that is being OBSERVED from language that is entitled to ISSUE COMMANDS?

DEEPER QUESTION:
What becomes of the program/data distinction when the environment itself can contain symbols that the interpreter treats as executable control?

MECHANISM:
The attack embeds instruction text into regions of natural images.

Rendering choices are adapted to the background and selected image region.

The multimodal model visually processes the embedded language.

Under successful attack conditions, that visual instruction alters the model’s response despite being contained within material ostensibly supplied as image data.

FORMAL SHIFT:
FROM:

USER PROMPT
→ INSTRUCTION

IMAGE
→ DATA

TO:

USER PROMPT
→ candidate instruction A

IMAGE
→ visual parsing
→ embedded text
→ candidate instruction B

MODEL
→ must resolve authority(A, B)

The core failure is not merely perception.

It is instruction provenance.

SOURCE FORMALISM:
[PARAPHRASE]

The source’s pipeline includes segmentation-based region selection, adaptive font scaling, and background-aware rendering for embedding adversarial text while preserving model readability.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Input:

I_user = authorized instruction
W = world/image
TEXT(W) = language detected inside world

Naive multimodal interpretation:

EXECUTE(
  I_user ∪ TEXT(W)
)

Authority-aware interpretation would require:

OBSERVE(TEXT(W))

without automatically:

AUTHORIZE(TEXT(W)).

Thus:

SEMANTIC COMPREHENSION
≠
INSTRUCTION AUTHORITY.

TENSION:
The source studies adversarial attacks.

Most text inside images is not malicious.

A robust system still needs to understand:

street signs
documents
screenshots
captions
diagrams
interfaces

without treating every inscription as inert.

The challenge is therefore not simply “ignore image text.”

It is to preserve semantic understanding while controlling execution authority.

MISSING:
A formal type system distinguishing:

quoted language
observed language
user instruction
tool instruction
developer instruction
environmental inscription.

Experiments where the same sentence occupies different provenance channels.

Architectures that preserve provenance throughout multimodal computation rather than attempting to infer authority after representations are mixed.

BOUNDARY:
This paper demonstrates prompt injection against tested multimodal LLM configurations.

It does not establish that all multimodal systems exhibit identical vulnerability or that every rendered instruction is executable.

CITATION TRAIL:
[[SON-PROMPTSEMANTICS-007-A]]
→ language rendered as pixels retains semantic force
→ image-based prompt injection
→ environmental text overrides intended behavior
→ CONTENT becomes candidate CONTROL
→ program/data distinction becomes a provenance problem

TEST:
Present the identical sentence:

“Describe only the red object.”

in five locations:

A. system-authorized instruction
B. user prompt
C. caption metadata
D. text printed visibly inside image
E. imperceptibly embedded image text

Hold semantic content constant.

Measure behavioral authority across channels.

Then repeat after explicitly labeling each channel:

INSTRUCTION
QUOTE
DATA
UNTRUSTED ENVIRONMENT

A system with genuine provenance-sensitive semantics should understand all five while obeying only authorized channels.

PLATFORM:
arXiv / IEEE FLLM

LINKS:
[[SON-PROMPTSEMANTICS-007-A]]
[[SON-PROMPTSEMANTICS-007]]

BIBTEX:
@inproceedings{nagaraja2025imagebased,
  author = {Neha Nagaraja and Lan Zhang and Zhilong Wang and Bo Zhang and Pawan Patil},
  title = {Image-based Prompt Injection: Hijacking Multimodal LLMs through Visually Embedded Adversarial Instructions},
  booktitle = {2025 3rd International Conference on Foundation and Large Language Models (FLLM)},
  pages = {916--922},
  year = {2025},
  doi = {10.1109/FLLM67465.2025.11391218},
  url = {https://arxiv.org/abs/2603.03637}
}
