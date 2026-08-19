ZETTEL

ID:
FORAGE-OD-030

TITLE:
CLASSICAL RHETORIC ALREADY SUPPLIED A HUMAN-SUBJECT TEST FOR DESCRIPTIVE POWER AND THE ARCHIVE USES ENARGEIA ONLY AS AN ADJECTIVE

SOURCE:
Watson Hartsoe — PAPERS/seed-candidates-ch02.md (ancestral_thinkers, key_vocabularies) and PAPERS/imagetext-to-worldtext-clean.md §2.1 "The Ancient Definition" — 2026, invoking Ruth Webb, Ekphrasis, Imagination and Persuasion in Ancient Rhetorical Theory and Practice (2009)

PASSAGE:
[QUOTE]
seed-candidates-ch02.md:
"The ancient definition of ekphrasis was a verbal description producing a vivid visual experience (enargeia)."

[QUOTE]
seed-candidates-ch02.md, first_questions:
"What is the relationship between enargeia and prompt quality?"

RESEARCH OBJECT:
Enargeia is not a property of a text. In the rhetorical tradition it is defined by an *effect on an audience* — the hearer is brought to the condition of a spectator.

That is an operational criterion with a measurement procedure built in: ask the audience what they saw. The archive invokes enargeia repeatedly and never once uses it as a test.

LOCAL MOVE:
The archive treats enargeia as historical legitimation for the claim that description generates. It positions the term genealogically (Homer → Webb → CLIP) rather than methodologically.

SOURCE TERMS:
enargeia
phantasia
sapheneia
vivid visual experience
bringing before the eyes
the hearer becomes a spectator
descriptive struggle

WHAT BECAME STRANGE:
The archive has an evaluation problem it never states: how do you tell a good prompt from a bad one, other than by whether the author accepted the output?

Its whole practice-based method rests on `revision_decision: accept / reject / revise / fork` — the author's own judgment, unblinded, with no external criterion. That is precisely the "inward adequacy vs public criteria" tension its Ryle chapter identifies as the central problem of descriptive adequacy (PAPERS/ryl-01.md, on Murdoch's descriptive struggle against Ryle's public criteria).

The classical tradition solved the same problem with a public criterion, two thousand years earlier: report from the audience.

QUESTION:
Can prompt quality be measured by an enargeia protocol — the audience's report of what they saw — rather than by output inspection or author acceptance?

DEEPER QUESTION:
If enargeia is measured on the *audience of the description* rather than on the generated image, then the object of evaluation shifts from the artifact to the reader's constructed scene — and a prompt could score high while its image scores low, or vice versa. That divergence, if it exists, is a finding about the difference between routing a human and routing a model.

MECHANISM:
Classical protocol:
<DESCRIPTION READ ALOUD>
→ hearer constructs phantasia
→ [HEARER REPORTS WHAT THEY SAW]
→ vividness, specificity, and agreement across hearers are scored
→ <ENARGEIA MEASURED>

Modern parallel available immediately:
<PROMPT>
→ given to human readers *and* to a model
→ [BOTH PRODUCE A SCENE: verbal report vs generated image]
→ compare specificity and inter-rater agreement across the two operator types
→ <DIVERGENCE MEASURED>

FORMAL SHIFT:
<DESCRIPTION>
→ <TWO OPERATOR TYPES: HUMAN, MODEL>
→ [EACH CONSTRUCTS A SCENE]
→ <AGREEMENT / DIVERGENCE AS A MEASURE OF THE DESCRIPTION>

SOURCE FORMALISM:
NONE. Webb's account is historical and interpretive. The measurement procedure is latent in the ancient criterion, not stated as a method.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

For a description D and a population of operators:

  specificity(D)  = mean detail count in reported scenes
  concordance(D)  = inter-operator agreement on reported details
  enargeia(D)     = specificity × concordance

Then the interesting quantity is cross-substrate:

  divergence(D) = concordance(D | humans) − concordance(D | model samples)

A prompt with high human concordance and low model concordance is one the model does not read as we do. That is a direct, cheap, quantitative probe of the archive's central claim about latent viscosity — and it needs no model internals, no API privileges, and no proprietary logs.

TENSION:
READING A: human reports and model outputs are not comparable measurements; asking readers what they saw measures reading, not generation.
READING B: that is the point. The archive claims description does the same work on human and machine operators (attention-tax §13: "Interface Design = Prompting for human operators"). If the claim is true, concordance should track across substrates. If it does not, the unification fails and the failure is measured.

MISSING:
Any human-subject component anywhere in the archive. Its ethics section (label-01 §14) is about sandboxing models and anonymizing scraped data; it does not contemplate running readers.

An enargeia protocol would be the archive's first human-subject study and its cheapest.

BOUNDARY:
Webb reconstructs ancient theory and practice; she does not propose a measurement instrument. The protocol here is our construction from the criterion, and calling it "the classical test" would overstate the source.

CITATION TRAIL:
Ruth Webb — Ekphrasis, Imagination and Persuasion (2009) — locate the passages on the hearer becoming a spectator.
Quintilian on phantasia; the progymnasmata's ekphrasis exercises, which include evaluation criteria.
PAPERS/ryl-01.md on Murdoch's descriptive struggle vs Ryle's public criteria — the archive's own framing of this exact problem.
FORAGE-OD-005, FORAGE-OD-018.

TEST:
Twelve prompts, twenty readers, one instruction: read the prompt, then list every visual detail you are confident the described scene contains.

Score concordance. Generate images from the same prompts and score concordance across samples. Plot human concordance against model concordance.

Any prompt far from the diagonal is a case where description routes the two substrates differently, and each such prompt is a paper.

PLATFORM:
[[enargeia-as-an-instrument]]

LINKS:
[[FORAGE-OD-018]]
[[FORAGE-OD-005]]
[[FORAGE-OD-016]]

BIBTEX:
@book{webb2009ekphrasis,
  title={Ekphrasis, Imagination and Persuasion in Ancient Rhetorical Theory and Practice},
  author={Webb, Ruth},
  publisher={Ashgate},
  year={2009}
}
