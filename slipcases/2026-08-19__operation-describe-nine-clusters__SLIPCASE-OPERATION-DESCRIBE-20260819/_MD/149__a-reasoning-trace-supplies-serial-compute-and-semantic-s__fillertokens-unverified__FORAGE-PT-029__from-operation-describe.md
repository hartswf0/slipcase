ZETTEL

ID: FORAGE-PT-029

TITLE: A reasoning trace supplies serial compute and semantic scaffolding, and the Rylean critique defeats only the second

SOURCE: Filler-token and pause-token studies in the chain-of-thought literature [UNVERIFIED — specific papers not retrieved in this forage]; read against PROGRAMS/argue.json and its three-arm test

PASSAGE: [PARAPHRASE] The reported pattern in this literature is that inserting semantically empty tokens before an answer can improve performance on some tasks, indicating that additional forward passes do work independently of the content of what is emitted. [QUOTE] argue.json: "<Ryle> [separates] <inference> from <argument> so that <philosophy_of_mind> [stops-confusing] <logical order> with <psychological discovery>"

RESEARCH OBJECT: Two separable functions inside one artifact. Length gives the system more sequential computation. Content gives it a scaffold that conditions the next step. Ryle's argument bites on the second — the *arrangement* is a genre convention, not a record. It has nothing to say about the first, because a human writing on paper gains no extra thinking steps from the paper's length.

LOCAL MOVE: This child splits the parent's single object (the trace) into a compute component and a semantic component, which makes the parent's three-arm test a decomposition rather than a horse race.

SOURCE TERMS: filler tokens / pause tokens / forward passes / chain of thought / logical order / psychological discovery

WHAT BECAME STRANGE: If length alone buys computation, then thinking time is *purchasable* in a way it never was for a writer, and the trace stops being analogous to an argument at all. The disanalogy is not that the machine's trace is less faithful than a human's — it is that the machine's trace is partly a *clock*, and human arguments have no clock component.

QUESTION: For a given task, what fraction of the trace's benefit survives replacement of its content by length-matched filler?

DEEPER QUESTION: If the compute component dominates, then "reasoning" improvements from prompting are a hardware allocation effect wearing an epistemic vocabulary — and the right comparison is not to argument but to giving a person more time.

MECHANISM: <PROMPT> -> [EMIT n TOKENS] -> two effects: (a) n additional forward passes with the same weights, (b) n tokens of content conditioning the distribution -> [ANSWER] . Filler isolates (a); permutation isolates (b).

FORMAL SHIFT: <TRACE> -> <COMPUTE BUDGET + SEMANTIC SCAFFOLD> -> [ABLATE EACH] -> <TWO SEPARATE EFFECT SIZES>

SOURCE FORMALISM: NONE verified in this forage.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] benefit(trace) = B_compute + B_semantic + interaction. Estimate B_compute from length-matched filler, B_semantic from content-preserving permutation, both against a no-trace baseline. Report the ratio per task type. Prediction: B_compute dominates on arithmetic and short-horizon tasks; B_semantic dominates where the trace commits to a decomposition.

TENSION: READING A: the split is real and the two components have different task profiles. READING B: filler gains are artifacts of specific training regimes and vanish with scale, in which case the trace is all scaffold and Ryle's critique applies undiluted.

MISSING: Verified citations for the filler-token results. Any study that decomposes rather than compares. Any account of what "more compute" means when the weights are fixed.

BOUNDARY: Nothing here licenses the claim that trace content is inert. It licenses the claim that content and length are confounded in every existing chain-of-thought comparison.

CITATION TRAIL: [[FORAGE-PT-002]] -> filler/pause-token studies (retrieve and verify) -> the compute/semantics split -> next: adaptive-computation and early-exit architectures, where compute allocation is explicit rather than smuggled through token count.

TEST: Three arms at matched token counts — genuine trace, filler, permuted trace — across four task families. Report B_compute and B_semantic per family. Any family where filler matches the genuine trace is a family where "reasoning" names a clock.

PLATFORM: [[the-trace-is-partly-a-clock]]

LINKS: [[FORAGE-PT-002]] [[FORAGE-PT-031]] [[FORAGE-PT-010]]

BIBTEX: @misc{fillertokens_unverified, title={Filler- and pause-token effects in chain-of-thought prompting}, note={[UNVERIFIED] cluster of results referenced without retrieval; verify before citing}, year={2026}}
