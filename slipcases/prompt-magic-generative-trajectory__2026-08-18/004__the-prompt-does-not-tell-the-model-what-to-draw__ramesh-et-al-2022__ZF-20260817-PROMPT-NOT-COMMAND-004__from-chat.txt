ZETTEL

ID:
ZF-20260817-PROMPT-NOT-COMMAND-004

TITLE:
The Prompt Does Not Tell the Model What to Draw

SOURCE:
Aditya Ramesh, Prafulla Dhariwal, Alex Nichol, Casey Chu, and Mark Chen, “Hierarchical Text-Conditional Image Generation with CLIP Latents” (2022).
https://arxiv.org/abs/2204.06125

PASSAGE:
[PARAPHRASE] DALL-E 2 is described as a two-stage generative system: a prior produces a CLIP image embedding conditioned on a text caption, then a decoder generates an image conditioned on that image representation. The learned embedding captures aspects of both semantics and style while permitting variation in details.

RESEARCH OBJECT:
Millière’s “incantation” metaphor quietly assumes the prompt acts like an instruction whose peculiar wording determines whether the machine obeys.

The architecture suggests another ontology.

The words do not function as a miniature drawing program.

They condition the production of a learned representation.

The representation then conditions image generation.

The prompt therefore does not contain the picture.

Nor does it specify all of the operations required to construct the picture.

It perturbs a statistical machinery already saturated with learned relations among language, visual concepts, semantics, and style.

LOCAL MOVE:
Stop treating:

PROMPT → PICTURE

as the operative relation.

Insert the hidden representational machinery:

TEXT
→ LEARNED REPRESENTATION
→ STOCHASTIC GENERATION
→ IMAGE

SOURCE TERMS:
CLIP
text caption
image embedding
prior
decoder
diffusion model
joint embedding space
semantics
style
variation

WHAT BECAME STRANGE:
The user writes words.

The machine does not execute those words as procedures.

It transforms their relation to a learned space and generates from there.

Prompting therefore looks like programming at the surface while lacking an ordinary programming language’s explicit operational semantics.

QUESTION:
If a prompt does not specify the operations that produce its output, in what precise sense can prompting be called programming?

DEEPER QUESTION:
What new class of control system appears when human-readable language selects or perturbs latent machine representations whose causal structure is neither specified by the user nor fully inspectable by them?

MECHANISM:
[PARAPHRASE] In the DALL-E 2 architecture described by Ramesh et al., textual conditioning is mediated through CLIP representations: a prior maps from caption conditioning toward an image embedding, and a decoder generates an image from that representation. Variation is intrinsic rather than fully specified by the text.

FORMAL SHIFT:
PROMPT = INSTRUCTION

becomes:

PROMPT = CONDITION ON A GENERATIVE PROCESS

and:

DESCRIPTION = PROGRAM TEXT

becomes:

DESCRIPTION
→ REPRESENTATIONAL CONSTRAINT
→ UNDERDETERMINED EXECUTION

SOURCE FORMALISM:
[PARAPHRASE]

text caption
→ prior
→ CLIP image embedding
→ decoder
→ image

The authors experiment with autoregressive and diffusion priors and use diffusion models for decoding.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Traditional explicit program:

P + INPUT
→ specified operations
→ OUTPUT

Prompt-conditioned generation:

p
→ E_text(p)
→ latent conditional distribution
→ sampled representation z
→ generative decoder
→ x

Therefore the prompt constrains:

P(x | p, M)

rather than fully specifying x.

A prompt is closer to a distribution-shaping intervention than a complete procedural description.

TENSION:
Prompt discourse repeatedly borrows the language of commands, programming, engineering, spells, and control.

But these metaphors disagree about where causality lives.

COMMAND suggests explicit obedience.

PROGRAM suggests executable semantics.

SPELL suggests effective form without transparent mechanism.

The DALL-E 2 machinery makes the third metaphor unexpectedly precise:

a surface expression can have reliable operational consequences without the user possessing a causal account of how those consequences are produced.

MISSING:
A theory distinguishing:

COMMAND
PROGRAM
QUERY
DESCRIPTION
CONDITION
CONSTRAINT
CONTROL SIGNAL

in generative interfaces.

Without this distinction, “prompt programming” risks becoming metaphor rather than a technical claim.

BOUNDARY:
This architecture describes DALL-E 2 specifically. Other generative systems can employ different conditioning mechanisms, architectures, interfaces, and additional control channels.

CITATION TRAIL:
[[MILLIERE-2022-WIRED-AI-CURATION]]
→ incantation / magic-word description of prompting
→ Ramesh et al.: text conditions a learned representational pipeline
→ unresolved edge: determine the minimum computational semantics required before natural-language interaction deserves the name PROGRAMMING

TEST:
Construct four formally distinct interaction classes:

A. deterministic command language
B. declarative constraint solver
C. database query
D. generative-model prompt

For each, specify:

what the expression denotes
what state it addresses
which operations are explicit
which operations are delegated
whether identical expressions determine identical outputs
what constitutes execution failure

Then test whether prompting forms a genuine fifth computational category or reduces to one of the existing classes.

PLATFORM:
DALL-E 2
CLIP
diffusion models
text-conditioned image generation

LINKS:
[[MILLIERE-2022-WIRED-AI-CURATION]]
[[PROMPT-NOT-THE-PROGRAM]]
[[DEFERRED-FORMALIZATION]]
[[DESCRIPTION-AS-CONDITION]]
[[OPERATIVE-EKPHRASIS]]

BIBTEX:
@article{ramesh2022hierarchical,
  title={Hierarchical Text-Conditional Image Generation with CLIP Latents},
  author={Ramesh, Aditya and Dhariwal, Prafulla and Nichol, Alex and Chu, Casey and Chen, Mark},
  journal={arXiv preprint arXiv:2204.06125},
  year={2022},
  url={https://arxiv.org/abs/2204.06125}
}
