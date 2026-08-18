from pathlib import Path
import re, json, hashlib, html, base64, os, textwrap, zipfile, shutil, subprocess, datetime
PKG=Path('/mnt/data/2026-08-17__the-shop-makes-the-prompt__SLIPCASE-20260817-AIACS-01')
cards=[]
def add(s): cards.append(textwrap.dedent(s).strip()+"\n")

add(r'''
ZETTEL

ID:
Z-AIACS-001

TITLE:
“Complementary lenses” may be where the paper stops thinking.

SOURCE:
AI Art as a Cultural System — section A08 — pp. 8–9.
PRIME ZETTEL FORAGE — INQUIRY + OPPOSITION — §§ orientation, collision, constraint.

PASSAGE:
[QUOTE]
“Each analytical lens we applied reveals a different facet, but they are ultimately complementary.”

RESEARCH OBJECT:
The synthesis converts unresolved causal disagreements into “facets” of one harmonious object.

LOCAL MOVE:
A08 resolves narrative theory, media theory, cultural analytics, cybernetics, and social systems into a single cultural-systems account.

SOURCE TERMS:
“complementary”
“nexus”
“symbolic systems”
“cybernetic systems”
“sociotechnical systems”

WHAT BECAME STRANGE:
Why should theories that locate agency, meaning, causation, and novelty in different places be complementary rather than mutually diagnostic?

QUESTION:
Which apparent “complementarities” conceal incompatible explanations of what actually produces an AI artwork?

DEEPER QUESTION:
What would happen if AI art were used not to synthesize these theories but to force them to disagree experimentally?

MECHANISM:
THEORY A assigns explanatory force to interpretation.
THEORY B assigns it to apparatus.
THEORY C assigns it to platform populations.
THEORY D assigns it to feedback.
The synthesis retains all four without determining when one explanation defeats another.

FORMAL SHIFT:
<multiple explanatory models>
→ <facets of AI art>
→ [SYNTHESIZE]
→ <one cultural-system account>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

For phenomenon P:

NARRATIVE(P) → inferred intention
MEDIA(P) → apparatus constraint
SOCIAL(P) → population/platform effect
CYBERNETIC(P) → feedback dynamics

The unresolved problem is not whether all four exist.
It is Δ explanatory power under controlled changes to P.

TENSION:
The forage protocol explicitly prefers “tensions over reconciliation” and tells us not to reconcile mismatches prematurely.

MISSING:
A case in which two lenses make different predictions.

BOUNDARY:
The source establishes coexistence of explanatory vocabularies, not their compatibility.

CITATION TRAIL:
Find empirical AI-art studies capable of discriminating platform effects, model effects, audience effects, and artist effects rather than redescribing all four.

TEST:
Take one AI-art phenomenon and construct predictions from each lens before looking at the evidence. Preserve any divergence rather than synthesizing it away.

PLATFORM:
[[AI Art as a Cultural System]]

LINKS:
[[Explanatory Competition]]
[[Cultural Systems]]
[[Against Premature Synthesis]]

BIBTEX:
@misc{AIArtCulturalSystem,
  title = {AI Art as a Cultural System},
  note = {User-provided research synthesis, sections A01--A08}
}

@misc{PrimeZettelForage,
  title = {PRIME ZETTEL FORAGE --- INQUIRY + OPPOSITION},
  note = {User-provided POML research protocol, version 3.0}
}
''')

add(r'''
ZETTEL

ID:
Z-AIACS-002

TITLE:
“AI art” may be too large an object for a Geertzian analysis.

SOURCE:
AI Art as a Cultural System — A01 and A08 — pp. 1, 9–10.

PASSAGE:
[PARAPHRASE]
The paper invokes Geertz to insist that aesthetic meaning must be located in the “life that surrounds” an artwork, then concludes by describing AI art broadly as a ritual of contemporary technoscientific society.

RESEARCH OBJECT:
A possible mismatch between a method of situated interpretation and an object defined at planetary technological scale.

LOCAL MOVE:
The paper scales from specific practices—prompt sharing, installations, particular artists—to “AI art” as a cultural system.

SOURCE TERMS:
“tenor of their setting”
“meaning-in-use”
“cultural system”
“ritual”
“technoscientific society”

WHAT BECAME STRANGE:
The more seriously we take context, the less obvious it becomes that “AI art” is a coherent cultural unit.

QUESTION:
What is the smallest social unit within which an AI artwork has a stable enough “setting” to be interpreted thickly?

DEEPER QUESTION:
Is the relevant cultural system Midjourney, a Discord server, a prompt-sharing lineage, an art school, a model community, a gallery circuit, or something else entirely?

MECHANISM:
A broad technological category groups practices whose local norms may differ radically.

FORMAL SHIFT:
<heterogeneous local practices>
→ <AI art>
→ [AGGREGATE]
→ <single cultural system>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

CULTURAL_UNIT ≠ TECHNOLOGY_CLASS

Possible unit:
{participants + repeated practices + shared distinctions + sanctions + circulation channels}

BOUNDARY:
The paper demonstrates that AI art is socially situated. It does not establish that all AI-art practices comprise one cultural system.

TENSION:
The Geertzian demand for setting pushes downward toward local practice; the paper's synthesis pushes upward toward civilization-scale diagnosis.

MISSING:
An argument for the scale at which the boundaries of the proposed cultural system should be drawn.

CITATION TRAIL:
Return to Geertz’s actual ethnographic treatment of artistic practices and compare its scale of description with contemporary ethnographies of Midjourney, Stable Diffusion, or prompt communities.

TEST:
Perform the same interpretive analysis at three scales:
one artist,
one platform community,
“AI art.”
Record which explanatory distinctions disappear as scale increases.

PLATFORM:
[[AI Art as a Cultural System]]

LINKS:
[[Unit of Analysis]]
[[Thick Description]]
[[Platform Cultures]]

BIBTEX:
@misc{AIArtCulturalSystem,
  title = {AI Art as a Cultural System},
  note = {User-provided research synthesis, sections A01 and A08}
}
''')

add(r'''
ZETTEL

ID:
Z-AIACS-003

TITLE:
An “AI aesthetic” may be a population distribution mistaken for a machine property.

SOURCE:
AI Art as a Cultural System — A03 and A07 — pp. 3, 7.

PASSAGE:
[QUOTE]
“What you think comes from the ‘machine’ in reality comes from its users.”

RESEARCH OBJECT:
Aesthetic style may emerge statistically from repeated user choices rather than reside intrinsically in a generative model.

LOCAL MOVE:
The paper uses Manovich to relocate apparent machine style into user populations and platform culture.

SOURCE TERMS:
“AI aesthetics”
“users”
“mass tastes”
“popular outputs”
“platform-driven network effects”
“style references”

WHAT BECAME STRANGE:
A style can appear machine-authored even if no individual user intends to create that collective style.

QUESTION:
At what point does an aggregate distribution of user choices become perceptually indistinguishable from an intrinsic property of the model?

DEEPER QUESTION:
Can a population accidentally author an aesthetic that every individual then experiences as an affordance of the machine?

MECHANISM:
many users
→ repeated prompt/style choices
→ disproportionately visible motifs
→ learned expectations
→ further imitation
→ apparent “AI style”

FORMAL SHIFT:
<distributed user selections>
→ <output distribution>
→ [REPEAT + CIRCULATE]
→ <perceived model aesthetic>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

PERCEIVED_STYLE =
f(model priors,
  user preference distribution,
  interface defaults,
  circulation,
  copying,
  ranking)

TENSION:
A03 simultaneously argues that algorithms leave “aesthetic fingerprints.” The paper therefore contains two competing causal accounts: machine-specific constraint and population-specific taste.

MISSING:
A way to estimate how much stylistic variance comes from models versus users versus platform circulation.

BOUNDARY:
The source does not establish that model architecture is aesthetically irrelevant.

CITATION TRAIL:
Lev Manovich on AI aesthetics; empirical studies of prompt corpora; comparative studies of output distributions across generative models.

TEST:
Hold prompts constant across several models, then hold model constant across several user populations. Compare which manipulation changes perceived “AI style” more.

PLATFORM:
[[AI Art as a Cultural System]]

LINKS:
[[Population Aesthetics]]
[[Platform Style]]
[[Model Fingerprints]]

BIBTEX:
@misc{AIArtCulturalSystem,
  title = {AI Art as a Cultural System},
  note = {User-provided synthesis, sections A03 and A07}
}
''')

add(r'''
ZETTEL

ID:
Z-AIACS-004

TITLE:
The default may be a hidden coauthor.

SOURCE:
AI Art as a Cultural System — A03, A07, A08 — pp. 2–3, 7, 9.

PASSAGE:
[PARAPHRASE]
The paper repeatedly says that algorithms, interfaces, training data, platform tendencies, and defaults constrain what users produce.

RESEARCH OBJECT:
Creative decisions can be made before the artist types anything.

LOCAL MOVE:
The source treats apparatus constraints as contributors to aesthetic form but never isolates the special role of defaults.

SOURCE TERMS:
“affordances”
“constraints”
“default biases”
“platforms”
“user interface”
“nudges”

WHAT BECAME STRANGE:
The prompt receives authorship attention precisely because it is visible, while defaults may determine far more while remaining invisible.

QUESTION:
How much of a generated image has already been decided by the platform before the user's description arrives?

DEEPER QUESTION:
Is prompting partly the experience of selecting within a world whose strongest aesthetic decisions have already been silently made?

MECHANISM:
training distribution
+ model architecture
+ safety rules
+ sampler
+ system prompt
+ interface defaults
→ prior output space

user prompt
→ local perturbation of that prior

FORMAL SHIFT:
<platform configuration>
→ <default possibility distribution>
→ [PROMPT]
→ <conditioned output>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

OUTPUT = GENERATOR(DEFAULTS, PROMPT)

The critical variable may be:

Δprompt = distance(output_with_prompt, output_under_default)

rather than merely inspecting the prompt text.

TENSION:
Prompt culture foregrounds linguistic virtuosity, while apparatus theory suggests much causal force resides elsewhere.

MISSING:
The source does not enumerate actual defaults or establish their relative contribution.

BOUNDARY:
“Hidden coauthor” is our inference about causal significance, not source terminology.

CITATION TRAIL:
Platform documentation, model cards, UI histories, sampler defaults, internal system instructions where available, and studies of default effects in interface design.

TEST:
Generate systematically with blank, minimal, ordinary, and highly specified prompts while changing one hidden/default parameter at a time.

PLATFORM:
[[AI Art as a Cultural System]]

LINKS:
[[Default Images]]
[[Invisible Authorship]]
[[Prompt as Perturbation]]

BIBTEX:
@misc{AIArtCulturalSystem,
  title = {AI Art as a Cultural System},
  note = {User-provided synthesis, sections A03, A07, and A08}
}
''')

add(r'''
ZETTEL

ID:
Z-AIACS-005

TITLE:
Prompt craft may be a vernacular before it is a language.

SOURCE:
AI Art as a Cultural System — A07 — p. 7.

PASSAGE:
[PARAPHRASE]
Prompt engineering is described as a learned skill; experienced practitioners acquire “style-specific vocabulary,” exchange prompt formulas, and develop shared lore.

RESEARCH OBJECT:
Prompt competence appears to be socially acquired vocabulary tied to communities of practice, not merely knowledge of software commands.

LOCAL MOVE:
The paper moves prompting from individual instruction-writing into collective craft transmission.

SOURCE TERMS:
“style-specific vocabulary”
“shared lore”
“technique”
“recipes”
“magic spells”
“communal workshop”

WHAT BECAME STRANGE:
Prompt expertise may reside less in knowing what words literally mean than in knowing what words do inside a particular model-community pair.

QUESTION:
When does recurrent model-specific wording become a technical vernacular?

DEEPER QUESTION:
Can a community possess a prompt dialect whose expressions are operationally meaningful even when their literal semantics are weak or misleading?

MECHANISM:
model behavior
→ experimental phrase
→ useful output
→ community circulation
→ copied convention
→ stabilized prompt term

FORMAL SHIFT:
<experimental wording>
→ <repeatable model effect>
→ [SOCIAL TRANSMISSION]
→ <vernacular technique>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

PROMPT_TERM meaning has at least two layers:

SEMANTIC(term)
OPERATIONAL(term, model_version, community_practice)

These can diverge.

TENSION:
If terms acquire meaning through model-specific effects, model updates can destroy the vernacular without changing the words.

MISSING:
Longitudinal evidence showing which prompt terms persist, mutate, or become obsolete across model versions.

BOUNDARY:
The source establishes shared vocabulary and learned skill, not a formal language.

CITATION TRAIL:
“Prompting AI Art: An Investigation into the Creative Skill of Prompt Engineering”; historical prompt guides; archived Discord discussions; version-specific prompt manuals.

TEST:
Track fifty recurrent prompt expressions across model versions and measure whether their output effects remain stable while their social use persists.

PLATFORM:
[[Prompt Practice]]

LINKS:
[[Operational Semantics]]
[[Prompt Vernacular]]
[[Model Drift]]

BIBTEX:
@misc{AIArtCulturalSystem,
  title = {AI Art as a Cultural System},
  note = {User-provided synthesis, section A07}
}
''')

add(r'''
ZETTEL

ID:
Z-AIACS-006

TITLE:
The “minority prompt” makes bias correction a user operation.

SOURCE:
AI Art as a Cultural System — A07 — p. 7.

PASSAGE:
[QUOTE]
Rivas develops a “minority prompt”: an instruction designed to counteract biases in model training databases.

RESEARCH OBJECT:
A structural representational problem is partially converted into extra linguistic work performed at generation time.

LOCAL MOVE:
The artist does not merely describe a desired image; he uses the prompt against the model's prior.

SOURCE TERMS:
“minority prompt”
“counteract”
“biases”
“instruction”
“activism”

WHAT BECAME STRANGE:
The same text box serves simultaneously as artistic description and corrective intervention against the system receiving the description.

QUESTION:
What kind of interface is a prompt box when some users must spend part of their description counteracting the model before they can describe what they want?

DEEPER QUESTION:
Does prompt-based correction relocate representational governance from model builders into the hands of individual users?

MECHANISM:
biased training distribution
→ undesired model prior
→ corrective linguistic intervention
→ altered generation distribution

FORMAL SHIFT:
<representational absence / bias>
→ <counter-instruction>
→ [PROMPT AGAINST PRIOR]
→ <otherwise less-likely representation>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

DESIRED_GENERATION =
PROMPT(content)
+
PROMPT(counter-prior)

The second term exists because the default distribution is not neutral.

TENSION:
Prompting is celebrated as democratized creative skill, but this case suggests competence may include learning how to compensate for failures users did not create.

MISSING:
Comparative evidence measuring how much corrective prompting different desired identities, bodies, relationships, or cultural settings require.

BOUNDARY:
The paper gives one politically explicit strategy; it does not establish that all marginalized users experience the same corrective burden.

CITATION TRAIL:
Felipe Rivas San Martín; scholarship on “Un archivo queer inexistente”; work on representational harms and text-to-image prompting.

TEST:
Construct matched image requests differing only in the represented social relation. Measure how many corrective prompt operations are needed to produce comparable fidelity.

PLATFORM:
[[Prompt Practice]]

LINKS:
[[Minority Prompt]]
[[Corrective Description]]
[[Default Bias]]

BIBTEX:
@misc{AIArtCulturalSystem,
  title = {AI Art as a Cultural System},
  note = {User-provided synthesis, section A07}
}
''')

add(r'''
ZETTEL

ID:
Z-AIACS-007

TITLE:
A better model could make a synthetic archive ethically worse.

SOURCE:
AI Art as a Cultural System — A07 — pp. 6–7.

PASSAGE:
[QUOTE]
Rivas treats AI glitches as “evidences of their simulatory character.”

RESEARCH OBJECT:
Technical failure functions as provenance.

LOCAL MOVE:
Rather than hiding malformed bodies and faces, the artwork recruits them to mark the images as fabricated historical possibilities.

SOURCE TERMS:
“simulatory character”
“bodily dissidence”
“this was not”
“fake archive”
“glitches”

WHAT BECAME STRANGE:
The artifact's ethical legibility depends partly on defects that model developers are trying to eliminate.

QUESTION:
What happens to the politics of a synthetic counter-archive when generative images become indistinguishable from documentary photographs?

DEEPER QUESTION:
Can technical progress erase a medium's accidental disclosure mechanism faster than cultural conventions of provenance replace it?

MECHANISM:
generation defect
→ perceptual anomaly
→ recognition of simulation
→ reduced documentary confusion
→ political reading as counter-history rather than recovered history

FORMAL SHIFT:
<synthetic historical scene>
→ <visible generation defect>
→ [READ AS SIMULATION]
→ <counter-archive rather than counterfeit document>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

MODEL_QUALITY ↑
VISIBLE_SIMULATION_SIGNAL ↓

If the work relies on that signal:

MODEL_QUALITY ↑
may imply
ETHICAL_DISCLOSURE ↓

TENSION:
Ordinary engineering defines malformed hands and faces as failures; the artwork makes those failures part of its truth conditions.

MISSING:
What replaces glitch-based disclosure when glitches disappear?

BOUNDARY:
The source supports this relation for Rivas's project, not for synthetic archives generally.

CITATION TRAIL:
Rivas San Martín; scholarship on synthetic archives, documentary truth, provenance, watermarking, and AI-generated historical imagery.

TEST:
Recreate equivalent fictional archival scenes with several generations of image models. Ask viewers whether they interpret each as documentary, reconstruction, or fiction before receiving contextual labels.

PLATFORM:
[[Synthetic Archives]]

LINKS:
[[Failure as Disclosure]]
[[Synthetic Fossils]]
[[Provenance Aesthetics]]

BIBTEX:
@misc{AIArtCulturalSystem,
  title = {AI Art as a Cultural System},
  note = {User-provided synthesis, section A07}
}
''')

add(r'''
ZETTEL

ID:
Z-AIACS-008

TITLE:
The implied author may become a diagnostic error rather than an author theory.

SOURCE:
AI Art as a Cultural System — A02 — pp. 1–2.

PASSAGE:
[PARAPHRASE]
Readers infer an intentional persona from a work even when that inferred intentionality reveals little about the process that actually produced it.

RESEARCH OBJECT:
AI increases the possible distance between experienced intention and production history.

LOCAL MOVE:
Narrative theory explains why an artwork can appear to “speak” despite lacking a single human intentional source.

SOURCE TERMS:
“implied author”
“reader-created construct”
“intentionality”
“actual process”
“persona”

WHAT BECAME STRANGE:
The theory is usually used to preserve interpretation despite uncertain authorship. AI may let us use the same phenomenon to measure how badly perceived authorship diverges from causal authorship.

QUESTION:
How large can the gap become between the agency audiences perceive and the agency the production process actually contains?

DEEPER QUESTION:
Could AI art become an experimental instrument for studying the human tendency to hallucinate coherent makers behind artifacts?

MECHANISM:
artifact cues
→ stylistic coherence
→ inferred persona
→ attributed intention

while:

actual production
→ distributed operations
→ no corresponding unified intentional agent

FORMAL SHIFT:
<artifact>
→ <perceived regularities>
→ [INFER AGENT]
→ <implied author>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

AUTHORSHIP_GAP =
distance(
  inferred agency map,
  documented production agency map
)

TENSION:
The paper treats implied authorship primarily as a reason AI art can still mean. The same mechanism may instead expose systematic misattribution.

MISSING:
Experiments comparing audience attribution with known production histories.

BOUNDARY:
The source does not claim implied authorship is an error; that is our proposed diagnostic use.

CITATION TRAIL:
Narratology on implied authors; empirical work on intentional stance, anthropomorphism, and agency attribution to generative systems.

TEST:
Show audiences identical outputs accompanied by different true production pipelines, then compare inferred authors, intentions, and responsibility.

PLATFORM:
[[Authorship After Generation]]

LINKS:
[[Implied Author]]
[[Agency Attribution]]
[[Causal Opacity]]

BIBTEX:
@misc{AIArtCulturalSystem,
  title = {AI Art as a Cultural System},
  note = {User-provided synthesis, section A02}
}
''')

add(r'''
ZETTEL

ID:
Z-AIACS-009

TITLE:
“Distributed authorship” is too blunt; generation contains different kinds of control.

SOURCE:
AI Art as a Cultural System — A03 and A07 — pp. 2, 7–8.

PASSAGE:
[PARAPHRASE]
The paper calls AI creation hybrid or distributed because humans select prompts or training inputs while the apparatus produces outcomes beyond direct control.

RESEARCH OBJECT:
Authorship may need to be decomposed into operations before it can be distributed.

LOCAL MOVE:
The paper asks whether credit belongs to prompt writers, model builders, or machines.

SOURCE TERMS:
“hybrid authorship”
“distributed”
“prompt”
“training sets”
“machine's creators”
“credit”

WHAT BECAME STRANGE:
“Who authored it?” may be malformed if different parties control different transformations.

QUESTION:
Which operations in generative production are actually being bundled together under the word authorship?

DEEPER QUESTION:
Would disputes about AI authorship become clearer if credit attached to operations rather than persons?

MECHANISM:
corpus construction
→ model design/training
→ interface/default configuration
→ prompting
→ generation
→ selection
→ editing
→ circulation

Different actors intervene at different transitions.

FORMAL SHIFT:
<production chain>
→ <actor-operation assignments>
→ [COLLAPSE]
→ <single authorship question>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

AUTHORSHIP_STACK = {
  dataset_authority,
  model_authority,
  parameter_authority,
  descriptive_authority,
  selection_authority,
  transformation_authority,
  publication_authority
}

TENSION:
The paper recognizes distributed agency but returns repeatedly to singular nouns: “artist,” “machine,” “creator,” “author.”

MISSING:
A vocabulary distinguishing forms of creative control without assuming they are interchangeable.

BOUNDARY:
The proposed stack is analytical reconstruction, not source syntax.

CITATION TRAIL:
Flusser on apparatus; work on distributed authorship; legal and philosophical analyses distinguishing conception, execution, selection, and control.

TEST:
Describe one finished AI artwork only as an operation ledger. Then ask where alternative theories of authorship place the decisive threshold.

PLATFORM:
[[Authorship After Generation]]

LINKS:
[[Operation Ledger]]
[[Agency Stack]]
[[Prompt Is Not the Whole Program]]

BIBTEX:
@misc{AIArtCulturalSystem,
  title = {AI Art as a Cultural System},
  note = {User-provided synthesis, sections A03 and A07}
}
''')

add(r'''
ZETTEL

ID:
Z-AIACS-010

TITLE:
Feedback is not yet autopoiesis.

SOURCE:
AI Art as a Cultural System — A05 — p. 4.

PASSAGE:
[PARAPHRASE]
The paper describes a GAN generator/discriminator loop as “autopoietic in a technical sense,” then moves to Parisi's critique of recursive epistemology and reduction of difference.

RESEARCH OBJECT:
Recursion, feedback, adaptation, autonomy, and autopoiesis are being allowed to slide into one another.

LOCAL MOVE:
A systems vocabulary is transferred from social theory and cybernetics onto machine-learning architecture.

SOURCE TERMS:
“autopoiesis”
“recursive loop”
“feedback”
“autonomy”
“recursive epistemology”
“reduction of difference”

WHAT BECAME STRANGE:
Why should two components repeatedly adjusting one another count as self-production?

QUESTION:
What minimum operation distinguishes autopoiesis from ordinary iterative optimization?

DEEPER QUESTION:
How much conceptual work in AI theory is being done by treating recursion as evidence of life-like organizational autonomy?

MECHANISM:
generator output
→ discriminator evaluation
→ parameter update
→ new generator output

The unresolved issue:
Does this loop reproduce the organization that produces it, or merely update variables inside a designed architecture?

FORMAL SHIFT:
<GAN training loop>
→ <recursive feedback>
→ [NAME AS AUTOPOIESIS]
→ <machine autonomy>

SOURCE FORMALISM:
Generator/discriminator recursion is described, but no formal criteria for autopoiesis are supplied.

OUR FORMALIZATION:
NONE

TENSION:
The same section warns that recursive closure may reduce difference. Calling recursion “autopoietic” risks celebrating the very closure the critique problematizes.

MISSING:
The operative definition of autopoiesis being used and evidence that the GAN meets it.

BOUNDARY:
The source licenses questioning the transfer; it does not establish that the use is incorrect.

CITATION TRAIL:
Luhmann; Maturana and Varela; Luciana Parisi; scholarship distinguishing feedback, self-organization, operational closure, and autopoiesis.

TEST:
Extract necessary conditions for autopoiesis from the cited theoretical lineage and evaluate the described GAN loop against each condition individually.

PLATFORM:
[[Cybernetic AI Art]]

LINKS:
[[Feedback Is Not Autopoiesis]]
[[Recursive Epistemology]]
[[Concept Migration]]

BIBTEX:
@misc{AIArtCulturalSystem,
  title = {AI Art as a Cultural System},
  note = {User-provided synthesis, section A05}
}
''')
add(r'''
ZETTEL

ID:
Z-AIACS-011

TITLE:
Randomness is not the same thing as difference.

SOURCE:
AI Art as a Cultural System — A05 — pp. 4–5.

PASSAGE:
[PARAPHRASE]
After describing AI's tendency to reproduce existing norms, the paper points to artists injecting randomness or noise to produce unexpected outputs and “introduce difference.”

RESEARCH OBJECT:
Statistical unpredictability and culturally consequential alterity are separate variables.

LOCAL MOVE:
Noise becomes the proposed escape mechanism from recursive sameness.

SOURCE TERMS:
“randomness”
“noise”
“difference”
“unexpected”
“surprise”
“novel territory”

WHAT BECAME STRANGE:
A system can generate an arbitrarily unlikely output without escaping the categories from which its likelihoods were built.

QUESTION:
What has to happen for stochastic deviation to become meaningful difference rather than unusual variation?

DEEPER QUESTION:
Can a generative system produce alterity merely by moving toward the tails of its own distribution?

MECHANISM:
existing distribution
→ perturbation/noise
→ improbable output

UNRESOLVED:

improbable output
?→ culturally new distinction

FORMAL SHIFT:
<trained possibility space>
→ <random perturbation>
→ [GENERATE OUTLIER]
→ <claimed difference>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

SURPRISE ≠ DIFFERENCE

surprisal(x) = rarity relative to model expectation

difference(x) requires an additional criterion:
a changed distinction, relation, category, or practice.

TENSION:
Parisi's “reduction of difference” is an epistemic/cultural critique; noise is a statistical operation. The paper moves between these levels without demonstrating the bridge.

MISSING:
A criterion for culturally meaningful difference.

BOUNDARY:
The source supports randomness as an artistic strategy; it does not prove randomness escapes recursive epistemology.

CITATION TRAIL:
Luciana Parisi; cybernetic theories of variety; artistic uses of indeterminacy; novelty metrics in computational creativity.

TEST:
Compare highly stochastic outputs with deliberately counter-normative but low-randomness outputs. Ask whether rarity and perceived conceptual difference covary.

PLATFORM:
[[Cybernetic AI Art]]

LINKS:
[[Difference Is Not Noise]]
[[Novelty]]
[[Counterfactual Generation]]

BIBTEX:
@misc{AIArtCulturalSystem,
  title = {AI Art as a Cultural System},
  note = {User-provided synthesis, section A05}
}
''')

add(r'''
ZETTEL

ID:
Z-AIACS-012

TITLE:
Semantic nonsense can turn interpretation itself into the artwork's observable behavior.

SOURCE:
AI Art as a Cultural System — A05 — pp. 4–5.

PASSAGE:
[PARAPHRASE]
Feingold's conversational heads and Eltes's chatbots generate exchanges that appear semantically plausible but frustrate coherent meaning, making spectators aware of their own attempts to repair the dialogue.

RESEARCH OBJECT:
A failed machine conversation can function as an instrument that elicits human interpretive labor.

LOCAL MOVE:
The artwork relocates meaning from machine dialogue into the spectator's effort to make the dialogue meaningful.

SOURCE TERMS:
“semantically plausible”
“ultimately senseless”
“impose meaning”
“derive sense”
“meaning-making process”

WHAT BECAME STRANGE:
The artwork may succeed because the conversation fails.

QUESTION:
Can machine incoherence be used deliberately to measure how much meaning spectators are willing to supply?

DEEPER QUESTION:
What kinds of surface coherence trigger the strongest repair behavior before audiences abandon interpretation altogether?

MECHANISM:
locally plausible language
→ expectation of coherent agent
→ global semantic failure
→ spectator repair
→ awareness of repair

FORMAL SHIFT:
<machine utterances>
→ <partial coherence>
→ [HUMAN REPAIR]
→ <experienced meaning>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

INTERPRETIVE_LABOR =
meaning attributed
− meaning recoverable from interaction structure

TENSION:
The source initially treats human meaning-making as what lets AI artworks function culturally. These installations suggest that same tendency can be made the object of critique.

MISSING:
A method for observing or measuring interpretive repair rather than inferring it after the fact.

BOUNDARY:
The source does not claim spectators are always fooled or that no machine meaning exists.

CITATION TRAIL:
Ken Feingold; Jonas Eltes; intentional stance; ELIZA effect; studies of coherence attribution in human-computer interaction.

TEST:
Systematically vary local grammatical plausibility and global conversational coherence while recording when viewers attribute intention, narrative, personality, or breakdown.

PLATFORM:
[[Meaning Repair]]

LINKS:
[[Causal Hallucination]]
[[Implied Agent]]
[[Semantic Plausibility]]

BIBTEX:
@misc{AIArtCulturalSystem,
  title = {AI Art as a Cultural System},
  note = {User-provided synthesis, section A05}
}
''')

add(r'''
ZETTEL

ID:
Z-AIACS-013

TITLE:
The body can function as a query operator.

SOURCE:
AI Art as a Cultural System — A06 — pp. 5–6.

PASSAGE:
[PARAPHRASE]
In Cacophonic Choir, approaching a sculptural agent changes garbled sound into semantically coherent testimony; physical proximity determines what can be heard.

RESEARCH OBJECT:
Movement through space performs an information-retrieval operation.

LOCAL MOVE:
The installation turns bodily distance into a parameter of narrative intelligibility.

SOURCE TERMS:
“proximity”
“sonically clearer”
“semantically more coherent”
“first-hand account”
“tune into”
“listening”

WHAT BECAME STRANGE:
The spectator does not merely move toward content. Moving is the command that transforms the content.

QUESTION:
What changes when bodily position is not navigation through a narrative but part of the narrative's executable syntax?

DEEPER QUESTION:
Can embodiment be understood as an input language whose gestures compile directly into disclosure, occlusion, emphasis, or memory?

MECHANISM:
body position
→ sensed distance
→ signal transformation
→ semantic legibility
→ testimony encountered

FORMAL SHIFT:
<BODY DISTANCE>
→ <proximity value>
→ [MODULATE SIGNAL]
→ <NARRATIVE LEGIBILITY>

SOURCE FORMALISM:
The source explicitly describes distance-dependent changes in sonic clarity and semantic coherence.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

LISTEN(distance):

if distance decreases:
    noise decreases
    testimony legibility increases

TENSION:
Narrative theory usually asks how an audience interprets representation. Here an audience action changes the representational conditions themselves.

MISSING:
A vocabulary distinguishing interpretation of a narrative from execution of a narrative interface.

BOUNDARY:
The source describes this operation in Cacophonic Choir; it does not establish it as a general property of AI art.

CITATION TRAIL:
Şölen Kıratlı, Hannah Wolfe, Alex Bundy; embodied interaction; locative narrative; interface dramaturgy.

TEST:
Rewrite the installation as a state machine in which bodily movement is the only input. Determine which parts of its meaning survive when spatial execution is replaced by a button.

PLATFORM:
[[Executable Narrative]]

LINKS:
[[Body as Input]]
[[Operative Ekphrasis]]
[[Embodied Query]]

BIBTEX:
@misc{AIArtCulturalSystem,
  title = {AI Art as a Cultural System},
  note = {User-provided synthesis, section A06}
}
''')

add(r'''
ZETTEL

ID:
Z-AIACS-014

TITLE:
A generative narrative may need to be read as a rule for producing stories, not as a story.

SOURCE:
AI Art as a Cultural System — A06 — p. 6.

PASSAGE:
[PARAPHRASE]
The paper proposes “system-narratives” in which audiences assemble narratives through interaction and generated content varies in response to input.

RESEARCH OBJECT:
The enduring object may be a generative procedure while each experienced narrative is only one execution.

LOCAL MOVE:
The paper moves from fixed narrative content toward systems that generate contingent narrative instances.

SOURCE TERMS:
“system-narratives”
“experiential narratives”
“algorithmically varied”
“personalized”
“co-creating”
“living system of symbols”

WHAT BECAME STRANGE:
Two spectators can encounter different texts and still be said to have experienced “the same work.”

QUESTION:
What is the work when none of its individual narrative realizations is identical to the work's generative capacity?

DEEPER QUESTION:
Does criticism of generative narrative require reading transition rules, memory, constraints, and possibility spaces rather than privileged outputs?

MECHANISM:
participant input
+ system state
+ generative procedure
→ narrative event
→ changed state
→ next possible event

FORMAL SHIFT:
<fixed narrative artifact>
→ <generative narrative system>
→ [EXECUTE WITH PARTICIPANT]
→ <one narrative trajectory>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

WORK = {STATE, RULES, INPUT_SPACE, GENERATOR}

STORY_i = EXECUTE(WORK, interaction_history_i)

Therefore:

STORY_i ≠ WORK

TENSION:
The paper still frequently interprets AI works through particular visible outputs even while describing systems whose identity exceeds any one output.

MISSING:
A critical method for sampling a generative work's unrealized possibilities.

BOUNDARY:
The source identifies variable system-narratives but does not supply this formal distinction.

CITATION TRAIL:
Interactive fiction; procedural rhetoric; generative literature; game studies; computational narratology.

TEST:
Analyze fifty runs of the same generative narrative. Separate features invariant across runs from features belonging only to particular trajectories.

PLATFORM:
[[Executable Narrative]]

LINKS:
[[The Prompt Is Not the Program]]
[[Program Versus Execution]]
[[Narrative State Space]]

BIBTEX:
@misc{AIArtCulturalSystem,
  title = {AI Art as a Cultural System},
  note = {User-provided synthesis, section A06}
}
''')

add(r'''
ZETTEL

ID:
Z-AIACS-015

TITLE:
“Prompting is ritual” remains an analogy until we find its sanctions.

SOURCE:
AI Art as a Cultural System — A07 and A08 — pp. 7–10.

PASSAGE:
[PARAPHRASE]
The paper compares prompts to recipes and magic spells, calls prompting a performative ritual, and finally describes AI art itself as a “ritual of our technoscientific society.”

RESEARCH OBJECT:
“Ritual” enters first as metaphor and later carries explanatory weight.

LOCAL MOVE:
Repeated prompt practice, communal norms, mentorship, and taboos are gathered under a ritual vocabulary.

SOURCE TERMS:
“ritual”
“incantations”
“oracle”
“performative”
“norms”
“mentorship”
“taboos”

WHAT BECAME STRANGE:
Repetition alone does not tell us whether something is a ritual, craft routine, game, protocol, superstition, pedagogy, or optimization practice.

QUESTION:
What observable property would make prompting ritual rather than merely repeated technical practice?

DEEPER QUESTION:
Where are the initiations, sanctions, sacred distinctions, efficacy beliefs, authorized performers, failures, and boundary-maintaining acts?

MECHANISM:
repeated practice
+ shared vocabulary
+ community transmission
+ normative distinctions
→ POSSIBLY ritualization

The missing step is the criterion.

FORMAL SHIFT:
<prompt practice>
→ <ritual metaphor>
→ [GENERALIZE]
→ <AI art as societal ritual>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
NONE

TENSION:
The paper begins with a Geertzian demand for diagnostics grounded in context, yet one of its most important anthropological terms is not itself diagnostically established.

MISSING:
Ethnographic evidence showing what participants treat as obligatory, efficacious, taboo, transformative, or identity-bearing.

BOUNDARY:
The source documents ritual-like features but does not establish an anthropological classification.

CITATION TRAIL:
Geertz on ritual and symbolic systems; anthropology of technical practice; ethnographies of prompt communities.

TEST:
Observe one prompt community without using the word ritual. Record repeated actions, sanctions, initiations, taboos, status markers, failure interpretations, and efficacy beliefs. Only afterward test whether “ritual” explains more than “craft.”

PLATFORM:
[[Prompt Practice]]

LINKS:
[[Ritual or Craft]]
[[Prompt Lore]]
[[Thick Description]]

BIBTEX:
@misc{AIArtCulturalSystem,
  title = {AI Art as a Cultural System},
  note = {User-provided synthesis, sections A07 and A08}
}
''')

add(r'''
ZETTEL

ID:
Z-AIACS-016

TITLE:
The prompt may be less interesting than the correction.

SOURCE:
AI Art as a Cultural System — A07 — p. 7.

PASSAGE:
[PARAPHRASE]
Prompt expertise develops through practice, copying, experimentation, model-specific vocabulary, and strategies for counteracting model tendencies.

RESEARCH OBJECT:
The informative unit of prompting may be the sequence of failures and repairs rather than the successful final text.

LOCAL MOVE:
The paper describes iteration socially but still treats “the prompt” as a visible artifact.

SOURCE TERMS:
“learned through practice”
“improved”
“style-specific vocabulary”
“iterating”
“try adding”
“prompt formula”

WHAT BECAME STRANGE:
A finished prompt hides the observations that made each phrase necessary.

QUESTION:
If prompt competence is learned through response to outputs, why treat the final prompt as the creative object rather than the trajectory of corrections that produced it?

DEEPER QUESTION:
Does generative authorship reside in a feedback history?

MECHANISM:
description_0
→ output_0
→ noticed failure_0
→ correction_1
→ output_1
→ noticed failure_1
→ correction_2
→ …

FORMAL SHIFT:
<desired artifact>
→ <provisional description>
→ [GENERATE / INSPECT / CORRECT]
→ <progressively specified artifact>

SOURCE FORMALISM:
The source describes iterative prompt modification but provides no explicit loop formalism.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

P_0 → G(P_0) → ERROR_0
P_1 = P_0 + correction(ERROR_0)
P_1 → G(P_1) → ERROR_1
...

The specification grows from encountered failure.

TENSION:
Prompt guides preserve successful incantations; learning actually occurs through unstable encounters between wording and outputs.

MISSING:
Prompt histories, rejected generations, and correction sequences.

BOUNDARY:
The source supports iteration but does not claim the loop rather than the final prompt is the proper unit of authorship.

CITATION TRAIL:
Prompt-engineering process studies; interface logs; version histories; creative process research; studies retaining rejected generations.

TEST:
Archive complete generation histories from expert and novice users. Compare final prompts with the sequence of constraints discovered through failures.

PLATFORM:
[[Prompt Practice]]

LINKS:
[[Deferred Formalization]]
[[Failure Becomes Specification]]
[[Prompt History]]

BIBTEX:
@misc{AIArtCulturalSystem,
  title = {AI Art as a Cultural System},
  note = {User-provided synthesis, section A07}
}
''')

add(r'''
ZETTEL

ID:
Z-AIACS-017

TITLE:
“Meaning-in-use” splits when use also changes what the system can do.

SOURCE:
AI Art as a Cultural System — A01, A05, A08 — pp. 1, 5, 9.

PASSAGE:
[PARAPHRASE]
The paper begins with meaning emerging from social use, then describes feedback systems in which human responses, curation, and interaction participate in changing artistic behavior.

RESEARCH OBJECT:
“Use” can name interpretation of an artifact or an operation inside a changing system.

LOCAL MOVE:
Geertzian meaning-in-use and cybernetic feedback are placed beside one another without distinguishing their senses of use.

SOURCE TERMS:
“meaning-in-use”
“feedback”
“reaction”
“adaptive”
“iteratively refine”
“interaction”

WHAT BECAME STRANGE:
In a painting, use may change interpretation without changing the painting. In an adaptive generative system, use can become input.

QUESTION:
What happens to cultural interpretation when the act that gives an artifact meaning also participates in producing its next state?

DEEPER QUESTION:
When does reception cease to be merely reception?

MECHANISM:
SEMIOTIC USE:
artifact → encounter → interpretation

CYBERNETIC USE:
system_state + encounter → input → new_system_state

FORMAL SHIFT:
<use as interpretation>
→ <interaction data>
→ [FEEDBACK]
→ <changed behavior>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

USE_s = interpretive consequence

USE_c = state-changing operation

The two can coexist but should not be collapsed.

TENSION:
The cultural-systems framing treats use as the source of meaning; the systems framing can make use part of the source of subsequent outputs.

MISSING:
Concrete cases specifying whether user interaction persists, trains, ranks, personalizes, or otherwise changes future generations.

BOUNDARY:
The paper does not establish that every platform learns from every user's interaction.

CITATION TRAIL:
Second-order cybernetics; recommender feedback; interactive generative artworks; platform personalization; Geertzian meaning-in-use.

TEST:
For one AI-art platform, trace every form of user behavior and classify it as:
interpretive only,
ephemeral input,
persistent personalization,
ranking signal,
or model-training signal.

PLATFORM:
[[AI Art as a Cultural System]]

LINKS:
[[Reception Becomes Operation]]
[[Meaning-in-Use]]
[[Feedback Culture]]

BIBTEX:
@misc{AIArtCulturalSystem,
  title = {AI Art as a Cultural System},
  note = {User-provided synthesis, sections A01, A05, and A08}
}
''')

add(r'''
ZETTEL

ID:
Z-AIACS-018

TITLE:
The strongest platform claim in the paper is also one of its least demonstrated.

SOURCE:
AI Art as a Cultural System — A07 — p. 7.

PASSAGE:
[PARAPHRASE]
The paper says Midjourney's rewards—how images are ranked and displayed—favor a particular high-fidelity illustrative look, helping that look become a de facto style.

RESEARCH OBJECT:
A specific causal mechanism is asserted between platform ranking and aesthetic convergence.

LOCAL MOVE:
The paper moves beyond “users like this style” and proposes that platform infrastructure amplifies it.

SOURCE TERMS:
“rewards”
“ranks”
“displays”
“favor”
“de facto style”
“network effects”

WHAT BECAME STRANGE:
This is more mechanically powerful than the surrounding discussion of taste, but the supplied synthesis does not show the receipt for the mechanism.

QUESTION:
Does Midjourney's circulation architecture actually cause aesthetic convergence, or are ranking and style simply correlated through user preference?

DEEPER QUESTION:
What portion of an aesthetic movement can be manufactured by visibility allocation?

MECHANISM:
candidate outputs
→ platform ranking/display
→ unequal visibility
→ imitation / preference reinforcement
→ output concentration

FORMAL SHIFT:
<generated population>
→ <visibility-ranked subset>
→ [IMITATION / SELECTION]
→ <platform aesthetic>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[UNVERIFIED]

RANKING_STYLE_FEEDBACK:
style frequency_t
→ visibility_t
→ imitation_t+1
→ style frequency_t+1

TENSION:
Elsewhere the paper quotes Manovich attributing apparent AI style primarily to users. A ranking mechanism would mean “the users” are themselves being conditioned by infrastructure.

MISSING:
Direct evidence about ranking rules, display mechanisms, user copying behavior, and longitudinal changes in style frequency.

BOUNDARY:
The supplied source asserts the mechanism but does not demonstrate it in the visible text.

CITATION TRAIL:
Midjourney interface histories; ranking documentation; public image feeds; prompt corpora; recommender-system studies; archived versions of community galleries.

TEST:
Reconstruct historical platform interfaces and correlate changes in visibility mechanisms with changes in prompt vocabulary and visual-style concentration.

PLATFORM:
[[Platform Aesthetics]]

LINKS:
[[Counterfeit Consensus]]
[[Visibility Allocation]]
[[Default Images]]

BIBTEX:
@misc{AIArtCulturalSystem,
  title = {AI Art as a Cultural System},
  note = {User-provided synthesis, section A07}
}
''')

add(r'''
ZETTEL

ID:
Z-AIACS-019

TITLE:
The “battle of metaphors” may be a battle over who is allowed to act.

SOURCE:
AI Art as a Cultural System — A04 and A08 — pp. 3, 9.

PASSAGE:
[PARAPHRASE]
AI is variously framed as tool, collaborator, or creative agent; the paper treats these as cultural narratives shaping debates around AI art.

RESEARCH OBJECT:
Metaphors may distribute agency and responsibility before any explicit argument about them begins.

LOCAL MOVE:
The paper treats metaphor primarily as discourse available for cultural analysis.

SOURCE TERMS:
“battle of metaphors”
“tool”
“collaborator”
“creative agent”
“mimicry”
“innovation”

WHAT BECAME STRANGE:
Calling a system a “tool” or “collaborator” may not simply describe the same process differently. Each metaphor may import a different social grammar of credit, obedience, responsibility, ownership, and expectation.

QUESTION:
What actions become sensible under “tool” that become strange under “collaborator,” and vice versa?

DEEPER QUESTION:
Do metaphors merely explain generative systems, or do they govern how people are permitted to relate to them?

MECHANISM:
metaphor
→ actor model
→ expected capacities
→ attribution of agency
→ norms of credit/responsibility
→ practice

FORMAL SHIFT:
<technical system>
→ <metaphoric role>
→ [ASSIGN EXPECTATIONS]
→ <socially available actions>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

TOOL:
human_intent → instrument → output

COLLABORATOR:
human ↔ artificial partner → negotiated output

AGENT:
artificial actor → action → consequences

Each graph contains different responsibility edges.

TENSION:
The source analyzes metaphor as cultural framing but does not ask whether the framing itself changes practice.

MISSING:
Evidence linking metaphor adoption to concrete differences in prompting, attribution, policy preferences, or creative behavior.

BOUNDARY:
The causal effect of metaphor is an open question, not established by the source.

CITATION TRAIL:
The AI & Society “battle of metaphors” work cited by the paper; conceptual metaphor theory; HCI research on framing and anthropomorphism.

TEST:
Randomly frame the same generative system as tool, collaborator, or agent, then measure changes in delegation, credit, blame, disclosure, and willingness to accept outputs.

PLATFORM:
[[Cultural Models of AI]]

LINKS:
[[Metaphors Govern Action]]
[[Agency Attribution]]
[[Interface Ontology]]

BIBTEX:
@misc{AIArtCulturalSystem,
  title = {AI Art as a Cultural System},
  note = {User-provided synthesis, sections A04 and A08}
}
''')

add(r'''
ZETTEL

ID:
Z-AIACS-020

TITLE:
The real object may be the path by which an image became possible.

SOURCE:
AI Art as a Cultural System — A08 — pp. 9–10.

PASSAGE:
[PARAPHRASE]
The paper ends by locating AI art's meaning across interface design, community rules, dataset bias, art-historical references, artist intention, infrastructure, interpretation, and cultural narrative.

RESEARCH OBJECT:
The “setting” surrounding an AI image is partly a causal production chain, not merely interpretive context.

LOCAL MOVE:
The paper expands context until the artwork is distributed across technical and social relations.

SOURCE TERMS:
“technical infrastructure”
“human interpretation”
“cultural narrative”
“user interface”
“rules”
“dataset”
“training”
“setting”

WHAT BECAME STRANGE:
Once enough of the surrounding system is causally necessary to explain the artifact, “context” stops looking like something outside the artwork.

QUESTION:
At what point does an artwork's context become part of the thing we must preserve in order to understand the artwork at all?

DEEPER QUESTION:
Is an AI image an object, or is it the visible residue of a path through a cultural-technical system?

MECHANISM:
dataset
→ model
→ platform configuration
→ prompt practice
→ generation
→ selection
→ circulation
→ interpretation

FORMAL SHIFT:
<visible image>
→ <production provenance graph>
→ [TRACE]
→ <cultural-technical event>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

ARTWORK_EVENT = (
  artifact,
  production_path,
  platform_state,
  prompt_history,
  selection_history,
  circulation_context
)

TENSION:
The paper repeatedly asks how to contextualize the artwork, but its own analysis suggests that context may be constitutive rather than supplementary.

MISSING:
A principled boundary around which causal predecessors and subsequent uses belong to the work's identity.

BOUNDARY:
The source supports distributed meaning and production; it does not claim that the complete provenance graph is the artwork.

CITATION TRAIL:
Geertz on the “tenor of setting”; provenance studies; media archaeology; software studies; process ontology; archival practices for generative work.

TEST:
Attempt to archive one AI artwork in progressively richer forms:
image only;
image + prompt;
image + prompt history;
full production ledger.
Ask at which stage another researcher can actually reconstruct the aesthetic decisions that matter.

PLATFORM:
[[AI Art as a Cultural System]]

LINKS:
[[Artwork as Path]]
[[Provenance Graph]]
[[The House That Words Built]]

BIBTEX:
@misc{AIArtCulturalSystem,
  title = {AI Art as a Cultural System},
  note = {User-provided synthesis, section A08}
}
''')
add(r'''
ZETTEL

ID:
Z-RF-20260817-001

TITLE:
A default image can be a semantic fallback rather than an interface default.

SOURCE:
Hannu Simonen, Atte Kiviniemi, Hannah Johnston, Helena Barranha, Jonas Oppenlaender — “An Exploration of Default Images in Text-to-Image Generation” — arXiv:2505.09166, v6 revised 25 January 2026.

PASSAGE:
[PARAPHRASE]
Text-to-image systems are designed to return an image even when a prompt contains unknown terms. Simonen et al. call one resulting failure mode “default images”: visually similar images appearing across otherwise unrelated prompts. Their expanded study analyzes more than 750,000 Midjourney images.

RESEARCH OBJECT:
“Default” splits into at least two different mechanisms: a setting selected before interaction and a recurrent output produced when textual conditioning provides insufficient discriminating information.

LOCAL MOVE:
The source operationalizes a phenomenon that [[Z-AIACS-004]] treated more broadly as a hidden prior. It shows that recognizable defaults can be detected in outputs without first locating an explicit UI setting.

SOURCE TERMS:
“default images”
“unknown terms”
“unrelated prompts”
“text-to-image generation”
“user satisfaction”

WHAT BECAME STRANGE:
A model does not need a blank prompt to expose its defaults. A sufficiently unrecognized or weakly discriminating prompt can act like a probe that reveals what the system does when language stops steering it.

QUESTION:
What exactly is being exposed by a default image: training-data frequency, model architecture, alignment, aesthetic tuning, prompt preprocessing, or some interaction among them?

DEEPER QUESTION:
Could deliberately bad prompts be a better instrument for studying a generative model than carefully optimized prompts?

MECHANISM:
poorly discriminating / unknown textual input
→ insufficient prompt-specific guidance
→ generation still must proceed
→ recurrent visual attractor
→ similar images across unrelated prompts

FORMAL SHIFT:
<weakly recognized prompt>
→ <conditioning signal>
→ [GENERATE DESPITE LOW SEMANTIC SPECIFICITY]
→ <default-like output cluster>

SOURCE FORMALISM:
The study searches for consistent visual similarity across outputs associated with unrelated prompts and expands the investigation computationally to more than 750,000 Midjourney images.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

DEFAULT_STRENGTH(p, m)
≈ similarity(
    G_m(p),
    outputs generated from semantically unrelated prompts
  )

The key comparison is not blank prompt versus filled prompt.
It is semantic difference in input versus visual difference in output.

TENSION:
[[Z-AIACS-004]] treated defaults primarily as pre-prompt platform configuration. Simonen et al. reveal a different class of default that emerges through the model’s response to weak or unknown conditioning. Both may exist, but they should not share one causal label.

MISSING:
A decomposition of default images across model weights, model versions, prompt preprocessing, system-level instructions, sampler configuration, and interface behavior.

BOUNDARY:
The study establishes recurrent default images in Midjourney. It does not establish which internal component is causally responsible for each default.

CITATION TRAIL:
[[Z-AIACS-004]]
→ Simonen et al., “An Exploration of Default Images in Text-to-Image Generation”
→ default as observable fallback behavior rather than merely preset configuration
→ locate the layer that produces the fallback

TEST:
Construct semantically unrelated nonsense, rare-word, vague, and ordinary prompts. Run the identical prompt set through multiple model versions and, where possible, multiple interfaces to the same underlying model. If default clusters follow the model version rather than the interface, the causal locus moves downward in the stack.

PLATFORM:
[[Default Images]]

LINKS:
[[Z-AIACS-004]]
[[Model Priors]]
[[Semantic Failure]]
[[Generative Attractors]]

BIBTEX:
@misc{SimonenEtAl2025DefaultImages,
  author = {Hannu Simonen and Atte Kiviniemi and Hannah Johnston and Helena Barranha and Jonas Oppenlaender},
  title = {An Exploration of Default Images in Text-to-Image Generation},
  year = {2025},
  eprint = {2505.09166},
  archivePrefix = {arXiv},
  primaryClass = {cs.HC},
  doi = {10.48550/arXiv.2505.09166}
}
''')

add(r'''
ZETTEL

ID:
Z-RF-20260817-002

TITLE:
The user’s prompt may not be the prompt the model receives.

SOURCE:
Felipe Rivas San Martín — Un Archivo Inexistente — Écfrasis, 2024 — “Notas sobre un archivo inexistente,” especially pp. 46–50.

PASSAGE:
[PARAPHRASE]
Rivas notes that in many publicly accessible models, language layers can intervene between the user’s instruction and the model, recoding the original instruction as hidden prompts generated by the online system.

RESEARCH OBJECT:
Prompting may contain an unobserved translation layer between authored instruction and executed conditioning.

LOCAL MOVE:
The source turns [[Z-AIACS-004]]’s metaphorical “hidden coauthor” into a concrete interface problem: the visible prompt may be transformed before generation.

SOURCE TERMS:
“prompts ocultos”
“recodifican”
“instrucciones del usuario”
“modelo”
“sistemas en línea”

WHAT BECAME STRANGE:
Prompt studies frequently archive the text a user typed and call it the input. If another text is generated downstream, the archive may have preserved the wrong computational object.

QUESTION:
What counts as “the prompt” when visible user text is only the first representation in a hidden chain of linguistic transformations?

DEEPER QUESTION:
Can prompt authorship be studied without access to the transformations between interface text and model conditioning?

MECHANISM:
user instruction
→ platform language layer
→ recoded / augmented instruction
→ model conditioning
→ generation

FORMAL SHIFT:
<USER TEXT>
→ <INTERMEDIARY LANGUAGE REPRESENTATION>
→ [RECODE / AUGMENT]
→ <EXECUTED CONDITIONING>

SOURCE FORMALISM:
Rivas distinguishes the user’s instruction from intervening language layers that may recode it before it reaches the model. He does not provide implementation syntax for those layers.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

P_visible ≠ necessarily P_executed

P_visible
→ T_platform(P_visible)
→ P_executed
→ G(P_executed)

T_platform is epistemically important even when unavailable to the user.

TENSION:
Prompt scholarship often interprets generated outputs as responses to visible textual prompts. Hidden recoding means apparent prompt/output relations can actually be platform-transformation/output relations.

MISSING:
Versioned records of system prompts, prompt rewriting, automatic expansion, moderation transformations, translation layers, or other preprocessing for actual image-generation services.

BOUNDARY:
Rivas states that such hidden prompt layers occur in many accessible systems. The passage does not establish that every model or the particular Stable Diffusion workflow used in the artwork contains the same hidden transformation.

CITATION TRAIL:
[[Z-AIACS-004]]
→ Rivas San Martín, Un Archivo Inexistente
→ hidden prompt recoding
→ distinguish authored prompt from executed prompt
→ inspect platform-specific transformation chains

TEST:
For any platform exposing both a consumer interface and lower-level API, submit matched visible prompts through each route. Compare outputs and inspect any available request logs. Search platform documentation and source code for prompt expansion, rewriting, safety prefixes, templates, translation, or conditioning augmentation.

PLATFORM:
[[Prompt Provenance]]

LINKS:
[[Z-AIACS-004]]
[[Hidden Prompts]]
[[Prompt Provenance]]
[[The Prompt Is Not the Program]]

BIBTEX:
@book{RivasSanMartin2024Archivo,
  author = {Felipe Rivas San Martín},
  title = {Un Archivo Inexistente},
  publisher = {Écfrasis, ediciones},
  address = {Santiago},
  year = {2024},
  isbn = {978-956-09200-7-2}
}
''')

add(r'''
ZETTEL

ID:
Z-RF-20260817-003

TITLE:
Interfaces can suppress exploration before ranking ever begins.

SOURCE:
Maddalena Torricelli, Mauro Martino, Andrea Baronchelli, Luca Maria Aiello — “The role of interface design on prompt-mediated creativity in Generative AI” — arXiv:2312.00233, 2023; accepted WebSci 2024.

PASSAGE:
[PARAPHRASE]
Across more than 145,000 prompts from Stable Diffusion and Pick-a-Pic, the authors find that interface features that divert attention away from prompt editing and offer shortcuts for generating variants are associated with substantially less exploration of novel concepts and less detail in submitted prompts.

RESEARCH OBJECT:
A platform can change the distribution of generated ideas by changing the cheapest next action.

LOCAL MOVE:
The evidence follows [[Z-AIACS-018]]’s search for platform mechanisms but finds a better-supported mechanism than the parent’s unverified Midjourney-ranking claim.

SOURCE TERMS:
“interface design”
“prompt-mediated creativity”
“exploration”
“exploitation”
“image variants”
“novel concepts”

WHAT BECAME STRANGE:
Aesthetic convergence need not begin with an algorithm preferentially ranking certain pictures. It can begin earlier, when an interface makes variation cheaper than re-description.

QUESTION:
How much apparent model-level aesthetic repetition is actually path dependence introduced by the interface’s next-action affordances?

DEEPER QUESTION:
Does a generative interface quietly define what kind of creativity is economically convenient?

MECHANISM:
current generation
→ interface presents cheap variant action
→ user modifies image rather than concept
→ reduced prompt revision
→ reduced topical movement
→ locally concentrated trajectory

FORMAL SHIFT:
<current creative state>
→ <available interface operations>
→ [SELECT LOW-COST NEXT ACTION]
→ <constrained exploration trajectory>

SOURCE FORMALISM:
The study compares longitudinal prompt behavior across two platforms and measures exploration of new concepts and prompt detail in relation to differing interface functionality.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

CREATIVE_TRANSITION =
f(current_output,
  available_actions,
  action_costs,
  user_intention)

Interface design changes the transition probabilities even if the generator is held conceptually separate.

TENSION:
[[Z-AIACS-018]] proposed:
ranking → visibility → imitation → aesthetic concentration.

Torricelli et al. support a different path:
interface action → reduced prompt exploration → trajectory concentration.

The first mechanism remains possible but should not borrow evidence from the second.

MISSING:
A study holding the generative model constant while experimentally changing only interface operations.

BOUNDARY:
The observational comparison associates interface differences with prompt behavior. It does not by itself prove that interface design alone causes the entire between-platform difference.

CITATION TRAIL:
[[Z-AIACS-018]]
→ Torricelli et al.
→ interface-mediated exploration
→ separate pre-generation path dependence from post-generation ranking effects

TEST:
Build two interfaces over the same model: one privileging “make variants,” another privileging “rewrite description.” Randomly assign users and compare semantic distance between successive prompts, visual diversity, concept count, and final-output convergence.

PLATFORM:
[[Platform Aesthetics]]

LINKS:
[[Z-AIACS-018]]
[[Interface Governance]]
[[Creative Trajectories]]
[[Affordance-Induced Convergence]]

BIBTEX:
@misc{TorricelliEtAl2023Interface,
  author = {Maddalena Torricelli and Mauro Martino and Andrea Baronchelli and Luca Maria Aiello},
  title = {The role of interface design on prompt-mediated creativity in Generative AI},
  year = {2023},
  eprint = {2312.00233},
  archivePrefix = {arXiv},
  primaryClass = {cs.CY},
  doi = {10.48550/arXiv.2312.00233}
}
''')

add(r'''
ZETTEL

ID:
Z-RF-20260817-004

TITLE:
Prompt vocabulary is operational because modifiers are learned as probes.

SOURCE:
Jonas Oppenlaender — “A Taxonomy of Prompt Modifiers for Text-To-Image Generation” — arXiv:2204.13988v3, 2023; related journal DOI 10.1080/0144929X.2023.2286532.

PASSAGE:
[PARAPHRASE]
Oppenlaender’s three-month ethnographic and autoethnographic study identifies six classes of prompt modifier. Practitioners repeatedly run a prompt, inspect its outcome, and modify the prompt; the paper explicitly describes prompts as probes into the model’s latent space.

RESEARCH OBJECT:
Prompt vocabulary is not simply a lexicon of descriptions. It is a repertoire of experimentally acquired interventions.

LOCAL MOVE:
The source sharpens [[Z-AIACS-005]] by replacing the loose idea of a “prompt dialect” with observed classes of modifier and a documented practice for discovering their effects.

SOURCE TERMS:
“prompt modifiers”
“prompt engineering”
“iterative”
“experimental”
“probes”
“latent space”

WHAT BECAME STRANGE:
A word can enter prompt culture because of what repeated generations show that it does, not because its ordinary-language definition predicts its effect.

QUESTION:
When practitioners circulate a modifier, what exactly is being transmitted: semantic meaning, a causal hypothesis, an empirical recipe, or a remembered correlation with desirable outputs?

DEEPER QUESTION:
Could prompt vernacular be modeled less like a natural-language dialect and more like an evolving library of experimentally discovered operators?

MECHANISM:
candidate phrase
→ generation
→ observed effect
→ repeated experiment
→ community circulation
→ conventional modifier role

FORMAL SHIFT:
<natural-language phrase>
→ <community prompt modifier>
→ [APPLY AS PROBE]
→ <observed generative displacement>

SOURCE FORMALISM:
Oppenlaender identifies six categories of prompt modifier and documents an iterative practice in which practitioners run prompts, observe outcomes, and adapt subsequent prompts.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

A prompt expression e has at least:

SEMANTIC_ROLE(e)
OPERATIONAL_ROLE(e, model, configuration)
COMMUNITY_ROLE(e, practice)

These roles need not coincide.

TENSION:
Calling prompt practice a “language” suggests relatively stable meanings. The source instead describes an experimental craft whose terms acquire practical force through model-contingent observation.

MISSING:
Longitudinal evidence showing how individual modifiers change operational role when models, interfaces, or aesthetic norms change.

BOUNDARY:
The taxonomy documents practice in an early text-to-image community centered substantially on VQGAN–CLIP-era systems. It does not establish universal modifier categories across later generators.

CITATION TRAIL:
[[Z-AIACS-005]]
→ Oppenlaender, “A Taxonomy of Prompt Modifiers”
→ modifier classes + prompts as probes
→ operational vocabulary rather than merely stylistic vocabulary
→ follow modifiers across model generations

TEST:
Select historically common prompt modifiers from archived guides. Execute them unchanged on every recoverable model version. Compare their ordinary-language meaning, measured image effect, and community-described function at each date.

PLATFORM:
[[Prompt Vernacular]]

LINKS:
[[Z-AIACS-005]]
[[Operational Semantics]]
[[Prompt Modifiers]]
[[Prompts as Probes]]

BIBTEX:
@misc{Oppenlaender2022PromptModifiers,
  author = {Jonas Oppenlaender},
  title = {A Taxonomy of Prompt Modifiers for Text-To-Image Generation},
  year = {2022},
  eprint = {2204.13988},
  archivePrefix = {arXiv},
  primaryClass = {cs.MM},
  doi = {10.48550/arXiv.2204.13988}
}
''')

add(r'''
ZETTEL

ID:
Z-RF-20260817-005

TITLE:
Trial and error is not noise around prompting; it is part of the interaction form.

SOURCE:
Vivian Liu, Lydia B. Chilton — “Design Guidelines for Prompt Engineering Text-to-Image Generative Models” — arXiv:2109.06977, 2021; revised 2023.

PASSAGE:
[PARAPHRASE]
Liu and Chilton characterize open-ended text interaction as double-edged: users can enter almost anything, but poor results force brute-force trial and error. Their evaluation covers 5,493 generations across five experiments, 51 subjects, and 51 styles.

RESEARCH OBJECT:
The apparent freedom of an unconstrained text box transfers specification work from interface structure into repeated empirical correction.

LOCAL MOVE:
The source gives [[Z-AIACS-016]] an earlier empirical basis: correction is not merely how experts polish prompts but a recurring consequence of open-ended text as an interaction modality.

SOURCE TERMS:
“open-ended”
“text as interaction”
“brute-force trial and error”
“subject”
“style”
“success and failure modes”

WHAT BECAME STRANGE:
The interface appears maximally expressive because it accepts arbitrary language, yet this same absence of explicit structure can make users discover the system’s constraints by failure.

QUESTION:
Does natural-language freedom reduce formalization, or merely defer formalization until after generation?

DEEPER QUESTION:
Could the repeated correction sequence be the interface’s missing specification language appearing temporally rather than syntactically?

MECHANISM:
underspecified / mismatched description
→ generation
→ visible failure
→ inferred missing constraint
→ prompt revision
→ regeneration

FORMAL SHIFT:
<open-ended intention>
→ <provisional text>
→ [GENERATE AND INSPECT]
→ <newly discovered constraint>

SOURCE FORMALISM:
The paper experimentally varies prompt keywords and model hyperparameters, examining coherent outputs and success/failure modes across thousands of generations.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

S_0 = initial specification

G(S_0) → failure evidence E_0

S_1 = S_0 ∪ constraint(E_0)

The effective specification is accumulated over executions rather than completed before execution.

TENSION:
Prompt interfaces are often described as lowering the need for formal specification. The documented trial-and-error burden suggests that specification may still occur, but after execution and through perceptual diagnosis.

MISSING:
Process data showing exactly which constraints users infer from each failed generation.

BOUNDARY:
Liu and Chilton document trial-and-error interaction and design guidelines. They do not name the process “deferred formalization.”

CITATION TRAIL:
[[Z-AIACS-016]]
→ Liu & Chilton
→ brute-force correction as an empirical feature of open-ended text interaction
→ recover failure-to-constraint transitions
→ compare with conventional programming/debugging

TEST:
Record complete screen, prompt, parameter, and output histories for a generation task. After every revision, ask the user what newly discovered constraint caused the edit. Reconstruct the specification in the order it became explicit.

PLATFORM:
[[Deferred Formalization]]

LINKS:
[[Z-AIACS-016]]
[[Failure Becomes Specification]]
[[Prompt History]]
[[Describe Generate Inspect Correct]]

BIBTEX:
@misc{LiuChilton2021PromptEngineering,
  author = {Vivian Liu and Lydia B. Chilton},
  title = {Design Guidelines for Prompt Engineering Text-to-Image Generative Models},
  year = {2021},
  eprint = {2109.06977},
  archivePrefix = {arXiv},
  primaryClass = {cs.HC},
  doi = {10.48550/arXiv.2109.06977}
}
''')

add(r'''
ZETTEL

ID:
Z-RF-20260817-006

TITLE:
The minority prompt corrects downstream while the bias remains upstream.

SOURCE:
Felipe Rivas San Martín — Un Archivo Inexistente — Écfrasis, 2024 — “Un prompt minoritario,” pp. 46–50.

PASSAGE:
[PARAPHRASE]
Rivas says prompts are his only direct point of intervention in the Stable Diffusion workflow he describes, while the model’s algorithmic configuration and training database arrive already given and are not neutral. He proposes the “prompt minoritario” specifically to counter biases manifested in those prior conditions.

RESEARCH OBJECT:
A minority prompt is a downstream compensatory operation against upstream conditions the artist does not control.

LOCAL MOVE:
This qualifies [[Z-AIACS-006]]. The source does not simply relocate governance to the user; it makes visible an asymmetry between the layer where bias originates and the layer where the artist can intervene.

SOURCE TERMS:
“única incidencia”
“configuración algorítmica”
“base de entrenamiento”
“no son neutrales”
“prompt minoritario”
“contrarrestar”

WHAT BECAME STRANGE:
The person asked to repair representation may have access only to the least structural layer of the system.

QUESTION:
When a prompt compensates successfully for biased priors without altering them, has anything in the underlying representational system actually been corrected?

DEEPER QUESTION:
Should prompt-based bias correction be understood as agency, workaround, accessibility technique, invisible labor, or all four?

MECHANISM:
upstream training/configuration bias
→ skewed baseline generation
→ user observes mismatch
→ minority prompt adds counter-conditioning
→ locally altered output
→ upstream distribution remains unchanged

FORMAL SHIFT:
<UPSTREAM BIAS>
→ <DEFAULT GENERATIVE TENDENCY>
→ [DOWNSTREAM COUNTER-PROMPT]
→ <LOCAL REPRESENTATIONAL REPAIR>

SOURCE FORMALISM:
Rivas gives concrete examples in which requests for two men yielded classed or racialized defaults, then describes modifying prompt instructions to counter the training-data tendencies.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

STRUCTURAL_REPAIR changes M

COMPENSATORY_REPAIR changes conditioning c

G(M, c)
→ mismatch

G(M, c + counter_condition)
→ desired local result

while M remains fixed.

TENSION:
[[Z-AIACS-006]] asked whether representational governance had been relocated to users. Rivas’s account suggests something harsher: responsibility for local correction may be displaced to the user while authority over the causal substrate remains elsewhere.

MISSING:
Evidence comparing the amount of corrective prompting required across represented groups and determining whether repeated user corrections ever feed back into model or platform changes.

BOUNDARY:
Rivas documents his own artistic practice and theorizes “prompt minoritario.” The source does not establish that every successful corrective prompt leaves every relevant system layer unchanged.

CITATION TRAIL:
[[Z-AIACS-006]]
→ Rivas San Martín, “Un prompt minoritario”
→ only point of artist intervention versus predetermined model/database
→ distinguish compensatory from structural repair
→ measure corrective labor

TEST:
Create matched requests varying one represented social category at a time. Give users a fixed success criterion and measure iterations, added tokens, negative constraints, and time required to reach it. Repeat after model updates to see whether corrective labor decreases or merely changes vocabulary.

PLATFORM:
[[Minority Prompt]]

LINKS:
[[Z-AIACS-006]]
[[Corrective Description]]
[[Compensatory Labor]]
[[Representational Governance]]

BIBTEX:
@book{RivasSanMartin2024Archivo,
  author = {Felipe Rivas San Martín},
  title = {Un Archivo Inexistente},
  publisher = {Écfrasis, ediciones},
  address = {Santiago},
  year = {2024},
  isbn = {978-956-09200-7-2}
}
''')

add(r'''
ZETTEL

ID:
Z-RF-20260817-007

TITLE:
In Rivas’s archive, error is an ethical boundary, not merely an aesthetic trace.

SOURCE:
Felipe Rivas San Martín — Un Archivo Inexistente — Écfrasis, 2024 — “Cuerpos extraños, el error como evidencia,” pp. 53–57.

PASSAGE:
[PARAPHRASE]
Rivas explicitly treats malformed bodies as an ethical-political limit: their visible errors prevent the generated quasi-photographs from pretending to replace a violent past that prevented those imagined records from existing. The error marks “this has not been.”

RESEARCH OBJECT:
Generation failure is deliberately recruited to prevent speculative memory from crossing into counterfeit evidence.

LOCAL MOVE:
The primary source strengthens [[Z-AIACS-007]]. The glitch-as-provenance reading was not merely an external interpretation; Rivas makes the ethical function of error explicit.

SOURCE TERMS:
“error como evidencia”
“límite ético-político”
“esto no ha sido”
“cuasifotografías”
“deformaciones corporales”

WHAT BECAME STRANGE:
Model improvement can remove a defect that is performing ethical work for the artwork.

QUESTION:
What must replace accidental model error when technical development erases the visible boundary between counter-history and historical evidence?

DEEPER QUESTION:
Should some generative artworks deliberately manufacture non-realism once the generator no longer supplies it accidentally?

MECHANISM:
synthetic historical scene
→ generation defect remains visible
→ viewer detects impossibility
→ documentary claim is interrupted
→ speculative status remains legible

FORMAL SHIFT:
<SYNTHETIC MEMORY>
→ <VISIBLE IMPOSSIBILITY>
→ [BLOCK DOCUMENTARY READING]
→ <SPECULATIVE COUNTER-ARCHIVE>

SOURCE FORMALISM:
The source establishes a repeated interpretive operation: malformed hands, limbs, faces, and bodies expose the synthetic condition of the generated images.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

If:

REALISM ↑
ACCIDENTAL_DISCLOSURE ↓

then maintaining the work’s ethical boundary requires:

DELIBERATE_DISCLOSURE ↑

unless another provenance convention takes over.

TENSION:
Technical evaluation treats anatomical error as something to eliminate. Rivas’s artwork depends on error as a safeguard against historical substitution.

MISSING:
A provenance technique that preserves the force of “this has not been” without depending on model incompetence.

BOUNDARY:
The artwork demonstrates one productive use of error. It does not license the claim that technical defects are inherently ethical or politically emancipatory.

CITATION TRAIL:
[[Z-AIACS-007]]
→ Rivas San Martín, “Cuerpos extraños, el error como evidencia”
→ error as explicit ethical-political boundary
→ model improvement threatens disclosure
→ search synthetic-documentary practices for deliberate non-indexical marking

TEST:
Generate equivalent fictional archival scenes using increasingly photorealistic model generations. Remove labels. Measure when viewers shift from “speculative construction” to “possibly authentic photograph.” Then test deliberate provenance devices that restore the original distinction.

PLATFORM:
[[Synthetic Archives]]

LINKS:
[[Z-AIACS-007]]
[[Error as Evidence]]
[[Synthetic Fossils]]
[[Provenance Aesthetics]]

BIBTEX:
@book{RivasSanMartin2024Archivo,
  author = {Felipe Rivas San Martín},
  title = {Un Archivo Inexistente},
  publisher = {Écfrasis, ediciones},
  address = {Santiago},
  year = {2024},
  isbn = {978-956-09200-7-2}
}
''')

add(r'''
ZETTEL

ID:
Z-RF-20260817-008

TITLE:
The “AI look” may be a social average rendered through a model.

SOURCE:
Hito Steyerl — “Mean Images” — New Left Review 140/141 — March–June 2023 — pp. 82–97.

PASSAGE:
[QUOTE]
“Mean images are far from random hallucinations. They are predictable products of data populism.”

RESEARCH OBJECT:
Steyerl refuses the clean choice between “the machine made the style” and “users made the style.” The model renders correlated averages extracted from socially produced data.

LOCAL MOVE:
The source complicates [[Z-AIACS-003]] by adding a third causal object between machine architecture and current user taste: historical social distributions sedimented into training data.

SOURCE TERMS:
“mean images”
“social filter”
“correlated averages”
“data populism”
“latent social patterns”
“social signal”

WHAT BECAME STRANGE:
An aesthetic can look intrinsically machinic while functioning as a compressed portrait of already-existing social regularities.

QUESTION:
How can we distinguish a model’s architectural fingerprint from a training corpus’s social average when both are visible only through generated output?

DEEPER QUESTION:
Is the “machine aesthetic” sometimes society encountering its own statistical self-portrait and misrecognizing it as alien intelligence?

MECHANISM:
social production of images
→ large-scale data capture
→ statistical training representation
→ model rendering
→ correlated averages
→ apparent machine aesthetic

FORMAL SHIFT:
<SOCIAL IMAGE DISTRIBUTION>
→ <STATISTICAL REPRESENTATION>
→ [GENERATE]
→ <MEAN IMAGE>

SOURCE FORMALISM:
Steyerl characterizes generative images as statistical renderings indexed to probability and discusses the “mean image” as a rendition of correlated averages produced through a social filter.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

PERCEIVED_AI_STYLE
=
MODEL_TRANSFORM(
  HISTORICAL_SOCIAL_DISTRIBUTION,
  current conditioning
)

Therefore:

MACHINE_EFFECT versus USER_EFFECT

is incomplete without:

CORPUS_SOCIAL_EFFECT.

TENSION:
[[Z-AIACS-003]] placed model fingerprints against user-population effects. Steyerl suggests those categories are entangled before the present user arrives because the model has already internalized a historically produced population of images.

MISSING:
Methods for causally separating architecture, training distribution, fine-tuning, prompt population, and interface circulation.

BOUNDARY:
“Mean image” is a critical-theoretical description of statistical cultural production, not a quantitative estimator of how much each causal layer contributes.

CITATION TRAIL:
[[Z-AIACS-003]]
→ Steyerl, “Mean Images”
→ correlated averages as social signal
→ split machine/user binary into architecture/corpus/current-practice
→ seek controlled cross-model and cross-dataset comparisons

TEST:
Hold architecture and prompts constant while changing training distributions where reproducible models permit it. Then hold dataset and prompts constant while changing architecture. Compare which visual regularities survive each intervention.

PLATFORM:
[[Population Aesthetics]]

LINKS:
[[Z-AIACS-003]]
[[Mean Images]]
[[Social Filter]]
[[Training Data as Culture]]

BIBTEX:
@article{Steyerl2023MeanImages,
  author = {Hito Steyerl},
  title = {Mean Images},
  journal = {New Left Review},
  number = {140/141},
  year = {2023},
  pages = {82--97}
}
''')

add(r'''
ZETTEL

ID:
Z-RF-20260817-009

TITLE:
Geertz shifts the unit of analysis from the artwork to the equipment for grasping it.

SOURCE:
Clifford Geertz — “Art as a Cultural System” — MLN 91(6) — December 1976 — pp. 1473–1499.

PASSAGE:
[QUOTE]
“Art and the equipment to grasp it are made in the same shop.”

RESEARCH OBJECT:
Aesthetic capacity itself is culturally produced alongside the objects it makes intelligible.

LOCAL MOVE:
This changes [[Z-AIACS-002]]’s scale question. The problem may not be finding the smallest community called an “AI-art culture,” but locating the practices that jointly produce artifacts and the competence required to recognize, judge, and use them.

SOURCE TERMS:
“equipment to grasp it”
“experience”
“aesthetic”
“cultural system”
“meaning”
“setting”

WHAT BECAME STRANGE:
The relevant boundary of an art world may lie wherever its perceptual and interpretive equipment is being reproduced—not wherever its artworks happen to circulate.

QUESTION:
What is the “equipment to grasp” AI art, and where is that equipment learned?

DEEPER QUESTION:
Could prompt guides, comparison grids, Discord critique, model-version lore, parameter vocabularies, failure recognition, and aesthetic memes be part of the artwork’s cultural apparatus rather than merely commentary around it?

MECHANISM:
repeated participation in situated practices
→ learned distinctions and sensitivities
→ competent perception/judgment
→ recognition of aesthetic significance
→ reproduction of practice

FORMAL SHIFT:
<COMMUNITY PRACTICE>
→ <PERCEPTUAL / INTERPRETIVE EQUIPMENT>
→ [APPLY IN ENCOUNTER]
→ <AESTHETIC DIFFERENCE BECOMES LEGIBLE>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

A cultural unit may be detected where:

ARTIFACT_PRODUCTION
and
COMPETENCE_PRODUCTION

recurrently reproduce one another.

TENSION:
[[Z-AIACS-002]] asks for the smallest stable “setting.” Geertz’s formulation suggests stability and size may be the wrong criteria. A dispersed online practice could still be one analytic unit if it reproduces shared equipment for seeing.

MISSING:
Ethnographic evidence identifying which learned distinctions actually separate competent insiders from casual users of generative-image systems.

BOUNDARY:
Geertz does not discuss generative AI or online prompt communities. Applying his “equipment to grasp” formulation to those settings is our extension.

CITATION TRAIL:
[[Z-AIACS-002]]
→ Geertz, “Art as a Cultural System”
→ art and aesthetic equipment co-produced
→ replace geographic/platform boundary with competence-production question
→ ethnographically trace how people learn to see AI images

TEST:
Recruit novices and experienced practitioners. Present identical generations and ask them to notice failures, infer likely prompting/model behavior, compare variants, and explain aesthetic judgments. Trace where the distinctions used by experts were learned.

PLATFORM:
[[AI Art as a Cultural System]]

LINKS:
[[Z-AIACS-002]]
[[Equipment to Grasp]]
[[Communities of Practice]]
[[Aesthetic Competence]]

BIBTEX:
@article{Geertz1976ArtCulturalSystem,
  author = {Clifford Geertz},
  title = {Art as a Cultural System},
  journal = {MLN},
  volume = {91},
  number = {6},
  year = {1976},
  pages = {1473--1499}
}
''')

add(r'''
ZETTEL

ID:
Z-RF-20260817-010

TITLE:
Autopoiesis requires self-production, not merely recursive adjustment.

SOURCE:
Humberto R. Maturana — “The Organization of the Living: A Theory of the Living Organization” — International Journal of Man-Machine Studies 7(3) — 1975 — pp. 313–332.

PASSAGE:
[PARAPHRASE]
Maturana characterizes an autopoietic system as a network of processes producing components whose interactions continuously and recursively generate and realize that same network as a concrete unity.

RESEARCH OBJECT:
The criterion missing from a generic feedback loop is organizational self-production.

LOCAL MOVE:
The source executes [[Z-AIACS-010]]’s test by recovering the machinery hidden by the loose equation feedback = recursion = autopoiesis.

SOURCE TERMS:
“autonomy”
“self-production”
“autopoiesis”
“network of processes”
“production of components”
“unity”

WHAT BECAME STRANGE:
A loop can recursively change values forever without producing the organization that makes the loop a unity.

QUESTION:
What components of a GAN training process are produced by the process itself and, in turn, regenerate the organization that produces them?

DEEPER QUESTION:
If the architecture, objective, training regime, execution environment, and system boundary are supplied from outside, in what precise sense could GAN training be called autopoietic?

MECHANISM:
AUTOPOIETIC:
network of production processes
→ produces components
→ component interactions
→ regenerate the production network
→ realize system as unity

ORDINARY ITERATIVE OPTIMIZATION:
externally specified architecture/objective
→ calculate loss
→ update parameters
→ repeat

FORMAL SHIFT:
<RECURSIVE UPDATE LOOP>
→ <TEST FOR COMPONENT SELF-PRODUCTION>
→ [TEST FOR REGENERATION OF ORGANIZATION]
→ <AUTOPOIESIS OR NOT>

SOURCE FORMALISM:
Maturana explicitly defines autopoietic organization through recursive production of components and realization of the network as a unity.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

RECURSION is necessary for many loops.

AUTOPOIESIS additionally asks whether:

PRODUCE(components)
→ components sustain PRODUCE
→ system organization is thereby continuously realized.

TENSION:
A GAN’s generator and discriminator recursively change parameters, but parameter updating alone does not establish that they produce the organization or boundary that constitutes the GAN as a system.

MISSING:
A component-by-component mapping from GAN training to the autopoietic production relations required by the biological theory.

BOUNDARY:
This source defines living-system autopoiesis. Whether that concept can legitimately be generalized to computational systems remains a separate question.

CITATION TRAIL:
[[Z-AIACS-010]]
→ Maturana, “The Organization of the Living”
→ autopoiesis as recursive component-production
→ compare against GAN architecture
→ follow Varela, Maturana & Uribe 1974 for the original characterization and model

TEST:
Write a table with each required autopoietic relation in one column and each GAN process in another. For every alleged equivalence, identify what the GAN itself produces and what must be supplied externally. Reject the analogy wherever no source-side operation can be mapped without metaphor.

PLATFORM:
[[Cybernetic AI Art]]

LINKS:
[[Z-AIACS-010]]
[[Autopoiesis]]
[[Self-Production]]
[[Feedback Is Not Autopoiesis]]

BIBTEX:
@article{Maturana1975LivingOrganization,
  author = {Humberto R. Maturana},
  title = {The Organization of the Living: A Theory of the Living Organization},
  journal = {International Journal of Man-Machine Studies},
  volume = {7},
  number = {3},
  year = {1975},
  pages = {313--332}
}
''')

add(r'''
ZETTEL

ID:
Z-RF-20260817-011

TITLE:
ELIZA’s apparent conversational agency can be decomposed into small symbolic operations.

SOURCE:
Joseph Weizenbaum — “ELIZA—A Computer Program for the Study of Natural Language Communication Between Man and Machine” — Communications of the ACM 9(1) — January 1966 — pp. 36–45 — DOI 10.1145/365153.365168.

PASSAGE:
[PARAPHRASE]
ELIZA scans input for keywords, uses those keywords to select decomposition rules, and generates responses through associated reassembly rules. The paper treats keyword identification, minimal context, transformation choice, and responses without keywords as explicit technical problems.

RESEARCH OBJECT:
Conversational plausibility can emerge from an inspectable chain of shallow operations without a corresponding unified conversational understanding.

LOCAL MOVE:
This pushes [[Z-AIACS-012]] beneath the psychological label “interpretive repair” into source machinery that can actually be manipulated.

SOURCE TERMS:
“keywords”
“decomposition rules”
“reassembly rules”
“minimal context”
“transformation”
“script”

WHAT BECAME STRANGE:
The spectator may infer one speaking agent from a sequence assembled by several independent rule-selection operations.

QUESTION:
Which minimal ELIZA mechanisms contribute most strongly to a user’s perception that there is one coherent interlocutor behind the responses?

DEEPER QUESTION:
How little computational continuity is required before human interpretation supplies the rest?

MECHANISM:
input sentence
→ keyword scan
→ keyword precedence
→ select decomposition rule
→ decompose input
→ choose reassembly rule
→ construct response
→ user interprets response as conversational continuation

FORMAL SHIFT:
<USER UTTERANCE>
→ <KEYWORD / RULE REPRESENTATION>
→ [DECOMPOSE + REASSEMBLE]
→ <APPARENT CONVERSATIONAL RESPONSE>

SOURCE FORMALISM:
A keyword indexes associated decomposition and reassembly rules. Decomposition patterns divide the input into components; reassembly rules reuse selected components to construct a reply. Keyword ranking limits which rule family is attempted.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

PERCEIVED_AGENT =
ELIZA_RULE_OUTPUT
+
HUMAN_CONTINUITY_INFERENCE

The research variable is not whether the program “understands.”
It is how changes to rule machinery alter the second term.

TENSION:
[[Z-AIACS-012]] treats machine incoherence as eliciting human repair. ELIZA shows that plausibility is not simply “nonsense versus sense”; it can be engineered locally through keyword choice, minimal-context decomposition, substitutions, and reassembly while global understanding remains absent.

MISSING:
Controlled evidence linking particular ELIZA mechanisms to measured changes in attributed understanding, personality, memory, or intentionality.

BOUNDARY:
Weizenbaum’s implementation demonstrates a symbolic mechanism for ELIZA. It does not prove that contemporary generative dialogue systems produce perceived agency through the same machinery.

CITATION TRAIL:
[[Z-AIACS-012]]
→ Weizenbaum 1966
→ keyword/decomposition/reassembly machinery
→ decompose apparent agency into executable operations
→ experimentally ablate operations and measure interpretation

TEST:
Run matched ELIZA variants with keyword ranking, pronoun transformation, memory behavior, decomposition specificity, or reassembly diversity independently removed. Ask users to rate coherence, understanding, personality, intentionality, and conversational continuity after each variant.

PLATFORM:
[[Meaning Repair]]

LINKS:
[[Z-AIACS-012]]
[[ELIZA]]
[[Agency Attribution]]
[[Interpretive Repair]]
[[Executable Plausibility]]

BIBTEX:
@article{Weizenbaum1966ELIZA,
  author = {Joseph Weizenbaum},
  title = {ELIZA---A Computer Program for the Study of Natural Language Communication Between Man and Machine},
  journal = {Communications of the ACM},
  volume = {9},
  number = {1},
  year = {1966},
  pages = {36--45},
  doi = {10.1145/365153.365168}
}
''')
add(r'''
ZETTEL

ID:
Z-RF-20260818-012

TITLE:
A prompt may address the archive of descriptions more than the pictured world.

SOURCE:
Jonas Oppenlaender — “A Taxonomy of Prompt Modifiers for Text-To-Image Generation” — 2022/2023 — §6.2.1 “Social aspects of prompt engineering.”

PASSAGE:
[PARAPHRASE]
Oppenlaender argues that because text-to-image systems were trained on image-text material scraped from the Web, practitioners must do more than describe the image they want. They may need to anticipate how other people would have described or reacted to such an image online.

RESEARCH OBJECT:
Prompting can require modeling a historical population of describers rather than directly describing a desired visual world.

LOCAL MOVE:
This changes [[Z-RF-20260817-009]]. The “equipment to grasp” AI art may include practical knowledge about how images were captioned, tagged, admired, classified, and circulated before the current user ever encountered the model.

SOURCE TERMS:
“imagine and predict”
“other people”
“described”
“reacted”
“images posted on the Web”
“prompt engineering”

WHAT BECAME STRANGE:
A successful prompt can be semantically indirect yet operationally accurate because it predicts the language surrounding images in the training ecology.

QUESTION:
Is prompt expertise partly an archaeology of other people’s past descriptions?

DEEPER QUESTION:
When users learn that “trending on ArtStation,” an artist name, a photographic term, or an aesthetic adjective produces a useful effect, are they learning visual language or reverse-engineering sedimented metadata culture?

MECHANISM:
historical image
→ social description / caption / tag / reaction
→ image-text training pair
→ learned statistical relation
→ current prompt anticipates historical wording
→ desired visual tendency becomes more likely

FORMAL SHIFT:
<DESIRED IMAGE>
→ <HYPOTHESIZED HISTORICAL DESCRIPTION>
→ [PROMPT WITH THAT DESCRIPTION]
→ <MODEL REACTIVATES ASSOCIATED VISUAL REGULARITIES>

SOURCE FORMALISM:
Oppenlaender describes CLIP-based systems as using shared vector representations for text and images and explicitly identifies practitioners’ need to imagine how other people described and reacted to images on the Web.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Prompting may contain an inverse problem:

desired_visual_state V
→ infer likely historical language L
→ submit L
→ model maps L toward V

The user is not only describing V.
The user is estimating L.

TENSION:
[[Z-RF-20260817-009]] follows Geertz toward culturally learned aesthetic competence. This source suggests a peculiar additional competence: learning not simply how one’s culture describes things, but how a massive and partly inaccessible archive appears to have described them.

MISSING:
Evidence showing whether expert prompt writers actually form explicit theories about training-data language, or whether this knowledge remains tacit and outcome-driven.

BOUNDARY:
The source documents this problem for text-to-image prompting. It does not show that every effective modifier corresponds transparently to a recoverable historical caption pattern.

CITATION TRAIL:
[[Z-RF-20260817-009]]
→ Oppenlaender, “A Taxonomy of Prompt Modifiers”
→ prompting requires anticipating historical Web descriptions
→ prompt expertise as reverse inference into an image-text archive
→ compare actual corpus language with practitioner folk explanations

TEST:
Take a set of historically successful prompt modifiers. Search accessible image-text datasets for the linguistic contexts surrounding those terms. Compare practitioner explanations of what each modifier “does” with the actual image-caption associations in the corpus.

PLATFORM:
[[Prompt Vernacular]]

LINKS:
[[Z-RF-20260817-009]]
[[Z-RF-20260817-004]]
[[Training Data as Culture]]
[[Archive of Descriptions]]
[[Prompt Archaeology]]

BIBTEX:
@misc{Oppenlaender2022PromptModifiers,
  author = {Jonas Oppenlaender},
  title = {A Taxonomy of Prompt Modifiers for Text-To-Image Generation},
  year = {2022},
  eprint = {2204.13988},
  archivePrefix = {arXiv},
  primaryClass = {cs.MM}
}
''')

add(r'''
ZETTEL

ID:
Z-RF-20260818-013

TITLE:
A stable prompt ritual can preserve a false causal theory.

SOURCE:
Jonas Oppenlaender — “A Taxonomy of Prompt Modifiers for Text-To-Image Generation” — 2022/2023 — §6.2.2, discussion of workflows, idiosyncratic choices, and folk theories.

PASSAGE:
[PARAPHRASE]
Oppenlaender notes that practitioners make idiosyncratic choices such as particular seeds or canvas dimensions and explicitly raises the possibility that some such practices are folk theories: causal attributions that may or may not be true.

RESEARCH OBJECT:
Community persistence is evidence that a practice is socially real, not evidence that its causal explanation is technically correct.

LOCAL MOVE:
This puts [[Z-RF-20260817-004]] under opposition. A prompt term can acquire an operational reputation through experimentation and circulation while the community misidentifies why the observed effect occurred.

SOURCE TERMS:
“idiosyncratic choices”
“folk theories”
“causal attributions”
“may or may not be true”
“experimentation”
“experience”

WHAT BECAME STRANGE:
The same trial-and-error process that produces expertise can also produce superstition.

QUESTION:
How do prompt communities distinguish robust operators from lucky correlations?

DEEPER QUESTION:
Does stochastic generation make prompt culture unusually hospitable to technically false but culturally durable causal beliefs?

MECHANISM:
prompt variation
→ stochastic output
→ salient desirable result
→ causal attribution to recent modification
→ repetition / sharing
→ community convention

without necessarily establishing:

modification
→ causal effect

FORMAL SHIFT:
<OBSERVED CO-OCCURRENCE>
→ <PRACTITIONER CAUSAL ATTRIBUTION>
→ [SOCIAL REPLICATION]
→ <STABILIZED TECHNIQUE OR FOLK THEORY>

SOURCE FORMALISM:
The source explicitly distinguishes practitioner choices grounded in experimentation from possible folk theories whose causal attribution may be false.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

SOCIAL_STABILITY(term)
≠
CAUSAL_EFFECT(term)

A useful test requires:

same prompt
same model/configuration
many seeds
with_modifier / without_modifier

rather than remembered exemplary outputs.

TENSION:
[[Z-RF-20260817-004]] treats prompt modifiers as experimentally acquired operators. Oppenlaender’s own later discussion blocks a simple inference from acquired practice to genuine mechanism.

MISSING:
Controlled ablation studies of historically important “magic terms,” quality boosters, repeated terms, seed rituals, and dimension-specific prompt lore.

BOUNDARY:
The source proposes folk theory as a possibility for some practitioner choices. It does not demonstrate that any particular named modifier is causally inert.

CITATION TRAIL:
[[Z-RF-20260817-004]]
→ Oppenlaender §6.2.2
→ practitioner folk theories
→ distinguish cultural efficacy from computational efficacy
→ experimentally ablate prompt lore

TEST:
Select twenty widely circulated prompt prescriptions. For each one, preregister the claimed effect and evaluate it across many matched generations, seeds, subjects, and model versions. Preserve separately:
technical effect,
perceived effect,
community belief,
and historical persistence.

PLATFORM:
[[Prompt Vernacular]]

LINKS:
[[Z-RF-20260817-004]]
[[Prompt Folk Theory]]
[[Magic Terms]]
[[Operational Semantics]]
[[Causal Hallucination]]

BIBTEX:
@misc{Oppenlaender2022PromptModifiers,
  author = {Jonas Oppenlaender},
  title = {A Taxonomy of Prompt Modifiers for Text-To-Image Generation},
  year = {2022},
  eprint = {2204.13988},
  archivePrefix = {arXiv},
  primaryClass = {cs.MM}
}
''')

add(r'''
ZETTEL

ID:
Z-RF-20260818-014

TITLE:
The shop that makes aesthetic competence can contain trade secrets.

SOURCE:
Clifford Geertz — “Art as a Cultural System” — 1976 — p. 1497.
Jonas Oppenlaender — “A Taxonomy of Prompt Modifiers for Text-To-Image Generation” — 2022/2023 — §3.2.1.

PASSAGE:
[QUOTE]
Geertz: “Art and the equipment to grasp it are made in the same shop.”

[PARAPHRASE]
Oppenlaender found that practitioners did not always disclose prompts; commercial interests, including NFT sales, could motivate creators to keep prompts secret.

RESEARCH OBJECT:
A cultural system can reproduce aesthetic competence unevenly when operative knowledge itself becomes scarce property.

LOCAL MOVE:
[[Z-RF-20260817-009]] assumed that the cultural “shop” reproduces the equipment by which participants learn to perceive and make distinctions. Prompt culture introduces restricted access inside the shop.

SOURCE TERMS:
“equipment to grasp”
“practitioners”
“share”
“prompts”
“secret”
“commercial interests”

WHAT BECAME STRANGE:
A community can publicly circulate artworks while privately withholding the procedures required to reproduce their effects.

QUESTION:
What kind of cultural system teaches people to recognize an aesthetic while preventing them from acquiring the means to reproduce it?

DEEPER QUESTION:
Does prompt secrecy turn aesthetic competence into stratified technical capital?

MECHANISM:
public output
→ community admiration / interpretation

but:

private prompt history
→ restricted operational knowledge
→ asymmetric reproducibility
→ expertise / market advantage

FORMAL SHIFT:
<PUBLIC ARTIFACT>
→ <SHARED AESTHETIC JUDGMENT>
→ [WITHHOLD GENERATIVE PROCEDURE]
→ <UNEQUAL PRODUCTION COMPETENCE>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

The “shop” can split:

SHOP_perception
= public images + discourse + comparison

SHOP_operation
= prompts + workflow + parameters + rejected outputs

Access(SHOP_perception) may be high
while
Access(SHOP_operation) is low.

TENSION:
Geertz’s formulation suggests that aesthetic objects and capacities arise from common cultural formation. Prompt economies make it possible for the perceptual equipment and operative equipment to circulate under different access regimes.

MISSING:
Ethnographic evidence about when prompt secrecy increases status, economic value, stylistic differentiation, or barriers to novice learning.

BOUNDARY:
Oppenlaender documents some prompt withholding in an early community. It does not establish secrecy as the dominant organization of prompt culture.

CITATION TRAIL:
[[Z-RF-20260817-009]]
→ Geertz’s “equipment to grasp”
→ Oppenlaender’s observation of prompt secrecy
→ split perceptual competence from operative competence
→ study unequal transmission inside creative communities

TEST:
Compare open-prompt and closed-prompt creative communities. Measure how quickly newcomers learn to identify styles, reproduce styles, invent modifiers, and explain failures. Test whether withholding affects perceptual learning differently from generative skill.

PLATFORM:
[[AI Art as a Cultural System]]

LINKS:
[[Z-RF-20260817-009]]
[[Equipment to Grasp]]
[[Prompt Secrecy]]
[[Technical Capital]]
[[Communities of Practice]]

BIBTEX:
@article{Geertz1976ArtCulturalSystem,
  author = {Clifford Geertz},
  title = {Art as a Cultural System},
  journal = {MLN},
  volume = {91},
  number = {6},
  year = {1976},
  pages = {1473--1499}
}

@misc{Oppenlaender2022PromptModifiers,
  author = {Jonas Oppenlaender},
  title = {A Taxonomy of Prompt Modifiers for Text-To-Image Generation},
  year = {2022},
  eprint = {2204.13988},
  archivePrefix = {arXiv}
}
''')

add(r'''
ZETTEL

ID:
Z-RF-20260818-015

TITLE:
Body prompting falsifies “prompt equals text” without proving “body equals language.”

SOURCE:
Jonas Oppenlaender, Hannah Johnston, Johanna Silvennoinen, Helena Barranha — “Artworks Reimagined: Exploring Human-AI Co-Creation through Body Prompting” — 2024 — arXiv:2408.05476.

PASSAGE:
[PARAPHRASE]
The authors implement “body prompting” as an input modality for generative image creation in a public installation. Interviews with 79 visitors identify three embodied interaction strategies: re-creating, reimagining, and casual interaction.

RESEARCH OBJECT:
Prompting is better defined by its role in conditioning generation than by textuality.

LOCAL MOVE:
This pressures [[Z-AIACS-013]]. Bodily movement can clearly become generative input, but calling the body an “input language” adds a stronger claim than the source requires.

SOURCE TERMS:
“body prompting”
“input modality”
“embodied interaction”
“re-creating”
“reimagining”
“casual interaction”
“AI co-creation”

WHAT BECAME STRANGE:
The category “prompt” survives after words disappear.

QUESTION:
What minimum property makes an input a prompt?

DEEPER QUESTION:
Should “prompt” name a representational form, an intentional instruction, or simply any sensed intervention that conditions a generative state transition?

MECHANISM:
participant bodily action
→ sensed bodily configuration
→ system interpretation / mapping
→ generative conditioning
→ transformed artwork

FORMAL SHIFT:
<BODILY ACTION>
→ <MACHINE-READABLE BODY STATE>
→ [CONDITION GENERATION]
→ <IMAGE TRANSFORMATION>

SOURCE FORMALISM:
The source operationalizes bodily interaction as an input modality to a generative AI installation and reports three observed strategies of participant interaction.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

PROMPT(x) may require only:

x is sensed
AND
x modifies generative conditioning

This definition does not require:

x is linguistic
x has syntax
x is propositionally explicit.

TENSION:
[[Z-AIACS-013]] proposed embodiment as an “input language.” Body prompting supports the weaker claim that the body can control state. Language would additionally require distinctions such as combinability, grammar, conventional signs, or systematic semantics.

MISSING:
Evidence showing whether participants learn stable bodily correspondences that can be recombined intentionally, rather than merely discovering responsive gestures.

BOUNDARY:
The study establishes embodied generative interaction. It does not establish a bodily language or formal grammar.

CITATION TRAIL:
[[Z-AIACS-013]]
→ Oppenlaender et al., “Artworks Reimagined”
→ prompt without text
→ split prompting from language
→ determine what additional evidence would establish embodied syntax

TEST:
Repeat the installation longitudinally. Test whether participants acquire reusable gesture units, predict their effects, combine them compositionally, teach them to others, and detect malformed combinations. If none occur, retain “input modality” and reject “language.”

PLATFORM:
[[Executable Narrative]]

LINKS:
[[Z-AIACS-013]]
[[Body as Input]]
[[Body Prompting]]
[[Prompt Beyond Language]]
[[Embodied Control]]

BIBTEX:
@misc{OppenlaenderEtAl2024BodyPrompting,
  author = {Jonas Oppenlaender and Hannah Johnston and Johanna Silvennoinen and Helena Barranha},
  title = {Artworks Reimagined: Exploring Human-AI Co-Creation through Body Prompting},
  year = {2024},
  eprint = {2408.05476},
  archivePrefix = {arXiv},
  primaryClass = {cs.HC}
}
''')

add(r'''
ZETTEL

ID:
Z-RF-20260818-016

TITLE:
Turner’s “operator” and a computational prompt operate on different kinds of state.

SOURCE:
Victor W. Turner — The Forest of Symbols: Aspects of Ndembu Ritual — 1967 — “Symbols in Ndembu Ritual.”
Jonas Oppenlaender — “A Taxonomy of Prompt Modifiers for Text-To-Image Generation” — 2022/2023 — §§2.2, 5.

PASSAGE:
[PARAPHRASE]
Turner treats ritual symbols as inseparable from social process rather than as static containers of meaning.

[PARAPHRASE]
Oppenlaender describes prompt modifiers as phrases added to textual inputs to direct a text-to-image system toward different generated results.

RESEARCH OBJECT:
“Operator” splits into a social-process sense and a computational-conditioning sense.

LOCAL MOVE:
This corrects an easy extension of [[Z-AIACS-015]]. The apparent bridge between Turner’s active symbols and executable prompts is interesting precisely because it is not an equivalence.

SOURCE TERMS:
Turner:
“symbol”
“ritual”
“social process”

Oppenlaender:
“prompt modifier”
“direct”
“textual input”
“resulting image”

WHAT BECAME STRANGE:
The same prompt expression can potentially operate twice: once on a machine state and once on relations among people who recognize, value, copy, prohibit, or politicize it.

QUESTION:
When does a prompt term become both a computational intervention and a social symbol?

DEEPER QUESTION:
Can the two effects diverge so completely that a computationally useless prompt remains socially powerful, or a computationally powerful modifier remains culturally meaningless?

MECHANISM:
COMPUTATIONAL:
prompt term
→ conditioning
→ generation changes

SOCIAL:
shared prompt term
→ interpretation / status / norm / affiliation
→ social practice changes

FORMAL SHIFT:
<PROMPT EXPRESSION>
→ <TWO POSSIBLE STATE SPACES>
→ [OPERATE]
→ <MODEL-STATE CHANGE AND/OR SOCIAL-PROCESS CHANGE>

SOURCE FORMALISM:
Oppenlaender supplies an explicit technical role for modifiers as additions to prompts intended to direct generated outputs.

Turner supplies a processual account of ritual symbols embedded in social action, not computational syntax.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

For expression e:

C(e) = measurable generative effect

S(e) = measurable social-practice effect

Four cases become possible:

C high / S high
C high / S low
C low / S high
C low / S low

TENSION:
Calling prompts “ritual incantations” collapses two distinct operations. Yet separating them completely misses cases such as “minority prompt,” where technical conditioning and public political meaning are intentionally coupled.

MISSING:
Cases measuring both machine-level and community-level consequences of the same prompt expression.

BOUNDARY:
Formal resemblance between a prompt acting on a model and a Turnerian symbol acting within social process does not establish genealogy or theoretical identity.

CITATION TRAIL:
[[Z-AIACS-015]]
→ Turner, The Forest of Symbols
→ Oppenlaender, prompt modifiers
→ split computational operation from social operation
→ search for expressions with divergent C(e) and S(e)

TEST:
Choose prompt expressions with strong community identities: “masterpiece,” named artists, “minority prompt,” “AI art,” deprecated magic terms. Ablate each expression computationally while independently testing whether its presence changes how practitioners interpret the maker, method, status, or politics of the resulting artifact.

PLATFORM:
[[Prompt Practice]]

LINKS:
[[Z-AIACS-015]]
[[Turner]]
[[Prompt Operators]]
[[Ritual or Craft]]
[[Social Process]]

BIBTEX:
@book{Turner1967Forest,
  author = {Victor W. Turner},
  title = {The Forest of Symbols: Aspects of Ndembu Ritual},
  publisher = {Cornell University Press},
  year = {1967}
}

@misc{Oppenlaender2022PromptModifiers,
  author = {Jonas Oppenlaender},
  title = {A Taxonomy of Prompt Modifiers for Text-To-Image Generation},
  year = {2022},
  eprint = {2204.13988},
  archivePrefix = {arXiv}
}
''')

add(r'''
ZETTEL

ID:
Z-RF-20260818-017

TITLE:
Talking about AI art can become part of the machinery that makes the next artwork.

SOURCE:
Jonas Oppenlaender — “A Taxonomy of Prompt Modifiers for Text-To-Image Generation” — 2022/2023 — §§2.2, 3.2.1, 5, 6.2.1.

PASSAGE:
[PARAPHRASE]
Oppenlaender documents practitioners learning prompt techniques through community resources, social-media posts, shared prompts, guides, experimentation, and observation of others’ work. Those learned expressions are then inserted into later generations.

RESEARCH OBJECT:
Discourse surrounding an artwork can feed causally into subsequent artifacts rather than merely interpreting prior ones.

LOCAL MOVE:
This sharpens [[Z-AIACS-017]]. “Meaning-in-use” and feedback are not only joined when a platform learns from users. Human cultural circulation itself can create a feedback loop without any model retraining.

SOURCE TERMS:
“online community”
“shared”
“resources”
“experimentation”
“prompts”
“community-learning”

WHAT BECAME STRANGE:
The commentary layer can become production infrastructure while the model weights remain completely unchanged.

QUESTION:
When does criticism, discussion, or prompt-sharing stop being reception and become part of the generative apparatus?

DEEPER QUESTION:
Can an AI-art culture modify a model’s effective behavior socially without modifying the model technically?

MECHANISM:
output
→ public discussion / prompt disclosure / aesthetic judgment
→ reusable expression learned by another practitioner
→ new prompt
→ new generation
→ further public circulation

FORMAL SHIFT:
<ARTIFACT>
→ <SOCIAL DESCRIPTION / EVALUATION>
→ [REINSERT INTO PROMPT PRACTICE]
→ <NEW ARTIFACT>

SOURCE FORMALISM:
Oppenlaender documents community learning, shared prompt resources, iterative experimentation, and the movement of techniques from community discourse into prompt practice.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

No weight update is required:

G fixed

output_t
→ discourse_t
→ prompt_{t+1}
→ G(prompt_{t+1})
→ output_{t+1}

Culture changes the input distribution around a fixed generator.

TENSION:
[[Z-AIACS-017]] distinguished interpretive use from cybernetic state-changing use. Here the generator’s internal state need not change, yet reception still changes future production by changing human prompting practice.

MISSING:
Longitudinal traces linking identifiable community discussions to later changes in prompt vocabulary and output distributions.

BOUNDARY:
The source documents community transmission but does not quantify how strongly particular discussions reshape population-level generation.

CITATION TRAIL:
[[Z-AIACS-017]]
→ Oppenlaender’s online ethnography
→ shared discourse enters future prompts
→ cultural feedback without model learning
→ trace phrase propagation through generation histories

TEST:
Identify newly introduced prompt terms in timestamped community archives. Track adoption through later prompts and generated outputs while holding model version fixed. Estimate whether discourse-driven prompt diffusion produces measurable visual convergence.

PLATFORM:
[[AI Art as a Cultural System]]

LINKS:
[[Z-AIACS-017]]
[[Cultural Feedback]]
[[Prompt Diffusion]]
[[Reception Becomes Operation]]
[[Community Learning]]

BIBTEX:
@misc{Oppenlaender2022PromptModifiers,
  author = {Jonas Oppenlaender},
  title = {A Taxonomy of Prompt Modifiers for Text-To-Image Generation},
  year = {2022},
  eprint = {2204.13988},
  archivePrefix = {arXiv}
}
''')

add(r'''
ZETTEL

ID:
Z-RF-20260818-018

TITLE:
Sontag asks for descriptive rather than prescriptive form-language just before prompting makes description prescriptive.

SOURCE:
Susan Sontag — “Against Interpretation” — 1964; collected in Against Interpretation and Other Essays — 1966 — §§8–10.
Jonas Oppenlaender — “A Taxonomy of Prompt Modifiers for Text-To-Image Generation” — 2022/2023.

PASSAGE:
[PARAPHRASE]
Sontag asks criticism to develop a descriptive rather than prescriptive vocabulary for artistic forms and argues that criticism should reveal how a work is what it is rather than extract hidden meaning.

[PARAPHRASE]
In text-to-image systems, practitioners use textual descriptions and modifiers precisely to alter style, quality, subject, and other aspects of the produced image.

RESEARCH OBJECT:
The same aesthetic vocabulary can change causal position: after an artwork it describes form; before generation it can prescribe form.

LOCAL MOVE:
This changes the Sontag/Geertz opposition in [[Z-AIACS-013]]. Generative systems do not merely invite another theory of interpretation. They can move critical language upstream into production.

SOURCE TERMS:
Sontag:
“descriptive”
“prescriptive”
“vocabulary”
“forms”
“how it is what it is”

Oppenlaender:
“style modifier”
“quality booster”
“prompt”
“control”

WHAT BECAME STRANGE:
A sentence such as “high contrast, shallow depth of field, asymmetrical composition” can be criticism in one temporal position and control syntax in another.

QUESTION:
What happens to aesthetic criticism when its descriptive vocabulary doubles as an executable production interface?

DEEPER QUESTION:
Can a culture’s vocabulary for noticing form become the control surface through which future forms are statistically reproduced?

MECHANISM:
historically:

artwork
→ critic observes form
→ descriptive vocabulary

generatively:

descriptive vocabulary
→ prompt conditioning
→ artwork

FORMAL SHIFT:
<AESTHETIC DESCRIPTION>
→ <MODEL CONDITIONING>
→ [GENERATE]
→ <FORM BEARING FEATURES NAMED BY THE DESCRIPTION>

SOURCE FORMALISM:
Sontag explicitly distinguishes descriptive from prescriptive vocabulary.

Oppenlaender identifies style modifiers, quality boosters, subject terms, repetition, image prompts, and related devices for directing image generation.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

CRITICISM:
FORM → WORD

PROMPTING:
WORD → CONDITIONING → FORM

Generative systems partially reverse the arrow.

TENSION:
Sontag wants description to resist the domination of art by interpretation. Once descriptive form-language becomes generative control, even non-hermeneutic description can participate in standardizing what future art looks like.

MISSING:
Evidence showing whether aesthetic vocabulary taken from criticism and art history measurably narrows or expands generated formal possibilities.

BOUNDARY:
A prompt does not literally execute natural language as deterministic code. The reverse-arrow formalization describes causal conditioning, not exact compilation.

CITATION TRAIL:
[[Z-AIACS-013]]
→ Sontag, “Against Interpretation”
→ descriptive versus prescriptive vocabulary
→ Oppenlaender’s prompt modifiers
→ description migrates from criticism into generation
→ test whether critical vocabulary becomes aesthetic prior

TEST:
Build paired corpora of formal art criticism and prompt-language modifiers. Identify migrated terms, then measure whether frequent critical descriptors systematically induce recurrent compositional or stylistic features across model generations.

PLATFORM:
[[Art as Cultural System & AI Prompting]]

LINKS:
[[Z-AIACS-013]]
[[Z-AIACS-017]]
[[Against Interpretation]]
[[Description Becomes Operation]]
[[Operative Ekphrasis]]

BIBTEX:
@book{Sontag1966AgainstInterpretation,
  author = {Susan Sontag},
  title = {Against Interpretation and Other Essays},
  publisher = {Farrar, Straus and Giroux},
  year = {1966}
}

@misc{Oppenlaender2022PromptModifiers,
  author = {Jonas Oppenlaender},
  title = {A Taxonomy of Prompt Modifiers for Text-To-Image Generation},
  year = {2022},
  eprint = {2204.13988},
  archivePrefix = {arXiv}
}
''')

add(r'''
ZETTEL

ID:
Z-RF-20260818-019

TITLE:
Putting “Edo-period” in a prompt is not yet cultural context.

SOURCE:
Clifford Geertz — “Art as a Cultural System” — 1976 — pp. 1473–1499.
Jonas Oppenlaender — “A Taxonomy of Prompt Modifiers for Text-To-Image Generation” — 2022/2023 — §§2.1–2.2.

PASSAGE:
[PARAPHRASE]
Geertz insists that giving aesthetic objects cultural significance is a local matter tied to the forms of life in which aesthetic sensibilities are cultivated.

[PARAPHRASE]
Text-to-image systems statistically associate textual inputs with visual representations learned from large image-text corpora; prompt modifiers can be used to induce recognizable style and subject tendencies.

RESEARCH OBJECT:
A culturally named prompt token and a culturally situated meaning are different things.

LOCAL MOVE:
This opposes the easy analogy in the prompting notes that adding historical periods, local motifs, or cultural labels to prompts thereby “encodes cultural context.” The model may instead return a statistical visual stereotype associated with the label.

SOURCE TERMS:
Geertz:
“local matter”
“aesthetic force”
“social activity”

Oppenlaender:
“subject term”
“style modifier”
“textual input”
“trained”
“images and text”

WHAT BECAME STRANGE:
More cultural vocabulary in a prompt can produce a more culturally recognizable image while containing less situated cultural knowledge.

QUESTION:
When does a cultural reference in a prompt carry local meaning, and when is it merely an index into a learned visual cluster?

DEEPER QUESTION:
Can text-to-image generation make cultural thinness look like cultural specificity?

MECHANISM:
cultural label
→ statistical image-text association
→ visually recognizable trope
→ audience recognizes cultural category

but possibly without:

local practice
→ situated distinctions
→ participant knowledge
→ cultural significance

FORMAL SHIFT:
<CULTURAL NAME>
→ <MODEL-LEARNED VISUAL ASSOCIATIONS>
→ [GENERATE]
→ <CULTURALLY LEGIBLE SURFACE>

SOURCE FORMALISM:
Oppenlaender describes text-to-image systems as trained on image-text pairs and describes style and subject modifiers used to steer visual output.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

CULTURAL_SPECIFICITY_visual
≠
CULTURAL_THICKNESS_contextual

A prompt can increase the first while leaving the second unchanged.

TENSION:
The uploaded prompting account argues that “samurai warrior in Edo-period painting style” invokes cultural codes and values. Geertz’s insistence on locality makes that inference precisely what needs demonstration rather than assumption.

MISSING:
Comparisons between what insiders in the invoked cultural practice regard as consequential distinctions and what the model changes when supplied the corresponding cultural label.

BOUNDARY:
The existence of statistical stereotypes does not imply that generated imagery cannot participate in genuine local meaning after generation. It only blocks the inference that naming a culture in a prompt already supplies that context.

CITATION TRAIL:
[[Z-RF-20260817-009]]
→ Geertz, local aesthetic significance
→ Oppenlaender, image-text conditioning and prompt modifiers
→ split culturally labeled generation from culturally situated interpretation
→ compare model-visible features with locally consequential distinctions

TEST:
Choose a culturally specific artistic practice with expert participants. Generate outputs from increasingly elaborate cultural labels. Ask practitioners which locally meaningful distinctions are present, absent, distorted, or replaced by generic markers. Compare these judgments with visual changes caused by the added prompt tokens.

PLATFORM:
[[Geertz’s Symbolic Anthropology and Art as Cultural System]]

LINKS:
[[Z-RF-20260817-009]]
[[Thin Cultural Specificity]]
[[Thick Description]]
[[Prompt Stereotype]]
[[Local Meaning]]

BIBTEX:
@article{Geertz1976ArtCulturalSystem,
  author = {Clifford Geertz},
  title = {Art as a Cultural System},
  journal = {MLN},
  volume = {91},
  number = {6},
  year = {1976},
  pages = {1473--1499}
}

@misc{Oppenlaender2022PromptModifiers,
  author = {Jonas Oppenlaender},
  title = {A Taxonomy of Prompt Modifiers for Text-To-Image Generation},
  year = {2022},
  eprint = {2204.13988},
  archivePrefix = {arXiv}
}
''')

add(r'''
ZETTEL

ID:
Z-RF-20260818-020

TITLE:
The most Geertzian object may be the distinction a practitioner learns to notice.

SOURCE:
Clifford Geertz — “Art as a Cultural System” — 1976 — especially p. 1497.
Jonas Oppenlaender, Rhema Linder, Johanna Silvennoinen — “Prompting AI Art: An Investigation into the Creative Skill of Prompt Engineering” — 2023 — arXiv:2303.13534.

PASSAGE:
[PARAPHRASE]
Geertz argues that capacities for aesthetic response are brought into actual existence through experience within particular worlds of things, practices, and distinctions.

[PARAPHRASE]
Oppenlaender, Linder, and Silvennoinen found that participants could judge prompt quality and write descriptive prompts but lacked the style-specific vocabulary needed for effective prompting; the authors conclude that prompt engineering is a non-intuitive skill acquired through practice and learning.

RESEARCH OBJECT:
Prompt expertise may be less about accumulating words than acquiring perceptual distinctions that make certain words worth trying.

LOCAL MOVE:
This deepens [[Z-RF-20260817-009]]. “Equipment to grasp” can be operationalized as the difference between what novices and practitioners are capable of noticing, naming, and correcting.

SOURCE TERMS:
Geertz:
“equipment to grasp”
“experience”

Oppenlaender et al.:
“style-specific vocabulary”
“skill”
“practice”
“learning”
“refine prompts”

WHAT BECAME STRANGE:
A novice and expert can look at the same failed generation yet inhabit different actionable worlds because only one sees what distinction should become the next instruction.

QUESTION:
Is the deepest unit of prompt expertise a word, or a learned capacity to detect a correctable difference?

DEEPER QUESTION:
Could we reconstruct an AI-art culture by cataloguing not its preferred styles but the failures its members have learned to see?

MECHANISM:
repeated generation
→ encounter with outputs
→ socially learned aesthetic distinctions
→ detection of specific mismatch
→ vocabulary attached to mismatch
→ targeted correction

FORMAL SHIFT:
<OUTPUT>
→ <PERCEPTUALLY AVAILABLE DIFFERENCE>
→ [NAME / CORRECT]
→ <NEXT GENERATIVE ACTION>

SOURCE FORMALISM:
The prompt-skill study distinguishes prompt evaluation, prompt writing, and prompt refinement, and identifies lack of style-specific vocabulary among inexperienced participants.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

EXPERTISE is not merely:

lexicon size

but:

NOTICE(output, desired_state)
→ discriminable difference d
→ associate intervention i
→ test i

Culture may reside in the learned mapping:

d → i

TENSION:
A lexical account says experts know special prompt terms. A Geertzian account suggests those terms matter because practitioners have acquired sensitivities that make certain differences salient in the first place.

MISSING:
Process evidence showing what experts perceive before they choose a modifier, rather than only recording the modifier they eventually type.

BOUNDARY:
The empirical prompt study shows differences in skill and vocabulary. It does not establish that perceptual discrimination is the causal source of those differences.

CITATION TRAIL:
[[Z-RF-20260817-009]]
→ Geertz’s acquired aesthetic equipment
→ Oppenlaender et al., prompt skill
→ vocabulary versus perceptual distinction
→ instrument the moment before prompt revision

TEST:
Give novices and experts identical imperfect generations and require them to mark every noticed discrepancy before allowing prompt editing. Compare discrepancy categories, granularity, correction choices, and successful subsequent generations. Track which distinctions novices acquire through training.

PLATFORM:
[[AI Art as a Cultural System]]

LINKS:
[[Z-RF-20260817-009]]
[[Equipment to Grasp]]
[[Prompt Expertise]]
[[Failure Becomes Specification]]
[[Aesthetic Attention]]

BIBTEX:
@article{Geertz1976ArtCulturalSystem,
  author = {Clifford Geertz},
  title = {Art as a Cultural System},
  journal = {MLN},
  volume = {91},
  number = {6},
  year = {1976},
  pages = {1473--1499}
}

@misc{OppenlaenderLinderSilvennoinen2023PromptingAIArt,
  author = {Jonas Oppenlaender and Rhema Linder and Johanna Silvennoinen},
  title = {Prompting AI Art: An Investigation into the Creative Skill of Prompt Engineering},
  year = {2023},
  eprint = {2303.13534},
  archivePrefix = {arXiv}
}
''')
# ---------- compile cards and field ----------
def field(text, name):
    m=re.search(rf'(?ms)^\s*{re.escape(name)}:\s*\n(.*?)(?=\n[A-Z][A-Z /_-]*:\s*\n|\Z)', text)
    return m.group(1).strip() if m else ''
def slug(s):
    s=s.lower().replace('’','').replace('“','').replace('”','').replace('—','-')
    s=re.sub(r'[^a-z0-9]+','-',s).strip('-')
    return s[:70] or 'untitled'
records=[]
for i,c in enumerate(cards,1):
    rid=field(c,'ID')
    title=field(c,'TITLE')
    src=field(c,'SOURCE')
    sig='MULTISOURCE' if '\n' in src else ('AIACS' if 'AI Art as a Cultural System' in src else 'SOURCE')
    fn=f"{i:03d}__{slug(title)}__{sig}__{rid}__from-chat.txt"
    (PKG/fn).write_text(c,encoding='utf-8')
    (PKG/'_MD'/fn.replace('.txt','.md')).write_text(c,encoding='utf-8')
    h=hashlib.sha256(c.encode()).hexdigest()
    rec={'order':i,'id':rid,'title':title,'source':src,'platform':field(c,'PLATFORM'),'links':re.findall(r'\[\[([^\]]+)\]\]',field(c,'LINKS')),'wikilinks':re.findall(r'\[\[([^\]]+)\]\]',c),'filename':fn,'sha256':h,'payload':c,'origin':'visible-assistant-output-reconstructed'}
    records.append(rec)

# whole deck
zettels_txt=[]
for r in records:
    zettels_txt.append(f"===== {r['order']:03d} · {r['id']} · {r['title']} =====\n")
    zettels_txt.append(r['payload'])
(PKG/'ZETTELS.txt').write_text('\n'.join(zettels_txt),encoding='utf-8')
(PKG/'ZETTELS.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
with (PKG/'ZETTELS.jsonl').open('w',encoding='utf-8') as f:
    for r in records:
        rr={k:v for k,v in r.items() if k!='payload'}; rr['payload']=r['payload']
        f.write(json.dumps(rr,ensure_ascii=False)+'\n')

ids={r['id'] for r in records}
platforms=sorted({p.strip('[]') for r in records for p in re.findall(r'\[\[([^\]]+)\]\]',r['platform'])})
relations=[]
for r in records:
    for j,p in enumerate(re.findall(r'\[\[([^\]]+)\]\]',r['platform']),1):
        relations.append({'type':'MEMBER_OF','source':r['id'],'field':'PLATFORM','ordinal':j,'literal':f'[[{p}]]','target':p,'resolution':'PLATFORM','provenance':'NATIVE'})
    for j,l in enumerate(r['links'],1):
        res='ZETTEL' if l in ids else ('PLATFORM' if l in platforms else 'GHOST')
        relations.append({'type':'LINKS_TO','source':r['id'],'field':'LINKS','ordinal':j,'literal':f'[[{l}]]','target':l,'resolution':res,'provenance':'NATIVE'})
    for j,l in enumerate(r['wikilinks'],1):
        res='ZETTEL' if l in ids else ('PLATFORM' if l in platforms else 'GHOST')
        relations.append({'type':'WIKILINKS_TO','source':r['id'],'field':'PAYLOAD','ordinal':j,'literal':f'[[{l}]]','target':l,'resolution':res,'provenance':'NATIVE'})
# backlinks derived from explicit links, dedup by pair
seen=set()
for rel in list(relations):
    if rel['type']=='LINKS_TO' and rel['resolution']=='ZETTEL':
        key=(rel['target'],rel['source'])
        if key not in seen:
            seen.add(key)
            relations.append({'type':'BACKLINK','source':rel['target'],'field':'DERIVED','ordinal':1,'literal':rel['source'],'target':rel['source'],'resolution':'ZETTEL','provenance':'DERIVED'})
ghosts=sorted({rel['target'] for rel in relations if rel['resolution']=='GHOST'})

# source urls, bibliography and local resource map
source_urls={
'Geertz1976ArtCulturalSystem':'https://www.jstor.org/stable/2907147',
'Oppenlaender2022PromptModifiers':'https://arxiv.org/abs/2204.13988',
'OppenlaenderLinderSilvennoinen2023PromptingAIArt':'https://arxiv.org/abs/2303.13534',
'LiuChilton2021PromptEngineering':'https://arxiv.org/abs/2109.06977',
'TorricelliEtAl2023Interface':'https://arxiv.org/abs/2312.00233',
'SimonenEtAl2025DefaultImages':'https://arxiv.org/abs/2505.09166',
'OppenlaenderEtAl2024BodyPrompting':'https://arxiv.org/abs/2408.05476',
'Steyerl2023MeanImages':'https://newleftreview.org/issues/ii140/articles/hito-steyerl-mean-images',
'RivasSanMartin2024Archivo':'https://www.academia.edu/128733868/Un_Archivo_Inexistente',
'Rivas2025InexistentArchive':'https://doi.org/10.21134/a3y8jg10',
'Maturana1975LivingOrganization':'https://www.sciencedirect.com/science/article/pii/S0020737375800150',
'Weizenbaum1966ELIZA':'https://doi.org/10.1145/365153.365168',
'Sontag1966AgainstInterpretation':'https://us.macmillan.com/books/9780312280864/againstinterpretationandotheressays/',
'Turner1967Forest':'https://www.cornellpress.cornell.edu/book/9780801491016/the-forest-of-symbols/'
}
refs=r'''% checkpoint: SLIPCASE-20260817-AIACS-01
% package: 2026-08-17__the-shop-makes-the-prompt__SLIPCASE-20260817-AIACS-01
% schema: SLIPCASE v15.55-AM
% return path: 000__RETURN_PATH.txt

@article{Geertz1976ArtCulturalSystem,
  author={Geertz, Clifford},
  title={Art as a Cultural System},
  journal={MLN},
  year={1976},
  volume={91},
  number={6},
  pages={1473--1499},
  doi={10.2307/2907147},
  url={https://www.jstor.org/stable/2907147}
}

@misc{Oppenlaender2022PromptModifiers,
  author={Oppenlaender, Jonas},
  title={A Taxonomy of Prompt Modifiers for Text-To-Image Generation},
  year={2022},
  eprint={2204.13988},
  archivePrefix={arXiv},
  doi={10.48550/arXiv.2204.13988},
  url={https://arxiv.org/abs/2204.13988}
}

@misc{OppenlaenderLinderSilvennoinen2023PromptingAIArt,
  author={Oppenlaender, Jonas and Linder, Rhema and Silvennoinen, Johanna},
  title={Prompting AI Art: An Investigation into the Creative Skill of Prompt Engineering},
  year={2023},
  eprint={2303.13534},
  archivePrefix={arXiv},
  doi={10.48550/arXiv.2303.13534},
  url={https://arxiv.org/abs/2303.13534}
}

@misc{LiuChilton2021PromptEngineering,
  author={Liu, Vivian and Chilton, Lydia B.},
  title={Design Guidelines for Prompt Engineering Text-to-Image Generative Models},
  year={2021},
  eprint={2109.06977},
  archivePrefix={arXiv},
  doi={10.48550/arXiv.2109.06977},
  url={https://arxiv.org/abs/2109.06977}
}

@misc{TorricelliEtAl2023Interface,
  author={Torricelli, Maddalena and Martino, Mauro and Baronchelli, Andrea and Aiello, Luca Maria},
  title={The role of interface design on prompt-mediated creativity in Generative AI},
  year={2023},
  eprint={2312.00233},
  archivePrefix={arXiv},
  doi={10.48550/arXiv.2312.00233},
  url={https://arxiv.org/abs/2312.00233}
}

@misc{SimonenEtAl2025DefaultImages,
  author={Simonen, Hannu and Kiviniemi, Atte and Johnston, Hannah and Barranha, Helena and Oppenlaender, Jonas},
  title={An Exploration of Default Images in Text-to-Image Generation},
  year={2025},
  eprint={2505.09166},
  archivePrefix={arXiv},
  doi={10.48550/arXiv.2505.09166},
  url={https://arxiv.org/abs/2505.09166}
}

@misc{OppenlaenderEtAl2024BodyPrompting,
  author={Oppenlaender, Jonas and Johnston, Hannah and Silvennoinen, Johanna and Barranha, Helena},
  title={Artworks Reimagined: Exploring Human-AI Co-Creation through Body Prompting},
  year={2024},
  eprint={2408.05476},
  archivePrefix={arXiv},
  doi={10.48550/arXiv.2408.05476},
  url={https://arxiv.org/abs/2408.05476}
}

@article{Steyerl2023MeanImages,
  author={Steyerl, Hito},
  title={Mean Images},
  journal={New Left Review},
  year={2023},
  number={140/141},
  pages={82--97},
  doi={10.64590/uhm},
  url={https://newleftreview.org/issues/ii140/articles/hito-steyerl-mean-images}
}

@book{RivasSanMartin2024Archivo,
  author={Rivas San Martín, Felipe},
  title={Un Archivo Inexistente},
  publisher={Écfrasis, ediciones},
  address={Santiago},
  year={2024},
  isbn={978-956-09200-7-2},
  url={https://www.academia.edu/128733868/Un_Archivo_Inexistente}
}

@article{Rivas2025InexistentArchive,
  author={Rivas San Martín, Felipe},
  title={Inexistent Archive},
  journal={ReCIA - Journal of the Arts Research Centre},
  year={2025},
  number={1},
  pages={153--171},
  doi={10.21134/a3y8jg10},
  url={https://revistas.innovacionumh.es/index.php/recia/en/article/view/2825}
}

@article{Maturana1975LivingOrganization,
  author={Maturana, Humberto R.},
  title={The Organization of the Living: A Theory of the Living Organization},
  journal={International Journal of Man-Machine Studies},
  year={1975},
  volume={7},
  number={3},
  pages={313--332},
  url={https://www.sciencedirect.com/science/article/pii/S0020737375800150}
}

@article{Weizenbaum1966ELIZA,
  author={Weizenbaum, Joseph},
  title={ELIZA---A Computer Program for the Study of Natural Language Communication Between Man and Machine},
  journal={Communications of the ACM},
  year={1966},
  volume={9},
  number={1},
  pages={36--45},
  doi={10.1145/365153.365168},
  url={https://doi.org/10.1145/365153.365168}
}

@book{Sontag1966AgainstInterpretation,
  author={Sontag, Susan},
  title={Against Interpretation and Other Essays},
  publisher={Farrar, Straus and Giroux},
  year={1966}
}

@book{Turner1967Forest,
  author={Turner, Victor W.},
  title={The Forest of Symbols: Aspects of Ndembu Ritual},
  publisher={Cornell University Press},
  year={1967}
}
'''
(PKG/'SLIPCASE-20260817-AIACS-01__references.bib').write_text(refs,encoding='utf-8')

local_resource_files={p.name:p for p in (PKG/'_RESOURCES').iterdir() if p.is_file()}
resources=[
 {'name':'AI Art as a Cultural System','type':'PDF','state':'LOCAL_FILE','local':'_RESOURCES/AI_Art_as_a_Cultural_System__provided.pdf','provided_by':'user'},
 {'name':'Art as Cultural System & AI Prompting','type':'PDF','state':'LOCAL_FILE','local':'_RESOURCES/Art_as_Cultural_System_and_AI_Prompting__provided.pdf','provided_by':'user'},
 {'name':'Geertz’s Symbolic Anthropology and Art as Cultural System','type':'PDF','state':'LOCAL_FILE','local':'_RESOURCES/Geertz_Symbolic_Anthropology_and_Art__provided.pdf','provided_by':'user'},
 {'name':'PRIME ZETTEL FORAGE v3.0','type':'PROMPT','state':'PASTED','local':'_PROMPTS/prime_zettel_forage__v3.0__prior.txt','provided_by':'user'},
 {'name':'SLIPCASE v15.55-AM','type':'PROMPT','state':'PASTED','local':'_PROMPTS/assembly_prompt__v15.55-AM.txt','provided_by':'user'},
]
for key,url in source_urls.items():
    resources.append({'name':key,'type':'SOURCE_URL','state':'LINK_ONLY','url':url,'provided_by':'web-verification-2026-08-17'})
for fn in sorted(local_resource_files):
    if fn.endswith('.pdf') and not any(r.get('local','').endswith(fn) for r in resources):
        resources.append({'name':fn,'type':'PDF','state':'LOCAL_FILE','local':'_RESOURCES/'+fn,'provided_by':'retrieved-public-source'})
# resource receipts for link-only
for r in resources:
    if r['state']=='LINK_ONLY':
        out=PKG/'_RESOURCES'/('LINK_ONLY__'+slug(r['name'])+'.txt')
        out.write_text(f"NAME: {r['name']}\nSTATE: LINK_ONLY\nURL: {r['url']}\nVERIFIED: bibliographic/source landing page checked 2026-08-17 via web search\n",encoding='utf-8')
        r['local']=str(out.relative_to(PKG))

# machine files
nodes=[]
for r in records: nodes.append({'id':r['id'],'type':'ZETTEL','title':r['title'],'sha256':r['sha256'],'path':r['filename']})
for p in platforms: nodes.append({'id':'PLATFORM:'+p,'type':'PLATFORM','title':p})
for g in ghosts: nodes.append({'id':'GHOST:'+g,'type':'GHOST','title':g})
for rs in resources: nodes.append({'id':'RESOURCE:'+rs['name'],'type':'RESOURCE','title':rs['name'],'state':rs['state'],'path':rs.get('local'),'url':rs.get('url')})
with (PKG/'_SLIPCASE/NODES.jsonl').open('w',encoding='utf-8') as f:
    for x in nodes:f.write(json.dumps(x,ensure_ascii=False)+'\n')
with (PKG/'_SLIPCASE/RELATIONS.jsonl').open('w',encoding='utf-8') as f:
    for x in relations:f.write(json.dumps(x,ensure_ascii=False)+'\n')
with (PKG/'_SLIPCASE/RESOURCES.jsonl').open('w',encoding='utf-8') as f:
    for x in resources:f.write(json.dumps(x,ensure_ascii=False)+'\n')
with (PKG/'_SLIPCASE/APPEARANCES.jsonl').open('w',encoding='utf-8') as f:
    for r in records:
        f.write(json.dumps({'zettel':r['id'],'origin':'current conversation assistant output','appearance':'reconstructed visible payload','compiler_note':'No machine-readable conversation export was available; payloads were reconstructed from visible conversation text and hashed at compilation.'},ensure_ascii=False)+'\n')
(PKG/'_SLIPCASE/ALIASES.json').write_text('{}\n',encoding='utf-8')

# ---------- field views ----------
from collections import Counter,defaultdict
back=defaultdict(list)
for rel in relations:
    if rel['type']=='LINKS_TO' and rel['resolution']=='ZETTEL': back[rel['target']].append(rel['source'])
link_count=Counter(rel['target'] for rel in relations if rel['type']=='LINKS_TO')
platform_count=Counter(rel['target'] for rel in relations if rel['type']=='MEMBER_OF')
maptxt=["MAP — THE SHOP MAKES THE PROMPT","",f"ZETTELS: {len(records)}",f"PLATFORMS: {len(platforms)}",f"GHOSTS: {len(ghosts)}",f"NATIVE LINKS: {sum(1 for x in relations if x['type']=='LINKS_TO')}",""]
maptxt.append("SUPPORTED DESCENTS")
for r in records:
    parents=[l for l in r['links'] if l in ids]
    if parents: maptxt.append(f"{', '.join(parents)} -> {r['id']} · {r['title']}")
maptxt += ["","ROOT PLATFORMS"]+[f"{k}: {v} cards" for k,v in platform_count.most_common()]
maptxt += ["","MOST CONNECTED ADDRESSES"]+[f"{k}: {v}" for k,v in link_count.most_common(20)]
(PKG/'000__MAP.txt').write_text('\n'.join(maptxt)+'\n',encoding='utf-8')

open_edges=[]
for r in records:
    for nm in ['QUESTION','DEEPER QUESTION','MISSING','BOUNDARY','TEST']:
        val=field(r['payload'],nm)
        if val and val!='NONE': open_edges.append(f"{r['id']} · {nm}\n{val}\n")
(PKG/'000__OPEN_EDGES.txt').write_text('OPEN EDGES\n\n'+'\n'.join(open_edges),encoding='utf-8')

# MOCs
mocs={
'01__prompt-as-diagnostic-practice.md':'''# Prompt as Diagnostic Practice\n\nCore lineage: [[Z-AIACS-016]] -> [[Z-RF-20260817-005]] -> [[Z-RF-20260818-020]].\n\nPrompt skill is not reducible to composing a good string. It is the learned ability to notice a correctable difference in an output, infer a plausible intervention, and test it.\n\nRelated: [[Z-RF-20260817-004]], [[Z-RF-20260818-013]], [[Z-RF-20260818-012]].\n''',
'02__culture-inside-the-generator.md':'''# Culture Inside the Generator\n\n[[Z-AIACS-003]] -> [[Z-RF-20260817-008]] adds historical corpus effects to the machine/user binary. [[Z-AIACS-004]] -> [[Z-RF-20260817-001]] separates interface defaults from semantic fallback defaults. [[Z-AIACS-006]] -> [[Z-RF-20260817-006]] shows corrective work occurring downstream of upstream representational conditions.\n''',
'03__description-changes-causal-position.md':'''# Description Changes Causal Position\n\n[[Z-RF-20260818-018]] reverses the ordinary critical arrow: FORM -> WORD becomes WORD -> CONDITIONING -> FORM. [[Z-RF-20260818-015]] pressures the assumption that prompts must be textual. [[Z-RF-20260818-016]] splits computational and social operation.\n''',
'04__provenance-and-the-visible-residue.md':'''# Provenance and the Visible Residue\n\n[[Z-AIACS-020]] treats the image as a residue of a production path. [[Z-RF-20260817-007]] shows visible error functioning as an ethical boundary. [[Z-RF-20260817-002]] warns that even the visible prompt may not exhaust the conditioning chain.\n'''
}
for fn,body in mocs.items():(PKG/'_MOCS'/fn).write_text(body,encoding='utf-8')
(PKG/'_ARRANGEMENTS/01__paper-trail.txt').write_text('PAPER TRAIL\n\nZ-RF-20260817-009 -> Z-RF-20260818-020 -> Z-RF-20260817-004 -> Z-RF-20260818-012 -> Z-RF-20260818-013 -> Z-RF-20260817-005 -> Z-RF-20260817-008 -> Z-RF-20260817-006 -> Z-RF-20260817-003 -> Z-RF-20260818-018 -> Z-RF-20260818-015\n',encoding='utf-8')

# bibliography views
bib_txt='BIBLIOGRAPHY — SLIPCASE-20260817-AIACS-01\n\n'+refs
(PKG/'000__BIBLIOGRAPHY.txt').write_text(bib_txt,encoding='utf-8')
(PKG/'000__BIBLIOGRAPHY.html').write_text('<!doctype html><meta charset="utf-8"><title>Bibliography</title><style>body{font:16px Georgia;max-width:900px;margin:40px auto;line-height:1.5;white-space:pre-wrap}</style><body>'+html.escape(bib_txt)+'</body>',encoding='utf-8')
restxt=['RESOURCES — SLIPCASE-20260817-AIACS-01','']
for r in resources: restxt.append(f"{r['state']} · {r['name']}\n  {r.get('local','')}\n  {r.get('url','')}")
(PKG/'000__RESOURCES.txt').write_text('\n'.join(restxt)+'\n',encoding='utf-8')
(PKG/'000__PROMPTS.txt').write_text('PROMPTS\n\n1. _PROMPTS/assembly_prompt__v15.55-AM.txt — exact SLIPCASE assembly instrument supplied by user.\n2. _PROMPTS/prime_zettel_forage__v3.0__prior.txt — prior forage instrument supplied by user.\n',encoding='utf-8')

# ---------- paper ----------
paper_slug='the-shop-makes-the-prompt'
paper_date='2026-08-17'
paper_md=r'''---
title: "The Shop Makes the Prompt"
subtitle: "Cultural Competence, Reverse Description, and the Operational Life of AI Art"
author: "Watson Hartsoe"
date: "{paper_date}"
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

# References
'''
paper_md=paper_md.replace('{paper_date}',paper_date)
(PKG/f'{paper_slug}__{paper_date}.md').write_text(paper_md,encoding='utf-8')

source_map='''SOURCE MAP — THE SHOP MAKES THE PROMPT\n\nCHECKPOINT: SLIPCASE-20260817-AIACS-01\nSTATUS: Working Paper · AI-augmented research process\n\nCLAIM 1 — Prompt expertise is better modeled as diagnostic practice than as mastery of a final string.\nZETTELS: Z-AIACS-016; Z-RF-20260817-004; Z-RF-20260817-005; Z-RF-20260818-020.\nCITEKEYS: Oppenlaender2022PromptModifiers; OppenlaenderLinderSilvennoinen2023PromptingAIArt; LiuChilton2021PromptEngineering.\nTYPE: COMPILER SYNTHESIS grounded in empirical prompt-practice studies.\n\nCLAIM 2 — The relevant learned unit may be a noticed, correctable difference.\nZETTELS: Z-RF-20260817-009; Z-RF-20260818-020.\nCITEKEYS: Geertz1976ArtCulturalSystem; OppenlaenderLinderSilvennoinen2023PromptingAIArt.\nTYPE: COMPILER SYNTHESIS; not source terminology.\n\nCLAIM 3 — Prompting can operate as reverse description of historical image-text culture.\nZETTELS: Z-RF-20260818-012; Z-RF-20260817-008.\nCITEKEYS: Oppenlaender2022PromptModifiers; Steyerl2023MeanImages.\nTYPE: SOURCE-LED INFERENCE.\n\nCLAIM 4 — Corrective prompting can be downstream labor against upstream representational conditions.\nZETTELS: Z-AIACS-006; Z-RF-20260817-006; Z-RF-20260817-007.\nCITEKEYS: Rivas2025InexistentArchive.\nTYPE: COMPILER DISTINCTION (compensatory vs structural repair).\n\nCLAIM 5 — Interface action costs can shape creative trajectories before ranking effects are invoked.\nZETTELS: Z-AIACS-018; Z-RF-20260817-003.\nCITEKEYS: TorricelliEtAl2023Interface.\nTYPE: SOURCE-GROUNDED.\n\nCLAIM 6 — Description changes causal position when critical vocabulary becomes generative conditioning.\nZETTELS: Z-RF-20260818-018; Z-RF-20260818-015.\nCITEKEYS: Sontag1966AgainstInterpretation; Oppenlaender2022PromptModifiers; OppenlaenderEtAl2024BodyPrompting.\nTYPE: COMPILER SYNTHESIS.\n\nCLAIM 7 — Cultural feedback can alter future outputs without a model weight update.\nZETTELS: Z-AIACS-017; Z-RF-20260818-017.\nCITEKEYS: Oppenlaender2022PromptModifiers.\nTYPE: COMPILER FORMALIZATION.\n\nBOUNDARY\nThe paper does not claim that prompt practice is a formal language, that all AI art belongs to one cultural system, that all prompt lore is causally valid, or that observed associations between interface design and behavior prove a single causal mechanism.\n'''
(PKG/f'{paper_slug}__SOURCE_MAP.txt').write_text(source_map,encoding='utf-8')

making=f'''MAKING HISTORY — THE SHOP MAKES THE PROMPT\n\nCHECKPOINT: SLIPCASE-20260817-AIACS-01\nSCHEMA: SLIPCASE v15.55-AM\nDATE: 2026-08-17\nSTATUS: Working Paper · AI-augmented research process\n\nWHO\nResearcher: Watson Hartsoe\nAssembly model: GPT-5.6 Sol\n\nPROVIDED\n- User-provided AI Art as a Cultural System PDF.\n- User-provided Art as Cultural System & AI Prompting PDF.\n- User-provided Geertz’s Symbolic Anthropology and Art as Cultural System PDF.\n- PRIME ZETTEL FORAGE prompt.\n- SLIPCASE v15.55-AM assembly instrument.\n- Visible zettel field in the current conversation.\n\nPRESERVED\n- Three supplied PDFs as local resources.\n- Exact supplied prompt files from mounted uploads.\n- Forty zettel payloads reconstructed from visible conversation output and preserved as root TXT plus _MD mirrors.\n\nIMPORTANT PAYLOAD BOUNDARY\nNo machine-readable export of the full originating conversation was available. The 40 zettel payloads were reconstructed from the visible assistant messages in the active context rather than copied from an external transcript file. Their SHA-256 hashes identify the compiled payloads in this checkpoint; the run does NOT claim byte identity to an unavailable chat export.\n\nRETRIEVED\n- Public source PDFs from arXiv for Oppenlaender 2022, Oppenlaender/Linder/Silvennoinen 2023, Liu/Chilton 2021, Torricelli et al. 2023, Oppenlaender et al. 2024, and Simonen et al. 2025.\n- Public bibliographic/source landing pages for Geertz, Steyerl, Rivas, Maturana, Weizenbaum, and Sontag were checked on 2026-08-17.\n\nDERIVED\n- Complete relation graph from PLATFORM, LINKS, and all wikilinks in the compiled cards.\n- Ghost and backlink registry.\n- Four MOCs and a paper trail.\n- Bibliography and source/resource ledger.\n- Working paper: The Shop Makes the Prompt.\n- SOURCE_MAP, reader, network, printable cards, standalone replication capsule, mark, verification report, manifest, and ZIP.\n\nCONTROL\n- The paper title, argument, connective prose, MOCs, graph resolutions, and visual design were generated during assembly.\n- Source claims were limited to compiled evidence and verified source records.\n- The strongest wager selected from the field is that prompt expertise is learned diagnostic sensitivity to correctable differences, not simply mastery of a textual prompt language.\n\nUNVERIFIED\n- Human peer review.\n- Universal generality across current and future image models.\n- Causal validity of particular prompt folk theories absent controlled ablation.\n- Full reconstruction fidelity to any zettel text that existed outside the visible active conversation.\n'''
(PKG/'000__MAKING_HISTORY.txt').write_text(making,encoding='utf-8')
(PKG/f'{paper_slug}__MAKING_HISTORY.txt').write_text(making,encoding='utf-8')
assembly_appendix='''ASSEMBLY APPENDIX — THE SHOP MAKES THE PROMPT\n\nEXACT ASSEMBLY INSTRUMENT:\n  SLIPCASE_FINAL_PROMPT.txt\n  _PROMPTS/assembly_prompt__v15.55-AM.txt\n\nPRIOR FORAGE INSTRUMENT:\n  _PROMPTS/prime_zettel_forage__v3.0__prior.txt\n\nCLAIM TRACE:\n  the-shop-makes-the-prompt__SOURCE_MAP.txt\n\nRETURN / REBUILD:\n  000__RETURN_PATH.txt\n  000__REBUILD.txt\n  _SLIPCASE/VERIFICATION.txt\n\nThe exact assembly prompt is embedded in index.html and preserved verbatim in the package.\n'''
(PKG/f'{paper_slug}__ASSEMBLY_APPENDIX.txt').write_text(assembly_appendix,encoding='utf-8')

# mark
mark='''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round"><circle cx="31.5" cy="32" r="1.7" fill="currentColor" stroke="none"/><path d="M24 28c3.5-4 11.5-4 15 0"/><path d="M18 23c7-8 21-8 28 0" opacity=".72"/><path d="M13 18c10-12 29-12 39 0" opacity=".42"/><path d="M27.5 37.5c2.5 2 6 2 8.5-.2" opacity=".7"/></svg>'''
(PKG/'MARK.svg').write_text(mark,encoding='utf-8')

# ---------- compile paper through pandoc ----------
# paper header + build
header=r'''\usepackage{fontspec}
\usepackage{microtype}
\usepackage{geometry}
\usepackage{xcolor}
\usepackage{graphicx}
\usepackage{eso-pic}
\usepackage{hyperref}
\definecolor{quietgray}{gray}{0.55}
\AtBeginDocument{%
\AddToShipoutPictureFG*{%
  \put(36,22){\makebox[0pt][l]{\scriptsize\color{quietgray}Working Paper · AI-augmented research process}}%
  \put(560,18){\makebox[0pt][r]{\scriptsize\color{quietgray}$\circ\!\!\raisebox{1pt}{\scriptsize ))}$}}%
}}
\setlength{\parindent}{1.2em}
\setlength{\parskip}{0.35em}
'''
(PKG/'_SLIPCASE/paper_header.tex').write_text(header,encoding='utf-8')
cmd=['pandoc',f'{paper_slug}__{paper_date}.md','-f','markdown+raw_tex','-s','-t','latex','--citeproc',f'--bibliography=SLIPCASE-20260817-AIACS-01__references.bib','-o',f'{paper_slug}__{paper_date}.tex','-V','documentclass=article','-V','papersize=letter','-V','fontsize=11pt','-V','geometry:margin=1in','-V','mainfont=DejaVu Serif','-V','sansfont=DejaVu Sans','-V','monofont=DejaVu Sans Mono','-V','colorlinks=true','-V','linkcolor=black','-V','urlcolor=blue','-H','_SLIPCASE/paper_header.tex']
subprocess.run(cmd,cwd=PKG,check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
for _ in range(2):
    subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error',f'{paper_slug}__{paper_date}.tex'],cwd=PKG,check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

# ---------- network SVG / HTML ----------
try:
    import networkx as nx
    G=nx.Graph()
    for r in records:G.add_node(r['id'],kind='zettel',title=r['title'])
    for p in platforms:G.add_node('P:'+p,kind='platform',title=p)
    for g in ghosts:G.add_node('G:'+g,kind='ghost',title=g)
    for rel in relations:
        if rel['type'] not in ('LINKS_TO','MEMBER_OF'): continue
        a=rel['source']
        if rel['resolution']=='ZETTEL': b=rel['target']
        elif rel['resolution']=='PLATFORM': b='P:'+rel['target']
        else: b='G:'+rel['target']
        G.add_edge(a,b)
    pos=nx.spring_layout(G,seed=17,k=0.65,iterations=130)
except Exception:
    G=None;pos={r['id']:(i%8,i//8) for i,r in enumerate(records)}
# scale positions
all_nodes=list(pos)
xs=[pos[n][0] for n in all_nodes] or [0]; ys=[pos[n][1] for n in all_nodes] or [0]
def sx(x): return 40+(x-min(xs))/(max(xs)-min(xs)+1e-9)*1120
def sy(y): return 40+(y-min(ys))/(max(ys)-min(ys)+1e-9)*720
svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="800" viewBox="0 0 1200 800">','<rect width="100%" height="100%" fill="white"/>','<g stroke="#bbb" stroke-width="0.8">']
if G:
    for a,b in G.edges(): svg.append(f'<line x1="{sx(pos[a][0]):.1f}" y1="{sy(pos[a][1]):.1f}" x2="{sx(pos[b][0]):.1f}" y2="{sy(pos[b][1]):.1f}"/>')
svg.append('</g><g font-family="Arial, sans-serif">')
for n in all_nodes:
    kind=G.nodes[n].get('kind') if G else 'zettel'
    x,y=sx(pos[n][0]),sy(pos[n][1])
    radius=5 if kind=='zettel' else (3.6 if kind=='platform' else 2.5)
    fill='#111' if kind=='zettel' else ('#666' if kind=='platform' else '#bbb')
    svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{radius}" fill="{fill}"/>')
    if kind=='zettel': svg.append(f'<text x="{x+7:.1f}" y="{y+3:.1f}" font-size="7" fill="#333">{html.escape(n)}</text>')
svg.append('</g></svg>')
(PKG/'NETWORK.svg').write_text('\n'.join(svg),encoding='utf-8')
network_html='''<!doctype html><meta charset="utf-8"><title>Network</title><style>body{margin:0;font-family:system-ui;background:#fafafa}header{padding:14px 20px;border-bottom:1px solid #ddd;background:white;position:sticky;top:0}object{width:100%;height:calc(100vh - 55px)}</style><header><b>THE SHOP MAKES THE PROMPT</b> · complete field topology · zettels black · platforms gray · ghosts light</header><object data="NETWORK.svg" type="image/svg+xml"></object>'''
(PKG/'NETWORK.html').write_text(network_html,encoding='utf-8')

# ---------- reader ----------
compact=[{'id':r['id'],'title':r['title'],'source':r['source'],'platform':r['platform'],'links':r['links'],'backlinks':back.get(r['id'],[]),'payload':r['payload'],'filename':r['filename']} for r in records]
reader_data=json.dumps(compact,ensure_ascii=False).replace('</','<\\/')
reader_html=f'''<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>The Shop Makes the Prompt · Reader</title><style>
*{{box-sizing:border-box}} body{{margin:0;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;background:#f7f6f2;color:#171717;height:100vh;overflow:hidden}} .app{{display:grid;grid-template-columns:310px 1fr;height:100vh}} aside{{border-right:1px solid #bbb;background:#fff;display:flex;flex-direction:column;min-width:0}} header{{padding:15px;border-bottom:1px solid #ddd}} h1{{font:600 17px Georgia;margin:0 0 3px}} .muted{{font-size:11px;color:#666}} input{{width:100%;margin-top:10px;padding:9px;border:1px solid #aaa;background:white;font:12px monospace}} #list{{overflow:auto;flex:1}} .item{{padding:10px 13px;border-bottom:1px solid #eee;cursor:pointer}} .item:hover,.item.active{{background:#efeee9}} .id{{font-size:10px;color:#777}} .ttl{{font:600 13px Georgia;margin-top:3px}} main{{overflow:auto;padding:30px 4vw 80px}} .card{{max-width:900px;margin:auto;background:white;border:1px solid #ccc;padding:28px 34px;box-shadow:0 1px 8px #0000000b}} pre{{white-space:pre-wrap;font:13px/1.55 ui-monospace,monospace;margin:0}} .nav{{max-width:900px;margin:0 auto 12px;display:flex;gap:8px;flex-wrap:wrap}} button{{border:1px solid #aaa;background:white;padding:6px 9px;font:11px monospace;cursor:pointer}} @media(max-width:720px){{.app{{grid-template-columns:1fr}} aside{{position:absolute;z-index:3;width:86vw;height:100vh;transform:translateX(-100%);transition:.2s}} aside.open{{transform:translateX(0)}} main{{padding:16px}} .card{{padding:18px}} #menu{{display:inline-block!important}}}} #menu{{display:none}}
</style></head><body><div class="app"><aside id="side"><header><h1>The Shop Makes the Prompt</h1><div class="muted">40 cards · neighborhood-first research desk</div><input id="q" placeholder="search cards, sources, links"></header><div id="list"></div></aside><main><div class="nav"><button id="menu">DECK</button><button onclick="surprise()">SURPRISE</button><button onclick="copyCard()">COPY</button><button onclick="location.href='NETWORK.html'">GRAPH</button><button onclick="location.href='000__BIBLIOGRAPHY.html'">BIBLIOGRAPHY</button></div><div id="card" class="card"></div></main></div><script>
const cards={reader_data}; let current=cards[0]; const list=document.getElementById('list'), card=document.getElementById('card'), q=document.getElementById('q');
function renderList(a=cards){{list.innerHTML='';a.forEach(c=>{{let d=document.createElement('div');d.className='item'+(current&&c.id===current.id?' active':'');d.innerHTML='<div class="id">'+c.id+'</div><div class="ttl"></div>';d.querySelector('.ttl').textContent=c.title;d.onclick=()=>show(c);list.appendChild(d)}})}}
function linkify(s){{return s.replace(/\[\[([^\]]+)\]\]/g,(m,x)=>'<a href="#" data-link="'+x.replace(/"/g,'&quot;')+'">[['+x+']]</a>')}}
function show(c){{current=c;card.innerHTML='<pre>'+linkify(escapeHtml(c.payload))+'</pre>';history.replaceState(null,'','#'+encodeURIComponent(c.id));renderList(filter());document.querySelectorAll('[data-link]').forEach(a=>a.onclick=e=>{{e.preventDefault();let t=cards.find(z=>z.id===a.dataset.link);if(t)show(t);else alert('GHOST / external address: '+a.dataset.link)}});document.getElementById('side').classList.remove('open')}}
function escapeHtml(s){{return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}}
function filter(){{let x=q.value.toLowerCase();return cards.filter(c=>(c.id+' '+c.title+' '+c.source+' '+c.payload).toLowerCase().includes(x))}} q.oninput=()=>renderList(filter());
function surprise(){{show(cards[Math.floor(Math.random()*cards.length)])}} function copyCard(){{navigator.clipboard.writeText(current.payload)}}
document.getElementById('menu').onclick=()=>document.getElementById('side').classList.toggle('open'); let hash=decodeURIComponent(location.hash.slice(1));show(cards.find(c=>c.id===hash)||cards[0]);
</script></body></html>'''
(PKG/'READER.html').write_text(reader_html,encoding='utf-8')

# printable cards
cards_html=['<!doctype html><meta charset="utf-8"><title>Printable Cards</title><style>@page{size:4in 6in;margin:.25in}body{margin:0;font-family:Georgia}.c{break-after:page;width:3.5in;height:5.5in;overflow:hidden;padding:.15in}.id{font:8pt monospace;color:#666}.t{font:bold 15pt Georgia;margin:6pt 0 9pt}.b{font:8.1pt/1.18 monospace;white-space:pre-wrap}</style>']
for r in records: cards_html.append(f'<section class="c"><div class="id">{html.escape(r["id"])}</div><div class="t">{html.escape(r["title"])}</div><div class="b">{html.escape(r["payload"])}</div></section>')
(PKG/'CARDS.html').write_text('\n'.join(cards_html),encoding='utf-8')

# ---------- index / metadata texts before capsule ----------
start=f'''START HERE — SLIPCASE-20260817-AIACS-01\n\nTITLE: The Shop Makes the Prompt\nSUBTITLE: Cultural Competence, Reverse Description, and the Operational Life of AI Art\nRESEARCHER: Watson Hartsoe\nDATE: 2026-08-17\nSCHEMA: SLIPCASE v15.55-AM\n\nThis checkpoint compiles the current AI-art cultural-systems forage into 40 zettels: 20 initial pressure zettels, 11 source-led descendants, and 9 recursive descendants. The paper wager is that prompt expertise is not fundamentally mastery of a string or language but learned diagnostic sensitivity to correctable differences.\n\nBegin with the paper, then 000__MAP.txt, then READER.html.\n\nBOUNDARY: No machine-readable export of the full originating conversation was available. Zettel payloads were reconstructed from visible active-context assistant outputs; the package records this explicitly and does not claim byte identity to an unavailable chat transcript.\n'''
(PKG/'000__START_HERE.txt').write_text(start,encoding='utf-8')
return_path=f'''RETURN PATH\n\nCHECKPOINT: SLIPCASE-20260817-AIACS-01\nSCHEMA: SLIPCASE v15.55-AM\nPACKAGE: {PKG.name}\nRESEARCHER: Watson Hartsoe\nDATE: 2026-08-17\nREJOIN PHRASE: THE SHOP MAKES THE PROMPT\nASSEMBLY PROMPT: SLIPCASE_FINAL_PROMPT.txt\nPAPER: {paper_slug}__{paper_date}.pdf\nSOURCE MAP: {paper_slug}__SOURCE_MAP.txt\nBIBLIOGRAPHY: SLIPCASE-20260817-AIACS-01__references.bib\nREBUILD: 000__REBUILD.txt\n\nREJOIN: Provide index.html or this ZIP to a fresh context and say: THE SHOP MAKES THE PROMPT. Preserve compiled payload hashes before merging; do not silently rewrite reconstructed cards.\n'''
(PKG/'000__RETURN_PATH.txt').write_text(return_path,encoding='utf-8')
index_txt=f'''INDEX — SLIPCASE-20260817-AIACS-01\n\nPACKAGE: {PKG.name}\nZETTELS: {len(records)}\nPLATFORMS: {len(platforms)}\nGHOST LABELS: {len(ghosts)}\nRELATIONS: {len(relations)}\nRESOURCES REGISTERED: {len(resources)}\n\nPRIMARY ARTIFACTS\nindex.html — standalone replication capsule\nREADER.html — offline research desk\nNETWORK.html / NETWORK.svg — field topology\nCARDS.html — printable 4×6 cards\n000__MAP.txt — textual topology\n000__BIBLIOGRAPHY.txt / html — evidence ledger\n000__RESOURCES.txt — resources and link states\n000__OPEN_EDGES.txt — live research frontier\nSLIPCASE_FINAL_PROMPT.txt — exact assembly instrument\n{paper_slug}__{paper_date}.pdf — working paper\n{paper_slug}__SOURCE_MAP.txt — paper claim trace\n\nMACHINE STATE\n_SLIPCASE/MANIFEST.json\n_SLIPCASE/NODES.jsonl\n_SLIPCASE/RELATIONS.jsonl\n_SLIPCASE/RESOURCES.jsonl\n_SLIPCASE/APPEARANCES.jsonl\n_SLIPCASE/ALIASES.json\n_SLIPCASE/VERIFICATION.txt\n'''
(PKG/'000__INDEX.txt').write_text(index_txt,encoding='utf-8')
rebuild=f'''REBUILD — SLIPCASE-20260817-AIACS-01\n\n1. Treat every root zettel TXT as evidence payload. Do not edit in place.\n2. Verify each _MD mirror is byte-identical to its root TXT counterpart.\n3. Parse ID, SOURCE, PLATFORM, LINKS, every [[ADDRESS]], and BIBTEX from payloads.\n4. Resolve exact zettel IDs first; unresolved addresses remain GHOSTS. Never fuzzy-merge.\n5. Regenerate ZETTELS.json/jsonl, NODES, RELATIONS, backlinks, MAP, MOCs, reader, network, and cards.\n6. Compile the paper with the bibliography, then verify every paper citekey exists in the .bib.\n7. Preserve the exact assembly instrument in SLIPCASE_FINAL_PROMPT.txt and _PROMPTS/.\n8. Recompute SHA-256 for every file and write a new MANIFEST.\n9. Render the PDF and inspect pages.\n10. Zip the root contents and test the archive.\n\nCURRENT PAPER BUILD\npandoc {paper_slug}__{paper_date}.md -f markdown+raw_tex -s -t latex --citeproc --bibliography=SLIPCASE-20260817-AIACS-01__references.bib -o {paper_slug}__{paper_date}.tex -V documentclass=article -V papersize=letter -V fontsize=11pt -V geometry:margin=1in -V mainfont='DejaVu Serif' -H _SLIPCASE/paper_header.tex\nxelatex -interaction=nonstopmode -halt-on-error {paper_slug}__{paper_date}.tex\nxelatex -interaction=nonstopmode -halt-on-error {paper_slug}__{paper_date}.tex\n'''
(PKG/'000__REBUILD.txt').write_text(rebuild,encoding='utf-8')

# ghosts report
from collections import defaultdict
inbound=defaultdict(list)
for rel in relations:
    if rel['resolution']=='GHOST' and rel['type']=='LINKS_TO': inbound[rel['target']].append(rel['source'])
ghosttxt=['GHOSTS — OPEN INTELLECTUAL ADDRESSES','']
for g in ghosts: ghosttxt.append(f"[[{g}]] · inbound explicit LINKS: {', '.join(sorted(set(inbound[g]))) or 'none'}")
(PKG/'_SLIPCASE/GHOSTS.txt').write_text('\n'.join(ghosttxt)+'\n',encoding='utf-8')

# standalone capsule -- embed all text files and PDFs as base64 downloads
embed={}
for p in PKG.rglob('*'):
    if not p.is_file() or p.name=='index.html': continue
    rel=str(p.relative_to(PKG))
    # omit temporary latex auxiliaries from capsule
    if p.suffix in ('.aux','.log','.out','.bcf','.run.xml'): continue
    data=p.read_bytes()
    if p.suffix.lower() in ('.txt','.md','.json','.jsonl','.html','.svg','.tex','.bib','.poml'):
        try: embed[rel]={'encoding':'utf8','data':data.decode('utf-8'),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)}
        except: embed[rel]={'encoding':'base64','data':base64.b64encode(data).decode(),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)}
    elif p.suffix.lower()=='.pdf':
        embed[rel]={'encoding':'base64','data':base64.b64encode(data).decode(),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'mime':'application/pdf'}

capsule_json=json.dumps(embed,ensure_ascii=False).replace('</','<\\/')
index_html=f'''<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>The Shop Makes the Prompt · Slipcase</title><style>
*{{box-sizing:border-box}}body{{margin:0;background:#f3f1eb;color:#171717;font-family:Georgia,serif}}header{{padding:32px max(24px,5vw) 22px;background:#fff;border-bottom:1px solid #bbb}}h1{{font-size:34px;margin:0 0 7px;letter-spacing:-.02em}}.sub{{font-size:17px;color:#444}}.status{{font:11px ui-monospace,monospace;margin-top:13px;color:#666}}nav{{display:flex;gap:6px;flex-wrap:wrap;margin-top:18px}}button{{font:11px ui-monospace,monospace;background:#fff;border:1px solid #aaa;padding:7px 10px;cursor:pointer}}main{{max-width:1180px;margin:auto;padding:28px max(20px,4vw) 80px}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px}}.panel{{background:#fff;border:1px solid #c8c5bd;padding:18px;min-height:120px}}h2{{font-size:18px;margin:0 0 10px}}.metric{{font:28px ui-monospace,monospace}}.tiny{{font:11px/1.5 ui-monospace,monospace;color:#666}}#cards .card{{cursor:pointer}}#cards .card:hover{{border-color:#222}}pre{{font:12px/1.5 ui-monospace,monospace;white-space:pre-wrap}}dialog{{width:min(900px,94vw);height:min(84vh,900px);border:1px solid #888;padding:0}}dialog header{{padding:12px 15px;position:sticky;top:0}}dialog pre{{padding:20px;overflow:auto;height:calc(100% - 55px);margin:0}}a{{color:#184a7a}}.mark{{position:fixed;right:15px;bottom:12px;width:27px;opacity:.35}}</style></head><body><header><h1>The Shop Makes the Prompt</h1><div class="sub">Cultural Competence, Reverse Description, and the Operational Life of AI Art</div><div class="status">Working Paper · AI-augmented research process · SLIPCASE-20260817-AIACS-01 · evidence, prompts, and making history preserved</div><nav><button onclick="downloadFile('{paper_slug}__{paper_date}.pdf')">PAPER PDF</button><button onclick="openText('000__MAP.txt')">MAP</button><button onclick="openText('000__OPEN_EDGES.txt')">OPEN EDGES</button><button onclick="openText('000__BIBLIOGRAPHY.txt')">BIBLIOGRAPHY</button><button onclick="openText('000__MAKING_HISTORY.txt')">MAKING HISTORY</button><button onclick="openText('SLIPCASE_FINAL_PROMPT.txt')">ASSEMBLY PROMPT</button><button onclick="openText('000__REBUILD.txt')">REBUILD</button></nav></header><main><section class="grid"><div class="panel"><h2>Zettels</h2><div class="metric">{len(records)}</div><div class="tiny">20 initial pressure cards · 11 source-led descendants · 9 recursive descendants</div></div><div class="panel"><h2>Relations</h2><div class="metric">{len(relations)}</div><div class="tiny">native PLATFORM/LINKS/wikilinks plus derived backlinks</div></div><div class="panel"><h2>Ghosts</h2><div class="metric">{len(ghosts)}</div><div class="tiny">unresolved intellectual addresses preserved rather than fuzzy-matched</div></div><div class="panel"><h2>Paper wager</h2><div class="tiny">Prompt expertise is learned diagnostic sensitivity to correctable differences, not merely mastery of a textual string.</div></div></section><h2 style="margin-top:28px">Deck</h2><div id="cards" class="grid"></div><h2 style="margin-top:28px">Embedded resources</h2><div id="files" class="grid"></div></main><img class="mark" src="data:image/svg+xml;base64,{base64.b64encode(mark.encode()).decode()}" alt=""><dialog id="dlg"><header><b id="dt"></b> <button style="float:right" onclick="dlg.close()">CLOSE</button></header><pre id="dp"></pre></dialog><script>
const deck={json.dumps(compact,ensure_ascii=False).replace('</','<\\/')}; const files={capsule_json}; const dlg=document.getElementById('dlg'); const dt=document.getElementById('dt'),dp=document.getElementById('dp');
function openCard(c){{dt.textContent=c.id+' · '+c.title;dp.textContent=c.payload;dlg.showModal()}} function openText(p){{let x=files[p];if(!x)return alert('not embedded');dt.textContent=p;dp.textContent=x.encoding==='utf8'?x.data:'[binary file · '+x.bytes+' bytes]';dlg.showModal()}}
function bytesFor(x){{if(x.encoding==='utf8')return new TextEncoder().encode(x.data);let b=atob(x.data),u=new Uint8Array(b.length);for(let i=0;i<b.length;i++)u[i]=b.charCodeAt(i);return u}}
function downloadFile(p){{let x=files[p];if(!x)return alert('not embedded');let blob=new Blob([bytesFor(x)],{{type:x.mime||'application/octet-stream'}});let a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=p.split('/').pop();a.click();setTimeout(()=>URL.revokeObjectURL(a.href),2000)}}
const cards=document.getElementById('cards');deck.forEach(c=>{{let d=document.createElement('div');d.className='panel card';d.innerHTML='<div class="tiny">'+c.id+'</div><h2></h2><div class="tiny"></div>';d.querySelector('h2').textContent=c.title;d.querySelectorAll('.tiny')[1].textContent=c.source;d.onclick=()=>openCard(c);cards.appendChild(d)}});
const fl=document.getElementById('files');Object.keys(files).filter(p=>p.startsWith('_RESOURCES/')||p.startsWith('_PROMPTS/')).sort().forEach(p=>{{let x=files[p],d=document.createElement('div');d.className='panel';d.innerHTML='<div class="tiny"></div><h2></h2><button>DOWNLOAD</button>';d.querySelector('.tiny').textContent=x.bytes+' bytes · '+x.sha256.slice(0,12);d.querySelector('h2').textContent=p;d.querySelector('button').onclick=()=>downloadFile(p);fl.appendChild(d)}})
</script></body></html>'''
(PKG/'index.html').write_text(index_html,encoding='utf-8')

# save script source for intentional reconstruction
shutil.copy('/tmp/build_aiacs.py',PKG/'_SLIPCASE/rebuild_compiler.py')
