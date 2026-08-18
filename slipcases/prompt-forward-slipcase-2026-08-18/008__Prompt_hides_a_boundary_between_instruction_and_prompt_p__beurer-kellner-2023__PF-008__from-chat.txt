ZETTEL

ID: PF-008

TITLE:
“Prompt” hides a boundary between instruction and prompt program.

SOURCE:
Beurer-Kellner, Fischer, and Vechev — Prompting Is Programming: A Query Language for Large Language Models — 2023.

PASSAGE:
[PARAPHRASE] LMQL combines natural-language prompting with scripting, constraints, and control flow so that model interaction can be programmed rather than expressed only as free-form instructions.

RESEARCH OBJECT:
Some prompt artifacts already contain executable control structures not present in ordinary natural-language requests.

LOCAL MOVE:
LMQL turns prompt construction into a hybrid language-programming problem.

SOURCE TERMS:
language model programming; constraints; control flow; query language.

WHAT BECAME STRANGE:
“Write my literature review” and an LMQL program are not merely prompts of different quality; they may belong to different computational forms.

QUESTION:
Where should the boundary between prompt, prompt program, and generative application be drawn?

DEEPER QUESTION:
Does scholarly evaluation need to classify the artifact's computational structure before evaluating its contribution?

MECHANISM:
<natural-language task + program structure>
→ <LMQL representation>
→ [constrained model execution]
→ <controlled output>

FORMAL SHIFT:
<prompt intention>
→ <query program>
→ [execute with constraints/control flow]
→ <model output>

SOURCE FORMALISM:
LMQL syntax and execution model.

OUR FORMALIZATION:
NONE

TENSION:
A theory that calls every model-facing instruction a “prompt” may erase precisely the technical differentiation it wants academia to recognize.

MISSING:
A taxonomy from free-text instruction through structured prompt programs to full agent systems.

BOUNDARY:
LMQL demonstrates one programming approach, not the universal native form of prompting.

CITATION TRAIL:
DSPy; Guidance; prompt templates; agent workflow languages.

TEST:
Classify one hundred published LLM systems by whether their model-facing artifacts are text instructions, structured templates, constrained programs, or graph-level pipelines.

PLATFORM:
[[Prompt Is Too Broad a Unit]]

LINKS:
[[LMQL]]
[[Prompt Program]]
[[Generative Application]]

BIBTEX:
@inproceedings{beurerkellner2023lmql,
  author={Luca Beurer-Kellner and Marc Fischer and Martin Vechev},
  title={Prompting Is Programming: A Query Language for Large Language Models},
  booktitle={Proceedings of the ACM SIGPLAN Conference on Programming Language Design and Implementation},
  year={2023},
  pages={1946--1969}
}