ZETTEL

ID:
FIELD-20260817-03

TITLE:
The archive and the active prompt must diverge: remember everything, load selectively.

SOURCE:
MULTISOURCE — OpenAI Harness Engineering; Anthropic Prompting Best Practices; OpenAI Prompt Caching. SOURCE URLs: https://openai.com/index/harness-engineering/ ; https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices ; https://developers.openai.com/api/docs/guides/prompt-caching

PASSAGE:
[OUR INFERENCE] Durable prompt practice needs two different stores: a rich archive that preserves genealogy and an active context that retrieves only the evidence and constraints relevant to the current execution.

RESEARCH OBJECT:
Recursive prompt work has an information-architecture problem. If every correction remains inline, the prompt sediments. If corrections are discarded, genealogy vanishes. The solution is not a perfect master prompt but a separation between preserved field state and selectively hydrated execution state.

LOCAL MOVE:
Split PROMPT MEMORY into ARCHIVAL MEMORY and ACTIVE CONTEXT.

SOURCE TERMS:
map; source of truth; fresh context; progress files; git logs; exact prefix; stable content; retrieval

WHAT BECAME STRANGE:
Faithful preservation and efficient execution have opposite appetites. The archive wants surplus; the active prompt wants discrimination.

QUESTION:
What retrieval rule selects enough archived knowledge to prevent repeated mistakes without reintroducing prompt sedimentation?

DEEPER QUESTION:
Can forgetting be made a controlled operation rather than an accidental loss of context?

MECHANISM:
ARCHIVE A_t preserves evidence/history → task q arrives → RETRIEVE(A_t,q) → ACTIVE CONTEXT C_t ⊂ A_t → execution → result/evaluation → archive update.

FORMAL SHIFT:
ONE EVER-GROWING PROMPT becomes TWO-LAYER MEMORY: IMMUTABLE/RICH ARCHIVE + TASK-SPECIFIC HYDRATED CONTEXT.

SOURCE FORMALISM:
OpenAI recommends a map into maintained repository knowledge; Anthropic recommends external artifacts for reconstruction across fresh contexts; prompt caching rewards stable prefixes. The two-layer architecture is compiler synthesis.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
A_t = all preserved evidence; C_t = RETRIEVE(A_t, goal_t, risk_t, budget_t), C_t ⊂ A_t. CONTEXT RECALL DEBT = archived evidence omitted from C_t that would have changed the execution materially.

TENSION:
Selective retrieval creates a new failure: the archive can preserve the right correction while the active context fails to recall it. Preservation alone does not produce continuity.

MISSING:
A measurable criterion for context recall debt and a retrieval policy for contradictions, old failures, and model-version-specific rules.

BOUNDARY:
The two-layer architecture and “context recall debt” are [OUR FORMALIZATION], not source terminology.

CITATION TRAIL:
[[WWP-20260817-03]] → map not manual → [[WWP-20260817-04]] → externalized state → [[WWP-20260817-08]] → stable/variable topology → archive/active-context split.

TEST:
Seed an archive with known critical corrections, then vary retrieval policies. Measure repeated-error rate and identify cases where omitted archived evidence would have prevented failure.

PLATFORM:
Long-running research agents / prompt repositories / recursive zettel systems

LINKS:
[[WWP-20260817-03]]
[[WWP-20260817-04]]
[[WWP-20260817-08]]

BIBTEX:
@misc{openai2026harness, author={{OpenAI}}, title={Harness Engineering: Leveraging Codex in an Agent-First World}, year={2026}, url={https://openai.com/index/harness-engineering/}}
@misc{anthropic_prompting_best_practices, author={{Anthropic}}, title={Prompting Best Practices}, url={https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices}}
@misc{openai_prompt_caching, author={{OpenAI}}, title={Prompt Caching}, url={https://developers.openai.com/api/docs/guides/prompt-caching}}
