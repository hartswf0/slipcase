ZETTEL

ID:
EMPOWERMENT-001

TITLE:
Nominal interface choice is weaker than an action channel whose alternatives produce reliably distinguishable future states.

SOURCE:
Tobias Jung, Daniel Polani, and Peter Stone — “Empowerment for Continuous Agent–Environment Systems” — Adaptive Behavior 19(1) — 2011 — pp. 16–39.

SOURCE URL:
https://arxiv.org/abs/1201.6583

PASSAGE:
[PARAPHRASE]
Empowerment measures how much influence an agent has on its environment that can also be sensed by the agent, generalizing controllability and observability through an information-theoretic action-to-future-state channel.

RESEARCH OBJECT:
DISTINGUISHABLE CONSEQUENCE CAPACITY.

LOCAL MOVE:
Give “control” a technical lower bound without mistaking it for authorship: an interface is weak when distinct user interventions collapse into indistinguishable consequences.

SOURCE TERMS:
empowerment
channel capacity
controllability
observability
stochastic transitions
sensorimotor loop

WHAT BECAME STRANGE:
A long natural-language instruction can carry less effective control than one well-coupled spatial operation.

QUESTION:
Can creative-interface control be estimated from the mutual information between interventions and artistically relevant future states?

DEEPER QUESTION:
What representation of the future state preserves meaningful artistic distinctions without rewarding trivial pixel variation?

MECHANISM:
User intervention A → system dynamics → perceived future artifact Φ(Y′). Effective control increases when different A reliably lead to distinguishable Φ(Y′).

FORMAL SHIFT:
<NUMBER OF CONTROLS> → <CAPACITY OF CONTROL-TO-CONSEQUENCE CHANNEL>

SOURCE FORMALISM:
Empowerment is defined as an information-theoretic channel capacity between actions and future sensed states under the system dynamics.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
CreativeControl(s)=max_{p(A)} I(A;Φ(Y′)|s). Φ must be task- and observer-relative.

TENSION:
High empowerment can describe skillful game play that is not authorship; causal capacity is not a legal or aesthetic conclusion.

MISSING:
A defensible artistically relevant feature map Φ and empirical validation against human judgments of steering.

BOUNDARY:
Use empowerment to measure effective influence, not to infer authorship automatically.

CITATION TRAIL:
[[RETENTION-005-Y-B]] → empowerment → observable control → distinguishable consequence capacity.

TEST:
Estimate intervention→feature-state mutual information for text-only, mask, pose, and parameter controls on the same edit task. Compare the metric to expert judgments of controllability and invariant preservation.

PLATFORM:
[[class-is-not-a-path]]

LINKS:
[[RETENTION-005-Y-B]]
[[RETENTION-005-Y-C]]
[[effective-control]]

BIBTEX:
@article{jung2011empowerment,
  author  = {Jung, Tobias and Polani, Daniel and Stone, Peter},
  title   = {Empowerment for Continuous Agent--Environment Systems},
  journal = {Adaptive Behavior},
  volume  = {19},
  number  = {1},
  pages   = {16--39},
  year    = {2011},
  doi     = {10.1177/1059712310392389}
}
