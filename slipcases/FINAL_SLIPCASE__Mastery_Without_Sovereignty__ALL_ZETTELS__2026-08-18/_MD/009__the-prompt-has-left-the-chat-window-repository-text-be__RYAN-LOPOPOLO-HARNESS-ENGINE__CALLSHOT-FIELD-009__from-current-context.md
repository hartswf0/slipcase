ZETTEL

ID:
CALLSHOT-FIELD-009

TITLE:
THE PROMPT HAS LEFT THE CHAT WINDOW: REPOSITORY TEXT BECOMES AMBIENT INSTRUCTION FOR FUTURE AGENTS.

SOURCE:
Ryan Lopopolo, “Harness engineering: leveraging Codex in an agent-first world,” OpenAI, 2026-02-11. SOURCE URL: https://openai.com/index/harness-engineering/

PASSAGE:
[QUOTE]
“we treat it as the table of contents.”

RESEARCH OBJECT:
AGENT INSTRUCTION IS BECOMING AN ENVIRONMENTAL PROPERTY OF THE WORKSPACE RATHER THAN A TURN-BY-TURN UTTERANCE.

LOCAL MOVE:
OpenAI describes a short AGENTS.md injected into context and used as a map to structured repository documentation. The operative instructions already exist in the work environment before a user asks the next task.

SOURCE TERMS:
“AGENTS.md” · “table of contents” · “system of record” · “repository knowledge” · “map”

WHAT BECAME STRANGE:
The workspace begins to speak. Files intended partly for artificial workers become part of the causal environment of future action.

QUESTION:
What is the complete effective prompt when relevant instructions are distributed across a repository?

DEEPER QUESTION:
Are persistent instruction files a new architectural layer: textual infrastructure that structures action without being restated by the current speaker?

MECHANISM:
USER TASK + AMBIENT INSTRUCTIONS + LOCAL STATE + RETRIEVED DOCS → AGENT ACTION.

FORMAL SHIFT:
PROMPT AS UTTERANCE → PROMPT AS INSTRUCTION ENVIRONMENT.

SOURCE FORMALISM:
[PARAPHRASE]
OpenAI reports that a monolithic AGENTS.md failed and that a shorter file works as a map to deeper repository sources of truth.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
EFFECTIVE_PROMPT_t = REQUEST_t + AMBIENT_INSTRUCTIONS(repo) + RETRIEVED_DOCS(repo) + LOCAL_STATE(repo).

TENSION:
Persistent context improves consistency but makes the complete causal instruction set less visible and creates stale-rule inheritance.

MISSING:
Action-level provenance showing exactly which ambient instructions were loaded and influential.

BOUNDARY:
This is one contemporary engineering pattern, not a universal agent architecture.

CITATION TRAIL:
[[CALLSHOT-20260817-03]] → persistent context → OpenAI harness engineering → instruction becomes environmental.

TEST:
Run identical repository tasks with rules in user prompts, one monolithic AGENTS.md, short map + deep docs, and no persistent instructions. Measure success, drift, context cost, and traceability.

PLATFORM:
Codex · AGENTS.md · software repositories

LINKS:
[[CALLSHOT-20260817-03]] [[CALLSHOT-FIELD-010]] [[CALLSHOT-FIELD-014]]

BIBTEX:
@misc{Lopopolo2026Harness, author={Lopopolo, Ryan}, title={Harness engineering: leveraging Codex in an agent-first world}, year={2026}, month=feb, url={https://openai.com/index/harness-engineering/}}
