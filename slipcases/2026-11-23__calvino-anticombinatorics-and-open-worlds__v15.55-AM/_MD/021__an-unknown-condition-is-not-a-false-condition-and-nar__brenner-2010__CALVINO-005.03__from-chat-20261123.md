ZETTEL

ID: CALVINO-005.03

TITLE:
An unknown condition is not a false condition, and narrative action depends on who knows the difference.

SOURCE:
Michael Brenner — "Creating Dynamic Story Plots with Continual Multiagent Planning" — Proceedings of AAAI-10 (2010), pp. 1517–1522, especially pp. 1518–1519.

PASSAGE:
[PARAPHRASE]
Brenner's Multiagent Planning Language (MAPL) uses multi-valued state variables that can include an unknown value. Characters possess beliefs about the world and may acquire information through sensing, copresence, and communication.

An action depends not only on its physical preconditions but also on what its controlling agent knows. Plans can be revised when observations or communications change an agent's available information.

RESEARCH OBJECT:
Epistemic availability as a distinct condition of narrative action.

LOCAL MOVE:
Brenner separates the physical conditions under which an action is possible from the knowledge conditions under which a character can deliberately execute it.

This makes different characters' beliefs part of the machinery of plot construction.

SOURCE TERMS:
"Multiagent Planning Language";
"multi-valued state variables";
"unknown";
"knowledge preconditions";
"copresence";
"communication";
"temporary subgoals";
"Continual Multiagent Planning."

WHAT BECAME STRANGE:
Calvino asks whether particular actions are compatible.

Brenner's architecture makes that question insufficient.

An action may be physically possible but unavailable to a character because the character does not know how to perform it or does not know that its preconditions hold.

The same physical world can therefore contain different actionable possibility spaces for different characters.

QUESTION:
Should narrative anticombinatorics eliminate impossible events, or eliminate events that particular characters cannot knowingly undertake from their situated perspectives?

DEEPER QUESTION:
Does narrative possibility belong to the world, the character's representation of the world, or the relation between them?

MECHANISM:
A character maintains beliefs about relevant variables.

Perception and communication can update those beliefs.

Changed beliefs can activate goals, invalidate plans, or permit actions previously unavailable to the character.

Continual planning alternates between planning, execution, observation, and revision.

FORMAL SHIFT:
Shared physical environment
→ agent-specific beliefs and goals
→ [perception, communication, planning]
→ agent-specific action availability
→ revised beliefs and plans.

SOURCE FORMALISM:
MAPL extends PDDL.

It uses multi-valued state variables.

It introduces knowledge and commitment preconditions for actions.

It provides sensing, copresence, and communication models.

Brenner presents CMP Agent(S,G), an algorithm that performs monitoring, replanning, action execution, state estimation, and processing of messages or requests.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

World state:
W(t)

Belief state of character i:
B_i(t)

Physical executability:
Executable(a, W(t))

Perceived executability:
KnownExecutable(a, B_i(t))

An action can satisfy:

Executable(a, W(t)) = true

while:

KnownExecutable(a, B_i(t)) = false

An observation can change the second condition without changing the first.

TENSION:
Brenner's MAPL places knowledge conditions on autonomous action.

R. Michael Young's later HEADSPACE research explicitly accommodates actions undertaken because characters mistakenly believe their physical preconditions hold.

These approaches do not treat belief-relative executability identically.

MISSING:
A mechanism for modeling actions undertaken with unjustified confidence, mistaken beliefs, incomplete knowledge, or deliberately misleading information.

A criterion for deciding when an agent should act despite uncertainty.

BOUNDARY:
MAPL and CMP provide a concrete planning architecture, not a complete theory of literary interpretation or aesthetics.

Brenner explicitly distinguishes the capacity to generate dynamic plots from the capacity to generate interesting ones.

CITATION TRAIL:
[[CALVINO-005]]
→ Brenner (2010), MAPL state representation and CMP Algorithm 1
→ Brenner and Nebel (2009), continual planning
→ Thorne and Young (2017), false beliefs and failed actions
→ Young (2017), HEADSPACEX.

TEST:
Create a shared narrative world containing one concealed fact and two characters.

Run three conditions:

A. The fact is known to both characters.

B. The fact is unknown to one character.

C. One character holds a false belief about the fact.

Keep physical conditions identical.

Compare generated plans, executed actions, failed actions, and belief revisions.

Determine whether a single global compatibility matrix can reproduce the differences.

PLATFORM:
[[Situated Narrative Possibility]]
[[Multiagent Storyworld Planning]]

LINKS:
[[CALVINO-005]]
[[CALVINO-005.01]]
[[CALVINO-005.02]]
[[CALVINO-008]]
[[CALVINO-016]]

BIBTEX:
@inproceedings{brenner2010creating,
  author    = {Brenner, Michael},
  title     = {Creating Dynamic Story Plots with Continual Multiagent Planning},
  booktitle = {Proceedings of the Twenty-Fourth AAAI Conference on Artificial Intelligence},
  pages     = {1517--1522},
  year      = {2010},
  publisher = {AAAI Press},
  url       = {https://cdn.aaai.org/ojs/7567/7567-13-11097-1-2-20201228.pdf}
}
