ZETTEL

ID:
REFLECT-002

TITLE:
Maude makes the transition theory itself into data that another transition theory can execute.

SOURCE:
Francisco Durán, Steven Eker, Santiago Escobar, Narciso Martí-Oliet, José Meseguer, Rubén Rubio, and Carolyn Talcott — “Programming and Symbolic Computation in Maude” — 2019 — §8, “Reflection, META-LEVEL, and Meta-Interpreters.”

PASSAGE:
[PARAPHRASE]
Rewriting logic is reflective: a finitely presented rewrite theory R and a term t can be represented as data inside a universal rewrite theory U, with rewriting under R mirrored by rewriting the representation of <R,t> under U. U can represent itself, yielding a reflective tower.

RESEARCH OBJECT:
The RULE SYSTEM joins the state.

LOCAL MOVE:
A transition semantics no longer needs to remain external to the configurations being manipulated.

The semantics can itself acquire a representation and participate in computation.

SOURCE TERMS:
reflection
rewrite theory
universal theory
metatheory
representation
META-LEVEL
reflective tower

WHAT BECAME STRANGE:
The parent’s reflexive model:

    <S_t,T_t,I_t>
      →
    <S_{t+1},T_{t+1},I_{t+1}>

is not merely a sociological possibility.

Rewriting logic supplies an explicit formal mechanism for representing T itself as manipulable data.

QUESTION:
Does reflection truly eliminate fixed semantic structure, or merely relocate it into the universal meta-theory U?

DEEPER QUESTION:
Can a computational system modify the rules by which its own rule modifications are interpreted without eventually presupposing another fixed level?

MECHANISM:
object level:

    R ⊢ t →* t'

representation:

    <R,t>

meta level:

    U ⊢ <R,t> →* <R,t'>

and because U is representable in itself:

    <U,<R,t>>

can itself participate in a higher reflective level.

FORMAL SHIFT:
<TRANSITION THEORY AS META-LEVEL BACKGROUND>
→ <TRANSITION THEORY AS OBJECT-LEVEL DATA>
→ [META-INTERPRETATION]
→ <REFLECTIVE COMPUTATION>

SOURCE FORMALISM:
The source gives the equivalence:

    R ⊢ t →* t'
    iff
    U ⊢ <R,t> →* <R,t'>

for represented finitely presented rewrite theories and terms.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Expand state:

    Γ_meta = <R, t>

Then a meta-transition can alter:

    <R,t>
       →
    <R',t'>

so the transition policy R can itself become a coordinate of configuration.

TENSION:
A particular realization of U and the Maude META-LEVEL still provides an operative substrate for the reflective computation.

Self-representation does not automatically imply substrate-free semantics.

MISSING:
A worked case where a running Maude program alters a represented rewrite theory and then continues computation under the altered theory.

BOUNDARY:
META-STABILITY cannot distinguish social from computational systems merely by asking whether the rule system can become state.

CITATION TRAIL:
[[MINIMUM-026]]
→ semantic self-modification
→ rewriting-logic reflection
→ universal theory U
→ reflective tower
→ fixed-meta-level question.

TEST:
Represent a small rewrite theory R in Maude.

Perform a metalevel transformation:

    R → R'

that changes one transition rule.

Then execute the same represented term t under R and R'.

Compare behavioral difference while tracing which interpreter level remains unchanged.

PLATFORM:
[[description-becomes-operation]]

LINKS:
[[MINIMUM-026]]
[[reflection]]
[[rewrite-theory-as-data]]
[[reflective-tower]]
[[ontology-change]]

BIBTEX:
@article{DuranEtAl2019,
  author  = {Dur{\'a}n, Francisco and Eker, Steven and Escobar, Santiago and Mart{\'i}-Oliet, Narciso and Meseguer, Jos{\'e} and Rubio, Rub{\'e}n and Talcott, Carolyn},
  title   = {Programming and Symbolic Computation in Maude},
  journal = {arXiv preprint arXiv:1910.08416},
  year    = {2019}
}
