---
title: "From Imagetext to Worldtext"
subtitle: "Operative Description and the Persistence of Consequences"
author: "Watson Hartsoe"
date: "Working paper · November 2026"
documentclass: article
fontsize: 11pt
papersize: letter
geometry: "top=0.78in,bottom=0.78in,left=1.22in,right=1.22in"
colorlinks: true
linkcolor: "MidnightBlue"
urlcolor: "MidnightBlue"
linestretch: 1.07
secnumdepth: 0
header-includes:
- |
  \setlength{\emergencystretch}{2em}
  \setlength{\parskip}{0.55em}
---

**Abstract.** A description can make an image, place an object, or alter a rule. These operations make different kinds of claims on what happens next. I call *worldtext* a generative symbolic field in which words, images, objects, and actions can express, query, and revise a shared world. Its distinguishing condition is consequential re-entry. A relation established in one encounter remains available to matter in another, even when the medium or point of view changes. I develop this claim through three instruments from my design practice. In the Builders’ Game, a delivery count certifies a threshold that the test never checks as a doorway. In *House of Dust*, moonlight sets Penelope and her loom to unraveling, although the animation resets its phase. In *Shield Grid*, a substring turns a question about authority into a visual invocation. These cases distinguish execution, situated adequacy, and persistence. I propose *thick prompting* as a method for tracing the context, operators, and judgments that let a description acquire consequences beyond its first output.

**Keywords** · worldtext, operative description, operative ekphrasis, thick prompting, generative media, research through design

# 1. The doorway that was already complete

The Builders’ Game calls one of its challenges THE THRESHOLD. The player is asked for two pillars and a slab. After those pieces are delivered, the inspected completion predicate has all it needs. It counts the deliveries. It does not ask whether the pillars stand apart, whether the slab spans them, or whether anyone can pass between them. The word *threshold* suggests an opening that affords passage. What the program certifies is an inventory. The difference becomes visible because the apparatus has made one reading of the description executable (Hartsoe 2026, dossier 1).

This is a useful failure for an account of generative media. The words have done real work. The pieces are available to be selected and moved. A partial translation has acquired the authority to announce a completed task. If the player can return to that arrangement, point to the pieces, and change what they afford, the initial output becomes part of an ongoing situation. The capacity to produce the pieces and the capacity to continue working in the same situation belong to different parts of the apparatus.

I call that ongoing situation a *worldtext* when it takes the form of a generative symbolic field that can be described, pictured, inferred, continued, and re-entered. The field includes the relations from which its expressions are made and the operations through which those relations may change. A scene description and a view of the scene can be co-expressions of a world when a consequential relation can be recovered across them. Their agreement is an achievement of the apparatus. A system may achieve it through a runtime, a reader, an editor, a performer, or a combination of them.

The paper’s wager is that **a description becomes world-forming when some consequence survives the occasion that produced it and becomes available to a later encounter**. Survival may mean retaining a fact, preserving an explicit choice among alternatives, carrying forward a changed relationship, or keeping a trace of why a revision was made. The requirement is selective. A world can keep a broken promise while leaving the color of the door open. That selectivity makes a world both coherent and unfinished, and gives a participant something specific to contest.

# 2. From verbal–visual relations to consequential re-entry

The point of departure is *Operation / Describe*, my research project with Jay David Bolter on the passage from imagetext to Worldtext (Hartsoe and Bolter n.d.). The account developed here focuses on a consequence of that passage for design.

Mitchell’s *Picture Theory* situates ekphrasis within a larger inquiry into the relations between the visible and the readable. Its concept of imagetext offers a way to consider verbal and visual forms in their conjunction (Mitchell 1994). Bajohr’s *operative ekphrasis* brings a further relation into view. In text-to-image generation, verbal input participates in producing the image. A caption and a resulting image can be related through an operation whose material conditions include encoders, learned representations, and a generation pipeline (Bajohr 2024a). The joint availability of text and image representations can enable that operation while the system still assigns them different roles. In DALL·E 2, a prior predicts an image embedding from text conditioning and a decoder uses the image embedding to produce pixels (Ramesh et al. 2022).

Worldtext shifts the question from how a word produces a view to how a relation established through one expression can bear on another. An image may show a broken bridge. A later route planner, character, or editor can treat the break as a fact that narrows the available actions. Another view may omit the bridge entirely while still belonging to the same world, provided the break can matter when the route comes into question. Image fidelity and world continuity therefore answer different questions. The first asks how an expression presents something. The second asks what can be carried from it and with what authority.

This extension also draws on the tradition of texts that require action from their readers. Aarseth’s cybertext places the operations that produce a textual sequence inside the analysis of the work (Aarseth 1997). Navigating a link, executing a score, and editing a scene can each yield a different realized sequence. Worldtext takes up the narrower question of what can be carried forward as a commitment when a sequence becomes material for further production. An editable branch can retain a decision. An image generator may depend on a reference that disappears when the resulting image is exported. Interactivity can coexist with fragile continuity, while a comparatively spare interface can expose a durable account of what was changed.

Bajohr’s *(Berlin, Miami)* makes that division hard to miss. In his Venice talk he suggests that recurring people, places, and things can give a reader a world whose causal connections are fragile. His earlier account calls attention to surface narration, where the form of storytelling invites readers to infer connections across discontinuities (Bajohr 2024b, 2025). In his production note he describes reading that the Jawling had been pregnant, then typing “Jawling pregnancies” to elicit an account of its reproductive cycle (Bajohr 2024c). The two words were sufficient for the author because he had already identified a character and a prior event. His reading then became part of the conditions for the next generation. Here a world relation travels through a person and back into the system. The published novel alone cannot reveal how often its apparent continuity depended on that intervention.

Two computational uses of *world model* help locate the claim. Ha and Schmidhuber model future observations conditional on an agent’s actions and test transfer from a learned simulator to the original environment (2018). Wong and colleagues, including Tenenbaum, use a language model to translate utterances into expressions in a probabilistic programming language. The resulting program supports inference and can be extended with new concepts or rules (2023). These are distinct ways of assigning consequences to an action or utterance. They help specify what evidence a project should produce when it says a world remembers, supports intervention, or can be taught a rule. Worldtext also encompasses the relations that remain with readers, performers, and editors. A fictional world can be operative in practice even where its commitments have no unified internal representation.

# 3. Locating the operator

The effective unit of operative description is the *context stack*. It comprises the words, the selected referents, the state available at the time, the interpretive rules or model, and the validation or editorial decisions that determine what takes effect. Two people can utter the same sentence while addressing different entities. The same person can address the same entity through two interfaces and trigger different operations. In the inspected Builders’ Game, typed “move pillar” reaches the noun-matching delivery loop before the typed move handler, while “put that there” can reach a move operation when the interface has bound the two referents. The voice route can use an external model’s tool selection. The project thus contains multiple instruction grammars behind one activity (Hartsoe 2026, dossier 1).

Sol LeWitt’s *Wall Drawing 51* gives a precise example of a sparse description with a thick situation. Its instruction connects the architectural points of a site by straight lines. A door frame, a column, or a fire alarm becomes available as a point because it belongs to the installation’s architecture and because a draftsperson can identify and mark it. The two simultaneous 1970 Turin installations yielded distinct realizations. The variation belongs to the work’s rule, which calls on what the site supplies (MASS MoCA n.d.). Michael Newman’s reading of Mallarmé’s *Le Livre* puts a complementary emphasis on discretion. In the account accompanying his 2026 Venice talk, an operator uses chance to place pages in a cabinet under a numerical constraint. The performer selects an arrangement within a space of possibilities that someone has already designed (Newman 2026).

These examples distinguish three functions often compressed into the word *operator*. Someone or something fixes the space of permissible outcomes. Someone or something chooses a particular realization. Someone or something decides whether to accept its consequences. In a generative workflow those functions can be distributed across an author, a model, a renderer, a runtime, a platform, and an editor. In LeWitt the physical site also supplies facts absent from the score. The practical question is which parts of the context the participant can see and change. The historical question, posed more broadly by AIMODELS, is how an earlier organization of labor and measurement comes to be represented as a machine operation (ERC AIMODELS n.d.).

# 4. When moonlight tells Penelope what to do

Alison Knowles and James Tenney’s 1967 *House of Dust* draws quatrains from four lists, with slots for material, place, light, and inhabitants. A selected quatrain became the score for a public sculpture. The poem’s circulation between computation and built space depended on further choices and work (BAMPFA 2022). The Odyssey-based *House of Dust* in my practice puts that passage between forms under inspection. Its initial score reads:

> A HOUSE OF WOVEN THREAD  
> AT THE SWINEHERD’S HUT  
> USING DAYLIGHT  
> INHABITED BY PENELOPE AND A RETURNING STRANGER

In the implementation, “a returning stranger” resolves to the authored Odysseus asset. This association has a precise provenance. The lookup carries a reading of the story into the software. It also narrows the possibilities: a stranger in this score has an assigned identity that the reader of the quatrain could otherwise leave open. An enumerated check recorded in the experiment dossier found 500 possible scores, each of which produced a recipe with three objects and two inhabitants and survived a round trip through the score encoding. That establishes the bounded score module’s behavior. Loading the required drawings is a separate operation. The drawing program checks them before committing a new poem and world together (Hartsoe 2026, dossiers 2–3).

Moonlight is where description begins to act as a rule. In the inspected source, with the relevant score conditions in place, substituting moonlight for daylight switches the loom to an unraveling track and selects Penelope’s unweaving pose. The illumination line thus changes what a person does and what happens to an object. Yet the woven fraction follows a repeating 16-second phase. A later loop can show the same action without carrying a material history of how much cloth remains. A scene can perform a consequence convincingly while the next encounter inherits only the conditions for performing it again.

This difference suggests a demanding test for Worldtext. Ask the same question twice, once after the action and once after returning from a change of view, time, or medium. If the work invites the participant to believe Penelope has undone a night’s labor, there must be some carrier of that fact when the amount of cloth becomes relevant. An authored loop can satisfy a different artistic purpose. A production that chooses to preserve uncertainty might retain two possible amounts or leave the cloth unmeasured. The test is whether the work makes clear what kind of continuity the participant is entitled to use.

# 5. When a reading becomes a rule

*Shield Grid* translates segmented language into visual structure. In a bounded execution of its extracted classifier, “Can we decide?” was assigned QUESTION, while “Who can decide?” was assigned INVOCATION. Both were assigned REPAIR on the world-operation axis. The question mark initially assigns QUESTION. A later invocation condition matches the characters “o ” inside “Who ” and overwrites that assignment. Downstream, QUESTION maps to FRACTURE and INVOCATION to RADIATE (Hartsoe 2026, dossier 5). One substring changes the visual treatment even though both sentences are questions.

The difference matters because “Who can decide?” asks about authority. The system gives the phrase a different visual force, but the difference was produced by a lexical match and the ordering of branches. The same result could be defended as a deliberate reading of the phrase in a different work. Here the trace identifies what happened in this one. It also identifies a point for revision. The designer can revise the matching rule, change how conflicting assignments are handled, or use a cell override to make a particular reading explicit. Those are different interventions with different scopes.

The case identifies three judgments that a fluent output can compress. **Execution** asks which operation occurred. **Adequacy** asks whether the operation fulfills the situated task or supports the interpretation claimed for it. **Persistence** asks which of its effects continue to constrain later encounters. The threshold tally executes and can be retained, while its adequacy as a doorway test remains open. Penelope’s unweaving is legible within a scene, while the amount undone need not persist. A glyph assignment may propagate reliably even when the interpretation behind it is fragile. An account of Worldtext has to leave room for disagreement at each of these points.

# 6. Thick prompting as a method

Geertz’s use of thick description, following Ryle’s wink example, distinguishes bodily movement from the socially situated action it may perform (Geertz 1973). A longer account of the eyelid would leave the relevant difference unexplained. Thick prompting borrows that attention to consequential distinctions. It studies the relation between an utterance and what a practice makes possible with it. A two-word phrase can be thick when it invokes a character with a recoverable history. A page of elaborate description can be thin as evidence if the conditions that made its output possible are unavailable.

The unit of evidence is a documented prompt–output sequence. Preserve the wording, the addressed entities, the initial state, the route through the system, any supplied references or rules, the resulting artifact, and the decision that accepted or rejected it. Then vary one consequential condition. Keep the parts constant and change their placement. Keep the score constant and replace daylight with moonlight. Keep the punctuation and change the phrasing. Follow the result through a second encounter and record which effect survives, who can revise it, and how that revision is attributed. When a model is stochastic, record the model and sampling conditions when available and retain a bounded set of alternatives. A comparison supports claims about the observed conditions and trajectories.

The Association Field in Cineosis offers a different kind of sequence. An editor walks a path of clips and uses LAY to seat them into a spoken line. The inspected implementation uses line boundaries supplied by its kernel and can carry remaining steps forward when the current line cannot accommodate the full path (Hartsoe 2026, dossier 4). The same words and source clips can therefore support different cuts. What a later editor needs to recover is the chosen path, the resulting intervals, and the distinction between a candidate clip and a committed edit. A rendered montage can carry the composition to an audience while leaving these decisions inaccessible to the next maker. The ability to re-enter a world is consequently also a question of continuing authorship.

One useful stopping rule is to end a comparison once there is enough evidence to distinguish the proposed explanations. In Shield Grid, the extracted rule and its contrasting inputs identify a mechanism. More attractive renderings would add little to that finding. A claim about what viewers understand would require a different comparison. In a creative workflow, the aim may instead be to preserve several materially different readings so that the next maker can choose between them. This is why a record of a rejected interpretation can matter as much as a prompt that worked. It gives the world a history that someone can reopen.

# 7. Limits and implications

The cases support distinctions among specific operations. They are based on source inspection and bounded executions recorded in the project dossiers. The doorway comparison remains a proposed run, the loom evidence concerns a repeating phase, and the Shield Grid check exercised an extracted function. These materials do not establish how participants understand the interfaces or how a particular generative model preserves state over long runs. A production account, such as Villeneuve’s description of puppeteers creating shadows for the performers in *Arrival*, offers an adjacent case of a deliberately arranged cue. It shows how a world can be made available to someone through timing and presence before it is available to an audience as a finished image. The contribution of that cue to the finished performance remains a separate inference (Villeneuve and Beguš 2026, 15:25–17:30).

A strong objection is that insisting on persistence would exclude literary and artistic worlds whose discontinuities are essential to them. The objection helps specify what is meant by a consequence. A contradiction can persist as a contradiction. Two versions of an event can remain separately available and shape different encounters. A participant may be entitled to inspect which version a scene uses without having the power to resolve the dispute. Worldtext can be incomplete and disputable because what it must preserve is the availability of a relation for further interpretation or action. An interface that silently overwrites the losing version makes a different artistic and epistemic choice from one that allows both to be revisited.

The term also does not require treating a model’s latent space as a complete fictional universe. A latent representation can contribute productive possibilities. A canon can establish selected commitments. An artifact can express some of them, and a history can record how they changed. Those are different functions, even when one system performs several of them. Asking where each function lives makes it possible to compare worlds assembled through human practice, authored rules, learned models, and combinations of the three.

# Conclusion

An operative description can give a world something to keep. The Builders’ Game shows how narrowly a machine may certify what has happened. *House of Dust* shows how much a line of poetry can set in motion and how little of that motion a loop must remember. *Shield Grid* shows how a small reading decision can acquire visible force and why its provenance matters. In a worldtext, the next description arrives in a situation changed by the last one. Its new referents, possible actions, and rights of revision are the substance of the world.

\clearpage

# References

\small

Aarseth, Espen J. 1997. [*Cybertext: Perspectives on Ergodic Literature*](https://www.press.jhu.edu/books/title/1398/cybertext). Johns Hopkins University Press.

Bajohr, Hannes. 2024a. “Operative Ekphrasis: The Collapse of the Text/Image Distinction in Multimodal AI.” *Word & Image* 40 (2), 77–90. [doi:10.1080/02666286.2024.2330335](https://doi.org/10.1080/02666286.2024.2330335).

Bajohr, Hannes. 2024b. “[Cohesion Without Coherence: Artificial Intelligence and Narrative Form](https://transit.berkeley.edu/2024/cohesion-without-coherence-artificial-intelligence-and-narrative-form/).” Translated by Kayla Rose van Kooten. *TRANSIT* 14 (2).

Bajohr, Hannes. 2024c. “(Berlin, Miami).” Excerpts and production note. [*Ensemble Park* 1](https://www.ensemblepark.com/issues/ensemble_park_1.pdf).

Bajohr, Hannes. 2025. “[The Latent Space of Meaning and the Novel: World Models in AI and Literature](https://www.youtube.com/watch?v=hmchpa_Ek20).” Chat Token Vector, Ca’ Foscari University of Venice, June 12.

BAMPFA. 2022. [*By Alison Knowles: A Retrospective (1960–2022)*](https://bampfa.org/sites/default/files/AlisonKnowles_LargePrint_DIGITAL_v3.pdf). Exhibition text.

ERC AIMODELS. n.d. “[The Culture of Algorithmic Models: Advancing the Historical Epistemology of Artificial Intelligence](https://pric.unive.it/projects/ai-models/home).” Ca’ Foscari University of Venice. Project description.

Geertz, Clifford. 1973. “Thick Description: Toward an Interpretive Theory of Culture.” In *The Interpretation of Cultures*. Basic Books.

Ha, David, and Jürgen Schmidhuber. 2018. “[World Models](https://worldmodels.github.io/).” arXiv:1803.10122.

Hartsoe, Watson. 2026. “[Grounded Experiment Dossiers: From Wording to Consequence](https://chatgpt.com/library?file_id=libfile_6a9f9eac7dfc8191b18354ff8742c3f5&account_id=personal).” Research notes, October 15. Primary artifacts: [Builders’ Game](https://hartswf0.github.io/tractor-dce-gyo/builders-game.html), [House of Dust](https://hartswf0.github.io/odyssey-halfworld/house-of-dust.html), and [Shield Grid](https://hartswf0.github.io/text-ure/shield%2052/1.html).

Hartsoe, Watson, and Jay David Bolter. n.d. [*Operation / Describe: From Imagetext to Worldtext*](https://hartswf0.github.io/operation-describe/). Research project.

MASS MoCA. n.d. “[Wall Drawing 51](https://massmoca.org/event/walldrawing51/).” Exhibition entry for Sol LeWitt’s June 1970 work.

Mitchell, W. J. T. 1994. [*Picture Theory: Essays on Verbal and Visual Representation*](https://press.uchicago.edu/ucp/books/book/chicago/P/bo3683962.html). University of Chicago Press.

Newman, Michael. 2026. “[Art as ‘Operation’: From Lovelace and Mallarmé to Adversarial Poetry](https://www.youtube.com/watch?v=ce3rNpXdu30).” Recording description. Adversarial Poetry symposium, Ca’ Foscari University of Venice, October 1.

Ramesh, Aditya, Prafulla Dhariwal, Alex Nichol, Casey Chu, and Mark Chen. 2022. “[Hierarchical Text-Conditional Image Generation with CLIP Latents](https://arxiv.org/abs/2204.06125).” arXiv:2204.06125.

Villeneuve, Denis, and Nina Beguš. 2026. “[Arrival: A Conversation with Denis Villeneuve and Dr. Nina Beguš](https://www.youtube.com/watch?v=7QoS5uK52DY).” Academy Museum of Motion Pictures, November 2.

Wong, Lionel, Gabriel Grand, Alexander K. Lew, Noah D. Goodman, Vikash K. Mansinghka, Jacob Andreas, and Joshua B. Tenenbaum. 2023. “[From Word Models to World Models: Translating from Natural Language to the Probabilistic Language of Thought](https://arxiv.org/abs/2306.12672).” arXiv:2306.12672.
