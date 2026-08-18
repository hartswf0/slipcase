ZETTEL

ID:
Z-RF-20260818-017

TITLE:
Talking about AI art can become part of the machinery that makes the next artwork.

SOURCE:
Jonas Oppenlaender — “A Taxonomy of Prompt Modifiers for Text-To-Image Generation” — 2022/2023 — §§2.2, 3.2.1, 5, 6.2.1.

PASSAGE:
[PARAPHRASE]
Oppenlaender documents practitioners learning prompt techniques through community resources, social-media posts, shared prompts, guides, experimentation, and observation of others’ work. Those learned expressions are then inserted into later generations.

RESEARCH OBJECT:
Discourse surrounding an artwork can feed causally into subsequent artifacts rather than merely interpreting prior ones.

LOCAL MOVE:
This sharpens [[Z-AIACS-017]]. “Meaning-in-use” and feedback are not only joined when a platform learns from users. Human cultural circulation itself can create a feedback loop without any model retraining.

SOURCE TERMS:
“online community”
“shared”
“resources”
“experimentation”
“prompts”
“community-learning”

WHAT BECAME STRANGE:
The commentary layer can become production infrastructure while the model weights remain completely unchanged.

QUESTION:
When does criticism, discussion, or prompt-sharing stop being reception and become part of the generative apparatus?

DEEPER QUESTION:
Can an AI-art culture modify a model’s effective behavior socially without modifying the model technically?

MECHANISM:
output
→ public discussion / prompt disclosure / aesthetic judgment
→ reusable expression learned by another practitioner
→ new prompt
→ new generation
→ further public circulation

FORMAL SHIFT:
<ARTIFACT>
→ <SOCIAL DESCRIPTION / EVALUATION>
→ [REINSERT INTO PROMPT PRACTICE]
→ <NEW ARTIFACT>

SOURCE FORMALISM:
Oppenlaender documents community learning, shared prompt resources, iterative experimentation, and the movement of techniques from community discourse into prompt practice.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

No weight update is required:

G fixed

output_t
→ discourse_t
→ prompt_{t+1}
→ G(prompt_{t+1})
→ output_{t+1}

Culture changes the input distribution around a fixed generator.

TENSION:
[[Z-AIACS-017]] distinguished interpretive use from cybernetic state-changing use. Here the generator’s internal state need not change, yet reception still changes future production by changing human prompting practice.

MISSING:
Longitudinal traces linking identifiable community discussions to later changes in prompt vocabulary and output distributions.

BOUNDARY:
The source documents community transmission but does not quantify how strongly particular discussions reshape population-level generation.

CITATION TRAIL:
[[Z-AIACS-017]]
→ Oppenlaender’s online ethnography
→ shared discourse enters future prompts
→ cultural feedback without model learning
→ trace phrase propagation through generation histories

TEST:
Identify newly introduced prompt terms in timestamped community archives. Track adoption through later prompts and generated outputs while holding model version fixed. Estimate whether discourse-driven prompt diffusion produces measurable visual convergence.

PLATFORM:
[[AI Art as a Cultural System]]

LINKS:
[[Z-AIACS-017]]
[[Cultural Feedback]]
[[Prompt Diffusion]]
[[Reception Becomes Operation]]
[[Community Learning]]

BIBTEX:
@misc{Oppenlaender2022PromptModifiers,
  author = {Jonas Oppenlaender},
  title = {A Taxonomy of Prompt Modifiers for Text-To-Image Generation},
  year = {2022},
  eprint = {2204.13988},
  archivePrefix = {arXiv}
}
