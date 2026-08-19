ZETTEL

ID: FORAGE-PT-002

TITLE: If logical order is not discovery order, then the *sequence* of a reasoning trace is a genre convention that nonetheless has causal force

SOURCE: PROGRAMS/argue.json — <Initial_Interpretation>, after Gilbert Ryle, "Thinking and Inferring"

PASSAGE: [QUOTE] "Build a system that prevents the category mistake of reading the finished shape of an argument backward into the living activity of thought." [QUOTE] "<person> [comes-to-see] <something> before <person> [can-publicly-state] <why-it-follows>." [QUOTE] "<Ryle> [separates] <inference> from <argument> so that <philosophy_of_mind> [stops-confusing] <logical order> with <psychological discovery>."

RESEARCH OBJECT: Order as an independent variable. An argument is arranged for a reader; a discovery happened in some other order. So the ordering of any reasoning trace carries information about the *genre of arguments*, not about the process that produced the conclusion.

LOCAL MOVE: The theory installs a firewall against retrospective projection — it forbids treating the tidy artifact as a recording.

SOURCE TERMS: category mistake / finished shape / living activity / logical order / psychological discovery / comes-to-see

WHAT BECAME STRANGE: In an autoregressive system the ordered trace is re-read as input at every step. So the genre convention is not inert: the *arrangement* conditions what comes next. The artifact of presentation becomes a cause of the conclusion it purports to justify.

QUESTION: Does the ordering of reasoning steps change the answer distribution independently of the steps' content?

DEEPER QUESTION: If yes, the trace is neither a record nor a decoration but a third thing — a self-addressed arrangement whose rhetorical form does computational work. What is the right name for that?

MECHANISM: <PREMISES SEEN AT ONCE> -> [ARRANGEMENT INTO LINEAR ARGUMENT] -> <ORDERED TEXT> -> [RE-READ AS CONTEXT] -> conditions subsequent tokens -> <CONCLUSION>. The last arrow is absent for a human writing on paper and present for a model.

FORMAL SHIFT: <DISCOVERY> -> <ARRANGED ARGUMENT> -> [SELF-CONDITIONING] -> <ANSWER SHIFTED BY FORM ALONE>

SOURCE FORMALISM: NONE (the theory is a category-mistake detector, not an apparatus).

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Compare P(answer | steps in argued order) with P(answer | same steps permuted) and with P(answer | length-matched filler). Three arms separate content, order, and mere length.

TENSION: READING A: the trace is scratch computation rendered in words; order reflects real dependency and the analogy to written arguments is misleading. READING B: order is conventional, borrowed from the genre of proofs, and its causal force is a stylistic accident with epistemic consequences.

MISSING: Any account of what fixes the order in the first place — dependency, training-corpus convention, or decoding dynamics.

BOUNDARY: Ryle's target is philosophy of mind. He offers no claim about machines; the extension is ours and needs its own evidence.

CITATION TRAIL: Ryle — "Thinking and Inferring" (1953). Chain-of-thought faithfulness; filler-token and pause-token studies. [[FORAGE-PT-021]]

TEST: Three arms, identical steps: argued order / permuted order / equal-length filler. If permutation moves the answer as much as filler does, order is doing no logical work. If permutation moves it more, order has causal force independent of content — and the trace is a self-addressed arrangement.

PLATFORM: [[the-trace-is-an-arrangement]]

LINKS: [[FORAGE-PT-001]] [[FORAGE-PT-019]] [[FORAGE-PT-021]]

BIBTEX: @unpublished{argue_program, title={Inference-Against-Argument Engine}, note={PROGRAMS/argue.json, program theory after Ryle, "Thinking and Inferring"}, year={2026}}
