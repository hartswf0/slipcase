ZETTEL

ID:
INGOLD-PROMPT-003

TITLE:
A PROMPT MAY WORK NOT BY SPECIFYING THE RESULT BUT BY GIVING A CAPABLE SYSTEM ENOUGH GUIDANCE TO CONTINUE.

SOURCE:
Tim Ingold — Making: Anthropology, Archaeology, Art and Architecture — 2013 — Chapter 8, “Telling by Hand,” pp. 110–111.

PASSAGE:
[QUOTE]
“the story offers guidance without specification”

[PARAPHRASE]
For Ingold, telling need not exhaustively encode knowledge required for action. Stories orient attention and indicate what to notice, allowing practitioners to proceed through guided rediscovery; complete specifications can provide information without teaching anyone how to carry on.

RESEARCH OBJECT:
GUIDANCE WITHOUT COMPLETE SPECIFICATION.

LOCAL MOVE:
Ingold separates two kinds of linguistic efficacy: SPECIFICATION states enough information to define a project; TELLING orients a knowledgeable practitioner so they can find their way. This destabilizes the assumption that natural-language programming works because English has become a high-level specification language.

SOURCE TERMS:
telling; story; specification; guidance; guided rediscovery; attention; project; itinerary; carry on

WHAT BECAME STRANGE:
An LLM may act on a vague prompt for the same structural reason an expert acts on incomplete instructions: the prompt does not contain all the knowledge. It recruits a system that already contains—or reconstructs—ways of continuing.

QUESTION:
Where is the information that makes an underspecified prompt executable?

DEEPER QUESTION:
Does deferred formalization describe information progressively added by the USER, or information progressively selected from capabilities already latent in the MODEL?

MECHANISM:
A linguistic utterance directs attention and establishes direction; a competent practitioner supplies situational knowledge not encoded in the utterance; action reveals circumstances; guidance and competence jointly determine continuation.

FORMAL SHIFT:
<LANGUAGE AS COMPLETE SPECIFICATION>
→ <LANGUAGE AS GUIDANCE>
→ [RECRUIT PRIOR COMPETENCE + SITUATED JUDGEMENT]
→ <CONTINUED ACTION>

SOURCE FORMALISM:
Ingold explicitly distinguishes SPECIFICATION WITHOUT GUIDANCE from GUIDANCE WITHOUT SPECIFICATION and contrasts PROJECT with ITINERARY.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
OUTPUT = PROMPT + MODEL PRIORS + CONTEXT + DEFAULTS + INFERENCE + TOOL BEHAVIOR + ITERATIVE CORRECTION. The prompt may function as INDEX rather than COMPLETE DESCRIPTION.

TENSION:
“The Prompt Is Not the Program” argues formalization is delayed. Ingold suggests a rival reading: some apparent deferred formalization is never formalized by the user at all; it is delegated to prior competence.

MISSING:
A method to distinguish USER-SUPPLIED CONSTRAINT, MODEL-INFERRED CONSTRAINT, PLATFORM DEFAULT, TRAINING-INDUCED CONVENTION, TOOL-IMPOSED CONSTRAINT.

BOUNDARY:
Ingold’s story/specification distinction concerns skilled practice and education, not LLM inference; prompt-as-guidance is [OUR INFERENCE].

CITATION TRAIL:
[[THE PROMPT IS NOT THE PROGRAM]] → Ingold — “Telling by Hand” → Polanyi → Alexander → Winograd/SHRDLU → programming by example → program synthesis from partial specifications.

TEST:
Give the same short prompt to models with substantially different priors or tool environments; keep wording constant and record unstated constraints each system supplies.

PLATFORM:
[[THE PROMPT IS NOT THE PROGRAM]]

LINKS:
[[THE PROMPT IS NOT THE PROGRAM]]
[[PROMPT AS GUIDANCE]]
[[GUIDANCE WITHOUT SPECIFICATION]]

BIBTEX:
@book{ingold2013making_telling,
  author = {Ingold, Tim},
  title = {Making: Anthropology, Archaeology, Art and Architecture},
  publisher = {Routledge},
  year = {2013},
  doi = {10.4324/9780203559055}
}
