ZETTEL

ID: PF-015

TITLE:
Provenance is selectable description, not necessarily total conversational capture.

SOURCE:
Moreau and Missier, eds. — PROV-DM: The PROV Data Model — 2013.

PASSAGE:
[PARAPHRASE] PROV represents entities, activities, agents, and relations describing how things were produced, used, and influenced.

RESEARCH OBJECT:
Provenance can follow consequential production relations without equating provenance with exhaustive recording.

LOCAL MOVE:
PROV supplies a structured account of what happened rather than requiring one undifferentiated history stream.

SOURCE TERMS:
entity; activity; agent; generation; use; influence.

WHAT BECAME STRANGE:
“Keep the whole conversation” is not the only imaginable provenance model.

QUESTION:
What rule should decide which prompt interactions become provenance entities and which remain disposable residue?

DEEPER QUESTION:
Can contribution-sensitive provenance be generated prospectively without distorting inquiry?

MECHANISM:
<events>
→ <provenance entities/activities>
→ [relate by use/generation/influence]
→ <trace>

FORMAL SHIFT:
<conversation stream>
→ <PROV-like graph>
→ [retain consequential relations]
→ <bounded provenance>

SOURCE FORMALISM:
W3C PROV entity/activity/agent relation model.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
PRESERVE(edge) iff edge is evidentially necessary for a consequential claim.

TENSION:
Selecting only “consequential” events requires a judgment that may become clear only retrospectively.

MISSING:
A prospective retention rule that does not require omniscience.

BOUNDARY:
PROV does not prescribe what a university should retain from AI conversations.

CITATION TRAIL:
PROV-O; workflow provenance; research-data retention standards.

TEST:
Have independent researchers compress the same AI interaction into minimal PROV graphs and measure disagreement over what must be retained.

PLATFORM:
[[Bounded Provenance]]

LINKS:
[[W3C PROV]]
[[Conversation Residue]]
[[Contribution-Sensitive Record]]

BIBTEX:
@techreport{moreau2013prov,
  editor={Luc Moreau and Paolo Missier},
  title={PROV-DM: The PROV Data Model},
  institution={World Wide Web Consortium},
  year={2013}
}