ZETTEL

ID: TEST-001

TITLE:
Simulation testing does not test “the game” at once; it tests whether one statistical consequence falls inside an acceptable range.

SOURCE:
UK Gambling Commission — Testing Strategy for Compliance with Remote Gambling and Software Technical Standards — Procedure for Testing — 2024.

SOURCE URL:
https://www.gamblingcommission.gov.uk/strategy/testing-strategy-for-compliance-with-remote-gambling-and-software-technical/3-procedure-for-testing

PASSAGE:
[PARAPHRASE] The Commission defines simulation testing as automated high-volume play used to determine whether actual RTP falls within an acceptable range of expected RTP.

RESEARCH OBJECT:
Testing becomes analytically interesting when decomposed by what each test can actually see. Simulation testing observes aggregate statistical performance; emulation targets rare outcomes; manual play exposes common player-visible behavior.

LOCAL MOVE:
The testing strategy distributes epistemic access across different test procedures instead of treating “tested” as a single condition.

SOURCE TERMS:
simulation testing
emulation testing
manual game play
actual RTP
expected RTP
rare game outcomes
game fairness

WHAT BECAME STRANGE:
A certificate can summarize multiple epistemically different encounters with the software. “The software was tested” hides which behaviors were observable under which procedure.

QUESTION:
What does a test make visible, and therefore what can remain invisible while still passing?

DEEPER QUESTION:
Are technical standards best understood not merely as rules governing machines but as epistemic architectures governing what institutions are capable of knowing about machines?

MECHANISM:
<SYSTEM>
→ choose test procedure
→ [PRODUCE PARTICULAR EVIDENCE]
→ <COMPLIANCE JUDGMENT>

Simulation:
many runs → aggregate distribution

Emulation:
constructed condition → rare outcome behavior

Manual play:
human interaction → ordinary visible behavior

FORMAL SHIFT:
<SOFTWARE>
→ <TEST-SPECIFIC OBSERVATION>
→ [EVALUATE]
→ <CERTIFICATION EVIDENCE>

SOURCE FORMALISM:
The Commission distinguishes at least:
SIMULATION
EMULATION
MANUAL GAME PLAY

and assigns different evidentiary purposes to each.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

OBSERVABLE(SYSTEM, TEST) ≠ SYSTEM

Therefore:

PASS(TEST₁) ⇏ PASS(TEST₂)

and:

Σ PASS(TESTᵢ) still does not imply exhaustive observation of SYSTEM.

TENSION:
The uploaded source compresses certification into a story in which an agency runs “hundreds of thousands” of playthroughs, searches for patterns, and certifies the RNG if none appear. fileciteturn0file0L84-L94 The Commission's testing strategy distinguishes multiple forms of evidence and requires reports to identify test scope, methods, versions, platforms, limitations, and results.

MISSING:
The public regulatory guidance does not reveal every proprietary procedure an approved testing laboratory applies.

BOUNDARY:
This does not imply certification is weak or arbitrary. It identifies certification as a bounded evidentiary process whose strength depends on the relationship between tests and possible failures.

CITATION TRAIL:
UKGC Testing Strategy.
Specific approved test-house methodologies.
Software testing literature on oracle problems, coverage, property testing, and model-based testing.
Science and technology studies of standards and certification.

TEST:
For one certified game, obtain the testing scope and construct a matrix:

FAILURE MODE × TEST PROCEDURE × OBSERVABILITY.

Identify failures for which no listed procedure supplies a direct observation.

PLATFORM:
[[Tests construct what can be known about programs]]

LINKS:
[[RNG-001]]
[[Certification as epistemic architecture]]
[[Passing is indexed to a test]]

BIBTEX:
@misc{ukgc_testing_procedure_2024,
  author       = {{UK Gambling Commission}},
  title        = {Testing Strategy for Compliance with Remote Gambling and Software Technical Standards: Procedure for Testing},
  year         = {2024},
  url          = {https://www.gamblingcommission.gov.uk/strategy/testing-strategy-for-compliance-with-remote-gambling-and-software-technical/3-procedure-for-testing},
  note         = {Updated 13 September 2024; accessed 2026-08-17}
}