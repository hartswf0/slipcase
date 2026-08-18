ZETTEL

ID:
STAGING-002

TITLE:
A configuration file can become code merely because it changes more slowly than the rest of the input.

SOURCE:
Neil D. Jones, Carsten K. Gomard, and Peter Sestoft — Partial Evaluation and Automatic Program Generation — 1993 — Preface.

PASSAGE:
[PARAPHRASE]
The authors observe that many ordinary programs have interpretive behavior because they are parameterized by relatively stable inputs such as configuration files. When such an input changes slowly, specializing the program with respect to it can profitably generate a new specialized program.

RESEARCH OBJECT:
CONFIGURATION and PROGRAM are not formally separated by causal power.

A configuration can be residualized into the program that interprets it.

LOCAL MOVE:
The parent proposed comparing programs with configuration files to discover what is unique about PROGRAM ROLE.

Partial evaluation supplies a counterexample to any simple categorical separation.

SOURCE TERMS:
configuration files
parameterized
specialization
static input
specialized program
interpretive behaviour

WHAT BECAME STRANGE:
A configuration file may begin as:

DATA READ BY PROGRAM

and end as:

STRUCTURE OF A NEW PROGRAM.

No change in intended behavior is required.

QUESTION:
What criterion could distinguish program from configuration if semantics-preserving transformation can move information between those roles?

DEEPER QUESTION:
Is the distinction only one of staging, mutability frequency, authority, or conventional engineering practice?

MECHANISM:
general program P
+
configuration C
+
runtime input x
→ result.

Specialization:

P + C
→ P_C

then:

P_C + x
→ same result.

FORMAL SHIFT:
<CONFIGURATION AS INPUT>
→ [PARTIAL EVALUATION]
→ <CONFIGURATION RESIDUALIZED AS CODE>

SOURCE FORMALISM:
The partial-evaluation equation applies to any suitable static input; the authors explicitly name configuration files as a practical example.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Before:

    Run(P,C,x)

After:

    P_C = Specialize(P,C)

    Run(P_C,x)

with:

    Run(P,C,x) ≃ Run(P_C,x).

TENSION:
Operational systems still often distinguish configuration and code for security, provenance, update frequency, tooling, and human expectations.

MISSING:
Whether PROGRAM should be defined semantically at all or partly by an engineering governance regime.

BOUNDARY:
Semantic influence over future behavior does not uniquely identify programs because configuration data can have that influence and can even be transformed into code.

CITATION TRAIL:
[[UPTAKE-003]]
→ TEST includes configuration files
→ partial evaluation of slowly varying configuration
→ configuration/program boundary becomes staging-relative
→ governance may be the missing discriminator.

TEST:
Take one real application with a configuration file.

A. execute normally.
B. specialize the application against the configuration and remove the file.
C. change the residual program so it behaves as though the configuration changed.

Ask which artifact is now “the configuration.”

PLATFORM:
[[description-becomes-operation]]

LINKS:
[[UPTAKE-003]]
[[configuration-as-code]]
[[staging]]
[[program-role]]

BIBTEX:
@book{JonesGomardSestoft1993,
  author    = {Jones, Neil D. and Gomard, Carsten K. and Sestoft, Peter},
  title     = {Partial Evaluation and Automatic Program Generation},
  publisher = {Prentice Hall},
  year      = {1993}
}
