ZETTEL

ID: FORAGE-PA-009

TITLE: Bateson's circuit at the prompt box: the loop learns even when no weights update — but is the user playing against the program or functioning for it?

SOURCE: PAPERS/cyber-00.md sections 3, 5 ("Bateson: Mind Is the Circuit, Not the Skull"; "Flusser and the Apparatus") and PAPERS/cyber-02.md sections 3, 5

PASSAGE: [QUOTE, cyber-00] "The prompt is a difference. The output is a difference. The surprise is a difference. The revision is a difference. The generated image becomes a perceptual perturbation. The user's next idea is shaped by the perturbation. The circuit learns, even if no model weights are updated." [QUOTE, cyber-02] "The 'mind' of generative AI, if the term is to be used at all, is not in the weights alone. It is in the circuit completed by the user." [QUOTE, cyber-00] "Flusser's question returns with new force: **Are users playing against the apparatus, or merely functioning for it?**"

RESEARCH OBJECT: The relocation of cognition from model to loop, via Bateson's cane example ("The cane, hand, nervous system, ground, and environment form a circuit"; mind = "the pathway of difference that makes a difference"), fused with Flusser's camera-apparatus: the model as "a program of possibilities" the user plays against, with the standing danger of becoming a "functionary... endlessly realizing possibilities already contained within the program while imagining themselves free."

LOCAL MOVE: Dissolves the "does the model have a mind?" debate as a container error: [QUOTE, cyber-00] "many debates about AI cognition remain trapped in the wrong container... Bateson would ask a different question: What is the larger circuit in which this system participates, and what differences does it transmit?" And flips the risk register: "The danger is not that AI becomes intelligent in isolation. The danger is that human-AI circuits become stupid, rigid, addictive, extractive, or destructive while still appearing intelligent at the surface."

SOURCE TERMS: ecology of mind; difference that makes a difference; completed circuit; schismogenesis; apparatus; program; functionary; technical images; computational mannerism; apparatus literacy; black-box aesthetics

WHAT BECAME STRANGE: Learning without training — user adaptation, prompt folk-knowledge, style stabilization, and community templates constitute circuit-level learning invisible to any model-centric analysis ("Even when model weights are fixed, the human-system ecology changes. Users adapt to the apparatus. The apparatus adapts the user." — cyber-02). Also style: "The model produces the look of significance without the world that made the sign significant" (cyber-00 on computational mannerism).

QUESTION: What are the observables of circuit-level learning (prompt-genre convergence, regeneration rates, vocabulary drift), and can they be measured independently of model metrics?

DEEPER QUESTION: Is there a principled boundary between playing-against and functioning-for — or does the apparatus absorb every counter-move as one more realized possibility, making Flusserian freedom undecidable from inside the loop?

MECHANISM: Prompt → generation → surprise/disappointment → revision → new generation; differences propagate around the loop and sediment as user habit, community template, and interface default. The apparatus structures "ease and difficulty governing appearance" ("The politics of AI images lies not only in what appears, but in the structure of ease and difficulty governing appearance"). Pathology mode (Bateson): the loop optimizes a local metric while degrading the ecology that gives the metric meaning (cyber-02: "AI ethics often asks whether the machine did the right thing. Cybernetic ethics asks whether the loop remains viable.").

FORMAL SHIFT: Unit of analysis moves from model to human-machine-environment loop; "AI creativity," agency, and responsibility become circuit properties — "distributed, but not dissolved" — to be traced and reassigned, not located.

SOURCE FORMALISM: Bateson's difference/circuit vocabulary; Flusser's apparatus/program/functionary triad; no notation in either paper.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Loop state x_t = ⟨user-model of apparatus, apparatus defaults, artifact⟩; update x_{t+1} = f(x_t, surprise_t) with weights frozen inside f. Circuit-learning = drift in user-model and defaults; functionary condition = trajectory confined to high-probability region of the program's possibility space; playing-against = policy that increases reachable-set entropy (von Foerster's imperative operationalized).

TENSION: cyber-03.md re-derives the same loop as RITUAL ("archive → symbolic invocation → model operation → artifact → interpretation → feedback → revised invocation") — the Bateson framing makes the loop cognitive, the Geertz framing makes it symbolic; whether the primitive is information or meaning is exactly what the two papers don't settle between them. calvino.md would call the functionary the writer who forgets the machine's constraints are inherited.

MISSING: Any account of when weight updates DO re-enter the loop (RLHF on usage data, fine-tuning on generated outputs) — the strongest version of the circuit claim, where user adaptation literally becomes model gradient, is untouched.

BOUNDARY: The circuit claim explicitly does not attribute human-sense mind to the model ("not because the model alone has a mind in the human sense"); it is a unit-of-analysis claim, not a consciousness claim.

CITATION TRAIL: Bateson, *Steps to an Ecology of Mind* (blind man's cane; difference that makes a difference; schismogenesis); Flusser, *Towards a Philosophy of Photography* (apparatus, functionary, technical images); von Foerster (ethical imperative); Beer (requisite variety); Deleuze (modulation, dividual — the control-society framing of the same loop in cyber-00 section 6).

TEST: Longitudinal prompt-log study with frozen model weights: measure convergence of user prompt-genres and reachable-output diversity over sessions; circuit-learning predicts genre convergence; functionary-condition predicts shrinking output entropy despite growing user confidence.

PLATFORM: Text-to-image communities (prompt recipes, style tags), chat LLMs with fixed checkpoints.

LINKS: [[FORAGE-PA-008]], [[FORAGE-PA-011]], [[FORAGE-PA-004]], [[FORAGE-PA-006]]

BIBTEX: @book{bateson1972steps, author={Bateson, Gregory}, title={Steps to an Ecology of Mind}, publisher={Ballantine}, year={1972}} @book{flusser1983philosophy, author={Flusser, Vil{\'e}m}, title={Towards a Philosophy of Photography}, publisher={Reaktion Books}, year={2000}, note={orig. 1983}} % cyber-00.md/cyber-02.md unattributed essays in repo.
