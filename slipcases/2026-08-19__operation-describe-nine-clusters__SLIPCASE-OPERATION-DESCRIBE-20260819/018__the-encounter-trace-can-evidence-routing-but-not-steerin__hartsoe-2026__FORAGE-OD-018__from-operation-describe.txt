ZETTEL

ID:
FORAGE-OD-018

TITLE:
THE ENCOUNTER TRACE CAN EVIDENCE ROUTING BUT NOT STEERING, AND THE ARCHIVE USES THE WORDS INTERCHANGEABLY

SOURCE:
Watson Hartsoe — PAPERS/operative-description-framework.md §8 (controlled vocabulary, "Steering") and §9 (contribution architecture); PAPERS/abc-cineosis-paper.md §4 (the encounter trace ⟨A, B, C, R, A'⟩); against PAPERS/ricoeur.md §III "The Death of Naive Intention" — 2026

PASSAGE:
[QUOTE]
framework §8:
"Steering: The ethical/design problem of guiding generative systems without pretending to fully control them."

[QUOTE]
framework §9:
"CORE CONTRIBUTION ────► Operative description as a theory of generative steering."

[PARAPHRASE]
ricoeur.md §III: inscription severs the trace from the author's intention; what the trace means cannot be settled by appeal to what was meant.

RESEARCH OBJECT:
Routing is a property of a system: a description changed which action occurred. Steering is a property of an agent: someone intended the change and adjusted toward a goal.

The archive's evidence base — prompt logs, revision chains, encounter traces — is inscribed action. By the archive's own hermeneutics, inscribed action does not testify to intention. So the evidence can establish routing and cannot establish steering.

LOCAL MOVE:
The framework names steering as the *core* contribution while banning "cybernetic" and "operator" from the vocabulary (framework §8). It keeps the helmsman and discards the words that made the helmsman a technical concept.

What remains is a claim about intention supported by evidence about consequence.

SOURCE TERMS:
steering
routing
encounter trace
prompt-output-revision loop
guiding without fully controlling
revision decision: accept / reject / revise / fork

WHAT BECAME STRANGE:
The archive's revision log has a field for the operator's decision (accept / reject / revise / fork) and treats it as evidence of steering.

But a recorded decision is another inscription. It is the detective's report from ryl-01: written after the achievement, cleaned of false starts, arranged to justify. The archive's own Ryle chapter says such a record is not a transcript of the search.

The archive's method chapter trusts exactly the kind of document its theory chapter taught it to distrust.

QUESTION:
What evidence could distinguish an operator who steered from an operator who was routed and then wrote down a rationale?

DEEPER QUESTION:
If no such evidence exists in principle, should the dissertation's core contribution be restated as a theory of *routing*, with steering demoted to a design aspiration?

MECHANISM:
Routing (observable):
<DESCRIPTION> → <ACTION CHANGE> → <LOGGED>

Steering (not observable from the log):
<GOAL> → <MODEL OF THE SYSTEM> → <CHOSEN DESCRIPTION> → <FEEDBACK COMPARED TO GOAL> → <CORRECTION>

The log records the first and second-to-last terms. It records neither the goal nor the comparison. Both are supplied by the analyst, who is also the operator.

FORMAL SHIFT:
<ENCOUNTER TRACE>
→ <SEQUENCE OF INSCRIPTIONS>
→ [ANALYST SUPPLIES GOAL AND COMPARISON]
→ <NARRATIVE OF STEERING>

SOURCE FORMALISM:
The archive supplies the trace ⟨A, B, C, R, A'⟩ and the loop OD → TP → PORL → WT. Neither contains a goal term or an error term. A control system without a setpoint and an error signal is not a control system.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Minimal conditions for a steering claim:

  1. goal g declared *before* the loop, not reconstructed after
  2. an error measure e_t = δ(output_t, g) computable by a third party
  3. evidence that the next description was selected to reduce e_t
  4. e_t decreasing over the loop more than under a control policy that ignores e_t

The archive's practice-based method can satisfy 1–3 with one procedural change: pre-register the goal per loop.
Condition 4 requires a comparison arm the archive has never proposed: a *random-revision* control.

Without the random-revision arm, every practice-based archive shows a trajectory and calls it steering.

TENSION:
READING A: this demands a positivist standard inappropriate to practice-based research, where the researcher's judgment is the instrument.
READING B: the archive itself demands falsifiability, counterfactuals, and negative cases in five separate documents. Holding its own method to a lower bar than its objects is the inconsistency, not the standard.

MISSING:
Pre-registered goals in any archive entry. Any random-revision control. Any third-party-computable error measure. The YAML schema (framework §6) has `revision_decision` but no `goal` and no `error`.

BOUNDARY:
This does not show that no steering occurred. It shows the archive's evidence type cannot distinguish steering from post-hoc rationalization, and that the fix is procedural and cheap.

CITATION TRAIL:
Ricoeur — "The Model of the Text" — on intention and the autonomy of the trace.
PAPERS/ryl-01.md — the detective's report as retrospective artifact.
Ashby, Design for a Brain — for what a setpoint and error signal formally require.
PAPERS/winnograd.md §5 — Suchman on plans as resources for action rather than determinants of it, which is the same split under different names.
FORAGE-OD-012, FORAGE-OD-017, FORAGE-OD-024.

TEST:
Add two fields to the archive's YAML schema: `goal` (written before the prompt) and `error_note` (written before seeing the output). Run twenty entries with them.

Then add a control arm: twenty entries where the next prompt is drawn at random from a pool of plausible revisions. Compare trajectories.

If the pre-registered arm converges faster on the declared goal, steering is evidenced. If not, the archive has discovered something more interesting than steering.

PLATFORM:
[[routing-is-not-steering]]

LINKS:
[[FORAGE-OD-017]]
[[FORAGE-OD-012]]
[[FORAGE-OD-024]]
[[FORAGE-OD-027]]

BIBTEX:
@unpublished{hartsoe2026framework,
  author = {Hartsoe, Watson},
  title = {Operation Describe: Practice-Based Dissertation Framework},
  note = {OPERATION DESCRIBE archive, PAPERS/operative-description-framework.md},
  year = {2026}
}
