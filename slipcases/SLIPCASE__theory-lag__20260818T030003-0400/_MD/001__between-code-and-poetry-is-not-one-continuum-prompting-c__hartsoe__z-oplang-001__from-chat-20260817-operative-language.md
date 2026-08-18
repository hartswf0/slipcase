ZETTEL

ID:
Z-OPLANG-001

TITLE:
“Between code and poetry” is not one continuum: prompting combines semantic slack with consequence coupling.

SOURCE:
Watson Hartsoe — BETWEEN CODE AND POETRY: Committee notes toward a prompt-forward dissertation — 2026 — §§12, 21.

SOURCE URL:
sandbox:/mnt/data/Pasted%20markdown(20260817-170730).md

PASSAGE:
[QUOTE]
“A conventional programming language tries to minimize interpretive ambiguity. A prompt language often works through controlled ambiguity.”

[PARAPHRASE]
The manuscript later sharpens the contrast by placing a formally constrained expression such as `x = x + 1` against “Make the house behave as though it remembers everyone who has lived there”: the latter must remain evocatively interpretable while also functioning as an operative specification.

RESEARCH OBJECT:
A two-variable account of operative language:

1. SEMANTIC SLACK — how much of an expression’s realization remains unresolved by the expression itself.
2. CONSEQUENCE COUPLING — how directly interpretation of the expression can alter the reachable states of an operative system.

Prompting becomes theoretically interesting not because it occupies a midpoint between code and poetry, but because it can combine HIGH SEMANTIC SLACK with HIGH CONSEQUENCE COUPLING.

LOCAL MOVE:
The source first refuses the identity claim “prompts are code” and instead argues that prompting pressures the category of computational language. It then identifies “controlled ambiguity” as productive rather than defective. The later code/poetry comparison adds the missing operational fact: an interpretively open phrase can nevertheless be supplied to machinery expected to produce a consequential realization.

SOURCE TERMS:
“controlled ambiguity”
“probabilistic”
“context”
“interpretation”
“formal semantics”
“prompt language”
“code”
“poetry”
“operative specification”
“produce further language, images, actions, programs, or worlds”

WHAT BECAME STRANGE:
“Between” now looks misleading.

It implies a single axis:

<CODE> ←—— <PROMPT> ——→ <POETRY>

But two properties that the metaphor bundles together can vary independently.

Poetry can permit substantial interpretive openness without directly changing computational state.

Formal programs can be tightly consequence-coupled while heavily constraining admissible interpretation.

Generative prompts can occupy the unusual region in which substantial unresolved meaning is delegated to an interpreter while the resulting interpretation is still permitted to reorganize what the system does next.

The interesting object may therefore not be a hybrid genre between two established forms. It may be a previously difficult-to-engineer combination of properties.

QUESTION:
Is the distinctive computational property of prompting not “ambiguity,” but the ability to maintain high semantic slack while remaining strongly coupled to consequential machinery?

DEEPER QUESTION:
What changes historically when systems become capable of converting interpretively underdetermined expressions into actions without requiring humans to formalize most of the missing specification beforehand?

MECHANISM:
<human expression>
contains a partially specified criterion.

The expression leaves multiple dimensions unresolved.

<learned interpreter>
uses context, training, examples, prior state, and affordances to complete enough of the specification to produce a realization.

The realization changes or proposes a new system state.

<human judgment>
accepts, rejects, or corrects that interpretation.

That judgment can then re-enter the system as another underspecified expression.

The mechanism is therefore not merely:

<ambiguous-language>
→ <output>

but:

<partial specification>
→ [interpretive completion]
→ <consequential realization>
→ [judgment]
→ <revised partial specification>

FORMAL SHIFT:
<SYMBOLIC EXPRESSION WITH UNRESOLVED PARAMETERS>
→ <CONTEXT-CONDITIONED REPRESENTATION>
→ [INTERPRET / COMPLETE SPECIFICATION]
→ <ALTERED REACHABLE POSSIBILITY SPACE>

SOURCE FORMALISM:
NONE.
The source supplies the verbal distinction between conventional programming’s attempt to minimize interpretive ambiguity and prompt language’s use of controlled ambiguity, but it does not define measurable axes of semantic slack or consequence coupling.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

S(e,c) = semantic slack of expression e under context c
        = degree to which consequential aspects of realization remain unspecified by e.

K(e,i,s) = consequence coupling of expression e interpreted by system i in state s
          = degree to which interpreting e can alter the system’s reachable future states.

A provisional field:

                         CONSEQUENCE COUPLING
                         LOW              HIGH

SEMANTIC     LOW        literal /        formal program /
SLACK                   descriptive      tightly specified
                        notation         operative notation

             HIGH       poetry /         generative prompt /
                        metaphor         operative natural language


The important claim is not:

PROMPT = HIGH S + HIGH K

as a definition.

It is the weaker research hypothesis:

A major affordance of contemporary prompting is the engineering of symbolic interactions in which S and K can simultaneously remain high.

TENSION:
The distinction immediately faces counterexamples.

Code is not uniformly low-slack: declarative languages, constraint programming, underspecified APIs, tests, configuration systems, and learned components can leave realization open.

Poetry and ordinary speech are not necessarily low-coupling: laws, vows, commands, contracts, ritual utterances, institutional classifications, and human instructions can produce material consequences despite interpretive openness.

Prompts themselves can be highly specified and low-slack.

The two-axis model therefore cannot define “the prompt” by quadrant without reproducing the categorical mistake it was invented to escape.

MISSING:
Operational measures for both variables.

“Semantic slack” currently conflates several different absences:
- unspecified values,
- unspecified procedures,
- lexical ambiguity,
- pragmatic dependence,
- tolerance for variation,
- dependence on learned priors.

“Consequence coupling” also needs decomposition:
- immediacy,
- number of mediators,
- reversibility,
- scope of affected state,
- authority to act,
- probability that interpretation produces the intended consequence.

The missing actor is also <the interpreter>. The same words may have radically different slack and coupling depending on what kind of interpreter receives them.

BOUNDARY:
The evidence does NOT establish that prompts uniquely possess semantic slack or consequence coupling.

It does NOT establish that prompting constitutes a distinct language.

It does NOT establish a clean historical break between formal programs and generative prompts.

It supports a narrower opening: the source’s own “between code and poetry” metaphor can be decomposed into at least two independently variable properties, and contemporary generative systems make one previously unusual combination—interpretive openness plus direct computational consequence—especially visible.

CITATION TRAIL:
1. Revised Report on the Algorithmic Language ALGOL 60 — for a contrasting case in which interpretation is deliberately stabilized by explicit syntax and semantics.
2. Clifford Geertz — “Thick Description: Toward an Interpretive Theory of Culture” — for description whose significance depends upon contextual interpretation rather than geometry or syntax alone.
3. Research on underspecification and declarative/constraint programming — to kill any simple equation of programming with path specification or fully explicit semantics.
4. Pragmatics and speech-act theory — to test whether high-semantic-slack/high-consequence-coupling language long predates generative computation.
5. Generative-model experiments varying prompt explicitness while holding task and model constant.

TEST:
Construct one invariant intended transformation—for example, changing an interactive house so that it “remembers previous occupants.”

Express the same intended transformation through progressively different representational regimes:

A. explicit deterministic code,
B. declarative rules,
C. structured prompt/schema,
D. detailed natural-language prompt,
E. “Make the house remember,”
F. “Again, but make it remember them.”

For each regime measure separately:

1. what information had to be explicitly supplied;
2. what the interpreter had to infer;
3. output variance across repeated executions;
4. dependence on prior context;
5. degree of human correction required;
6. how directly the expression altered reachable system states;
7. whether failures exposed previously tacit criteria.

If semantic slack can increase substantially while consequence coupling remains high, the proposed field gains empirical content.

If the apparent effect disappears once context, interpreter, and affordances are controlled, abandon or subdivide the distinction.

PLATFORM:
[[Operative Language]]

LINKS:
[[Semantic Slack]]
[[Consequence Coupling]]
[[Specification Completion]]

BIBTEX:
@unpublished{hartsoe2026betweencodepoetry,
  author = {Hartsoe, Watson},
  title = {Between Code and Poetry: Committee Notes Toward a Prompt-Forward Dissertation},
  year = {2026},
  note = {Unpublished manuscript supplied by the author}
}
