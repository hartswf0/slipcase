ZETTEL

ID:
FORAGE-OD-008

TITLE:
SHUFFLING THE TOOL LIST WITHOUT CHANGING A SINGLE WORD DROPS ONE MODEL'S SUCCESS RATE FROM 41.0% TO 27.0%

SOURCE:
Chengrui Huang, Zhengliang Shi, Yuntao Wen, Xiuying Chen, Peng Han, Shen Gao, Shuo Shang — What Affects the Stability of Tool Learning? An Empirical Study on the Robustness of Tool Learning Frameworks — arXiv:2407.03007 — 2024 — §5.2 "Order of Candidate Toolsets"

PASSAGE:
[PARAPHRASE]
On the I1-tool dataset, Deepseek-chat scores 41.0% with the original toolset ordering and 27.0% when the toolset is randomly shuffled. GPT-3.5 moves only 55.0% → 52.5%.

[QUOTE]
"Open-source model suffers from the positional bias of tools"

[QUOTE]
"powerful models with higher Success Rate are more skillful in solving tasks, thereby showing less instability toward positional bias, and vice versa"

RESEARCH OBJECT:
A 14-point swing in routing produced by pure ordering. No semantic content changed. No description was rewritten. Nothing was described differently.

This is a route change with ΔG large and *no descriptive cause*.

LOCAL MOVE:
Huang et al. are auditing robustness, not theorizing description. They treat position sensitivity as an engineering defect.

For the archive it is not a defect. It is a rival explanation for its entire primary-case effect size.

SOURCE TERMS:
positional bias of tools
order of candidate toolsets
shuffle
success rate
I1-tool
robustness
stability

WHAT BECAME STRANGE:
The archive's causal design is "hold the input constant and vary only the description." But varying a description almost always changes its *length*, and changing length shifts the position of everything after it.

Every description edit is silently also a position edit. The archive's cleanest causal claim has an untreated confound built into the manipulation itself.

QUESTION:
How much of the archive's expected ΔG is attributable to position rather than semantics, and how can a description be edited without moving anything?

DEEPER QUESTION:
If a large share of routing is typographic, is "operative description" partly a theory of *layout* — and does that make Farocki's operational image the wrong ancestor and the typesetter the right one?

MECHANISM:
<TOOL LIST ORDER>
→ primacy/recency weighting in attention over context
→ margin shifts between candidate tools
→ [READOUT SELECTS]
→ <DIFFERENT TOOL, IDENTICAL TEXT>

and, as confound:

<DESCRIPTION EDIT>
→ token count changes
→ all downstream segments shift position
→ [POSITION EFFECT]
→ ΔG observed and misattributed to semantics

FORMAL SHIFT:
<ORDINAL POSITION>
→ <ATTENTION WEIGHT>
→ [SELECTION MARGIN]
→ <ROUTE>

SOURCE FORMALISM:
Reported success rates: Deepseek-chat 41.0% original vs 27.0% shuffled (I1-tool); GPT-3.5 55.0% vs 52.5%; ~3 point difference on I1-instruction for GPT-3.5.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Decompose again:
  m = m_name + m_desc + m_position + ε

Huang et al. bound m_position for one operator class: up to ~14 points of success rate.
Wu et al. bound m_desc for capable operators: "a few points."

Provisional and uncomfortable ordering for weak operators:
  |m_position| > |m_desc|

Required experimental discipline, which the archive does not currently specify: **length-matched description variants**, with padding, so that position is held fixed while semantics varies.

TENSION:
READING A: position effects are a property of weak models and will vanish as models improve, so they are a transient nuisance.
READING B: position effects are a property of attention over long contexts and will *grow* as tool catalogs grow, so they are structural.

Huang et al.'s own gradient (weaker model → stronger bias) supports A. Long-context degradation results support B. Undecided.

MISSING:
Any position-controlled experiment in the archive. Framework §5's "Delta test" asks only "Can you point to where a description changed the generated world?" — a question that cannot distinguish semantics from layout.

BOUNDARY:
This is tool-selection robustness on two models and one benchmark family from 2024. It does not license a general claim that description is epiphenomenal. It licenses the claim that the archive's manipulation is confounded and must be length-matched.

CITATION TRAIL:
"Lost in the middle" / primacy-recency in long contexts.
Evaluating Position Bias in LLM Recommendations — arXiv:2508.02020.
Hardt, Jagadeesan, Mendler-Dünner — Performative Power — arXiv:2203.17232 — where display *position* is the identification strategy, not the confound.
FORAGE-OD-009.

TEST:
Length-matched description pairs. Construct D₁ and D₂ with identical token counts and different semantics; also construct D₁ placed at position p and position p' with identical text.

Report ΔG_semantic (length-matched) and ΔG_positional (text-matched) side by side on the same task.

If ΔG_positional ≥ ΔG_semantic, the primary case must be rebuilt or renamed.

PLATFORM:
[[the-typographic-residue]]

LINKS:
[[FORAGE-OD-004]]
[[FORAGE-OD-009]]
[[FORAGE-OD-003]]

BIBTEX:
@article{huang2024stability,
  title={What Affects the Stability of Tool Learning? An Empirical Study on the Robustness of Tool Learning Frameworks},
  author={Huang, Chengrui and Shi, Zhengliang and Wen, Yuntao and Chen, Xiuying and Han, Peng and Gao, Shen and Shang, Shuo},
  journal={arXiv preprint arXiv:2407.03007},
  year={2024},
  url={https://arxiv.org/abs/2407.03007}
}
