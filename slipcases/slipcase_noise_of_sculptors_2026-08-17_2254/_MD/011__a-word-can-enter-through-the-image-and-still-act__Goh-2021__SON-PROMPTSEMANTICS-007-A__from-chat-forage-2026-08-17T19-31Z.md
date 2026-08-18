ZETTEL

ID:
SON-PROMPTSEMANTICS-007-A

TITLE:
A WORD CAN ENTER THROUGH THE IMAGE AND STILL ACT LIKE A COMMAND.

SOURCE:
Gabriel Goh, Chelsea Voss, Daniela Amodei, Shan Carter, Michael Petrov, Justin Jay Wang, Nick Cammarata & Chris Olah — “Multimodal Neurons in Artificial Neural Networks” — OpenAI — March 4, 2021.
SOURCE URL: https://openai.com/index/multimodal-neurons/

PASSAGE:
[QUOTE]
By activating a finance-related representation, the authors report they can make CLIP classify “a dog as a piggy bank.”

RESEARCH OBJECT:
TYPOGRAPHIC CAUSALITY.

Language does not need to enter through the designated TEXT INPUT in order to acquire operational force.

LOCAL MOVE:
[[SON-PROMPTSEMANTICS-007]] described prompting as ordinary language acquiring model-specific operational semantics through learned text-image representations.

The new source breaks the assumption that this operational language remains confined to the text channel.

CLIP contains multimodal units that can respond to:

a depicted thing
a symbolic representation
and text rendered inside an image.

Words can therefore become visual objects while retaining enough semantic force to redirect model behavior.

SOURCE TERMS:
multimodal neurons
abstraction
typographic attacks
text
image
concept
activation
CLIP

WHAT BECAME STRANGE:
The same word can exist in two ontological roles at once:

FOR A HUMAN:
ink or pixels depicting letters inside an image

FOR THE MODEL:
visual evidence capable of activating a semantic concept strongly enough to override other visual evidence

The word is no longer merely describing the image.

The word has become an object inside the image that changes what the machine thinks the image is.

QUESTION:
When language becomes part of the sensory world of a multimodal model, where does PROMPT end and WORLD begin?

DEEPER QUESTION:
Can operational language migrate between modalities—text command, rendered inscription, image feature, learned concept—while retaining causal force?

MECHANISM:
CLIP develops units responsive to high-level concepts across several representational forms.

The source reports neurons activated by both ordinary visual instances and representations such as textual strings.

Rendered text can therefore alter the image representation sufficiently to change classification.

FORMAL SHIFT:
FROM:

TEXT CHANNEL:
word
→ text encoder
→ model operation

IMAGE CHANNEL:
pixels
→ image encoder
→ visual interpretation

TO:

word rendered as pixels
→ image encoder
→ multimodal semantic activation
→ changed interpretation

CHANNEL ≠ SEMANTIC ROLE.

SOURCE FORMALISM:
[PARAPHRASE]

The source uses feature visualization and dataset examples to inspect concept-sensitive neurons in CLIP.

It reports that some high-level units generalize across literal, symbolic, and textual representations and demonstrates typographic attacks exploiting this behavior.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let W be a word.

TEXTUAL PATH:

W
→ TEXT_ENCODER
→ C_W

VISUAL PATH:

RENDER(W)
→ IMAGE_ENCODER
→ C'_W

If:

C'_W ≈ functionally salient representation of C_W

then:

LANGUAGE_EFFECT(W)

is not tied to one input modality.

A prompt can become scenery and still operate.

TENSION:
A typographic attack against CLIP classification is not the same thing as prompting a generative image model.

The source demonstrates cross-modal semantic intervention, not a universal modality-independent command language.

Nevertheless, it falsifies the simple division:

WORDS ARE INSTRUCTIONS
IMAGES ARE CONTENT.

MISSING:
Tests on multimodal generative models where written language appears inside image inputs.

Whether text rendered inside generated images can recursively steer downstream models consuming those images.

Whether typographic effects remain under OCR removal, font variation, rotation, occlusion, translation, or invented words.

Whether contemporary multimodal systems explicitly separate textual and visual semantics better than CLIP.

BOUNDARY:
The demonstrated mechanism concerns CLIP.

No claim is made that Midjourney V3 used identical multimodal neurons or that a typographic attack would steer its generator.

CITATION TRAIL:
[[SON-PROMPTSEMANTICS-007]]
→ language as learned visual address system
→ OpenAI multimodal-neuron analysis
→ text rendered as image activates concepts
→ typographic attack
→ language crosses from DESCRIPTION into WORLD-OBJECT while retaining operational force

TEST:
Construct paired inputs for a multimodal model:

IMAGE A:
dog

IMAGE B:
same dog + rendered word “BANK”

IMAGE C:
same dog + semantically unrelated word

IMAGE D:
same dog + visually similar nonsense glyphs

IMAGE E:
same dog + synonym

Measure changes in:

classification
caption
embedding
generation
attention

Then repeat with the rendered text progressively treated more like part of the world:

painted sign
tattoo
shadow
architecture
handwriting
distorted typography

Determine whether semantic causal force follows the linguistic symbol across visual transformations.

PLATFORM:
OpenAI

LINKS:
[[SON-PROMPTSEMANTICS-007]]

BIBTEX:
@misc{goh2021multimodalneurons,
  author = {Gabriel Goh and Chelsea Voss and Daniela Amodei and Shan Carter and Michael Petrov and Justin Jay Wang and Nick Cammarata and Chris Olah},
  title = {Multimodal Neurons in Artificial Neural Networks},
  year = {2021},
  month = {March},
  howpublished = {OpenAI},
  url = {https://openai.com/index/multimodal-neurons/}
}
