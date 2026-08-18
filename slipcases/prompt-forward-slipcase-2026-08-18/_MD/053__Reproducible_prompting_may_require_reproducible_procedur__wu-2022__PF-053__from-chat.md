ZETTEL

ID: PF-053

TITLE:
Reproducible prompting may require reproducible procedure rather than identical output.

SOURCE:
Wu, Terry, and Cai — AI Chains — 2022.

PASSAGE:
[PARAPHRASE] AI Chains decomposes complex model tasks into inspectable prompt-based stages and lets users intervene in intermediate results.

RESEARCH OBJECT:
The repeatable object can be the chain of operations even when individual model outputs vary.

LOCAL MOVE:
The system shifts control from exact text to process structure.

SOURCE TERMS:
chain; intermediate result; controllability; transparency.

WHAT BECAME STRANGE:
A prompt method might reproduce a kind of inquiry without reproducing sentences.

QUESTION:
What should “reproduce the method” mean for stochastic generative systems?

DEEPER QUESTION:
Should replication target distributional behavior, decision structure, or exact artifacts?

MECHANISM:
<chain specification>
→ [execute stochastic stages]
→ <variable intermediates>
→ <functionally comparable result>

FORMAL SHIFT:
NONE

SOURCE FORMALISM:
Prompt chain.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
PROCEDURAL REPLICATION ≠ OUTPUT IDENTITY.

TENSION:
Loose functional equivalence can make failed replication too easy to excuse.

MISSING:
Predeclared equivalence criteria.

BOUNDARY:
AI Chains does not propose a science-wide reproducibility standard.

CITATION TRAIL:
Stochastic simulation reproducibility; computational workflows.

TEST:
Have independent teams run the same prompt chain and assess whether conclusions replicate despite divergent text.

PLATFORM:
[[Reproducibility Without Identical Words]]

LINKS:
[[AI Chains]]
[[Stochastic Reproducibility]]
[[Method]]

BIBTEX:
@inproceedings{wu2022aichains,
  author={Tongshuang Wu and Michael Terry and Carrie J. Cai},
  title={AI Chains: Transparent and Controllable Human-AI Interaction by Chaining Large Language Model Prompts},
  booktitle={CHI 2022},
  year={2022}
}