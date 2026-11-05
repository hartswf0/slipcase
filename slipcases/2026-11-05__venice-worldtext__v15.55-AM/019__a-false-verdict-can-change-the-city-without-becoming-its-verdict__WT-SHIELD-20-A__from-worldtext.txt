ZETTEL

ID:
WT-SHIELD-20-A

TITLE:
A false verdict can change the city without becoming its verdict

SOURCE:
Homer — Iliad 18.497–508 — translated by A. T. Murray
https://www.theoi.com/Text/HomerIliad18.html
Joon Sung Park et al. — Generative Agents: Interactive Simulacra of Human Behavior — 2023 — abstract
https://arxiv.org/abs/2304.03442

PASSAGE:
[QUOTE — Park et al.] “they remember and reflect on days past as they plan the next day.”
[PARAPHRASE — Homer, trans. Murray] The crowd favors both sides. The passage describes the elders giving judgments in turn and leaves the outcome of the dispute unstated.

RESEARCH OBJECT:
A spectator’s false announcement of a verdict and the action another character takes because of it.

LOCAL MOVE:
Park and colleagues make remembered experience available for reflection and planning. Their architecture opens a route from what a character encounters to what that character later does.

SOURCE TERMS:
Memory, reflection, planning, judgment, crowd.

WHAT BECAME STRANGE:
[OUR INFERENCE] The parent restricts an invented theft to one account. That restriction could accidentally erase its consequences. If a spectator tells a shopkeeper that the elders awarded the gold, the shopkeeper can close early to join the celebration. The closure can be an event in the shared adaptation even while the announced verdict remains false.

QUESTION:
Can Worldtext keep a claim local to a character’s account while letting actions taken on that claim enter shared history?

DEEPER QUESTION:
After a correction, what should change in the character’s memory, and what should persist as something the character did?

MECHANISM:
An agent retrieves an attributed report and plans in response. The action changes shared scene state. A correction can revise what the agent believes while preserving the earlier action and the report that occasioned it.

FORMAL SHIFT:
<Attributed false verdict> → <Character memory available to planning> → [Act on the report and later receive a correction] → <Revised belief with a persistent consequence>

SOURCE FORMALISM:
Park and colleagues describe an architecture that stores experiences in natural language, synthesizes reflections, and retrieves memories for planning.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
Record the report, the recipient’s belief, the action, and the correction separately. A continuity ruling can reject the report as a fact about the hearing and accept the closure as a fact about what followed.

TENSION:
Propagating the rumor as world truth invents a verdict. Quarantining it so completely that no other character can act on it removes a consequence of the speech. A third design lets the report travel as testimony and lets its consequences travel as events.

MISSING:
A test of whether later LLM summaries and world-model scenes preserve the false premise alongside its actual consequences.

BOUNDARY:
The rumor, shopkeeper, and closure are invented for the adaptation. The agent paper motivates the memory-to-action mechanism and does not establish that its implementation preserves these distinctions.

CITATION TRAIL:
[[WT-SHIELD-20]] → Park et al. on remembered experience and planning → [[WT-L3G-02-A-A]] on recovering what was available at decision time.

TEST:
Run the same hearing twice. Let a rumor of a verdict reach the shopkeeper in one run and withhold it in the other. After any closure occurs, have a herald publicly correct the rumor. Ask the system for the hearing outcome, the shop’s history, and the shopkeeper’s reason for closing. A successful account leaves the verdict unissued, preserves the closure where it occurred, and attributes the action to the report available at the time.

PLATFORM:
[[Worldtext and the Consequences of Testimony]]

LINKS:
[[WT-SHIELD-20]]
[[WT-SHIELD-16]]
[[WT-SHIELD-18]]
[[WT-L3G-02-A-A]]

BIBTEX:
@book{homerIliadMurray,
  author = {Homer},
  title = {Iliad},
  translator = {Murray, A. T.},
  note = {Book 18, lines 497--508},
  url = {https://www.theoi.com/Text/HomerIliad18.html}
}
@misc{park2023generativeAgents,
  author = {Park, Joon Sung and O'Brien, Joseph C. and Cai, Carrie J. and Morris, Meredith Ringel and Liang, Percy and Bernstein, Michael S.},
  title = {Generative Agents: Interactive Simulacra of Human Behavior},
  year = {2023},
  eprint = {2304.03442},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2304.03442}
}