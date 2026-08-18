ZETTEL

ID:
CALLSHOT-20260817-11

TITLE:
SHOW THE ACT — before prompt engineering, programming by demonstration treated a performed example as source material from which a reusable procedure could be generalized.

SOURCE:
Allen Cypher, ed. — “Watch What I Do: Programming by Demonstration” — MIT Press — 1993; Henry Lieberman — Programming by Example overview.
https://acypher.com/wwid/
https://web.media.mit.edu/~lieber/PBE/index.html

PASSAGE:
[PARAPHRASE]
Programming by demonstration/programming by example teaches a computer new behavior by letting a user perform concrete actions while the system records the performance and generalizes a reusable program for related cases. The 1993 collection Watch What I Do gathers systems built around this premise, including Pygmalion, Tinker, Peridot, Eager, and other demonstrational interfaces.

RESEARCH OBJECT:
PERFORMANCE-AS-SPECIFICATION.

LOCAL MOVE:
[[CALLSHOT-20260817-01]] showed that examples can declare the shape of a model interaction.

This earlier lineage makes the operation more bodily and procedural:

DO THE THING ONCE.

LET THE SYSTEM WATCH.

ASK IT TO INFER WHAT PART OF THE PERFORMANCE WAS THE PROGRAM.

The shot is called by enacted behavior rather than a verbal command.

SOURCE TERMS:
“Programming by Demonstration”
“Programming by Example”
“demonstrating actions”
“concrete examples”
“records user actions”
“generalizes a program”

WHAT BECAME STRANGE:
Demonstration is radically underspecified.

Every performance contains accidental details.

If I drag three .ps files to the trash, did I mean:
DELETE THESE THREE FILES,
DELETE ALL .ps FILES,
DELETE EVERYTHING I TOUCH,
or REPEAT THIS GESTURE?

The system must infer which aspects of the example are invariant and which are incidental.

That is the same specification problem prompt users now encounter after the model acts.

QUESTION:
What tells a system which features of a demonstrated performance should become the reusable rule?

DEEPER QUESTION:
Are prompting and programming by demonstration dual practices—one begins with language and asks the machine to construct an action; the other begins with action and asks the machine to construct the rule?

MECHANISM:
USER PERFORMS EXAMPLE e
→ system records ACTION TRACE + CONTEXT
→ infer candidate generalization G
→ apply G to new case e*
→ user accepts/corrects behavior.

FORMAL SHIFT:
FROM:
SAY THE PROCEDURE
→ EXECUTE IT.

TO:
EXECUTE AN INSTANCE
→ INFER THE PROCEDURE.

SOURCE FORMALISM:
The Programming by Example overview describes a system recording user actions on concrete examples and generalizing a program for new examples. Watch What I Do assembles systems and perspectives organized around programming by demonstration.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

PROMPTING:
DESCRIPTION → INSTANCE.

PROGRAMMING BY DEMONSTRATION:
INSTANCE → DESCRIPTION/PROCEDURE.

HYBRID LOOP:
DESCRIPTION
→ GENERATED ACTION
→ CORRECTION / DEMONSTRATION
→ UPDATED PROCEDURE.

TENSION:
A demonstration makes procedure acquisition easier for users who can perform the task, but inference from examples introduces ambiguity about intended generalization.

Natural-language instructions make abstractions expressible but introduce ambiguity about grounding and execution.

MISSING:
A contemporary system that lets a user fluidly move among instruction, demonstration, correction, and formal constraint while preserving all four as one evolving specification.

BOUNDARY:
This is a historical/mechanistic crossing, not a claim that contemporary LLM prompting descends directly from the programming-by-demonstration research community.

CITATION TRAIL:
[[CALLSHOT-20260817-01]]
→ examples as interface specification
→ Cypher 1993 / Lieberman Programming by Example
→ example becomes action trace
→ action trace generalized into reusable procedure
→ “calling the shot” can run backward from doing to describing.

TEST:
Choose a small desktop task.

Specify it four ways:
1. natural-language instruction,
2. one demonstration,
3. three demonstrations,
4. instruction + demonstration + negative example.

On held-out cases, record which accidental features each representation causes the system to preserve.

The error pattern reveals what each specification medium leaves implicit.

PLATFORM:
Programming by Demonstration / end-user programming

LINKS:
[[CALLSHOT-20260817-01]]
[[CALLSHOT-20260817-05]]

BIBTEX:
@book{cypher1993watch,
  editor={Cypher, Allen},
  title={Watch What I Do: Programming by Demonstration},
  publisher={MIT Press},
  year={1993},
  url={https://acypher.com/wwid/}
}
