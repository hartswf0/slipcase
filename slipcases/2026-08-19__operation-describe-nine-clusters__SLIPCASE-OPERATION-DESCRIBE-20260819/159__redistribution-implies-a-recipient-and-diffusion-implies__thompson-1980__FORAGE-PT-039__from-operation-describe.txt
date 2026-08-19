ZETTEL

ID: FORAGE-PT-039

TITLE: Redistribution implies a recipient and diffusion implies none, and the problem of many hands showed decades ago which one actually happens

SOURCE: Dennis Thompson, "Moral Responsibility of Public Officials: The Problem of Many Hands", American Political Science Review (1980) [UNVERIFIED pagination]; Andreas Matthias, "The responsibility gap: Ascribing responsibility for the actions of learning automata", Ethics and Information Technology (2004) [UNVERIFIED]; read against PROGRAMS/agential.json sixth operation

PASSAGE: [PARAPHRASE] Thompson's problem of many hands: when an outcome results from the contributions of many officials, each contribution is individually too small or too mediated to ground responsibility, and the result is that no one is held — not that responsibility passes to someone else. [QUOTE] agential.json: "[redistributes] <responsibility>"

RESEARCH OBJECT: A word choice with consequences. Redistribution is conservative: it moves a quantity from one holder to another. Diffusion is dissipative: the quantity ceases to be held. The parent asked whether the sixth operation ever fires; this child asks whether the operation, when it fires, is the one named — and the prior literature says it is not.

LOCAL MOVE: This child dates the phenomenon before AI. If many hands already dissipated responsibility in bureaucracies in 1980, then generative systems intensify a known mechanism rather than introducing one, and the apparatus vocabulary is a late arrival to a solved diagnosis.

SOURCE TERMS: many hands / moral responsibility / ascription / responsibility gap / learning automata / redistribute

WHAT BECAME STRANGE: The corpus's critique presents itself as revealing a hidden operation. The operation was named forty-six years ago in political theory, with a fuller account: not only that responsibility disperses, but that dispersal is a *predictable consequence of division of labour* and therefore a design property of organisations, not a novel property of machines.

QUESTION: In cases where a system mediates a decision, does responsibility land on an identifiable party, disperse across many, or vanish — and which of the three is modal?

DEEPER QUESTION: If dissipation is a property of divided labour generally, then inserting a system is just one more hand, and the interesting variable is not the machine but the *number of hands* and the *documentation of each handoff*. That makes the remedy procedural and boring, which may be why the apparatus framing prefers the machine as the culprit.

MECHANISM: <OUTCOME> -> [MANY CONTRIBUTIONS, EACH SMALL OR MEDIATED] -> each contributor's causal share below the ascription threshold -> [NO CONTRIBUTOR MEETS THE STANDARD] -> <NOBODY HELD; RESPONSIBILITY DISSIPATES RATHER THAN TRANSFERS>

FORMAL SHIFT: <RESPONSIBILITY AS A CONSERVED QUANTITY> -> <RESPONSIBILITY AS A DISSIPATIVE ONE> -> [COUNT HANDS, NOT MACHINES] -> <GAP AS A FUNCTION OF CHAIN LENGTH>

SOURCE FORMALISM: NONE — both sources argue in prose.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] For a decision chain with n contributors, let share_i be contributor i's causal contribution and theta the ascription threshold. Dissipation occurs when max_i share_i < theta. Adding a system increments n and lowers every share. Prediction: the gap widens with chain length independently of whether any link is automated.

TENSION: READING A (Thompson generalised): the machine is one more hand and the mechanism is division of labour, so AI ethics is a special case of organisational responsibility. READING B (Matthias): learning systems are different in kind because their behaviour is not predictable by the deployer, so the share is not merely small but *unforeseeable*, which defeats ascription in a new way.

Discriminating evidence: compare cases where the automated link was predictable against cases where it was not. If gaps of the same size appear in both, Reading A holds and novelty claims are inflated.

MISSING: Verified pagination for both sources. Any measurement of chain length against attributability. Any case where an automated link demonstrably lowered attributability below what an equivalent human link would have.

BOUNDARY: Thompson writes about public officials and Matthias about learning automata; neither addresses generative systems specifically, and the transfer is ours.

CITATION TRAIL: [[FORAGE-PT-012]] -> Thompson 1980 -> many hands and dissipation -> Matthias 2004 -> the novelty claim -> next: the moral crumple zone, where the dissipation is shown to terminate on a designated human rather than vanishing.

TEST: Assemble ten documented failures with decision chains of varying length, half with an automated link. Code where responsibility was formally assigned. If assignment failure tracks chain length rather than automation, redistribution is the wrong word and dissipation is the right one.

PLATFORM: [[dissipation-not-redistribution]]

LINKS: [[FORAGE-PT-012]] [[FORAGE-PT-025]] [[FORAGE-PT-042]] [[FORAGE-PT-052]]

BIBTEX: @article{thompson1980many, title={Moral Responsibility of Public Officials: The Problem of Many Hands}, author={Thompson, Dennis F.}, journal={American Political Science Review}, volume={74}, number={4}, year={1980}, note={[UNVERIFIED] pagination not verified in this forage}}
