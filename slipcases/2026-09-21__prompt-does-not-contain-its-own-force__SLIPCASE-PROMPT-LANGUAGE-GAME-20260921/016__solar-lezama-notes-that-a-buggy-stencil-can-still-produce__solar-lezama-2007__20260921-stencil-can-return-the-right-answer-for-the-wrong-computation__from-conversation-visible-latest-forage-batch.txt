ZETTEL

ID:
20260921-stencil-can-return-the-right-answer-for-the-wrong-computation

TITLE:
Solar-Lezama Notes That a Buggy Stencil Can Still Produce the Correct Answer—Only More Slowly

SOURCE:
Armando Solar-Lezama et al. — “Sketching Stencils” — PLDI 2007 — §3. ([people.csail.mit.edu](https://people.csail.mit.edu/asolar/papers/Solar-LezamaATBSS07.pdf?utm_source=chatgpt.com))

PASSAGE:
[PARAPHRASE] The paper explains that low-level stencil bugs can be subtle. In iterative algorithms, a buggy stencil can still eventually produce the correct answer while requiring much longer to converge. The authors motivate sketching partly because final-output inspection can therefore fail to reveal an implementation defect. ([people.csail.mit.edu](https://people.csail.mit.edu/asolar/papers/Solar-LezamaATBSS07.pdf?utm_source=chatgpt.com))

RESEARCH OBJECT:
A candidate satisfying a terminal outcome criterion while violating an important process criterion.

LOCAL MOVE:
The source separates “eventually returns the right answer” from “implements the intended computation correctly and efficiently.”

SOURCE TERMS:
buggy stencil
correct answer
longer to converge
low-level expressions
subtle effects
specification

WHAT BECAME STRANGE:
A verifier can certify the wrong thing if it observes only the final state. More verification does not necessarily improve correspondence; the tested variable must be the one that actually matters.

QUESTION:
What properties of a generated artifact or agent trajectory remain invisible to a verifier that scores only terminal success?

DEEPER QUESTION:
Should prompt tests specify not only acceptable outcomes but acceptable paths, resource costs, dependencies, provenance, and state transitions?

MECHANISM:
candidate implementation generated
→ candidate contains low-level bug
→ iterative process still converges
→ terminal output matches expected result
→ weak verifier accepts
→ hidden process defect survives.

FORMAL SHIFT:
<TEST FINAL OUTPUT>
→ <TEST OUTPUT + TRAJECTORY / COST / INVARIANTS>
→ [VERIFY PROCESS]
→ <STRONGER CORRESPONDENCE>

SOURCE FORMALISM:
The paper uses a full stencil specification plus sketches with holes whose low-level loop bounds are synthesized; it explicitly notes that buggy iterative stencils may still return correct answers. ([people.csail.mit.edu](https://people.csail.mit.edu/asolar/papers/Solar-LezamaATBSS07.pdf?utm_source=chatgpt.com))

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
Verifier(result) is weaker than
Verifier(result, trajectory, invariants, cost).

TENSION:
Overconstraining the path can reject valid novel solutions and defeat the purpose of leaving implementation detail open.

MISSING:
A principled distinction between process properties that express genuine intent and process properties that should remain open to discovery.

BOUNDARY:
Stencil programs have precise numerical semantics and measurable execution cost. Artistic or semantic generation often lacks equally objective process invariants.

CITATION TRAIL:
[[20260921-sketching-stencils-specifies-structure-and-synthesizes-loop-bounds]]
→ buggy-stencil convergence case
→ executable verification itself becomes an object requiring design.

TEST:
For the same WAG construction, create one verifier checking only final geometry and another checking geometry plus illegal intermediate intersections, part count, attachment validity, and construction sequence. Search for outputs that pass one but fail the other.

PLATFORM:
[[possibility-space-of-prompting]]

LINKS:
[[20260921-sketching-stencils-specifies-structure-and-synthesizes-loop-bounds]]
[[weak-verifier]]
[[process-specification]]
[[Sketch]]

BIBTEX:
@inproceedings{solarlezama2007sketching,
  author = {Solar-Lezama, Armando and Arnold, Gilad and Tancau, Liviu and Bodik, Rastislav and Saraswat, Vijay and Seshia, Sanjit},
  title = {Sketching Stencils},
  booktitle = {Proceedings of the ACM SIGPLAN Conference on Programming Language Design and Implementation},
  year = {2007}
}
