ZETTEL

ID:
PROMPT-ONTOLOGY-003

TITLE:
Context engineering admits that the prompt has evaporated, then tries to stabilize a larger object.

SOURCE:
Lingrui Mei et al. — “A Survey of Context Engineering for Large Language Models” — 2025 — SOURCE URL: https://arxiv.org/abs/2507.13334

PASSAGE:
[PARAPHRASE] Mei et al. argue that modern LLM systems no longer operate on a single static string. They formalize the historical prompt-engineering view as context C equal to a monolithic prompt, then replace it with a dynamically structured set of contextual components assembled, retrieved, selected, processed, and managed by system-level functions.

RESEARCH OBJECT:
CONTEXT ENGINEERING AS BOTH CORRECTION AND SYMPTOM.

It correctly demonstrates that PROMPT-AS-STATIC-STRING is inadequate for contemporary systems. Yet the repair expands the causal object toward system-level execution conditions.

LOCAL MOVE:
Do not treat “context” as the solution. Ask whether enlarging the noun solves identity or merely moves its boundary.

SOURCE TERMS:
context engineering
dynamic structured information
assembly function
context retrieval
context processing
context management
stateful

WHAT BECAME STRANGE:
The prompt disappears by becoming context. Context then expands to include memory, retrieval, tools, multimodal inputs, state, and orchestration. The object becomes more causally plausible and less bounded.

QUESTION:
At what point does context engineering stop describing an input and begin describing the execution system itself?

DEEPER QUESTION:
Can a generative control object be both bounded enough to version and rich enough to be causally adequate?

MECHANISM:
Modern systems dynamically assemble multiple information sources into a context before inference. System performance is conditioned on this assembled state, not on one user-authored string alone.

FORMAL SHIFT:
FROM:
C = prompt

TO:
C = {c1, c2, …, cn}
assembled by system functions

THEN PRESSURE:
What belongs to C, and what remains a condition of C’s interpretation?

SOURCE FORMALISM:
The source writes autoregressive generation as Pθ(Y|C) and explicitly contrasts historical C = prompt with a dynamically structured context assembled from components.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

As causal coverage K(C) increases by absorbing consequential variables, boundedness B(C) may decrease.

The unresolved problem is not simply maximizing K. It is specifying identity conditions under changing C.

TENSION:
Context engineering offers a practical system abstraction and does not claim to be a metaphysical ontology. Yet its expansion demonstrates why “prompt” cannot simply be rescued by adding more context fields.

MISSING:
A principled stopping rule for what belongs to the operative control object versus the surrounding execution environment.

BOUNDARY:
The source is a survey and formal framework for context engineering. The boundedness–causality tension is our inference from its scope expansion.

CITATION TRAIL:
[[DEFAULT-IMAGES-CHI26-B-1]]
→ visible prompt may differ from executed input
→ context engineering rejects static-string prompt model
→ control object expands toward whole system
→ prompt ontology becomes boundary problem.

TEST:
Construct nested execution records of increasing thickness: visible text; role messages; full context; context plus tools; plus model/version; plus sampling state; plus selection. Measure how much behavioral variance each added layer explains and where “same prompt” judgments cease to be useful.

PLATFORM:
LLM systems; context engineering; RAG; memory; agents.

LINKS:
[[DEFAULT-IMAGES-CHI26-B-1]] [[WORKWORDS-PROMPT-004]]

BIBTEX:
@article{Mei2025ContextEngineering,
  title={A Survey of Context Engineering for Large Language Models},
  author={Mei, Lingrui and Yao, Jiayu and Ge, Yuyao and others},
  journal={arXiv preprint arXiv:2507.13334},
  year={2025},
  url={https://arxiv.org/abs/2507.13334}
}
