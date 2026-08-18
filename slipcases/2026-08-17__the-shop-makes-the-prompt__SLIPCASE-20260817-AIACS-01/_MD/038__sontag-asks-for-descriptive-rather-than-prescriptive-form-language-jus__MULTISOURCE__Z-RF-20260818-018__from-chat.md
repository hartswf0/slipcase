ZETTEL

ID:
Z-RF-20260818-018

TITLE:
Sontag asks for descriptive rather than prescriptive form-language just before prompting makes description prescriptive.

SOURCE:
Susan Sontag — “Against Interpretation” — 1964; collected in Against Interpretation and Other Essays — 1966 — §§8–10.
Jonas Oppenlaender — “A Taxonomy of Prompt Modifiers for Text-To-Image Generation” — 2022/2023.

PASSAGE:
[PARAPHRASE]
Sontag asks criticism to develop a descriptive rather than prescriptive vocabulary for artistic forms and argues that criticism should reveal how a work is what it is rather than extract hidden meaning.

[PARAPHRASE]
In text-to-image systems, practitioners use textual descriptions and modifiers precisely to alter style, quality, subject, and other aspects of the produced image.

RESEARCH OBJECT:
The same aesthetic vocabulary can change causal position: after an artwork it describes form; before generation it can prescribe form.

LOCAL MOVE:
This changes the Sontag/Geertz opposition in [[Z-AIACS-013]]. Generative systems do not merely invite another theory of interpretation. They can move critical language upstream into production.

SOURCE TERMS:
Sontag:
“descriptive”
“prescriptive”
“vocabulary”
“forms”
“how it is what it is”

Oppenlaender:
“style modifier”
“quality booster”
“prompt”
“control”

WHAT BECAME STRANGE:
A sentence such as “high contrast, shallow depth of field, asymmetrical composition” can be criticism in one temporal position and control syntax in another.

QUESTION:
What happens to aesthetic criticism when its descriptive vocabulary doubles as an executable production interface?

DEEPER QUESTION:
Can a culture’s vocabulary for noticing form become the control surface through which future forms are statistically reproduced?

MECHANISM:
historically:

artwork
→ critic observes form
→ descriptive vocabulary

generatively:

descriptive vocabulary
→ prompt conditioning
→ artwork

FORMAL SHIFT:
<AESTHETIC DESCRIPTION>
→ <MODEL CONDITIONING>
→ [GENERATE]
→ <FORM BEARING FEATURES NAMED BY THE DESCRIPTION>

SOURCE FORMALISM:
Sontag explicitly distinguishes descriptive from prescriptive vocabulary.

Oppenlaender identifies style modifiers, quality boosters, subject terms, repetition, image prompts, and related devices for directing image generation.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

CRITICISM:
FORM → WORD

PROMPTING:
WORD → CONDITIONING → FORM

Generative systems partially reverse the arrow.

TENSION:
Sontag wants description to resist the domination of art by interpretation. Once descriptive form-language becomes generative control, even non-hermeneutic description can participate in standardizing what future art looks like.

MISSING:
Evidence showing whether aesthetic vocabulary taken from criticism and art history measurably narrows or expands generated formal possibilities.

BOUNDARY:
A prompt does not literally execute natural language as deterministic code. The reverse-arrow formalization describes causal conditioning, not exact compilation.

CITATION TRAIL:
[[Z-AIACS-013]]
→ Sontag, “Against Interpretation”
→ descriptive versus prescriptive vocabulary
→ Oppenlaender’s prompt modifiers
→ description migrates from criticism into generation
→ test whether critical vocabulary becomes aesthetic prior

TEST:
Build paired corpora of formal art criticism and prompt-language modifiers. Identify migrated terms, then measure whether frequent critical descriptors systematically induce recurrent compositional or stylistic features across model generations.

PLATFORM:
[[Art as Cultural System & AI Prompting]]

LINKS:
[[Z-AIACS-013]]
[[Z-AIACS-017]]
[[Against Interpretation]]
[[Description Becomes Operation]]
[[Operative Ekphrasis]]

BIBTEX:
@book{Sontag1966AgainstInterpretation,
  author = {Susan Sontag},
  title = {Against Interpretation and Other Essays},
  publisher = {Farrar, Straus and Giroux},
  year = {1966}
}

@misc{Oppenlaender2022PromptModifiers,
  author = {Jonas Oppenlaender},
  title = {A Taxonomy of Prompt Modifiers for Text-To-Image Generation},
  year = {2022},
  eprint = {2204.13988},
  archivePrefix = {arXiv}
}
