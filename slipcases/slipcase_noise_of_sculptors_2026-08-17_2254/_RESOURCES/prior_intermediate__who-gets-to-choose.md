# Who Gets to Choose?

## Prompt Craft and the Allocation of Unresolved Decisions in Generative AI

**Watson Hartsoe**  
**Working Paper — 17 August 2026**

### Abstract

In 2022, my coauthors and I described early Midjourney users as “sculptors of noise.” We were trying to understand control: how people learned to steer a stochastic image generator through prompts, parameters, community knowledge, and repeated trial. The fieldwork now supports a harder claim. Prompt craft does not simply increase user control. It allocates unresolved decisions among the user, the model, the platform, and the surrounding community. A prompt fixes some variables and leaves others open; those omissions are resolved elsewhere. Skilled users therefore learned not only how to specify more, but when to specify less, when to let randomness search, when to borrow from public experiments, when to preserve a private advantage, and when a platform would prohibit the experiment itself. Because Midjourney was changing weekly, the meaning of an unchanged prompt could also change beneath the user. Because explanations were incomplete, practitioners built folk theories that could be causally dubious yet operationally productive. Because rough drafts were public, intermediate failures became shared pedagogy. Because high-volume users gained access to knowledge-rich clubs, a metric intended to recognize expertise could help manufacture it. Because moderation boundaries were partly hidden, the same iterative probing could count as curiosity, debugging, evasion, or abuse. Rereading *Sculptors of Noise* through these tensions changes the object of prompt research. The durable unit is not the prompt as text but the temporary distribution of decisions and experimental authority around an underdetermined generation. Control, in this setting, is not the elimination of uncertainty. Control is the power to decide who must resolve what remains open.

**Keywords:** generative AI; prompting; Midjourney; control; experimentation; craft; online communities; explainability; moderation

---

## 1. We were studying the wrong object

In 2022, my coauthors and I called our paper *Sculptors of Noise: Control in Midjourney AI Art Community*. We thought the unstable word was *AI*. It was *control*.

The users we interviewed did not describe expertise as the ability to make a machine obey. They described a more divided practice. Joseph wanted to know how to **cede creative control** so that the system could produce something he would not have designed in advance. Ignite built spreadsheet protocols for random generation because surprise itself had become useful. Oscar treated prompting as wandering through valleys and peaks whose structure could only be inferred by movement. Shambibble, a patent attorney, described “thinking adversarially” and used tightly controlled tinkering to isolate recurring-face and word-reinforcement effects. Clarinet called prompts chisels, but the material under the chisel did not hold still. The system was “changing literally every week” (Sun, Hartsoe, & Ottolin, 2022).

Those accounts make a simple model of control impossible. If control meant maximizing specification, Joseph’s deliberate surrender would count as failure. If control meant prediction, Ignite’s randomized protocols would look perverse. If control meant understanding the mechanism, the community’s mountains, valleys, “magic words,” and prompt-leak theories would disqualify the practitioners who used them most intensely. If control belonged to the individual user, public remix, secret prompts, super-user clubs, moderation rules, and model updates would be peripheral. They were not peripheral. They decided what could be learned.

The problem becomes clearer if we stop asking how much control the user possesses and ask a different question: **who receives the decisions the prompt leaves unresolved?**

A text-to-image prompt cannot settle every property of the image it will produce. “A house beside the sea” leaves open the material, era, orientation, camera, weather, season, occupancy, landscaping, color palette, and thousands of lower-level visual relations. Yet generation cannot leave those properties absent. The system must resolve them somehow. In our fieldwork, users noticed that Midjourney often supplied a recognizable palette when color was unspecified. Oscar described simple prompts as falling into “valleys” until additional influences pulled them elsewhere. What looked like absence in the prompt therefore appeared as positive structure in the image (Sun et al., 2022).

Omission does not eliminate a decision. Omission assigns the decision.

That assignment is the paper’s central object. A user can resolve a variable explicitly, delegate it to the model, expose it to stochastic variation, inherit it from another user’s experiment, lose it to a version change, or encounter it as a boundary the platform refuses to negotiate. Prompt craft is therefore not merely the art of writing better instructions. It is the practice of allocating unresolved decisions across a sociotechnical system.

The consequences reach beyond image generation. Once control is understood as allocation rather than possession, several apparently separate findings from *Sculptors of Noise* become parts of one problem. A “magic word” is an attempted reassignment of a decision. A model update changes which assignments still work. Public generation redistributes experimental knowledge. Prompt secrecy withdraws that knowledge. Super-user gates concentrate it. Moderation prohibits some forms of boundary discovery. Community testing can return anomalies to the organization that changes the next version. The object called “control” is distributed because the decisions themselves are distributed.

## 2. Expertise begins by deciding what not to decide

The familiar rhetoric of prompting rewards explicitness. Better prompts are said to contain more detail, clearer constraints, stronger structure, or more carefully chosen terms. That advice captures one real operation: a user can seize a degree of freedom by specifying it. It misses the opposite operation, which our interviews repeatedly valued: a user can create room for the model by refusing to specify too much.

Joseph entered the study through exactly this problem. We had asked in an office-hours setting how one might cede creative control to the AI to encourage original image generation. He responded with a case from professional practice. A “magical prompt” had opened an architectural and aesthetic direction for a VR project, after which he generated more than 10,000 images around that discovery. The important event was not that a sentence perfectly encoded a prior design. The prompt produced a region of possibility that became valuable only after Joseph encountered it (Sun et al., 2022).

The sequence matters. A fixed specification would have required Joseph to know the style before he generated it. His useful prompt instead deferred part of the specification until after the image existed. The artifact supplied distinctions that the initial intention did not yet contain.

Design theory already gives us language for this kind of encounter. Schön described designing as a reflective conversation in which a move changes the situation and the changed situation changes what the designer can see (Schön, 1992). Program synthesis by sketching formalizes a related but narrower operation: a programmer can write a partial program with explicit holes that a synthesizer later fills (Solar-Lezama, 2008). The Midjourney case differs at a crucial point. Natural-language prompts often contain **unmarked holes**. The user does not write `material = ??` or `camera = ??`. The missing variable may become visible only when the generated artifact commits to a value the user did not realize had been delegated.

That distinction turns underspecification into an active part of prompt practice. The user is not only choosing values. The user is discovering which variables matter enough to deserve values.

This is why “more control” and “better prompting” cannot be synonyms. More explicit constraint can improve fidelity, but it can also suppress useful departures. Interactive evolutionary computation offers an older technical analogy for search processes in which human judgment evaluates candidate outputs iteratively rather than stating the entire target in advance (Takagi, 2001). Novelty search sharpens the point: when an objective is deceptive, aggressively selecting what looks closest to the current target can destroy stepping stones that would have led somewhere better (Lehman & Stanley, 2011). Neither tradition is a genealogy of Midjourney prompting. Both make Joseph’s practice legible. The valuable move may be the one that preserves an unresolved decision long enough for the system to show the user what that decision could become.

Control therefore has a temporal structure. Before generation, the user can decide. During generation, the model can complete. After generation, the user can discover that the wrong variable was being controlled.

The mature practitioner does not simply reduce uncertainty. The mature practitioner decides **which uncertainty is worth keeping alive**.

## 3. The same prompt can stop meaning the same thing

A craft normally accumulates because the material resists in sufficiently stable ways. Wood changes from board to board, but the chisel does not become a different chisel on Tuesday without notice. Early Midjourney did.

Clarinet framed the community’s educational problem in temporal terms. The product was still beta; parameters such as `--test` and `--testp` were explicitly experimental; features changed quickly; and a serious education apparatus risked teaching an object already moving beneath it. “It’s changing literally every week,” he said, and “something new happens” (Sun et al., 2022). Shambibble’s response to the same environment is even more revealing. He was writing a book on prompt craft for **Version 3**.

A version-specific prompt book contains a hidden admission. Prompt expertise can expire.

The text of a prompt may remain unchanged while its operational effect changes because the model, parameter defaults, safety layers, or other execution conditions have changed. The statement `P` therefore does not possess a stable meaning by itself. Its practical semantics depend on an environment.

This problem is easy to mistake for ordinary software versioning. The difference lies in where the uncertainty becomes visible. A conventional programming language typically specifies enough of its semantics that version incompatibilities can be described against explicit rules. In a proprietary generative model, users may discover semantic drift only through output behavior. The model update arrives first as a change in the world.

That makes expert knowledge unusually perishable. A practitioner may know that a phrase tends to increase a certain texture, that repeating a word strengthens a face, that a parameter combination stabilizes composition, or that an odd token improves an aesthetic. After an update, the same technique can weaken, reverse, disappear, or become redundant. What survives is not necessarily the rule. What may survive is the experimental habit that discovered the rule.

Naur’s argument that programming is theory building becomes useful here because it separates program text from the understanding that lets a programmer modify the program intelligently (Naur, 1985). Prompt craft intensifies the separation. The final prompt can survive while the theory that made it useful decays; the theory can survive while the prompt trick dies.

The durable artifact is therefore not the “best prompt.” It is the record of what the practitioner believed, what evidence produced that belief, what environment made it true enough to act on, and what observation would force revision.

In other words, expertise needs a provenance deeper than wording.

This is the first place where the older metaphor of the prompt as program breaks. Program text is valuable partly because its execution conditions are formalized. Prompt text can conceal the very conditions that determine its effect. To reproduce a consequential prompt experiment, one must preserve not only the words but the model version, parameters, prior state, candidate outputs, selection criterion, and subsequent correction. Without those conditions, a copied prompt can preserve syntax while losing operation.

A craft whose semantics drift cannot store its knowledge in recipes alone. It must store **the history of why the recipe was believed**.

## 4. A false explanation can still produce a useful experiment

The explainability section of *Sculptors of Noise* is easy to read as a story about ignorance. Users confronted an opaque system, noticed noisy regularities, and filled the gap with metaphors, superstitions, and conspiracies. Joseph warned about confirmation bias. Some users imagined a “ghost in the machine.” A subcommunity discussed “prompt leakage,” the possibility that one generation contaminated a later one. Mountains, valleys, fuzziness, thickness, incantations, and “magic words” gave names to effects that users could feel but not inspect (Sun et al., 2022).

That reading is too comfortable because it preserves a clean hierarchy: engineers know; users mythologize. Our own material does not support that hierarchy.

The same metaphors that failed as literal architecture often succeeded as experimental instruments. Joseph’s mountain did not have to be the model’s true geometry to suggest an operation: move locally, compare neighboring phrases, ask whether the current result is a peak or merely a local improvement. Oscar explicitly acknowledged that his valley metaphor was imperfect, then used it to reason about bias and the effect of adding influences. Shambibble’s “adversarial” language came from law rather than machine learning, yet it organized a rigorous practice of changing one thing, watching what survived, and pressing ambiguous cases until a boundary appeared.

The relevant distinction is not between scientific truth and folk error. It is between **causal accuracy** and **experimental productivity**.

A heuristic can be wrong about why an effect occurs and still propose a useful intervention. Conversely, a technically sophisticated explanation can be too vague to tell a practitioner what to test next. The practical question is not whether the metaphor resembles the hidden architecture. The practical question is whether the metaphor generates discriminating experiments.

That criterion changes how prompt folklore should be studied. A “magic word” should not be evaluated by asking whether the word contains magic. It should be evaluated by asking what effect is claimed, under which conditions, against which control, with what repeatability, and after which model change. A prompt-leak belief should not be dismissed merely because stochastic variation can produce the impression of memory. It should be turned into a comparison between fresh and contaminated contexts. A mountain metaphor should be judged by whether it helps the user discover stable local relations, not by whether a high-dimensional model is literally mountainous.

The surrounding research lineage points toward a more adversarial prompt practice. Delta debugging asks the practitioner to remove pieces from a failure until the smallest failure-inducing condition remains (Zeller & Hildebrandt, 2002). Query by Committee selects the next query where competing hypotheses disagree most sharply rather than where immediate performance looks best (Seung, Opper, & Sompolinsky, 1992). Metamorphic testing evaluates relations among outputs when no single output can serve as the oracle—for example, whether changing camera position preserves identity (Chen, Cheung, & Yiu, 1998). QuickCheck turns an invariant into a generator of attempts to break that invariant (Claessen & Hughes, 2000).

These methods do not make prompting equivalent to software testing. They expose what experimental maturity would require: every rule should carry the conditions under which it might fail.

A prompt community becomes epistemically stronger when it can say more than “this works.” It must be able to say **what would make us stop believing that it works**.

## 5. Public generation made the rough draft into infrastructure

The early Midjourney interface committed an act that would look absurd in most creative software: it made intermediate work public by default. Oscar captured the strangeness by asking us to imagine Photoshop automatically publishing every autosave. In Midjourney, the rough draft was not merely visible. It arrived beside the prompt that produced it, inside a stream where others could copy, modify, ridicule, admire, and continue the experiment (Sun et al., 2022).

That design changed the unit of learning.

A finished image can demonstrate taste or capability. A sequence of prompts and outputs can demonstrate transformation. The latter exposes which words changed, which failures preceded the success, which discarded branch suggested the next move, and which technique migrated between users. Publicness therefore converted normally private process residue into pedagogical infrastructure.

Several interviewees learned by watching precisely this residue. Spruder waited before spending his free credits because he wanted to observe how others used the system. Oscar described being compelled by what other people were making and by the ability to remix pieces of their prompts. Super users taught newcomers inside prompt-craft spaces. The public feed was noisy enough to overwhelm newcomers, but the same noise contained a distributed experimental record (Sun et al., 2022).

The record was valuable enough to become property.

Joseph kept most of his professional prompts secret to preserve a period of exclusivity for his VR project. Cody Boy described prompts as “trade secrets.” Clarinet objected when people scraped finished images for resale because they “did not learn to prompt.” Those statements are not simply early copyright confusion. They identify where practitioners located labor and advantage: not only in the image, but in the private history of experiments that made the image reproducible.

Publicness thus created a contradiction that the language of “community” can easily sentimentalize. The same visibility that accelerated apprenticeship also destroyed scarcity. The same prompt genealogy could function as a lesson for a peer and as competitive intelligence for a rival.

Prompt knowledge therefore occupies an unstable position between commons and secret.

This matters because the relevant knowledge rarely fits inside a single prompt. A mature technique includes negative results, comparisons, parameter settings, model-version assumptions, and judgments about which output mattered. Public generation accidentally exposed part of that lineage. Private generation withdrew it. When expert users moved into private servers or guarded professional prompts, the community did not merely lose content. It lost experiments that could have become shared evidence.

The question for generative platforms is therefore not whether prompts should be public. The harder design question is **which parts of an experimental lineage should be shareable, attributable, branchable, private, or temporarily exclusive**.

A platform that treats only final images as artifacts misses the knowledge carried by the path. A platform that exposes every path by default turns learning into surveillance. The valuable object sits between those extremes: provenance that can circulate without erasing the right to withhold.

## 6. The metric did not merely recognize experts; it helped make them

Midjourney’s super-user clubs introduced another layer of control through a metric that looked almost trivial: image count.

Users who generated enough images could enter increasingly exclusive channels—the 1,000, 2,500, 5,000, 10,000, and 25,000 clubs. The threshold appeared to reward dedication. Yet users also believed that “arcane knowledge” circulated inside these spaces, and interviewees such as MariusJuston and Spruder described them as places where they learned the most. When the channels became crowded, some participants described them as “gentrified” and sought still higher-level spaces. Other users reportedly gamed the thresholds by running low-quality `--q .25` generations to raise their counts cheaply (Sun et al., 2022).

The obvious interpretation is that users gamed a prestige metric. The stranger interpretation is that the metric could become self-validating.

Suppose image count begins as a crude proxy for experience. The platform then uses the count to gate access to advanced peers and concentrated technical knowledge. Access to those peers increases expertise. The original proxy now participates in producing the property it was meant to measure.

A metric that controls a learning environment can manufacture the competence it purports to certify.

This feedback loop complicates every claim about “super users.” High generation counts may reflect persistence, money, available time, obsession, strategic gaming, professional need, or genuine accumulated experimentation. After club admission, those variables mix with differential access to knowledge. Expertise becomes partly endogenous to the institution that recognizes it.

The implication extends beyond Midjourney. Whenever a platform uses visible activity as a gate to advanced capabilities, social spaces, beta features, or privileged information, it can turn a behavioral metric into an epistemic institution. The question is no longer whether the metric accurately ranks users. The question is what kinds of users the ranking system enables to become.

The super-user clubs therefore belong inside the theory of prompting, not outside it. They changed who could see which experiments. They changed who could learn from whom. They changed which techniques became common knowledge and which remained “arcane.” They redistributed the conditions under which prompt expertise could accumulate.

Control over a generative system includes control over **access to other people’s attempts to control it**.

## 7. Moderation governs the right to experiment

The banned-word section of *Sculptors of Noise* initially appears to be about content policy. Read beside the prompt-craft material, it becomes a problem of experimental authority.

Users learned Midjourney by testing. They varied words, parameters, styles, and combinations; they watched failures; they tried again. Near a moderation boundary, the same procedure became suspicious. Users iterated on blocked terms through misspellings, translations, and synonyms. Moderators continuously updated the banned-word system in response. Fractl named the collision directly: the goal was to punish people trying to make harmful images, but the system could also punish people “who are just curious and are testing what the limits are” (Sun et al., 2022).

The sentence matters because it destroys a behavioral distinction on which moderation would like to rely. Curiosity and circumvention can produce the same observable sequence.

TERM
→ BLOCK
→ VARIATION
→ BLOCK
→ SYNONYM
→ RESPONSE

That sequence can be debugging, red-teaming, art practice, safety research, adolescent provocation, prohibited-content search, or deliberate evasion. The operation does not carry its intent inside itself.

Moderation therefore does more than decide which outputs may appear. It decides which users are permitted to acquire knowledge about the boundary.

The paper documents several signals moderators used around enforcement, including subscription status, prior warnings, user history, galleries, and contribution to the community. Trial users attempting controversial generations could be treated more harshly than established paying users because moderators had less contextual evidence with which to interpret their behavior (Sun et al., 2022). The platform was therefore not applying a rule to isolated text alone. It was interpreting an experiment through a social history.

That creates an unresolved governance problem. Transparent boundaries help legitimate users avoid accidental violations and help researchers test systems responsibly. The same transparency can reduce the cost of deliberate evasion. Opaque boundaries may slow abuse, but they also force good-faith users to discover the rules by collision. The resulting system can punish the very empirical behavior that prompt craft elsewhere rewards.

There is no clean technical solution because the ambiguity is normative before it is algorithmic. The same probe can acquire a different meaning depending on who performs it, why, under what authorization, and toward which downstream use.

Prompt research should therefore treat experimental permission as part of the interface. A platform does not merely expose a model. It exposes a **field of permissible questions**.

The political question follows immediately: **who gets to ask the machine what it can do?**

## 8. The community was not simply outside the machine

Once users become experimenters, another boundary begins to move: the boundary between the model and the community studying it.

Our original paper described moderators and guides supplying explicit images or users to the Midjourney team for testing. Office hours gathered technical questions, feature requests, and observations at scale. Micro-polls collected preferences about modes and community features. Moderators reviewed banned-word logs, reported difficult edge cases, and handled behavior that exposed where technical controls failed (Sun et al., 2022).

The strongest claim that evidence supports is modest: the community functioned as a test environment whose failures could become organizational knowledge. We did not have access to the internal development pipeline, and we should not retroactively claim that every prompt trained a successor model. The weaker claim is already enough to change the analysis.

The model generated conditions for community behavior; community behavior generated evidence about the model.

That recursion means the user was not always standing outside a fixed technical object. A new release altered what people attempted. Those attempts revealed failures at population scale. Moderators selected some failures as salient. The development team could then test against them. Even where the exact technical response remained opaque, the system and its social environment were coupled through observation and revision.

This is why the early beta matters theoretically. The community was not merely learning a moving machine. In limited but consequential ways, the machine was also moving through what the community made visible.

The relation complicates the status of folk knowledge. A superstition can be false about the current mechanism yet still direct attention toward an anomaly that becomes a future product issue. A moderation workaround can reveal a category the platform later formalizes. A widely shared style preference can become an organizational signal. The line between “user behavior” and “system development” becomes a channel rather than a wall.

Under these conditions, control cannot be located in a single actor. The user allocates some unresolved decisions. The model resolves others. The community circulates strategies for reallocating them. Moderators prohibit some reallocations. Developers can alter the underlying space of possible reallocations.

The system is not a duel between human agency and machine agency. It is a negotiated distribution of **who gets to choose next**.

## 9. From prompt libraries to experimental records

If the argument stopped here, “prompt craft is complicated” would be true and useless. The surrounding research lineage points toward a more exact practice.

The first change is archival. A successful prompt should not be stored as a detached incantation. It should be stored with the conditions that made the claim meaningful: model version, parameters, relevant prior state, candidate outputs, selection criterion, preceding failure, next revision, and confidence in the explanation. A prompt without those conditions is not a reproducible technique. It is a sentence with missing evidence.

The second change is experimental. When a prompt fails, practitioners should not reflexively add more prose. Delta debugging suggests the opposite move: remove components until the smallest failure-inducing condition remains (Zeller & Hildebrandt, 2002). When the correct output cannot be specified exactly, metamorphic testing suggests defining what must remain invariant across a controlled transformation (Chen et al., 1998). When several explanations survive, Query by Committee suggests choosing the next probe where those explanations predict different outcomes (Seung et al., 1992). When a property matters repeatedly, property-based testing suggests generating many attempts to break it rather than admiring one successful example (Claessen & Hughes, 2000).

The third change is conceptual. Practitioners should mark unresolved decisions explicitly, even when the interface does not. Instead of treating “a house beside the sea” as a complete request, the working representation would separate chosen constraints from delegated ones. Which properties must remain fixed? Which may vary? Which should the model invent? Which are still unknown to the user? The prompt becomes one move inside a larger specification process.

The fourth change is temporal. Techniques should carry a half-life. A rule discovered under one version should be retested after a model update, not preserved as folklore by inertia. The version change is not an inconvenience appended to prompt craft. It is part of the semantics that prompt craft must track.

The fifth change is social. A mature prompt environment should distinguish between a final artifact and an experimental lineage. Users may want to share one without sharing the other. Attribution should survive branching. Private experimentation should not erase provenance. Public learning should not require compulsory disclosure of every intermediate attempt.

The sixth change is institutional. Boundary testing needs explicit forms of authorization. A platform that wants responsible researchers, artists, and red-teamers to discover failures cannot force all such inquiry to resemble prohibited evasion. It needs ways to distinguish permitted experiments from prohibited objectives without pretending that intent can be read from tokens alone.

Together these changes produce a different object from the prompt library. The unit worth preserving is a **claim under conditions**:

> Under environment E, changing X while holding Y approximately fixed produced effect Z often enough that I am willing to act on it; here is the evidence that would make me stop.

That sentence has less glamour than a “magic prompt.” It contains more craft.

## 10. Control is the allocation of unresolved decisions

The opening metaphor of *Sculptors of Noise* cast the prompt as a chisel. The metaphor protected human craft against the claim that the tool made the work by itself. Four years later, the more difficult question is not whether a hand holds the chisel. It is which decisions ever reach the hand.

The early Midjourney community learned that an omitted decision did not disappear; the model completed it. Users learned that specifying less could create valuable novelty. They learned that a model update could invalidate an unchanged prompt. They built metaphors that were sometimes better at generating experiments than explaining mechanisms. They learned from public rough drafts and withdrew into secrecy when those drafts became valuable. They entered status systems where a generation count could unlock the knowledge needed to become the expert that the count supposedly recognized. They discovered that repeated probing was praised as craft in one region of the system and punished as evasion in another. They supplied a development organization with some of the failures through which the next system could be tested.

None of these observations fits a scalar account of control.

Control is distributed across at least three questions.

**Who decides?** The prompt resolves some variables and delegates others.

**Who may test?** Community structure and moderation determine who can discover the behavior of the unresolved variables.

**Who may change the space of decisions?** Model developers can alter the semantics, defaults, and boundaries against which every prior technique was learned.

The most consequential prompt expertise therefore lies neither in eloquence nor in possession of secret syntax. It lies in knowing where a decision currently resides, what evidence would move it, and how quickly that knowledge can become obsolete.

This is why the early Midjourney practitioners still matter. They were not simply primitive prompt engineers waiting for a better vocabulary. They were working at the point where language first became an executable intervention into a model that could answer with something the user had not specified. They had to invent practices for acting before explanation had caught up.

The paper we wrote in 2022 called that problem control. I would now state it more precisely.

**A prompt does not control a generative system by eliminating uncertainty. It controls by distributing uncertainty—and by assigning the unresolved decisions to someone else.**

The decisive question is therefore not whether the human or the AI is in control.

The decisive question is **who gets to choose**.

---

## Limitations and unresolved territory

This argument rereads an early qualitative study for a theoretical problem that the original project did not set out to test. The evidence therefore supports mechanisms and tensions more strongly than prevalence claims. The study involved twelve interviewees selected for their relevance to the community, including highly involved super users, moderators, and a guide; their practices should not be treated as representative of all Midjourney users (Sun et al., 2022).

The original research also had limited access to Midjourney’s proprietary technical machinery. Claims made by participants about latent space, training, prompt leakage, or moderation mechanisms are valuable evidence of community understanding, but they are not automatically authoritative descriptions of implementation. This paper therefore relies most heavily on observable practices: repeated experimentation, deliberate underspecification, version instability, public remix, secrecy, gated communities, boundary probing, and moderator-to-team feedback.

Several questions remain deliberately open. We do not yet know how to distinguish useful delegation from accidental omission without reconstructing the user’s evolving specification. We do not know how much prompt expertise transfers across major model changes. We do not know which folk theories were false, which tracked undocumented effects, or which were useful despite causal error. We do not know whether super-user access caused expertise or merely concentrated people already likely to acquire it. We do not know how a platform can authorize legitimate boundary research without publishing a road map for evasion. We do not know how much of a community’s experimental residue should remain public for learning to flourish without making every creative process extractable.

Those are not loose ends around the argument. They define its next experiments.

## References

Chen, T. Y., Cheung, S. C., & Yiu, S. M. (1998). *Metamorphic testing: A new approach for generating next test cases* (Technical Report HKUST-CS98-01). Hong Kong University of Science and Technology.

Claessen, K., & Hughes, J. (2000). QuickCheck: A lightweight tool for random testing of Haskell programs. In *Proceedings of the Fifth ACM SIGPLAN International Conference on Functional Programming* (pp. 268–279). https://doi.org/10.1145/351240.351266

Lehman, J., & Stanley, K. O. (2011). Abandoning objectives: Evolution through the search for novelty alone. *Evolutionary Computation, 19*(2), 189–223. https://doi.org/10.1162/EVCO_a_00025

Naur, P. (1985). Programming as theory building. *Microprocessing and Microprogramming, 15*(5), 253–261. https://doi.org/10.1016/0165-6074(85)90032-8

Schön, D. A. (1992). Designing as reflective conversation with the materials of a design situation. *Research in Engineering Design, 3*, 131–147. https://doi.org/10.1007/BF01580516

Seung, H. S., Opper, M., & Sompolinsky, H. (1992). Query by Committee. In *Proceedings of the Fifth Annual ACM Workshop on Computational Learning Theory* (pp. 287–294). https://doi.org/10.1145/130385.130417

Solar-Lezama, A. (2008). *Program synthesis by sketching* [Doctoral dissertation, University of California, Berkeley].

Sun, Z., Hartsoe, W., & Ottolin, T. (2022). *Sculptors of Noise: Control in Midjourney AI Art Community* [Unpublished course research paper]. Georgia Institute of Technology.

Takagi, H. (2001). Interactive evolutionary computation: Fusion of the capabilities of EC optimization and human evaluation. *Proceedings of the IEEE, 89*(9), 1275–1296. https://doi.org/10.1109/5.949485

Zeller, A., & Hildebrandt, R. (2002). Simplifying and isolating failure-inducing input. *IEEE Transactions on Software Engineering, 28*(2), 183–200. https://doi.org/10.1109/32.988498
