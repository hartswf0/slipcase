ZETTEL

ID:
OPS-20260817-008

TITLE:
POML makes the prompt itself a compiled representation with source and rendering separated.

SOURCE:
Microsoft — POML: Prompt Orchestration Markup Language — repository and documentation — accessed August 17, 2026.
https://github.com/microsoft/POML

PASSAGE:
[PARAPHRASE]
POML provides semantic prompt components, external-data elements, a CSS-like styling layer, and templating constructs including variables, loops, and conditionals.

RESEARCH OBJECT:
PROMPT SOURCE CODE IS NOT IDENTICAL TO THE STRING THE MODEL RECEIVES.

LOCAL MOVE:
[[MJ-MARTINA-014-A-A]] treated templates as technologies acting upon the prompt writer.

POML makes another distinction explicit: one can author a structured representation of a prompt and render it into model-facing presentation.

SOURCE TERMS:
“semantic components”
“<role>”
“<task>”
“<example>”
“stylesheet”
“presentation”
“templating”
“variables”
“loops”
“conditionals”

WHAT BECAME STRANGE:
Once a prompt has:

SOURCE REPRESENTATION
TEMPLATE VARIABLES
CONTROL FLOW
DATA BINDINGS
STYLE RULES
RENDERING

the thing colloquially called “the prompt” has split into at least two objects:

the prompt program
and
the prompt instance.

QUESTION:
Which object should be preserved as the true research artifact: rendered prompt, POML source, variable bindings, or all three?

DEEPER QUESTION:
Does prompt programming require the same source/runtime distinction that became fundamental in conventional programming languages?

MECHANISM:
POML structures prompts with semantic markup, data components, presentation styling, and templating. The source is rendered into the format supplied to an LLM.

FORMAL SHIFT:
FROM:
PROMPT = STRING

TO:
PROMPT_SOURCE
+ DATA
+ VARIABLES
+ STYLE
+ RENDERER
→ PROMPT_INSTANCE.

SOURCE FORMALISM:
POML includes semantic components such as:

<role>
<task>
<example>
<document>
<table>
<img>

and templating/style mechanisms including:

{{ variables }}
for
if
<let>
<stylesheet>.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

P_instance =
RENDER(
  P_source,
  ENV,
  DATA,
  STYLE
)

Thus:

P_source ≠ P_instance

and:

same P_source
can generate
many P_instances.

TENSION:
Even if content and presentation are separated in authoring, LLM behavior may remain sensitive to the final rendered formatting.

POML therefore separates layers without making presentation semantically irrelevant.

MISSING:
A provenance standard recording source, renderer version, model-facing rendered prompt, environment bindings, and model version together.

BOUNDARY:
POML structures and renders prompts; it does not make natural-language semantics deterministic.

CITATION TRAIL:
[[MJ-MARTINA-014-A-A]]
→ template acts upon writer
→ POML formalizes structured prompt source
→ source and rendered prompt split
→ prompt artifact acquires compilation provenance
→ forage prompt reproducibility as build provenance.

TEST:
Create one POML source.

Render it through multiple:
styles,
data bindings,
conditional branches,
formatting choices.

Run all rendered instances against the same model snapshot.

Record behavior changes.

Then determine which differences belong to:
semantic source,
bound data,
presentation,
or stochastic execution.

PLATFORM:
POML; LLM prompt orchestration

LINKS:
[[MJ-MARTINA-014-A-A]]
[[MJ-MARTINA-004]]
[[MJ-MARTINA-021-A-A]]

BIBTEX:
@misc{zhang2025poml,
  title = {Prompt Orchestration Markup Language},
  author = {Zhang, Yuge and Chen, Nan and Xu, Jiahang and Yang, Yuqing},
  year = {2025},
  eprint = {2508.13948},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2508.13948}
}
