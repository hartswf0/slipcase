ZETTEL

ID:
CHANNEL-001

TITLE:
Creative control is a perceptible action-to-future channel, not a count of available controls.

SOURCE:
Tobias Jung, Daniel Polani, and Peter Stone — “Empowerment for Continuous Agent-Environment Systems” — Adaptive Behavior 19(1) — 2011.

SOURCE URL:
https://doi.org/10.1177/1059712310392389

PASSAGE:
[PARAPHRASE]
Empowerment measures an agent’s potential influence in terms of the information-theoretic channel from actions to future observable states. Different actions that cannot produce distinguishable future observations contribute little effective control regardless of nominal option count.

RESEARCH OBJECT:
CREATIVE CHANNEL CAPACITY.

LOCAL MOVE:
Give “a button is not evidence of agency” a technical lower bound: actions matter for practical steering when they generate reliably distinguishable, observable consequences.

SOURCE TERMS:
empowerment
channel capacity
controllability
observability
action
future state

WHAT BECAME STRANGE:
One text box can provide more effective artistic leverage than dozens of sliders, while many visible controls can collapse onto nearly identical futures.

QUESTION:
Can creative interfaces be evaluated by the number of artistically meaningful future differences a user can reliably produce and perceive?

DEEPER QUESTION:
How should the state representation be chosen so information-theoretic control measures meaningful artistic distinctions rather than trivial pixel changes?

MECHANISM:
action distribution A → system dynamics → future observable artifact state Y; channel capacity measures distinguishable influence available through the action channel.

FORMAL SHIFT:
<CONTROL COUNT> → <EFFECTIVE DISTINGUISHABLE FUTURES>

SOURCE FORMALISM:
Jung, Polani, and Stone formalize empowerment for agent-environment systems; “creative channel capacity” is our application.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
E_creative(s)=max_{p(a)} I(Φ(Y_future);A | s), where Φ is a task/observer-relative representation of artistically meaningful differences.

TENSION:
High empowerment does not imply authorship: a game player can have strong control over trajectories inside an upstream-authored expressive system.

MISSING:
A defensible Φ for artistic meaning and a method to estimate capacity in high-dimensional stochastic generators.

BOUNDARY:
Empowerment is evidence of effective influence, not of legal authorship, artistic quality, or originality.

CITATION TRAIL:
[[AGENCY-001]] → visible controls versus leverage → [[EMPOWERMENT-001]] → action/future channel → creative application.

TEST:
Compare interfaces with similar control counts. Estimate intervention-to-feature mutual information and compare it with expert judgments of controllability and successful target editing.

PLATFORM:
[[after-surprise]]

LINKS:
[[AGENCY-001]]
[[EMPOWERMENT-001]]
[[creative-channel-capacity]]
[[effective-options]]

BIBTEX:
@article{JungPolaniStone2011,
  author={Jung, Tobias and Polani, Daniel and Stone, Peter},
  title={Empowerment for Continuous Agent-Environment Systems},
  journal={Adaptive Behavior},
  volume={19},
  number={1},
  pages={16--39},
  year={2011},
  doi={10.1177/1059712310392389}
}
