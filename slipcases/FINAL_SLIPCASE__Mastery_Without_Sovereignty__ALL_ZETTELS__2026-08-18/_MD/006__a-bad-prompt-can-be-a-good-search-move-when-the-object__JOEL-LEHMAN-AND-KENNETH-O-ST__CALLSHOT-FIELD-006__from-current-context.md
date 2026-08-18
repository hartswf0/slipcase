ZETTEL

ID:
CALLSHOT-FIELD-006

TITLE:
A “BAD” PROMPT CAN BE A GOOD SEARCH MOVE WHEN THE OBJECTIVE ITSELF IS DECEPTIVE.

SOURCE:
Joel Lehman and Kenneth O. Stanley, “Abandoning Objectives: Evolution Through the Search for Novelty Alone,” Evolutionary Computation 19(2), 2011, 189–223. DOI 10.1162/EVCO_a_00025. SOURCE URL: https://pubmed.ncbi.nlm.nih.gov/20868264/

PASSAGE:
[QUOTE]
“Objective functions themselves may actively misdirect search toward dead ends.”

RESEARCH OBJECT:
DIRECTLY OPTIMIZING FOR THE CURRENT TARGET CAN DESTROY STEPPING STONES NEEDED TO REACH BETTER REGIONS.

LOCAL MOVE:
Lehman and Stanley demonstrate cases where novelty search outperforms objective-based search. Joshua’s deliberate “less rational” and “nonsensical” prompts can therefore be posed as a testable search strategy rather than mere play.

SOURCE TERMS:
“novelty search” · “deception” · “dead ends” · “objective” · “behavioral novelty”

WHAT BECAME STRANGE:
The most rational action may be to stop asking for what you currently think you want.

QUESTION:
Do expert prompters sometimes improve target attainment by temporarily optimizing for difference rather than resemblance?

DEEPER QUESTION:
Can natural-language specification become a deceptive objective that suppresses unforeseen but necessary stepping stones?

MECHANISM:
OBJECTIVE SEARCH → retain local improvement; NOVELTY SEARCH → retain behavioral difference → preserve unexpected stepping stones.

FORMAL SHIFT:
BETTER PROMPT = CLOSER TO TARGET → SEARCH VALUE CAN INCREASE WHILE TARGET SIMILARITY TEMPORARILY DECREASES.

SOURCE FORMALISM:
[PARAPHRASE]
Lehman and Stanley compare objective-driven evolutionary search with behavioral novelty search and report tasks where novelty search performs better.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
Objective: argmax SIM(G(P),T). Novelty: argmax DIST(B(P),ARCHIVE). Hybrid prompting can alternate exploitation and novelty phases.

TENSION:
Nonsense is not automatically novelty search; productive novelty requires a representation of meaningful behavioral difference.

MISSING:
Direct evidence of deceptive stepping stones in prompt/image spaces.

BOUNDARY:
This is a computational analogy, not evidence Midjourney uses novelty-search machinery.

CITATION TRAIL:
[[MJ-JOSHUA-007-A]] → Joshua’s nonsensical branch → Lehman & Stanley → objective itself may trap search → [[CALLSHOT-FIELD-002]] lineage preservation.

TEST:
Compare target-only selection, novelty-only selection, and alternating search. Preserve ancestry and identify winning artifacts whose necessary ancestors would have been discarded by target-only selection.

PLATFORM:
Evolutionary Computation · generative prompting

LINKS:
[[MJ-JOSHUA-007-A]] [[CALLSHOT-FIELD-002]]

BIBTEX:
@article{LehmanStanley2011,
 author={Lehman, Joel and Stanley, Kenneth O.},
 title={Abandoning Objectives: Evolution Through the Search for Novelty Alone},
 journal={Evolutionary Computation}, year={2011}, volume={19}, number={2}, pages={189--223},
 doi={10.1162/EVCO_a_00025}, url={https://pubmed.ncbi.nlm.nih.gov/20868264/}
}
