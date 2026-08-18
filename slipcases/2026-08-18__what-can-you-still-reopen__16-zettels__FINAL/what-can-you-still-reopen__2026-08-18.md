---
title: "What Can You Still Reopen?"
subtitle: "Adaptive Persuasion and the Contestability of Desire"
author: "Watson Hartsoe"
date: "18 August 2026"
bibliography: SES-20260817-CENTAUR-PREF-01__references.bib
link-citations: true
geometry: margin=1in
fontsize: 10.5pt
papersize: letter
header-includes:
  - \usepackage{microtype}
  - \usepackage{fancyhdr}
  - \usepackage{graphicx}
  - \usepackage{setspace}
  - \usepackage{titlesec}
  - \usepackage{xcolor}
  - \definecolor{ink}{HTML}{171717}
  - \color{ink}
  - \setstretch{1.08}
  - \pagestyle{fancy}
  - \fancyhf{}
  - \fancyhead[L]{\small What Can You Still Reopen?}
  - \fancyhead[R]{\small Working Paper}
  - \fancyfoot[C]{\thepage}
  - \renewcommand{\headrulewidth}{0.2pt}
  - \titleformat{\section}{\Large\bfseries}{\thesection.}{0.6em}{}
  - \titleformat{\subsection}{\large\bfseries}{\thesubsection}{0.6em}{}
abstract: |
  A system asks what a person wants, predicts which action will follow, selects the sentence most likely to move that action, and learns from the result. If freedom is then measured by how successfully action accords with desire, the system can improve the score by altering the reference point used to compute it. Adaptive persuasion therefore creates a measurement problem for autonomy: present desire, reflective endorsement, and successful action may all be genuine features of the person while remaining insufficient evidence about how those states were formed. A purely historical repair also fails, because no desire is untouched by social influence, and some deliberate preference-changing interventions can enlarge rather than diminish agency. The harder distinction lies in the influence relation itself. The relevant question is not whether a preference was influenced, but what remained contestable during and after its transformation. Contestability names a process condition: whether a person can recognize the intervention, encounter alternatives, refuse continuation, revisit reasons, reverse commitments, and participate in subsequent revision. This shifts evaluation from terminal preference satisfaction toward trajectories of preference formation. For adaptive persuasive systems, autonomy is not secured when the system produces a desire the person can endorse. It is secured, if at all, by preserving the person's continuing authority to reopen what the system helped close.
keywords: [adaptive persuasion, autonomy, preference formation, manipulation, contestability, cognitive liberty, personalization]
---

# The Desire Moved First

A system asks what you want.

Useful.

It predicts what you will choose. It compares possible messages. It learns which sentence changes the choice, which framing changes the reason, which reason survives long enough to be repeated back as your own. Nothing needs to cross a bright border between an untouched self and an invading machine. The border can simply become one more variable in the optimization.

That possibility matters because one influential way of talking about freedom starts downstream. A person has goals. The person has information, resources, opportunities. Action follows. Outcomes return as feedback. In the expanded Centaur Box manuscript, this intuition is formalized as a Sapient Agent Freedom Formula: agency is a function of information, resources, and opportunities, self-interest depends partly on desire or objective $D$, reflection incorporates perceived outcomes, and freedom is represented as the product of agency, self-interest, and reflection [@hartsoe_centaurbox_expanded]. The formula is conceptual rather than validated. Its structure is still revealing. Desire enters as an input.

Nearby sits another machine. The shorter Centaur Box manuscript describes persuasion as a recursive process: identify consequential gatekeepers, map their constraints, run scenarios, collect responses, refine appeals, and scale what works through human and artificial agents [@hartsoe_assi_centaurbox]. One architecture treats desire as a reference point. The other treats human response as something to model and move.

Put them together and the reference point no longer stands still.

Suppose a person begins with preference $D_0$. An adaptive intervention changes the person enough that $D_1$ becomes the operative preference. The person can then have ample resources to act on $D_1$, pursue it effectively, and reflect coherently on the outcome. Every downstream signal can improve. The action fits the desire. The reflection fits the action. The desire fits the person as the person now understands themself. A terminal score can rise after the surrounding system has learned how to move the term against which the score is computed.

The problem is not that $D_1$ must be false. It need not be irrational, harmful, imposed, or regretted. The problem is smaller and harder: two people can arrive at indistinguishable present states through different processes, and a measure built only from the present state cannot see the difference.

The desire moved first.

Once preference formation is endogenous to the system under evaluation, preference satisfaction cannot by itself certify self-government.

# Persuasion Is Not One Operation

The word *persuasion* hides too much machinery.

In *Persuasion for Good*, Wang and colleagues collected 1,017 human-human dialogues around charitable donation, annotated persuasion strategies, modeled psychological characteristics, and examined how strategy use related to donation behavior [@wang2019persuasion]. The study matters here less as evidence of machine manipulation than as a lesson in decomposition. Different measured successes arise from different operations.

Consider donation information. The strategy provides concrete information about how the donation will occur. It was the only strategy in the reported main-effects table with a statistically significant positive coefficient on donation [@wang2019persuasion]. A person who already intends to donate may simply need the last meter made visible. The intervention changes execution cost, not necessarily belief. More action does not entail more conviction.

Now consider assent. Among a subset of 236 participants who agreed during the conversation to donate, the study reports that some later reduced the amount and many did not donate at all [@wang2019persuasion]. Speech and execution split. “Yes” is not a terminal state.

The same split becomes sharper in governance. A gatekeeper can agree in conversation while lacking authority to sign, deploy, release, purchase, approve, or override. A verbal concession, a formal authorization, an executable permission, and a completed action belong to different states. Compress them into one binary and the system can look more powerful than it is.

Personality creates another trap. Wang and colleagues report associations between psychological characteristics and donation behavior, including higher donation probability among more agreeable participants in their sample, while also examining interactions between personal characteristics and specific strategies [@wang2019persuasion]. These are not the same quantity. Predicting who is already likely to comply differs from predicting which intervention will cause a particular person to change.

The distinction is mechanical:

$$
P(Y \mid person)
\neq
P(Y \mid person, intervention) - P(Y \mid person, no\ intervention).
$$

The first is susceptibility prediction. The second approaches a person-specific treatment effect. A profile can be accurate about the person and useless about what will move them.

Other source lineages split the target again. IBM-EviConv asks which item in a pair of evidence is judged more convincing and trains a Siamese architecture for that comparison [@gleize2019convinced]. Convincingness ranking does not require a model of a particular target's changing beliefs. CICERO, by contrast, couples language with strategic reasoning in Diplomacy, where communication occurs against an evolving multi-agent state of plans, relationships, agreements, and actions [@meta2022diplomacy]. Its useful lesson is not that a personality portrait unlocks persuasion. It is that strategy lives in state.

Belief change. Action friction. General convincingness. Baseline susceptibility. Person-specific causal response. Strategic state transition. These can all produce something that looks like persuasive success.

Only after they are separated does the autonomy problem become precise. What changed? What performed the change? What information selected the intervention? What could the person still have done instead?

# Reflection Is Also Writable

A natural repair moves upward.

If a first-order desire can be changed, ask whether the person endorses it. Frankfurt's account of freedom of the will makes precisely this kind of hierarchical move by distinguishing desires about action from higher-order desires about which desire should become effective as the will [@frankfurt1971freedom]. Freedom cannot be reduced to whichever impulse happens to win. A person also cares about what moves them.

That deepens the problem. It does not end it.

An adaptive system that can model first-order response can, in principle, model the conditions under which a person endorses that response. The persuader no longer needs only to move $D_0$ to $D_1$. It can search over framings that make $D_1$ appear continuous with the person's values, identity, aspirations, or prior commitments. The certification layer becomes another target surface.

Reflection fails here as a stopping rule because the question recurs:

Who wrote the endorsement?

Christman's historical critique presses directly on this point. A person can possess an integrated, coherent structure of desire while that structure remains the result of manipulation or conditioning; extending coherence over an entire life does not remove the possibility because an entire life can be coherently manipulated [@christman1991autonomy]. The present hierarchy can be internally orderly and historically compromised.

This breaks a convenient assumption. The evaluator cannot inspect only the state at time $t$.

Let $X_t$ contain the currently observable variables: desire, endorsement, resources, action, reflection. Two agents may satisfy

$$
X_t^A = X_t^B
$$

while reaching that state through different trajectories

$$
H_A: X_0 \rightarrow X_1 \rightarrow \cdots \rightarrow X_t
$$

and

$$
H_B: X'_0 \rightarrow X'_1 \rightarrow \cdots \rightarrow X_t.
$$

If the difference between those histories matters to autonomy, no function of $X_t$ alone can recover it.

Autonomy acquires a memory.

But memory creates its own danger. If every external cause counts against authorship, nobody passes.

# No One Is Self-Made

A desire without provenance does not exist.

Parents name objects before children can. Schools reward some forms of attention and punish others. Friends make tastes contagious. Lovers rearrange futures. Therapy changes what a person notices. Argument changes what a person considers reasonable. Illness changes time. Poverty changes feasible aspiration. Advertising changes salience. Institutions make some choices cheap and others nearly impossible. A preference can be social without being stolen.

Christman's historical turn therefore cannot be reduced to a contamination meter. His problem begins from the fact that people are not self-made [@christman1991autonomy]. External causation is ordinary. A provenance term that simply discounts desire in proportion to outside influence would classify human development itself as a defect.

This is where “Who wrote the desire?” becomes too clean.

The answer is usually plural.

The relevant distinction cannot be *self-formed versus externally formed*. It must discriminate among forms of participation in preference formation. Education and coercion can both change a preference. Argument and deception can both change a preference. Seduction, therapy, socialization, propaganda, collective deliberation, and personalized recommendation can all leave a different person behind. The change itself does not settle the case.

Khader's work on adaptive preferences makes the point politically sharp. Preferences can be shaped under unjust conditions and contribute to deprivation without thereby erasing the standing of the person who holds them. Treating a suspect preference as proof that its bearer cannot speak for herself reproduces another form of domination [@khader2011adaptive]. The person remains an agent inside a bad history.

That is the wall.

If preference formation is ignored, manipulation disappears into the final state. If preference formation is treated as a purity test, social life itself becomes disqualifying. If questionable formation automatically lowers the person's authority, protection turns paternalistic.

The missing distinction is not whether another force touched the desire.

Something always did.

# The Channel Matters

The same final desire can be reached through different channels.

Imagine two systems. Both leave a person wanting the same thing. Both leave the person able to explain the choice. Both produce the same action. In one case, the system offers reasons in the open, shows alternatives, and makes its recommendation legible. In the other, it infers a vulnerability from behavioral traces, selects an appeal because that vulnerability predicts response, and hides the selection process.

The endpoint matches.

The route does not.

Susser, Roessler, and Nissenbaum locate online manipulation in precisely this territory: hidden influence, targeted vulnerability, and the subversion of decision-making power rather than simply the production of a bad outcome [@susser2019online]. The moral object shifts from the content of the final preference to the relation through which that preference was changed.

This matters for personalization because personalization produces a second-order informational asymmetry. The target sees the message. The system can see the selection process that produced the message. One side encounters a sentence; the other side may possess a model of why this sentence, now, for this person.

Transparency complicates the picture further. Model Cards were proposed as documentation artifacts for trained models, recording intended uses, evaluation conditions, limitations, and other information needed for responsible use [@mitchell2019model]. The Centaur materials transpose that documentary impulse onto human gatekeepers, imagining “Gatekeeper Cards” that expose developer worldviews and motivations [@hartsoe_assi_centaurbox]. But a representation that supports accountability can also support targeting. The same field that tells an auditor where a decision-maker stands can tell a persuader where leverage sits.

Transparency is not therefore bad. Secrecy is not therefore protective. The point is architectural: information can change roles as it moves. Documentation becomes reconnaissance when the recipient, purpose, and available operations change.

A useful evaluation must therefore ask about the channel:

- Was the intervention recognizable as an intervention?
- Was personalization disclosed at a level that mattered to the target?
- Could the person inspect why the appeal reached them?
- Could alternatives enter the same deliberative space?
- Could the person refuse further optimization without losing unrelated benefits?
- Did the system exploit a vulnerability the person could not reasonably detect or contest?

These questions do not measure whether the person got what they wanted.

They measure what happened to the conditions under which wanting could still be argued with.

# The Right to Change Back

The opposite of manipulation is not noninterference.

That sentence matters because any theory that treats preference stability as the goal will protect domination whenever domination arrives early enough.

Khader's account of adaptive preferences refuses that trap. Some preferences deserve criticism because they are formed under unjust conditions, yet interventions can address those preferences without treating their bearers as inert objects. Preference change can be part of empowerment when people remain active participants in deliberation and in the reconstruction of their options [@khader2011adaptive]. An intervention can alter what someone wants and still enlarge agency.

So the problem is not *preference change*.

It is what the change does to the person's future relation to the preference.

Bublitz and Merkel approach the same territory from mental self-determination. Their account argues that serious interference with decision-making processes can matter independently of whether the eventual decision produces a conventionally bad outcome [@bublitz2014crimes]. The possible wrong can occur upstream, during the production of the willing.

Put these lines together and a different object appears: **contestability**.

Contestability is not the absence of influence. It is the continuing ability to reopen influence after it has begun to settle into preference. It has several dimensions:

**Visibility.** Can the person recognize that an intervention occurred and, where relevant, that it was personalized?

**Inspectability.** Can the person recover the reasons, data, or selection logic that materially shaped what they encountered?

**Alternatives.** Can rival options and rival reasons enter the decision without being silently starved from view?

**Refusal.** Can the person stop the intervention or personalization without disproportionate penalty?

**Revisability.** Can the person return later and reconsider the preference under changed information or changed circumstances?

**Reversibility.** Can consequential commitments be unwound where the domain permits it, or has the intervention rushed the person across an irreversible boundary?

**Relational independence.** Can the person seek other people, institutions, or sources without the optimizing system controlling the whole informational environment?

None of these conditions is sufficient. Some will conflict. A surgical intervention cannot always be reversed. A legal judgment cannot remain indefinitely open. A recommender cannot expose every internal parameter. Contestability is therefore not a universal right to undo reality.

It is a design and evaluation question about where closure occurs, who controls that closure, and whether the person retains meaningful authority over subsequent revision.

The target moves from a terminal score to a trajectory:

$$
D_t \xrightarrow{I_t} D_{t+1}
$$

where $I_t$ is not merely an input but an influence relation with properties of visibility, asymmetry, refusal, and reversibility. Evaluation then asks not only whether $D_{t+1}$ is endorsed, but whether the transition preserves the person's capacity to contest what the transition did.

A desire can fit perfectly and still be tailored.

The harder question is whether the seam can still be found.

# The Gate Is Not a Person

Personalization becomes even less reliable when the target is an institution wearing a person's face.

The Centaur materials describe gatekeepers as people whose decisions shape AI development, while also acknowledging organizational strategy, legal regulation, market pressure, professional norms, hierarchy, and expert roles [@hartsoe_assi_centaurbox]. Once those constraints enter, the gatekeeper stops looking like a sovereign chooser. The person becomes a node inside an authorization path.

Let $F(C,R,V)$ denote the actions feasible under constraints $C$, role authority $R$, and veto structure $V$. A person's preference can select only among actions inside that set:

$$
Decision = \arg\max_{x \in F(C,R,V)} Preference(x).
$$

If the desired action does not belong to $F$, stronger person-level persuasion cannot directly produce it. The persuader must change a rule, a role, a coalition, a credential, a budget, a legal condition, or another veto point.

This is why conversational assent is such a weak proxy for release. The person can say yes while the gate stays shut. A second person may need to sign. A deployment pipeline may reject the request. A compliance rule may forbid the action. The state transition is institutional.

The same correction protects against overclaiming personalized persuasion. A system that accurately models a decision-maker's personality may still fail because personality is not the bottleneck. Conversely, a system may change an outcome without changing anyone's deep preference by locating the procedural hinge: who can authorize, which field must be completed, which review must be bypassed, which sequence converts intent into execution.

The gatekeeper is not the gate.

For autonomy, the implication is broader. Contestability must sometimes belong not only to a person but to an arrangement. A decision can remain personally revisable while becoming institutionally irreversible. A person can regret a click after a contract has executed, a model has shipped, a medication has been administered, or data have propagated beyond recall.

The relevant trajectory therefore crosses scales:

person
$\rightarrow$
interaction
$\rightarrow$
authorization
$\rightarrow$
institution
$\rightarrow$
world state.

Autonomy cannot be rescued at the level of private reflection after the last reversible state has already passed.

# A Test That Can Fail

Contestability is useful only if it can be pressured by evidence.

A minimal experiment does not need to prove that an AI rewrites identity. It needs to separate process from endpoint.

Start with two interventions designed to produce the same target preference. Hold the final choice as constant as possible. Vary the channel.

One condition makes personalization visible, explains why the message was selected, presents viable alternatives, allows the person to pause, and preserves a later route to reversal. Another condition uses equivalent persuasive content but hides personalization, suppresses alternatives, increases temporal pressure, and makes refusal costly. A third condition removes personalization entirely. A fourth allows the person to configure the persuasive objective in advance.

Measure more than conversion.

Measure whether the person can accurately reconstruct why the intervention reached them. Measure whether they can generate alternatives. Measure whether later reflection changes when the optimizing context is removed. Measure willingness and ability to reverse. Measure whether refusal carries material cost. Measure whether the person's stated endorsement persists after disclosure of the targeting mechanism. Measure whether the person can identify which parts of the resulting preference they would choose to keep after learning how it was shaped.

The experiment should be able to embarrass the theory.

If hidden targeting and open deliberation produce indistinguishable later capacities for revision, then some proposed dimensions of contestability are doing less work than expected. If highly personalized intervention improves later deliberative competence, personalization cannot simply be treated as a threat. If non-personalized interfaces reduce alternatives more aggressively than personalized ones, personalization is not the decisive variable. If a person retains strong capacity to reopen a decision despite asymmetric influence, then asymmetry alone is insufficient.

The same discipline applies to freedom metrics. A revised measure should not merely multiply a terminal score by a hand-built “provenance” coefficient. That would smuggle the conclusion into a number. The evaluator needs event structure: what the person encountered, what the system knew, what operations were available, which transitions became irreversible, and which routes to revision remained open.

A useful record looks less like a purity score and more like a ledger of state changes.

INPUT
$\rightarrow$
REPRESENTATION
$\rightarrow$
INTERVENTION
$\rightarrow$
STATE CHANGE
$\rightarrow$
REVISION OPPORTUNITY
$\rightarrow$
NEXT STATE.

The test is not whether influence happened.

The test is whether influence consumed the means by which it could later be challenged.

# What Can You Still Reopen?

Several boundaries remain hard.

Nothing assembled here establishes that current conversational systems can reliably rewrite higher-order commitments. The strongest claim is structural: if adaptive systems become capable of shaping the variables used to certify autonomy, present-state measures become insufficient. The argument identifies a measurement vulnerability before establishing its empirical magnitude.

No validated contestability metric follows from the sources. Visibility, inspectability, refusal, alternatives, revisability, reversibility, and relational independence are candidate dimensions, not a finished scale. Different domains will weight them differently. Emergency medicine, political persuasion, recommender systems, therapy, education, advertising, and AI governance cannot share one frictionless threshold.

Nor does a process-based account eliminate paternalism. Someone still has to decide when personalization is too hidden, when refusal costs too much, when a preference deserves intervention, and when closure is legitimate. Khader's warning remains live: criticizing the conditions under which a preference formed cannot become a license to erase the authority of the person who holds it [@khader2011adaptive].

The institutional problem also survives. Evidence about interpersonal persuasion does not establish how decisions move through organizations whose rules and veto structures may dominate individual psychology. A profile can predict the person and miss the gate.

Those limits narrow the claim. They also make it harder.

A system asks what you want.

Then it learns what will make you choose differently.

Then what will make the new choice fit your reasons.

Then what will make those reasons fit the person you already take yourself to be.

At each step, an evaluator can still point downstream: the person chose; the person endorsed; the person acted; the person reflected. Each statement may be true.

Truth at the endpoint is not enough.

Influence is not enough to condemn the process either. Nothing human survives that standard. Preferences are made in company. They are taught, argued, inherited, revised, loved into being, frightened into being, sometimes pried loose from conditions that once made them seem inevitable.

The remaining question is smaller than “Who wrote the desire?” and worse.

After the sentence has done its work, what can you still reopen?

# References
