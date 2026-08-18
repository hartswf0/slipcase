ZETTEL

ID:
Z-RF-20260817-003

TITLE:
Interfaces can suppress exploration before ranking ever begins.

SOURCE:
Maddalena Torricelli, Mauro Martino, Andrea Baronchelli, Luca Maria Aiello — “The role of interface design on prompt-mediated creativity in Generative AI” — arXiv:2312.00233, 2023; accepted WebSci 2024.

PASSAGE:
[PARAPHRASE]
Across more than 145,000 prompts from Stable Diffusion and Pick-a-Pic, the authors find that interface features that divert attention away from prompt editing and offer shortcuts for generating variants are associated with substantially less exploration of novel concepts and less detail in submitted prompts.

RESEARCH OBJECT:
A platform can change the distribution of generated ideas by changing the cheapest next action.

LOCAL MOVE:
The evidence follows [[Z-AIACS-018]]’s search for platform mechanisms but finds a better-supported mechanism than the parent’s unverified Midjourney-ranking claim.

SOURCE TERMS:
“interface design”
“prompt-mediated creativity”
“exploration”
“exploitation”
“image variants”
“novel concepts”

WHAT BECAME STRANGE:
Aesthetic convergence need not begin with an algorithm preferentially ranking certain pictures. It can begin earlier, when an interface makes variation cheaper than re-description.

QUESTION:
How much apparent model-level aesthetic repetition is actually path dependence introduced by the interface’s next-action affordances?

DEEPER QUESTION:
Does a generative interface quietly define what kind of creativity is economically convenient?

MECHANISM:
current generation
→ interface presents cheap variant action
→ user modifies image rather than concept
→ reduced prompt revision
→ reduced topical movement
→ locally concentrated trajectory

FORMAL SHIFT:
<current creative state>
→ <available interface operations>
→ [SELECT LOW-COST NEXT ACTION]
→ <constrained exploration trajectory>

SOURCE FORMALISM:
The study compares longitudinal prompt behavior across two platforms and measures exploration of new concepts and prompt detail in relation to differing interface functionality.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

CREATIVE_TRANSITION =
f(current_output,
  available_actions,
  action_costs,
  user_intention)

Interface design changes the transition probabilities even if the generator is held conceptually separate.

TENSION:
[[Z-AIACS-018]] proposed:
ranking → visibility → imitation → aesthetic concentration.

Torricelli et al. support a different path:
interface action → reduced prompt exploration → trajectory concentration.

The first mechanism remains possible but should not borrow evidence from the second.

MISSING:
A study holding the generative model constant while experimentally changing only interface operations.

BOUNDARY:
The observational comparison associates interface differences with prompt behavior. It does not by itself prove that interface design alone causes the entire between-platform difference.

CITATION TRAIL:
[[Z-AIACS-018]]
→ Torricelli et al.
→ interface-mediated exploration
→ separate pre-generation path dependence from post-generation ranking effects

TEST:
Build two interfaces over the same model: one privileging “make variants,” another privileging “rewrite description.” Randomly assign users and compare semantic distance between successive prompts, visual diversity, concept count, and final-output convergence.

PLATFORM:
[[Platform Aesthetics]]

LINKS:
[[Z-AIACS-018]]
[[Interface Governance]]
[[Creative Trajectories]]
[[Affordance-Induced Convergence]]

BIBTEX:
@misc{TorricelliEtAl2023Interface,
  author = {Maddalena Torricelli and Mauro Martino and Andrea Baronchelli and Luca Maria Aiello},
  title = {The role of interface design on prompt-mediated creativity in Generative AI},
  year = {2023},
  eprint = {2312.00233},
  archivePrefix = {arXiv},
  primaryClass = {cs.CY},
  doi = {10.48550/arXiv.2312.00233}
}
