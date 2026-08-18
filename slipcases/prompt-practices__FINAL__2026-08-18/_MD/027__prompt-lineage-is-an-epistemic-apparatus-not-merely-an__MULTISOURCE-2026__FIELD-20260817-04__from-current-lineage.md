ZETTEL

ID:
FIELD-20260817-04

TITLE:
Prompt lineage is an epistemic apparatus, not merely an authorship ledger.

SOURCE:
MULTISOURCE — Mahdavi Goloujeh, Sullivan & Magerko 2024; Hollan, Hutchins & Kirsh 2000; Hill et al. 1992. SOURCE URLs: https://doi.org/10.1145/3613905.3650947 ; https://doi.org/10.1145/353485.353487 ; https://doi.org/10.1145/142750.142751

PASSAGE:
[OUR INFERENCE] A lineage becomes epistemic when its diffs, failures, reasons, and results alter what a later user can infer—not merely when it tells who contributed what.

RESEARCH OBJECT:
The field separates two provenance functions that are often collapsed. CREDIT PROVENANCE answers who contributed. EPISTEMIC PROVENANCE answers what changed, why it changed, what evidence motivated the change, and what happened afterward.

LOCAL MOVE:
Replace LINEAGE AS AUTHORSHIP LEDGER with LINEAGE AS EXPERIMENTAL APPARATUS.

SOURCE TERMS:
prompt modification; distributed through time; edit wear; provenance; contribution; history; evidence

WHAT BECAME STRANGE:
A version edge can carry more knowledge than either endpoint. “Added this phrase because output X failed test Y under model Z” is an experimental observation compressed into a transition.

QUESTION:
What information must a prompt diff preserve before it can teach rather than merely attribute?

DEEPER QUESTION:
Could a prompt repository become a cumulative experimental science if every mutation preserved reason, evidence, result, and uncertainty?

MECHANISM:
VERSION_i + observed failure/evidence → motivated diff Δ_i → VERSION_i+1 → execution → result/evaluation; future users inspect transition rather than only endpoint.

FORMAL SHIFT:
EDGE=(author,time,diff) becomes EPISTEMIC_EDGE=(reason,evidence,diff,result,confidence,environment).

SOURCE FORMALISM:
Mahdavi et al. show modification/credit are socially consequential; Hollan et al. show earlier products can transform later cognition; Hill et al. make interaction histories perceptible on artifacts. Epistemic provenance is compiler synthesis.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
EDGE_i={from,to,actor,reason,evidence_ref,diff,result_ref,test_ref,environment_ref,confidence}; a lineage is a graph of hypotheses and interventions, not only versions.

TENSION:
More detailed provenance can improve learning while increasing surveillance, ownership claims, burden of annotation, and privacy risk.

MISSING:
Evidence that reason/evidence/result-enriched diffs improve transfer enough to justify their capture cost.

BOUNDARY:
The cited sources support components of the mechanism, not the proposed schema as a whole.

CITATION TRAIL:
[[SCGAI-003]] → prompts modify over time → [[SCGAI-003-A]] → temporal products transform later cognition → [[SCGAI-008-A]] → visible interaction history → epistemic provenance.

TEST:
Give users identical final prompts with (A) attribution-only history, (B) raw diffs, or (C) reason+evidence+result enriched diffs; test prediction, debugging, and transfer.

PLATFORM:
Prompt repositories / collaborative AI workspaces / research archives

LINKS:
[[SCGAI-003]]
[[SCGAI-003-A]]
[[SCGAI-008-A]]
[[SCGAI-008]]

BIBTEX:
@inproceedings{mahdavigoloujeh2024social, author={Mahdavi Goloujeh, Atefeh and Sullivan, Anne and Magerko, Brian}, title={The Social Construction of Generative AI Prompts}, year={2024}, doi={10.1145/3613905.3650947}}
@article{hollan2000distributed, author={Hollan, James and Hutchins, Edwin and Kirsh, David}, title={Distributed Cognition: Toward a New Foundation for Human-Computer Interaction Research}, year={2000}, doi={10.1145/353485.353487}}
@inproceedings{hill1992editwear, author={Hill, William C. and Hollan, James D. and Wroblewski, Dave and McCandless, Tim}, title={Edit Wear and Read Wear}, year={1992}, doi={10.1145/142750.142751}}
