ZETTEL

ID: FORAGE-WT-001

TITLE: The DAPG: a worldtext is a typed provenance graph with seven node types and nine edge types

SOURCE: worldtext/syntheses/worldtext-formal-engine.md — §II "Graph Model", §V.1 "Directed Acyclic Provenance Graph (DAPG)", §1.2 "Design Principle"

PASSAGE: [QUOTE] "Worldtext is not a database. It is a **runtime** — a repository that executes coherence checks, propagates consequences, maintains provenance, and logs operator behavior. The runtime treats the filesystem as its state store and the LLM session as its execution context." [QUOTE] "N = { Source, Entity, Rule, Trace, Change, Violation, Operator }" ... "E = { extraction, constraint, citation, contradiction, consequence, provenance, threshold, governance, feedback }"

RESEARCH OBJECT: The formal data model of a coherence-preserving world-repository: a directed graph whose node and edge types carry mutability discipline (Source immutable; Trace/Change/Violation append-only; Entity/Rule/Operator mutable).

LOCAL MOVE: The file converts a folkloric practice (keeping a lore wiki) into a typed graph specification, assigning each markdown directory a node type and each cross-reference an edge type — so that "world coherence" becomes a graph property rather than an aesthetic judgment.

SOURCE TERMS: DAPG (Directed Acyclic Provenance Graph); Source/Entity/Rule/Trace/Change/Violation/Operator; extraction/constraint/citation/contradiction/consequence/provenance/threshold/governance/feedback edges; chronicle (append-only trace list); inverted term index.

WHAT BECAME STRANGE: The Operator is a first-class node in the world graph — the human is data inside the artifact they maintain, with tracked "vocabulary, query history, audit results." The world models its own author.

QUESTION: Can a fiction repository's coherence really be reduced to reachability and typing constraints on a graph, or does the graph only index coherence that lives elsewhere (in the operator's theory)?

DEEPER QUESTION: If provenance edges make every entity trace to immutable evidence, what is the ontological status of a deliberately invented (fictional) entity — is invention itself a Source node, and does the DAPG then collapse the fact/fiction distinction into a single provenance discipline?

MECHANISM: Filesystem-as-state-store: directories map to node types (evidence/ → Source, entities/ → Entity, distinctions/+rituals/ → Rule, conflicts/ → contradiction edges, thresholds/ → threshold edges, chronicle.md → append-only Trace log), with a fourfold index (by_type, by_scale, by_source, by_term).

FORMAL SHIFT: From "world bible as document" to "world as G = (N, E) with typed nodes, typed edges, and per-type mutability constraints."

SOURCE FORMALISM: [QUOTE] "DAPG { nodes: Map<NodeID, Node>; edges: Map<EdgeID, Edge>; index: { by_type: Map<NodeType, Set<NodeID>>; by_scale: Map<Scale, Set<NodeID>>; by_source: Map<SourceID, Set<NodeID>>; by_term: Map<Term, Set<NodeID>> // inverted index }; chronicle: List<Trace> // append-only }". Also INV-4 "∀ source ∈ G.sources : source.content = source.original_content — Evidence is immutable" and INV-5 (traces append-only).

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Mutability as a function μ: NodeType → {immutable, append-only, mutable}; a worldtext is well-formed iff every write operation w on node n satisfies μ(type(n)) ⊒ kind(w). Coherence checking then factors into type-checking (static) plus invariant-checking (dynamic).

TENSION: The name says "Directed Acyclic" but the edge set contains `contradiction` marked "(bidirectional)" and citation/provenance edges that plausibly form cycles with extraction edges (Source→Entity→Source); the acyclicity claim is asserted in the acronym but never proven or enforced by any listed invariant. Rival reading: DAPG is acyclic only over provenance edges, not over the full edge set.

MISSING: No formal semantics for edge composition (does extraction ∘ citation imply provenance?); no account of edge deletion; no definition of SPECIES_ENUM or SCALE_ENUM contents, though INV-7 requires membership in them.

BOUNDARY: The spec covers structure, not meaning: it cannot say what a Rule *means*, only what it must be connected to. §IX concedes natural-language rules "cannot" be formally checked "with current NLP."

CITATION TRAIL: worldtext-formal-engine.md → cites "Lineage Forge — Code/Math Genome (OUTPUT_B_FORMAL_ECHO)" as source; maps onto COSMIC_LAW.md (invariant specification) and prime-prompt.md (runtime bootstrap) in §VI.1.

TEST: Build the graph from the actual repo and check INV-1 through INV-7 mechanically; the file itself predicts ≥95% trail resolution (§VII) — a checkable claim against the current filesystem.

PLATFORM: Markdown filesystem + LLM session (declared); implementable as any property graph store with typed nodes.

LINKS: [[FORAGE-WT-002]], [[FORAGE-WT-003]], [[FORAGE-WT-010]], [[FORAGE-WT-012]]

BIBTEX: @unpublished{worldtext-formal-engine-2026, title={Worldtext Formal Engine — Coherence-Preserving Repository Runtime}, note={worldtext/syntheses/worldtext-formal-engine.md, OPERATION-DESCRIBE repository}, year={2026}, month={apr}}
