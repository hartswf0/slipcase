ZETTEL

ID:
PROMPT-GENRE-20260922-005

TITLE:
The prompt can be larger than its transcript

SOURCE:
Richard A. Bolt, "Put-That-There: Voice and Gesture at the Graphics Interface," SIGGRAPH, 1980.

SOURCE URL:
https://www.media.mit.edu/speech/papers/1980/bolt_SIGGRAPH80_put-that-there.pdf

PASSAGE:
[PARAPHRASE]\nPut-That-There combines speech with pointing and display context so pronouns can refer economically to visible objects and destinations.

RESEARCH OBJECT:
[OUR INFERENCE]\nTHE EFFECTIVE PROMPT INCLUDES SITUATED, MULTIMODAL STATE THAT MAY NOT APPEAR IN THE TEXT TRANSCRIPT.

LOCAL MOVE:
Make deixis a central counterexample to text-only prompt analysis.

SOURCE TERMS:
deixis; gesture; pointing; context; reference

WHAT BECAME STRANGE:
Remove the gesture and shared screen state and the phrase 'put that there' loses its referents.

QUESTION:
What must be archived to reconstruct a prompt when the string alone is insufficient?

DEEPER QUESTION:
How should provenance systems represent cursor, mask, gaze, viewport, selection, attached media, prior turns, and tool state?

MECHANISM:
Speech supplies a relation while gesture binds variables to entities already present in the field.

FORMAL SHIFT:
TRANSCRIPT(P) is a strict subset of EFFECTIVE_INPUT(P).

SOURCE FORMALISM:
[PARAPHRASE]\nVoice and gesture are interpreted together against the graphical situation.

OUR FORMALIZATION:
P_effective = text + gesture + selected referent + scene state + interaction history.

TENSION:
Richer context makes interaction economical but makes later reconstruction harder.

MISSING:
Standard archival representation for multimodal prompt state.

BOUNDARY:
Put-That-There is a graphics interface, not a generative AI system.

CITATION TRAIL:
Bolt -> deixis -> transcript insufficiency -> situated prompt.

TEST:
Replay the same transcript with different gesture traces and show divergent valid interpretations.

PLATFORM:
Deixis; multimodal HCI; prompting

LINKS:
[[PROMPT-GENRE-20260922-001]]
[[PROMPT-GENRE-20260922-006]]
[[PROMPT-GENRE-20260922-018]]

BIBTEX:
@inproceedings{bolt1980put,
  author={Bolt, Richard A.},
  title={Put-That-There: Voice and Gesture at the Graphics Interface},
  booktitle={Proceedings of SIGGRAPH 1980},
  pages={262--270},
  year={1980}
}
