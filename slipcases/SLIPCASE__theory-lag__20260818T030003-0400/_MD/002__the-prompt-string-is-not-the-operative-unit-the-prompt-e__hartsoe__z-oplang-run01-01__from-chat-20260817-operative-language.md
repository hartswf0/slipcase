ZETTEL

ID:
Z-OPLANG-RUN01-01

TITLE:
The prompt string is not the operative unit; the prompt-event includes an addressable situation.

SOURCE:
Watson Hartsoe — BETWEEN CODE AND POETRY: Committee notes toward a prompt-forward dissertation — 2026 — §2, “Deixis and ekphrasis.” fileciteturn1file0L67-L94

SOURCE URL:
sandbox:/mnt/data/Pasted%20markdown(20260817-170730).md

PASSAGE:
[PARAPHRASE]
Expressions such as “this,” “that,” “again,” and “the previous style” cannot be interpreted from their words alone. Prompting frequently operates by intervening in an already-existing computational situation whose prior outputs and available referents supply the missing meaning.

RESEARCH OBJECT:
<prompt-event>, rather than <prompt-string>, as the minimum unit of analysis.

A prompt may be radically underdetermined as autonomous text while remaining perfectly usable because the relevant object, history, selection, or state is computationally available for reference.

LOCAL MOVE:
The source introduces deixis to break the assumption that prompts are self-contained textual instructions. It shifts attention from what the expression contains to the situation into which the expression points.

SOURCE TERMS:
“deictic”
“points”
“situation”
“where the speaker stands”
“what has already happened”
“available for reference”
“active context”
“intervention”

WHAT BECAME STRANGE:
The phrase “prompt text” begins to conceal the object of study.

“Again” contains almost no specification of what is to happen again. Yet within an interaction it may be operationally sufficient.

What makes the expression viable is therefore partly outside the expression.

The new variable is not merely <context> in the broad linguistic sense, but <computational addressability>: which elements of the existing situation can the system resolve from a deictic expression?

QUESTION:
What has to become computationally addressable before an underspecified natural-language expression can operate reliably upon an existing machine state?

DEEPER QUESTION:
Is prompting better understood as writing texts for interpretation, or as making symbolic interventions into states that already contain manipulable referents?

MECHANISM:
<interaction-state>
contains <addressable entities>, <history>, and <prior outputs>.

<human>
[produces] <deictic expression>.

<system>
[resolves] <expression> against <interaction-state>.

<resolved reference>
[constrains] <possible transformation>.

<transformation>
[produces] <new interaction-state>.

The meaning-producing machinery therefore spans the expression and its addressable environment.

FORMAL SHIFT:
<PROMPT STRING>
→ <PROMPT + ADDRESSABLE CONTEXT>
→ [RESOLVE REFERENCE]
→ <SITUATED OPERATION>

SOURCE FORMALISM:
NONE.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

<prompt-event> :=
{
  <speaker>,
  <expression>,
  <addressable-context>,
  <interpreter>,
  <available-actions>,
  <generated-consequence>,
  <subsequent-judgment>
}

Viability is partly a function of:

V(e,c,i)

where:
e = expression,
c = computationally addressable context,
i = interpreter.

The same e may be viable under c1 and meaningless under c2.

TENSION:
Ordinary speech is also deictic.

“Put that there” depends on a shared situation without becoming a computational prompt.

Deixis therefore cannot define prompting by itself.

The unresolved difference lies in what kinds of context have been rendered machine-addressable and what consequences may follow once reference succeeds.

MISSING:
A taxonomy of computationally addressable context:
- conversation history,
- selected regions,
- files,
- images,
- interface state,
- tool state,
- world objects,
- hidden system instructions,
- persistent memory.

Also missing is a distinction between context available to the human and context actually available to the interpreter.

BOUNDARY:
The evidence does not show that deixis is unique to prompting.

It does not establish a native prompt grammar.

It establishes only that analyzing the visible prompt string independently of its operative situation can radically misdescribe what the expression does.

CITATION TRAIL:
Karl Bühler — deictic field and demonstrative reference.
Charles J. Fillmore — deixis and frame semantics.
HCI work on direct manipulation and selection-based commands.
Research on conversational grounding and multimodal reference resolution.

TEST:
Hold the expression constant:

“Make this darker.”

Change only what is computationally addressable:
A. no selected object,
B. one selected image,
C. selected region within image,
D. multiple candidate referents,
E. prior conversational referent only.

Measure when the expression remains viable, when clarification becomes necessary, and which contextual structures the system actually uses.

PLATFORM:
[[Operative Language]]

LINKS:
[[Computational Addressability]]
[[Deixis as Interface]]
[[Prompt Event]]

BIBTEX:
@unpublished{hartsoe2026betweencodepoetry,
  author = {Hartsoe, Watson},
  title = {Between Code and Poetry: Committee Notes Toward a Prompt-Forward Dissertation},
  year = {2026},
  note = {Unpublished manuscript supplied by the author}
}
