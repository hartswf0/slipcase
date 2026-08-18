ZETTEL

ID:
CALLSHOT-20260817-04

TITLE:
ACT, LOOK, REWRITE THE PLAN — ReAct makes observation part of the prompt program.

SOURCE:
Shunyu Yao et al. — “ReAct: Synergizing Reasoning and Acting in Language Models” — ICLR 2023.
https://arxiv.org/abs/2210.03629

PASSAGE:
[PARAPHRASE]
ReAct interleaves reasoning traces with task-specific actions. Actions interact with external information sources or environments; returned observations allow the model to update plans, handle exceptions, and choose subsequent actions.

RESEARCH OBJECT:
OBSERVATION-AS-PROGRAM-INPUT.

LOCAL MOVE:
The ordinary prompt picture is:

USER
→ MODEL
→ ANSWER.

ReAct replaces it with:

THINK
→ ACT
→ WORLD ANSWERS BACK
→ THINK DIFFERENTLY
→ ACT AGAIN.

The crucial prompt practice is not a clever opening instruction.

It is designing a loop in which reality gets another turn.

SOURCE TERMS:
“reasoning”
“acting”
“interleaved”
“action plans”
“external sources”
“environments”
“additional information”

WHAT BECAME STRANGE:
The environment effectively becomes a co-author of the prompt.

Every tool result is new text conditioning the next operation.

Execution produces specification.

QUESTION:
Which tasks become dramatically more reliable when the model is forced to alternate proposal with observation instead of producing a complete plan before touching the world?

DEEPER QUESTION:
Is an agent fundamentally a language model, or a recurrence relation in which model output and world observation continuously rewrite one another?

MECHANISM:
STATE_t
→ REASON
→ ACTION_t
→ ENVIRONMENT
→ OBSERVATION_t
→ updated STATE
→ REASON
→ ACTION_t+1.

FORMAL SHIFT:
FROM:
PROMPT
→ COMPLETION

TO:
PROMPT₀
→ ACTION₀
→ OBSERVATION₀
→ PROMPT₁
→ ACTION₁
→ ...

SOURCE FORMALISM:
ReAct explicitly interleaves reasoning traces and task-specific actions, using observations gathered through action to update subsequent reasoning and plans.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

PROGRAM UNIT
≠ PROMPT.

PROGRAM UNIT
=
MODEL
↔ ENVIRONMENT LOOP.

The user’s shot is called by specifying:
GOAL,
AVAILABLE ACTIONS,
OBSERVABLE FEEDBACK,
STOP CONDITION.

TENSION:
More acting creates more opportunities to correct mistaken beliefs.

It also creates more opportunities for mistaken actions to alter external state.

MISSING:
A principled rule for when the agent should OBSERVE, ACT, ASK, SIMULATE, or STOP.

BOUNDARY:
ReAct does not imply that exposing private reasoning traces is necessary for effective tool use in every modern system.

CITATION TRAIL:
[[MJ-GC-030]]
→ description enters interaction state
→ [[MJ-GC-030-A]]
→ utterance interpreted into operation
→ ReAct
→ operation returns observation
→ observation rewrites next operation.

TEST:
Take one task currently executed as a single long prompt.

Refactor it into:

OBSERVE
→ CHOOSE ONE ACTION
→ READ CONSEQUENCE
→ REVISE
→ REPEAT.

Compare completion accuracy and error recoverability.

PLATFORM:
Language agents / tool environments

LINKS:
[[MJ-GC-030]]
[[MJ-GC-030-A]]
[[CALLSHOT-20260817-03]]

BIBTEX:
@article{yao2022react,
  title={ReAct: Synergizing Reasoning and Acting in Language Models},
  author={Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan},
  journal={arXiv preprint arXiv:2210.03629},
  year={2022},
  url={https://arxiv.org/abs/2210.03629}
}
