ZETTEL

ID:
MINIMUM-026

TITLE:
The deeper cultural/computational difference may be that programs usually hold their operational ontology fixed during a run while social actors can renegotiate the categories defining the state space.

SOURCE:
COLLISION — Bourdieu 1977; Deleuze and Guattari 1987; W3C SCXML 2015.

PASSAGE:
[PARAPHRASE]
SCXML normatively specifies in advance what counts as a state, transition, event, legal configuration, and transition-selection procedure. Bourdieu’s practices and Deleuze–Guattari’s assemblages instead make historical dispositions, authorization, and changing social classifications part of the phenomenon being explained. 23

RESEARCH OBJECT:
The strongest boundary candidate has moved from DETERMINACY to META-STABILITY.

LOCAL MOVE:
The comparison asks whether the rule system itself can change from inside the process it regulates.

SOURCE TERMS:
SCXML:
legal state configuration
transition
processor

BOURDIEU:
habitus
improvisation

DELEUZE/GUATTARI:
assemblage
incorporeal transformation

WHAT BECAME STRANGE:
Human interpretation is not problematic merely because multiple responses are possible.

The harder case is when participants can change:

what the states are,
what the rules mean,
who is authorized,
and what counts as valid execution.

QUESTION:
Must a programming language hold F, I, S, and T fixed during execution?

DEEPER QUESTION:
What happens when a system can rewrite its own interpreter, state ontology, or authority structure?

MECHANISM:
CLASSICAL FIXED SEMANTICS:

    <F,I,S,T> fixed
    e causes transitions within S.

REFLEXIVE SOCIAL PROCESS:

    γ_t
    → action
    → modifies not only γ
      but possibly F,I,S,T themselves.

FORMAL SHIFT:
<STATE TRANSITION>
→ <SEMANTICS / ONTOLOGY TRANSITION>

SOURCE FORMALISM:
SCXML provides a fixed normative interpretation algorithm. 24

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Ordinary:

    T_t : S → Δ(S)

Reflexive:

    <S_t,T_t,I_t>
        → 
    <S_{t+1},T_{t+1},I_{t+1}>

The semantics itself becomes state.

TENSION:
Programming systems can also support:
reflection,
self-modifying code,
dynamic linking,
metaprogramming,
language extension,
and interpreter rewriting.

Therefore even META-STABILITY may be a gradient, not an absolute boundary.

MISSING:
A theory of self-modifying semantic systems.

BOUNDARY:
This is a new research hypothesis, not a conclusion supplied by any single source.

CITATION TRAIL:
reflection.
self-interpreters.
metaobject protocols.
institutional change.
endogenous ontology.

TEST:
Construct:
A. fixed-transition program,
B. self-modifying interpreter,
C. institution whose participants can alter its rules.

Compare not output unpredictability but WHICH COMPONENTS OF THE SEMANTIC MACHINE MAY THEMSELVES CHANGE.

PLATFORM:
[[description-becomes-operation]]

LINKS:
[[semantic-self-modification]]
[[ontology-change]]
[[reflexive-execution]]
[[culture-computation-boundary]]

BIBTEX:
@techreport{W3CSCXML2015,
  author      = {{World Wide Web Consortium}},
  title       = {State Chart XML (SCXML): State Machine Notation for Control Abstraction},
  institution = {W3C},
  year        = {2015}
}

@book{Bourdieu1977,
  author     = {Bourdieu, Pierre},
  title      = {Outline of a Theory of Practice},
  translator = {Nice, Richard},
  publisher  = {Cambridge University Press},
  year       = {1977}
}

@book{DeleuzeGuattari1987,
  author     = {Deleuze, Gilles and Guattari, F{\'e}lix},
  title      = {A Thousand Plateaus: Capitalism and Schizophrenia},
  translator = {Massumi, Brian},
  publisher  = {University of Minnesota Press},
  year       = {1987}
}
