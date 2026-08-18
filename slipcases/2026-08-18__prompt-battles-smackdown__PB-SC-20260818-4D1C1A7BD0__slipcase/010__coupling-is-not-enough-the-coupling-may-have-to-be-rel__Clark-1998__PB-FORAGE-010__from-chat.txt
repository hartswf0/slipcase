ZETTEL

ID:
PB-FORAGE-010

TITLE:
Coupling is not enough; the coupling may have to be reliable before capability changes owners.

SOURCE:
Andy Clark and David J. Chalmers — The Extended Mind — 1998 — Analysis 58(1):7–19.

PASSAGE:
[PARAPHRASE]
Clark and Chalmers argue that some cognitive processes can extend across agent and environment when external components play an active causal role in a coupled system. They also resist the objection that external resources are too contingent by emphasizing reliable coupling: resources can count as part of the operative cognitive system when they are generally available when required.

RESEARCH OBJECT:
[[PB-FORAGE-003]] moved the unit of capability from MODEL toward MODEL + OPERATOR.

The Extended Mind makes that move harder.

Not every temporary coupling licenses a new system boundary.

A randomly encountered expert who rescues a model once is different from an operator-model configuration that is reliably available and repeatedly integrated into competent action.

LOCAL MOVE:
Split:

ASSISTED PERFORMANCE

from:

COUPLED CAPABILITY.

SOURCE TERMS:
active externalism
coupled system
active causal role
behavioral competence
reliable coupling
external resources
cognitive process

WHAT BECAME STRANGE:
If the Prompt Pilot counts as part of the capability whenever the Pilot causally improves output, then almost any consultant, search engine, evaluator, or lucky hint becomes part of “the system.”

But if only reliably coupled resources count, capability attribution acquires a temporal condition.

The question becomes not merely:

what components produced this result?

but:

which components are stably available to reproduce this competence?

QUESTION:
How reliable must a human-model coupling become before it makes sense to attribute a capability to the coupled system rather than call the result assisted performance?

DEEPER QUESTION:
Is portability a hidden requirement of benchmark capability?

MECHANISM:
Changing or removing an active external component changes behavioral competence.

Yet repeated availability determines whether that component is a stable part of the operative system or merely an episodic intervention.

Capability attribution therefore depends on both causal contribution and coupling structure.

FORMAL SHIFT:
<MODEL PERFORMANCE>
→ <CAUSALLY COUPLED COMPONENTS>
→ [TEST RELIABILITY OF COUPLING]
→ <ASSISTED EVENT OR STABLE SYSTEM CAPABILITY>

SOURCE FORMALISM:
Clark and Chalmers propose a coupled-system analysis in which internal and external components can jointly govern behavior.

They argue that reliable coupling, rather than location inside the skull, can matter to whether an external resource belongs to the operative cognitive package.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

For model M and operator O:

CausalContribution(O,M,T) > 0

is insufficient for:

Capability(M+O,T).

Add a coupling condition:

R(O,M,T) = probability that the relevant operator-resource configuration is available and effectively recruited when task T occurs.

Then distinguish:

episodic augmentation:
R is low or contingent

stable coupled capability:
R is high across relevant contexts.

TENSION:
Benchmarking wants capability to belong to a portable object called “the model.”

Interactive practice often achieves competence through contingent configurations of models, histories, tools, people, retrieval systems, and interfaces.

A strict portability criterion may erase how useful AI systems actually work.

Abandoning it may make “model capability” impossible to localize.

MISSING:
A capability report that separately records:

component contribution
coupling reliability
operator dependence
history dependence
tool dependence
transfer across operators.

BOUNDARY:
Clark and Chalmers argue about cognition, not machine-learning benchmark attribution.

Their account does not prove that a human-model pair is literally one cognitive subject.

It supplies a criterion that pressures simplistic ownership of observed competence.

CITATION TRAIL:
[[PB-FORAGE-003]]
→ Clark and Chalmers on coupled systems
→ reliable coupling
→ coupling-constitution objections
→ determine when orchestration should count as the evaluated system.

TEST:
Construct three conditions for the same task:

A. model alone
B. model + randomly assigned expert
C. model + operator who has developed a stable history of working with that model.

Repeat over many tasks and interruptions.

Then swap operators and models.

Measure which capabilities survive decoupling and which collapse.

The key evidence is not maximum score but the dependency structure revealed by removal and substitution.

PLATFORM:
[[Capability Attribution]]

LINKS:
[[PB-FORAGE-003]]
[[Coupled Capability]]
[[Assisted Performance]]
[[Reliable Coupling]]

BIBTEX:
@article{clark1998extended,
  title={The Extended Mind},
  author={Clark, Andy and Chalmers, David J.},
  journal={Analysis},
  volume={58},
  number={1},
  pages={7--19},
  year={1998},
  doi={10.1093/analys/58.1.7}
}
