ZETTEL

ID:
FORAGE-OD-001

TITLE:
THE CENTRAL METRIC OF OPERATIVE DESCRIPTION SUBTRACTS TWO SPACES AND CALLS THE RESULT A NUMBER

SOURCE:
Watson Hartsoe — OPERATION DESCRIBE archive — PAPERS/attention-tax-semiotics.md §14 "The Formal Model" — 2026; cross-read with PAPERS/operative-description-framework.md §5 "Boundary and Validation" — 2026

PASSAGE:
[QUOTE]
attention-tax-semiotics.md §14:
"M(D, O, S) = Act_after(D, O, R, A) - Act_before(D, O, R, A)"

[QUOTE]
operative-description-framework.md §5:
"A description is non-operative when it does not change the generation, selection, revision, interpretation, or archival status of an output (ΔG = 0)."

RESEARCH OBJECT:
The load-bearing quantity of the entire dissertation is written as an arithmetic difference between two objects that are not numbers.

Act is an action-space. ΔG is announced as an equality with zero. Nothing in the archive defines subtraction on action-spaces, or the zero element of that structure.

LOCAL MOVE:
The archive imports the notation of a difference in order to make operativity look measurable, and thereby to make the boundary claim ("when is a description NOT operative") look falsifiable.

The notation does the rhetorical work of a metric without ever being given a metric.

SOURCE TERMS:
action-space
generation-space delta
ΔG
ΔP
attention tax
operator
non-operative
observable difference

WHAT BECAME STRANGE:
"ΔG = 0" reads as an empirical condition but functions as a definition.

Because no measure is supplied, any disagreement about whether a description was operative becomes a disagreement about what to count, not about what happened.

QUESTION:
What mathematical structure must the action-space have for ΔG = 0 to be a checkable claim rather than an interpretive judgment?

DEEPER QUESTION:
If the archive's own YAML schema already records the delta as a set of changed channels rather than a scalar, is the scalar formalism not merely unfinished but wrong for the object?

MECHANISM:
<DESCRIPTION D>
→ enters an operator's context
→ changes the operator's set of available/likely actions
→ [ARCHIVE WRITES THIS AS Act_after − Act_before]
→ the subtraction is never defined
→ operativity becomes adjudicated by the analyst rather than measured

FORMAL SHIFT:
<ACTION SPACE>
→ <SCALAR DIFFERENCE>
→ [FALSIFICATION CLAIM]
→ <UNCHECKABLE BOUNDARY>

SOURCE FORMALISM:
The archive supplies:

O = ⟨A, M, P, R, G, Act, F⟩
D : S → S'
M(D, O, S) = Act_after − Act_before
Tax(D, O) = resources required for O to parse D without error
failure iff Tax(D, O) > A(O)

It does not supply: the type of Act, a norm on Act, or a definition of the difference operator.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let Act be a probability distribution over a finite action set 𝒜.

Then the missing operator is a divergence, not a subtraction:

ΔG(D) = 𝒟( Act(· | context + D) ‖ Act(· | context) )

with 𝒟 any statistical distance (total variation, KL, Jensen–Shannon).

Non-operative becomes a threshold claim, not an identity:

D is non-operative at level ε iff ΔG(D) < ε

This immediately exposes what the scalar notation hid: ε must be justified, and ΔG is a function of the operator and the context, never of D alone.

TENSION:
READING A: ΔG is shorthand for a real but unformalized quantity, and formalizing it is routine cleanup.

READING B: ΔG cannot be a scalar at all, because the archive's own data schema records the delta as six independent qualitative channels (style, world_state, interface, narrative, image_text_relation, archive_status). On that reading the scalar formalism misdescribes the object and should be replaced, not completed.

MISSING:
A stated type for Act. A justified ε. Any worked example in the archive where ΔG is computed rather than asserted.

BOUNDARY:
The evidence licenses only the claim that the archive's formalism is under-specified. It does not license the claim that operative description is false, unmeasurable, or trivial.

CITATION TRAIL:
PAPERS/operative-description-framework.md §6 (the generation_delta YAML block, which is already a six-channel measure).
PAPERS/witt.md §7 "Measurement as Contact" (the archive's own theory of measurement, never applied to ΔG).
Statistical distance in distribution-shift literature.
Performative prediction (Perdomo et al.) for a worked formalism of "the description changes the distribution it describes."

TEST:
Take one existing entry from the archive's YAML schema. Recompute its generation_delta as a vector in {0,1}^6. Then ask whether any of the archive's prose claims about ΔG survive when the delta is a vector rather than a number.

If a prose claim requires ordering two deltas ("more operative than"), the scalar formalism is doing work the six-channel measure cannot do — and that work must be justified separately.

PLATFORM:
[[the-measure-problem-in-operative-description]]

LINKS:
[[FORAGE-OD-002]]
[[FORAGE-OD-003]]
[[FORAGE-OD-033]]

BIBTEX:
@unpublished{hartsoe2026attentiontax,
  author = {Hartsoe, Watson},
  title = {Attention-Tax Semiotics: Cybernetic Operator Pragmatics and the Constellation of Meaning},
  note = {OPERATION DESCRIBE archive, PAPERS/attention-tax-semiotics.md},
  year = {2026}
}
