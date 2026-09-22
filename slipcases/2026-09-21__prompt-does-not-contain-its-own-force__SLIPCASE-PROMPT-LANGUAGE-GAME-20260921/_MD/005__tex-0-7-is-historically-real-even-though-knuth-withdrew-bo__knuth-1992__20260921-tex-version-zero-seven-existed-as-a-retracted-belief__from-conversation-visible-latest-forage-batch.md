ZETTEL

ID:
20260921-tex-version-zero-seven-existed-as-a-retracted-belief

TITLE:
TeX 0.7 Is Historically Real Even Though Knuth Withdrew Both the Change and the Version

SOURCE:
Donald E. Knuth — “The Error Log of TeX” — entries for 30 October and 1 November 1982; collected in Literate Programming — 1992. ([dokumen.pub](https://dokumen.pub/literate-programming-1.html?utm_source=chatgpt.com))

PASSAGE:
[PARAPHRASE] On 30 October 1982 Knuth recorded that he had found what he believed was a definitive definition of the printer’s point, changed TeX accordingly, and incorporated the change into Version 0.7. On 1 November he wrote “Oops!”, retracted error 546, retracted TeX Version 0.7, judged the source flaky, and returned to his earlier value after confirmation from NBS Circular 570. ([dokumen.pub](https://dokumen.pub/literate-programming-1.html?utm_source=chatgpt.com))

RESEARCH OBJECT:
A software version functioning as an epistemic event even after its technical state is withdrawn.

LOCAL MOVE:
The error log preserves a state that ordinary release history might erase: not just incorrect code, but a temporarily accepted source hierarchy and the reason for reversing it.

SOURCE TERMS:
definitive
conjecture
Version 0.7
retract
flaky
confirmed
NBS Circular 570

WHAT BECAME STRANGE:
Version 0.7 disappears from the accepted technical lineage but remains essential to the knowledge lineage. The important artifact is partly a belief transition that cannot be reconstructed from the surviving code alone.

QUESTION:
Should an evolving prompt system assign persistent identities to retracted configurations so later researchers can cite the failed theory they embodied?

DEEPER QUESTION:
What should versioning mean when two configurations have identical active text but differ because one comes before a failed intervention and the other after its retraction?

MECHANISM:
source judged authoritative
→ rule changed
→ version emitted
→ source credibility collapses
→ rule reverted
→ version withdrawn
→ previous technical state restored
→ epistemic state remains changed.

FORMAL SHIFT:
<VERSION = ACTIVE FILE STATE>
→ <VERSION = FILE STATE + EVIDENCE STATE>
→ [RETRACT]
→ <TECHNICAL RETURN WITHOUT EPISTEMIC RETURN>

SOURCE FORMALISM:
The chronological error log assigns numbered changes, dates, version transitions, retractions, and explanatory comments. ([dokumen.pub](https://dokumen.pub/literate-programming-1.html?utm_source=chatgpt.com))

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
Config_A(text=x, history=unquestioned)
≠
Config_B(text=x, history=reverted_after_falsification)

TENSION:
Persisting every rejected configuration may overwhelm later maintainers and give weak or mistaken experiments disproportionate archival weight.

MISSING:
Admission rules determining which failed configurations deserve stable archival identity.

BOUNDARY:
Knuth’s log records a highly disciplined deterministic software project. Stochastic agent experiments can generate far more ambiguous reversals.

CITATION TRAIL:
[[20260921-tex-error-log-preserves-retracted-belief]]
→ exact TeX 0.7 retraction
→ negative knowledge requires version identities that survive rollback.

TEST:
When a prompt change is reverted, require a RETRACTED version object containing old configuration, triggering evidence, reason for retraction, and later reproducer. Test whether future maintainers avoid independently rediscovering the same false fix.

PLATFORM:
[[prompt-harness]]

LINKS:
[[20260921-tex-error-log-preserves-retracted-belief]]
[[retraction]]
[[negative-knowledge]]
[[version-identity]]

BIBTEX:
@book{knuth1992literate,
  author = {Knuth, Donald E.},
  title = {Literate Programming},
  year = {1992},
  publisher = {Center for the Study of Language and Information}
}
