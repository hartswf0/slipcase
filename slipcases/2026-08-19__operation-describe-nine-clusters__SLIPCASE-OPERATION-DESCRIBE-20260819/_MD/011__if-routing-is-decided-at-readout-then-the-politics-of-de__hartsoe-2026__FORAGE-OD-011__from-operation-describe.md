ZETTEL

ID:
FORAGE-OD-011

TITLE:
IF ROUTING IS DECIDED AT READOUT, THEN THE POLITICS OF DESCRIPTION IS THE POLITICS OF A COMMITMENT RULE NOBODY WRITES DOWN

SOURCE:
Shiyang Chen — arXiv:2606.16364 — 2026, read against Watson Hartsoe — PAPERS/operation-describe-label-01.md §7 "Authority: Asymmetric Platform Power" and §15 "Power: Asymmetric Discipline" — 2026

PASSAGE:
[QUOTE]
label-01 §7:
"Descriptions only route when backed by systemic authority. Maintainers label issues; platform policies enforce toxicity queues; developers define schemas. The political question is: who controls the categories that route action, and who is routed by them?"

[PARAPHRASE]
Chen locates the deciding computation at a late-layer readout, downstream of every segment the schema author wrote.

RESEARCH OBJECT:
The archive's political chapter locates authority in whoever *writes* the description. The mechanism locates the decision in whoever *trained the commitment rule*.

Those are different parties, and only one of them is nameable in the archive's current account.

LOCAL MOVE:
Chen's finding relocates agency without intending to. It says: the harness is not the bottleneck. The harness is exactly what the schema author controls.

SOURCE TERMS:
readout stage
harness
systemic authority
categories that route action
asymmetric discipline
commitment

WHAT BECAME STRANGE:
The archive asks "who controls the descriptions that route action" and answers "platform architects, software developers, institutional administrators."

But for the machine operator, the party with the most routing power is the one who determined how representations become commitments — a post-training decision, undocumented, unversioned in the artifact the researcher can see, and belonging to neither the schema author nor the user.

Authority in the primary case is held by an absent third party.

QUESTION:
Who is the responsible party for a route decided by a commitment rule that no schema author wrote and no user can inspect?

DEEPER QUESTION:
Does the archive's contestability requirement ("easy contestability or reversibility," label-01 §16) become incoherent when the decisive rule is not a text at all?

MECHANISM:
<SCHEMA AUTHOR> writes name + description
→ enters harness
→ [POST-TRAINING COMMITMENT RULE, AUTHORED ELSEWHERE, DECIDES]
→ route
→ <CONSEQUENCE BORNE BY THE ROUTED SUBJECT>

The chain has three parties and the archive's political vocabulary names two.

FORMAL SHIFT:
<AUTHORED DESCRIPTION>
→ <REPRESENTATION>
→ [UNAUTHORED COMMITMENT RULE]
→ <ROUTE>
→ <UNCONTESTABLE OUTCOME>

SOURCE FORMALISM:
NONE in the political register. Chen supplies mechanism; the archive supplies politics; nothing joins them.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Three-party routing:

  A₁ = author of the description (visible, citable, contestable)
  A₂ = author of the commitment rule (invisible, uncitable, versioned only as a model name)
  A₃ = the routed subject

The archive's political claim is about A₁ → A₃.
The mechanism says most of the routing power is A₂ → A₃.

Contestability requires an addressable party. A₂ is addressable only through a version string.

TENSION:
READING A: A₂ is just infrastructure, like a compiler; we do not hold compiler authors politically responsible for what programs do.
READING B: unlike a compiler, A₂'s rule is statistical, undocumented, and changes without notice between versions — so the compiler analogy licenses an irresponsibility the archive would not accept for any human institution.

The archive's own banned-terms list forbids "compiler" (framework §8) — a prohibition that now looks prescient rather than stylistic.

MISSING:
Any method in the archive for attributing a route between A₁ and A₂. Without it, the political chapter cannot assign responsibility for the primary case.

BOUNDARY:
This says the archive's authority account is incomplete for machine operators. It says nothing against the account for human operators, where A₁ and A₂ often coincide in an institution.

CITATION TRAIL:
PAPERS/cyber-00.md §11 and PAPERS/cyber-02.md §2 — Barad's agential cut, which is the archive's existing tool for exactly this question of where responsibility is drawn.
Model-card and version-pinning practice.
FORAGE-OD-014, FORAGE-OD-032.

TEST:
Hold description and prompt fixed. Vary only the model version across a provider's release history. Measure route change.

Any ΔG obtained is attributable to A₂ alone. Comparing that ΔG to the description-induced ΔG gives the first empirical apportionment of routing authority in the archive.

PLATFORM:
[[allocation-is-not-commitment]]

LINKS:
[[FORAGE-OD-010]]
[[FORAGE-OD-014]]
[[FORAGE-OD-032]]

BIBTEX:
@unpublished{hartsoe2026diligenceanswers,
  author = {Hartsoe, Watson},
  title = {Due-Diligence Answers: Operative Description},
  note = {OPERATION DESCRIBE archive, PAPERS/operation-describe-label-01.md},
  year = {2026}
}
