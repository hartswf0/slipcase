ZETTEL

ID:
WORKWORDS-PROMPT-001

TITLE:
In prompt programming, specification and implementation can occupy the same sentence.

SOURCE:
Jenny T. Liang, Melissa Lin, Nikitha Rao, and Brad A. Myers — “Prompts Are Programs Too! Understanding How Developers Build Software Containing Prompts” — Proceedings of the ACM on Software Engineering — 2025 — DOI: 10.1145/3729342

PASSAGE:
[PARAPHRASE] Liang et al.’s interviews with 20 prompt developers identify a structural difference between traditional programming and prompt programming: requirements that would ordinarily be specified separately from implementation can instead be expressed directly in the prompt, where the prompt simultaneously states desired behavior and constitutes part of the mechanism intended to produce that behavior.

[PARAPHRASE] They also find that experienced prompt programmers repeatedly construct mental models of how a foundation model responds to a prompt, yet those mental models remain unreliable even after many prompts and iterations.

RESEARCH OBJECT:
PROMPT COLLAPSES THE DISTANCE BETWEEN SPECIFICATION AND IMPLEMENTATION.

“Make the answer concise” can be simultaneously:

a requirement about the desired artifact

and

a computational intervention intended to cause that artifact.

The sentence says what ought to happen while participating in making it happen.

LOCAL MOVE:
This sharpens the work-and-words problem.

Words do not become operations simply because they are imperative.

Prompt programming creates an apparatus in which a requirement can also function as part of its own implementation.

SOURCE TERMS:
prompt programming
requirements
implementation
mental model
foundation model
prompt iteration
software development

WHAT BECAME STRANGE:
Traditional programming permits us to ask whether the implementation satisfies the specification.

What happens when specification and implementation are partly the same artifact?

A failed prompt may no longer tell us whether:

the requirement was wrong,
the implementation was wrong,
the interpreter behaved unexpectedly,
or the sentence failed in both roles simultaneously.

QUESTION:
What forms of criticism, debugging, and verification become possible when specification and implementation are entangled?

DEEPER QUESTION:
Is the prompt best understood as code, specification, test, interface utterance, or an historically unusual artifact that partially occupies all four positions?

MECHANISM:
Developer writes natural-language requirement
→ foundation model interprets same language as conditioning
→ output becomes evidence about both requirement and implementation
→ developer revises language
→ revised specification is also revised implementation.

FORMAL SHIFT:
FROM:

SPECIFICATION
→ IMPLEMENTATION
→ EXECUTION
→ TEST AGAINST SPECIFICATION

TO:

PROMPT {SPECIFICATION + PARTIAL IMPLEMENTATION}
→ EXECUTION
→ OUTPUT
→ REVISION OF THE SAME ARTIFACT.

SOURCE FORMALISM:
The source uses qualitative grounded-theory analysis of interviews with 20 developers and compares activities in prompt programming with traditional software development.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

R = expressed requirement
P = prompt text
I = operational implementation.

Traditional software:

R ≠ I

and:

TEST(I,R).

Prompt programming may instead contain:

R ⊂ P
and
P ⊂ I.

Thus changing the requirement can directly change the implementation:

ΔR → ΔP → ΔI.

TENSION:
“Prompts are programs too” is productive but potentially too quick.

If prompts were simply another programming language, the collapse between requirement and implementation would be less interesting.

The stronger possibility is that prompt practice violates the distinction by which we normally recognize programming in the first place.

MISSING:
A taxonomy of sentences according to whether they function as:

requirement only,
implementation only,
example,
constraint,
test,
context,
or several simultaneously.

BOUNDARY:
The source studies developers building LLM-powered software. It does not establish that every conversational or generative-image prompt should be treated as a program.

CITATION TRAIL:
[[DEFAULT-IMAGES-CHI26-B-1]]
→ executed prompt differs from visible prompt
→ Liang et al.
→ prompt becomes implementation as well as specification
→ next edge: requirements engineering, executable specifications, contracts, and programming-by-example.

TEST:
Take a real production prompt.

Annotate every clause independently as:

SPECIFICATION
IMPLEMENTATION
TEST
EXAMPLE
CONTEXT
META-INSTRUCTION.

Then delete clauses one at a time.

If clauses routinely occupy several categories and their removal changes both what counts as success and how success is produced, specification/implementation collapse is empirically visible.

PLATFORM:
LLM application development; prompt programming.

LINKS:
[[DEFAULT-IMAGES-CHI26-B-1]]

BIBTEX:
@article{Liang2025PromptsPrograms,
  author = {Liang, Jenny T. and Lin, Melissa and Rao, Nikitha and Myers, Brad A.},
  title = {Prompts Are Programs Too! Understanding How Developers Build Software Containing Prompts},
  journal = {Proceedings of the ACM on Software Engineering},
  volume = {2},
  year = {2025},
  doi = {10.1145/3729342}
}
