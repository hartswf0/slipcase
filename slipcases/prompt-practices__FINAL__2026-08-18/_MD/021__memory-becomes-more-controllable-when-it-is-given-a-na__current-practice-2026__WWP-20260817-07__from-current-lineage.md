ZETTEL

ID:
WWP-20260817-07

TITLE:
Memory becomes more controllable when it is given a name the model must carry.

SOURCE:
David Soria Parra and Den Delimarsky — “The 2026-07-28 Specification” — Model Context Protocol Blog — July 28, 2026 — https://blog.modelcontextprotocol.io/posts/2026-07-28/

PASSAGE:
[QUOTE] “the model can see the handle and thread it between tools.”

RESEARCH OBJECT:
The MCP design makes application state addressable through explicit handles passed as tool arguments. State can become more controllable when it ceases being invisible continuity and becomes an explicit object in the model’s manipulable world.

LOCAL MOVE:
Replace IMPLICIT SESSION MEMORY with ADDRESSABLE STATE OBJECTS.

SOURCE TERMS:
stateless protocol; handle; tool argument; request; state; multi round-trip requests; input_required; self-describing

WHAT BECAME STRANGE:
A tiny identifier can carry more durable continuity than thousands of remembered words. Language gains an operation of REFERENCE: words can point into persistent computational memory.

QUESTION:
When should a prompt carry state itself, and when should it carry stable references to state stored elsewhere?

DEEPER QUESTION:
Could future prompting increasingly consist of handles, IDs, links, schemas, selectors, and references rather than descriptive prose?

MECHANISM:
REQUEST1 → operation creates state → HANDLE h → later request contains h → server resolves h → state recovered/transformed.

FORMAL SHIFT:
STATE=hidden session continuity becomes STATE=EXPLICIT REFERENCE → RESOLVABLE OBJECT.

SOURCE FORMALISM:
The MCP specification update uses a stateless protocol core while allowing applications to mint explicit handles and pass them as later tool arguments.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
HANDLE h := ADDRESS(S); prompts can preserve h rather than serialize S; ZETTEL_ID/SOURCE_ID/TEST_ID can become computational handles.

TENSION:
Explicit IDs make lineage addressable and machine-operable, but the more meaning is dereferenced elsewhere, the less self-contained the linguistic artifact becomes.

MISSING:
A grammar for reference integrity when handles point to changed, deleted, forked, unauthorized, or obsolete state.

BOUNDARY:
MCP handles are an application-state mechanism; applying them to zettel lineage is [OUR FORMALIZATION — NOT SOURCE SYNTAX].

CITATION TRAIL:
[[SCGAI-008]] → provenance → [[SCGAI-003]] → histories → MCP explicit handles → identifiers as operational words.

TEST:
Implement a recursive research workflow with inline serialized state versus immutable external IDs; compare context size, lineage errors, recovery, branching, and auditability.

PLATFORM:
Model Context Protocol / agent architectures / recursive research systems

LINKS:
[[SCGAI-008]]
[[SCGAI-003]]

BIBTEX:
@misc{soriaparra2026mcp, author={Soria Parra, David and Delimarsky, Den}, title={The 2026-07-28 Specification}, organization={Model Context Protocol}, year={2026}, url={https://blog.modelcontextprotocol.io/posts/2026-07-28/}}
