---
title: "The Shop Makes the Prompt"
subtitle: "Cultural Competence, Reverse Description, and the Operational Life of AI Art"
author: "Watson Hartsoe"
date: "2026-08-17"
abstract: |
  Text-to-image prompting is often described as a new language for expressing artistic intention. That description puts the competence in the wrong place. Prompting is better understood as a culturally learned diagnostic practice: practitioners inspect generated artifacts, notice differences that have become salient through experience, infer what textual or other intervention might move the system, and test that intervention against a model whose behavior already contains traces of training data, platform design, and prior social description. Clifford Geertz's claim that art and the "equipment to grasp it" are made together becomes unusually literal here. In generative practice, equipment for grasping an image becomes equipment for correcting the next one. The prompt is therefore not a transparent statement of intention and not a stable programming language. It is a provisional move inside a sociotechnical loop in which description changes causal position: words that once followed art as criticism can precede art as conditioning. This paper develops that wager through research on prompt modifiers, prompt skill, trial-and-error interaction, interface design, default images, body prompting, Hito Steyerl's "mean images," and Felipe Rivas San Martín's minority prompt. The consequence is methodological: the most revealing archive of AI art is not a gallery of outputs or a collection of final prompts, but a history of noticed differences, failed generations, corrective moves, hidden priors, and socially transmitted techniques.
keywords: [AI art, prompt engineering, cultural systems, text-to-image, aesthetic competence, human-AI interaction, generative media]
---

\newpage

# Introduction: the wrong object is the prompt

Generative-image culture has made a small text box carry an extraordinary amount of theory. The box is treated as an interface to intention, a new artistic medium, a programming language, an incantation, a compressed brief, and sometimes the location where human authorship survives. Each description catches something real. Yet all of them tend to isolate the string that a user submits. They make *the prompt* look like the stable unit of creative action.

The evidence in this field points elsewhere. Research on text-to-image practice finds that effective prompting is learned through experimentation; prompt modifiers circulate as practical techniques; inexperienced users can recognize prompt quality while still lacking the style-specific vocabulary needed for effective refinement; and open-ended text interaction often produces brute-force trial and error when results are poor [@Oppenlaender2022PromptModifiers; @OppenlaenderLinderSilvennoinen2023PromptingAIArt; @LiuChilton2021PromptEngineering]. Interface design also changes how much users continue to explore: shortcuts for producing variants are associated with reduced exploration of novel concepts and with less detailed prompting [@TorricelliEtAl2023Interface]. These findings make the final string a misleadingly thin artifact. They point to a trajectory in which a person learns what to notice, which difference matters, and what kind of intervention might change it.

This paper makes a stronger claim. **Prompt expertise is not fundamentally mastery of a language. It is the acquisition of culturally and technically situated equipment for noticing correctable differences.** The user does not merely translate an intention into words. The user encounters an output, recognizes a mismatch through learned aesthetic distinctions, forms a causal hypothesis about a partly opaque generator, and tries another move. What appears as linguistic skill is inseparable from perceptual training, platform affordances, model-specific regularities, community lore, and the sedimented social descriptions contained in training data.

Geertz provides the hinge. In *Art as a Cultural System*, he argues that aesthetic capacities do not stand outside the worlds in which artworks are made; art and the capacities required to grasp it are formed together [@Geertz1976ArtCulturalSystem]. The generative case makes that proposition operational. The equipment for grasping an AI image is often immediately reused as equipment for changing the next image. Seeing becomes a control problem. Description migrates from commentary into conditioning.

That migration is not simply a triumph of linguistic agency. It also exposes asymmetry. The generator can fall back toward recurring default images when textual conditioning fails to discriminate strongly [@SimonenEtAl2025DefaultImages]. Training data can render social averages as if they were machine-native aesthetics [@Steyerl2023MeanImages]. Artists can be forced to spend prompt effort counteracting class, race, gender, or archival biases that originated upstream, as Rivas San Martín's "minority prompt" makes explicit [@Rivas2025InexistentArchive]. The competence acquired by practitioners is therefore partly competence in the system's failures.

The argument proceeds in five steps. First, prompting is reconstructed as diagnostic practice rather than string production. Second, Geertz's "equipment to grasp" is extended cautiously into an equipment to correct. Third, prompt language is shown to be a reverse description of an inherited image-text archive rather than a direct description of the pictured world. Fourth, the paper separates user skill from the cultural and infrastructural priors that skill must work against. Finally, it shows why description itself changes causal position in generative systems, producing a feedback loop in which criticism, community discourse, and interface choices can become production infrastructure.

# 1. Prompting as diagnostic practice

Oppenlaender's ethnography of early text-to-image practice identifies six classes of prompt modifier and describes prompt engineering as an iterative, experimental activity [@Oppenlaender2022PromptModifiers]. The importance of that finding is not the taxonomy alone. A modifier is learned in relation to observed output. The practitioner tries a phrase, inspects what happened, repeats or alters the experiment, and circulates what seems to work. Prompt terms therefore acquire an *operational reputation* in addition to ordinary semantic meaning.

This distinction matters because operational reputation can be wrong. Oppenlaender explicitly discusses idiosyncratic practitioner choices and the possibility of folk theories about causation [@Oppenlaender2022PromptModifiers]. Stochastic generation makes a dangerous epistemic environment: a salient successful output can follow a recent prompt change without having been robustly caused by it. A community can stabilize the technique socially even when the causal theory is weak. Thus the same process that produces expertise can also produce superstition. The correct research question is not whether prompt lore exists, but which parts are computationally effective, under what model versions, and which parts mainly organize community identity or expectation.

The experimental literature on prompt skill reinforces the process view. Oppenlaender, Linder, and Silvennoinen found that untrained participants could evaluate prompt quality and produce descriptive prompts, yet lacked the style-specific vocabulary necessary for more effective prompting [@OppenlaenderLinderSilvennoinen2023PromptingAIArt]. This result is often summarized as evidence that prompt engineering is a learnable skill. More interestingly, it leaves open *what is actually learned*. A vocabulary can be memorized. A skilled practice, however, requires knowing when a distinction is relevant and when a term is worth trying.

Liu and Chilton locate the problem at the interface level. They describe open-ended text interaction as double-edged: it offers enormous expressive freedom but can force users into brute-force trial and error when a generation fails [@LiuChilton2021PromptEngineering]. The result complicates claims that natural language removes formalization. The formal work may simply occur later. A vague initial description produces an artifact; the artifact makes a missing constraint visible; the user adds that constraint; the next artifact reveals another. Specification accumulates temporally through failure.

This suggests a different unit of analysis:

\begin{quote}
output $\rightarrow$ noticed difference $\rightarrow$ causal hypothesis $\rightarrow$ intervention $\rightarrow$ new output.
\end{quote}

The prompt string is only one state in this loop. What changes the research problem is the *noticed difference*. Two people can receive the same image and possess different actionable worlds because one sees a lighting mismatch, a compositional cliché, a model-specific hand failure, an unwanted social stereotype, or a telltale default that the other does not recognize. The deepest evidence of expertise may therefore appear one moment before the next prompt is written.

# 2. From equipment to grasp to equipment to correct

Geertz's argument about art resists the idea that aesthetic perception is a universal capacity applied to autonomous objects. The ability to respond to art is itself cultivated in forms of life, and his memorable formulation that art and the equipment to grasp it are made together gives us a better way to define the relevant cultural unit [@Geertz1976ArtCulturalSystem]. The question is not necessarily whether "AI art" is one culture. It is where shared sensitivities are reproduced.

For generative practice, those sensitivities are unusually consequential because they can immediately become operations. A practitioner learns to see a difference, names it, and feeds that name back into generation. The cultural formation of perception becomes part of a control loop. We can therefore split expertise into at least three coupled capacities:

1. **discrimination** - noticing a difference in an output;
2. **diagnosis** - forming a hypothesis about what produced the difference;
3. **intervention** - choosing a prompt, parameter, body movement, or interface action intended to alter the next state.

This is stronger than saying experts know more prompt terms. A novice can copy a phrase without knowing when it applies. Conversely, an expert may recognize a problem without possessing a reliable intervention because the model has changed. The mapping from difference to intervention is versioned and local.

The distinction also explains why prompt secrecy matters. Early prompt communities sometimes withheld prompts for commercial reasons [@Oppenlaender2022PromptModifiers]. If outputs circulate publicly while procedures remain private, the cultural "shop" can split. A public sphere may teach spectators what to admire while a restricted operative sphere controls how those effects are reproduced. Aesthetic competence becomes stratified: perception may be broadly distributed while generative competence remains scarce.

This is one reason to resist the metaphor of a universal prompt language. Languages imply some durable relation between expression and meaning. Prompt practice is closer to a field of situated correspondences among words, models, interfaces, versions, and communities. The same phrase can retain ordinary-language meaning while losing its generative effect after a model update. Conversely, a seemingly strange phrase can remain operationally useful because it indexes learned correlations that have little to do with literal description.

# 3. Reverse description: prompting the archive that described the world

The most consequential complication comes from the training relation between language and images. Oppenlaender notes that effective practitioners may have to imagine how other people on the Web would have described or reacted to an image [@Oppenlaender2022PromptModifiers]. This changes the direction of description. The user is not always naming the desired visual world directly. The user may be estimating the language that historically surrounded visually similar material in the training ecology.

Prompting can therefore contain an inverse problem:

\begin{quote}
desired visual tendency $V$ $\rightarrow$ hypothesize historical wording $L$ $\rightarrow$ submit $L$ $\rightarrow$ model maps toward $V$.
\end{quote}

The competence here is partly archival, though the archive is inaccessible and statistical rather than a conventional catalog. Terms such as artist names, media labels, genre descriptors, camera vocabulary, platform names, and evaluative phrases can work because of how images and texts were co-produced online. The user learns the aftereffects of those associations by experiment.

Steyerl's "mean images" supplies a cultural theory of what sits upstream of this practice. Generative images, she argues, are statistical renderings of socially produced data; the apparent machine image can be a "social filter" rendering correlated averages and latent social patterns [@Steyerl2023MeanImages]. This breaks the usual opposition between machine style and user taste. There is at least a third term: the historical distribution of images, descriptions, values, and classifications already sedimented into the training process.

This matters for Geertz. A naïve application of cultural context to prompting says that adding "Edo-period," "queer archive," or another culturally specific label injects cultural meaning. That is not enough. A cultural name can increase visual recognizability while decreasing contextual thickness. It may index a statistical cluster of recognizable markers rather than situated knowledge. The generated surface can look more specific precisely because it has collapsed local distinctions into a portable stereotype.

The research problem is therefore not "does the prompt contain cultural context?" It is: **which cultural distinctions are available to the model, which are available to the practitioner, and which are available only to participants in the living practice being invoked?** These three sets need not coincide.

# 4. The user corrects what the user did not choose

If prompt skill develops partly as competence in a model's inherited associations, then expertise has a political asymmetry. Some of the work users learn to perform exists because the system's prior is not neutral.

Rivas San Martín's *Inexistent Archive* provides a precise case. The project imagines fictional historical photographs of queer, non-binary, and working-class people in Latin America. Rivas describes the need to counteract class and race biases in model training data and develops the concept of the "minority prompt" from this obstacle [@Rivas2025InexistentArchive]. The prompt becomes more than description. It is a local corrective operation against upstream representational conditions.

That correction should not be confused with structural repair. If a user adds counter-conditioning to obtain one desired result while the model and dataset remain unchanged, the user has altered the local generation, not necessarily the system that made the correction necessary. The labor is downstream; authority over the causal substrate is upstream. Prompt agency and prompt burden are therefore compatible.

The same project makes another inversion visible. Rivas retains bodily errors as an ethical-political limit that marks the images' fabricated origin and prevents the speculative archive from covering over the violence that prevented those records from existing [@Rivas2025InexistentArchive]. Technical failure becomes provenance. A model improvement that eliminates malformed bodies can consequently remove an ethical disclosure device. "Better" generation is not monotonically better art.

Simonen and colleagues' work on default images gives a different form of upstream pressure. Their study shows that text-to-image systems can produce visually similar outputs across unrelated or unknown prompts and analyzes this phenomenon across more than 750,000 Midjourney images [@SimonenEtAl2025DefaultImages]. A default is therefore not only a UI setting selected before interaction. It can be an observable fallback behavior exposed when language fails to provide enough discriminating guidance. Deliberately poor prompts can act as probes into the generator's attractors.

Together, the minority prompt and default image reveal two opposite encounters with the prior. In one, the user adds language to push against an unwanted tendency. In the other, language stops steering and the tendency becomes visible. Both suggest that a complete archive of prompting must preserve more than successful final strings. It needs baseline behavior, failures, counter-prompts, version information, and the evidence by which a user diagnosed the problem.

# 5. Interfaces choose the cheap next move

The model is not the only place where possibility is shaped. Torricelli and colleagues' analysis of more than 145,000 prompts across two generative platforms finds that interfaces offering shortcuts for image variants and diverting attention from prompt editing are associated with reduced exploration of novel concepts and less detail in prompts [@TorricelliEtAl2023Interface]. The result supplies a concrete mechanism for platform aesthetics that does not require assuming an opaque ranking algorithm.

A platform can change creative trajectories simply by changing the cost of the next action. If "make variants" is one tap while re-description requires more effort, local exploitation becomes cheaper than conceptual movement. The interface does not need to impose a style explicitly. It can alter transition probabilities through affordances.

This distinction matters because claims about "AI style" frequently collapse multiple causal layers: model architecture, training data, prompt population, interface actions, ranking, and imitation. The evidence currently supports some mechanisms more strongly than others. Interface-mediated exploration has observational support [@TorricelliEtAl2023Interface]. The stronger claim that a particular platform ranking system causes a specific visual style requires its own receipts. A cultural-systems account should not smooth these layers into a harmonious network; it should force them to make different predictions.

The practical consequence is methodological. To study generative aesthetics, researchers should hold layers constant wherever possible. Keep the model fixed and change interface actions. Keep prompts fixed and change models. Keep architecture fixed and change training distributions where reproducible models permit it. Preserve the mismatches. "Culture" becomes analytically useful when it helps locate mechanisms rather than when it simply names everything surrounding the image.

# 6. Description changes causal position

Susan Sontag's call for a descriptive rather than over-interpretive criticism creates an unexpected bridge to generative practice. She wanted criticism to show how an artwork is what it is, resisting the reduction of sensuous form to hidden content [@Sontag1966AgainstInterpretation]. In ordinary criticism, the arrow runs from form to words. A critic observes contrast, texture, framing, rhythm, scale, or tone and develops language adequate to what is already there.

In a text-conditioned generator, much of the same vocabulary can move upstream:

\begin{quote}
FORM $\rightarrow$ WORD \hspace{1cm} becomes \hspace{1cm} WORD $\rightarrow$ CONDITIONING $\rightarrow$ FORM.
\end{quote}

The word does not deterministically compile into the visual feature, but it becomes causally operative. A descriptive vocabulary becomes a control surface. This is a deeper transformation than simply "using words to make pictures." Cultural vocabularies for noticing art can become ingredients in the statistical reproduction of future art.

Yet even here, text should not be mistaken for the essence of prompting. Oppenlaender and colleagues' body-prompting installation demonstrates generative conditioning through embodied input in a public art setting [@OppenlaenderEtAl2024BodyPrompting]. The category "prompt" survives after textual language disappears. What unifies text prompting and body prompting is not syntax but intervention into the system's next state.

That observation disciplines the stronger metaphor that "the body is a language." An input modality is not automatically a language. To establish an embodied syntax we would need evidence of stable units, recombination, learned correspondences, malformed combinations, or systematic semantics. The source establishes control, not grammar. The larger lesson is useful: prompting should be defined by its position in a generative transition before being defined by its representational medium.

# 7. The cultural loop without model learning

A final consequence follows from the circulation of prompt knowledge. Community discourse does not have to change model weights in order to change what a fixed model produces. Outputs are posted; prompts are disclosed or reverse-engineered; aesthetic judgments attach to them; terms circulate; another user inserts those terms into a new prompt; and a new output enters circulation [@Oppenlaender2022PromptModifiers]. The cultural loop can operate around a technically fixed generator.

This gives a sharper account of "meaning-in-use" for generative systems. Use can mean interpretation, but interpretation can become future input through social transmission. Reception becomes production infrastructure without any adaptive model update. What changes is the human input distribution.

The same loop also explains why technically false prompt theories can matter. A modifier may have weak causal effect yet strong social effect if it signals expertise, taste, affiliation, or adherence to a community recipe. Conversely, a technically powerful modifier may remain culturally invisible. Prompt expressions can operate on two state spaces at once: machine conditioning and social organization. The two effects should be measured separately.

# Discussion: archive the difference, not just the string

The paper's wager can now be stated compactly. **The most consequential unit of prompt culture is not the prompt term but the learned mapping from a noticed difference to a possible intervention.** This mapping is culturally acquired, technically contingent, and politically uneven.

That claim changes what should be archived. A final prompt suppresses the reason each phrase entered. A final image suppresses rejected alternatives. A prompt guide suppresses failed causal hypotheses. A screenshot suppresses model version, interface action costs, and defaults. If scholars want to understand generative art as a cultural system, they need trajectories that preserve at least:

- the desired state as understood at that moment;
- the generated candidate;
- the difference the practitioner noticed;
- the explanation the practitioner entertained;
- the intervention chosen;
- the model and interface state;
- whether the intervention worked across repetitions;
- how the technique was learned, shared, withheld, or contested.

This is not an argument for total provenance. Total provenance is impossible and can become its own fetish. It is an argument that the culturally interesting object is often the transition by which a difference becomes actionable.

The proposal also yields direct empirical tests. Expert and novice participants can be shown identical flawed generations and asked to annotate every discrepancy before editing the prompt. Their noticed differences can be compared before their vocabularies are compared. Prompt folklore can be ablated across seeds and model versions. Matched interfaces can vary only the cost of variant generation versus re-description. Cultural labels can be evaluated by practitioners from the invoked traditions rather than by generic recognizability. Default-image probes can test what surfaces when language ceases to discriminate.

# Limitations and unresolved territory

Several boundaries matter. First, the field joins sources produced across different generations of text-to-image systems. Practices documented around VQGAN-CLIP-era tools cannot automatically be generalized to contemporary diffusion and multimodal systems. The instability is part of the object: operational prompt knowledge can expire.

Second, the proposed "equipment to correct" is an extension of Geertz, not his terminology. Geertz supplies an account of culturally formed aesthetic competence; this paper asks what happens when that competence enters an iterative generative loop. Historical influence is not claimed.

Third, the argument does not show that all prompt skill is perceptual. Some expertise may be lexical, technical, strategic, social, or domain-specific. The stronger claim is that vocabularies alone cannot explain effective correction without attention to the distinctions users learn to notice.

Fourth, corpus effects, model architecture, interface design, ranking, and current user taste remain difficult to separate causally. Steyerl's "mean image" is a critical description of socially sedimented statistical rendering, not a quantitative decomposition of those causes [@Steyerl2023MeanImages]. The field needs controlled interventions rather than broader synthesis.

Finally, not every meaningful use of generative art is aimed at correction. Body prompting, chance operations, intentional misuse, and practices that cultivate surprise can reject the goal of converging on a pre-specified image. The diagnostic loop is strongest where practitioners are steering toward or away from recognizable conditions. Its boundary is exactly where "failure" ceases to be a defect and becomes the event the work was seeking.

# Conclusion: the shop makes the prompt

A prompt appears to begin with words. The research reviewed here suggests that it begins earlier, in a learned capacity to see what those words might need to change.

Geertz's shop is therefore not a metaphorical decoration for AI art. It identifies a concrete research problem. The community makes images, but it also makes the sensitivities by which images are judged; those sensitivities make failures legible; failures motivate interventions; interventions circulate as prompt lore; and that lore changes what the fixed generator is asked to produce. Meanwhile the generator carries its own inherited social distributions, defaults, and biases, forcing users to learn not only how to describe worlds but how to negotiate the machine's sedimented descriptions of worlds.

The prompt is not the cultural system. It is one move through it. The better object is the loop in which perception becomes correction and description becomes operation.

# Appendix A - Assembly Instrument

The exact assembly instrument for this working paper is preserved verbatim as `SLIPCASE_FINAL_PROMPT.txt` and `_PROMPTS/assembly_prompt__v15.55-AM.txt`. The complete prompt is not reproduced in the paper body because the package and standalone `index.html` preserve it directly.

# Appendix B - Making History

This paper was assembled from forty compiled zettels, three user-provided research PDFs, the supplied recursive forage instrument, and public source records and PDFs registered in the accompanying resource ledger. The zettel payloads in this checkpoint were reconstructed from visible conversation output rather than copied from a machine-readable full-chat export; their hashes therefore identify the compiled checkpoint payloads, not an unavailable upstream transcript. Full control, retrieval, preservation, and uncertainty notes are recorded in `000__MAKING_HISTORY.txt`.

# Appendix C - Replication Path

Checkpoint: `SLIPCASE-20260817-AIACS-01`. Begin with `000__RETURN_PATH.txt` and `000__REBUILD.txt`. The claim-to-evidence chain is in `the-shop-makes-the-prompt__SOURCE_MAP.txt`; machine state is under `_SLIPCASE/`; exact zettel payloads are root `.txt` cards with byte-identical `_MD/` mirrors. Recompute hashes before any merge and preserve unresolved addresses as ghosts rather than fuzzy-matching them.

# References
