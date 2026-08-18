ZETTEL

ID:
CALLSHOT-20260817-10

TITLE:
LET THE CURRENT WORLD WRITE THE GRAMMAR — decode-time grammars prevent the model from naming objects, columns, APIs, or variables that do not actually exist.

SOURCE:
Shuoming Zhang et al. — “Decode-Time Grammars: Constrained LLM Generation over a Refinement Order of Grammar Fragments” — July 20, 2026.
https://arxiv.org/abs/2607.18357

PASSAGE:
[PARAPHRASE]
The authors instantiate grammar fragments from a runtime environment Γ. Open reference positions are tightened into typed slots whose permitted candidates are exactly the names, fields, APIs, or options currently available. Newly generated declarations are added to Γ so later generation can refer to them. They prove a “No-Ghost” property for these constrained references and report eliminating ghost references by construction in their evaluated settings.

RESEARCH OBJECT:
WORLD-INDEXED-GRAMMAR.

LOCAL MOVE:
[[CALLSHOT-20260817-02]] constrained syntax.

But syntactically legal AI output can still say:

CALL nonexistent_function()

SELECT nonexistent_column

USE variable_never_declared.

This July 2026 work pushes constraint one level deeper.

Do not merely say:

“only use things that exist.”

At each point in generation, make the current environment determine which names are legal to utter.

SOURCE TERMS:
“runtime environment Gamma”
“typed slots”
“names”
“fields”
“APIs”
“options”
“newly generated declarations”
“No-Ghost soundness”

WHAT BECAME STRANGE:
Reality becomes grammar.

The model’s vocabulary changes as the world changes.

Create x and the word x becomes legally available downstream.

Delete a field and its name disappears from reachable continuations.

QUESTION:
Could interactive generative worlds expose their current state as a decode-time grammar so the model literally cannot refer to absent objects or illegal operations?

DEEPER QUESTION:
What happens when natural language is not merely checked against the world after generation, but continuously constrained by the world’s present ontology during generation?

MECHANISM:
RUNTIME ENVIRONMENT Γ_t
contains currently valid:

NAMES
FIELDS
FUNCTIONS
OPTIONS
DECLARATIONS.

At generation hole h:

POLICY
→ choose grammar fragment
→ tighten references to Γ_t-valid candidates
→ decode.

If generation creates new declaration d:

Γ_{t+1}
=
Γ_t ∪ {d}.

Later output may legally reference d.

FORMAL SHIFT:
FROM:
GENERATE
→ CHECK WHETHER REFERENT EXISTS
→ REPAIR HALLUCINATION.

TO:
CURRENT WORLD STATE
→ DEFINE LEGAL REFERENCES
→ GENERATE
→ GHOST REFERENCE UNREACHABLE.

SOURCE FORMALISM:
The paper defines environment-indexed grammar fragments and a tightening operation that replaces open reference positions with Γ-typed slots. It states a No-Ghost soundness property for those constrained references.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

WORLD_t
=
{
ENTITIES_t,
PROPERTIES_t,
VERBS_t,
RELATIONS_t
}.

Then define:

GRAMMAR_t
=
COMPILE(WORLD_t).

At token generation:

LEGAL_NEXT
=
GRAMMAR_t(prefix).

World change:

WORLD_t → WORLD_{t+1}

implies:

GRAMMAR_t → GRAMMAR_{t+1}.

The world becomes its own prompt boundary.

TENSION:
Not every meaningful constraint is mask-enforceable.

The paper characterizes a boundary of properties that can be enforced through decoding masks.

A model can still select a legally existing object for the wrong reason.

MISSING:
The boundary between:

UNREPRESENTABLE ERROR
and
LEGAL BUT WRONG ACTION.

BOUNDARY:
The paper evaluates programming-language and structured-generation settings including TileLang, SQL, and P4; extending the mechanism to open-ended interactive worlds is [OUR INFERENCE].

CITATION TRAIL:
[[MJ-GC-030-B-C]]
→ logic + control
→ [[CALLSHOT-20260817-02]]
→ syntax-constrained generation
→ Zhang et al. 2026
→ environment-indexed grammar
→ current world decides which references can be generated
→ description becomes state-dependent operation.

TEST:
Build a toy world with:

objects,
named properties,
legal verbs,
changing state.

Compile the current world into the model’s allowable action/reference grammar before every generation step.

Then deliberately prompt for:

NONEXISTENT OBJECT
DELETED OBJECT
UNDECLARED VARIABLE
ILLEGAL VERB
STALE PROPERTY.

Measure which hallucinations disappear by construction and which survive as semantically wrong but formally legal moves.

PLATFORM:
LLM constrained decoding / gproj / environment-indexed grammars

LINKS:
[[MJ-GC-030-B-C]]
[[MJ-GC-030-B-D]]
[[CALLSHOT-20260817-02]]
[[CALLSHOT-20260817-03]]

BIBTEX:
@article{zhang2026decodetime,
  title={Decode-Time Grammars: Constrained LLM Generation over a Refinement Order of Grammar Fragments},
  author={Zhang, Shuoming and Xu, Ruiyuan and Li, Haofeng and Yu, Qiuchu and Zhang, Yangyu and Xia, Chunwei and Feng, Xiaobing and Wang, Chenxi and Cui, Huimin and Zhao, Jiacheng},
  journal={arXiv preprint arXiv:2607.18357},
  year={2026},
  url={https://arxiv.org/abs/2607.18357}
}
