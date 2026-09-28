ZETTEL

ID:
ENCOUNTER-OP-034

TITLE:
An encounter may leave a trace in how the human models the entity on the next turn.

SOURCE:
Johannes Schneider — “Mental model shifts in human-LLM interactions” — 2025 — Journal of Intelligent Information Systems 63, 1737–1752. ([doi.org](https://doi.org/10.1007/s10844-025-00960-6))

PASSAGE:
[PARAPHRASE] Across more than 200,000 real-world conversations, users displayed more human-like communication patterns from the second turn onward in measures including politeness, language complexity, and prompt length; the author presents these as initial indications rather than definitive proof of a mental-model shift. ([doi.org](https://doi.org/10.1007/s10844-025-00960-6))

RESEARCH OBJECT:
Post-contact behavioral change supplies a scalable candidate trace for encounter-induced reclassification of the artificial partner.

LOCAL MOVE:
Schneider turns an otherwise inaccessible user mental model into within-conversation behavioral proxies.

SOURCE TERMS:
mental model
machine
human
politeness
language complexity
prompt length
real-world conversations
communication pattern

WHAT BECAME STRANGE:
The consequential transition may occur extremely early: the first response can change how the user addresses the system on the second turn.

QUESTION:
Is a measurable shift in the user’s model of the AI an encounter signature or merely interface adaptation?

DEEPER QUESTION:
Can the same method detect movement in the opposite direction, from apparent person back toward instrument?

MECHANISM:
initial system expectation
→ first AI response
→ updated prediction about interlocutor
→ altered linguistic behavior in subsequent prompt.

FORMAL SHIFT:
<PRE-RESPONSE USER MODEL>
→ <AI RESPONSE>
→ [MODEL UPDATE]
→ <CHANGED USER BEHAVIOR>

SOURCE FORMALISM:
The study uses computational-linguistic indicators including politeness, language complexity, and prompt length and compares their behavior over successive conversation turns. ([doi.org](https://doi.org/10.1007/s10844-025-00960-6))

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

OTHER_MODEL_SHIFT =
distance(
  user_behavior_after_contact,
  user_behavior_before_contact
)

But interpret only alongside explicit probes of:
perceived agency,
tool/person classification,
expected capabilities,
expected fallibility.

TENSION:
The same reduction in prompt explicitness could reflect learning how to use the interface efficiently rather than treating the system as more human.

MISSING:
Convergent evidence connecting linguistic proxies to independently elicited user models.

BOUNDARY:
Schneider explicitly frames the computational evidence as an initial step. Linguistic behavior does not directly reveal an internal mental model.

CITATION TRAIL:
[[ENCOUNTER-AI-018]]
[[ENCOUNTER-AI-019]]
[[ENCOUNTER-AI-023]]
→ Schneider 2025
→ experimental mental-model elicitation
→ turn-by-turn entity classification
→ model-shift encounter trace.

TEST:
After selected turns, ask participants to make predictions about what the AI can:
remember,
understand,
refuse,
infer,
initiate,
and revise.
Compare changes in those predictions with the behavioral linguistic indicators.

PLATFORM:
[[Operational Encounter Model]]

LINKS:
[[ENCOUNTER-AI-018]]
[[ENCOUNTER-AI-019]]
[[ENCOUNTER-AI-023]]
[[Other-Model Shift]]

BIBTEX:
@article{Schneider2025MentalModels,
  author = {Johannes Schneider},
  title = {Mental model shifts in human-LLM interactions},
  journal = {Journal of Intelligent Information Systems},
  year = {2025},
  volume = {63},
  pages = {1737--1752},
  doi = {10.1007/s10844-025-00960-6}
}