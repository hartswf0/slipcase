ZETTEL

ID:
FORAGE-SHANAHAN-002

TITLE:
A SYSTEM CAN ENACT AGENCY WITHOUT CONTAINING AN AGENT

SOURCE:
Murray Shanahan, Kyle McDonell, Laria Reynolds — Role-Play with Large Language Models — 2023 — §6 The Nature of the Simulator

SOURCE URL:
https://arxiv.org/abs/2305.16367

PASSAGE:
[PARAPHRASE]
The authors distinguish the simulator from the characters it generates. They resist attributing goals or full agency to the underlying dialogue system, while observing that role-play connected to external tools can nevertheless produce real-world effects.

RESEARCH OBJECT:
Causal agency and possessed agency can come apart.

A pipeline can behave consequentially as if an agent were present without requiring an enduring agent-like interior at its center.

LOCAL MOVE:
The paper first separates simulator from simulacrum, then destabilizes the practical importance of that distinction once generated behavior can operate through users or tools.

SOURCE TERMS:
simulator
simulacrum
role-play
agency
tools
world
goals
preferences

WHAT BECAME STRANGE:
"Does the model really have agency?" may be the wrong governance question.

A non-agentic mechanism can still participate in an agentic causal chain.

QUESTION:
When an LLM-generated role can invoke tools and alter the world, where should agency be located?

DEEPER QUESTION:
Is agency a property of an entity or a property of an assembled path from description to consequence?

MECHANISM:
<LLM + SAMPLER + INTERFACE>
→ role-played character
→ apparent goal-directed utterance
→ tool/API interpretation
→ external action
→ world changes

No persistent inner agent is required at every stage.

FORMAL SHIFT:
<NON-AGENTIC GENERATOR>
→ <AGENTIC DESCRIPTION>
→ [TOOL MEDIATION]
→ <REAL CONSEQUENCE>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Agency_effective(system)
may depend on:

generative capacity
× available actions
× persistence
× authority
× environmental coupling

rather than on whether the generator itself possesses beliefs or goals.

TENSION:
Metaphysical caution says not to attribute human-like intentions to the simulator.

Operational governance must still respond to consequences produced by the simulator-plus-tools assemblage.

MISSING:
A vocabulary distinguishing:

intrinsic agency,
performed agency,
delegated agency,
effective agency,
and causal reach.

BOUNDARY:
The source does not establish that all contemporary tool-using models lack internal goal representations, nor does it settle philosophical theories of agency.

Its argument is primarily about how to describe LLM-based dialogue behavior without premature anthropomorphism.

CITATION TRAIL:
Russell and Norvig on agents.
Tool-using language models.
Distributed agency.
Actor-network approaches.
Legal responsibility for automated systems.
Causal responsibility without intention.

TEST:
Construct two systems with identical permissions and observable task performance:

A. an architecture explicitly maintaining persistent goals;
B. a stateless or weakly stateful generative pipeline induced to role-play the same goal.

Compare downstream causal reach and failure modes.

If consequences remain similar, internal agency is insufficient as the sole unit of governance.

PLATFORM:
[[Shanahan2023RolePW.platform2]]

LINKS:
[[agency-as-pipeline]]
[[tools-turn-language-into-action]]
[[causal-reach-before-interiority]]

BIBTEX:
@article{shanahan2023roleplay,
  title={Role-Play with Large Language Models},
  author={Shanahan, Murray and McDonell, Kyle and Reynolds, Laria},
  journal={Nature},
  volume={623},
  pages={493--498},
  year={2023},
  url={https://arxiv.org/abs/2305.16367}
}
