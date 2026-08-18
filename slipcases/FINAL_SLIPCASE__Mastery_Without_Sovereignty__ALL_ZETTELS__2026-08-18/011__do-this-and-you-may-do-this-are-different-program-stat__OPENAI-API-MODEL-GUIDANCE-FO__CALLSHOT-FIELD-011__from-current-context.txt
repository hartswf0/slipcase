ZETTEL

ID:
CALLSHOT-FIELD-011

TITLE:
“DO THIS” AND “YOU MAY DO THIS” ARE DIFFERENT PROGRAM STATEMENTS.

SOURCE:
OpenAI API, “Model guidance” for GPT-5.6, current documentation accessed 2026-08-17. SOURCE URL: https://developers.openai.com/api/docs/guides/latest-model

PASSAGE:
[QUOTE]
“Define what level of action each request authorizes”

RESEARCH OBJECT:
AGENT PROMPTS MUST DISTINGUISH DESIRED OUTCOMES FROM THE AUTHORITY DELEGATED TO PURSUE THEM.

LOCAL MOVE:
Current OpenAI guidance recommends explicit autonomy and approval boundaries so agents can continue safe in-scope work while stopping before external, destructive, costly, or scope-expanding actions.

SOURCE TERMS:
“autonomy” · “approval boundaries” · “authorizes” · “external” · “destructive” · “costly” · “scope-expanding”

WHAT BECAME STRANGE:
Natural language now allocates temporary jurisdiction. A goal does not by itself specify what powers have been granted.

QUESTION:
What linguistic forms reliably distinguish task intent from authorization?

DEEPER QUESTION:
Do agent systems require a capability-security theory of prompting in which understanding a goal and possessing authority are orthogonal?

MECHANISM:
GOAL → candidate actions; AUTHORIZATION POLICY → allowed / confirm / forbidden; AGENT acts only inside envelope.

FORMAL SHIFT:
PROMPT = DESIRED OUTCOME → PROMPT = OUTCOME + DELEGATED POWERS + BOUNDARIES + STOP CONDITIONS.

SOURCE FORMALISM:
[PARAPHRASE]
OpenAI advises developers to name safe local actions and require confirmation for external writes, destructive actions, purchases, or material scope expansion.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
GOAL G does not imply AUTHORIZATION(A). Permission policy filters the action set independently of semantic relevance.

TENSION:
Natural-language permission rules are weaker than enforced capability boundaries; fluent compliance can never substitute for hard controls.

MISSING:
Usable compositional patterns for ordinary users to delegate authority without writing a security policy.

BOUNDARY:
The guidance is model/application practice, not a formal authorization language.

CITATION TRAIL:
[[CALLSHOT-20260817-06]] → authorization envelope → [[CALLSHOT-FIELD-010]] distributed control → [[CALLSHOT-FIELD-014]] orchestration.

TEST:
Run equivalent agent tasks under increasingly explicit authorization policies with identical hard tool permissions. Separate linguistic compliance from enforced capability safety.

PLATFORM:
OpenAI GPT-5.6 · agent permissions · autonomy

LINKS:
[[CALLSHOT-20260817-06]] [[CALLSHOT-FIELD-010]] [[CALLSHOT-FIELD-014]]

BIBTEX:
@misc{OpenAIModelGuidance2026, author={{OpenAI}}, title={Model guidance}, year={2026}, url={https://developers.openai.com/api/docs/guides/latest-model}}
