ZETTEL

ID: PF-055

TITLE:
A loop becomes method when its branching conditions become inspectable.

SOURCE:
Wu et al. — PromptChainer — 2022.

PASSAGE:
[PARAPHRASE] PromptChainer represents multi-step LLM workflows visually so users can scaffold intermediate outputs and debug failures at multiple granularities.

RESEARCH OBJECT:
Iteration alone is not method; inspectable transitions and intervention points matter.

LOCAL MOVE:
The tool externalizes sequence and intermediate state.

SOURCE TERMS:
prompt chaining; visual programming; intermediate outputs; debugging.

WHAT BECAME STRANGE:
“Generate, test, reject, revise” remains underspecified until one can say what caused the transition from one state to the next.

QUESTION:
What minimum transition rule converts iterative prompting into a reportable method?

DEEPER QUESTION:
Can tacit judgment be represented without falsifying it into rigid criteria?

MECHANISM:
<state n>
→ [evaluate/intervene]
→ <state n+1>
→ ...
→ <artifact>

FORMAL SHIFT:
<conversation>
→ <workflow graph>
→ [debug transitions]
→ <repeatable procedure>

SOURCE FORMALISM:
Visual prompt chain.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
METHOD LOOP = states + transition conditions + stopping condition.

TENSION:
Creative practice often uses tacit stopping rules.

MISSING:
A representation for tacit but consequential evaluation.

BOUNDARY:
PromptChainer supports debugging; it does not define scholarly method.

CITATION TRAIL:
Workflow modeling; reflective practice; tacit knowledge.

TEST:
Compare reproducibility of loops documented only as transcripts versus loops documented with transition rationale.

PLATFORM:
[[When a Loop Becomes Method]]

LINKS:
[[PromptChainer]]
[[Iteration]]
[[Transition Rule]]

BIBTEX:
@inproceedings{wu2022promptchainer,
  author={Tongshuang Wu and Ellen Jiang and Aaron Donsbach and Jeff Gray and Alejandra Molina and Michael Terry and Carrie J. Cai},
  title={PromptChainer: Chaining Large Language Model Prompts through Visual Programming},
  booktitle={CHI Conference on Human Factors in Computing Systems Extended Abstracts},
  year={2022},
  doi={10.1145/3491101.3519729}
}