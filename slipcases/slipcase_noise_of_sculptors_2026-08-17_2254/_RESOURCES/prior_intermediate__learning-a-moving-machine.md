# Learning a Moving Machine
## Prompt Craft as Vernacular System Identification

**Watson Hartsoe**  
**Working Paper — 17 August 2026**

### Abstract

Prompting is commonly framed as instruction writing: a user states an intention, a generative model executes it, and expertise consists in finding better words. An early ethnography of the Midjourney community, *Sculptors of Noise: Control in Midjourney AI Art Community* (Sun, Hartsoe, & Ottolin, 2022), captured a practice that was already much stranger. Expert users generated tens of thousands of images, treated trial and error as a teacher, mapped “latent space” with improvised metaphors, guarded some prompts as trade secrets while learning from public remix, gamed image-count thresholds to enter knowledge-rich super-user spaces, and probed moderation boundaries whose rules were partly hidden. The model itself was changing weekly. This paper rereads that fieldwork as evidence of **vernacular system identification**: a socially distributed practice of learning an opaque, stochastic, and changing machine from repeated input-output encounters without access to its internal model. The claim is analogical, not genealogical; Midjourney users were not running formal identification algorithms. Yet the comparison exposes a set of unresolved mechanisms that “prompt engineering” hides. Silence in a prompt delegates decisions to model defaults. Prompt expertise has a half-life when model versions change. Folk theories can be causally wrong yet operationally productive. Public generation turns rough drafts into pedagogical infrastructure while simultaneously destroying process secrecy. Metrics used to recognize experts can create expertise by controlling access to expert communities. Moderation governs not only content but who may probe the system. Finally, contemporary generative interfaces make some formerly speculative variables—persistent context, model-added style, personalization, user-feedback pipelines—explicit. The resulting argument is that prompt expertise is not primarily a stable linguistic competence located in an individual. It is temporary, experimental, infrastructural, and political: knowledge of how to act on a moving machine whose response surface, memory, defaults, and permissible tests are partly controlled elsewhere.

**Keywords:** prompting; generative AI; Midjourney; system identification; black-box experimentation; online communities; explainability; moderation; craft

---

## 1. The prompt is a probe

In the opening of *Sculptors of Noise*, one Midjourney user rejects a familiar account of AI image generation. “We are sculptors of noise,” Clarinet says; prompts are chisels whose “force, angle, strength, specificity, and other ineffable things” matter to the result (Sun et al., 2022). The image is memorable because it refuses two reductions at once. It refuses the claim that the machine acts alone, but it also refuses the idea that the prompt simply specifies the image. A chisel does not describe the sculpture. It is an intervention into material whose behavior has to be learned.

That distinction is easy to lose in the vocabulary that later formed around “prompt engineering.” The phrase encourages a view of the prompt as a compact technical object: an instruction whose quality can be improved through wording, ordering, examples, constraints, or parameters. Sometimes that description is adequate. But the early Midjourney field site captured a different and more consequential activity. The research team spent more than one hundred hours participating in the Discord community and conducted more than fifteen hours of semi-structured interviews with twelve users, including moderators, a guide, a regular user, and super users (Sun et al., 2022). Across those observations, skilled use repeatedly appeared not as the possession of a definitive sentence but as an experimental practice. “Trial and error is the teacher,” the paper concludes in its prompt-craft section. Users changed words, compared results, generated large families of images, kept spreadsheets, formed theories, watched one another work, and revised their understanding of the machine.

Joseph, a professional creative director, described finding a “magical prompt” that opened an aesthetic and architectural style useful for a VR project and then exploring that discovery through more than 10,000 generations. Ignite developed spreadsheet protocols that combined hundreds of artists, styles, and nouns to produce randomized experiments. Shambibble’s patent-law background led him to describe his own approach as adversarial and empirical. Oscar tested stereotypes and biases and constructed visual maps of what he called Midjourney’s “latent space.” These are not merely anecdotes about colorful early adopters. They identify the actual epistemic problem of prompting: the user must decide what to do next while the causal structure relating words, parameters, model state, stochastic sampling, and output remains only partially visible.

Control theory has a useful, if deliberately limited, term for a neighboring problem. System identification is the practice of building models of a dynamic system from observed input-output data (Ljung, 1999). In formal engineering, identification can involve deliberately designed signals, mathematical model classes, estimators, validation procedures, and explicit criteria for informative experiments. Midjourney users were not doing this in any strict sense, and no historical influence is implied. Their objects were images rather than transfer functions; their models were often metaphorical; their evaluation criteria could be aesthetic and mutable. Nevertheless, “system identification” makes one hidden feature of prompt craft legible: a prompt can be a **probe** before it is an instruction.

The difference matters. If a prompt is primarily an instruction, a failed generation asks: *How should I rewrite this request?* If it is also a probe, failure asks additional questions: *What did this input reveal about the system? Which variable changed? What competing explanations survive? What experiment would distinguish them?* Prompt practice becomes a form of empirical inquiry into a machine that is encountered from the outside.

This paper argues that the most productive rereading of *Sculptors of Noise* is therefore not as an early catalogue of prompt tricks but as an ethnography of **vernacular system identification under drift**. The term “vernacular” matters. The users did not possess an official language for the system’s internal mechanisms. They constructed working vocabularies from outputs: magic words, mountains and valleys, “fuzzy” and “thick” models, a “ghost in the machine,” prompt leakage, recurring colors, stylistic gravity. Some of those explanations were almost certainly wrong, some were technically imprecise, and some may have tracked real but undocumented effects. Their practical problem was precisely that these categories could not be cleanly separated from the interface.

Reading the fieldwork this way brings together observations that otherwise look unrelated: omitted prompt details, version changes, superstition, secrecy, public remix, super-user clubs, banned-word probing, and community feedback. They are all conditions on what can be learned about the machine. The central object is not the prompt alone. It is the experimental relation among user, interface, model version, public community, platform rules, and the history of prior outputs.

## 2. A field site organized around uncertainty

The 2022 Midjourney community was an unusually revealing site because neither the product nor the knowledge surrounding it had stabilized. The research team found a public system whose interface looked mature enough to purchase and use professionally while still behaving like a beta. Clarinet pointed to explicitly experimental parameters such as `--test` and `--testp` and complained that users expected product-level consistency from features literally labeled as tests. His explanation of the onboarding problem was temporal: “it’s changing literally every week [and] something new happens” (Sun et al., 2022). The problem was not merely inadequate documentation. Documentation itself was trying to describe a moving target.

The paper’s community-design frame originally treated this instability as one challenge among many: onboarding, scaling, moderation, user roles, publicness, copyright, and prompt craft. With hindsight, instability can be read as the condition linking them. A community had to learn a machine while the object of learning was changing. It had to distinguish randomness from updates, useful heuristics from superstition, and durable skill from version-specific accidents. It had to decide which discoveries should circulate publicly and which could be privately owned. Moderators had to enforce behavioral rules against a generator whose ability to realize problematic requests was itself improving. Users were simultaneously customers, experimenters, teachers, competitors, and—in some contexts—sources of feedback to the organization building the system.

This is a very different epistemic environment from learning a conventional deterministic tool. When a Photoshop command behaves unexpectedly, the practitioner can often assume that the software has a stable specification, consult documentation, repeat the operation, and isolate user error. In the Midjourney field site, repetition itself did not guarantee diagnosis because output varied stochastically, interfaces and models changed, documentation lagged, and the platform did not expose a causal trace explaining how each word affected each image. Joseph explicitly compared perceived changes in the system to coin flips: after several surprising outcomes, users could feel as though the model had changed or remembered previous prompts even when random variation was sufficient to explain the pattern.

The paper calls some of the resulting beliefs “superstition and confirmation bias.” That description is important but incomplete. Superstition did not arise in opposition to experimentation. It often arose *from* experimentation conducted without enough observability to identify the cause of an effect. The same repeated input-output encounters that produced genuine craft knowledge could also produce false causal stories. That is the first deep tension in the field: the practice needed empirical learning, but the structure of the system made empirical learning unusually vulnerable to misattribution.

The rest of the paper follows the consequences of that tension.

## 3. Silence is delegated control

One of the least dramatic observations in *Sculptors of Noise* may be one of its most consequential. Super users noticed “a common color palette” in Midjourney images when prompts did not specify colors or branding (Sun et al., 2022). Shambibble praised the model’s ability to take “a vague notion” and fill in details that “look cool.” Oscar’s valley metaphor described simple prompts as falling into familiar regions until additional influences gave them somewhere else to go.

These observations imply that omission is not neutral. An image must still have a color palette when the prompt names no colors. It must still have a composition when the prompt names no composition, a lighting condition when none is specified, and some answer to innumerable other questions the user may not even realize they have delegated. The missing instruction does not create an empty variable in the output. It transfers decision authority.

This can be stated more precisely. Let a prompt explicitly constrain some subset of consequential variables, S. Let U be the remaining variables that still require values for generation to complete. The practical behavior of the system is not simply:

> prompt → image.

It is closer to:

> explicit constraints S + unresolved variables U → model completion of U → image.

This is not a claim about one internal algorithm. It is a description of the control relation visible at the interface. A user who omits a dimension is permitting some combination of model prior, learned correlations, product tuning, active parameters, stochastic sampling, and other context to settle it.

Contemporary Midjourney documentation makes this older observation newly legible without resolving its historical mechanism. In current documentation, Midjourney explicitly says that Standard mode adds its own “creative touch,” while Raw reduces that automatic treatment; the `--stylize` parameter controls how strongly Midjourney applies its learned artistic training, and model versions may handle prompts differently (Midjourney, n.d.-a, n.d.-b, n.d.-c). These current features cannot be projected backward to prove what produced the 2022 common palette. They do, however, confirm that the relation between stated prompt and generated artifact is productively understood in terms of **delegated degrees of freedom**. Modern interfaces increasingly make some of those degrees explicit.

This reframes an old debate about model “creativity.” When a model adds a compelling architectural material or composition that the user did not specify, one description says the model contributed creatively. Another says the user delegated an unmarked variable that the model completed. These descriptions are not mutually exclusive. They describe the same event at different levels. The more useful research question is not whether the choice deserves the word creativity, but **which choices were delegated, under what defaults, and how strongly those defaults constrained the reachable artifact space**.

The practical implication is severe. Prompt comparison that looks only at text can miss the largest source of control: what the text leaves open. A robust prompt practice should therefore be able to produce a *default map*. Start with a heavily specified description. Remove one specification at a time. Observe the distribution that replaces it. Reintroduce counter-specifications. Repeat across model versions. The resulting object is not a better prompt. It is an empirical account of the system’s response to silence.

## 4. Expertise has a half-life

If omission makes prompt semantics dependent on the model, model updates make expertise historically unstable. The 2022 fieldwork contains this problem everywhere. The system was “changing literally every week.” Shambibble was writing a book specifically about prompt craft for Version 3. Joseph’s “magic words” were empirical discoveries tied to a particular system state. The paper records a community trying to stabilize advice at the same time the object of advice was moving.

Current Midjourney documentation states the issue directly: different model versions may “handle prompts differently” and possess different artistic styles (Midjourney, n.d.-b). That sentence turns an ethnographic tension into an explicit property of the interface. The identical text can cease to be the same operation when the execution environment changes.

The resulting distinction is between **prompt identity** and **operational identity**. Two prompts can be textually identical while operationally different because they are run against different model versions, default settings, reference systems, personalization states, or sampling behavior. A prompt repository that saves only text therefore confuses syntax with execution context.

This is why prompt expertise has a half-life. The phrase does not mean that all skills become obsolete at the same rate. It suggests a research program for separating brittle knowledge from transferable practice. A version-specific incantation may die quickly. A method for designing comparisons, reducing failures, preserving seeds, or testing an invariant may survive. The distinction is similar to Naur’s argument that programming expertise cannot be reduced to possession of program text: maintainability depends on a theory of the matter at hand that explains why the program has the form it does (Naur, 1985). In prompt practice, the need is even more acute because the environment can change without the prompt changing.

The fieldwork offers a natural way to study this. Recover historically successful prompt techniques and replay them across still-available model versions. Classify each as stable, weakened, amplified, reversed, obsolete, or formalized into an explicit feature. Then ask a harder question: which practitioners were good at predicting what would survive? If the transferable skill is not the phrase but the experimental method used to discover and validate it, then “prompt engineering” names the wrong durable competence.

There is also a temporal asymmetry in documentation. By the time a technique becomes teachable, the model may have changed. This creates a peculiar knowledge economy: the most current knowledge is often the least validated, while the most validated knowledge is often about yesterday’s system. The 2022 super-user channels, guide roles, office hours, unofficial manuals, and private servers can be read as attempts to solve this synchronization problem socially.

## 5. Wrong theories can still work

The paper’s most vivid epistemic material appears in its discussion of “magic.” Users confronted a generator that was highly responsive yet weakly explainable. Some beliefs were explicitly framed as conspiracies. “Prompt leakage” referred to the idea that Midjourney remembered earlier prompts and allowed them to affect later generations. Joseph understood enough probability to reject a simple version of the theory, yet admitted that certain experiences still made the possibility emotionally compelling. Users also tied themselves to phrases such as “trending on ArtStation,” “4K,” “Behance,” “photorealistic,” and “Unreal Engine,” sometimes attributing more causal power to them than Joseph thought they deserved. He estimated that such additions could sometimes move a strong result from “95% to 97%,” rather than from zero to ninety.

It would be easy to conclude that expert knowledge is simply what remains after superstition is removed. The paper’s own evidence points somewhere more interesting. Metaphors, guesses, and partial explanations were also “valuable currency” for improving outputs and organizing subcommunities. Joseph’s mountain-peak metaphor, Oscar’s valleys and galaxies, and other informal theories gave users ways to decide where to search next. Even when a metaphor was ontologically wrong, it could be experimentally productive.

This requires separating three properties of a folk theory:

1. **Causal accuracy:** does it correctly describe the mechanism?
2. **Predictive usefulness:** does it help anticipate outcomes?
3. **Control usefulness:** does it suggest interventions that reliably improve or diversify outcomes?

These properties need not coincide. A user can hold a poor causal model that nevertheless recommends a productive search strategy. “Move out of the valley” may be a bad description of the generator’s internal geometry but a good instruction to perturb a prompt that has converged on repetitive outputs. Conversely, a technically correct general explanation of diffusion may be too coarse to tell the user which noun to remove next.

This is not an argument for superstition. It is an argument for testing it more carefully. Black-box practice should not ask only, “Is this explanation technically true?” It should also ask, “What intervention does this explanation recommend, and does the effect replicate under controls?” Zeller and Hildebrandt’s delta debugging offers one useful discipline: when a prompt reliably induces a failure or effect, systematically remove parts until the smallest sufficient condition remains (Zeller & Hildebrandt, 2002). Query by Committee offers another: choose the next probe not because it is likely to produce the prettiest result but because competing explanations predict different outcomes (Seung, Opper, & Sompolinsky, 1992). Metamorphic testing contributes a third: when there is no single correct output, define relations that should remain stable under controlled prompt transformations (Chen, Cheung, & Yiu, 1998).

These methods do not turn aesthetic practice into software testing. They provide a vocabulary for distinguishing useful experience from uncontrolled anecdote. The unexplained “magic word” becomes a claim with an effect size, a boundary, a version, and a replication history.

The historical reversal of prompt leakage makes the distinction especially important. For the 2022 Midjourney setting, the paper presents cross-prompt memory as a community theory rather than an established mechanism. In contemporary conversational AI, however, prior state can be explicitly causal. OpenAI’s current documentation states that, when relevant memory and chat-history settings are enabled, information from prior conversations may be brought into later conversations (OpenAI, n.d.). The phenomenological complaint—“something I said earlier seems to be affecting this”—can therefore arise from entirely different mechanisms across systems: randomness, confirmation bias, visible conversation context, saved memory, retrieval, personalization, or a bug.

The lesson is not that the 2022 users were retrospectively right. It is that **state provenance has become part of prompt semantics**. A contemporary prompt experiment is uninterpretable unless the practitioner knows what prior state was available to the model. The older superstition becomes a warning against universal advice such as “each prompt is independent.” Whether that statement is true is now an architectural property, not a general principle of prompting.

## 6. The rough draft became public infrastructure

Midjourney’s early publicness generated another epistemic transformation. Oscar compared the default experience to Photoshop automatically publishing every autosave. The comparison is sharper than a generic claim about social media. Traditional creative systems tend to make publication the end of a process. Midjourney could make publication a byproduct of the process itself. Intermediate prompt-output pairs, abandoned attempts, near misses, and surprising variations became visible to strangers.

Oscar described seeing other people’s outputs and remixing their prompts as a major source of motivation and learning. The paper also reports the opposite orientation. Cody Boy described prompts as “trade secrets.” Joseph kept most of his prompts secret to preserve a period of exclusivity for professional work. Clarinet distinguished prompt learning from simply scraping high-resolution outputs and selling them. The platform therefore placed two goods in direct conflict:

> process visibility → apprenticeship, remix, serendipity, collective search

and

> process visibility → appropriation, loss of exclusivity, strategic secrecy.

The conflict is deeper than copyright. What is being contested is the status of **process information**. A final image is one informational object; the genealogy that produced it is another. Public-by-default generation made the latter unusually observable. In doing so it created what can be called pedagogical infrastructure: novices could learn not only from exemplary results but from the sequence of attempts surrounding them.

This proposition is testable. Compare novices who can see only selected final outputs with novices who can inspect full prompt-output genealogies, including failures. Give both groups a novel task and measure transfer, diagnosis, iteration count, and ability to explain why a modification worked. If genealogy exposure produces better transfer, the discarded intermediate states are not waste. They are instructional material.

Publicness also makes prompt expertise socially distributed. Ignite described Midjourney as an “endless mode game” whose story is made through prompts. Oscar called it a “multiplayer Imagination game” in which one person asks what something might look like and another riffs on the result. In such a setting, the causal predecessor of a prompt is not necessarily another prompt written by the same person. It may be someone else’s image, a failed attempt in the feed, a recurring joke, or an unexpected stylistic collision. The prompt is a move in a collective process.

This is where the language of individual “prompt skill” becomes misleading. The same person placed in a private interface and in a dense public remix environment may explore differently because the search topology has changed. A person can be more capable because they are surrounded by visible experiments. Expertise may belong partly to the network.

Contemporary Midjourney still describes itself as open by default while offering paid privacy controls; creations can be publicly discoverable unless users employ Stealth mode in appropriate contexts (Midjourney, n.d.-d). The product has therefore retained the tension rather than resolved it. Privacy is not merely a personal-data setting. It also controls whether the process can feed the social learning environment.

## 7. A metric can create the expert it claims to recognize

The early super-user clubs introduce an even stranger mechanism. Access was tied to generation counts: 1,000, 2,500, 5,000, 10,000, and 25,000 images. Users believed that “arcane knowledge” circulated in these spaces. MariusJuston and Spruder described them as among the places where they learned the most. Yet the paper also reports users “gaming” the threshold by running low-quality `--q .25` prompts to increase their counts more cheaply. As clubs filled, some expert users described them as “gentrified” and moved toward still higher-level spaces.

At first glance, this is simply a Goodhart-style story: once a metric becomes a target, people optimize the metric rather than the underlying quality. But the social topology makes the result more complicated. Suppose generation count C is used as a proxy for expertise E. The platform then grants high-C users access to a community K containing more experienced peers and more advanced knowledge. If K increases E, then the metric no longer merely measures expertise. It participates in producing it:

> experience → count → club access → knowledge → more expertise.

A user who games the count may enter without the expected level of expertise, yet entry itself may accelerate learning. The credential can be simultaneously bad measurement and effective intervention.

This suggests the term **metric-gated epistemology**: access to knowledge is allocated through a behavioral proxy that can reshape the distribution of the knowledge it is supposed to recognize. The phenomenon deserves more careful causal study than the 2022 project could provide. A threshold design could, in principle, support a regression-discontinuity-style comparison of users immediately below and above access boundaries. Did users improve after crossing? Did vocabulary, experimentation strategy, or network ties change? Were money and available compute silently converted into epistemic status because image counts depended on subscription and GPU access?

The deeper question is what the count actually measured. It may have been a noisy proxy for craft skill, but it also measured obsession, free time, money, persistence, willingness to experiment, or willingness to game platform mechanics. Any of those characteristics could predict participation in expert culture. The category “super user” therefore did not simply discover a natural population. It helped construct one.

This matters for current prompt practice because many generative systems now contain badges, leaderboards, rating tasks, invitation systems, usage tiers, private groups, beta programs, and preferential access to new features. These are not peripheral community mechanics. They allocate opportunities to learn the machine before others do. When semantics move quickly, early access is epistemic power.

## 8. Moderation governs who may know the boundary

The moderation section of *Sculptors of Noise* looks, on its surface, like a separate paper about prohibited content. In the context of vernacular system identification, it becomes central. Hidden safety rules create another black-box boundary. Users learn that a term is blocked, substitute a synonym or translation, misspell it, and observe the new response. Moderators then update lists or intervene. Fractl captures the resulting ambiguity precisely: the goal is to punish people trying to create harmful images, “but I think we also end up punishing people who are just curious and are testing what the limits are” (Sun et al., 2022).

The same experimental form can therefore have radically different institutional meanings:

> input → system response → modified input → system response.

That sequence can be debugging, red teaming, curiosity, circumvention, or abuse. Observable behavior alone may not distinguish them. Intent, authorization, social position, content, history, and subsequent use matter.

This turns moderation into an epistemic institution. It governs not only what may be generated but **who may discover the shape of the constraint**. The paper reports that moderators and guides themselves helped test new features and banned words, while ordinary users probing the same region could trigger escalating enforcement. It also reports that trial users and subscribed or established users could be evaluated with different contextual information. The platform therefore distributed permission to experiment unevenly.

The tension between transparency and circumvention follows directly. Publishing the precise boundary can help legitimate users predict what will be blocked and avoid accidental violations. It can also make systematic evasion easier. Keeping the rule hidden can slow circumvention while forcing legitimate users to infer the rule through failed attempts. In a system where practical knowledge is acquired experimentally, opacity does not eliminate probing. It changes who bears its cost.

This insight generalizes beyond safety. Any hidden rate limit, ranking threshold, model-router rule, or policy classifier creates an incentive for black-box inference. The governance question is not simply whether the boundary should be transparent. It is how to create **authorized curiosity**: ways for researchers, creators, and ordinary users to learn the limits of a system without reproducing the harms those limits are intended to prevent.

The 2022 fieldwork cannot answer that question. It makes the conflict visible.

## 9. The community may be inside the model-development loop

A final boundary in the original paper is the boundary between “the model” and “the community.” The project was framed as an evaluation of an online community organized around an AI image generator. But its observations already show the community participating in the system’s development environment. Moderators and guides provided examples they considered noticeably explicit for internal testing. Office hours, micro-polls, feedback channels, user reports, ratings, and massive volumes of generation exposed failure modes at a scale unavailable in a laboratory.

The paper was appropriately cautious about causal claims. It explicitly notes places where the researchers had not seen evidence that polls influenced product decisions. The same caution is necessary today. Current documentation cannot be used to reconstruct 2022 internal pipelines. Yet current Midjourney dataset documentation does establish a more general contemporary relation: Midjourney says its training data include data provided by users through the service and human-provided annotations, ratings, and preferences, alongside public, third-party, and internally generated data (Midjourney, 2026). The documentation also states that data collection for model development began in 2022.

The important point is not to infer that every 2022 prompt directly trained the next model. That would exceed the evidence. The important point is that the analytic boundary between user community and technical model can be porous. A generative system can be organized as a recurrent circuit:

> model_t → user interactions → selected reports/ratings/data → development pipeline → model_t+1.

Once that possibility exists, community behavior is not merely reaction to the model. It can become part of the environment that produces successor models. Users may simultaneously be consumers of model behavior and contributors to the evidence through which future behavior is shaped.

This creates a reflexive form of system identification. Users identify the model through outputs, while the organization may identify users’ preferences, failures, or undesirable behaviors through the same interaction stream. Each side is learning the other. The community’s experimental practices can become product signals; product changes then invalidate or reshape community knowledge.

This is the deepest reason prompt expertise has a half-life. The practitioner is not learning a static black box. The black box may be learning from a population of practitioners, or at least changing through organizational processes partly informed by population behavior. The object and the observing community can co-evolve.

## 10. From prompt engineering to experimental provenance

If prompt craft is a vernacular form of system identification, what should a mature practice preserve?

The default answer has been prompts: save the wording that worked. The evidence in *Sculptors of Noise* suggests that this is insufficient. A successful prompt without its model version, parameters, prior context, observed alternatives, rejected hypotheses, and failure history is an orphaned result. Its apparent reproducibility may vanish when moved to a different execution environment.

A stronger unit is an **experimental provenance record**. For each consequential generation, preserve at least:

- the exact input and execution environment;
- the model/version and explicit parameters;
- relevant prior context or memory state;
- the output set, not only the selected winner;
- the criterion by which one output was preferred;
- the change made next and why;
- hypotheses about the mechanism, marked as hypotheses;
- controls or comparisons that tested those hypotheses;
- failures minimized into small reproducible cases when possible;
- invariants that should survive controlled transformations.

Older technical traditions suggest concrete operations for making such records useful. Delta debugging can shrink a failure-inducing prompt rather than responding to every failure with more prose (Zeller & Hildebrandt, 2002). Metamorphic testing can specify relations among outputs when no single correct output exists—for example, that changing camera position should preserve character identity (Chen et al., 1998). Property-based testing can turn an invariant into a generator of new adversarial cases (Claessen & Hughes, 2000). Query by Committee can select a diagnostic prompt that maximizes disagreement among competing explanations rather than maximizing immediate artifact quality (Seung et al., 1992). Schön’s reflective design work is a reminder that the artifact may change the designer’s understanding of the problem rather than merely reveal an implementation error (Schön, 1992). Naur warns that the final textual artifact may preserve much less knowledge than the practitioner’s theory of why it works (Naur, 1985).

None of these lineages makes generative prompting historically unprecedented. That is precisely why they are useful. They strip away weak novelty claims and isolate the distinctive conjunction: natural language can trigger execution while leaving consequential variables unmarked; the result can reveal those omissions immediately; the evaluator can change after seeing the result; the model’s semantics may change across versions; social infrastructure changes which experiments are visible; and platform governance changes which experiments are permissible.

A prompt-practice tool built around this account would not begin with a giant text box labeled “prompt.” It would begin with a history of claims and probes. It would support paired comparisons, controlled deletions, version replay, context isolation, counterexample preservation, and public or private branching. It would distinguish a user value (“keep the same character”) from a model workaround (“repeat the name three times because Vx drops identity”). On model migration it would retest the workaround and invite its deletion if the failure disappeared. It would treat history as evidence but not automatically feed all history back into the model, because retention and retrieval are different operations.

The purpose is not to make artists behave like QA engineers. It is to give empirical craft a memory stronger than folklore.

## 11. What changed between 2022 and now

The value of returning to a 2022 field site is not nostalgia. It is that several variables that were then experiential, hidden, or metaphorical have since become explicit product concepts.

First, model-added style is now user-addressable. Midjourney’s Raw and Stylize documentation openly distinguishes more literal control from stronger automatic artistic treatment (Midjourney, n.d.-a, n.d.-c). The old observation that an underspecified prompt fell into a recognizable Midjourney “vibe” has become partly parameterized.

Second, version dependence is explicit. Current Midjourney documentation warns that versions handle prompts differently (Midjourney, n.d.-b). The 2022 problem of a Version-3 prompt book aging under weekly updates is now a documented semantics problem.

Third, publicness has become a controllable economic feature rather than merely an ambient Discord condition. Midjourney continues to describe an open-by-default environment while reserving Stealth controls for higher subscription tiers (Midjourney, n.d.-d). The conflict between public apprenticeship and private process ownership has become product architecture.

Fourth, iterative search is increasingly built into the interface. Current Midjourney Draft and Conversational modes are explicitly designed for faster prototyping and can assist users in writing prompts (Midjourney, n.d.-e). The “trial and error” once carried largely by community practice is becoming a supported product loop.

Fifth, cross-interaction state is no longer universally dismissible as superstition. In systems such as ChatGPT, saved memories and referenced chat history can influence later interactions when enabled (OpenAI, n.d.). Prompt independence is now something that must be established, not assumed.

Sixth, user behavior can be formally entangled with model development. Midjourney’s 2026 dataset documentation describes user-provided data, annotations, ratings, and preferences among training-data categories (Midjourney, 2026). Again, this does not prove a specific 2022 pipeline. It demonstrates that the community/model boundary that appeared porous in the early ethnography has become explicitly porous in present documentation.

The striking continuity is therefore not any particular “magic word.” It is the practice of learning by intervention. The striking change is that the environment in which those interventions occur now contains more explicit state, more explicit controls, and more explicit organizational use of interaction data. Prompt craft did not simply become more scientific. The system being investigated acquired more layers.

## 12. Discussion: expertise as a temporary relation

The common description of prompt expertise locates skill inside an individual: the expert knows how to phrase requests. *Sculptors of Noise* offers evidence for a different ontology. Expertise was distributed across at least six relations.

### 12.1 Expert ↔ default

The expert knows what the model tends to supply when the prompt is silent, and when to accept or counter-specify it.

### 12.2 Expert ↔ version

The expert knows which behaviors belong to the present execution environment and which are likely to decay under updates.

### 12.3 Expert ↔ experiment

The expert does not merely accumulate successful phrases; they manipulate variables, compare outputs, revisit failures, and sometimes deliberately introduce randomness.

### 12.4 Expert ↔ community

The expert sees other experiments, inherits vocabulary, gains access to advanced subgroups, teaches, hoards, remixes, or strategically withdraws.

### 12.5 Expert ↔ governance

The expert learns where experimentation is allowed, where probing is punished, and which knowledge can be publicly circulated.

### 12.6 Expert ↔ provenance

The expert can distinguish what is known from what is guessed, what worked on which version, and which observation produced a rule.

These relations make expertise **temporary** rather than merely tacit. Tacit knowledge is often difficult to articulate but can remain stable in a stable craft environment. Prompt knowledge can be articulable and still expire because the system changes. It can also be socially unavailable because the relevant experiment happened in a private server, a gated club, or an inaccessible version.

This suggests that the unit of analysis should be neither the isolated prompt nor the isolated user. It should be the **prompt practice environment**: a moving arrangement of model, parameters, prior state, user theory, visible peer experiments, access controls, moderation, and version history.

Calling this “vernacular system identification” is useful only if its limits remain explicit. The practitioners are generally not estimating a mathematical plant model. Their output space is high-dimensional and often judged aesthetically. Their objectives can change after seeing results. The system may not be stationary. The interface may deliberately conceal internal variables. Social signals can alter what experiments are attempted. In other words, almost every assumption that makes formal identification tractable is weakened.

That is exactly what makes the comparison productive. It tells us why prompt folklore is inevitable and why better prompt “tips” are not enough. The problem is not simply that users lack documentation. They are trying to infer causal structure from a system whose response surface is stochastic, underdetermined, versioned, stateful, socially mediated, and institutionally bounded.

## 13. Limitations and unresolved questions

This paper deliberately makes a secondary analysis of an early qualitative study do new theoretical work. That creates several limits.

First, *Sculptors of Noise* was a course research project focused on community design, not a longitudinal study of prompt expertise. Its twelve interviews were purposive and weighted toward highly involved users; the super-user stories are therefore evidence of practices, not prevalence estimates for the full population. The field site also moved quickly enough that descriptions could become obsolete during the research itself.

Second, the original project had limited access to Midjourney’s internal technical mechanisms. Its descriptions of “latent space,” banned-word scoring, model training, and other internals often came through participants or limited observation. Those passages are valuable evidence of community understanding but should not automatically be treated as authoritative architecture. This is particularly important where later source checking creates uncertainty about technical genealogy. The present argument relies on the observable practices more than on uncertain claims about proprietary implementation.

Third, contemporary Midjourney documentation is used only to mark present-day contrasts and continuities. It does not retroactively establish what Midjourney did internally in 2022. When current documentation says that model versions handle prompts differently, Standard mode adds creative treatment, or training data may include user-provided data and preference signals, those statements describe current documented practices and categories.

Fourth, the system-identification analogy may over-formalize creative practice if treated literally. Aesthetic judgment is not reducible to prediction error, and practitioners may value surprise precisely because it violates a prior target. The analogy is strongest at the level of experimental relation: controlled interventions, observed outputs, provisional hypotheses, validation, and drift.

The unresolved questions are more valuable than a false closure:

- How can prompt practitioners distinguish a stable causal effect from a stochastic coincidence with minimal generation budgets?
- Which model defaults are strongest when users omit specifications, and how do those defaults vary across demographic, stylistic, and domain contexts?
- What is the decay curve of prompt knowledge across model updates?
- When does a false folk theory remain a productive control heuristic, and when does it become costly superstition?
- How much learning comes from access to others’ failed intermediate generations rather than polished outputs?
- Do usage thresholds merely sort experts, or do gated communities produce expertise after entry?
- How should systems create legitimate pathways for boundary testing without teaching circumvention?
- Which user interactions actually enter evaluation, training, personalization, or product-development pipelines?
- How should a reproducible prompt experiment record memory, retrieval, personalization, and other hidden state?
- Can platforms expose enough causal provenance to support empirical learning without pretending that every generative outcome has a simple explanation?

These questions are not peripheral to prompting. They define what it would mean for prompt practice to become cumulative knowledge rather than a sequence of rapidly aging tricks.

## 14. Conclusion: learn the relation, not the phrase

The most revealing sentence in *Sculptors of Noise* may be the simplest: “trial and error is the teacher.” Taken literally, it sounds like folk wisdom. Taken as an empirical description, it names a new research object.

The early Midjourney experts were not merely learning a vocabulary that translated cleanly into images. They were learning how to act on a system they could not fully inspect. Their language mixed metaphors and experiments because the interface gave them outputs without a complete causal account. Their expertise depended on what the model supplied when they were silent, which version they were using, which failures they had seen, which communities they could enter, which experiments others exposed publicly, and which boundaries moderators permitted them to probe. Their knowledge was useful precisely because it was situated—and fragile for the same reason.

The strongest lesson for contemporary prompt practice is therefore not “write better prompts.” It is: **preserve and improve the experiment by which the prompt became meaningful**.

A prompt is a probe into a response surface. A successful output is evidence, but weak evidence on its own. A repeated failure can be more informative than a polished success. A folk metaphor can be useful without being true. A public rough draft can teach more than a final artifact. A metric can create the expertise it claims to measure. A safety rule can determine who is allowed to know where the boundary lies. A version change can preserve the words while changing the operation. A remembered conversation can make yesterday’s superstition into today’s mechanism.

What deserves to be called prompt expertise, then, is not possession of magic language. It is the capacity to maintain a disciplined relation to a moving machine: to notice defaults, design probes, preserve counterexamples, separate effect from explanation, track execution context, learn socially without confusing popularity with causality, and know when old knowledge has expired.

The prompt is the visible move. The practice is the experiment.

---

## References

Chen, T. Y., Cheung, S. C., & Yiu, S. M. (1998). *Metamorphic testing: A new approach for generating next test cases* (Technical Report HKUST-CS98-01). Hong Kong University of Science and Technology. https://arxiv.org/abs/2002.12543

Claessen, K., & Hughes, J. (2000). QuickCheck: A lightweight tool for random testing of Haskell programs. In *Proceedings of the Fifth ACM SIGPLAN International Conference on Functional Programming* (pp. 268–279). https://doi.org/10.1145/351240.351266

Ljung, L. (1999). *System identification: Theory for the user* (2nd ed.). Prentice Hall PTR.

Midjourney. (n.d.-a). *Raw*. Midjourney Documentation. Retrieved August 17, 2026, from https://docs.midjourney.com/hc/en-us/articles/32634113811853-Raw

Midjourney. (n.d.-b). *Version*. Midjourney Documentation. Retrieved August 17, 2026, from https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version

Midjourney. (n.d.-c). *Stylize*. Midjourney Documentation. Retrieved August 17, 2026, from https://docs.midjourney.com/hc/en-us/articles/32196176868109-Stylize

Midjourney. (n.d.-d). *Keeping your creations private*. Midjourney Documentation. Retrieved August 17, 2026, from https://docs.midjourney.com/hc/en-us/articles/28014645615373-Keeping-Your-Creations-Private

Midjourney. (2026, January 20). *AB2013 Documentation*. Midjourney Documentation. https://docs.midjourney.com/hc/en-us/articles/42829949256205-AB2013-Documentation

Midjourney. (n.d.-e). *Draft & Conversational Modes*. Midjourney Documentation. Retrieved August 17, 2026, from https://docs.midjourney.com/hc/en-us/articles/35577175650957-Draft-Conversational-Modes

Naur, P. (1985). Programming as theory building. *Microprocessing and Microprogramming, 15*(5), 253–261. https://doi.org/10.1016/0165-6074(85)90032-8

OpenAI. (n.d.). *How does “Reference saved memories” work?* OpenAI Help Center. Retrieved August 17, 2026, from https://help.openai.com/en/articles/11146739-how-does-reference-saved-memories-work

Schön, D. A. (1992). Designing as reflective conversation with the materials of a design situation. *Research in Engineering Design, 3*, 131–147. https://doi.org/10.1007/BF01580516

Seung, H. S., Opper, M., & Sompolinsky, H. (1992). Query by committee. In *Proceedings of the Fifth Annual ACM Workshop on Computational Learning Theory* (pp. 287–294). https://doi.org/10.1145/130385.130417

Sun, Z., Hartsoe, W., & Ottolin, T. (2022). *Sculptors of noise: Control in Midjourney AI art community*. Unpublished course research paper, Georgia Institute of Technology, CS 6470: Design of Online Communities.

Zeller, A., & Hildebrandt, R. (2002). Simplifying and isolating failure-inducing input. *IEEE Transactions on Software Engineering, 28*(2), 183–200. https://doi.org/10.1109/32.988498
