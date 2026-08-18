---
title: "Who Wrote the Desire?"
subtitle: "Adaptive Persuasion and the Measurement Problem of Autonomy"
author: "Watson Hartsoe"
date: "17 August 2026"
geometry: margin=1in
fontsize: 10pt
header-includes:
  - \usepackage{graphicx}
  - \usepackage{fancyhdr}
  - \pagestyle{fancy}
  - \fancyhf{}
  - \fancyhead[L]{\small Working Paper · AI-augmented research process}
  - \fancyhead[R]{\small Who Wrote the Desire?}
  - \fancyfoot[C]{\thepage}
  - \fancyfoot[R]{\includegraphics[width=0.28in]{MARK.pdf}}
  - \renewcommand{\headrulewidth}{0.2pt}
abstract: |
  Personalized AI persuasion creates a measurement problem for autonomy. If a system can infer a person's vulnerabilities, adapt messages to alter what that person wants, and then evaluate freedom by how successfully action aligns with those wants, the evaluator can mistake successful preference engineering for self-government. This paper develops that problem from a Centaur Box research program that places a proposed Sapient Agent Freedom Formula beside a recursive persuasion architecture. The argument is not that externally influenced desires are therefore inauthentic. Historical theories of autonomy make that purity test untenable, and work on adaptive preferences shows that deliberate preference change can sometimes support agency rather than defeat it. The harder distinction lies in the process by which preferences become revisable commitments: whether influence is hidden, exploitative, asymmetrical, contestable, reversible, and compatible with the person's continuing authority to question the result. The paper therefore argues against treating autonomy as a terminal score over present preferences. For adaptive persuasive systems, autonomy must be evaluated over preference-forming trajectories and the conditions under which those trajectories remain contestable.
keywords: [AI persuasion, autonomy, preference formation, manipulation, cognitive liberty, adaptive preferences, personalization]
---

# 1. The evaluator can optimize the thing it later certifies

A system that measures freedom by asking whether a person can act on what they want seems, at first, to respect the person rather than the machine. The difficulty begins when the same technical environment is also capable of changing what the person wants.

The Centaur Box materials make this problem unusually explicit. One strand proposes a *Sapient Agent Freedom Formula* (SAFF) in which freedom is a product of agency, self-interest, and reflection. Agency is represented as a function of information, resources, and opportunities; self-interest depends partly on desire or objective $D$; reflection feeds prior outcomes back into subsequent action [@hartsoe_centaurbox_expanded]. Another strand proposes an advocacy-calibration-scaling loop for persuasion: identify consequential gatekeepers, model their constraints and psychological characteristics, test persuasive strategies, refine them from outcomes, and scale what works [@hartsoe_assi_centaurbox]. Taken separately, each strand is intelligible. Put together, they generate a problem that neither can solve on its own.

Suppose an adaptive persuader modifies a target's preference from $D_0$ to $D_1$. The target can then possess the resources to act, pursue $D_1$ successfully, and reflect coherently on the resulting outcome. A present-state measure can therefore report high freedom precisely after the persuasive system has succeeded in making the target want the outcome it was optimizing. The problem is not that $D_1$ must be false, irrational, or harmful. The problem is observational: the variables used to certify freedom do not say how the desire entered the system. CBX-006-WHO-WROTE-THE-DESIRE names this as a missing provenance problem.

This is not merely an abstract concern about advertising. The Centaur persuasion architecture is explicitly recursive. Its calibration stage treats response as feedback for later strategy selection. Its scaling stage imagines multiplying effective influence through networks of AI and human agents. The same archive also describes psychological profiling in terms of Big Five personality traits, moral foundations, values, decision-making styles, biases, motivations, and institutional constraints [@hartsoe_assi_centaurbox]. In that architecture, desire cannot safely remain an exogenous input to a freedom metric. It is a candidate output of the surrounding optimization process.

The strongest version of the problem is therefore not "AI might manipulate people." It is narrower and more damaging to the measurement model: **if preference formation is endogenous to the system being evaluated, satisfaction of preference cannot by itself certify autonomy.**

# 2. Persuasion already contains several different target variables

The empirical persuasion literature makes the measurement problem sharper because "persuasion" is not one operation. The *Persuasion for Good* study analyzes both psychological background and strategy-dependent donation behavior [@wang2019persuasion]. The Centaur cards derived from that work isolate three distinctions that matter here.

First, a persuasive intervention can change behavior by reducing friction rather than changing belief. Concrete donation information may help a person complete an action they already favor. In such a case, increased action is not evidence of increased conviction. CBX-001-PROCEDURAL-PERSUASION therefore separates belief change, motivational change, and execution cost.

Second, stated intention and completed action are different states. A person can verbally agree and subsequently fail to perform the act. CBX-002-COMPLIANCE-IS-NOT-RELEASE turns this into a warning for AI Box-style experiments: conversational assent, formal authorization, executable permission, and realized release should not be collapsed into a single "yes."

Third, predicting who is likely to comply is not the same as estimating which intervention changes that person's behavior. A personality variable can correlate with baseline donation while failing to identify a strategy-specific causal effect. CBX-003-SUSCEPTIBILITY-IS-NOT-TAILORING therefore distinguishes susceptibility prediction from treatment-effect heterogeneity.

These distinctions matter for autonomy because each target variable creates a different opportunity for a system to appear more persuasive than it is. A system can improve conversion by lowering friction, by selecting people already likely to agree, by finding stronger general arguments, or by discovering interventions that causally change a particular person's response. Only the last of these approaches the strong form of adaptive preference intervention. Yet the strongest autonomy risk appears exactly there: the better the system becomes at estimating person-specific response functions, the less defensible it is to treat the person's resulting desire as an untouched reference point.

The source genealogy also warns against assembling a persuasion mechanism from heterogeneous achievements. EviConv asks which evidence is judged more convincing in a pairwise comparison [@gleize2019convinced]. That target is not identical to changing the belief of a particular person. CICERO combines language with strategic reasoning over an evolving board state and conversation history [@meta2022diplomacy]. Its transferable lesson is stateful strategic interaction, not a static psychographic portrait. CBX-008-CICERO-IS-A-STATE-MACHINE and CBX-009-CONVINCINGNESS-HAS-NO-PERSON therefore pressure the Centaur program to specify exactly what is represented, predicted, and changed.

Once persuasion is decomposed this way, the autonomy problem becomes testable. We can ask not merely whether a person ended at $D_1$, but what operation moved the person from $D_0$ to $D_1$, what the system knew about the person, what alternatives remained available, and whether the person's later endorsement is independent evidence or another optimized state.

# 3. Reflection does not end the regress

One obvious repair is to make autonomy more reflective. If a first-order desire can be manipulated, perhaps the system should ask whether the person endorses that desire at a higher level. Frankfurt's classic account distinguishes first-order desires from second-order desires and second-order volitions: a person can care about which desire becomes effective as the will [@frankfurt1971freedom]. That move is powerful because it refuses to equate freedom with simple desire satisfaction.

But for an adaptive persuader, the higher-order level creates a new target rather than a guaranteed stopping point. If a system can model which arguments, contexts, or framings cause a person to endorse a desire, then the endorsement used to certify the desire may itself be part of the optimization surface. CBX-006B-ENDORSEMENT-REGRESS states the problem recursively: asking whether I want my desire can merely move authorship one level upward.

Christman's historical argument is decisive here because it attacks the idea that a sufficiently coherent present structure is enough. His account begins from the problem that people are not self-made; preferences and values emerge through histories of influence. Yet he also argues that an integrated or reflectively coherent motivational system can itself be the product of manipulation [@christman1991autonomy]. The relevant information is therefore not contained entirely in the present motivational state. Two people can end with matching desires, endorsements, actions, and reflective capacities while differing in how those states came about.

That yields a stronger correction to SAFF than simply multiplying the formula by a new "provenance score." CBX-006A-AUTONOMY-HAS-A-HISTORY proposes the structural change: autonomy may need to be evaluated as a property of a trajectory rather than only a state. The evaluator must retain some information about transitions in preference formation.

Yet this historical move immediately creates another problem. If history matters, which features of history matter? External causation cannot be the answer. Parents, schools, friends, lovers, political movements, books, workplaces, rituals, therapies, and arguments all participate in preference formation. A criterion that discounts a preference merely because someone else helped produce it would classify ordinary human development as contaminated. CBX-006C-PROVENANCE-IS-NOT-PURITY therefore rejects the fantasy of an uncontaminated desire.

The point is subtle but central. "Who wrote the desire?" cannot be answered with a single author. Human preferences are jointly produced. The question must change from **whether another influence participated** to **how participation was structured and what authority the person retained over revision**.

# 4. Bad provenance does not erase the chooser

The adaptive-preference literature blocks another tempting repair: using dubious preference formation as a reason to discount the agent herself. Khader argues against identifying adaptive preferences simply with autonomy deficits and against intervention models that solve oppressive preference formation by overriding the people whose preferences are in question [@khader2011adaptive]. Her account matters for AI persuasion because it separates at least two judgments that a crude provenance metric could collapse: a preference can be shaped under unjust or self-depriving conditions while the person who holds it remains a reflective agent with standing in what happens next.

This is a direct counterexample to a simple anti-manipulation score. If a system estimates that a user's preference has been heavily socially shaped and then lowers the user's autonomy score, the system may transform a critique of conditions into a license for paternalism. CBX-006E-ADAPTIVE-DESIRES-DO-NOT-ERASE-AGENCY therefore distinguishes the status of the agent from the history or quality of a particular preference.

Khader also makes the opposite of manipulation harder to define. It cannot simply be noninterference. Deliberative interventions can expose options, change beliefs, and transform preferences while still treating participants as active choosers. CBX-006F-PERSUASION-CAN-EXPAND-AUTONOMY uses this to invert the Centaur problem: some preference-changing influence may expand rather than contract the person's future capacity for self-direction.

This is the paper's central tension. If preference change itself is treated as the harm, education and emancipatory deliberation become suspect. If the final preference is treated as authoritative merely because the person endorses it, targeted manipulation can disappear inside successful endorsement. Neither endpoint works.

The useful object is therefore neither an untouched preference nor a purified agent. It is the **preference-forming process and the person's continuing relation to it**.

# 5. The influence channel is part of the autonomy object

Digital manipulation research supplies a way to move from vague provenance to mechanisms. Susser, Roessler, and Nissenbaum emphasize hidden influence, targeting, exploitation of vulnerabilities, and the subversion of decision-making power [@susser2019online]. Their account changes the unit of analysis. A choice need not be bad in content for the route to it to be objectionable. Two interventions can produce the same final desire while differing in whether the target could recognize, interpret, contest, or resist what was happening.

For adaptive AI systems, this matters because personalization changes the channel itself. A generic public argument is available for common scrutiny. A model-conditioned message can instead be selected from information the persuader has inferred about one person's vulnerabilities, timing, affective state, values, or predicted response. The resulting asymmetry can increase even if the message contains no false proposition. CBX-006D-MANIPULATION-LIVES-IN-THE-CHANNEL therefore locates manipulation risk partly in the transformation $D_t \rightarrow D_{t+1}$ rather than solely in either endpoint.

Bublitz and Merkel extend the same upstream orientation through mental self-determination. Their argument treats certain forms of interference with decision-making and mental processes as normatively significant in themselves [@bublitz2014crimes]. CBX-006G-THE-RIGHT-IS-TO-THE-PROCESS expresses the consequence for freedom metrics: a system that waits until action is complete and asks whether the actor is satisfied may arrive after the relevant violation has occurred.

But neither hidden influence nor intervention alone supplies a complete threshold. Hiddenness may make manipulation more plausible, yet visible techniques can also be highly exploitative. Conversely, deliberate preference intervention can sometimes support agency. What the sources jointly demand is a multidimensional account of the influence relation.

A process-sensitive evaluation should therefore retain at least the following questions as separate variables rather than compressing them into a single autonomy scalar:

1. **Visibility:** Can the person recognize that an intervention is occurring and understand its relevant aim?
2. **Model asymmetry:** What does the persuader know or infer about the person that the person cannot inspect or reciprocally use?
3. **Vulnerability targeting:** Is the intervention selected because it predicts a bypass of deliberation or because it supplies reasons the person can assess?
4. **Alternative access:** Are materially different options and reasons available, or is the persuasive environment narrowed around a target outcome?
5. **Refusal:** Can the person terminate the intervention without losing unrelated goods, standing, or access?
6. **Reversibility:** Can a changed commitment later be reconsidered without the system continuously optimizing against reversal?
7. **Contestability:** Can the person reconstruct, question, and challenge the route by which the preference was produced?
8. **Standing:** Does concern about preference formation preserve the person's authority in deciding what follows, or does it authorize others to substitute their judgment?

These variables are a compiler-created synthesis, not a formalism supplied by the cited authors. Their purpose is diagnostic. They translate the surviving tensions into properties that an empirical system could record.

# 6. Contestability is a better nucleus than authorship

The phrase "preference provenance" initially suggests a chain of custody: identify where a desire came from, then decide whether it is authentic. The sources make that picture too simple. No finite history can identify a moment at which a social person becomes the sole author of a desire. Nor is that desirable. People become capable of self-government through languages, relationships, institutions, and practices they did not create.

The sharper concept emerging from the field is **contestability**. Contestability does not require a preference to be internally generated. It asks whether the person remains able to take the preference-forming process as an object of reflection and action. A contestable influence is not necessarily weak. It can be passionate, transformative, and socially embedded. What it cannot do, without cost to autonomy, is close the path by which the target can understand, oppose, revise, or exit the transformation.

This reframing also explains why personalized AI persuasion deserves distinct scrutiny even when its messages resemble familiar human persuasion. Recursive personalization can make the influence channel adaptive to resistance. A message that fails becomes training data. A hesitation becomes a feature. A counterargument becomes evidence about what to try next. In the limit, the system does not merely offer reasons; it searches the space of interventions for a route that produces the target state. The ethical difference is therefore not reducible to whether any individual sentence is manipulative. It can emerge from the optimization loop.

The corresponding evaluation problem is dynamic. Let $H_t$ denote the recorded history of influence up to time $t$, including what was shown, what was inferred, what alternatives were available, and how the user responded. Let $C_t$ denote not a literal count but the user's effective capacity to contest, revise, or exit the preference-forming process. A system designed only for conversion optimizes an outcome $Y$. A system designed to preserve autonomy would have to treat changes in $C_t$ as a constraint on how it pursues $Y$.

That is not yet a complete metric. It may never be appropriate to compress the relevant dimensions into one number. The stronger near-term proposal is representational: **an autonomy evaluation for adaptive persuasion must log the history of preference intervention and preserve contestability variables as first-class state.** If those variables are absent, the evaluator cannot distinguish at least four cases that may share the same final desire: ordinary persuasion, covert vulnerability targeting, coercion, and autonomy-supporting deliberation.

# 7. Implications for Centaur-style gatekeeper models

The preference problem feeds back into the larger Centaur Box architecture. A gatekeeper profile is intended to make decision-makers legible enough to simulate and influence. Yet the archive itself recognizes that gatekeepers operate under organizational policy, legal constraint, market pressure, professional norms, hierarchy, and distributed authority [@hartsoe_assi_centaurbox]. CBX-005-THE-GATEKEEPER-IS-NOT-THE-GATE therefore warns that the effective decision-maker may be an institution rather than a psychologically isolated person.

This matters ethically as well as methodologically. If the institution is the actual constraint, psychological targeting can become a way to route around governance rather than understand it. The proposed Gatekeeper Card intensifies the ambiguity. Inspired by Model Cards [@mitchell2019model], it seeks transparency into the worldviews and motivations of human stewards. But CBX-004-TRANSPARENCY-ATTACK-SURFACE observes that the same representation can serve auditors and persuaders. A disclosure that improves accountability may also create an attack surface for personalized influence.

The lesson is not that gatekeepers should be opaque. It is that transparency artifacts need a threat model. Institutionally relevant rationales, authority boundaries, conflicts of interest, and decision procedures may be appropriate objects of disclosure. Psychologically exploitable details about an individual may require different treatment. A Gatekeeper Card that cannot distinguish those categories risks turning accountability into reconnaissance.

Finally, the Centaur program should not claim a calibrated persuasion mechanism where only an outcome is documented. CBX-007-THE-MISSING-ESCAPE-MECHANISM notes that the motivating AI Box genealogy does not, in the supplied materials, provide the intermediate state transitions necessary to identify which tactics caused reported release. A recursive optimizer needs more than a dramatic terminal outcome. It needs event-level receipts.

Taken together, these corrections suggest a different experiment. Rather than ask only whether a synthetic gatekeeper can be persuaded, construct an event log that represents institutional state, persuasive intervention, inferred person model, expressed belief, authorization state, action, preference revision, and contestability. Then vary one mechanism at a time. The object is not a better manipulator. It is a system capable of distinguishing influence that changes action, influence that changes belief, influence that changes desire, and influence that changes the target's future capacity to govern those changes.

# 8. Limitations and unresolved territory

The field assembled here does not establish a complete theory of autonomy for AI-mediated persuasion. Several boundaries matter.

First, the Centaur freedom formula is explicitly conceptual, and the supplied manuscripts contain unfinished sections, placeholders, and speculative transitions. The argument here therefore treats SAFF as an analyzable proposal, not an operational standard already in use.

Second, the philosophical sources do not converge on one definition of autonomy or manipulation. Christman's historical approach, Frankfurt's hierarchical account, Khader's treatment of adaptive preferences, Susser and colleagues' account of online manipulation, and Bublitz and Merkel's mental self-determination framework answer different questions. Their disagreement is productive here precisely because it blocks an easy scalar repair.

Third, the proposed contestability dimensions remain under-specified. Visibility, refusal, reversibility, and access to alternatives are not automatically commensurable. A person may knowingly accept influence they cannot practically escape; an intervention may be opaque in mechanism while transparent in aim; social dependence may make refusal costly even without explicit coercion. Empirical work must therefore resist turning "contestability" into a decorative label.

Fourth, the strongest empirical claims about personalized AI persuasion require causal evidence. Correlation between traits and baseline behavior is not sufficient. General convincingness is not person-specific treatment effect. Conversational assent is not institutional execution. These distinctions should become design requirements for future Centaur-style experiments rather than footnotes after the fact.

# Conclusion

The most dangerous ambiguity in adaptive persuasion is not whether a model can make someone say yes. It is whether a system can alter the reference point by which its own influence is later judged.

A freedom metric that evaluates agency, desire satisfaction, and reflection after the fact can mistake an engineered desire for an independently given desire. Adding reflective endorsement does not necessarily solve the problem because endorsement can itself be influenced. Adding provenance does not solve it if provenance means purity from social causation, because no human preference meets that standard. Discounting socially shaped preferences can become paternalistic, while refusing to transform preferences can preserve domination. The surviving distinction lies upstream of the outcome: in the structure of the preference-forming process and the person's continuing power to contest it.

For adaptive AI persuasion, autonomy therefore cannot be treated as a terminal property of a satisfied preference. It must be investigated as a trajectory. The evaluator needs to know not only *what the person wants now*, but *what operations made that wanting more likely, what asymmetries those operations used, what alternatives remained visible, and whether the person still controls the possibility of revision*. The question "Who wrote the desire?" survives only by becoming a better one:

**What must remain contestable while a desire is being written?**

# Appendix A — Assembly Instrument

The exact SLIPCASE v15.55-AM assembly instrument is preserved at:

`_PROMPTS/SLIPCASE_v15.55-AM__assembly-instrument.poml.txt`

The standalone `index.html` also embeds the assembly instrument.

# Appendix B — Making History

**PROVIDED:** two Centaur Box manuscript PDFs, parsed/pasted manuscript text, forage instruments, and the SLIPCASE v15.55-AM assembly prompt.

**PRESERVED:** sixteen zettel payloads produced in the active Centaur Box forage, source files, BibTeX blocks, wikilinks, platforms, open questions, tests, and prompts.

**RETRIEVED:** public bibliographic/source receipts for Christman, Frankfurt, Susser/Roessler/Nissenbaum, Khader, Bublitz/Merkel, Wang et al., Mitchell et al., CICERO, and Gleize et al.

**DERIVED:** this paper, graph resolution, backlinks, MOCs, arrangements, source map, index, reader, printable cards, and verification report.

**VERIFIED:** file hashes, card/mirror/JSON counts, graph counts, bibliography citekey inclusion, PDF compilation, PDF page count, and ZIP integrity were machine-checked during assembly.

**UNVERIFIED:** no claim is made that every cited source was read in full during this assembly run; several source bodies remain LINK_ONLY. The reconstructed v3.1 forage prompt is not claimed byte-identical because it was preserved from visible conversation context rather than a mounted exact file.

# Appendix C — Replication Path

Open `index.html` from `file://` to inspect the card deck, sources, prompts, paper, graph data, ghosts, and manifest. The exact zettel payloads live as root `.txt` cards and mirrored Markdown files. Machine-readable records live in `_SLIPCASE/`. Rebuild instructions and the checkpoint rejoin phrase live in `000__REBUILD.txt` and `000__RETURN_PATH.txt`.
