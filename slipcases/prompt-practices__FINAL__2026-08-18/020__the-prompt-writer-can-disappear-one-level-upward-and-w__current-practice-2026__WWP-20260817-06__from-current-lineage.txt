ZETTEL

ID:
WWP-20260817-06

TITLE:
The prompt writer can disappear one level upward and write only the conditions from which prompts are generated.

SOURCE:
OpenAI — “Prompt generation” — OpenAI API Documentation — https://developers.openai.com/api/docs/guides/prompt-generation — accessed 2026-08-17

PASSAGE:
[PARAPHRASE] OpenAI’s Playground can generate prompts, functions, and schemas from a task description using meta-prompts and meta-schemas.

RESEARCH OBJECT:
Prompt engineering recursively consumes itself. HUMAN → TASK DESCRIPTION → META-PROMPT → GENERATED PROMPT → MODEL relocates durable work from operative wording toward goals, failure criteria, examples, evaluations, and invariants.

LOCAL MOVE:
Replace PROMPT AUTHORING with PROMPT COMPILATION.

SOURCE TERMS:
meta-prompt; prompt generation; schema generation; task description; best practices; optimization

WHAT BECAME STRANGE:
As systems improve at writing instructions, human expertise can migrate toward deciding what the instructions must accomplish rather than possessing special incantations.

QUESTION:
What remains irreducibly human in prompt engineering after the operative prompt itself is generated automatically?

DEEPER QUESTION:
Is the mature prompt engineer becoming more like a language designer who specifies conditions under which useful instructions can be synthesized?

MECHANISM:
TASK DESCRIPTION → META-PROMPT → CANDIDATE PROMPT → EVALUATION → revision/regeneration → production prompt.

FORMAL SHIFT:
AUTHOR: HUMAN→PROMPT becomes HUMAN→SPECIFICATION; COMPILER: MODEL→PROMPT.

SOURCE FORMALISM:
OpenAI documents meta-prompts for generating/improving prompts and meta-schemas for generating schemas from task descriptions.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
S → COMPILE(S) → {P1…Pn} → EVAL(Pi) → SELECT/MUTATE → P*; P* is disposable while S+EVAL may be durable.

TENSION:
Automatic generation can relocate rather than eliminate prompt engineering because the meta-prompt itself may need optimization.

MISSING:
The stopping condition: at what layer does specification become explicit enough that another meta-layer stops helping?

BOUNDARY:
The source documents tooling; the claim that specification+evaluation become the durable program is [OUR INFERENCE].

CITATION TRAIL:
[[SCGAI-004-A]] → epistemic intervention → automated prompt generation → meta-prompts → test examples+evals versus hand-authored strings.

TEST:
Compare hand-authored prompt, compiled task description, and task description+examples+evals under model migration; measure repair cost.

PLATFORM:
OpenAI Playground / automated prompt optimization systems

LINKS:
[[SCGAI-004-A]]
[[SCGAI-003]]

BIBTEX:
@misc{openai_prompt_generation, author={{OpenAI}}, title={Prompt Generation}, howpublished={OpenAI API Documentation}, url={https://developers.openai.com/api/docs/guides/prompt-generation}, note={Accessed 2026-08-17}}
