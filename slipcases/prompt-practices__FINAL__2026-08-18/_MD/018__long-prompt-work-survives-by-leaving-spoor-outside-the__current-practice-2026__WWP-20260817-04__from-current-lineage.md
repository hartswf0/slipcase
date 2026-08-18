ZETTEL

ID:
WWP-20260817-04

TITLE:
Long prompt work survives by leaving spoor outside the conversation.

SOURCE:
Anthropic — “Prompting best practices” — Claude Platform Documentation — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices — accessed 2026-08-17

PASSAGE:
[QUOTE] “Review progress.txt, tests.json, and the git logs.”

RESEARCH OBJECT:
Work spanning context windows can externalize state into files, tests, scripts, and repository history so a fresh context reconstructs where the task stands. Continuity moves from retained conversation to recoverable environment.

LOCAL MOVE:
Replace MAKE THE MODEL REMEMBER with MAKE THE WORK REDISCOVERABLE.

SOURCE TERMS:
multiple context windows; tests.json; progress.txt; git logs; setup scripts; verification tools; filesystem; fresh context

WHAT BECAME STRANGE:
A fresh model context can possess continuity without possessing memory of the previous conversation. The agent forgets; the workspace remembers.

QUESTION:
What traces must work leave behind so a fresh agent can reconstruct operative state without inheriting the prior conversation?

DEEPER QUESTION:
Could prompt practice become deliberately amnesiac—periodically discarding conversation while preserving externally testable state?

MECHANISM:
CONTEXT1 performs work → commits artifacts/state/tests → context disappears → CONTEXT2 inspects workspace → reconstructs state → verifies → continues.

FORMAL SHIFT:
MEMORY=CONVERSATION HISTORY becomes MEMORY=RECONSTRUCT(ARTIFACTS, TESTS, LOGS, STATE_FILES, VERSION_HISTORY).

SOURCE FORMALISM:
Anthropic recommends structured tests, setup scripts, progress artifacts, git logs, verification tools, and explicit restart procedures for long-horizon work.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
ABIDING STATE = state preserved in the world rather than in the conversational subject.

TENSION:
External state improves robustness but can omit intention, uncertainty, tacit rationale, and rejected branches—precisely the genealogy from which later insight may arise.

MISSING:
Which state categories must survive: facts, goals, tests, failures, rationales, uncertainties, rejected branches, source provenance, social lineage?

BOUNDARY:
The source addresses agentic technical work; extension to research notebooks/zettel systems is [OUR INFERENCE].

CITATION TRAIL:
[[SCGAI-003]] → history modifies later prompting → long-running agent workflows → filesystem reconstruction → environmental memory.

TEST:
Run a multi-day task under full chat history, summary-only, and fresh-context+structured-workspace continuation; compare recovery and recurrent error.

PLATFORM:
Claude Code / agent workspaces / long-running research workflows

LINKS:
[[SCGAI-003]]
[[SCGAI-004-A]]

BIBTEX:
@misc{anthropic_prompting_best_practices, author={{Anthropic}}, title={Prompting Best Practices}, howpublished={Claude Platform Documentation}, url={https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices}, note={Accessed 2026-08-17}}
