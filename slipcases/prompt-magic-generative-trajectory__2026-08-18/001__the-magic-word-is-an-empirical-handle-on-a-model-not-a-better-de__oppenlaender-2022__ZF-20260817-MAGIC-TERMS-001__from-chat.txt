ZETTEL

ID:
ZF-20260817-MAGIC-TERMS-001

TITLE:
The “Magic Word” Is an Empirical Handle on a Model, Not a Better Description

SOURCE:
Jonas Oppenlaender, “A Taxonomy of Prompt Modifiers for Text-To-Image Generation” (2022; rev. 2023).
https://arxiv.org/abs/2204.13988

PASSAGE:
[PARAPHRASE] Oppenlaender identifies six practitioner categories of prompt modifiers: subject terms, image prompts, style modifiers, quality boosters, repeating terms, and “magic terms.” A magic term is semantically unlike the rest of the prompt and is introduced to increase the likelihood of surprising results. Prompt practice proceeds iteratively through defining, modifying, solidifying, varying, and mixing or excluding elements.

RESEARCH OBJECT:
Millière’s description of prompting as “alchemy” or “incantation” becomes stranger when treated literally rather than rhetorically. Practitioners really did develop vocabularies of terms whose effectiveness could not be inferred from their ordinary meanings. The important distinction is therefore not between skilled and unskilled description. It is between semantic description and empirical control.

A prompt can contain words because they accurately describe the desired image, but it can also contain words because previous executions revealed that those words perturb a particular model in a useful way.

The latter are less like adjectives and more like handles discovered on an opaque machine.

LOCAL MOVE:
Replace:

PROMPT SKILL = finding increasingly accurate words for an artistic intention

with:

PROMPT SKILL = discovering which textual interventions reliably alter a particular generative system.

SOURCE TERMS:
prompt modifier
subject term
style modifier
image prompt
quality booster
repeating term
magic term
prompt engineering
iterative experimentation
weights

WHAT BECAME STRANGE:
The most technically effective word may be the least semantically defensible word.

A person can therefore become better at communicating with the model by becoming worse, in an ordinary linguistic sense, at describing what they want.

“Magic words” are not merely mystification. They are evidence that natural language has acquired a second, machine-local pragmatics.

QUESTION:
When a word works because of what a model does with it rather than because of what the word conventionally means, what kind of language practice has emerged?

DEEPER QUESTION:
Does prompt expertise consist in expressing intention, or in learning a private empirical dialect produced accidentally by the interaction of training data, architecture, interface, and model version?

MECHANISM:
[PARAPHRASE] Practitioners iteratively generate images, inspect effects, add or remove modifiers, consult community resources, reuse successful phrases, and sometimes apply weighting. Oppenlaender explicitly describes prompt engineering as an acquired practice of experimentation and trial and error.

FORMAL SHIFT:
DESCRIPTION → REPRESENTATION

becomes:

INTERVENTION → EXECUTION → OBSERVED EFFECT → RETAINED PHRASE → REINTERVENTION

The operative unit is no longer the sentence alone.

It is the experimentally stabilized relation:

phrase ↔ model behavior

SOURCE FORMALISM:
[PARAPHRASE]

Oppenlaender gives an iterative sequence:

Define
→ Modify
→ Solidify
→ Vary
→ Mix / Exclude

and distinguishes six modifier classes.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

M = a particular model/version
p = prompt
t = candidate textual modifier
G(M,p) = distribution of generated outputs
Δ(t|M,p) = observed change produced by adding t

Then a practitioner can retain t even when:

semantic_relevance(t,p) ≈ 0

provided:

useful_effect(Δ(t|M,p)) >> 0

Prompt craft therefore permits:

SEMANTICALLY WEAK TERM
→ MODEL-SPECIFIC EFFECT
→ PRACTITIONER RETENTION
→ “MAGIC WORD”

TENSION:
Millière treats prompt skill as evidence of human artistic intentionality.

Oppenlaender reveals a less comfortable possibility: part of that skill consists precisely in manipulating causal relations the practitioner does not understand.

Expertise and ignorance can therefore increase together.

MISSING:
We do not yet know how much prompt expertise survives migration between model architectures, checkpoints, interfaces, or retrained versions.

Without that evidence, “prompt engineering” may describe anything from durable artistic competence to temporary mastery of implementation quirks.

BOUNDARY:
Oppenlaender’s taxonomy arose from early text-to-image communities and systems including VQGAN–CLIP, Midjourney, and DALL-E 2. It should not be assumed to constitute a universal grammar of generative prompting.

CITATION TRAIL:
[[MILLIERE-2022-WIRED-AI-CURATION]]
→ Millière: prompting as “alchemy” / “incantation”
→ Oppenlaender: practitioner taxonomy includes literal “magic terms”
→ unresolved edge: determine whether magic terms behave as durable linguistic operators or disposable model exploits

TEST:
Choose 30 historically documented prompt modifiers from the source corpus.

Execute controlled prompt ablations across:
1. multiple model families
2. multiple versions of the same model
3. multiple subjects
4. multiple seeds

Measure whether each modifier retains:
a. direction of effect
b. magnitude of effect
c. stylistic coherence
d. semantic interpretability

If the effect disappears across versions while ordinary semantic terms persist, classify the modifier as MODEL-LOCAL rather than LANGUAGE-GENERAL.

PLATFORM:
VQGAN–CLIP
Midjourney
DALL-E 2
text-to-image prompting communities

LINKS:
[[MILLIERE-2022-WIRED-AI-CURATION]]
[[PROMPT-AS-EMPIRICAL-DIALECT]]
[[MODEL-LOCAL-LANGUAGE]]
[[DEFERRED-FORMALIZATION]]

BIBTEX:
@article{oppenlaender2022taxonomy,
  title={A Taxonomy of Prompt Modifiers for Text-To-Image Generation},
  author={Oppenlaender, Jonas},
  journal={arXiv preprint arXiv:2204.13988},
  year={2022},
  url={https://arxiv.org/abs/2204.13988}
}
