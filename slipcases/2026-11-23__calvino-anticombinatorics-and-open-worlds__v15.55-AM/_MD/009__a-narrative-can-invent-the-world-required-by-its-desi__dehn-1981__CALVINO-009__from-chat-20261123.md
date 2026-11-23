ZETTEL

ID: CALVINO-009

TITLE:
A narrative can invent the world required by its desired events.

SOURCE:
Natalie Dehn — "Story Generation After TALE-SPIN" — IJCAI (1981), pp. 16–17.

PASSAGE:
[PARAPHRASE]
Dehn challenges the assumption that authors first construct a complete fictional world and then let events unfold inside it. Writers frequently invent characters, places, and relationships to justify events they have already chosen.

RESEARCH OBJECT:
Retroactive construction of narrative worlds from desired dramatic outcomes.

LOCAL MOVE:
Dehn contrasts impartial world simulation with author-directed story generation. Her proposed AUTHOR model pursues narrative goals and reformulates them as the story develops.

SOURCE TERMS:
"author intentionality"; "conceptual reformulation";
"reminding"; "opportunity enhancement metagoal."

WHAT BECAME STRANGE:
The author's creative act may not be the final selection of a narrative from a preexisting possibility space. It may be the invention of a possibility space in which a desired narrative becomes plausible.

QUESTION:
Could anticombinatorics operate backward, constructing the necessary world from an imagined event rather than selecting an event from an already defined world?

DEEPER QUESTION:
When a fictional city is inferred from disparate images or narrative episodes, which properties must be shared and which can be invented afterward?

MECHANISM:
A desired episode creates explanatory requirements. The author introduces places, characters, relations, and earlier events to satisfy them.

FORMAL SHIFT:
Desired dramatic event
→ required causal conditions
→ [retroactive world construction]
→ supporting fictional world.

SOURCE FORMALISM:
Dehn distinguishes storyworld simulation from author-intent-based generation and describes goal reformulation and reminding. The conference paper does not supply a complete executable specification of every operation.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Given desired event E:

Find or construct world W
such that E is narratively possible in W.

W* = construct_world(E, narrative_goals)

This is not equivalent to reconstructing a historically real world from observations.

TENSION:
Retroactive worldbuilding risks arbitrary explanations. Forward simulation risks requiring too many irrelevant details before the story begins.

MISSING:
A method for preserving global world consistency while allowing new settings and backstories to be introduced on demand.

BOUNDARY:
Dehn's account concerns computational models of authorship. It does not establish that a generated world is geographically unique or that retrospective invention is equivalent to inference about reality.

CITATION TRAIL:
Dehn, "Story Generation After TALE-SPIN."
Meehan (1977).
Calvino, Invisible Cities.
Research on abductive reasoning and narrative planning.

TEST:
Begin with three independently imagined scenes from one fictional city. Compare forward world simulation with backward construction of a shared city capable of containing all three scenes. Record required inventions, contradictions, and unresolved spatial relations.

PLATFORM:
[[Narrative World Reconstruction]]
[[The Foundry — Imagined Place from Diverse Images]]

LINKS:
[[CALVINO-005]]
[[CALVINO-006]]
[[CALVINO-012]]
[[CALVINO-017]]

BIBTEX:
@inproceedings{dehn1981story,
  author    = {Dehn, Natalie},
  title     = {Story Generation After TALE-SPIN},
  booktitle = {Proceedings of the Seventh International Joint Conference on Artificial Intelligence},
  pages     = {16--17},
  year      = {1981},
  url       = {https://ijcai.org/proceedings/1981/4}
}
