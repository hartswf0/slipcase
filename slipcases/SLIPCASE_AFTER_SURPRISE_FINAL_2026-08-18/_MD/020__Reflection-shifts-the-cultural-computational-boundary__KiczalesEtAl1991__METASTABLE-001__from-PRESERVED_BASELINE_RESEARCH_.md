ZETTEL

ID:
METASTABLE-001

TITLE:
Reflection shifts the cultural/computational boundary from “can the rules change?” to “what constrains legitimate rule-change?”

SOURCE:
COLLISION — Gregor Kiczales, Jim des Rivières, and Daniel G. Bobrow — The Art of the Metaobject Protocol — 1991; Francisco Durán et al. — “Programming and Symbolic Computation in Maude” — 2019.

PASSAGE:
[PARAPHRASE]
Metaobject protocols deliberately expose a region of language behavior that users may modify, while reflective rewriting logic can represent rule theories as manipulable objects. In both cases, computational semantics can become a target of computation rather than remaining an immutable background.

RESEARCH OBJECT:
META-MUTABILITY survives the destructive test.

But it does not yet erase all distinction.

The new unresolved variable is the RULES OF RULE CHANGE.

LOCAL MOVE:
The parent’s candidate boundary:

SOCIAL:
rules may change

COMPUTATIONAL:
rules fixed

is killed.

A stronger candidate becomes:

HOW IS THE SPACE OF LEGITIMATE META-CHANGE DELIMITED?

SOURCE TERMS:
reflection
metaobject protocol
region of behavior
universal theory
metalevel
language behavior
rule

WHAT BECAME STRANGE:
Kiczales explicitly conceptualizes not one fixed language but a REGION of possible languages reachable through an exposed protocol.

This resembles institutional variation more than the classical fixed-semantics picture did.

QUESTION:
Is computational reflection distinguished from social reflexivity because its meta-changes remain typed and delimited by a pre-existing meta-language?

DEEPER QUESTION:
Can a system generate a genuinely new semantic distinction that was not representable in the ontology of its meta-level before the change?

MECHANISM:
base semantics M₀
→ expose metaobjects / represented rules
→ legal metalevel operations
→ M₁
→ altered base behavior.

But:

legal meta-operations
are themselves constrained by
meta-language / universal interpreter.

FORMAL SHIFT:
<FIXED SEMANTICS>
→ <MUTABLE SEMANTICS>
→ [META-RULES]
→ <CONSTRAINED SPACE OF SEMANTIC VARIATION>

SOURCE FORMALISM:
Kiczales et al. describe a protocol-defined region of language behaviors around a default.

Maude represents rewrite theories inside a universal reflective theory.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

    M_t = current semantics
    Ω   = space of representable semantic modifications.

Then:

    MetaStep : M_t × m ∈ Ω → M_{t+1}

The new question is whether Ω itself is fixed.

A stronger reflexive case would permit:

    Ω_t → Ω_{t+1}.

TENSION:
Reflective towers and self-representation make it difficult to identify a simple final meta-level.

Conversely, social institutions also contain explicit constitutions, amendment procedures, professional jurisdictions, and vocabularies that constrain what counts as legitimate change.

MISSING:
A comparison between:

metaobject protocols
reflective rewrite theories
constitutional amendment
scientific paradigm/category revision
institutional reclassification.

BOUNDARY:
“Rules can change” is no longer a viable absolute separator.

The live boundary candidate is representability and governance of meta-change.

CITATION TRAIL:
[[MINIMUM-026]]
→ self-modifying semantic systems
→ metaobject protocols
→ reflective rewriting logic
→ rules of rule-change.

[[MINIMUM-025]]
→ ontology instability
→ possibility that the transition ontology itself changes
→ meta-ontology as new target.

TEST:
Construct three systems:

A. ordinary fixed interpreter
B. reflective interpreter that can alter predefined semantic hooks
C. system that can introduce a new category of semantic hook not previously representable.

For each identify:

    what may change
    what cannot change
    who authorizes change
    how new distinctions become representable.

PLATFORM:
[[description-becomes-operation]]

LINKS:
[[MINIMUM-025]]
[[MINIMUM-026]]
[[meta-mutability]]
[[rules-of-rule-change]]
[[ontology-change]]
[[reflection]]

BIBTEX:
@book{KiczalesEtAl1991,
  author    = {Kiczales, Gregor and des Rivi{\`e}res, Jim and Bobrow, Daniel G.},
  title     = {The Art of the Metaobject Protocol},
  publisher = {MIT Press},
  address   = {Cambridge, MA},
  year      = {1991}
}

@article{DuranEtAl2019,
  author  = {Dur{\'a}n, Francisco and Eker, Steven and Escobar, Santiago and Mart{\'i}-Oliet, Narciso and Meseguer, Jos{\'e} and Rubio, Rub{\'e}n and Talcott, Carolyn},
  title   = {Programming and Symbolic Computation in Maude},
  journal = {arXiv preprint arXiv:1910.08416},
  year    = {2019}
}
