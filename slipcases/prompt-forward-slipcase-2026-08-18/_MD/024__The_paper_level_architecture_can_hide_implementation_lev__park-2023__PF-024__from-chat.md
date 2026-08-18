ZETTEL

ID: PF-024

TITLE:
The paper-level architecture can hide implementation-level prompt machinery.

SOURCE:
Park et al. — Generative Agents: Interactive Simulacra of Human Behavior — 2023.

PASSAGE:
[PARAPHRASE] The generative-agent architecture is presented through memory, reflection, planning, retrieval, and behavior, with ablations showing that major architectural components matter to performance.

RESEARCH OBJECT:
Scholarly architecture may be described one level above the prompts that instantiate it.

LOCAL MOVE:
The paper foregrounds functional modules; repository implementation contains prompt machinery underneath them.

SOURCE TERMS:
memory stream; reflection; planning; retrieval; generative agents.

WHAT BECAME STRANGE:
A prompt may be indispensable implementation while remaining nearly invisible in the conceptual vocabulary of the paper.

QUESTION:
At what abstraction level should prompt work receive scholarly description?

DEEPER QUESTION:
When is a prompt merely implementation detail, and when is it the actual mechanism of a claimed contribution?

MECHANISM:
<architectural concept>
→ <prompt-based implementation>
→ [model execution]
→ <agent capability>

FORMAL SHIFT:
NONE

SOURCE FORMALISM:
Memory/reflection/planning architecture plus component ablations.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
CONCEPTUAL MODULE → PROMPT IMPLEMENTATION → BEHAVIOR.

TENSION:
Treating every implementation prompt as a core scholarly object would flatten useful abstraction.

MISSING:
Criteria distinguishing incidental prompt wording from load-bearing prompt mechanism.

BOUNDARY:
The paper's architectural claims cannot be reduced to prompt text alone.

CITATION TRAIL:
Generative Agents code; DSPy; program synthesis; implementation studies.

TEST:
Trace one published architectural claim down to the exact prompts and code paths that realize it.

PLATFORM:
[[Where the Prompt Disappears]]

LINKS:
[[Architecture]]
[[Implementation]]
[[Abstraction Level]]

BIBTEX:
@inproceedings{park2023generative,
  author={Joon Sung Park and Joseph C. O'Brien and Carrie J. Cai and Meredith Ringel Morris and Percy Liang and Michael S. Bernstein},
  title={Generative Agents: Interactive Simulacra of Human Behavior},
  booktitle={Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology},
  year={2023}
}