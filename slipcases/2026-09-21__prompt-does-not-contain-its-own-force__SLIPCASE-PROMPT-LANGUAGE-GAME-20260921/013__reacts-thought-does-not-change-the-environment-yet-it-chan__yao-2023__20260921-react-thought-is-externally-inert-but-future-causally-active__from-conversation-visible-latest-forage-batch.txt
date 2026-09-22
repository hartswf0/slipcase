ZETTEL

ID:
20260921-react-thought-is-externally-inert-but-future-causally-active

TITLE:
ReAct’s “Thought” Does Not Change the Environment, Yet It Changes the Context That Selects Later Actions

SOURCE:
Shunyu Yao et al. — “ReAct: Synergizing Reasoning and Acting in Language Models” — ICLR 2023 — §2. ([arxiv.org](https://arxiv.org/pdf/2210.03629?utm_source=chatgpt.com))

PASSAGE:
[PARAPHRASE] ReAct defines language-space thoughts as actions that do not affect the external environment and therefore produce no observation feedback. Instead, the thought is appended to the context so it can support later reasoning or acting. The paper lists plan formation, observation extraction, progress tracking, exception handling, and plan adjustment among its uses. ([arxiv.org](https://arxiv.org/pdf/2210.03629?utm_source=chatgpt.com))

RESEARCH OBJECT:
An output that is inert with respect to the external world but causally active with respect to future model behavior.

LOCAL MOVE:
ReAct splits causal effect into at least two domains: external environment state and internal interaction context.

SOURCE TERMS:
language space
thought
context
external environment
observation feedback
action
plan
exception

WHAT BECAME STRANGE:
“Inert” is relative to a state boundary. A thought does nothing to the external world while changing the textual state from which the next world-changing action is generated.

QUESTION:
How many distinct state spaces must be tracked before the causal status of an agent output can be described accurately?

DEEPER QUESTION:
Could a supposedly non-executing prompt still be operational if it modifies memory, planning state, retrieved context, rankings, or future action probabilities?

MECHANISM:
model generates thought
→ no environment call
→ no external observation
→ thought appended to context
→ next generation conditioned on changed context
→ later action selection changes
→ world may change later.

FORMAL SHIFT:
<INERT VS ACTIVE>
→ <ACTIVE-WITH-RESPECT-TO-WHICH-STATE?>
→ [UPDATE CONTEXT OR ENVIRONMENT]
→ <MULTI-LAYER CAUSALITY>

SOURCE FORMALISM:
ReAct defines an augmented action space Â = A ∪ L, with language-space elements updating context but not the external environment. ([arxiv.org](https://arxiv.org/pdf/2210.03629?utm_source=chatgpt.com))

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
effects(output) =
{
  context_state,
  memory_state,
  tool_state,
  environment_state,
  human_state
}

TENSION:
Some deployed systems hide reasoning traces or do not preserve them in subsequent context, so the same textual category “thought” can have different causal architectures.

MISSING:
A causal-state inventory for actual agent runtimes rather than a binary action/thought label.

BOUNDARY:
ReAct specifies its own research architecture; its definition of thought does not automatically describe proprietary agent systems.

CITATION TRAIL:
[[20260921-react-distinguishes-language-that-cannot-change-world-from-actions-that-can]]
→ ReAct’s context update
→ external non-action can still be an operation on future action state.

TEST:
Run identical agent trajectories while selectively preventing thought text from entering subsequent context. Measure which downstream actions change despite identical external observations.

PLATFORM:
[[agentic-prompting]]

LINKS:
[[20260921-react-distinguishes-language-that-cannot-change-world-from-actions-that-can]]
[[ReAct]]
[[context-state]]
[[causal-layer]]

BIBTEX:
@inproceedings{yao2023react,
  author = {Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan},
  title = {ReAct: Synergizing Reasoning and Acting in Language Models},
  booktitle = {International Conference on Learning Representations},
  year = {2023}
}
