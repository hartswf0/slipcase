ZETTEL

ID:
PROGRAMROLE-003

TITLE:
Turing’s universal machine makes the rules portable by putting them inside the machine as exchangeable description.

SOURCE:
Alan M. Turing — “On Computable Numbers, with an Application to the Entscheidungsproblem” — 1936 — §§5–6, especially pp. 240–242.

PASSAGE:
[PARAPHRASE]
Turing first converts a machine table into a finite standard description. In explaining universality, he imagines a machine whose operation depends on having the rules of another machine written within it and whose steps consult those rules. He then observes that treating those internal rules as removable and exchangeable yields something very close to the universal machine.

RESEARCH OBJECT:
The foundational program-like object is not merely INPUT.

It is an EXCHANGEABLE REPRESENTATION OF RULES whose presence changes how a fixed machine proceeds.

LOCAL MOVE:
The parent’s COUNTERFACTUAL CONTROL idea gains a historically sharper form:

PORTABLE RULE SUBSTITUTION.

SOURCE TERMS:
standard description
rules of operation
universal machine
complete configuration
exchange
description number

WHAT BECAME STRANGE:
Turing’s key move is not simply:

DATA CHANGES OUTPUT.

It is:

DATA REPRESENTS THE RULE SYSTEM THE RECEIVER CONSULTS WHILE GENERATING ITS OWN TRANSITIONS.

QUESTION:
Does representing an exchangeable transition policy distinguish program-like inputs from ordinary data inputs?

DEEPER QUESTION:
Can prompts, configurations, legal rules, and cultural prescriptions also satisfy this stronger criterion by altering how a receiver interprets subsequent inputs?

MECHANISM:
machine M
→ standard description SD(M)

fixed universal machine U
+
SD(M)
→ U consults represented rules
→ reproduces M’s sequence.

FORMAL SHIFT:
<RULES EXTERNAL TO MACHINE>
→ <FINITE RULE DESCRIPTION>
→ [INTERNALIZE AS EXCHANGEABLE DATA]
→ <FIXED MACHINE BEHAVES AS DESCRIBED MACHINE>

SOURCE FORMALISM:
Turing defines a standard description of a machine and a universal machine supplied with such a description.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

A stronger program-role candidate:

    PolicyInput(p,I)

iff p is interpreted as specifying or selecting a transition policy used by I over subsequent configurations.

Then:

    I[p](x)

rather than merely:

    I(p,x).

TENSION:
A sufficiently sophisticated configuration file can also select transition policy.

The criterion may identify PROGRAM-LIKE CONTROL rather than programs uniquely.

MISSING:
A formal distinction between:
RULE-SELECTING INPUT
and
ORDINARY OPERAND INPUT.

BOUNDARY:
Turing provides a powerful mechanism for program relativity but not a modern syntactic definition of PROGRAM.

CITATION TRAIL:
[[UPTAKE-003]]
→ counterfactual control
→ Turing universal machine
→ exchangeable represented rules
→ program-like input as transition-policy parameter.

TEST:
Construct three inputs to one interpreter:

A. numerical operand
B. configuration option
C. encoded transition table.

Hold the interpreter fixed.

Measure whether each changes:
one result,
a bounded parameter,
or the transition policy applied to an open class of future inputs.

PLATFORM:
[[description-becomes-operation]]

LINKS:
[[UPTAKE-003]]
[[turing-universal-machine]]
[[exchangeable-rules]]
[[program-role]]

BIBTEX:
@article{Turing1936,
  author  = {Turing, A. M.},
  title   = {On Computable Numbers, with an Application to the Entscheidungsproblem},
  journal = {Proceedings of the London Mathematical Society},
  series  = {2},
  volume  = {42},
  pages   = {230--265},
  year    = {1936},
  doi     = {10.1112/plms/s2-42.1.230}
}
