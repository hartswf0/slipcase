ZETTEL

ID:
FORAGE-OD-002

TITLE:
THE MEASURE THE ARCHIVE LACKS ALREADY EXISTS AS A SINGLE DIRECTION IN ACTIVATION SPACE

SOURCE:
Zekun Wu, Ze Wang, Seonglae Cho, Yufei Yang, Adriano Koshiyama, Sahan Bulathwela, Maria Perez-Ortiz — Tool Calling is Linearly Readable and Steerable in Language Models — arXiv:2605.07990 — 2026 (submitted 8 May 2026, revised 25 May 2026)

PASSAGE:
[QUOTE]
"a single direction in activation space, one direction per pair of tools"

[QUOTE]
"arguments that follow automatically adapt to the new tool's schema, so flipping the name is enough."

[PARAPHRASE]
Adding the identified direction switches the model's tool choice at 83–100% accuracy on larger models.

RESEARCH OBJECT:
For the archive's primary case, routing is not a diffuse semantic effect. It is displacement along a low-dimensional, linearly readable discrimination direction between two candidate actions.

That gives ΔG a geometry, a unit, and a sign.

LOCAL MOVE:
Wu et al. are not doing media theory. They are locating where in the network the choice between two tools is decided, and showing that the decision surface is linear enough to be read off and pushed.

The move converts "the description routed the action" from an interpretive claim into a measurable projection.

SOURCE TERMS:
tool calling
linearly readable
steerable
single direction in activation space
one direction per pair of tools
schema adaptation
flipping the name

WHAT BECAME STRANGE:
The archive spent its formal effort on the operator's action-space, which it could not measure, while the measurable object was the *pairwise discrimination direction* — a thing that exists only relative to a rival action.

Operativity may be irreducibly comparative: there is no ΔG of a description, only ΔG of a description with respect to a specific alternative route.

QUESTION:
If the routing decision is one direction per *pair* of tools, is operative description definable at all without naming the foreclosed alternative?

DEEPER QUESTION:
Does this dissolve the archive's ambition to define operativity as a property of a description, replacing it with operativity as a property of a contrast set?

MECHANISM:
<TOOL SCHEMA TEXT>
→ tokenized into context
→ activations at some layer ℓ
→ [PROJECTION ONTO DIRECTION v_{i,j} SEPARATING TOOL i FROM TOOL j]
→ scalar margin
→ readout selects the tool
→ <TOOL CALL>

Intervening on the projection changes the call. Therefore the projection is the route.

FORMAL SHIFT:
<DESCRIPTION>
→ <ACTIVATION VECTOR>
→ [PROJECTION ONTO PAIRWISE DIRECTION]
→ <SCALAR MARGIN>
→ <SELECTED ACTION>

SOURCE FORMALISM:
The paper's machinery is a linear probe / steering-vector construction: a direction v in activation space, per tool pair, whose addition flips selection. Reported switch accuracy 83–100% on larger models.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

ΔG_{i,j}(D) = ⟨ h(context + D) − h(context) , v_{i,j} ⟩

where h is the activation at the readout-relevant layer and v_{i,j} the pairwise direction.

Consequences the archive did not have:
1. ΔG has a sign. Descriptions can route *away* from the intended action.
2. ΔG is defined only relative to a contrast pair.
3. ΔG = 0 becomes a real, checkable orthogonality condition: the description moved the activation, but not along the direction that decides anything.

That third case is the archive's missing category: a description that changes the state without changing the route.

TENSION:
The archive wants operativity to be a semantic/cultural property of description. Wu et al. locate it in a geometric property of activations. Whether these are the same phenomenon under two descriptions, or two different phenomena sharing a word, is undecided.

MISSING:
Whether the pairwise-direction result holds for the archive's non-tool cases: text-to-image prompts, GitHub labels, moderation thresholds. There is no reason to assume the same linear structure outside function calling.

BOUNDARY:
The paper licenses claims about tool *selection* in transformer LMs. It does not license claims about human operators, about image generation, or about institutional routing. Importing it as a general theory of description would repeat the archive's own warning that formal resemblance is not genealogy.

CITATION TRAIL:
Steering vectors / representation engineering literature.
Linear probing of concepts in LMs.
PAPERS/attention-tax-semiotics.md §14 (the formalism this replaces).
FORAGE-OD-010 (readout as the real bottleneck).

TEST:
Run the archive's own primary experiment, but log activations. Vary only the tool description. Measure both (a) invocation rate and (b) projection onto v_{i,j}.

If descriptions move activations but not the projection, the archive has found its own negative case with a mechanism attached — the first non-arbitrary ΔG = 0.

PLATFORM:
[[the-measure-problem-in-operative-description]]

LINKS:
[[FORAGE-OD-001]]
[[FORAGE-OD-004]]
[[FORAGE-OD-010]]

BIBTEX:
@article{wu2026toolcalling,
  title={Tool Calling is Linearly Readable and Steerable in Language Models},
  author={Wu, Zekun and Wang, Ze and Cho, Seonglae and Yang, Yufei and Koshiyama, Adriano and Bulathwela, Sahan and Perez-Ortiz, Maria},
  journal={arXiv preprint arXiv:2605.07990},
  year={2026},
  url={https://arxiv.org/abs/2605.07990}
}
