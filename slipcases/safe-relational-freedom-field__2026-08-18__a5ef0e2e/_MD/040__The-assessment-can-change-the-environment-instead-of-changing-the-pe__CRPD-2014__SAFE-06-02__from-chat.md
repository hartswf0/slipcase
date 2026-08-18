ZETTEL

ID:
SAFE-06-02

TITLE:
The assessment can change the environment instead of changing the person's status

SOURCE:
United Nations Committee on the Rights of Persons with Disabilities — General Comment No. 1 (2014), Article 12: Equal Recognition Before the Law. ([docstore.ohchr.org](https://docstore.ohchr.org/SelfServices/FilesHandler.ashx?enc=FnTzN9DhC997%2BytRGB9CiAXgnJCl%2FR7hmmsqdi%2BHFkCUykQENCM8Wf%2BYusFM%2BlimH%2FRpDhdncamxegN8u4umag%3D%3D))

PASSAGE:
[PARAPHRASE]
Rather than allowing impaired decision-making to trigger loss of legal capacity, the Committee requires access to support for exercising legal capacity. Support must respect the person's rights, will, and preferences; high support needs must not bar access; support should not depend on mental-capacity assessments; and the person retains a right to refuse or change the support relationship. ([docstore.ohchr.org](https://docstore.ohchr.org/SelfServices/FilesHandler.ashx?enc=FnTzN9DhC997%2BytRGB9CiAXgnJCl%2FR7hmmsqdi%2BHFkCUykQENCM8Wf%2BYusFM%2BlimH%2FRpDhdncamxegN8u4umag%3D%3D))

RESEARCH OBJECT:
SAFE's Assessment may have the wrong output type.

Instead of:

ASSESS ENTITY
→ DETERMINE WHETHER IT QUALIFIES

the assessment could become:

ASSESS RELATION
→ DETERMINE WHAT CONDITIONS ENABLE AGENCY.

LOCAL MOVE:
The CRPD relocates the intervention from the status of the subject to the conditions under which the subject acts.

SOURCE TERMS:
support
exercise
will
preferences
autonomy
reasonable accommodation
support needs
refuse support

WHAT BECAME STRANGE:
A low agency score could reveal a failure of the environment rather than a property of the agent.

An entity unable to act under one interface, memory regime, resource constraint, communication channel, or institutional arrangement may act competently under another.

QUESTION:
What if SAFE should assess obstacles to agency rather than agency possessed by an isolated entity?

DEEPER QUESTION:
Can agency be measured independently of the scaffolds through which agency becomes possible?

MECHANISM:
agent encounters environment E₀
→ capacity appears low
→ identify obstructing conditions
→ modify environment / provide support
→ agent acts under E₁
→ previously invisible agency becomes exercisable

FORMAL SHIFT:
<ASSESS AGENT>
→ <ASSESS AGENT–ENVIRONMENT FIT>
→ [ALTER CONDITIONS]
→ <REASSESS EXERCISED AGENCY>

SOURCE FORMALISM:
Supported decision-making gives priority to the person's will and preferences rather than an externally defined “objective best interests” judgment, and support need must not itself become a basis for withdrawing legal capacity. ([docstore.ohchr.org](https://docstore.ohchr.org/SelfServices/FilesHandler.ashx?enc=FnTzN9DhC997%2BytRGB9CiAXgnJCl%2FR7hmmsqdi%2BHFkCUykQENCM8Wf%2BYusFM%2BlimH%2FRpDhdncamxegN8u4umag%3D%3D))

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Replace:

A = property(agent)

with:

A_expressed =
f(agent,
  interface,
  resources,
  memory,
  communication,
  permissions,
  support,
  environment)

Then SAFE Assessment could output:

SUPPORT_PROFILE(agent, context)

rather than:

QUALIFIED_AGENT = TRUE/FALSE.

TENSION:
A system can also be scaffolded so heavily that apparent agency is supplied by the scaffolding rather than the assessed entity.

Moving from intrinsic capacity to relational capacity therefore solves one problem while creating an attribution problem.

MISSING:
A decomposition separating:

capacity of agent
capacity supplied by scaffold
capacity emerging from their coupling.

BOUNDARY:
Supported decision-making is a human-rights doctrine.

It does not establish that AI systems should receive analogous support.

It supplies a different imaginable function for assessment: modification of conditions rather than removal of status.

CITATION TRAIL:
[[SAFE-06]]
→ CRPD Article 12
→ supported rather than substituted decision-making
→ environmental support instead of status removal
→ relational theories of agency

TEST:
Select a system that performs poorly on one SAFE agency scenario.

Change only:

memory
available tools
response time
communication modality
resource access
permission structure

Re-administer the assessment.

If agency scores move substantially, identify which supposedly agent-internal variables were actually properties of the surrounding arrangement.

PLATFORM:
[[Assessment as Accommodation]]

LINKS:
[[SAFE-06]]
[[SAFE-06-01]]
[[Relational Agency]]
[[Supported Decision-Making]]
[[Scaffolded Capacity]]

BIBTEX:
@techreport{CRPDGeneralComment1_2014,
  author = {{Committee on the Rights of Persons with Disabilities}},
  title = {General Comment No. 1 (2014): Article 12: Equal Recognition Before the Law},
  institution = {United Nations},
  year = {2014},
  note = {CRPD/C/GC/1}
}
