ZETTEL

ID:
Z-OPLANG-MELT02-01

TITLE:
A regenerable text may still fail to carry the theory required to modify it.

SOURCE:
Peter Naur — “Programming as Theory Building” — 1985 — especially pp. 229–232 in the available reprint.

SOURCE URL:
https://pages.cs.wisc.edu/~remzi/Naur.pdf

PASSAGE:
[QUOTE]
“the program text and its documentation has proved insufficient as a carrier of some of the most important design ideas.”

[PARAPHRASE]
Naur argues that the theory built by programmers has primacy over program text and documentation. Someone who possesses the theory can explain how parts of the program map onto affairs of the world, justify why they are present, and respond constructively to demands for modification.

RESEARCH OBJECT:
<MODIFICATION-COMPETENCE> as a stronger test of whether a compressed representation preserves the theory of a work.

Our earlier proposal asked:

What is the smallest program from which the dissertation can be regenerated?

Naur makes that test look dangerously weak.

A representation might regenerate a recognizable artifact while failing to preserve the understanding required to alter that artifact coherently when the world changes.

LOCAL MOVE:
Naur separates the written products of programming from the knowledge possessed by programmers who understand what those products are for.

SOURCE TERMS:
“theory building”
“program text”
“documentation”
“knowledge”
“world”
“modification”
“explain”
“justification”
“similarity”

WHAT BECAME STRANGE:
Regeneration no longer looks like proof of theoretical preservation.

A prompt might repeatedly regenerate:

<the same argument>
<the same application>
<the same architecture>

because its environment supplies missing priors.

But if an unforeseen requirement arrives, the compressed object may contain no basis for deciding what should bend and what must remain invariant.

The important test is therefore not:

CAN IT REPRODUCE?

but:

CAN IT CHANGE FOR THE RIGHT REASONS?

QUESTION:
What must a compressed prompt preserve so that a future interpreter can make a previously unforeseen modification without destroying the work’s intellectual commitments?

DEEPER QUESTION:
Could the “theory of the program” be operationally identified not by reproducibility but by counterfactual modification competence?

MECHANISM:
<artifact>
can be reproduced from
<compressed representation>.

But:

<new world condition>
[requires]
<judgment of similarity and relevance>.

That judgment depends upon a theory connecting:

<program structures>
↔
<affairs of the world>.

If the representation does not preserve enough of that mapping, regeneration succeeds while modification fails.

FORMAL SHIFT:
<GENERATIVE REPRESENTATION>
→ [REGENERATE]
→ <RECOGNIZABLE ARTIFACT>

becomes:

<GENERATIVE REPRESENTATION>
+ <UNFORESEEN CHANGE>
→ [INTERPRET WHY STRUCTURES EXIST]
→ [MODIFY]
→ <COHERENT DESCENDANT>

SOURCE FORMALISM:
Naur does not supply mathematical syntax.

He distinguishes program text/documentation from the theory possessed by programmers and uses competence under explanation and modification as evidence of possessing that theory.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

R(P) = fidelity of artifact regeneration from representation P.

M(P, ΔW) = coherence of modification under previously unspecified world change ΔW.

Then:

high R(P)

does not imply

high M(P, ΔW).

A representation preserving the “program theory” should survive both.

TENSION:
A sufficiently rich generative model may supply background theory that is absent from the prompt itself.

If so, successful modification may demonstrate the theory of:

<prompt + interpreter + context>

rather than the theory encoded by <prompt>.

This makes it difficult to locate the intellectual structure in the compressed text alone.

MISSING:
A criterion for “right reasons.”

A modification may look coherent while relying on different reasoning from the original researcher.

Also missing is a way to distinguish:
- preserved theory,
- reconstructed theory,
- substituted theory,
- lucky behavioral equivalence.

BOUNDARY:
Naur does not discuss LLMs or prompting.

His account does not prove that prompt-based regeneration loses theory.

It supplies a counterexample to treating successful textual reconstruction as sufficient evidence that the underlying theory has been transmitted.

CITATION TRAIL:
Gilbert Ryle — knowing how / intelligent performance.
Thomas Kuhn — theory possession and exemplary application.
Peter Naur — modification and programmer knowledge.
Program comprehension and architectural decision records.
Counterfactual evaluation of generative specifications.

TEST:
Create a compact generative representation capable of reconstructing one substantial argument or program.

Give it to a fresh interpreter.

Test three tasks:

A. regenerate the original;
B. explain why each major structure exists;
C. respond to an unforeseen requirement that conflicts with one local feature but not the governing theory.

Compare whether regeneration fidelity predicts modification coherence.

If A succeeds while C fails, compression has preserved realization without preserving theory.

PLATFORM:
[[Theory of the Program]]

LINKS:
[[Deferred Formalization]]
[[Modification Competence]]
[[The Prompt Is Not the Program]]

BIBTEX:
@article{naur1985programming,
  author = {Naur, Peter},
  title = {Programming as Theory Building},
  journal = {Microprocessing and Microprogramming},
  volume = {15},
  number = {5},
  pages = {253--261},
  year = {1985},
  doi = {10.1016/0165-6074(85)90032-8}
}
