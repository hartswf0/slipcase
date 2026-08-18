ZETTEL

ID:
SCGAI-003-A

TITLE:
Prompt history may not record the cognition; it may be part of the cognition.

SOURCE:
James Hollan, Edwin Hutchins, and David Kirsh — “Distributed Cognition: Toward a New Foundation for Human-Computer Interaction Research” — ACM TOCHI 7(2) — 2000 — pp. 174–196 — https://doi.org/10.1145/353485.353487

PASSAGE:
[QUOTE] “Processes may be distributed through time in such a way that the products of earlier events can transform the nature of later events.” (p. 176)

RESEARCH OBJECT:
Distributed cognition strengthens the move from final prompt to trajectory: earlier external products can participate in later cognition by changing the environment in which the next prompt is conceived.

LOCAL MOVE:
Replace PROMPT HISTORY AS PROVENANCE RECORD with PROMPT HISTORY AS ACTIVE COGNITIVE SUBSTRATE.

SOURCE TERMS:
distributed cognition; unit of analysis; external structure; distributed through time; products of earlier events; information trajectories

WHAT BECAME STRANGE:
Deleting history may remove part of the machinery by which the thinking was possible. The same final prompt accompanied by a different history can be a cognitively different object.

QUESTION:
Does access to prompt lineage change what users can infer, modify, or create even when the final prompt is identical?

DEEPER QUESTION:
Where should the prompting cognitive system end: user, user+model, user+model+history, or a temporally extended network of prior artifacts?

MECHANISM:
P0 → Y0 → interpretation0 → P1 → Y1 → …; each output alters the environment in which the next prompt is formulated.

FORMAL SHIFT:
HISTORY AS LOG(PAST) becomes HISTORY AS STATE(NOW).

SOURCE FORMALISM:
Distributed cognition examines processes across social members, between internal/external structures, and through time, where products of earlier events transform later events.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
GenerateNext=f(user_state,H_t,current_goal); removing H_t while preserving P_t can change the available computation.

TENSION:
History could genuinely support cognition or merely contain information experts have internalized; functional contribution must be demonstrated.

MISSING:
Controlled evidence separating usefulness of the final prompt from usefulness of its trajectory, including branching rather than flattened chronology.

BOUNDARY:
Distributed cognition does not imply every artifact is cognitive; inclusion requires a demonstrated functional relationship.

CITATION TRAIL:
[[SCGAI-003]] → prompts modify over time → [[SCGAI-007]] → distributed cognition → Hollan/Hutchins/Kirsh 2000 → test documentary versus constitutive lineage.

TEST:
Give matched groups the same final prompt, with or without full failed/branching history, then test transfer to a related task.

PLATFORM:
Iterative generative-AI interfaces / prompt history systems

LINKS:
[[SCGAI-003]]
[[SCGAI-007]]

BIBTEX:
@article{hollan2000distributed, author={Hollan, James and Hutchins, Edwin and Kirsh, David}, title={Distributed Cognition: Toward a New Foundation for Human-Computer Interaction Research}, journal={ACM Transactions on Computer-Human Interaction}, volume={7}, number={2}, pages={174--196}, year={2000}, doi={10.1145/353485.353487}, url={https://doi.org/10.1145/353485.353487}}
