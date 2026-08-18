ZETTEL

ID:
PROMPT-ONTOLOGY-001

TITLE:
A prompt ontology can classify the inscription before it establishes the identity of the operative object.

SOURCE:
Victoria Basmov, Yoav Goldberg, and Reut Tsarfaty — “Prompts in the Wild: A Large Analyzed Collection of Transactional Prompts in Code” — LAW XX — 2026 — SOURCE URL: https://aclanthology.org/2026.law-main.19/

PASSAGE:
[PARAPHRASE] Basmov et al. argue that prompts are linguistic objects worthy of scientific study, collect 57.5K transactional prompts from GitHub, and introduce an ontology of prompt properties and formal/semantic components. In describing “inherent prompt properties,” they include that prompts are texts written in a language, formulate a task, and serve to elicit output. Their corpus represents prompts as role-message sequences whose text is further decomposed into instructions.

RESEARCH OBJECT:
The source secures a rich LINGUISTIC ONTOLOGY of transactional prompt inscriptions. It does not by itself secure an OPERATIONAL ONTOLOGY of the causal object that produced a model behavior.

LOCAL MOVE:
Split WHAT IS WRITTEN from WHAT ACTED.

SOURCE TERMS:
linguistic objects
transactional prompts
prompt ontology
role-messages
instructions
first-order objects
programming language

WHAT BECAME STRANGE:
The paper sets out to establish prompts as first-order scientific objects precisely by adding structure to recoverable texts. Yet recoverability may be why the text is available as an object, not evidence that the text exhausts the operative unit.

QUESTION:
When does a linguistic ontology of prompts license causal claims about model behavior, and when does it only describe the inscriptions developers store?

DEEPER QUESTION:
Has prompt research mistaken the easiest layer to archive for the layer at which the system’s operative instruction has identity?

MECHANISM:
Source code exposes strings and role-message structures. Static analysis recovers them. Ontological annotation stabilizes them as rows, components, and features. Downstream behavior, however, can depend on runtime variables not contained in that recovered inscription.

FORMAL SHIFT:
FROM:
PROMPT = STRUCTURED TEXTUAL OBJECT

TO:
PROMPT-TEXT = STRUCTURED TEXTUAL OBJECT
while
OPERATIVE CONTROL = UNRESOLVED.

SOURCE FORMALISM:
The source’s ontology organizes prompt features including language, task/domain, input characteristics, output characteristics, role-message structure, and semantic kinds of instructions.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let T be the recoverable prompt inscription and E the execution event.

Ontology O(T) can be well-defined even when causal identity I(E) is not.

O(T) ≠ proof that T is the sufficient causal unit of E.

TENSION:
The source’s linguistic-object framing is methodologically productive and explicitly scoped; the stronger causal reading is not required for its dataset to be valuable. The tension arises when prompt scholarship moves from “we can structure this inscription” to “this inscription is the object that directly shaped the behavior.”

MISSING:
Runtime context, hidden instructions, rewriting, retrieved material, model version, tool schemas, stochastic state, and post-generation selection are not contained by a text-only identity condition.

BOUNDARY:
This zettel does not claim Basmov et al. confuse linguistic and causal ontology. It identifies a boundary their deliberately linguistic ontology makes visible.

CITATION TRAIL:
[[WORKWORDS-PROMPT-001]]
→ prompts as programs
→ Basmov et al. establish prompts as linguistic first-order objects
→ objecthood itself becomes the live question
→ what conditions make a prompt the same operative object across executions?

TEST:
Take a sample of transactional prompts with identical recovered text and execute them across controlled changes to system instructions, model versions, retrieval, tools, and stochastic conditions. Measure which behavioral properties remain invariant. Compare textual identity with operational invariance.

PLATFORM:
LAW 2026; GitHub transactional prompts; LLM software.

LINKS:
[[WORKWORDS-PROMPT-001]] [[WORKWORDS-PROMPT-008]]

BIBTEX:
@inproceedings{Basmov2026PromptsWild,
  title={Prompts in the Wild: A Large Analyzed Collection of Transactional Prompts in Code},
  author={Basmov, Victoria and Goldberg, Yoav and Tsarfaty, Reut},
  booktitle={Proceedings of the 20th Linguistic Annotation Workshop (LAW XX)},
  pages={257--308},
  year={2026},
  doi={10.18653/v1/2026.law-main.19},
  url={https://aclanthology.org/2026.law-main.19/}
}
