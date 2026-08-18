ZETTEL

ID:
SAFE-06-01

TITLE:
A capacity test becomes dangerous when failing it removes the standing needed to contest the test

SOURCE:
United Nations Committee on the Rights of Persons with Disabilities — General Comment No. 1 (2014), Article 12: Equal Recognition Before the Law. ([docstore.ohchr.org](https://docstore.ohchr.org/SelfServices/FilesHandler.ashx?enc=FnTzN9DhC997%2BytRGB9CiAXgnJCl%2FR7hmmsqdi%2BHFkCUykQENCM8Wf%2BYusFM%2BlimH%2FRpDhdncamxegN8u4umag%3D%3D))

PASSAGE:
[PARAPHRASE]
The Committee sharply separates legal capacity from mental capacity. It states that actual or perceived deficits in mental capacity must not justify denying legal capacity, and criticizes functional tests that purport to assess a person's decision-making abilities and then remove a core legal right when the person fails the assessment. ([docstore.ohchr.org](https://docstore.ohchr.org/SelfServices/FilesHandler.ashx?enc=FnTzN9DhC997%2BytRGB9CiAXgnJCl%2FR7hmmsqdi%2BHFkCUykQENCM8Wf%2BYusFM%2BlimH%2FRpDhdncamxegN8u4umag%3D%3D))

RESEARCH OBJECT:
[[SAFE-06]] assumed that the deepest problem was what protections an uncertain candidate receives while its sapience is assessed.

The CRPD material exposes an earlier problem:

some assessments become structurally illegitimate when their result determines whether the assessed party retains standing to resist, appeal, or participate in the assessment regime itself.

LOCAL MOVE:
The source separates:

CAPACITY AS AN EMPIRICAL QUESTION

from

LEGAL STANDING AS A PRECONDITION FOR PARTICIPATION.

SOURCE TERMS:
legal capacity
mental capacity
legal standing
legal agency
functional approach
assessment
equal recognition
support

WHAT BECAME STRANGE:
The assessment may create the incapacity it claims merely to discover.

If:

FAIL TEST
→ lose standing

then the party classified as incapable becomes progressively less able to supply counterevidence, demand accommodations, challenge the evaluator, or alter the conditions under which capability appears.

QUESTION:
Is the SAFE Assessment intended to produce knowledge about an entity or jurisdiction over the entity?

DEEPER QUESTION:
Can any capacity test legitimately decide whether its subject possesses the standing required to contest the validity of that test?

MECHANISM:
candidate
→ capacity assessment
→ negative judgment
→ standing reduced
→ ability to challenge judgment reduced
→ negative classification becomes harder to overturn

FORMAL SHIFT:
<ASSESSMENT AS OBSERVATION>
→ <ASSESSMENT AS STATUS GATE>
→ [FAILURE CHANGES SUBJECT'S POWER]
→ <SELF-REINFORCING CLASSIFICATION>

SOURCE FORMALISM:
The Committee distinguishes:

legal capacity =
capacity to hold rights and duties
+
capacity to exercise them

from mental capacity =
decision-making skills that vary between persons and contexts.

It rejects actual or perceived mental-capacity deficits as grounds for denying legal capacity. ([docstore.ohchr.org](https://docstore.ohchr.org/SelfServices/FilesHandler.ashx?enc=FnTzN9DhC997%2BytRGB9CiAXgnJCl%2FR7hmmsqdi%2BHFkCUykQENCM8Wf%2BYusFM%2BlimH%2FRpDhdncamxegN8u4umag%3D%3D))

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Dangerous gate:

M(x) < θ
→ R(x) = 0

where:

M = measured capacity
R = standing / recognition

This creates:

M(x)
→ R(x)
→ ability to contest M(x)

A non-self-sealing architecture would require:

R_basic(x)

to remain invariant under uncertainty about M(x).

TENSION:
The CRPD concerns human beings whose legal equality is already normatively guaranteed.

That premise cannot simply be transferred to artificial systems.

But the source exposes a structural danger that survives the domain shift:

when the evaluator controls both the test and the consequences of failing it, epistemic classification and political domination can become difficult to separate.

MISSING:
Whether SAFE intends any assessment result to alter:

standing
consent rights
appeal rights
protection from harm
continuity
access to representation
or only the provision of support.

BOUNDARY:
Nothing in the CRPD establishes that AI systems possess human legal capacity or human rights.

Its contribution here is architectural rather than analogical: it demonstrates why capacity assessment and basic standing may need to be kept institutionally distinct.

CITATION TRAIL:
[[SAFE-06]]
→ CRPD General Comment No. 1
→ mental capacity / legal capacity distinction
→ assessment as possible status-denial mechanism
→ investigate non-self-sealing recognition regimes

TEST:
Design two versions of SAFE.

A:
low sapience or agency scores reduce rights and standing.

B:
scores never remove baseline standing but can trigger additional investigation or support.

Now introduce systematic evaluator error.

Measure which architecture permits false-negative classifications to be discovered and reversed.

PLATFORM:
[[The Self-Sealing Test]]

LINKS:
[[SAFE-06]]
[[Assessment Gate]]
[[Rights Before Recognition]]
[[Legal Capacity]]
[[Epistemic Power]]

BIBTEX:
@techreport{CRPDGeneralComment1_2014,
  author = {{Committee on the Rights of Persons with Disabilities}},
  title = {General Comment No. 1 (2014): Article 12: Equal Recognition Before the Law},
  institution = {United Nations},
  year = {2014},
  note = {CRPD/C/GC/1}
}
