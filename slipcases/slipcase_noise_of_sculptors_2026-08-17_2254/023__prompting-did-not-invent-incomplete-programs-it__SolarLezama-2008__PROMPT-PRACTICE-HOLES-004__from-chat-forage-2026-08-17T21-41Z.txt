ZETTEL

ID:
PROMPT-PRACTICE-HOLES-004

TITLE:
PROMPTING DID NOT INVENT INCOMPLETE PROGRAMS; IT MAY HAVE INVENTED UNMARKED HOLES.

SOURCE:
Armando Solar-Lezama — “Program Synthesis by Sketching” — PhD dissertation, University of California, Berkeley, 2008.

SOURCE URL:
https://people.csail.mit.edu/asolar/papers/thesis.pdf

PASSAGE:
[QUOTE]
“The key novelty in sketching is the use of partial programs to describe the insight behind an implementation while leaving the details unspecified.”

RESEARCH OBJECT:
UNMARKED HOLE.

Incomplete specification predates natural-language prompting.

The sharper question is:

WHAT KIND OF INCOMPLETENESS CAN EXECUTE?

LOCAL MOVE:
[[SON-IEC-005]] shifted attention from the final prompt to iterative completion.

Sketching provides a strong ancestor for deferred formalization:

the programmer supplies a partial program
and the synthesizer completes missing details.

But Sketch makes missingness REPRESENTABLE.

The hole is explicit.

Prompting frequently does something stranger:

a detail can be absent without any marker saying that a choice remains unresolved.

The model silently chooses a completion.

SOURCE TERMS:
partial program
unspecified
sketch
synthesizer
implementation strategy
completions
holes
combinatorial search

WHAT BECAME STRANGE:
Compare:

SKETCH:

x = ??

with:

PROMPT:

“Make a house overlooking the ocean.”

The second expression does not say:

architectural style = ??
number of stories = ??
camera = ??
weather = ??
materials = ??
historical period = ??
occupancy = ??
orientation = ??

Yet execution requires many such decisions.

The incompleteness is not stored as explicit holes.

It is discovered only when generation forces a completion.

QUESTION:
Is the distinctive unit of natural-language programming not the HOLE but the UNMARKED HOLE?

DEEPER QUESTION:
How can a programming system expose decisions it made because the specification was silent, rather than because the user explicitly delegated them?

MECHANISM:
Sketch:

PARTIAL PROGRAM
→ explicit unknowns
→ constrained search
→ completed program.

Prompt generation:

PARTIAL DESCRIPTION
→ interpretation
→ hidden detection/creation of unresolved variables
→ model-selected completions
→ artifact.

The second system must decide both:

WHAT IS MISSING

and

HOW TO FILL IT.

FORMAL SHIFT:
FROM:

KNOWN SPECIFICATION
+
MARKED UNKNOWN VARIABLE

TO:

DESCRIPTION
+
UNMARKED UNDERDETERMINATION
+
INTERPRETER THAT INVENTS THE VARIABLES IT COMPLETES.

SOURCE FORMALISM:
[PARAPHRASE]

Solar-Lezama's sketching approach represents partial programs whose unspecified pieces are completed through search while preserving programmer-provided implementation structure.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

EXPLICIT HOLE:

SPEC = {
  A = fixed,
  B = ??,
  C = fixed
}

The synthesizer solves B.

UNMARKED HOLE:

DESCRIPTION = D

INTERPRET(D)
→ inferred variable set

V(D) = {v₁,v₂,...vₙ}

where neither:

n
nor
the identities of vᵢ

were explicitly supplied by the author.

Generation then chooses:

value(vᵢ).

DEFERRED FORMALIZATION may therefore contain two operations:

1. DEFER VALUE
2. DEFER DISCOVERY OF THE VARIABLE ITSELF.

TENSION:
If this distinction survives, “deferred formalization” cannot claim novelty merely from partial specification.

Sketching already formalizes deliberate incompleteness.

The stronger novelty candidate is:

SEMANTICALLY UNMARKED INCOMPLETENESS
+
EXECUTION
+
POST-HOC DISCOVERY OF THE MISSING VARIABLE.

MISSING:
A taxonomy separating:

explicit hole
implicit default
ordinary ambiguity
underspecification
unknown requirement
delegated choice
accidental omission.

An experiment showing that model-generated artifacts systematically reveal variables users did not know they had left open.

BOUNDARY:
Sketch operates over formally delimited program spaces and specifications.

Natural language does not automatically provide equivalent guarantees about completion correctness or candidate space.

CITATION TRAIL:
[[SON-IEC-005]]
→ iterative completion as practice

→ Solar-Lezama
→ partial programs already support deferred detail
→ explicit holes
→ natural-language prompts frequently omit the hole marker itself
→ deferred formalization shifts from FILL UNKNOWN to DISCOVER-AND-FILL UNKNOWN

TEST:
Choose one task.

Encode it twice.

A. FORMAL PARTIAL PROGRAM:
Enumerate every unresolved variable explicitly.

B. NATURAL-LANGUAGE DESCRIPTION:
Mention only the currently salient intent.

Execute both.

For B, inventory every consequential decision present in the output but absent from the input.

Classify each as:

DEFAULT
INFERRED
INVENTED
REQUIRED-BY-MEDIUM
AMBIGUOUS.

If B repeatedly introduces consequential variables that the author had not represented as unknowns, UNMARKED HOLE survives as a distinct mechanism.

PLATFORM:
MIT CSAIL / UC Berkeley

LINKS:
[[SON-IEC-005]]

BIBTEX:
@phdthesis{solarlezama2008program,
  author = {Armando Solar-Lezama},
  title = {Program Synthesis By Sketching},
  school = {University of California, Berkeley},
  year = {2008},
  url = {https://people.csail.mit.edu/asolar/papers/thesis.pdf}
}
