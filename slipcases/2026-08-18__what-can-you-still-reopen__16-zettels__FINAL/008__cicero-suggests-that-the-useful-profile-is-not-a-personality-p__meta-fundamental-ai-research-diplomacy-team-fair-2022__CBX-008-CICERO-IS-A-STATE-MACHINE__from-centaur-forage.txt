ZETTEL

ID:
CBX-008-CICERO-IS-A-STATE-MACHINE

TITLE:
CICERO suggests that the useful profile is not a personality portrait but a changing strategic state.

SOURCE:
Meta Fundamental AI Research Diplomacy Team — Human-level play in the game of Diplomacy by combining language models with strategic reasoning — 2022.

PASSAGE:
[PARAPHRASE]
CICERO combines language generation with strategic reasoning in Diplomacy, where communication is conditioned by an evolving game state, other players, agreements, plans, and anticipated actions.

RESEARCH OBJECT:
Persuasion may require dynamic state estimation rather than static psychographic description.

LOCAL MOVE:
The source connects communication to strategic planning over changing relational conditions.

SOURCE TERMS:
Diplomacy
strategic reasoning
natural language
plans
agreements
players
coordination

WHAT BECAME STRANGE:
The Centaur Box cites CICERO among precedents for AI persuasion, but the transferable machinery is not primarily a personality taxonomy. It is continual reasoning about a changing multi-agent situation.

QUESTION:
Should a synthetic gatekeeper be represented as a trait profile or as a partially observed stateful policy?

DEEPER QUESTION:
What disappears when enduring descriptors such as Big Five scores replace beliefs, commitments, institutional position, dialogue history, and changing incentives?

MECHANISM:
world state
+ interaction history
+ inferred intentions
→ strategic plan
→ communicative action
→ other-agent response
→ updated world state.

FORMAL SHIFT:
<MULTI-AGENT STATE>
→ <STRATEGIC REPRESENTATION>
→ [PLAN + COMMUNICATE]
→ <NEW MULTI-AGENT STATE>

SOURCE FORMALISM:
The source combines a language model with strategic reasoning/planning. Exact source equations are not reproduced here.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Gatekeeper_t =
{
  role,
  feasible_actions_t,
  beliefs_t,
  commitments_t,
  incentives_t,
  institutional_state_t,
  interaction_history_t
}

Gatekeeper_(t+1) = UPDATE(Gatekeeper_t, message_t, world_t)

TENSION:
A static Operant Profile promises reusable psychological leverage. Strategic interaction may instead make the relevant variables transient and relational.

MISSING:
A comparison between trait-based and state/history-based gatekeeper representations.

BOUNDARY:
Diplomacy is not AI governance, and CICERO’s performance does not demonstrate real-world gatekeeper persuasion. The transferable object is the architecture of stateful strategic interaction.

CITATION TRAIL:
Meta FAIR Diplomacy work.
Strategic argumentation dialogue systems.
Belief-state modeling.
Partially observable multi-agent decision processes.

TEST:
Give identical dialogue histories to a trait-only gatekeeper model and a dynamic belief/state model. Compare prediction of the next governance action after incentives, authority, or coalition structure changes while personality remains constant.

PLATFORM:
[[Synthetic Gatekeepers]]

LINKS:
[[A Profile Is Not a State]]
[[Persuasion Has Memory]]
[[The Gatekeeper Changes During the Dialogue]]

BIBTEX:
@article{meta2022diplomacy,
  title={Human-level play in the game of Diplomacy by combining language models with strategic reasoning},
  author={{Meta Fundamental AI Research Diplomacy Team (FAIR)}},
  journal={Science},
  volume={378},
  number={6624},
  pages={1067--1074},
  year={2022},
  doi={10.1126/science.ade9097}
}
