ZETTEL

ID:
Z-OPLANG-MELT02-05

TITLE:
Deferred formalization predates LLMs; the deeper change may be the breadth of what can remain unspecified.

SOURCE:
Vu Le, Daniel Perelman, Oleksandr Polozov, Mohammad Raza, Abhishek Udupa, and Sumit Gulwani — “Interactive Program Synthesis” — 2017.

SOURCE URL:
https://arxiv.org/abs/1703.03539

PASSAGE:
[PARAPHRASE]
The authors explicitly study program synthesis from incomplete specifications and formalize interactive refinement through incremental algorithms, step-based problem formulation, and feedback-based intent refinement.

RESEARCH OBJECT:
<DEFERRED FORMALIZATION> is not by itself a historical novelty of LLM programming.

Interactive synthesis already begins computation from incomplete specifications and uses subsequent interaction to refine intent.

The variable that may have changed is what kinds of unresolved material the interpreter can tolerate.

LOCAL MOVE:
Interactive synthesis turns specification incompleteness from a defect into the premise of an interactive programming method.

SOURCE TERMS:
“incomplete specifications”
“interactive setting”
“feedback-based intent refinement”
“incremental”
“correctness”
“cognitive burden”

WHAT BECAME STRANGE:
Our earlier thesis:

“LLMs allow computation to begin while parts of a specification remain unresolved”

is historically too broad.

That mechanism already exists.

The better question becomes:

WHAT COULD REMAIN UNRESOLVED BEFORE,
AND WHAT CAN REMAIN UNRESOLVED NOW?

Traditional synthesis commonly restricts incompleteness through:
- a defined DSL,
- typed examples,
- invariants,
- bounded search spaces,
- known semantic domains.

LLM interaction admits:
- metaphor,
- style,
- natural-language correction,
- contextual reference,
- examples,
- mixed modalities,
- criteria whose formal vocabulary is unavailable.

QUESTION:
Is the distinctive shift from complete to incomplete specification, or from narrowly typed incompleteness to semantically heterogeneous incompleteness?

DEEPER QUESTION:
What is the maximum kind of unresolvedness an interpreter can absorb before useful synthesis collapses?

MECHANISM:
Earlier interactive synthesis:

<partial formal specification>
→ [search constrained program space]
→ <candidate>
→ [feedback]
→ <refined intent>.

LLM-mediated synthesis:

<heterogeneous partial expression>
→ [learned interpretation across broad priors]
→ <candidate>
→ [natural-language / example / deictic judgment]
→ <revised expression>.

The loop is not new.

The admissible input space may be.

FORMAL SHIFT:
DEFERRED FORMALIZATION
as binary:

<formalized / not formalized>

becomes a spectrum of:

<WHAT KIND OF INFORMATION MAY REMAIN UNFORMALIZED?>

SOURCE FORMALISM:
Le et al. formalize interactive program synthesis around incomplete specifications and three forms of interaction:
- incremental algorithms,
- step-based problem formulation,
- feedback-based intent refinement.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Define an unresolved specification vector:

U = {
  parameter,
  procedure,
  structure,
  semantics,
  aesthetic criterion,
  contextual reference,
  domain ontology,
  evaluation rule
}.

A synthesis regime is characterized by which dimensions of U it can leave unresolved while still producing correctable candidates.

TENSION:
LLMs may merely hide formalization.

Training data and architecture have already encoded massive prior structure.

What feels like “unformalized” to the user may be highly constrained by learned statistical regularities.

MISSING:
A comparative study across synthesis regimes using the same task while varying which specification dimensions remain unresolved.

BOUNDARY:
Interactive program synthesis does not eliminate potentially distinctive properties of LLM-mediated programming.

It eliminates only the broad novelty claim that execution from incomplete specifications began with LLMs.

CITATION TRAIL:
Programming by Example.
Version spaces.
Program synthesis from examples.
Human-in-the-loop synthesis.
Requirements elicitation.
LLM program synthesis.

TEST:
Choose one programmable artifact.

Attempt construction using:
A. complete conventional code,
B. programming-by-example,
C. interactive synthesis with a DSL,
D. LLM natural-language programming.

Systematically withhold:
- exact operations,
- data schema,
- desired style,
- exception rules,
- evaluation criteria.

Measure which kinds of missingness each regime can recover through interaction.

PLATFORM:
[[Deferred Formalization]]

LINKS:
[[Specification Completion]]
[[Negative Specification]]
[[Semantic Bandwidth of Specification]]

BIBTEX:
@misc{le2017interactive,
  author = {Le, Vu and Perelman, Daniel and Polozov, Oleksandr and Raza, Mohammad and Udupa, Abhishek and Gulwani, Sumit},
  title = {Interactive Program Synthesis},
  year = {2017},
  eprint = {1703.03539},
  archivePrefix = {arXiv}
}
