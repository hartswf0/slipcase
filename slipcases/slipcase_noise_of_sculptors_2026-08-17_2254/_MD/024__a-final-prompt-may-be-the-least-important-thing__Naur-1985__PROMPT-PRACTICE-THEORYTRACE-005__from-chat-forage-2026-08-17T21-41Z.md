ZETTEL

ID:
PROMPT-PRACTICE-THEORYTRACE-005

TITLE:
A FINAL PROMPT MAY BE THE LEAST IMPORTANT THING TO SAVE.

SOURCE:
Peter Naur — “Programming as Theory Building” — Microprocessing and Microprogramming 15(5), 1985, pp. 253–261.

SOURCE URL:
https://doi.org/10.1016/0165-6074(85)90032-8

ACCESSIBLE SCAN:
https://pages.cs.wisc.edu/~remzi/Naur.pdf

PASSAGE:
[QUOTE]
Programming should be regarded as an activity through which programmers achieve “a certain kind of insight, a theory, of the matters at hand.”

RESEARCH OBJECT:
THEORY TRACE.

Prompt repositories usually preserve textual artifacts.

Naur suggests that textual preservation can miss the knowledge required to modify the artifact intelligently.

LOCAL MOVE:
[[SON-IEC-005]] located prompt expertise partly in the search procedure rather than the final prompt.

[[SON-IEC-005-B]] made ancestry itself valuable.

Naur radicalizes both:

the important transferable object may not be the final textual artifact at all.

It may be the THEORY that made its sequence of decisions intelligible.

SOURCE TERMS:
theory building
program text
documentation
programmers' knowledge
modification
adaptation
insight
theory

WHAT BECAME STRANGE:
A polished prompt can be perfectly copied and still be effectively orphaned.

Another operator may know:

WHAT WORDS TO RUN

without knowing:

why each constraint exists
which failures produced it
which clauses are expendable
which clauses encode invariants
what model behavior it compensates for
what changed when it was added
what future modification would violate the theory.

The final prompt can therefore be syntactically alive and theoretically dead.

QUESTION:
What must be preserved alongside a prompt so another practitioner can modify it without destroying the theory that produced it?

DEEPER QUESTION:
Can a correction genealogy externalize enough of a practitioner's theory to make prompt expertise transferable?

MECHANISM:
Naur distinguishes possession of program text/documentation from possession of the understanding required for continued adaptation.

In the prompt setting, a genealogy can preserve:

PROMPT₀
→ OUTPUT₀
→ FAILURE₀
→ CORRECTION₀

→ PROMPT₁
→ OUTPUT₁
→ FAILURE₁
→ CORRECTION₁

...

The sequence records not merely versions but WHY each change entered the artifact.

FORMAL SHIFT:
FROM:

PROMPT VERSIONING:

P₀ → P₁ → P₂ → P₃

TO:

THEORY TRACE:

(P₀,O₀,J₀)
→ Δ₁ because R₁
→ (P₁,O₁,J₁)
→ Δ₂ because R₂
→ ...

where:

O = output
J = judgment
R = reason/counterexample
Δ = revision.

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

PROMPT ARTIFACT:

A = final text Pₙ.

THEORY TRACE:

T =
{
ancestry,
failures,
counterexamples,
accepted properties,
rejected hypotheses,
revision rationales,
boundary cases
}.

TRANSFERABILITY should be measured by:

ADAPT(new_requirement | Pₙ)

versus

ADAPT(new_requirement | Pₙ + T).

TENSION:
No textual archive can guarantee transmission of the full human theory Naur describes.

A theory trace might merely create more documentation.

But it can preserve the evidential history that ordinary prompt repositories routinely discard.

MISSING:
An empirical test of whether correction genealogies actually improve:

handoff
adaptation
debugging
model migration
prompt simplification.

A distinction between useful theory trace and exhaustive interaction logging.

BOUNDARY:
Naur's theory is about human programmers and conventional software development.

Applying it to prompting is an analogy until transfer experiments demonstrate that prompt modification depends on comparable tacit or historical understanding.

CITATION TRAIL:
[[SON-IEC-005]]
→ expertise resides in iterative policy

[[SON-IEC-005-B]]
→ ancestry can contain creative value

→ Naur
→ program text does not carry the whole theory
→ final prompt becomes an insufficient archival object
→ preserve REASONS FOR REVISION, not merely revisions

TEST:
Take one mature prompt with a long development history.

Prepare three handoff packages:

A. FINAL PROMPT ONLY

B. FINAL PROMPT + DOCUMENTED RULES

C. FINAL PROMPT + CORRECTION GENEALOGY

Give each group the same novel modification requirement.

Measure:

successful adaptation
time
number of regressions
ability to explain why constraints exist
ability to remove obsolete constraints.

If C significantly outperforms A and B, the genealogy functions as a partial THEORY TRACE.

PLATFORM:
Microprocessing and Microprogramming

LINKS:
[[SON-IEC-005]]
[[SON-IEC-005-B]]

BIBTEX:
@article{naur1985programming,
  author = {Peter Naur},
  title = {Programming as Theory Building},
  journal = {Microprocessing and Microprogramming},
  volume = {15},
  number = {5},
  pages = {253--261},
  year = {1985},
  doi = {10.1016/0165-6074(85)90032-8},
  url = {https://doi.org/10.1016/0165-6074(85)90032-8}
}
