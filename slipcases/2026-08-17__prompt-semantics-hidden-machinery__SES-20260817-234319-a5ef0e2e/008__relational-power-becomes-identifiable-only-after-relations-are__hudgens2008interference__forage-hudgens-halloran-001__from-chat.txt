ZETTEL

ID:
FORAGE-HUDGENS-HALLORAN-001

TITLE:
RELATIONAL POWER BECOMES IDENTIFIABLE ONLY AFTER RELATIONS ARE CUT INTO GROUPS

SOURCE:
Michael G. Hudgens and M. Elizabeth Halloran — Toward Causal Inference With Interference — 2008 — §2.1 Potential Outcomes

PASSAGE:
[PARAPHRASE]
Hudgens and Halloran relax the usual assumption that one person's outcome cannot depend on another person's treatment. Their potential outcome Y_ij(z_i) can depend on the treatment assignments of other people in the same group.

But the notation simultaneously assumes that treatment assignments in every other group cannot affect that person's outcome.

They call this partial interference.

RESEARCH OBJECT:
The move from individual causality to relational causality does not eliminate non-interference.

It moves the boundary.

LOCAL MOVE:
The source makes interference estimable by partitioning a population into groups inside which interference may occur and between which it may not.

SOURCE TERMS:
interference
partial interference
groups
potential outcomes
treatment program
contamination
SUTVA

WHAT BECAME STRANGE:
The boundary of the group is doing causal work.

What looks like a neutral description of the population determines which relations are allowed to exist in the estimand.

QUESTION:
If platform relations cross communities, feeds, markets, devices, and institutions, where could a defensible partial-interference boundary actually be drawn?

DEEPER QUESTION:
Does measuring relational power always require first constructing an exterior in which further relations are declared causally irrelevant?

MECHANISM:
<POPULATION WITH POSSIBLE INTERDEPENDENCE>
→ partition into groups
→ permit dependence within group
→ prohibit dependence across groups
→ define potential outcomes
→ identify direct / indirect / total / overall effects

FORMAL SHIFT:
<UNBOUNDED RELATIONAL FIELD>
→ <GROUPED POTENTIAL-OUTCOME SPACE>
→ [DECLARE CROSS-GROUP NON-INTERFERENCE]
→ <IDENTIFIABLE RELATIONAL EFFECTS>

SOURCE FORMALISM:
Hudgens and Halloran define the potential outcome of individual j in group i under the group's treatment vector z_i as:

Y_ij(z_i)

This permits Y_ij to depend on other treatment assignments within group i.

The notation assumes Y_ij(z_i) does not depend on treatment assignments in groups i' ≠ i.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

The estimator requires a cut:

RELATIONS
→ WITHIN(C): causally admissible
→ ACROSS(C): causally excluded

where C is the chosen partition.

Changing C can therefore change the causal object being measured.

TENSION:
[[FORAGE-HARDT-VILJOEN-001]] treated Hardt et al.'s non-interference assumption as potentially excluding the relational phenomenon of interest.

Hudgens and Halloran show that relaxing non-interference does not solve the problem in general.

Without restrictions on where interference can travel, the potential-outcome space becomes unwieldy.

The problem is therefore sharper:
relational power may require a boundary for identification, while platform power may consist partly in crossing precisely such boundaries.

MISSING:
A principled way to infer or test the boundaries of interference rather than stipulating them in advance.

A platform may generate:
cross-group recommendation effects,
migration,
shared trends,
market effects,
creator adaptation,
media coverage,
and institutional responses.

These processes make "sufficiently separate groups" difficult to define.

BOUNDARY:
Hudgens and Halloran do not claim partial interference is universally appropriate.

Their method explicitly requires groups sufficiently separated for cross-group interference to be plausibly absent.

CITATION TRAIL:
[[FORAGE-HARDT-VILJOEN-001]]
→ Hudgens and Halloran's partial-interference assumption
→ the group boundary becomes part of the causal model
→ network-interference and exposure-mapping literature
→ methods that permit interference without fixed isolated groups

TEST:
Take one platform intervention and estimate its indirect effect repeatedly under alternative partitions:

geographic region,
friendship community,
content cluster,
creator-audience network,
language group,
and randomly assigned artificial clusters.

If estimated relational power changes substantially with the partition, treat "group" as a causal modeling decision requiring empirical justification rather than preprocessing.

PLATFORM:
[[relational-power-under-interference]]

LINKS:
[[FORAGE-HARDT-VILJOEN-001]]
[[partial-interference-is-a-boundary-operation]]
[[the-unit-of-power-is-not-given]]

BIBTEX:
@article{hudgens2008interference,
  title={Toward Causal Inference With Interference},
  author={Hudgens, Michael G. and Halloran, M. Elizabeth},
  journal={Journal of the American Statistical Association},
  volume={103},
  number={482},
  pages={832--842},
  year={2008},
  doi={10.1198/016214508000000292}
}
