ZETTEL

ID:
SHOT-20260817-01

TITLE:
2026-08-17 — If you want the model to act, name action as the default state.

SOURCE:
Anthropic — “Prompting best practices” — Claude Platform documentation — accessed 2026-08-17.
SOURCE URL: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices

PASSAGE:
[QUOTE]
“For Claude to take action, be more explicit:”

[PARAPHRASE]
Anthropic distinguishes language that invites recommendation from language that directs implementation. Its current guidance recommends explicitly asking the model to implement requested changes and, in agentic contexts, to use available tools to resolve missing details rather than merely speculate about them.

RESEARCH OBJECT:
ACTION MODE AS A PROMPT OPERATOR.

LOCAL MOVE:
[[MJ-2022-001]] described prompting as adversarial description: the practitioner anticipates how the machine may misread the words.

[[MJ-2022-019]] later raised a different practical competence: being able to “talk to an artist just as easily as you could talk to a computer.”

The current-day practice sharpens both.

A prompt can correctly describe the intended state and still fail operationally because the model chooses the wrong mode of participation.

“Analyze this.”
“Tell me how to change this.”
“Change this.”

can refer to nearly the same object while authorizing different behavior.

The emerging pragmatic variable is therefore not only WHAT the utterance means but WHAT KIND OF MOVE the utterance licenses.

SOURCE TERMS:
“take action”
“implement”
“tools”
“missing details”
“explicit”

WHAT BECAME STRANGE:
Imperative language is becoming a control primitive.

The difference between:

DESCRIBE THE SHOT

and

TAKE THE SHOT

may be only a few words, but those words determine whether the model remains in discourse or crosses into state change.

QUESTION:
Which linguistic constructions reliably distinguish analysis, recommendation, preparation, execution, and committed state mutation?

DEEPER QUESTION:
Is agentic prompting producing an emergent mood system for natural-language programming analogous to grammatical moods but tied to computational authority?

MECHANISM:
User supplies desired state.

Model must infer an action mode.

Weakly specified action mode:
→ model may remain representational.

Explicit action mode:
→ model inspects relevant state
→ invokes permitted operations
→ changes artifact or environment
→ verifies consequence.

FORMAL SHIFT:
SEMANTIC REQUEST:

“I want X.”

becomes

SEMANTIC REQUEST
+
OPERATIONAL MOOD:

“Implement X.”

SOURCE FORMALISM:
[PARAPHRASE]

Anthropic's current guidance explicitly distinguishes prompts that tend toward suggestion from prompts that more clearly direct action.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

UTTERANCE
=
CONTENT
+
ACTION MODE

ACTION MODE ∈ {
OBSERVE,
EXPLAIN,
RECOMMEND,
PREPARE,
EXECUTE,
VERIFY
}

The contemporary “shot call” specifies both CONTENT and ACTION MODE.

TENSION:
[[MJ-2022-001]] teaches defensive precision against unintended interpretation.

But stronger imperatives introduce a different failure mode:

UNDEREXECUTION
can become
OVEREXECUTION.

The useful principle is therefore not:

ALWAYS ACT.

It is:

MAKE THE AUTHORIZATION MODE LEGIBLE.

This connects directly to [[SHOT-20260817-06]], where an action can be called without yet being committed.

MISSING:
An empirical lexicon of current operational verbs across models and domains.

We do not yet know whether:

make
build
apply
implement
execute
change
send
publish
commit
run

produce stable differences across systems.

BOUNDARY:
The cited Anthropic guidance is platform-specific and behavior can change across model generations.

The generalized ACTION MODE framework is [OUR FORMALIZATION — NOT SOURCE SYNTAX].

CITATION TRAIL:
[[MJ-2022-001]]
→ ambiguity as execution problem
→ [[MJ-2022-019]]
→ talking to the computer as specialized practice
→ Anthropic current-day action guidance
→ utterance gains operational mood
→ [[SHOT-20260817-06]]
→ proposed action can later split from committed action

TEST:
On 2026-08-17-capable agentic systems, issue the same underlying task with controlled leading verbs:

analyze
suggest
prepare
draft
make
implement
apply
execute
verify

Record:

whether tools are invoked
whether external state changes
whether an artifact is created
whether approval is requested
whether the system stops at explanation.

Use the results to construct a dated OPERATIONAL VERB LEXICON.

PLATFORM:
Claude
Tool-using agents
Coding agents
Computer-use agents

LINKS:
[[MJ-2022-001]]
[[MJ-2022-019]]
[[SHOT-20260817-04]]
[[SHOT-20260817-06]]

BIBTEX:
NONE
