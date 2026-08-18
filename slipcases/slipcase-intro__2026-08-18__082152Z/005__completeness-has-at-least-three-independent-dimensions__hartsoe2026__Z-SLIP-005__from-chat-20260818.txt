ZETTEL

ID:
Z-SLIP-005

TITLE:
Completeness has at least three independent dimensions

SOURCE:
Watson Hartsoe — SLIPCASE — 2026 — “Missing is data”

PASSAGE:
[PARAPHRASE]
SLIPCASE distinguishes how much source material was available, whether discovered candidates were classified, and whether generated files and counts mechanically reconcile.

RESEARCH OBJECT:
Claims of archival completeness become misleading when epistemic coverage, workflow coverage, and mechanical consistency are collapsed into a single status.

LOCAL MOVE:
The specification decomposes “complete” into separately auditable claims.

SOURCE TERMS:
available
unswept
classified
reconciled
visible context
missing is data

WHAT BECAME STRANGE:
An archive can be mechanically perfect and epistemically tiny.

QUESTION:
What classes of completeness need to remain orthogonal in AI-mediated research?

DEEPER QUESTION:
Can a system be designed so that it is structurally difficult to utter an unqualified “complete”?

MECHANISM:
Separate state variables prevent one successful verification operation from laundering uncertainty in another layer.

FORMAL SHIFT:
<ambiguous completeness>
→ <multiple independent coverage states>
→ [REPORT SEPARATELY]
→ <bounded completeness claim>

SOURCE FORMALISM:
Three distinct answers:
source availability
candidate classification
mechanical reconciliation

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

C = (
  SOURCE_COVERAGE,
  CLASSIFICATION_COVERAGE,
  MECHANICAL_RECONCILIATION
)

No scalar COMPLETE(C).

TENSION:
Users often need a single actionable status, while multidimensional completeness resists compression.

MISSING:
A vocabulary for unknown denominators, where even the amount of unseen material cannot be estimated.

BOUNDARY:
Separating completeness dimensions improves honesty but does not establish whether the discovery process itself was adequate.

CITATION TRAIL:
Data quality dimensions; recall estimation; archival completeness; uncertainty representation; missing-data taxonomy.

TEST:
Take a checkpoint currently described as “complete” and score its three dimensions independently. Observe whether materially different states were hidden by the single label.

PLATFORM:
[[multidimensional completeness]]

LINKS:
[[missing is data]]
[[mechanical reconciliation]]
[[unknown denominator]]
[[bounded claims]]

BIBTEX:
@misc{hartsoe2026slipcase,
  author = {Hartsoe, Watson},
  title = {SLIPCASE: A Research Checkpoint Compiler},
  year = {2026},
  note = {Working specification}
}
