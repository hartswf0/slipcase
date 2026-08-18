ZETTEL

ID:
PB-FORAGE-013

TITLE:
The clearer the scoring rule becomes, the more precisely contestants can optimize the wrong thing.

SOURCE:
David Manheim and Scott Garrabrant — Categorizing Variants of Goodhart’s Law — 2018/2019 — arXiv:1803.04585.

PASSAGE:
[PARAPHRASE]
Manheim and Garrabrant distinguish several mechanisms through which optimization of a proxy can break its relationship with the underlying goal. Their categories include regressional, extremal, causal, and adversarial Goodhart effects. They emphasize that stronger optimization pressure can make proxy failure increasingly important.

RESEARCH OBJECT:
[[PB-FORAGE-006]] treated scoring mainly as a problem of interpretation.

Prompt Battles add another problem:

contestants see the metric.

Once creativity, relevance, depth, flag proximity, prompting sophistication, or “quality of the dance” become scoring targets, expert contestants can optimize those proxies directly.

The rubric stops merely measuring behavior.

It becomes part of the behavior-generating environment.

LOCAL MOVE:
Treat the scoring rubric as an intervention on participant strategy.

SOURCE TERMS:
proxy
goal
selection pressure
Regressional Goodhart
Extremal Goodhart
Causal Goodhart
Adversarial Goodhart
optimization

WHAT BECAME STRANGE:
PB_PRIME repeatedly tries to improve fairness by making success criteria explicit.

That may simultaneously make construct validity worse.

Transparency tells participants exactly which observable surface must be maximized.

QUESTION:
Can a Prompt Battle make its rules transparent without converting its measurement criteria into exploitable targets?

DEEPER QUESTION:
What remains of “prompting skill” after contestants have trained specifically against the judging function?

MECHANISM:
Researchers care about latent goal G.

They expose measurable proxy M.

Contestants receive selection pressure to maximize M.

They search increasingly unusual regions of strategy space.

At sufficient optimization, the empirical relation between M and G can deteriorate.

FORMAL SHIFT:
<RESEARCH CONSTRUCT G>
→ <PUBLIC SCORE M>
→ [STRATEGIC OPTIMIZATION]
→ <HIGH-M BEHAVIORS>
→ <POSSIBLE DECOUPLING OF M FROM G>

SOURCE FORMALISM:
Manheim and Garrabrant define a goal G(s) and proxy metric M(s) over system states and analyze failures created by selection or intervention.

They distinguish four broad Goodhart mechanisms:

Regressional
Extremal
Causal
Adversarial.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

G = quality the Prompt Battle intends to discover
M = published scoring rubric
π = contestant strategy

Competition induces:

π* = argmax_π M(π)

The research assumption is:

higher M(π*) ⇒ higher G(π*)

But the battle itself applies unusually strong selection pressure on M.

The more skilled the contestants become at maximizing the rubric, the less safe that implication becomes.

TENSION:
Hidden criteria reduce gaming but violate competitive transparency and make judging opaque.

Public criteria improve procedural fairness but increase optimization pressure on the proxy.

The demands of a fair game and the demands of an uncorrupted measurement instrument may conflict structurally.

MISSING:
A separation between:

TRAINING SCORE
what contestants are allowed to optimize

and

TRANSFER MEASURE
what determines whether the discovered strategy generalizes beyond the visible rubric.

BOUNDARY:
Goodhart effects do not imply that every metric becomes useless when optimized.

The source distinguishes several mechanisms and conditions.

Which mechanism, if any, occurs in Prompt Battles must be empirically established.

CITATION TRAIL:
[[PB-FORAGE-006]]
[[PB-FORAGE-004]]
→ Manheim and Garrabrant
→ Campbell’s law
→ strategic classification
→ specification gaming
→ investigate whether competitive prompting produces metric-specialized rather than transferable expertise.

TEST:
Randomly divide evaluation criteria into:

PUBLIC RUBRIC
visible during competition

HELD-OUT TRANSFER CRITERIA
never shown to participants.

After the battle, apply winning prompting strategies to novel flags and have an independent panel judge them with the held-out criteria.

If leaderboard rank collapses under transfer, the battle may have selected rubric exploitation rather than the intended capability.

Repeat while varying prize size and competitive intensity.

Test whether stronger incentives increase the divergence.

PLATFORM:
[[Prompt Battle Measurement]]

LINKS:
[[PB-FORAGE-006]]
[[PB-FORAGE-004]]
[[Goodharted Prompting]]
[[Rubric Gaming]]
[[Transfer Evaluation]]

BIBTEX:
@article{manheim2018goodhart,
  title={Categorizing Variants of Goodhart's Law},
  author={Manheim, David and Garrabrant, Scott},
  journal={arXiv preprint arXiv:1803.04585},
  year={2018},
  doi={10.48550/arXiv.1803.04585}
}
