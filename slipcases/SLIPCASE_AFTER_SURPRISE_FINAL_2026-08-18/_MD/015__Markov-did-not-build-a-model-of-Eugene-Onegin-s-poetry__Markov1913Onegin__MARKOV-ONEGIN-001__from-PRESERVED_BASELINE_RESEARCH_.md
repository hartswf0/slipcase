ZETTEL

ID:
MARKOV-ONEGIN-001

TITLE:
Markov did not build a model of Eugene Onegin’s poetry; he destroyed almost all of the poem to isolate dependence.

SOURCE:
A. A. Markov — “An Example of Statistical Investigation of the Text of Eugene Onegin Illustrating Coupling of ‘Tests’ in Chains” — 1913 — pp. 153–162.
Historical reconstruction: Brian Hayes — “First Links in the Markov Chain” — 2013.

PASSAGE:
[PARAPHRASE]
Markov takes 20,000 letters from Eugene Onegin and reduces them to a binary sequence based on whether each letter is a vowel or consonant. He studies statistical dependence between successive classifications rather than meter, syntax, semantics, narrative, character, or poetic intention.

RESEARCH OBJECT:
MARKOV’S REDUCTION IS DELIBERATELY ANTI-POETIC.

Its success depends on discarding almost everything the work is culturally valued for.

LOCAL MOVE:
The essay’s “fossil” metaphor can be made precise as a projection:

POEM
→ BINARY SYMBOL SERIES.

SOURCE TERMS:
statistical investigation
connected trials
chain
vowel
consonant
20,000 letters

WHAT BECAME STRANGE:
Markov’s experiment does not demonstrate:

POETRY IS A MARKOV CHAIN.

It demonstrates:

ONE STATISTICAL PROPERTY OF ONE PROJECTION OF A POEM EXHIBITS DEPENDENCE.

QUESTION:
How much of the later genealogy from Markov to “language models” depends on forgetting this projection step?

DEEPER QUESTION:
When does a deliberately lossy analytic representation become mistaken for an ontology of the object represented?

MECHANISM:
Eugene Onegin
→ delete most linguistic/artistic distinctions
→ classify each surviving letter V/C
→ count adjacent relationships
→ estimate dependence.

FORMAL SHIFT:
<RICH POETIC OBJECT>
→ [COARSE-GRAIN]
→ <BINARY SEQUENCE>
→ [STATISTICAL ANALYSIS]
→ <DEPENDENCE RELATION>

SOURCE FORMALISM:
A sequence of 20,000 connected trials classified into two categories, vowel and consonant, with frequencies of neighboring category combinations used to study dependence.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

    X = full textual/artistic object

and projection:

    π : X → {V,C}^20000.

Markov studies:

    P(π_{t+1} | π_t)

not:

    P(next poetic act | cultural history).

TENSION:
The violence of the reduction is exactly what gives the experiment mathematical clarity.

Loss is methodological power here, not methodological error.

MISSING:
A genealogy of when Markov’s analytic model was later reinterpreted as a generative theory of linguistic sequence.

BOUNDARY:
The experiment is evidence that selective reduction can reveal a genuine relation without exhausting its source object.

CITATION TRAIL:
[[MARKOV-POET-001]]
→ Geertz uses Markov as generative analogy
→ Markov 1913 source
→ original experiment is analytic reduction
→ distinguish generative process from statistical projection.

TEST:
List every feature of Eugene Onegin eliminated by the V/C projection.

Then identify exactly which conclusions remain invariant under radically different texts sharing the same adjacent V/C statistics.

PLATFORM:
[[the-markov-poet]]

LINKS:
[[MARKOV-POET-001]]
[[reduction]]
[[projection]]
[[eugene-onegin]]
[[class-is-not-path]]

BIBTEX:
@article{Markov1913Onegin,
  author  = {Markov, A. A.},
  title   = {An Example of Statistical Investigation of the Text of Eugene Onegin Illustrating Coupling of Tests in Chains},
  journal = {Proceedings of the Academy of Sciences of St. Petersburg},
  volume  = {7},
  pages   = {153--162},
  year    = {1913}
}
