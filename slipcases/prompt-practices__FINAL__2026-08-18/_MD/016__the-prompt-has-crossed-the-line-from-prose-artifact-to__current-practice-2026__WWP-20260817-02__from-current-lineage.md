ZETTEL

ID:
WWP-20260817-02

TITLE:
The prompt has crossed the line from prose artifact to versioned software artifact.

SOURCE:
OpenAI — “Prompting” — OpenAI API Documentation — https://developers.openai.com/api/docs/guides/prompting — accessed 2026-08-17

PASSAGE:
[QUOTE] “Treat prompts as application code.”

RESEARCH OBJECT:
Production guidance makes a category move: prompts can live in named modules, receive typed inputs, accumulate tests/evaluations, retain git histories, pass review, receive release tags, and support rollback.

LOCAL MOVE:
Replace PROMPT DOCUMENT with PROMPT SOFTWARE OBJECT.

SOURCE TERMS:
application code; named modules; typed arguments; tests; fixtures; evaluation checks; git history; PR review; release tags; feature flags; rollback

WHAT BECAME STRANGE:
A prompt without its tests can resemble source code without its test suite; a prompt without its version may no longer identify a reproducible object.

QUESTION:
What is the minimum reproducible unit of a contemporary prompt practice?

DEEPER QUESTION:
If prompt changes are reviewed, tested, versioned, compared, and rolled back like program changes, what remains of the distinction between prompt text and program text?

MECHANISM:
PROMPT → named module → typed variables → fixtures/evals → revision → diff → review → deployment → observed behavior → rollback/next revision.

FORMAL SHIFT:
PROMPT=STRING becomes PROMPT_OBJECT={TEXT, INPUT_SCHEMA, TESTS, EVALS, VERSION, CHANGE_HISTORY, DEPLOYMENT_CONTEXT}.

SOURCE FORMALISM:
OpenAI recommends code-managed production prompts, typed/validated inputs, test/evaluation coverage, git history, review, release tags, and deployment controls.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
PROMPT_IDENTITY = CONTENT_HASH + TEST_SET + MODEL_TARGET + VERSION + DEPENDENCIES.

TENSION:
Version control captures textual ancestry more easily than conceptual ancestry: why a phrase entered, what failure it solved, or whose practice it borrowed.

MISSING:
A provenance representation for failure observed, source borrowed, model migration, user preference, evaluation regression, community discovery, and theoretical commitment.

BOUNDARY:
Production engineering guidance does not imply every casual or creative prompt needs software-development infrastructure.

CITATION TRAIL:
[[SCGAI-003]] → modification over time → [[SCGAI-008]] → contribution tracking → prompt-as-code guidance → prompt repositories as executable genealogies.

TEST:
Compare final-prompt-only versus prompt+commits+failed outputs+tests+rationales when a new practitioner must safely modify a mature prompt.

PLATFORM:
Production LLM applications / prompt repositories

LINKS:
[[SCGAI-003]]
[[SCGAI-008]]

BIBTEX:
@misc{openai_prompting, author={{OpenAI}}, title={Prompting}, howpublished={OpenAI API Documentation}, url={https://developers.openai.com/api/docs/guides/prompting}, note={Accessed 2026-08-17}}
