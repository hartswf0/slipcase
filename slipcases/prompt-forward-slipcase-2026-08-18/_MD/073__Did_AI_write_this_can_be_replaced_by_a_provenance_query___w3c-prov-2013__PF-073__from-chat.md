ZETTEL

ID: PF-073

TITLE:
“Did AI write this?” can be replaced by a provenance query only if the provenance captures decision points.

SOURCE:
Moreau and Missier, eds. — PROV-DM — 2013.

PASSAGE:
[PARAPHRASE] PROV represents how entities were generated, used, and influenced through activities and agents.

RESEARCH OBJECT:
The factory floor plan is naturally expressible as an event-and-dependency graph.

LOCAL MOVE:
The source supplies a formal vocabulary for tracing production.

SOURCE TERMS:
entity; activity; agent; use; generation.

WHAT BECAME STRANGE:
Provenance can show where the words came from yet still omit why a researcher kept them.

QUESTION:
What decision-event types must be added to a provenance graph for scholarly contribution?

DEEPER QUESTION:
Can “rejection,” “verification,” and “defense” be represented as activities with evidentiary force?

MECHANISM:
<sources/prompts/outputs>
→ <PROV graph>
→ [add decision activities]
→ <contribution trace>

FORMAL SHIFT:
NONE

SOURCE FORMALISM:
PROV-DM.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
Activities: SPECIFY, GENERATE, REJECT, VERIFY, ARRANGE, DEFEND.

TENSION:
Encoding judgment into event labels can oversimplify what the judgment involved.

MISSING:
Semantics for decision activities.

BOUNDARY:
PROV gives generic relations, not a ready-made AI-writing schema.

CITATION TRAIL:
Humanly; CRediT; provenance ontologies.

TEST:
Build a PROV extension for one chapter's production history and see which committee questions remain unanswered.

PLATFORM:
[[From AI Question to Provenance Query]]

LINKS:
[[PROV]]
[[Factory Floor]]
[[Decision Trace]]

BIBTEX:
@techreport{moreau2013prov,
  editor={Luc Moreau and Paolo Missier},
  title={PROV-DM: The PROV Data Model},
  institution={World Wide Web Consortium},
  year={2013}
}