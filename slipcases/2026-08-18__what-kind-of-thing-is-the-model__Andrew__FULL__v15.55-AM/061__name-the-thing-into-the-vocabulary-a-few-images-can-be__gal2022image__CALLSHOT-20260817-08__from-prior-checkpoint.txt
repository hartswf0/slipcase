ZETTEL

ID:
CALLSHOT-20260817-08

TITLE:
NAME THE THING INTO THE VOCABULARY — a few images can be compressed into a new pseudo-word that can then be composed inside ordinary prompts.

SOURCE:
Rinon Gal et al. — “An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion” — 2022.
https://arxiv.org/abs/2208.01618

PASSAGE:
[PARAPHRASE]
Textual Inversion learns, from only a small set of images of a user-provided object or style, a new embedding representing that concept inside the text embedding space of a frozen text-to-image model. The learned pseudo-word can then be composed with ordinary natural-language prompts.

RESEARCH OBJECT:
USER-INVENTED-EXECUTABLE-WORD.

LOCAL MOVE:
[[MJ-GC-019]] treated prompt words as locations or attractors in semantic space.

This work permits the user to add a new handle to that space.

The operation is astonishingly literal:

SHOW THE SYSTEM A THING.

LEARN A WORD FOR IT.

USE THE WORD IN SENTENCES.

SOURCE TERMS:
“3-5 images”
“user-provided concept”
“new words”
“embedding space”
“frozen”
“composed”
“natural language sentences”

WHAT BECAME STRANGE:
Vocabulary is no longer only inherited.

A user can manufacture a local lexical item whose referent did not previously have a usable name inside the model’s text interface.

Naming becomes model customization.

QUESTION:
What is a “word” when it has no prior linguistic history and is created specifically as a learned control handle?

DEEPER QUESTION:
Could future prompting involve constructing private operational vocabularies whose terms compile entire bundles of visual, behavioral, or procedural constraints?

MECHANISM:
EXAMPLE IMAGES
→ optimize new embedding vector v*
while base model remains frozen
→ assign pseudo-token S*
→ place S* inside ordinary prompt
→ generation retrieves/composes learned concept.

FORMAL SHIFT:
FROM:
WORDS SELECT PREEXISTING CONCEPTS.

TO:
USER EXAMPLES
→ CREATE NEW WORD
→ NEW WORD BECOMES FUTURE CONTROL SURFACE.

SOURCE FORMALISM:
Textual Inversion learns a new text embedding from 3–5 images while keeping the text-to-image model frozen; the resulting learned “word” can be composed in natural-language prompts.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

EXAMPLES(E)
→ LEARN TOKEN τ_E.

Thereafter:

PROMPT(... τ_E ...)
→ invoke concept condensed from E.

The workflow is:

DEMONSTRATE
→ NAME
→ RECALL
→ COMPOSE.

TENSION:
Compressing a concept into one embedding may preserve some features while entangling others.

A callable name is not necessarily a clean symbolic definition.

MISSING:
A systematic account of what information survives and what is lost when a complex visual concept is compressed into a learned token.

BOUNDARY:
The learned pseudo-word is an embedding used by a particular model, not an ordinary word with stable meaning across people or models.

CITATION TRAIL:
[[MJ-GC-019]]
→ words as semantic coordinates
→ Textual Inversion
→ user creates new coordinate from examples
→ prompting becomes vocabulary construction.

TEST:
Create three learned pseudo-words:

OBJECT
STYLE
RELATIONAL CONFIGURATION.

Test each under radically different sentences.

Identify which kinds of learned “words” compose cleanly and which collapse outside their training context.

PLATFORM:
Text-to-image diffusion / Textual Inversion

LINKS:
[[MJ-GC-019]]
[[MJ-GC-020]]
[[CALLSHOT-20260817-01]]

BIBTEX:
@article{gal2022image,
  title={An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion},
  author={Gal, Rinon and Alaluf, Yuval and Atzmon, Yuval and Patashnik, Or and Bermano, Amit H. and Chechik, Gal and Cohen-Or, Daniel},
  journal={arXiv preprint arXiv:2208.01618},
  year={2022},
  url={https://arxiv.org/abs/2208.01618}
}
