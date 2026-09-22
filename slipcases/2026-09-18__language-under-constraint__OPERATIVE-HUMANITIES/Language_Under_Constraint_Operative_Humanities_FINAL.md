# Language Under Constraint
## Semantic Instruments for Operative Humanities

**Working Paper · September 2026**

### Abstract

Generative systems have made description executable, but execution alone does not make language a serious medium of inquiry. Once an artifact, model, or scholarly object exists, an instruction must negotiate a bounded difference inside a field of expected continuity: what may change, what must persist, and what remains uncertain. This essay calls that structure a linguistic transaction and argues that it provides a stronger basis for post-chat interfaces than the familiar ambition to expose or navigate latent space. The human should act in the ontology of the inquiry; the machine should translate those acts into model-space operations. From that premise follows a second claim: a medium for thinking cannot privilege one world view. The same object may need to become image, trajectory, causal graph, testimony, table, counterfactual, or sentence without losing the provenance that lets those representations answer to one another. Reading Bret Victor alongside Johanna Drucker, Lisa Samuels and Jerome McGann, David Kirsh and Paul Maglio, Lucy Suchman, Philip Agre, and technical work such as Prompt-to-Prompt and DragGAN, the essay proposes operative humanities as a practice in which description, deixis, deformation, and representation become reversible scholarly operations. The goal is not more interaction. It is a computational field in which transformations can be made without destroying what gives their differences meaning.

**Keywords:** operative humanities; semantic instruments; prompting; deixis; deformance; epistemic action; representation; persistence

## 1. The hidden preservation set

“Make the roof red.”

Three words.

But almost everything I mean is missing.

Keep the same roof. Keep its shape. Keep the house. Keep the camera. Keep the history. Change one thing. Preserve the rest.

That is where generative AI gets interesting.

We have learned how to make language produce things: images, video, code, worlds. The harder problem begins once something exists. How can language change one part of a computational object without destroying everything that gives that change meaning?

This small failure exposes a larger problem in the prevailing account of prompting. We have become fascinated by the fact that words can make things happen. A sentence can produce an image, program, mesh, voice, video, or scene. Description has acquired computational force. But generation is the easy case. The harder problem begins once there is something worth preserving. At that point language has to distinguish change from continuity: which entity is being addressed, which relation may vary, which properties are invariant, what side effects are acceptable, and what history must survive the operation.

The editing literature already encounters this problem in technical form. Prompt-to-Prompt begins from the observation that text-guided image models are naturally good at synthesis but awkward at editing because even a small change to the text prompt can produce an entirely different image. Editing, by contrast, presumes that some content from the original will remain stable. Hertz and colleagues therefore manipulate cross-attention during diffusion so that selected semantic changes can occur while aspects of the original composition are preserved (Hertz et al. 2023). The specific mechanism belongs to diffusion models, but the conceptual problem is broader: an edit is never defined only by what changes.

This suggests a different grammar for operative language. An utterance can carry at least three kinds of information: **CHANGE**, the requested difference; **HOLD**, the field that should persist; and **UNCERTAIN**, the region in which the system cannot guarantee preservation. “Make the roof red” changes material color while presumptively holding identity and geometry. “Make this paragraph angrier without changing its claim” changes rhetorical force while preserving argumentative content. “Treat these testimonies as accounts of the same event without resolving their disagreement” changes the relation among sources while explicitly forbidding semantic collapse. The important unit is no longer a prompt understood as a miniature commission. It is a transaction inside a persistent field.

## 2. From latent space to semantic instruments

The language of generative AI often describes the interface problem as access to latent space: users should steer, traverse, or expose the model’s hidden dimensions. This metaphor is seductive because latent representations genuinely contain degrees of variation unavailable in traditional software. But it starts from the ontology of the implementation. The fact that a model represents possibilities in a high-dimensional numerical space does not imply that a person should reason there. In many cases the better interface does the opposite: it lets the user act in a domain they understand while the machine performs the translation into its own representational machinery.

DragGAN provides a concrete example. The user selects a handle point on an image, identifies a target point, and drags one toward the other. The system performs feature-based motion supervision and point tracking to update the generative representation while maintaining a plausible image on the learned manifold (Pan et al. 2023). The user does not inspect or manipulate the GAN’s latent vector directly. The human contribution is deictic and perceptual: this point, there. The machine bears the burden of turning that meaningful constraint into model-space change.

Richard Bolt’s “Put-that-there” system made a related move more than four decades earlier. Voice and gesture were combined so that pronouns such as “that” and “there” could be resolved by pointing, producing what Bolt described as greater naturalness and economy of expression (Bolt 1980). The power of the phrase does not come from language alone. It comes from language operating inside a shared referential field. Philip Agre later made indexicality central to his account of deictic representation: the significance of a representation cannot always be separated from an agent’s current location, activity, attitudes, and goals (Agre 1997, 241–259). A coordinate can tell a system where something is; situated activity helps determine what that something means now.

These examples point toward the idea of a **semantic instrument**. A semantic instrument is not a natural-language interface pasted over an existing application. It is a stable coupling between a meaningful human action and a computational transformation. The action may be linguistic, spatial, gestural, graphical, or mixed. “Move this there” combines language and deixis. “Keep the dog’s face visible while I walk around the room” states a relational constraint whose low-level realization can be delegated to the system. “Show me where these accounts stop agreeing” names an analytical relation rather than a visualization type. The instrument earns its value when the user can learn what kinds of differences it makes without having to adopt the machine’s internal ontology.

This also clarifies why semantic instruments are not simply more controls. A control is useful only if its meaning is stable enough to become part of practice. The ambition is not to expose every parameter a model happens to possess. It is to construct handles at the level of the inquiry and compile them downward. The human operates on roofs, claims, voices, causal relations, camera attention, evidentiary disagreement, or temporal duration. The machine translates those operations into attention maps, geometric transforms, optimization steps, graph mutations, or whatever implementation is required. Latent space becomes a compiler target rather than a destination for the user.

## 3. One world view is not enough

Once a system can maintain persistent objects and relations, it is tempting to imagine that the successor to chat is a world: a continuous spatial environment containing entities, geometry, agents, history, and rules. Persistence would indeed solve real problems. Language could refer back to things that continue to exist. Changes could accumulate instead of producing disconnected outputs. Yet a persistent world view can harden into another representational bottleneck if it becomes the privileged form through which every question must pass.

Bret Victor’s *Media for Thinking the Unthinkable* is useful here because its central object is not immersion but representation. Victor argues that media are thinking tools: our representations of systems are how we understand them, and complex systems demand representations more powerful than those inherited from paper (Victor 2013). His demonstrations repeatedly refuse a single privileged view. One environment shows many variables and behaviors together; another links several stages of a transformation pipeline so that an element can be followed across representations; still others invite the construction of new visual forms around whatever relation needs to become perceptible. The medium’s power lies partly in moving among representations without severing their connection to the underlying system.

Consider a river.

Begin with water: a moving spatial representation of channel, floodplain, tributaries, fields, and towns.

Then make it velocity arrows.

Then sediment age.

Then a causal graph.

Then legislation.

Then oral histories.

Then forty years of change.

Then ten possible futures.

Then a table.

Then one sentence.

Then water again.

The important thing is not that the machine can generate all of these representations. The important thing is that the river survives their differences.

No one of these representations is the river. More importantly, none should become authoritative simply because a computer can render it convincingly. A causal graph clarifies dependency while stripping texture. A legal map makes jurisdiction visible while imposing boundaries that hydrology does not respect. Testimony restores situated language while resisting easy comparison at scale. A photorealistic environment restores spatial presence while hiding relationships that a diagram makes obvious. A medium for thinking therefore needs more than a better simulation. It needs the same object to survive translation among representations, with enough provenance that each representation remains answerable to the others.

This reverses a familiar ambition in generative media. The most consequential capability may not be increasingly realistic world synthesis. It may be **representational synthesis**: constructing the view that lets the present question become thinkable. The generative system is then not only a renderer of content but a producer of analytical forms. A scholar can ask not merely “change the river” but “make the river legible as a history of sediment,” “show the conflict between the legal and ecological river,” or “give me a representation in which these testimonies can disagree without disappearing from the same field.”

## 4. Operative humanities: interpretation by transformation

The humanities make this problem harder because their objects rarely arrive as neutral states waiting for the correct visualization. Johanna Drucker’s distinction between data and capta identifies the epistemological danger. Conventional data visualization often treats information as given and observer-independent. Drucker argues that humanistic information is better understood as capta: taken and constructed through interpretive decisions. A humanities approach to graphical display must therefore preserve ambiguity, complexity, observer dependence, and the interpretive conditions through which information becomes representable at all (Drucker 2011).

For an operative humanities, exposing computational state is consequently insufficient. The interface should also expose how something became a state variable. Who decided that these five documents describe one event? Why is this stretch of the river treated as one region rather than three? Why does a timeline begin at one date and not another? Who named an object ceremonial, domestic, evidence, property, or debris? A coordinate can be exact while the decision to make that coordinate salient remains interpretive. Formal precision does not remove this act; it can merely hide it.

A serious humanistic system should therefore be able to hold more than one account of its own objects. If one historian groups five documents as one episode and another treats them as three partially overlapping events, the second interpretation should not need to erase the first. If an institutional catalogue identifies an artifact one way while a descendant community rejects that category, the system should not automatically resolve the contradiction into a single convenient ontology. A world for humanistic inquiry may need to be polyphonic: a field of claims, measurements, descriptions, memories, sources, and interpretations whose differences remain computationally active.

Lisa Samuels and Jerome McGann’s “Deformance and Interpretation” provides an important precedent because it treats transformation itself as a critical method. Their deformance procedures deliberately alter textual objects—by reordering, isolating, adding, or otherwise working against habitual reading—in order to expose possibilities of meaning that conventional interpretation can leave inaccessible (Samuels and McGann 1999). The critical operation is not an illustration added after the interpretation; it participates in producing the interpretation.

Generative computation can enlarge this repertoire dramatically. A scholar might remove every first-person pronoun from a speech; freeze everything in a film except camera movement; render a century of legislation as barriers across the river it governs; spatialize every remembered place in an oral-history collection without merging conflicting memories; isolate every claim in an archive that depends on firsthand observation; reverse a chronology; exaggerate an uncertain date into an interval; or hold evidence constant while varying causal interpretation. These procedures need not be faithful representations of the object in any final sense. Their value can lie precisely in making a hidden relation difficult to ignore.

David Kirsh and Paul Maglio offer a cognitive vocabulary for why such procedures can work. In their study of Tetris, some rotations and translations are best understood as epistemic actions: actions performed not simply to advance the game state but to change the external world so that information becomes easier to uncover or mental computation becomes easier to perform (Kirsh and Maglio 1994). The relevance to scholarship is direct. A temporary deformation can be useful because it redistributes cognitive work. The scholar externalizes a difficult comparison, exaggerates a weak relation, removes interference, or materializes an alternative, then inspects the consequences.

This gives operative humanities a more precise meaning than “digital humanities with richer interfaces.” It names a practice in which computational operations become questions, arguments, and probes while provenance remains intact enough for those operations to be inspected and contested. The source must survive its deformation. The procedure must be explicit. The result must remain comparable with the undeformed object. The operation should be reversible when reversal matters. Most importantly, the transformed representation must not silently acquire the status of evidence merely because the machine produced it.

## 5. Description, deixis, and situated action

The same framework changes what prompting means. Description and deixis are complementary operations. Description can establish a category, constraint, atmosphere, hypothetical relation, or transformation whose referent is not yet present. Deixis binds language to particulars inside a shared situation. “A weathered wooden chair” can invoke an object; “move this” refers to one already present. “Make this chair feel less ceremonial without changing its proportions” combines semantic transformation, situated reference, and a preservation constraint.

The familiar chat interface forces language to carry too much of this burden because the transcript is often the primary persistent object. The user repeatedly redescribes state that both parties could have shared through a richer environment. Bolt’s old phrase “put that there” remains instructive precisely because its linguistic poverty indicates contextual richness. The words are incomplete in isolation and efficient in situation (Bolt 1980). The future of language with machines may therefore involve shorter language rather than more elaborate prompting: this, that one, again, less, before, keep this, not that, like this but heavier.

Lucy Suchman’s critique of planning places a further limit on the fantasy of a perfect prompt. On the planning view, plans prescribe action in detail; on the situated-action account, intentions and plans underdetermine what actually happens as actors encounter concrete circumstances (Suchman 2006, 51–68). A prompt treated as a blueprint reproduces the planning model. A stronger system keeps description available as a resource inside unfolding activity. The initial instruction orients action, but the consequences of action create new information that may change how the earlier description should be interpreted.

“Build a quiet house overlooking the river” begins something. Then the house exists. The view changes what the designer wants. Afternoon light reveals a problem. A path becomes possible where the plan expected a wall. A material behaves differently than expected. The next description emerges from the consequences of the previous operation. Language remains coupled to the object without fully determining it. The prompt is no longer a message that precedes the artifact; it becomes one persistent, revisable element in the situation.

This gives “prompt in motion” a stricter meaning. It is not simply the ability to issue prompts more frequently or with lower latency. It is the ability for descriptions to remain addressable while the world changes: to be narrowed, overridden, suspended, inherited, contradicted, or attached to the entities and relations they govern. Seeing directs the next utterance. Manipulation changes what the utterance refers to. History changes what must be preserved. The operative medium is the coupling among these forms rather than language alone.

## 6. Interaction is not the goal

A final complication prevents this argument from turning into a celebration of ever richer interaction. Victor’s earlier essay *Magic Ink* argues that for a large class of information software, explicit interaction is often a burden: a system should use environment and history to construct context-sensitive information graphics, treating interaction as a last resort when those sources are insufficient (Victor 2006). The claim sits productively against the instrumental ambitions of direct manipulation. Some tasks demand a responsive instrument. Others reveal design failure when the system asks the user to perform work it could already infer from context.

The future interface should therefore allocate interaction rather than maximize it. A scholar performing a deliberate deformance needs control over the transformation. A designer shaping a trajectory may need immediate handles. But a researcher should not have to reconstruct the same provenance graph every time a source is selected. A system that already knows the inquiry concerns disagreement might surface conflicting accounts automatically. A camera constraint that has already been established should persist without being restated. More controls do not necessarily produce more agency; they can simply externalize clerical work back onto the person.

This is also why the semantic instrument should not be understood as a universal dashboard. Its job is to preserve meaningful human intervention where intervention changes what can be thought, while using context to suppress unnecessary specification elsewhere. Sometimes the right operation is a sentence. Sometimes a point or drag. Sometimes a graph that appears because the system recognizes what comparison is underway. Sometimes the right action is to leave the scholar alone long enough for a representation to be read.

## 7. The wager

The research problem that follows is not “How do we make generative AI easier to control?” That formulation is too narrow because control presumes both an object and an objective already understood. The more consequential question is: **what transformations should a field of inquiry make possible, and what must survive those transformations for the result to remain knowledge rather than spectacle?**

Answering that question requires concepts that computer science has often treated as peripheral: provenance, interpretive position, uncertainty, contradiction, reversible speculation, source integrity, situated reference, and the distinction between evidence and a transformation performed upon evidence. In an operative humanities these are not merely ethical cautions attached after the system is built. They become architectural principles.

A system can distinguish source from deformation. It can let multiple interpretations remain active rather than collapsing them into one state. It can expose what was held constant during an edit. It can record who or what produced a relation. It can preserve uncertainty as uncertainty. It can allow one object to inhabit many representations without pretending that any representation is neutral. It can separate temporary epistemic operations from durable scholarly claims.

Such a medium would not eliminate friction. Some friction is the perceptible shape of a consequential choice. The aim is instead to stop spending human effort on reconstruction that the computational medium can perform, and redirect that attention toward distinctions requiring judgment. Sometimes that means direct manipulation. Sometimes language. Sometimes the system should infer the next useful representation from context. Sometimes the scholar should reject that inference. Sometimes the right move is to deform the object until a relation becomes visible. And sometimes the right move is to return to water.

After arrows, sediment, legislation, oral histories, trajectories, possible futures, tables, and sentences, the water is not the final or true representation of the river. It is simply another return to the object, now thickened by movement through representations. The scholar sees something different because the medium preserved enough continuity for differences to accumulate rather than erase one another.

That is the wager of operative humanities. The deepest promise of generative computation is not infinite content and not perfect simulation. It is the possibility of semantic instruments through which description, deixis, deformation, memory, and representation become parts of one persistent practice of inquiry. **Language becomes operative not when it can make anything happen, but when it can make a difference without losing everything that gives the difference meaning.**

## References

Agre, Philip E. 1997. “Deictic Representation.” In *Computation and Human Experience*, 241–259. Cambridge: Cambridge University Press. https://doi.org/10.1017/CBO9780511571169.013.

Bolt, Richard A. 1980. “‘Put-that-there’: Voice and Gesture at the Graphics Interface.” *ACM SIGGRAPH Computer Graphics* 14 (3): 262–270. https://doi.org/10.1145/800250.807503.

Drucker, Johanna. 2011. “Humanities Approaches to Graphical Display.” *Digital Humanities Quarterly* 5 (1). https://digitalhumanities.org/dhq/vol/5/1/000091/000091.html.

Hertz, Amir, Ron Mokady, Jay Tenenbaum, Kfir Aberman, Yael Pritch, and Daniel Cohen-Or. 2023. “Prompt-to-Prompt Image Editing with Cross-Attention Control.” *International Conference on Learning Representations (ICLR).* https://openreview.net/forum?id=_CDixzkzeyb.

Kirsh, David, and Paul Maglio. 1994. “On Distinguishing Epistemic from Pragmatic Action.” *Cognitive Science* 18 (4): 513–549. https://doi.org/10.1207/s15516709cog1804_1.

Pan, Xingang, Ayush Tewari, Thomas Leimkühler, Lingjie Liu, Abhimitra Meka, and Christian Theobalt. 2023. “Drag Your GAN: Interactive Point-based Manipulation on the Generative Image Manifold.” *ACM SIGGRAPH 2023 Conference Proceedings.* https://doi.org/10.1145/3588432.3591500.

Samuels, Lisa, and Jerome McGann. 1999. “Deformance and Interpretation.” *New Literary History* 30 (1): 25–56. https://doi.org/10.1353/nlh.1999.0010.

Suchman, Lucy A. 2006. *Human-Machine Reconfigurations: Plans and Situated Actions.* 2nd ed. Cambridge: Cambridge University Press. https://doi.org/10.1017/CBO9780511808418.007.

Victor, Bret. 2006. “Magic Ink: Information Software and the Graphical Interface.” https://worrydream.com/MagicInk/.

Victor, Bret. 2013. “Media for Thinking the Unthinkable: Designing a New Medium for Science and Engineering.” MIT Media Lab. https://worrydream.com/MediaForThinkingTheUnthinkable/.
