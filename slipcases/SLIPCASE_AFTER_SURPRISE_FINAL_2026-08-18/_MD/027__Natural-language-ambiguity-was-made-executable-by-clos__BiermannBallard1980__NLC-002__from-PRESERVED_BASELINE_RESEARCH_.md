ZETTEL

ID:
NLC-002

TITLE:
Natural-language ambiguity was made executable by closing a human–machine repair loop rather than by eliminating ambiguity.

SOURCE:
Alan W. Biermann and Bruce W. Ballard — “Toward Natural Language Computation I” — 1980 — pp. 71–74.

PASSAGE:
[PARAPHRASE]
NLC provides immediate visual feedback after each command so users can see misinterpretations, back up, and rephrase ambiguous or incorrect commands. Its parser uses nondeterministic transition networks, while later stages screen parses and execute the selected interpretation.

RESEARCH OBJECT:
AMBIGUITY and EXECUTION already coexist in a machine system.

The stabilizing mechanism is INTERACTIVE REPAIR.

LOCAL MOVE:
Instead of requiring a perfectly unambiguous source language before execution, NLC distributes semantic correction across repeated user/system interaction.

SOURCE TERMS:
ambiguity
misinterpretation
feedback
rephrase
nondeterministic transition nets
parser
execution

WHAT BECAME STRANGE:
The supposed historical divide:

AMBIGUOUS HUMAN LANGUAGE
versus
EXACT MACHINE EXECUTION

had already been engineered as a loop forty years before modern LLMs.

QUESTION:
Does a language need fixed semantics at inscription time if ambiguity can be resolved through execution-feedback-repair?

DEEPER QUESTION:
Is prompt interaction historically novel because the probabilistic interpreter internalizes more of the repair process, or because the repair loop now operates over a dramatically larger semantic space?

MECHANISM:
utterance
→ lexical alternatives
→ nondeterministic parse search
→ candidate semantic interpretation
→ execution
→ visible system consequence
→ user evaluates consequence
→ accept OR rephrase
→ next utterance.

FORMAL SHIFT:
<AMBIGUOUS DESCRIPTION>
→ [INTERPRET]
→ <TENTATIVE OPERATION>
→ [OBSERVE]
→ <REPAIR>
→ <STABILIZED INTENT>

SOURCE FORMALISM:
The parser is described as using nondeterministic transition nets related to augmented transition networks.

The system architecture explicitly includes context, semantics, a data world, execution, and visual feedback.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Instead of demanding:

    Interpret(u) = exactly_one_meaning

define an interactive process:

    μ₀ = Interpret(u₀)
    s₁ = Execute(μ₀,s₀)
    u₁ = Repair(u₀, Observe(s₁))

until:

    Accept(user, Observe(sₙ)).

TENSION:
NLC’s ambiguity is tightly bounded by hand-built lexical, syntactic, semantic, and domain constraints. Modern LLM ambiguity occurs in a much larger and less explicitly enumerated interpretation space.

MISSING:
A historical genealogy of clarification and repair from:

NLC
interactive semantic parsing
spoken dialogue systems
LLM conversational repair.

BOUNDARY:
Ambiguity does not prevent machine operativity.

It changes where semantic stabilization occurs.

CITATION TRAIL:
[[MINIMUM-024]]
→ NLC visual feedback
→ nondeterministic parsing
→ rephrasing after execution
→ ambiguity as interaction loop.

[[MINIMUM-025]]
→ underdetermination
→ formally/architecturally managed branching
→ observer-mediated repair.

TEST:
Implement the same ambiguous instruction in:

A. reject-unless-unambiguous compiler
B. NLC-style execute-and-repair loop
C. LLM conversational system.

Measure:
number of candidate interpretations,
repair turns,
incorrect actions before stabilization,
and explicitness of the interpretation space.

PLATFORM:
[[generative-collapse]]

LINKS:
[[MINIMUM-024]]
[[MINIMUM-025]]
[[ambiguity-repair-loop]]
[[interactive-semantics]]
[[NLC]]

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
