ZETTEL

ID:
winograd-flores-1986-cos-not-objective

TITLE:
Conditions of satisfaction are constitutive yet disputable, not objective facts waiting to be checked.

SOURCE:
Terry Winograd and Fernando Flores — Understanding Computers and Cognition — 1986 — Chapter 5, conversation-for-action discussion

SOURCE URL:
https://archive.org/details/understandingcom00wino

PASSAGE:
[SOURCE SUMMARY] The authors explicitly state that conditions of satisfaction are not objective realities independent of interpretation; requester and performer can disagree about whether they have been met.

RESEARCH OBJECT:
DISPUTED SATISFACTION AS A FIRST-CLASS STATE

LOCAL MOVE:
Refuse the easy compilation of satisfaction into a single boolean predicate.

SOURCE TERMS:
conditions of satisfaction; declaration; assessment; disagreement; interpretation

WHAT BECAME STRANGE:
The protocol’s apparent terminal state depends on a judgment that the theory says may remain contested.

QUESTION:
How should a runtime represent “done” when requester and performer inhabit incompatible assessments?

DEEPER QUESTION:
Can an institution remain computationally consistent without forcing one interpretation of satisfaction to become canonical?

MECHANISM:
<performance> → [ASSESS] → {satisfied, unsatisfied, disputed, renegotiated}

FORMAL SHIFT:
objective completion predicate → actor-indexed assessment

SOURCE FORMALISM:
No formal dispute calculus is supplied in the source.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
SATISFIED(agent,commitment,K) is actor-indexed; COMPLETE requires a settlement rule, not merely a sensed world state.

TENSION:
A database favors a single canonical status, while situated coordination can preserve divergent assessments.

MISSING:
Historical system behavior when Coordinator/ActionWorkflow participants disputed completion.

BOUNDARY:
The source supports interpretive disagreement, not unlimited relativism about every performance fact.

CITATION TRAIL:
Winograd/Flores conditions of satisfaction → ActionWorkflow satisfaction phase → DEMO acceptance → dispute semantics

TEST:
Create a completed task with conflicting customer/performer assessments and test whether the historical protocols preserve both views.

PLATFORM:
[[disputed-satisfaction]]

LINKS:
[[medina-mora-1992-background-runtime-a]]
[[dietz-1999-transaction-state]]
[[yolum-singh-2002-flexible-runtime-paths]]

BIBTEX:
@book{winogradflores1986understanding, author={Winograd, Terry and Flores, Fernando}, title={Understanding Computers and Cognition: A New Foundation for Design}, year={1986}, publisher={Ablex}, address={Norwood, NJ}}
