ZETTEL

ID: FORAGE-PT-052

TITLE: The vacuum has a name and a literature — the moral crumple zone, where liability lands on an operator who lacked the discretion to prevent the outcome

SOURCE: Madeleine Clare Elish, "Moral Crumple Zones: Cautionary Tales in Human-Robot Interaction", Engaging Science, Technology, and Society (2019) [UNVERIFIED pagination]; read against [[FORAGE-PT-025]] and [[FORAGE-PT-039]]

PASSAGE: [PARAPHRASE] Elish argues that in automated systems the human operator can become a component that absorbs responsibility for failures of the wider system, taking the blame for outcomes they had little practical capacity to control — a structural position she names by analogy with the crumple zone of a car, which is designed to absorb impact.

RESEARCH OBJECT: The named terminus of dissipation. The sibling child found that responsibility diffuses rather than transfers. This one finds that diffusion is not the end state: it *concentrates* on whichever human is closest to the failure, regardless of their discretion. So the answer to "who bears it" is neither the author nor nobody — it is the executor, by structural default and against the merits.

LOCAL MOVE: This child supplies the missing bearer for the accountability vacuum and shows that the assignment is already documented, so the corpus's discovery is a rediscovery with a citable prior name.

SOURCE TERMS: moral crumple zone / human operator / absorbing responsibility / human-machine system / cautionary tale

WHAT BECAME STRANGE: The parent's three roles resolve in the worst available way. AUTHOR is a system that cannot be held; BEARER attaches to the EXECUTOR by proximity rather than by authority; and the executor's lack of discretion — the very thing that should excuse them — is what put them in the position of absorbing the impact. The "human in the loop" is structurally a liability sink, and the safety rationale for placing them there is what supplies the sink.

QUESTION: In documented automation failures, does formal blame track discretion or proximity — and how often does it land on the party with least capacity to have prevented the outcome?

DEEPER QUESTION: If proximity beats discretion, then every proposal to add a human for oversight adds a crumple zone unless it also adds authority. That makes "human oversight" a governance requirement with a hidden precondition, and the precondition — real discretion, real time, real information — is almost never specified in the same document that requires the human.

MECHANISM: <SYSTEM AUTHORS OR EXECUTES> -> [HUMAN POSITIONED NEARBY FOR OVERSIGHT, WITH LIMITED TIME AND INFORMATION] -> <FAILURE> -> [BLAME SEEKS A PARTY WITH STANDING] -> nearest human has standing -> <EXECUTOR ABSORBS RESPONSIBILITY DESPITE LACKING DISCRETION>

FORMAL SHIFT: <DISSIPATED RESPONSIBILITY> -> <CONCENTRATED ON THE NEAREST STANDING PARTY> -> [PROXIMITY OVERRIDES AUTHORITY] -> <CRUMPLE ZONE>

SOURCE FORMALISM: NONE — a conceptual and case-based argument.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] For each party: discretion d (capacity to have altered the outcome) and proximity p (position in the causal chain at the point of failure). Merit assigns blame by d. The crumple-zone claim is that observed assignment tracks p. Testable by coding documented cases for both and comparing which predicts assignment.

TENSION: READING A (Elish as used here): assignment tracks proximity, so oversight without authority manufactures scapegoats and the remedy is to couple every oversight requirement to a discretion requirement. READING B: assignment tracks proximity only where discretion is *ambiguous*; where authority is clearly documented, blame follows the document — in which case the crumple zone is a symptom of poor specification rather than a structural inevitability.

Reading B is the more actionable and the more testable, and it predicts that cases with explicit authority documentation show merit-tracking assignment.

MISSING: Verified pagination. Any coded dataset of cases with both discretion and proximity scored. Any deployment document that specifies operator discretion alongside operator responsibility.

BOUNDARY: Elish argues from a small number of cautionary cases in human-robot interaction. Generalising to generative systems and to scripted service labour is an extension the source does not make.

CITATION TRAIL: [[FORAGE-PT-025]] [[FORAGE-PT-039]] [[FORAGE-PT-042]] -> Elish 2019 -> proximity against discretion -> next: [[FORAGE-PT-045]] on scripting coverage, since a worker speaking a generated script is the crumple zone in its most ordinary form.

TEST: Code twenty documented automation failures for each party's discretion and proximity, and for where formal blame landed. If proximity predicts assignment better than discretion, the structure is confirmed; if the relation weakens where authority is documented, Reading B holds and specification is the remedy.

PLATFORM: [[proximity-against-discretion]]

LINKS: [[FORAGE-PT-025]] [[FORAGE-PT-039]] [[FORAGE-PT-042]] [[FORAGE-PT-045]]

BIBTEX: @article{elish2019moral, title={Moral Crumple Zones: Cautionary Tales in Human-Robot Interaction}, author={Elish, Madeleine Clare}, journal={Engaging Science, Technology, and Society}, volume={5}, year={2019}, note={[UNVERIFIED] pagination not verified in this forage}}
