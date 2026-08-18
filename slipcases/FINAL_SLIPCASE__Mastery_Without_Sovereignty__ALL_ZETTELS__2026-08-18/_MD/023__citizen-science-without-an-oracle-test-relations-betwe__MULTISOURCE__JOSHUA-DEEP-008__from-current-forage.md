ZETTEL

ID:
JOSHUA-DEEP-008

TITLE:
CITIZEN SCIENCE WITHOUT AN ORACLE: TEST RELATIONS BETWEEN RUNS, NOT JUST WHETHER ONE IMAGE “LOOKS RIGHT.”

SOURCE:
Joshua Larson interview with Watson Hartsoe, 2022-10-18. Original local source: _RESOURCES/BLUE_MJ_Interview 2_Joshua.pages; best-effort extracted text: _RESOURCES/_joshua_decompressed_strings.txt. SOURCE URL: LOCAL_FILE | T. Y. Chen, S. C. Cheung, and S. M. Yiu, “Metamorphic Testing: A New Approach for Generating Next Test Cases,” Technical Report HKUST-CS98-01, 1998; arXiv:2002.12543. SOURCE URL: https://arxiv.org/abs/2002.12543

PASSAGE:
[QUOTE — JOSHUA, 1:29:21]
“doing kind of citizen science research type stuff, with varying levels of scientific rigor”

[QUOTE — JOSHUA, 48:51]
“experimentation is, that’s the best way for now.”

[PARAPHRASE — CHEN ET AL.]
Metamorphic testing addresses situations where a reliable test oracle is unavailable by testing expected relations among related executions.

RESEARCH OBJECT:
PROMPT CRAFT LACKS A SIMPLE ORACLE FOR AESTHETIC CORRECTNESS, BUT IT CAN STILL TEST RELATIONS THAT SHOULD HOLD ACROSS CONTROLLED PROMPT CHANGES.

LOCAL MOVE:
Joshua’s community experiments in a domain where “correct image” often has no determinate answer. Metamorphic testing supplies a methodologically strange but useful analogy: when you cannot judge a single execution against a known oracle, test relations among multiple executions produced by related inputs.

SOURCE TERMS:
“citizen science” · “varying levels of scientific rigor” · experimentation · test oracle · related executions · metamorphic relation

WHAT BECAME STRANGE:
Prompt craft may become more scientific without ever acquiring a ground-truth image. The unit of evidence can be a relation: changing only X should alter Y while preserving Z.

QUESTION:
Which prompt-craft claims can be rewritten as relations between controlled runs rather than anecdotes about impressive outputs?

DEEPER QUESTION:
Can a community build cumulative causal knowledge of an opaque generative model by maintaining a library of metamorphic relations even when aesthetic quality itself has no oracle?

MECHANISM:
CLAIM ABOUT PROMPT OPERATOR → DEFINE SOURCE PROMPT P AND TRANSFORM T(P) → SAMPLE BOTH → TEST EXPECTED RELATION R(outputs(P), outputs(T(P))) → ACCEPT / REJECT / QUALIFY CLAIM.

FORMAL SHIFT:
“THIS PROMPT WORKED” → “THIS CONTROLLED TRANSFORMATION PRODUCED A REPEATABLE RELATION.”

SOURCE FORMALISM:
[PARAPHRASE]
Chen, Cheung, and Yiu propose deriving follow-up test cases from successful cases and using relations among executions when conventional test oracles are unavailable.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
Example MR: Add lens term L while holding semantic content and sampling policy fixed. Expected relation: photographic-depth cues increase while subject identity distribution remains within tolerance.

TENSION:
Metamorphic relations can smuggle in false assumptions about how the model ought to behave. A beautifully repeatable relation may still reflect a transient model version rather than a stable semantic operator.

MISSING:
A catalog of prompt-craft claims translated into falsifiable relational tests, with versioned replication across systems and time.

BOUNDARY:
Metamorphic testing comes from software testing, where relations are usually specified from domain knowledge. Aesthetic prompt relations are often probabilistic and must be statistically defined.

CITATION TRAIL:
[[CALLSHOT-FIELD-001]] → community craft → Joshua’s “citizen science” → [[JOSHUA-DEEP-007]] noise/drift problem → Chen et al. oracle problem → relational experiments as a stronger community method.

TEST:
Take ten community prompt rules. For each, specify one expected metamorphic relation, preregister sampling count and metric, run across seeds and two model versions, and publish failed as well as successful relations.

PLATFORM:
Midjourney · citizen science · metamorphic testing

LINKS:
[[CALLSHOT-FIELD-001]] [[JOSHUA-DEEP-007]] [[JOSHUA-DEEP-009]]

BIBTEX:
@techreport{ChenCheungYiu1998,
 author={Chen, T. Y. and Cheung, S. C. and Yiu, S. M.},
 title={Metamorphic Testing: A New Approach for Generating Next Test Cases},
 institution={Hong Kong University of Science and Technology}, number={HKUST-CS98-01}, year={1998},
 url={https://arxiv.org/abs/2002.12543}
}
