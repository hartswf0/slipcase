ZETTEL

ID: FORAGE-PT-053

TITLE: A prohibition constrains more per token than a description, which is why negative specification outperforms explanation as a handover medium

SOURCE: [[FORAGE-PT-026]] (constraint as handover medium) developed against PROGRAMS/haunted.json AXIOM_03 ("constraint excludes") and the negative-prompt practice reported in PROGRAMS-adjacent material [no external study claimed]

PASSAGE: [QUOTE] haunted.json: "<constraint> [does_not_merely_limit] <generation> <constraint> [enables] <generation> <constraint> [excludes] <generation>" [QUOTE] theory.json: "<documentation> is a residue"

RESEARCH OBJECT: An efficiency asymmetry between two ways of specifying the same admissible region. A description picks out what is wanted and leaves the complement unaddressed. A prohibition removes a region and leaves everything else available. When the admissible region is large and irregular — as it is for most design spaces — enumerating what is forbidden is shorter than characterising what is permitted.

LOCAL MOVE: This child sharpens the parent's proposal from "constraint transfers better than prose" to a stated reason with a measurable quantity: constraint per token.

SOURCE TERMS: constraint / excludes / enables / admissible region / residue / negative specification

WHAT BECAME STRANGE: Every documentation convention is positive. Style guides say what to do; specifications describe intended behaviour; explanations narrate rationale. Meanwhile the artifacts that actually hold practice together — lint rules, code-review objections, negative prompts, house prohibitions — are negative, and they are treated as secondary to the positive documents they in fact govern.

QUESTION: For a fixed admissible region, does a prohibition set specify it in fewer tokens than a description set, and does it produce more coherent output from a stranger?

DEEPER QUESTION: If prohibitions dominate, then the transferable residue of any practice is its list of what not to do, and that list is exactly what practitioners fail to write down because it feels obvious to them. The most valuable handover document is the one whose contents are invisible to its author.

MECHANISM: <ADMISSIBLE REGION> -> [DESCRIBE IT POSITIVELY] -> many tokens, boundary underspecified -> stranger produces near-miss output ; <SAME REGION> -> [ENUMERATE EXCLUSIONS] -> fewer tokens, boundary sharp -> <STRANGER AVOIDS THE EXCLUDED AND EXPLORES THE REST>

FORMAL SHIFT: <POSITIVE SPECIFICATION> -> <NEGATIVE SPECIFICATION> -> [MEASURE CONSTRAINT PER TOKEN] -> <PROHIBITION AS THE EFFICIENT MEDIUM>

SOURCE FORMALISM: The three axioms; no formal treatment of specification efficiency in the source.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] For a target region R, let desc(R) and proh(R) be the token counts of the shortest positive and negative specifications that a stranger can use to produce output judged inside R. Efficiency = coherence achieved per token. Prediction: proh wins where R is large and its complement is small and nameable; desc wins where R is small and specific.

That prediction has a corollary: the more expert the practice, the more its knowledge is prohibitive, because experts have small complements they can name and large regions they cannot describe.

TENSION: READING A: prohibitions are more efficient and handover documents should be rewritten as exclusion lists. READING B: prohibitions cannot convey *purpose*, so a stranger avoids errors while producing work that satisfies no goal — coherent and pointless, which is worse than incoherent and aimed.

The discriminating case is the unforeseen task: a prohibition set gives no guidance where it is silent, while a rationale might extend. That is the same unbounded-demand problem again, arriving from the medium side.

MISSING: Any measurement of constraint per token. Any handover experiment comparing prohibition sets against rationale documents. Any method for eliciting the prohibitions an expert has not written down.

BOUNDARY: This is a prediction from an axiom, not a finding. Negative-prompt practice is suggestive and is not evidence about human handover.

CITATION TRAIL: [[FORAGE-PT-026]] [[FORAGE-PT-017]] [[FORAGE-PT-049]] -> negative specification -> constraint per token -> next: elicitation methods for tacit prohibitions, and [[FORAGE-PT-043]] on what happens at the task no specification covers.

TEST: One system, three handover conditions matched on token count: rationale prose, positive specification, prohibition list. Three strangers each, same modification task, blind coherence scoring. Then the unforeseen task. Prohibitions should win round one; if they collapse in round two, Reading B holds and both media are needed for different jobs.

PLATFORM: [[constraint-per-token]]

LINKS: [[FORAGE-PT-017]] [[FORAGE-PT-026]] [[FORAGE-PT-043]] [[FORAGE-PT-049]]

BIBTEX: @unpublished{haunted_program, title={Haunted Machine Criticism Engine}, note={PROGRAMS/haunted.json; developed with PROGRAMS/theory.json}, year={2026}}
