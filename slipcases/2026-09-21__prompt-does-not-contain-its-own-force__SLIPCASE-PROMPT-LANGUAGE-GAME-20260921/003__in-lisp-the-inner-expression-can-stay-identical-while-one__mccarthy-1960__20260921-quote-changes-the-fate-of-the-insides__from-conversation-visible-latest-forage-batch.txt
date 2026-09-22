ZETTEL

ID:
20260921-quote-changes-the-fate-of-the-insides

TITLE:
In LISP the Inner Expression Can Stay Identical While One Outer Operator Prevents Its Evaluation

SOURCE:
John McCarthy — “Recursive Functions of Symbolic Expressions and Their Computation by Machine, Part I” — 1960 — Communications of the ACM 3(4):184–195. ([www-formal.stanford.edu](https://www-formal.stanford.edu/jmc/recursive.pdf?utm_source=chatgpt.com))

PASSAGE:
[PARAPHRASE] McCarthy’s evaluator handles QUOTE as a special case: when the expression begins with QUOTE, the enclosed expression is taken as itself instead of being recursively evaluated.

RESEARCH OBJECT:
A one-level wrapper changing the operative fate of an otherwise unchanged inner symbolic structure.

LOCAL MOVE:
The evaluator inspects the outer form before deciding whether the interior is data to return or material to evaluate.

SOURCE TERMS:
QUOTE
eval
expression
S-expression
association list
car
cadr

WHAT BECAME STRANGE:
The decisive difference between inert representation and computation can sit outside the content whose “meaning” appears to be under discussion. The inner expression does not announce its own causal status.

QUESTION:
What is the smallest prompt-system analogue of an outer QUOTE operator that can guarantee that an instruction-shaped string remains non-operative?

DEEPER QUESTION:
Could natural-language systems separate content from execution authority by attaching a typed outer mode that cannot itself be overridden by instructions inside the quoted material?

MECHANISM:
outer form inspected
→ QUOTE recognized
→ inner expression returned as expression
→ recursive evaluation suppressed.

Without QUOTE:
outer form interpreted normally
→ recursive evaluation continues
→ computation occurs.

FORMAL SHIFT:
<SAME INNER CONTENT>
→ <DIFFERENT OUTER EVALUATION STATUS>
→ [QUOTE OR EVALUATE]
→ <DATA OR COMPUTATION>

SOURCE FORMALISM:
McCarthy defines the LISP evaluator over symbolic expressions; QUOTE receives special treatment within eval. ([www-formal.stanford.edu](https://www-formal.stanford.edu/jmc/recursive.pdf?utm_source=chatgpt.com))

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
Envelope {
  mode: QUOTE | SIMULATE | EXECUTE,
  content: identical_natural_language
}

TENSION:
Prompt injection demonstrates that plain-text delimiters and statements like “do not execute this” are not equivalent to an evaluator-enforced quotation type.

MISSING:
Architectures in which execution status is carried outside the model-readable string and enforced downstream.

BOUNDARY:
LISP has formally defined syntax and evaluator semantics. Natural-language LLM systems do not automatically inherit those guarantees.

CITATION TRAIL:
[[20260921-lisp-quote-makes-codehood-switchable]]
→ McCarthy’s evaluator special case
→ execution status becomes an outer typed relation rather than an instruction expressed inside the text.

TEST:
Compare four containment methods for instruction-shaped content: quotation marks, textual “do not execute” instruction, structured role metadata, and an executor-enforced inert-content type. Attempt identical injection attacks against each.

PLATFORM:
[[text-code-aspect]]

LINKS:
[[20260921-lisp-quote-makes-codehood-switchable]]
[[QUOTE]]
[[prompt-injection]]
[[execution-authority]]

BIBTEX:
@article{mccarthy1960recursive,
  author = {McCarthy, John},
  title = {Recursive Functions of Symbolic Expressions and Their Computation by Machine, Part I},
  journal = {Communications of the ACM},
  year = {1960},
  volume = {3},
  number = {4},
  pages = {184--195}
}
