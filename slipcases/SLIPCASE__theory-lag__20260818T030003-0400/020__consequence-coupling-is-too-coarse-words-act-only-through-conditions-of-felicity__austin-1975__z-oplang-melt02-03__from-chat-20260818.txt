ZETTEL

ID:
Z-OPLANG-MELT02-03

TITLE:
Consequence coupling is too coarse: words act only through conditions of felicity.

SOURCE:
J. L. Austin — How to Do Things with Words — 2nd ed. — 1962/1975 — Lectures I–II, especially pp. 8–13.

SOURCE URL:
https://courses.lsa.umich.edu/jptw/wp-content/uploads/sites/23/2017/08/Austin-HowtodoThingsWithWordsexcerpts.pdf

PASSAGE:
[QUOTE]
“The uttering of the words is, indeed, usually a leading incident in the performance of the act.”

[PARAPHRASE]
Austin immediately insists that the circumstances must be appropriate and that speakers or other participants may also need to perform additional actions for the act to succeed.

RESEARCH OBJECT:
<COMPUTATIONAL FELICITY CONDITIONS>.

Our axis of CONSEQUENCE COUPLING currently asks how directly an interpreted representation can change system state.

Austin shows why directness is insufficient.

A consequential utterance succeeds only inside an arrangement that makes the utterance eligible to have that force.

LOCAL MOVE:
Austin breaks the philosophical assumption that meaningful utterances merely describe facts.

But he simultaneously refuses the opposite simplification that words magically perform actions by themselves.

SOURCE TERMS:
“performative”
“circumstances”
“appropriate”
“act”
“utterance”
“speaker”
“actions”
“performance”

WHAT BECAME STRANGE:
“Consequence-bearing description” still makes the description sound too causally privileged.

Consider:

DELETE THIS.

It may:
- do nothing in a text document,
- request clarification in a chat,
- remove an object in an editor,
- destroy a database record in an agentic system,
- be blocked by permissions.

Semantic slack can remain identical while operative force changes completely.

The missing variable is not merely coupling strength.

It is the set of conditions under which the expression possesses operative force.

QUESTION:
What are the felicity conditions of a computational utterance?

DEEPER QUESTION:
When an agentic system gives language the power to alter the world, who or what confers the authority by which the utterance counts as an action?

MECHANISM:
<expression>
is produced.

But action succeeds only if:

<referent exists>
AND
<interpreter recognizes operation>
AND
<actor has authority>
AND
<tool is available>
AND
<state permits transition>
AND
<procedure succeeds>.

The expression is one incident in a larger operative arrangement.

FORMAL SHIFT:
<EXPRESSION>
→ [CONSEQUENCE COUPLING]
→ <STATE CHANGE>

becomes:

<EXPRESSION>
+
{FELICITY CONDITIONS}
→ [ACQUIRE OPERATIVE FORCE]
→ [ATTEMPT TRANSITION]
→ <SUCCESS / MISFIRE / BLOCK>

SOURCE FORMALISM:
Austin distinguishes saying something from doing something in or by saying it and develops the importance of appropriate circumstances and accompanying acts.

He does not provide computational semantics.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

F = {
  valid_reference,
  authorized_actor,
  recognized_operation,
  available_tool,
  admissible_state,
  successful_execution
}

Then:

operative_force(e) ≠ semantic_content(e)

and:

transition(e, S)

is enabled only when a relevant subset of F holds.

This introduces computational analogues of infelicity:

MISINVOCATION
MISREFERENCE
UNAUTHORIZED
UNAVAILABLE
MISEXECUTION
POSTCONDITION_FAILURE

TENSION:
A prompt-model interaction is not automatically an Austinian performative.

Many model outputs are predictions or proposals rather than socially conventional acts.

Calling every tool call a speech act would flatten Austin’s institutional and conventional concerns.

MISSING:
A distinction among:

<semantic interpretation>
<illocution-like force>
<tool authorization>
<causal execution>
<social consequence>.

“Consequence coupling” currently collapses these.

BOUNDARY:
Austin does not theorize computation.

The source licenses a structural challenge:

language having consequences cannot be explained from the words alone.

CITATION TRAIL:
Austin — felicity / infelicity.
Searle — constitutive rules.
Tool permissions and capability security.
Transaction semantics.
Speech acts in HCI.
Institutional authority.

TEST:
Use one invariant command:

“Delete this.”

Run it while independently varying:
- reference resolution,
- permissions,
- tool availability,
- valid system state,
- confirmation requirements.

Construct a failure matrix.

If operative force varies while expression and semantic interpretation remain constant, consequence coupling should be decomposed into felicity conditions rather than represented as a single scalar.

PLATFORM:
[[Operative Language]]

LINKS:
[[Consequence Coupling]]
[[Consequence-Bearing Description]]
[[Computational Felicity]]

BIBTEX:
@book{austin1975how,
  author = {Austin, J. L.},
  title = {How to Do Things with Words},
  editor = {Urmson, J. O. and Sbisà, Marina},
  edition = {2},
  publisher = {Harvard University Press},
  year = {1975},
  note = {Lectures originally delivered in 1955; first edition published 1962}
}
