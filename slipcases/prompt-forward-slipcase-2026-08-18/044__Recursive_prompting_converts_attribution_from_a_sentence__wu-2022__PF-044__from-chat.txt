ZETTEL

ID: PF-044

TITLE:
Recursive prompting converts attribution from a sentence problem into a workflow problem.

SOURCE:
Wu, Terry, and Cai — AI Chains — 2022.

PASSAGE:
[PARAPHRASE] AI Chains decomposes complex tasks into linked model operations in which the output of one step becomes input to another and users can inspect and modify intermediate results.

RESEARCH OBJECT:
Chaining creates causal structure among prompts and outputs.

LOCAL MOVE:
The system externalizes intermediate dependencies so users can debug and control them.

SOURCE TERMS:
AI chains; prompt chaining; intermediate results; transparency; controllability.

WHAT BECAME STRANGE:
Once outputs recursively become inputs, “who wrote the final sentence?” discards most of the causal architecture.

QUESTION:
What is the correct unit of attribution in a chained generative workflow?

DEEPER QUESTION:
Should contribution attach to nodes, edges, graph structure, or interventions on the graph?

MECHANISM:
<prompt₁>
→ <output₁/input₂>
→ [prompt₂ ...]
→ <final artifact>

FORMAL SHIFT:
<task>
→ <chain representation>
→ [execute/edit intermediate states]
→ <result>

SOURCE FORMALISM:
Prompt chain.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
ATTRIBUTION GRAPH = nodes(outputs/prompts) + edges(use/transformation).

TENSION:
Graph complexity can make provenance more accurate but practically unreadable.

MISSING:
A principled compression method.

BOUNDARY:
AI Chains addresses interaction design, not scholarly authorship.

CITATION TRAIL:
PromptChainer; W3C PROV; workflow provenance.

TEST:
Encode a recursive dissertation-generation sequence as a graph and compare attribution judgments against the final text alone.

PLATFORM:
[[Recursive Authorship Graph]]

LINKS:
[[AI Chains]]
[[Recursion]]
[[Workflow Attribution]]

BIBTEX:
@inproceedings{wu2022aichains,
  author={Tongshuang Wu and Michael Terry and Carrie J. Cai},
  title={AI Chains: Transparent and Controllable Human-AI Interaction by Chaining Large Language Model Prompts},
  booktitle={Proceedings of the 2022 CHI Conference on Human Factors in Computing Systems},
  year={2022},
  doi={10.1145/3491102.3517582}
}