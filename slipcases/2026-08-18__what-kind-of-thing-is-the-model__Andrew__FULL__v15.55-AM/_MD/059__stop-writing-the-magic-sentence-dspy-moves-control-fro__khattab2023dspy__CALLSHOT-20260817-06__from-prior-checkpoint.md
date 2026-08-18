ZETTEL

ID:
CALLSHOT-20260817-06

TITLE:
STOP WRITING THE MAGIC SENTENCE — DSPy moves control from hand-authored prompt strings into declarative modules, examples, metrics, and compilation.

SOURCE:
Omar Khattab et al. — “DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines” — 2023.
https://arxiv.org/abs/2310.03714

PASSAGE:
[PARAPHRASE]
DSPy criticizes LM pipelines built from hard-coded prompt templates discovered by trial and error. It instead represents pipelines as text-transformation graphs composed from declarative modules, then uses a compiler to optimize their parameters, including demonstrations and prompting strategies, against a metric.

RESEARCH OBJECT:
PROMPTING-AS-COMPILATION-TARGET.

LOCAL MOVE:
[[MJ-GC-030-B-B]] showed that changing the representation of a task can change whether generated code succeeds.

DSPy asks:

why should the human manually discover that representation at all?

The practitioner specifies:

WHAT GOES IN.
WHAT MUST COME OUT.
HOW MODULES CONNECT.
HOW SUCCESS IS SCORED.

Then a compiler searches for effective prompt-level implementation.

SOURCE TERMS:
“hard-coded prompt templates”
“trial and error”
“text transformation graphs”
“declarative modules”
“compiler”
“maximize a given metric”

WHAT BECAME STRANGE:
The prompt can stop being source code.

It becomes compiled residue.

A system may contain prompts everywhere while the practitioner writes almost none of them directly.

QUESTION:
Which parts of today’s prompt craft should become compiler responsibilities rather than human-authored prose?

DEEPER QUESTION:
If prompts are optimized intermediate representations, is “prompt engineering” analogous to hand-writing assembly before a compiler ecosystem has matured?

MECHANISM:
DECLARE MODULE SIGNATURES
→ compose pipeline
→ provide metric / examples
→ compiler proposes/selects demonstrations and prompting parameters
→ evaluate
→ retain stronger configuration.

FORMAL SHIFT:
FROM:
HUMAN
→ PROMPT STRING
→ MODEL.

TO:
HUMAN
→ DECLARATIVE PROGRAM + METRIC
→ COMPILER
→ PROMPTS / DEMOS / PARAMETERS
→ MODEL PIPELINE.

SOURCE FORMALISM:
DSPy represents LM pipelines as imperative text-transformation graphs whose LM calls are declarative modules and introduces compilation to optimize a pipeline against a metric.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

SOURCE PROGRAM:
{
SIGNATURES,
MODULE GRAPH,
METRIC,
EXAMPLES
}.

COMPILE
→ {
INSTRUCTIONS,
DEMONSTRATIONS,
PROMPT PARAMETERS
}.

The prompt becomes an implementation detail.

TENSION:
Automatic optimization can improve measured performance while producing prompts that are less interpretable or whose behavior overfits the evaluation metric.

MISSING:
Which prompt properties should remain deliberately authored because they express commitments not reducible to benchmark performance.

BOUNDARY:
DSPy does not eliminate prompting; it relocates much of prompt construction into an optimization process.

CITATION TRAIL:
[[MJ-GC-030-B-B]]
→ specification wording is causally active
→ DSPy
→ stop manually tuning wording
→ compile declarative intent into prompt implementations.

TEST:
Take a hand-tuned prompt workflow.

Rewrite only:
INPUT/OUTPUT SIGNATURES,
MODULE CONNECTIONS,
SUCCESS METRIC.

Let an optimizer select demonstrations/instructions.

Compare:
performance,
human labor,
legibility,
transfer across model changes.

PLATFORM:
DSPy / LM programming

LINKS:
[[MJ-GC-030-B-B]]
[[MJ-GC-030-B-A]]
[[CALLSHOT-20260817-05]]

BIBTEX:
@article{khattab2023dspy,
  title={DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines},
  author={Khattab, Omar and Singhvi, Arnav and Maheshwari, Paridhi and Zhang, Zhiyuan and Santhanam, Keshav and Vardhamanan, Sri and Haq, Saiful and Sharma, Ashutosh and Joshi, Thomas T. and Moazam, Hanna and Miller, Heather and Zaharia, Matei and Potts, Christopher},
  journal={arXiv preprint arXiv:2310.03714},
  year={2023},
  url={https://arxiv.org/abs/2310.03714}
}
