ZETTEL

ID:
CALLSHOT-FIELD-012

TITLE:
THE HIGH-VALUE PROMPT BECOMES INDEXICAL: POINT TO THE PRECEDENT, NAME THE DELTA, AND LET THE WORKSPACE CARRY THE REST.

SOURCE:
OpenAI, “How OpenAI uses Codex,” current guide accessed 2026-08-17. SOURCE URL: https://openai.com/business/guides-and-resources/how-openai-uses-codex/

PASSAGE:
[QUOTE]
“Structure your prompt as if you are writing a Github Issue”

RESEARCH OBJECT:
OPERATIVE PROMPTS CAN COMPRESS SPECIFICATION BY POINTING INTO EXISTING ARTIFACTS RATHER THAN RESTATING THEIR RULES.

LOCAL MOVE:
OpenAI recommends concrete file paths, component names, diffs, documentation snippets, and instructions such as implementing something the same way as an existing module.

SOURCE TERMS:
“Github Issue” · “file paths” · “component names” · “diffs” · “doc snippets” · “same way”

WHAT BECAME STRANGE:
“Do it like that thing over there” can convey more operative structure than a much longer self-contained description because the referenced artifact becomes part of the specification.

QUESTION:
When should practitioners explain a rule versus point to an executable precedent?

DEEPER QUESTION:
Does agentic work create a demonstrative programming language of HERE, THERE, THIS, LIKE THAT, EXCEPT THIS?

MECHANISM:
TARGET + EXEMPLAR + DELTA + INVARIANTS → AGENT INSPECTS → INFERS LOCAL PATTERN → TRANSFORMS TARGET → TESTS.

FORMAL SHIFT:
SELF-CONTAINED DESCRIPTION → INDEXICAL SPECIFICATION.

SOURCE FORMALISM:
[PARAPHRASE]
OpenAI’s Codex guide recommends prompts resembling engineering issues/PRs and including direct references into the codebase and documentation.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
SPEC=(TARGET, EXEMPLAR, Δ, INVARIANTS). Meaning depends on dereferencing the workspace.

TENSION:
Exemplars compress good structure and accidental quirks alike. Reference creates implicit inheritance.

MISSING:
A reliable way to state which properties of an exemplar should and should not transfer.

BOUNDARY:
The pattern depends on the agent having access to stable, inspectable reference artifacts.

CITATION TRAIL:
[[CALLSHOT-20260817-09]] → indexical prompting → [[CALLSHOT-FIELD-009]] ambient environment → [[CALLSHOT-FIELD-013]] tests constrain inherited ambiguity.

TEST:
Compare complete prose, exemplar-only, exemplar+delta, and exemplar+delta+tests. Measure prompt length, accuracy, unintended copied properties, and resilience to exemplar changes.

PLATFORM:
Codex · GitHub · software engineering

LINKS:
[[CALLSHOT-20260817-09]] [[CALLSHOT-FIELD-009]] [[CALLSHOT-FIELD-013]]

BIBTEX:
@misc{OpenAIUsesCodex2026, author={{OpenAI}}, title={How OpenAI uses Codex}, year={2026}, url={https://openai.com/business/guides-and-resources/how-openai-uses-codex/}}
