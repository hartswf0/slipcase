ZETTEL

ID:
WWP-20260817-01

TITLE:
The user no longer writes the prompt that actually runs.

SOURCE:
Michael Bolin — “Unrolling the Codex agent loop” — OpenAI — January 23, 2026 — https://openai.com/index/unrolling-the-codex-agent-loop/

PASSAGE:
[QUOTE] “As an end user, you don’t specify the prompt used to sample the model verbatim.”

RESEARCH OBJECT:
Current agent systems split USER UTTERANCE from EXECUTED PROMPT. The harness assembles a larger object containing instructions, tool definitions, environment constraints, conversation history, files/images, prior tool calls, and other state.

LOCAL MOVE:
Replace PROMPT = WHAT THE USER WROTE with PROMPT = ASSEMBLED EXECUTION CONTEXT.

SOURCE TERMS:
agent loop; prompt; instructions; tools; input; conversation history; context window; harness

WHAT BECAME STRANGE:
Natural-language programming appears immediate, yet the visible sentence is only one ingredient in an increasingly elaborate hidden compilation process.

QUESTION:
What transformations occur between the user’s visible utterance and the actual context sampled by the model?

DEEPER QUESTION:
If users cannot inspect the effective prompt, where should authorship and debugging attach: sentence, harness, tools, history, or composition?

MECHANISM:
USER INPUT → instructions + tools + environment + history + multimodal state → assembled context → model inference → tool/response → enlarged context → inference repeats.

FORMAL SHIFT:
PROMPT: USER_TEXT becomes EFFECTIVE_PROMPT: ASSEMBLE(USER_TEXT, INSTRUCTIONS, TOOLS, HISTORY, ENVIRONMENT, STATE).

SOURCE FORMALISM:
OpenAI describes the Codex agent loop as orchestration among user, model, and tools; the sampled input is assembled from multiple items rather than identical to the end-user message.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
VISIBLE_WORDS=U; EXECUTED_CONTEXT=C(U,H,T,I,E,S); U1=U2 does not imply C1=C2.

TENSION:
Prompt scholarship often analyzes visible strings while agent architectures locate causal power outside those strings.

MISSING:
A secure method for capturing the effective context actually presented during an agent execution.

BOUNDARY:
This architecture describes Codex/Responses-style agent loops and does not prove every generative system assembles context identically.

CITATION TRAIL:
[[SCGAI-007]] → prompting as socio-technical practice → current agent harnesses → visible prompt versus assembled model context.

TEST:
Hold the user utterance constant while varying tools, history, system instructions, files, environment, and memory one at a time; compare divergence with wording changes.

PLATFORM:
OpenAI Codex / Responses API / agent harnesses

LINKS:
[[SCGAI-007]]
[[SCGAI-003]]

BIBTEX:
@misc{bolin2026codexloop, author={Bolin, Michael}, title={Unrolling the Codex Agent Loop}, organization={OpenAI}, year={2026}, url={https://openai.com/index/unrolling-the-codex-agent-loop/}}
