ZETTEL

ID:
WORKWORDS-PROMPT-007

TITLE:
Prompt language becomes literally hybrid when prose, control flow, and constraints share one executable object.

SOURCE:
Luca Beurer-Kellner, Marc Fischer, and Martin Vechev — “Prompting Is Programming: A Query Language for Large Language Models” — PLDI 2023 — DOI: 10.1145/3591300

PASSAGE:
[PARAPHRASE] Beurer-Kellner, Fischer, and Vechev introduce Language Model Programming and LMQL, which combines textual prompting with scripting, control flow, and output constraints. Their runtime uses those constraints and program structure to produce an inference procedure rather than treating the prompt as an isolated string.

RESEARCH OBJECT:
THE “BETWEEN CODE AND NATURAL LANGUAGE” PROBLEM CAN BE MADE ARCHITECTURAL RATHER THAN METAPHORICAL.

LMQL does not resolve whether prose itself is code.

It builds an artifact in which statistical natural language and conventional programming constructs coexist.

LOCAL MOVE:
Do not ask only:

IS A PROMPT CODE?

Ask:

WHAT HAPPENS WHEN TWO DIFFERENT SEMANTIC REGIMES SHARE ONE PROGRAM?

SOURCE TERMS:
Language Model Programming
LMQL
constraints
control flow
text prompting
scripting
inference procedure

WHAT BECAME STRANGE:
The natural-language section can remain ambiguous and probabilistic while adjacent program structure is formal enough to branch, constrain, and reject.

One executable artifact can therefore contain zones with radically different commitments about meaning.

QUESTION:
Where exactly does formal semantics end and probabilistic interpretation begin inside a hybrid language-model program?

DEEPER QUESTION:
Can such a mixed artifact be understood using ordinary programming-language semantics, or does it require semantics for operations whose meanings are distributions rather than determinate transitions?

MECHANISM:
natural-language prompt fragments
+
scripting/control flow
+
constraints

→ LMQL program

→ runtime constructs efficient constrained inference

→ language model generations are filtered/guided according to program structure.

FORMAL SHIFT:
FROM:

NATURAL LANGUAGE versus PROGRAMMING LANGUAGE

TO:

FORMAL CONTROL STRUCTURE
⊗
PROBABILISTIC LANGUAGE INTERPRETATION.

SOURCE FORMALISM:
LMQL combines text prompting and scripting and permits constraints over language-model outputs. The implementation uses these constraints and control flow to construct an inference procedure.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Program state contains two kinds of transition:

deterministic/formal:

s --op--> s'

and model-mediated:

s --LM(text)--> Distribution(s').

A hybrid program alternates between them.

The semantic problem is therefore not simply nondeterminism.

It is interpretation entering the transition relation.

TENSION:
LMQL can make prompting look more like programming by surrounding it with formal machinery.

But that may leave the central anomaly untouched:

the crucial natural-language operation remains interpreted by a learned model rather than defined by a formal semantics.

Formal scaffolding does not formalize the words inside it.

MISSING:
A semantics that explicitly marks which transitions are:

defined,
sampled,
interpreted,
constrained,
tested,
or delegated.

BOUNDARY:
LMQL intentionally makes prompting more programmable. It does not prove that ordinary chat prompts already constitute a programming language.

CITATION TRAIL:
[[DEFAULT-IMAGES-CHI26-B-1]]
→ prompt passes through hidden machinery
→ LMQL makes surrounding machinery explicit
→ hybrid formal/probabilistic execution
→ next edge: probabilistic programming, nondeterministic semantics, effect systems, and contracts.

TEST:
Take a single LMQL program.

Draw every state transition.

Mark each edge:

FORMAL
MODEL-INTERPRETED
STOCHASTIC
CONSTRAINT-CHECKED.

Now perturb only the natural-language portions.

Measure which supposedly formal program properties remain invariant.

PLATFORM:
LMQL; Language Model Programming.

LINKS:
[[DEFAULT-IMAGES-CHI26-B-1]]

BIBTEX:
@inproceedings{BeurerKellner2023LMQL,
  author = {Beurer-Kellner, Luca and Fischer, Marc and Vechev, Martin},
  title = {Prompting Is Programming: A Query Language for Large Language Models},
  booktitle = {PLDI 2023},
  year = {2023},
  doi = {10.1145/3591300}
}
