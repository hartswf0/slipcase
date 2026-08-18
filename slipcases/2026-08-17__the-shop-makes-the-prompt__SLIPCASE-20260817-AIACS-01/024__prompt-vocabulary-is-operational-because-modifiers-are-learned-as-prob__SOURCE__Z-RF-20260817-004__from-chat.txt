ZETTEL

ID:
Z-RF-20260817-004

TITLE:
Prompt vocabulary is operational because modifiers are learned as probes.

SOURCE:
Jonas Oppenlaender — “A Taxonomy of Prompt Modifiers for Text-To-Image Generation” — arXiv:2204.13988v3, 2023; related journal DOI 10.1080/0144929X.2023.2286532.

PASSAGE:
[PARAPHRASE]
Oppenlaender’s three-month ethnographic and autoethnographic study identifies six classes of prompt modifier. Practitioners repeatedly run a prompt, inspect its outcome, and modify the prompt; the paper explicitly describes prompts as probes into the model’s latent space.

RESEARCH OBJECT:
Prompt vocabulary is not simply a lexicon of descriptions. It is a repertoire of experimentally acquired interventions.

LOCAL MOVE:
The source sharpens [[Z-AIACS-005]] by replacing the loose idea of a “prompt dialect” with observed classes of modifier and a documented practice for discovering their effects.

SOURCE TERMS:
“prompt modifiers”
“prompt engineering”
“iterative”
“experimental”
“probes”
“latent space”

WHAT BECAME STRANGE:
A word can enter prompt culture because of what repeated generations show that it does, not because its ordinary-language definition predicts its effect.

QUESTION:
When practitioners circulate a modifier, what exactly is being transmitted: semantic meaning, a causal hypothesis, an empirical recipe, or a remembered correlation with desirable outputs?

DEEPER QUESTION:
Could prompt vernacular be modeled less like a natural-language dialect and more like an evolving library of experimentally discovered operators?

MECHANISM:
candidate phrase
→ generation
→ observed effect
→ repeated experiment
→ community circulation
→ conventional modifier role

FORMAL SHIFT:
<natural-language phrase>
→ <community prompt modifier>
→ [APPLY AS PROBE]
→ <observed generative displacement>

SOURCE FORMALISM:
Oppenlaender identifies six categories of prompt modifier and documents an iterative practice in which practitioners run prompts, observe outcomes, and adapt subsequent prompts.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

A prompt expression e has at least:

SEMANTIC_ROLE(e)
OPERATIONAL_ROLE(e, model, configuration)
COMMUNITY_ROLE(e, practice)

These roles need not coincide.

TENSION:
Calling prompt practice a “language” suggests relatively stable meanings. The source instead describes an experimental craft whose terms acquire practical force through model-contingent observation.

MISSING:
Longitudinal evidence showing how individual modifiers change operational role when models, interfaces, or aesthetic norms change.

BOUNDARY:
The taxonomy documents practice in an early text-to-image community centered substantially on VQGAN–CLIP-era systems. It does not establish universal modifier categories across later generators.

CITATION TRAIL:
[[Z-AIACS-005]]
→ Oppenlaender, “A Taxonomy of Prompt Modifiers”
→ modifier classes + prompts as probes
→ operational vocabulary rather than merely stylistic vocabulary
→ follow modifiers across model generations

TEST:
Select historically common prompt modifiers from archived guides. Execute them unchanged on every recoverable model version. Compare their ordinary-language meaning, measured image effect, and community-described function at each date.

PLATFORM:
[[Prompt Vernacular]]

LINKS:
[[Z-AIACS-005]]
[[Operational Semantics]]
[[Prompt Modifiers]]
[[Prompts as Probes]]

BIBTEX:
@misc{Oppenlaender2022PromptModifiers,
  author = {Jonas Oppenlaender},
  title = {A Taxonomy of Prompt Modifiers for Text-To-Image Generation},
  year = {2022},
  eprint = {2204.13988},
  archivePrefix = {arXiv},
  primaryClass = {cs.MM},
  doi = {10.48550/arXiv.2204.13988}
}
