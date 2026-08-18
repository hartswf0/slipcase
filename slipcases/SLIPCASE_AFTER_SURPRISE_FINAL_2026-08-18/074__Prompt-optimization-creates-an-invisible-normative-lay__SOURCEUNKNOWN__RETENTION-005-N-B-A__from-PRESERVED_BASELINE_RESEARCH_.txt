ZETTEL

ID:
RETENTION-005-N-B-A

TITLE:
Prompt optimization creates an invisible normative layer because “better translation” is defined by an objective function.

SOURCE:
Yaru Hao, Zewen Chi, Li Dong, and Furu Wei — “Optimizing Prompts for Text-to-Image Generation” — 2022.

PASSAGE:
[PARAPHRASE]
Promptist rewrites user input into model-preferred prompts, optimizing for aesthetically pleasing generated images while attempting to preserve intention.

RESEARCH OBJECT:
PROMPT TRANSLATION HAS AN OBJECTIVE FUNCTION.

LOCAL MOVE:
The hidden translator is also a CRITIC; it decides how words should change according to an output-quality objective.

SOURCE TERMS:
model-preferred prompts
prompt adaptation
reward
aesthetic quality
user intention
reinforcement learning

WHAT BECAME STRANGE:
“Better translation” can mean aesthetic optimization, not semantic equivalence.

QUESTION:
Whose aesthetics are embedded in the objective function that rewrites the artist’s request before generation?

DEEPER QUESTION:
Can a system preserve semantic intent while systematically substituting another agent’s aesthetic policy?

MECHANISM:
q → adaptation policy O optimized for reward(aesthetic_score + intent_preservation) → p* → generator.

FORMAL SHIFT:
<TRANSLATION> → <TRANSLATION + NORMATIVE OPTIMIZATION>

SOURCE FORMALISM:
The method trains an adaptation policy using supervised learning and reinforcement learning with aesthetic and intent-preservation objectives.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
O(q|J), where objective J is part of the causal authorship chain; different J can yield different p* from identical q.

TENSION:
All interfaces encode objectives; explicit optimization may be more inspectable than tacit defaults.

MISSING:
Sensitivity analysis swapping aesthetic reward models while holding user prompt/generator fixed.

BOUNDARY:
Automatic prompt optimization is not neutral plumbing; its objective participates in the artistic causal chain.

CITATION TRAIL:
[[RETENTION-005-N-B]] → machine dialect → Promptist → aesthetics+intent objective → hidden translator becomes normative intermediary.

TEST:
Swap only prompt optimizer reward and compare rewritten text, output style, intent preservation, user preference.

PLATFORM:
[[class-is-not-a-path]]

LINKS:
[[RETENTION-005-N-B]]
[[promptist]]
[[normative-translation]]
[[objective-function]]
[[hidden-critic]]

BIBTEX:
NONE
