ZETTEL

ID:
UPTAKE-003

TITLE:
The strongest surviving invariant may be not specified uptake but counterfactual control: changing the representation must change the receiver’s behavioral policy.

SOURCE:
COLLISION — Alan W. Biermann and Bruce W. Ballard — “Toward Natural Language Computation I” — 1980; Manuel Clavel et al. — “The Maude 2.0 System” — 2003; Gregor Kiczales et al. — The Art of the Metaobject Protocol — 1991.

PASSAGE:
[PARAPHRASE]
NLC accepts English descriptions that alter immediate computation and can define new procedures. Maude shows that executability depends on interpreter level and strategy. Metaobject protocols show that descriptions can even modify parts of the interpreter’s own behavior.

RESEARCH OBJECT:
UPTAKE is too passive a word.

The cross-source invariant becoming visible is COUNTERFACTUAL CONTROL.

A representation is operative when variation in that representation produces systematic variation in what the receiving system can or will do.

LOCAL MOVE:
The inquiry shifts from asking:

IS THE TEXT EXECUTABLE?

to asking:

DOES THIS REPRESENTATION PARAMETERIZE BEHAVIOR IN A COUNTERFACTUALLY TRACEABLE WAY?

SOURCE TERMS:
command
procedure
execution
strategy
reflection
language behavior
interpreter

WHAT BECAME STRANGE:
This criterion no longer depends on:

determinism
Turing completeness
imperative syntax
fixed semantics
or physical machine code.

QUESTION:
Is counterfactual control strong enough to distinguish a program from ordinary causal input?

DEEPER QUESTION:
What additional structure distinguishes:

a program
a query
a command
a configuration file
a norm
a prompt

if all can counterfactually alter receiver behavior?

MECHANISM:
receiver I
+
configuration γ
+
representation r₁
→ behavior B₁

same I and relevant γ
+
representation r₂
→ behavior B₂

with:

    B₁ ≠ B₂

because of a systematic interpretation relation linking the difference in r to the difference in behavior.

FORMAL SHIFT:
<UPTAKE>
→ <COUNTERFACTUAL BEHAVIORAL PARAMETERIZATION>

SOURCE FORMALISM:
No cited source presents this as a universal definition.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Necessary candidate:

    ∃r₁,r₂,γ :
      r₁ ≠ r₂
      ∧
      Beh(I,r₁,γ) ≠ Beh(I,r₂,γ)

But ordinary inputs satisfy this too.

Stronger candidate:

    there exists a structured interpretation map M
    such that differences in syntactic/representational structure
    systematically compose into differences in behavior.

TENSION:
Even the stronger criterion may admit:

queries
protocol messages
legal instruments
musical scores
recipes.

This may be evidence that OPERATIVE DESCRIPTION is the correct genus and PROGRAM is a historically narrower subtype.

MISSING:
The extra discriminator for PROGRAM ROLE.

Candidates requiring further forage:

COMPOSITIONAL CONTROL
REUSABLE CONTROL
OPEN-ENDED CONTROL
CONTROL OVER A CLASS OF INPUTS
SELF-APPLICATION
EFFECTIVE REALIZATION.

BOUNDARY:
The current evidence supports abandoning deterministic execution as the boundary.

It does not yet support replacing it with counterfactual control as a sufficient definition of programming.

CITATION TRAIL:
[[MINIMUM-028]]
→ specified uptake
→ relative executability
→ strategy-dependent realization
→ counterfactual control.

[[MINIMUM-024]]
→ English command
→ English procedure definition
→ representational differences systematically alter computation.

TEST:
Create six pairs differing by one representation:

program
query
configuration file
legal order
cultural norm
LLM prompt.

Hold receiver/environment constant as far as possible.

For each measure:

1. Does representation variation change behavior?
2. Is the mapping compositional?
3. Does it govern a class of future inputs?
4. Can its behavior be reused?
5. Can its interpretation be mechanically realized?

Find the smallest predicate combination unique to the objects we independently call programs.

PLATFORM:
[[description-becomes-operation]]

LINKS:
[[MINIMUM-028]]
[[MINIMUM-024]]
[[counterfactual-control]]
[[program-role]]
[[operative-description]]

BIBTEX:
@article{BiermannBallard1980,
  author  = {Biermann, Alan W. and Ballard, Bruce W.},
  title   = {Toward Natural Language Computation I},
  journal = {American Journal of Computational Linguistics},
  volume  = {6},
  number  = {2},
  pages   = {71--86},
  year    = {1980}
}

@inproceedings{ClavelEtAl2003,
  author    = {Clavel, Manuel and Dur{\'a}n, Francisco and Eker, Steven and Lincoln, Patrick and Mart{\'i}-Oliet, Narciso and Meseguer, Jos{\'e} and Talcott, Carolyn},
  title     = {The Maude 2.0 System},
  booktitle = {Rewriting Techniques and Applications},
  series    = {Lecture Notes in Computer Science},
  volume    = {2706},
  pages     = {76--87},
  publisher = {Springer},
  year      = {2003}
}

@book{KiczalesEtAl1991,
  author    = {Kiczales, Gregor and des Rivi{\`e}res, Jim and Bobrow, Daniel G.},
  title     = {The Art of the Metaobject Protocol},
  publisher = {MIT Press},
  year      = {1991}
}
