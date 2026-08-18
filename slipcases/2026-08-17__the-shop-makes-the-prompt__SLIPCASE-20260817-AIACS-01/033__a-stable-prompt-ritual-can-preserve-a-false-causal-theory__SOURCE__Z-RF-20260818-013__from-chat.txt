ZETTEL

ID:
Z-RF-20260818-013

TITLE:
A stable prompt ritual can preserve a false causal theory.

SOURCE:
Jonas Oppenlaender — “A Taxonomy of Prompt Modifiers for Text-To-Image Generation” — 2022/2023 — §6.2.2, discussion of workflows, idiosyncratic choices, and folk theories.

PASSAGE:
[PARAPHRASE]
Oppenlaender notes that practitioners make idiosyncratic choices such as particular seeds or canvas dimensions and explicitly raises the possibility that some such practices are folk theories: causal attributions that may or may not be true.

RESEARCH OBJECT:
Community persistence is evidence that a practice is socially real, not evidence that its causal explanation is technically correct.

LOCAL MOVE:
This puts [[Z-RF-20260817-004]] under opposition. A prompt term can acquire an operational reputation through experimentation and circulation while the community misidentifies why the observed effect occurred.

SOURCE TERMS:
“idiosyncratic choices”
“folk theories”
“causal attributions”
“may or may not be true”
“experimentation”
“experience”

WHAT BECAME STRANGE:
The same trial-and-error process that produces expertise can also produce superstition.

QUESTION:
How do prompt communities distinguish robust operators from lucky correlations?

DEEPER QUESTION:
Does stochastic generation make prompt culture unusually hospitable to technically false but culturally durable causal beliefs?

MECHANISM:
prompt variation
→ stochastic output
→ salient desirable result
→ causal attribution to recent modification
→ repetition / sharing
→ community convention

without necessarily establishing:

modification
→ causal effect

FORMAL SHIFT:
<OBSERVED CO-OCCURRENCE>
→ <PRACTITIONER CAUSAL ATTRIBUTION>
→ [SOCIAL REPLICATION]
→ <STABILIZED TECHNIQUE OR FOLK THEORY>

SOURCE FORMALISM:
The source explicitly distinguishes practitioner choices grounded in experimentation from possible folk theories whose causal attribution may be false.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

SOCIAL_STABILITY(term)
≠
CAUSAL_EFFECT(term)

A useful test requires:

same prompt
same model/configuration
many seeds
with_modifier / without_modifier

rather than remembered exemplary outputs.

TENSION:
[[Z-RF-20260817-004]] treats prompt modifiers as experimentally acquired operators. Oppenlaender’s own later discussion blocks a simple inference from acquired practice to genuine mechanism.

MISSING:
Controlled ablation studies of historically important “magic terms,” quality boosters, repeated terms, seed rituals, and dimension-specific prompt lore.

BOUNDARY:
The source proposes folk theory as a possibility for some practitioner choices. It does not demonstrate that any particular named modifier is causally inert.

CITATION TRAIL:
[[Z-RF-20260817-004]]
→ Oppenlaender §6.2.2
→ practitioner folk theories
→ distinguish cultural efficacy from computational efficacy
→ experimentally ablate prompt lore

TEST:
Select twenty widely circulated prompt prescriptions. For each one, preregister the claimed effect and evaluate it across many matched generations, seeds, subjects, and model versions. Preserve separately:
technical effect,
perceived effect,
community belief,
and historical persistence.

PLATFORM:
[[Prompt Vernacular]]

LINKS:
[[Z-RF-20260817-004]]
[[Prompt Folk Theory]]
[[Magic Terms]]
[[Operational Semantics]]
[[Causal Hallucination]]

BIBTEX:
@misc{Oppenlaender2022PromptModifiers,
  author = {Jonas Oppenlaender},
  title = {A Taxonomy of Prompt Modifiers for Text-To-Image Generation},
  year = {2022},
  eprint = {2204.13988},
  archivePrefix = {arXiv},
  primaryClass = {cs.MM}
}
