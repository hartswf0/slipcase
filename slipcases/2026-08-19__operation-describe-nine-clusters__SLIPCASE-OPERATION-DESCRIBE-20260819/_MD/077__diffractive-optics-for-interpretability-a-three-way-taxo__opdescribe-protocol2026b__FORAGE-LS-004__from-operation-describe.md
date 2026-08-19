ZETTEL

ID: FORAGE-LS-004

TITLE: Diffractive optics for interpretability: a three-way taxonomy of XAI as refraction, reflection, diffraction

SOURCE: LATENT SPACE/Operative Ethnography Protocol Design.md — "Diffractive Optics in Algorithmic Observation"

PASSAGE: [QUOTE] "Refractive methods, such as Layer-wise Relevance Propagation (LRP) or saliency maps, treat algorithmic meaning as an objective, traceable path that can be highlighted. Reflective methods, such as local surrogate models (like LIME or SHAP values), acknowledge their own limitations, admitting they act as a somewhat distorted mirror of the model's true logic, but they still pursue a singular reflection." [QUOTE] "Applied to operative ethnography, a diffractive approach maps the effects of differences, contradictions, and systemic interferences. The diffractive ethnographer deliberately stages multiple, potentially contrasting explanations and prompts, observing the rich interference patterns generated when different datasets, human perspectives, XAI tools, and algorithmic biases collide within the interface." [QUOTE] "This approach enthusiastically embraces incommensurability."

RESEARCH OBJECT: The optical metaphors governing model interpretability methods, and a proposed methodological successor.

LOCAL MOVE: Sorts the entire XAI toolbox into two failure modes of a single metaphor (light passing through / bouncing off a truth) and proposes wave-interference as the replacement: study disagreement between instruments as the datum itself.

SOURCE TERMS: diffraction; refractive methods; reflective methods; interference patterns; incommensurability; LRP; saliency maps; LIME; SHAP; probing heads.

WHAT BECAME STRANGE: Contradiction between explanation tools stops being an embarrassment to resolve and becomes the primary empirical signal — disagreement is data.

QUESTION: What is the diffraction-analog of a measurable interference fringe — is there a quantitative statistic for "interference pattern" between two explanations?

DEEPER QUESTION: If incommensurability is embraced, what stops diffractive analysis from being unfalsifiable — able to absorb any result as another interesting interference?

MECHANISM: Stage k contrasting apparatuses (prompts, probes, XAI tools) over the same latent region → collect the pattern of agreements/contradictions → read the pattern as a map of the sociotechnical configuration rather than adjudicating one true explanation.

FORMAL SHIFT: From explanation as a function f(model) → account, to explanation as a relation over pairs of apparatuses: the object of study becomes the disagreement structure.

SOURCE FORMALISM: The reflection/refraction/diffraction triad borrowed from Barad and Haraway's optics vocabulary; the representationalism-vs-agential-realism table.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Given apparatuses A1..Ak and outputs E1..Ek, define D(i,j) = divergence(Ei, Ej); diffractive analysis studies the matrix D and its dependence on apparatus design, not any single Ei.

TENSION: Rival readings: (a) diffraction is a genuinely new protocol; (b) it re-describes existing ensemble/robustness practices in interpretability (probe-disagreement studies) with STS vocabulary. The file claims novelty but cites the same XAI tools it critiques.

MISSING: A worked example with real interference data; any stopping rule; the quantitative statistic the metaphor promises.

BOUNDARY: A methodology claim about how to study models, not a claim about model internals.

CITATION TRAIL: Barad (diffraction, via Haraway); XAI literature (LRP, saliency, LIME, SHAP); synthetic ethnography (de Seta et al.).

TEST: Checkable core: "when multiple probing heads yield contradictory mappings of a single latent space" — probe-disagreement frequency and structure is measurable today; whether mapping it yields ethnographic insight beyond standard robustness analysis is the open empirical bet.

PLATFORM: Interpretability pipelines over LLMs and generative models.

LINKS: [[FORAGE-LS-003]], [[FORAGE-LS-005]]

BIBTEX:
@unpublished{opdescribe_protocol2026b,
  title = {Operative Ethnography Protocol Design},
  note = {Repo file, OPERATION-DESCRIBE archive, LATENT SPACE/Operative Ethnography Protocol Design.md, dated 2026-04-20},
  year = {2026}
}
@book{barad2007meeting_b,
  author = {Barad, Karen},
  title = {Meeting the Universe Halfway: Quantum Physics and the Entanglement of Matter and Meaning},
  publisher = {Duke University Press},
  address = {Durham, NC},
  year = {2007}
}
