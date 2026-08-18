ZETTEL

ID:
Z-OPLANG-RUN01-10

TITLE:
A failed generation can function as negative specification by eliciting criteria that did not yet exist propositionally.

SOURCE:
Watson Hartsoe — The Warm Seed — 2026 — fragments 37–43, 82–86. fileciteturn0file0L478-L544 fileciteturn0file0L938-L984

SOURCE URL:
sandbox:/mnt/data/Pasted%20markdown(20260817-170018).md

PASSAGE:
[PARAPHRASE]
The text proposes that prompt failure can teach the writer what they were trying to ask and compares tacit aesthetic judgment to a musician stopping rehearsal with “No” despite lacking an explicit metric.

RESEARCH OBJECT:
<negative specification>: specification produced by recognizing and rejecting a realization before the relevant criterion can be positively articulated.

LOCAL MOVE:
The source refuses the assumption that inability to state a criterion means no criterion exists. It places tacit judgment inside the prompting process.

SOURCE TERMS:
“failed prompt”
“learned something”
“criterion”
“No”
“taste”
“leave unwritten”
“Again”

WHAT BECAME STRANGE:
Ordinary specification theory tends to imagine evaluation against pre-existing requirements.

But sometimes:

<rejection>
comes before
<explicit requirement>.

The user knows “not this” before knowing how to state what “this” violated.

Generation becomes a technique for eliciting otherwise tacit discriminations.

QUESTION:
Can rejection function as specification when the evaluator cannot yet positively state the violated criterion?

DEEPER QUESTION:
How much creative knowledge exists first as discriminatory capacity—an ability to recognize wrongness—rather than as explicit propositional instruction?

MECHANISM:
<underspecified intention>
[produces] <candidate>.

<human embodied/tacit judgment>
[detects] <violation>.

<rejection>
[marks] <boundary>.

Repeated boundaries
[carve] <viable region>.

Eventually some of those boundaries may become explicit constraints.

FORMAL SHIFT:
<TACIT CRITERION>
→ <FAILED REALIZATION>
→ [RECOGNIZE VIOLATION]
→ <NEGATIVE CONSTRAINT>
→ <REFINED POSSIBILITY SPACE>

SOURCE FORMALISM:
NONE.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let P be the current possibility space.

A rejected candidate r supplies evidence:

r ∉ A

where A is the unknown acceptable region.

Repeated rejections produce:

P_(t+1) = P_t \ N(r_t)

where N(r_t) is the region inferred to share the objectionable property.

The process approximates A without requiring a complete positive description of A.

TENSION:
A bare rejection does not explain which property caused failure.

The model may infer the wrong boundary.

Users can also rationalize judgments after the fact.

Negative specification therefore requires careful distinction between:
- discrimination,
- explanation,
- inferred constraint.

MISSING:
The mechanism translating “No” into the next viable variation.

Who infers what should change?
The human?
The model?
The interaction between them?

Also missing is a theory of when tacit judgment is reliable.

BOUNDARY:
Failure is not automatically informative.

Some failures reveal nothing except randomness, poor implementation, or evaluator inconsistency.

Negative specification applies only when rejection reliably narrows a meaningful possibility space.

CITATION TRAIL:
Michael Polanyi — tacit knowledge.
Donald Schön — reflection-in-action.
Aesthetic judgment.
Preference learning.
Active learning from negative examples.
Interactive evolutionary computation.

TEST:
Ask participants to produce an artifact they claim they “know when they see” but cannot initially specify.

After every rejection:
1. require only yes/no,
2. then ask for explanation,
3. compare model behavior under both conditions.

Determine whether iterative negative feedback converges even when explicit criteria remain sparse.

PLATFORM:
[[Deferred Formalization]]

LINKS:
[[Negative Specification]]
[[Tacit Criterion]]
[[Failure Becomes Specification]]

BIBTEX:
@unpublished{hartsoe2026warmseed,
  author = {Hartsoe, Watson},
  title = {The Warm Seed},
  year = {2026},
  note = {Unpublished manuscript supplied by the author}
}
