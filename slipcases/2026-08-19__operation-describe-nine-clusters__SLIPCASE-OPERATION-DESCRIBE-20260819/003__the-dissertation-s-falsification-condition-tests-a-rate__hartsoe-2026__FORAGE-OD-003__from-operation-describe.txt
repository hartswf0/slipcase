ZETTEL

ID:
FORAGE-OD-003

TITLE:
THE DISSERTATION'S FALSIFICATION CONDITION TESTS A RATE WHILE THE THEORY CLAIMS A DISTRIBUTION

SOURCE:
Watson Hartsoe — OPERATION DESCRIBE archive — PAPERS/operation-describe-label-01.md §17 "Disproof: Falsification Metrics" and Final Checklist Q9 — 2026

PASSAGE:
[QUOTE]
"The theory is falsified if experimentally varying LLM tool description text fails to change tool call rates under identical prompts, or if adding GitHub issue labels has no statistical effect on issue resolution times."

RESEARCH OBJECT:
The theory claims descriptions alter an operator's action-space. The disproof condition inspects a single scalar summary of that space — a call rate, a resolution time.

A description can leave the rate untouched while completely rearranging *which* calls, with *what* arguments, in *what* order. Under the stated condition, that description is scored non-operative.

LOCAL MOVE:
The archive converts a claim about structure into a claim about frequency, because frequency is what is cheap to log.

This is a measurement-availability substitution, and it is invisible because both are written as "change."

SOURCE TERMS:
falsified
tool call rates
statistical effect
resolution times
identical prompts
non-operative
ΔG = 0

WHAT BECAME STRANGE:
The archive's most rigorous-looking sentence is its weakest. It offers a test that its own theory should predict will frequently return "non-operative" for descriptions that are obviously doing work.

Rate-invariance is the *expected* signature of a description that redistributes rather than amplifies.

QUESTION:
What is the smallest change to the disproof condition that makes it capable of failing the theory for the right reason?

DEEPER QUESTION:
If the honest test is a distributional one, does the dissertation's public falsifiability claim survive contact with the sample sizes distributional tests require?

MECHANISM:
<DESCRIPTION VARIANT>
→ changes conditional distribution over ⟨tool, arguments, order, refusal⟩
→ [ANALYST COLLAPSES DISTRIBUTION TO MARGINAL CALL RATE]
→ redistribution cancels in the marginal
→ rate unchanged
→ description scored ΔG = 0
→ theory recorded as weakened by evidence that in fact confirms it

FORMAL SHIFT:
<ACTION DISTRIBUTION>
→ <MARGINAL RATE>
→ [SIGNIFICANCE TEST]
→ <FALSE NEGATIVE ON OPERATIVITY>

SOURCE FORMALISM:
NONE. The archive supplies no test statistic, no power analysis, and no pre-registered effect size.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Current condition, implicitly:
  H0 : E[1(call)] is equal across description variants

Required condition:
  H0 : Act(· | D₁) = Act(· | D₂) as distributions over ⟨tool, args, order, refusal⟩

The second implies the first; the first does not imply the second.

A description that is *purely redistributive* satisfies H0 in the first sense and violates it in the second. The archive currently has no name for this case; call it a **conservative route change**.

TENSION:
READING A: the rate test is a pragmatic proxy and the distributional claim is what the author means; the sentence is loose, not wrong.

READING B: the rate test is what will actually be run, defended, and reported, because it is the only version that is cheap. On this reading the proxy will silently become the theory.

MISSING:
A pre-registration. A named test statistic. A power analysis. A single worked example distinguishing amplifying from redistributive descriptions.

BOUNDARY:
This does not show the primary case is unrunnable. It shows the stated disproof is mis-specified relative to the stated claim.

CITATION TRAIL:
PAPERS/abc-cineosis-paper.md §4 Case 1 (the same test, restated as "delta in invocation rates and the propagation of parameter checks" — note that "propagation of parameter checks" is already distributional and is the better formulation buried in a different file).
Pre-registration norms in HCI.
Multivariate tests for categorical outcome distributions.

TEST:
Construct one description pair designed to be exactly rate-preserving and argument-changing — e.g. "Issue refund" vs "Issue refund only if invoice is uploaded." Run both. Report the call rate and the argument distribution side by side.

If the rate is flat and the arguments move, the archive has an empirical instance of a conservative route change, and the disproof condition must be rewritten.

PLATFORM:
[[the-measure-problem-in-operative-description]]

LINKS:
[[FORAGE-OD-001]]
[[FORAGE-OD-002]]
[[FORAGE-OD-004]]

BIBTEX:
@unpublished{hartsoe2026diligenceanswers,
  author = {Hartsoe, Watson},
  title = {Due-Diligence Answers: Operative Description},
  note = {OPERATION DESCRIBE archive, PAPERS/operation-describe-label-01.md},
  year = {2026}
}
