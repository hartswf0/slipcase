ZETTEL

ID: FORAGE-PA-006

TITLE: Breakdown reveals the structure of use: the broken hammer as design principle

SOURCE: PAPERS/winnograd.md, sections 1–2 ("The old dream: computation as mind"; "Heidegger's broken hammer and the visibility of design")

PASSAGE: [QUOTE] "The hammer breaks. It is too heavy, missing, awkward, misplaced. Suddenly the smooth activity is interrupted. The tool appears as an object of attention. The world that supported the action becomes visible as a network of dependencies. Breakdown is not an accident outside use; it is the moment that reveals the structure of use." And: [QUOTE] "the designer's real archive is not the ideal workflow but the breakdown log: the missed handoff, the failed interpretation, the ambiguous request, the unkept promise, the hidden dependency, the moment when the tool stops disappearing and becomes a problem."

RESEARCH OBJECT: Winograd & Flores's transposition of Heidegger's ready-to-hand/present-at-hand distinction into a design principle: tools are meaningful by withdrawing into practice; systems must be evaluated by how they participate in practices and how they surface, survive, and repair breakdown. Framed against the cognitivist ontology the book attacks: [QUOTE] "To think was to manipulate symbols. To know was to possess an adequate representation. To act was to execute a plan."

LOCAL MOVE: Converts phenomenology into method: "Design, then, is not decoration laid over computation. Design is applied ontology. It decides what kind of world the user is assumed to inhabit." The dangerous question "Can computers think?" is replaced by "what has to be forgotten about human life in order for that question to appear natural?" (forgetting embodiment, history, social obligation, thrownness, breakdown).

SOURCE TERMS: breakdown; ready-to-hand / present-at-hand; thrownness (via the forgetting list); applied ontology; breakdown log; situated action (Suchman); interaction grammar of repair

WHAT BECAME STRANGE: The interface — "not a neutral surface between user and machine" but "a practical field where certain actions become available... A system always carries a theory of the user."

QUESTION: What would an actual breakdown log look like as a first-class design artifact — schema, retention, who reads it — rather than as buried support tickets?

DEEPER QUESTION: If breakdown is the revelation of use-structure, do generative AI systems that smooth over their own failures (fluent wrong answers, silent recoveries) systematically destroy the one signal design needs — and is "designing for breakdown" (principle 3 of section 9) therefore anti-correlated with model quality as currently measured?

MECHANISM: Absorbed coping renders equipment invisible → interruption (missing/broken/awkward tool) forces present-at-hand attention → dependency network becomes inspectable → design intervenes at the revealed structure → repair restores (modified) transparency. Suchman's extension: systems designed around plans rather than situated action "blame users for not conforming to the system's model" and "make invisible work disappear."

FORMAL SHIFT: Evaluation unit shifts from task-completion in an idealized workflow to the breakdown-repair cycle in a lived practice; error moves from edge case to "first-class design condition."

SOURCE FORMALISM: NONE (Heidegger's distinction used as inherited conceptual machinery; no notation).

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Practice state ∈ {transparent, broken, repairing}; a design D is evaluated by (i) what its breakdowns reveal (info gain at transparent→broken), (ii) available repair verbs (broken→repairing transitions the interface itself affords), (iii) who bears repair cost. Cognitivist design optimizes only the transparent state.

TENSION: cyber-00.md/cyber-02.md reach a nearly identical prescription (expose the cut, design for correction) from Barad/cybernetics rather than Heidegger/Austin — convergent ethics, rival ontologies (entanglement vs thrownness). Bush's memex test (van.md) is the scholarship-specific case: pathless synthesis is breakdown rendered invisible.

MISSING: The book's own famous failure case — The Coordinator software and the critique that speech-act workflow tools bureaucratize communication — is named as "the central design wound" but not analyzed in depth.

BOUNDARY: The paper flags the limit itself: "Not every utterance wants to become a ticket... language is action, but action cannot be exhausted by a schema."

CITATION TRAIL: Winograd & Flores, *Understanding Computers and Cognition* (1986); Heidegger, *Being and Time* (ready-to-hand); Austin (speech acts); Maturana & Varela (autopoiesis); Dreyfus (expertise critique); Suchman (plans and situated actions); Dourish (implicitly, embodied interaction).

TEST: Instrument a working tool with a breakdown log; compare redesigns driven by breakdown-log analysis vs ideal-workflow analytics on repair time and misattributed user blame.

PLATFORM: Any interactive system; explicitly extended to AI assistants, calendars, collaborative editors in the source.

LINKS: [[FORAGE-PA-007]], [[FORAGE-PA-013]], [[FORAGE-PA-009]]

BIBTEX: @book{winograd1986understanding, author={Winograd, Terry and Flores, Fernando}, title={Understanding Computers and Cognition: A New Foundation for Design}, publisher={Ablex}, year={1986}, note={PAPERS/winnograd.md is an unattributed chapter about this book}}
