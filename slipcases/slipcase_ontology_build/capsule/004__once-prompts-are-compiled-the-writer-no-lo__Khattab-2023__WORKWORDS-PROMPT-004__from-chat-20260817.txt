ZETTEL

ID:
WORKWORDS-PROMPT-004

TITLE:
Once prompts are compiled, the writer no longer necessarily writes the words the model receives.

SOURCE:
Omar Khattab et al. — “DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines” — 2023 — arXiv:2310.03714

PASSAGE:
[PARAPHRASE] DSPy rejects long hard-coded prompt templates discovered through trial and error as the primary programming abstraction. Instead, developers specify language-model operations through declarative modules inside text-transformation graphs. A compiler then optimizes the pipeline against a metric, including by constructing demonstrations and prompting strategies.

RESEARCH OBJECT:
PROMPT AS INTERMEDIATE REPRESENTATION.

The human may specify:

what transformation should occur

while a compiler determines:

which actual prompt should cause it.

Prompt authorship and prompt wording separate.

LOCAL MOVE:
Push distant writing one step farther.

The distant writer does not merely write conditions under which text will be generated.

They can write conditions under which the instruction that generates the text will itself be generated.

SOURCE TERMS:
DSPy
declarative modules
compiler
text transformation graphs
prompt templates
metric
self-improving pipelines

WHAT BECAME STRANGE:
The prompt can cease being source text.

It becomes build output.

The thing traditionally treated as the author’s key creative artifact becomes analogous to compiled code that may be regenerated whenever the model, data, examples, or objective changes.

QUESTION:
If the prompt is compiler output, where does prompt authorship move?

DEEPER QUESTION:
Is the durable work the wording, the declarative specification, the evaluation metric, the examples, or the compiler that translates among them?

MECHANISM:
Developer specifies modules and pipeline
→ provides data / examples / metric
→ compiler explores effective realizations
→ optimized prompts or demonstrations are produced
→ pipeline executes.

FORMAL SHIFT:
FROM:

AUTHOR
→ PROMPT
→ MODEL
→ OUTPUT

TO:

AUTHOR
→ DECLARATION + METRIC
→ COMPILER
→ PROMPT
→ MODEL
→ OUTPUT.

SOURCE FORMALISM:
DSPy represents LM pipelines as text-transformation graphs composed of parameterized declarative modules.

Its compiler searches for configurations that optimize a user-specified metric.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Source artifact:

D = declaration.

Compiler:

C(D, examples, metric, model)
→ P*

Execution:

M(P*,x)
→ y.

Thus the human-authored description D and executed prompt P* need not be identical.

TENSION:
Compilation suggests a familiar programming genealogy.

But unlike ordinary compilation, the target artifact can remain natural-language-like, model-dependent, probabilistic, and empirically selected.

This is compilation without a stable machine language.

MISSING:
A provenance model capable of showing:

declaration
→ compiler decisions
→ generated prompt
→ model/version
→ output

without pretending that the generated prompt alone explains the result.

BOUNDARY:
DSPy is a particular programming framework. It demonstrates an architecture for prompt compilation rather than proving that all mature prompt practice will become compiler-mediated.

CITATION TRAIL:
[[DEFAULT-IMAGES-CHI26-B-1]]
→ visible prompt may differ from executed prompt
→ DSPy makes prompt derivation explicit and programmable
→ prompt becomes intermediate representation
→ next edge: compiler theory, build artifacts, source maps, and prompt receipts.

TEST:
Take one declarative DSPy program and compile it against:

two models,
two datasets,
two evaluation metrics.

Diff the resulting prompts.

Ask which artifact remains invariant enough to count as “the work.”

PLATFORM:
DSPy; LLM pipelines.

LINKS:
[[DEFAULT-IMAGES-CHI26-B-1]]

BIBTEX:
@article{Khattab2023DSPy,
  author = {Khattab, Omar and Singhvi, Arnav and Maheshwari, Paridhi and Zhang, Zhiyuan and Santhanam, Keshav and Vardhamanan, Sri and Haq, Saiful and Sharma, Ashutosh and Joshi, Thomas T. and Moazam, Hanna and Miller, Heather and Zaharia, Matei and Potts, Christopher},
  title = {DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines},
  year = {2023},
  url = {https://arxiv.org/abs/2310.03714}
}
