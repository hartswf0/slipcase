ZETTEL

ID:
Z-RF-20260818-020

TITLE:
The most Geertzian object may be the distinction a practitioner learns to notice.

SOURCE:
Clifford Geertz — “Art as a Cultural System” — 1976 — especially p. 1497.
Jonas Oppenlaender, Rhema Linder, Johanna Silvennoinen — “Prompting AI Art: An Investigation into the Creative Skill of Prompt Engineering” — 2023 — arXiv:2303.13534.

PASSAGE:
[PARAPHRASE]
Geertz argues that capacities for aesthetic response are brought into actual existence through experience within particular worlds of things, practices, and distinctions.

[PARAPHRASE]
Oppenlaender, Linder, and Silvennoinen found that participants could judge prompt quality and write descriptive prompts but lacked the style-specific vocabulary needed for effective prompting; the authors conclude that prompt engineering is a non-intuitive skill acquired through practice and learning.

RESEARCH OBJECT:
Prompt expertise may be less about accumulating words than acquiring perceptual distinctions that make certain words worth trying.

LOCAL MOVE:
This deepens [[Z-RF-20260817-009]]. “Equipment to grasp” can be operationalized as the difference between what novices and practitioners are capable of noticing, naming, and correcting.

SOURCE TERMS:
Geertz:
“equipment to grasp”
“experience”

Oppenlaender et al.:
“style-specific vocabulary”
“skill”
“practice”
“learning”
“refine prompts”

WHAT BECAME STRANGE:
A novice and expert can look at the same failed generation yet inhabit different actionable worlds because only one sees what distinction should become the next instruction.

QUESTION:
Is the deepest unit of prompt expertise a word, or a learned capacity to detect a correctable difference?

DEEPER QUESTION:
Could we reconstruct an AI-art culture by cataloguing not its preferred styles but the failures its members have learned to see?

MECHANISM:
repeated generation
→ encounter with outputs
→ socially learned aesthetic distinctions
→ detection of specific mismatch
→ vocabulary attached to mismatch
→ targeted correction

FORMAL SHIFT:
<OUTPUT>
→ <PERCEPTUALLY AVAILABLE DIFFERENCE>
→ [NAME / CORRECT]
→ <NEXT GENERATIVE ACTION>

SOURCE FORMALISM:
The prompt-skill study distinguishes prompt evaluation, prompt writing, and prompt refinement, and identifies lack of style-specific vocabulary among inexperienced participants.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

EXPERTISE is not merely:

lexicon size

but:

NOTICE(output, desired_state)
→ discriminable difference d
→ associate intervention i
→ test i

Culture may reside in the learned mapping:

d → i

TENSION:
A lexical account says experts know special prompt terms. A Geertzian account suggests those terms matter because practitioners have acquired sensitivities that make certain differences salient in the first place.

MISSING:
Process evidence showing what experts perceive before they choose a modifier, rather than only recording the modifier they eventually type.

BOUNDARY:
The empirical prompt study shows differences in skill and vocabulary. It does not establish that perceptual discrimination is the causal source of those differences.

CITATION TRAIL:
[[Z-RF-20260817-009]]
→ Geertz’s acquired aesthetic equipment
→ Oppenlaender et al., prompt skill
→ vocabulary versus perceptual distinction
→ instrument the moment before prompt revision

TEST:
Give novices and experts identical imperfect generations and require them to mark every noticed discrepancy before allowing prompt editing. Compare discrepancy categories, granularity, correction choices, and successful subsequent generations. Track which distinctions novices acquire through training.

PLATFORM:
[[AI Art as a Cultural System]]

LINKS:
[[Z-RF-20260817-009]]
[[Equipment to Grasp]]
[[Prompt Expertise]]
[[Failure Becomes Specification]]
[[Aesthetic Attention]]

BIBTEX:
@article{Geertz1976ArtCulturalSystem,
  author = {Clifford Geertz},
  title = {Art as a Cultural System},
  journal = {MLN},
  volume = {91},
  number = {6},
  year = {1976},
  pages = {1473--1499}
}

@misc{OppenlaenderLinderSilvennoinen2023PromptingAIArt,
  author = {Jonas Oppenlaender and Rhema Linder and Johanna Silvennoinen},
  title = {Prompting AI Art: An Investigation into the Creative Skill of Prompt Engineering},
  year = {2023},
  eprint = {2303.13534},
  archivePrefix = {arXiv}
}
