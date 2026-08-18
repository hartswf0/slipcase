ZETTEL

ID:
Z-OPLANG-RUN01-02

TITLE:
A prompt’s operative semantics may be distributed across the expression and a learned interpreter.

SOURCE:
Watson Hartsoe — BETWEEN CODE AND POETRY: Committee notes toward a prompt-forward dissertation — 2026 — §1, “The central question.” fileciteturn1file0L23-L59

SOURCE URL:
sandbox:/mnt/data/Pasted%20markdown(20260817-170730).md

PASSAGE:
[PARAPHRASE]
The manuscript proposes that a prompt’s “native language” may not be English or Python but an interaction among natural language, architecture, training distributions, context, examples, system constraints, tools, and iterative feedback.

RESEARCH OBJECT:
The distinction between <specified semantics> and <learned semantics>.

The important question may not be whether prompts are ambiguous while code is precise, but how much of an expression’s interpretation procedure is explicitly specified by a language and how much is supplied by an interpreter learned from prior data.

LOCAL MOVE:
The source destabilizes the search for a standalone prompt grammar by relocating meaning into a larger human-model-context configuration.

SOURCE TERMS:
“native language”
“semantics”
“model architecture”
“training distributions”
“context”
“examples”
“system constraints”
“tool affordances”
“iterative feedback”

WHAT BECAME STRANGE:
The ordinary assumption that a language contains the rules required to interpret its expressions.

In a formal language, a large portion of legitimate interpretation is deliberately stabilized.

In prompting, the visible expression may leave enormous interpretive work to a model whose competence was learned elsewhere.

The expression can therefore operate before its semantics have been exhaustively formalized.

QUESTION:
How much of a prompt’s semantics resides in the expression, and how much resides in the learned interpreter capable of supplying unstated structure?

DEEPER QUESTION:
Could programming languages be compared not by “formal versus natural” but by where they place the burden of semantic completion?

MECHANISM:
<expression>
[supplies] <partial constraints>.

<learned interpreter>
[combines] {
  <expression>,
  <context>,
  <training-derived priors>,
  <system constraints>,
  <examples>
}.

<interpretation>
[produces] <candidate consequence>.

Meaning is therefore operationally distributed rather than recoverable solely from surface syntax.

FORMAL SHIFT:
<SURFACE EXPRESSION>
→ <EXPRESSION + INTERPRETER STATE + CONTEXT>
→ [SEMANTIC COMPLETION]
→ <OPERATIVE INTERPRETATION>

SOURCE FORMALISM:
NONE.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Interpretation may be represented as:

I = f(E, C, M, S, X)

where:
E = expression,
C = context,
M = learned model,
S = system constraints,
X = examples/tool affordances.

The analytical question becomes how strongly I is determined by E relative to the other variables.

TENSION:
Conventional programs are also context-dependent.

Variable bindings, libraries, operating systems, runtime state, permissions, and environment variables can radically affect execution.

Therefore:

<CODE> = context-free
<PROMPT> = contextual

is false.

The surviving difference may concern the degree to which interpretation itself is delegated to learned rather than formally enumerated machinery.

MISSING:
A workable measure of semantic burden:
What percentage or kind of behavior must the expression specify?
What is inferred?
What is supplied by system instructions?
What is inherited from training?

Also missing is a clear comparison with declarative, constraint-based, and probabilistic programming.

BOUNDARY:
The source does not establish that learned semantics are exclusive to prompting or that conventional programming eliminates interpretation.

It opens a comparative axis concerning where semantic determination resides.

CITATION TRAIL:
Programming-language semantics.
Probabilistic programming.
Natural-language pragmatics.
Neural semantic parsing.
Learned program synthesis.
Constraint and declarative programming.

TEST:
Create equivalent tasks in:
A. deterministic code,
B. declarative language,
C. structured schema,
D. natural-language prompt.

Progressively remove explicit instructions while holding intended behavior fixed.

Measure how much missing structure each interpreter can reconstruct and what kinds of failure emerge.

PLATFORM:
[[Operative Language]]

LINKS:
[[Learned Semantics]]
[[Semantic Burden]]
[[Specification Completion]]

BIBTEX:
@unpublished{hartsoe2026betweencodepoetry,
  author = {Hartsoe, Watson},
  title = {Between Code and Poetry: Committee Notes Toward a Prompt-Forward Dissertation},
  year = {2026},
  note = {Unpublished manuscript supplied by the author}
}
