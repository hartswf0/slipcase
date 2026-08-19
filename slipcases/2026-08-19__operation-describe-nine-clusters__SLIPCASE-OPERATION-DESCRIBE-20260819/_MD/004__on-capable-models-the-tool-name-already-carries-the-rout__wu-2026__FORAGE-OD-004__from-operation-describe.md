ZETTEL

ID:
FORAGE-OD-004

TITLE:
ON CAPABLE MODELS THE TOOL NAME ALREADY CARRIES THE ROUTE AND THE DESCRIPTION ADDS ALMOST NOTHING

SOURCE:
Zekun Wu et al. — Tool Calling is Linearly Readable and Steerable in Language Models — arXiv:2605.07990 — 2026

PASSAGE:
[QUOTE]
"Adding short tool descriptions makes at most a small difference on 4B+ models and hurts some sub-1B models, where the longer prompt overwhelms the smaller model."

[QUOTE]
"instruction-tuned models at 4B+ already reach 93–100% without descriptions and gain at most a few points from them."

RESEARCH OBJECT:
The archive's primary case is chosen precisely because it offers the cleanest experimental control over description. Published evidence indicates that in that case the description is close to inert, and the *name* does the routing.

The dissertation's cleanest case is also its weakest case.

LOCAL MOVE:
Wu et al. ablate descriptions to isolate the steering mechanism, and find the mechanism is keyed to tool identity. Descriptions are treated as optional metadata, not as the control surface.

SOURCE TERMS:
short tool descriptions
name-only
instruction-tuned
4B+
sub-1B
longer prompt
overwhelms

WHAT BECAME STRANGE:
The archive's three-sentence defense opens: "We do not study labels as names, but as routing valves."

The evidence says the opposite. The name — the bare label — is the valve. The description is the brochure attached to it.

QUESTION:
If the operative unit in the primary case is the identifier rather than the sentence, is "operative description" the wrong name for the phenomenon the archive has actually found?

DEEPER QUESTION:
Was the whole rhetorical move away from "labels" a move away from the archive's own strongest object?

MECHANISM:
<TOOL NAME>
→ recognized as a lexical identifier with strong training-time associations
→ sets the pairwise discrimination margin almost entirely
→ [DESCRIPTION ADDED]
→ contributes a marginal adjustment, sometimes negative
→ <TOOL CALL>

The description is a second-order correction to a first-order naming effect.

FORMAL SHIFT:
<LABEL>
→ <IDENTIFIER EMBEDDING>
→ [PAIRWISE DISCRIMINATION]
→ <ROUTE>
with
<DESCRIPTION>
→ [MARGINAL PERTURBATION]
→ <SMALL SIGNED ADJUSTMENT>

SOURCE FORMALISM:
Reported: 93–100% correct selection without descriptions on instruction-tuned 4B+ models; "at most a few points" gain from adding descriptions; degradation on sub-1B and base models.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Decompose the route margin:

m = m_name + m_desc + m_position + ε

Wu et al.'s result: |m_desc| ≪ |m_name| for capable instruction-tuned operators.

Therefore the dissertation's contribution is not "descriptions route action." It is a claim about the *regime* in which m_desc becomes non-negligible.

That regime, not the general claim, is the defensible thesis.

TENSION:
READING A (Wu et al.): descriptions are near-inert; names suffice.
READING B (Chen, arXiv:2606.16364): boosting description tokens alone, excluding the name, still recovers 43.9% of failed selections — so description tokens carry independent causal signal.

Both cannot be the whole story. The reconciliation is probably that descriptions are inert *on easy discriminations* and causal *on hard ones* — but that is a hypothesis, not a finding.

MISSING:
Any experiment that varies description while holding name constant AND stratifies by discrimination difficulty. Neither cited paper does this. This is an open, cheap, publishable experiment.

BOUNDARY:
These are results about function-calling benchmarks, not about GitHub labels, moderation, or image prompts. They do not show that description is inert in general. They show that the archive's chosen showcase is the domain least favorable to its headline claim.

CITATION TRAIL:
Shiyang Chen — Looking Is Not Picking — arXiv:2606.16364 — 2026 (the rival reading).
Berkeley Function-Calling Leaderboard failure taxonomy.
PAPERS/operation-describe-label-01.md §20 ("We do not study labels as names").
Rigid designation / Kripke, for what a name does that a description cannot.

TEST:
Hold the user prompt and model fixed. Construct a 2×2: {informative name, opaque name} × {no description, informative description}.

Prediction if Reading A holds: the opaque-name × description cell recovers most of the loss, and the informative-name × description cell shows no gain.

That single 2×2 decides whether "operative description" names a general mechanism or a repair mechanism for failed naming.

PLATFORM:
[[names-route-descriptions-repair]]

LINKS:
[[FORAGE-OD-002]]
[[FORAGE-OD-005]]
[[FORAGE-OD-006]]
[[FORAGE-OD-007]]

BIBTEX:
@article{wu2026toolcalling,
  title={Tool Calling is Linearly Readable and Steerable in Language Models},
  author={Wu, Zekun and Wang, Ze and Cho, Seonglae and Yang, Yufei and Koshiyama, Adriano and Bulathwela, Sahan and Perez-Ortiz, Maria},
  journal={arXiv preprint arXiv:2605.07990},
  year={2026},
  url={https://arxiv.org/abs/2605.07990}
}
