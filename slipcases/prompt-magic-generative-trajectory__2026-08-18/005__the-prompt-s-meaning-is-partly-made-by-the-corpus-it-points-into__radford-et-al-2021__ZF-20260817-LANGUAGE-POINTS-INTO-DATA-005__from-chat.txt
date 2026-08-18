ZETTEL

ID:
ZF-20260817-LANGUAGE-POINTS-INTO-DATA-005

TITLE:
The Prompt’s Meaning Is Partly Made by the Corpus It Points Into

SOURCE:
Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, and Ilya Sutskever, “Learning Transferable Visual Models From Natural Language Supervision” (2021).
https://arxiv.org/abs/2103.00020

PASSAGE:
[PARAPHRASE] CLIP was trained on roughly 400 million image-text pairs gathered from the internet by learning to identify which textual description corresponded with which image. After training, natural-language expressions can reference learned visual concepts for downstream use.

RESEARCH OBJECT:
Millière says the prompter must discover words that “unlock specific styles or subjects.”

CLIP makes the verb UNLOCK more consequential than it first appears.

Words can affect image generation because language has already been statistically coupled to enormous quantities of visual material.

The artist does not encounter an empty machine awaiting description.

The artist speaks into a sedimented visual-linguistic archive.

The prompt works partly because somebody, somewhere, previously placed words near images.

Prompting therefore has ancestry.

LOCAL MOVE:
Replace:

ARTIST
→ WORD
→ MODEL
→ IMAGE

with:

HISTORICAL IMAGE-TEXT CORPUS
→ LEARNED ASSOCIATIONS
→ MODEL
← CURRENT PROMPT
→ GENERATED IMAGE

The present utterance operates through accumulated past descriptions.

SOURCE TERMS:
natural language supervision
image-text pairs
contrastive learning
natural-language references
visual concepts
zero-shot transfer
CLIP

WHAT BECAME STRANGE:
The prompt appears to be addressed to the future image.

Mechanically, much of its force comes from the past.

A current word becomes generatively powerful because of earlier image-text relations embedded during training.

The prompt is therefore not merely descriptive language.

It is a pointer into a learned cultural residue.

QUESTION:
When an artist discovers that a phrase reliably evokes a visual property, are they inventing a control technique or discovering a preexisting statistical association sedimented from the training corpus?

DEEPER QUESTION:
Can prompt authorship be understood without also treating training-data captioning, tagging, metadata, alt text, filenames, criticism, cataloguing, and ordinary internet description as part of the remote prehistory of the prompt?

MECHANISM:
[PARAPHRASE] CLIP learns joint visual-linguistic representations through contrastive training over hundreds of millions of image-text pairs, after which natural language can refer to learned visual concepts.

FORMAL SHIFT:
PROMPT MEANING = LINGUISTIC MEANING

becomes:

PROMPT EFFECT =
LINGUISTIC EXPRESSION
× LEARNED CORPUS ASSOCIATIONS
× MODEL ARCHITECTURE
× CURRENT GENERATIVE PROCEDURE

SOURCE FORMALISM:
[PARAPHRASE]

(image, text) pairs
→ contrastive pretraining
→ shared learned representations

After training:

natural language
→ reference to learned visual concepts
→ downstream zero-shot behavior.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

D = historical set of image-text relations
Train(D) = model parameters θ
p = present prompt

Then:

θ = sediment(D)

and:

effect(p) = G(p ; θ)

Therefore:

CURRENT PROMPT EFFECT
depends on
PAST DESCRIPTION PRACTICES

even where the current prompter cannot identify those practices.

The prompt is an intervention into a machine whose vocabulary has a history.

TENSION:
Millière’s formulation protects human authorship by locating intention in the present artist.

The technical lineage disperses causal contribution backward.

The prompter chooses the current words.

But the model’s response to those words was conditioned by innumerable prior acts of naming, labeling, captioning, photographing, illustrating, publishing, and categorizing.

Present intentionality operates through inherited statistical memory.

MISSING:
We lack adequate methods for tracing a particular successful prompt term backward from observed generative behavior toward the classes of training associations that made it effective.

The genealogy is usually inaccessible precisely where it becomes theoretically important.

BOUNDARY:
CLIP’s training procedure demonstrates that language-vision behavior can emerge from large-scale image-text supervision. It does not permit a simple one-to-one reconstruction of which individual training items caused a particular generated image or prompt effect.

CITATION TRAIL:
[[MILLIERE-2022-WIRED-AI-CURATION]]
→ “magic words” unlock styles and subjects
→ CLIP: natural-language expressions address visual concepts learned from internet-scale image-text relations
→ next edge: historical study of the descriptive labor that existed before prompting but now furnishes prompting with operative power

TEST:
Select ten prompt terms with unusually strong visual effects.

For each term:

1. document ordinary dictionary semantics
2. document pre-generative visual uses on the web
3. sample historical caption/metadata contexts where legally and technically possible
4. compare visual associations across multiple independently trained models
5. test synonymous substitutions

If visually similar effects persist despite lexical substitution, semantic concept may dominate.

If specific lexical strings produce distinctive effects not shared by synonyms, investigate corpus-specific descriptive history.

PLATFORM:
CLIP
internet-scale image-text training
multimodal representation learning

LINKS:
[[MILLIERE-2022-WIRED-AI-CURATION]]
[[LANGUAGE-AS-TRAINING-SEDIMENT]]
[[PROMPT-GENEALOGY]]
[[HOUSE-OF-LANGUAGE]]
[[DESCRIPTION-BEFORE-OPERATION]]

BIBTEX:
@article{radford2021learning,
  title={Learning Transferable Visual Models From Natural Language Supervision},
  author={Radford, Alec and Kim, Jong Wook and Hallacy, Chris and Ramesh, Aditya and Goh, Gabriel and Agarwal, Sandhini and Sastry, Girish and Askell, Amanda and Mishkin, Pamela and Clark, Jack and Krueger, Gretchen and Sutskever, Ilya},
  journal={arXiv preprint arXiv:2103.00020},
  year={2021},
  url={https://arxiv.org/abs/2103.00020}
}
