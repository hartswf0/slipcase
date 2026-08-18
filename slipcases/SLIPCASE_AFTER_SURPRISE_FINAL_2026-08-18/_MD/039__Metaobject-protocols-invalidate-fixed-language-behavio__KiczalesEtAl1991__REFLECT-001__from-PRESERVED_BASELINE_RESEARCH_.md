ZETTEL

ID:
REFLECT-001

TITLE:
Metaobject protocols invalidate fixed language behavior as a necessary property of programming systems.

SOURCE:
Gregor Kiczales, Jim des Rivières, and Daniel G. Bobrow — The Art of the Metaobject Protocol — 1991 — Introduction, pp. 1–7.

PASSAGE:
[PARAPHRASE]
Kiczales and collaborators contrast traditional languages whose behavior is treated as fixed with metaobject-protocol languages in which users can incrementally modify language behavior and implementation. They describe the implementation itself as a program and expose selected language-design decisions through protocols over metaobjects.

RESEARCH OBJECT:
The programming system can make its own semantic/implementation machinery an object of programming.

LOCAL MOVE:
The source converts:

LANGUAGE BEHAVIOR AS FIXED BACKGROUND

into:

LANGUAGE BEHAVIOR AS USER-ADJUSTABLE STRUCTURE.

SOURCE TERMS:
metaobject protocol
language behavior
implementation
reflection
protocol
metaobject
incremental adjustment

WHAT BECAME STRANGE:
The proposed cultural/computational boundary based on fixed semantics fails inside mainstream programming-language research.

The language user can participate in changing the rules governing program interpretation.

QUESTION:
If language behavior itself can be modified, what must remain fixed for execution to remain well-defined?

DEEPER QUESTION:
Is the stronger computational invariant not FIXED SEMANTICS but a FIXED META-PROTOCOL specifying how semantic variation may occur?

MECHANISM:
base language implementation
→ reify selected implementation/behavioral decisions as metaobjects
→ expose operations through metaobject protocol
→ user specializes protocol
→ altered language behavior / implementation
→ base-level programs run under modified behavior.

FORMAL SHIFT:
<FIXED I,T>
→ <METAOBJECT REPRESENTATION OF I,T COMPONENTS>
→ [PROGRAMMATIC MODIFICATION]
→ <I',T'>

SOURCE FORMALISM:
The book describes metaobject protocols as interfaces to a language enabling users to modify language behavior and implementation.

It models a region of possible language behaviors around a default language, with protocol methods controlling movement within that region.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Parent model:

    <F,I,S,T> fixed during interpretation.

MOP model:

    M = meta-level state describing selected components of I/T

    MetaStep(M, program_meta)
        → M'

    Run(base_program | M')
        → behavior'.

TENSION:
The modification is not unconstrained.

The metaobject protocol itself specifies which aspects of language behavior are exposed and what forms of intervention are legal.

MISSING:
A precise distinction between:

changing parameters of an interpreter,
changing implementation strategy,
changing observable semantics,
and changing the meta-protocol that defines allowable changes.

BOUNDARY:
Reflection defeats FIXED LANGUAGE BEHAVIOR as an absolute computational boundary.

It does not prove that a programming system can change every component of its own semantic ontology without constraint.

CITATION TRAIL:
[[MINIMUM-026]]
→ reflection
→ Kiczales / des Rivières / Bobrow
→ metaobject protocols
→ user-modifiable language behavior
→ search for fixed meta-rules.

TEST:
Select one semantic operation exposed by a CLOS metaobject protocol.

Run identical base-level source under:

A. default metaobject behavior
B. specialized metaobject behavior.

Identify exactly which coordinate of:

    <F,I,S,T>

changed and which meta-level constraints remained fixed.

PLATFORM:
[[description-becomes-operation]]

LINKS:
[[MINIMUM-026]]
[[metaobject-protocol]]
[[semantic-self-modification]]
[[open-language]]

BIBTEX:
@book{KiczalesEtAl1991,
  author    = {Kiczales, Gregor and des Rivi{\`e}res, Jim and Bobrow, Daniel G.},
  title     = {The Art of the Metaobject Protocol},
  publisher = {MIT Press},
  address   = {Cambridge, MA},
  year      = {1991}
}
