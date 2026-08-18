ZETTEL

ID: PF-064

TITLE:
Minimal provenance is a compression problem with epistemic loss.

SOURCE:
Moreau and Missier, eds. — PROV-DM — 2013.

PASSAGE:
[PARAPHRASE] Provenance records selected relations among entities, activities, and agents rather than requiring raw replay of every event.

RESEARCH OBJECT:
“Preserve only the quarry needed to prove the stone” requires a lossy compression criterion.

LOCAL MOVE:
PROV supports structured abstraction, but the choice of granularity remains external.

SOURCE TERMS:
provenance; entity; activity; relation.

WHAT BECAME STRANGE:
What looks like provenance hoarding before a dispute can become missing evidence afterward.

QUESTION:
What can safely be discarded before future claims are known?

DEEPER QUESTION:
Should provenance have multiple retention tiers rather than one minimal record?

MECHANISM:
<full event stream>
→ <selection/compression>
→ [retain provenance graph]
→ <future evidentiary use>

FORMAL SHIFT:
NONE

SOURCE FORMALISM:
PROV.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
MINIMAL PROVENANCE is claim-relative and time-relative.

TENSION:
Prospective minimality and retrospective sufficiency pull in opposite directions.

MISSING:
Retention policy under uncertainty.

BOUNDARY:
The source does not prescribe data-retention duration or granularity.

CITATION TRAIL:
Research-data retention; privacy minimization; audit logs.

TEST:
Simulate later disputes against provenance records compressed at different levels and measure evidentiary failure.

PLATFORM:
[[The Provenance Compression Problem]]

LINKS:
[[Data Minimization]]
[[Provenance]]
[[Future Claim]]

BIBTEX:
@techreport{moreau2013prov,
  editor={Luc Moreau and Paolo Missier},
  title={PROV-DM: The PROV Data Model},
  institution={World Wide Web Consortium},
  year={2013}
}