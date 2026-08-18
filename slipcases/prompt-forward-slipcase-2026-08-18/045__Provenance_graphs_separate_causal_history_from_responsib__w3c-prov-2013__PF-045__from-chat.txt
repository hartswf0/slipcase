ZETTEL

ID: PF-045

TITLE:
Provenance graphs separate causal history from responsibility only if responsibility is represented explicitly.

SOURCE:
Moreau and Missier, eds. — PROV-DM — 2013.

PASSAGE:
[PARAPHRASE] PROV distinguishes entities, activities, and agents and records relations of generation, use, derivation, association, and influence.

RESEARCH OBJECT:
A circuit diagram can describe production without automatically assigning normative responsibility.

LOCAL MOVE:
PROV makes history relational.

SOURCE TERMS:
entity; activity; agent; wasGeneratedBy; used; influence.

WHAT BECAME STRANGE:
A perfect causal graph can still leave “who answers for this claim?” unresolved.

QUESTION:
What additional relation is needed to move from provenance to scholarly responsibility?

DEEPER QUESTION:
Should responsibility be a provenance property at all, or a separate institutional judgment layered onto the graph?

MECHANISM:
<entities/activities/agents>
→ <PROV graph>
→ [trace production]
→ <descriptive provenance>
→ [? normative assignment ?]

FORMAL SHIFT:
NONE

SOURCE FORMALISM:
PROV-DM.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
PRODUCTION GRAPH + RESPONSIBILITY RULE = ACCOUNTABILITY MAP.

TENSION:
The aphorism's circuit diagram risks making descriptive trace look like adjudication.

MISSING:
Normative edges such as “defends claim,” “accepts responsibility,” “authorized inclusion.”

BOUNDARY:
PROV was not designed to settle authorship.

CITATION TRAIL:
PROV-O responsibility concepts; CRediT; publication ethics.

TEST:
Add responsibility relations to real AI-writing provenance graphs and test whether evaluators find them more useful than causal provenance alone.

PLATFORM:
[[From Provenance to Accountability]]

LINKS:
[[PROV]]
[[Responsibility]]
[[Causal Graph]]

BIBTEX:
@techreport{moreau2013prov,
  editor={Luc Moreau and Paolo Missier},
  title={PROV-DM: The PROV Data Model},
  institution={World Wide Web Consortium},
  year={2013}
}