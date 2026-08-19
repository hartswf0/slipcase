ZETTEL

ID:
FORAGE-OD-028

TITLE:
EVERY CASE IN THE ARCHIVE ADDS A DESCRIPTION AND NONE REMOVES ONE, WHICH FORFEITS THE CLEANEST AVAILABLE ISOLATION OF THE DESCRIPTION FROM ITS OBJECT

SOURCE:
Watson Hartsoe — PAPERS/operation-describe-label-01.md §3 and §7 ("Who can relabel the object?" via PAPERS/operation-describe-label-00.md §7); PAPERS/operative-description-framework.md §7 — 2026

PASSAGE:
[QUOTE]
label-01 §3:
"The counterfactual is the unlabeled or baseline state."

[QUOTE]
label-00 §7:
"Who can relabel the object? Who benefits from the label sticking?"

RESEARCH OBJECT:
The archive's designs all run in one direction: take an object, add a description, observe the route. The "unlabeled baseline" is always a *different* object — one that was never labeled.

Removal runs the manipulation on the same object. Label it, observe, unlabel it, observe again. The object is held perfectly constant because it *is* the same object. Nothing else in the archive achieves that.

LOCAL MOVE:
label-00 asks who can relabel and who benefits from a label sticking. Both questions presuppose removal. The answers document (label-01) drops them: §7 discusses who applies labels and §13 says operators contest "through system feedback loops such as appeals, relabeling, and retry protocols" — naming relabeling as a remedy and never as a method.

SOURCE TERMS:
relabel
unlabeled baseline
label sticking
appeals
retry protocols
reversibility
deprecation

WHAT BECAME STRANGE:
The archive's design chapter names reversibility as a virtue of good routing (label-01 §16: "easy contestability or reversibility"). Reversibility is treated as an ethical property of systems and never as an experimental resource for the researcher.

The thing the archive wants systems to have is the thing that would let it measure them.

QUESTION:
Does removing a description restore the prior route, or does the object retain a routing memory of having been described?

DEEPER QUESTION:
If routes do not fully revert, then descriptions leave a residue in the operator or the record — and "reversibility" as a design virtue is largely fictional, which would be the archive's strongest political finding and its most surprising one.

MECHANISM:
<OBJECT o, NO LABEL>  → baseline route r₀
<LABEL APPLIED>       → route r₁
<LABEL REMOVED>       → route r₂

Hysteresis (r₂ ≠ r₀) can arise from:
  operator memory (a maintainer who saw the label)
  record persistence (the removal is itself logged and visible)
  downstream artifacts (the label caused a comment, an assignment, a notification)
  model context (the removed description remains in an agent's history)

Each is separately testable, and each names a different party who retains the residue.

FORMAL SHIFT:
<DESCRIPTION APPLIED>
→ <ROUTE>
→ [DESCRIPTION REMOVED]
→ <RESIDUAL ROUTE>
→ <HYSTERESIS AS MEASURE OF INSCRIPTION DEPTH>

SOURCE FORMALISM:
NONE. No design in the archive includes a removal arm.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

  hysteresis h(D, o) = 𝒟( Act(· | o, D removed) ‖ Act(· | o, never labeled) )

h = 0 : the description was a valve; closing it restores the prior flow.
h > 0 : the description was an inscription; it changed the object's history and the history routes.

This gives the archive a *second* measure alongside ΔG, and the two together distinguish its two rival metaphors. The valve metaphor (label-01 §1: "symbolic valves") predicts h = 0. The inscription metaphor (Ricoeur, PAPERS/ricoeur.md §IV) predicts h > 0.

The archive uses both metaphors and has never noticed they make opposite predictions about removal.

TENSION:
READING A: labels are valves; removal restores the baseline; h ≈ 0.
READING B: labels are inscriptions; the trace persists; h > 0 and grows with the time the label was applied.

Discriminating evidence: GitHub's timeline API records label additions *and* removals with timestamps. h is estimable from public data today, at scale, with no consent problem, and nobody has estimated it.

MISSING:
Deprecated tool descriptions as a case. When a schema marks a function deprecated, the name persists and the description changes — a natural experiment in which the label is held fixed and only the description's stance moves.

BOUNDARY:
Hysteresis measured on GitHub confounds operator memory with record visibility, because removals are publicly logged. Separating them requires a setting where removal is silent, which GitHub is not.

CITATION TRAIL:
GitHub Timeline API — `unlabeled` events.
PAPERS/ricoeur.md §IV "Action as Inscription" — why removal should not restore.
Tombstoning and deprecation practice in API design.
FORAGE-OD-017, FORAGE-OD-022, FORAGE-OD-019.

TEST:
Scrape issues that were labeled and later unlabeled. Compare their post-removal activity to matched issues never labeled and to matched issues still labeled.

Three curves on one plot. If the removed group does not return to the never-labeled group, h > 0 and the valve metaphor fails — which would require rewriting the archive's opening defense.

PLATFORM:
[[unlabeling]]

LINKS:
[[FORAGE-OD-017]]
[[FORAGE-OD-022]]
[[FORAGE-OD-019]]
[[FORAGE-OD-015]]

BIBTEX:
@unpublished{hartsoe2026diligencequestions,
  author = {Hartsoe, Watson},
  title = {Due-Diligence Questions: Operative Description},
  note = {OPERATION DESCRIBE archive, PAPERS/operation-describe-label-00.md},
  year = {2026}
}
