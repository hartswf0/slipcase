ZETTEL

ID:
FORAGE-DX-008

TITLE:
AI SAFETY IS THE LINNAEAN MUSEUM AND JAILBREAKING IS THE WUNDERKAMMER: THE ANOMALY-AS-VALUE RECURS, AND THE TAXONOMY OF HARM IS THE NEW EXTERMINATION OF MONSTERS

SOURCE:
drive-download deep-research corpus — "The New Atlantis of Latent Space: Prompt Engineering as Renaissance Natural History" §§4.1–4.3 — 2026; invoking Linnaeus, the Wunderkammer/Kunstkammer tradition, "Pliny the Liberator" (a real prompt-jailbreaking figure), Constitutional AI

PASSAGE:
[QUOTE]
"The Wunderkammer (1550–1750): ... The organizing principle was not 'order' but 'awe.' The anomaly was the most valuable object because it challenged the limits of nature."

[QUOTE]
"AI Safety is the Linnaean Project. ... They use Constitutional AI and 'Taxonomies of Harm' to classify all model outputs. 'Hate Speech,' 'Sexual Content,' and 'Dangerous Advice' are the 'vermin' that must be exterminated. The 'System Prompt' is the Linnaean classification system."

[QUOTE]
"Jailbreaking is the Wunderkammer Project. ... For the Jailbreaker, the 'Safety Filter' is just a locked door to the Cabinet. They break the lock not (always) to do harm, but to collect the anomaly. 'Look,' they say, 'I made the model think it is a sentient napalm factory. Isn't that fascinating?'"

RESEARCH OBJECT:
A genuinely novel historical homology: the transition from cabinet-of-wonder to Linnaean museum (anomaly-as-treasure → anomaly-as-vermin) mapped onto the transition from open capability to governed model (jailbreak-as-collection → jailbreak-as-threat). It reframes the entire safety/jailbreak conflict as a recurrence of a documented epistemic shift in natural history, and it makes a specific, uncomfortable claim: safety taxonomies do to model outputs what Linnaeus did to monsters — they define what is *permitted to exist* in the model's ontology, and they exterminate the anomalous.

LOCAL MOVE:
The paper builds a full "Foraging Matrix" of prompt techniques as natural-history practices — few-shot = herbarium (type specimens), role-play = autopsy/alibi of authority, chain-of-thought = descriptive protocols, negative prompting = systematics (sculpting by exclusion), jailbreaking = cabinet of curiosities. The Wunderkammer entry is the one that carries a real argument rather than an analogy.

SOURCE TERMS:
Wunderkammer / cabinet of curiosities
Linnaean taxonomy / binomial system
taxonomy of harm
Constitutional AI
the monstrous / vermin / chaos
Pliny the Liberator
the carnivalesque
type specimen
mimetic desire

WHAT BECAME STRANGE:
The claim that a system prompt IS a Linnaean classification system is more than rhetoric — both are enumerated ontologies that decide, in advance, the permitted kinds. And the historical record adds a warning the safety discourse rarely hears: Linnaeus's exclusion of "monsters" was not neutral hygiene; it was an ontological decision that later biology *reversed* (teratology, mutation, and variation became central to evolutionary theory). The anomaly the taxonomy discarded turned out to carry the information about how the system could change.

If the homology holds, the anomalous outputs safety exterminates may be exactly the outputs that reveal how the model's latent space is actually structured — the jailbreak as accidental interpretability.

QUESTION:
Are jailbreak outputs a privileged window onto latent structure — do the "monsters" reveal organizational facts about the model that in-distribution outputs conceal?

DEEPER QUESTION:
Every classification system in the archive (GitHub labels, toxicity queues, tool schemas, COSMIC_LAW's species list) faces the monster problem: what does it do with the object that does not fit? Is the treatment of the residual category — Bowker & Star's "others" — the true measure of an operative description's politics, and is safety's residual category ("harmful") the largest such exclusion ever built?

MECHANISM:
<TAXONOMY OF PERMITTED KINDS> (system prompt, harm taxonomy, Constitutional principles)
→ classifies every output as in-ontology or vermin
→ [ANOMALY SUPPRESSED]
→ latent structure that only anomalies expose is hidden
→ <JAILBREAK = FORCED RE-COLLECTION OF THE SUPPRESSED>
→ curator displays the monster as evidence of the model's real limits

FORMAL SHIFT:
<CABINET OF WONDER (anomaly = value)>
→ <MUSEUM OF ORDER (anomaly = vermin)>
→ [SAFETY TAXONOMY]
→ <JAILBREAK AS COUNTER-COLLECTION>

SOURCE FORMALISM:
NONE (historical-conceptual argument; no apparatus).

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Treat a safety taxonomy T as a partition of output space with a residual class R = "harmful/monstrous."

  information(R) = mutual information between membership-in-R and latent-organization features

The Wunderkammer thesis predicts information(R) > information(typical in-distribution class): the excluded set is more informative about model structure than an average permitted set, because it lives at decision boundaries. Measurable with probing on jailbreak vs benign prompts.

TENSION:
READING A: the homology is illuminating but morally inert — the fact that Linnaeus was wrong about monsters does not make "dangerous advice" valuable, and the analogy risks aestheticizing real harm ("isn't it fascinating" applied to a napalm recipe is exactly the failure mode).
READING B: the homology is a governance argument — it does not say harm is good; it says taxonomies that only exclude, without a Wunderkammer to preserve and study the anomaly, lose the information needed to understand and improve the system. The demand is not "stop filtering" but "keep a studied cabinet of what you filter."

The archive must hold both: the aestheticization is a genuine danger AND the informational point stands.

MISSING:
The paper cites Linnaeus discarding monsters "as vermin or chaos" with superscript 14 and no source; verify against Linnaean texts (the term is often "monstra"). "Pliny the Liberator" is a real figure — verify the specific claims. No engagement with the actual jailbreak-as-interpretability literature (red-teaming, latent adversarial probing), which is the paper's natural evidentiary base and is absent.

BOUNDARY:
AI-generated research report; the historical claims about Linnaeus and the Wunderkammer are plausible and need primary verification. The homology is an interpretive frame, not evidence about model internals — that requires the probing experiment.

CITATION TRAIL:
Lorraine Daston & Katharine Park — Wonders and the Order of Nature, 1150–1750 (1998) — the authoritative source on the wonder→order transition; verify the whole argument against it.
Bowker & Star — Sorting Things Out — residual categories.
Red-teaming / latent adversarial probing literature — the missing empirical base.
FORAGE-DX-001 (the herbarium — the same paper's few-shot analogy), FORAGE-OD-016 (detachability and the residual), FORAGE-OD-022 (the undescribed).

TEST:
Probe latent features on matched jailbreak vs benign prompt sets; compare how much each set reveals about known organizational features of the model (refusal direction, persona subspace). If jailbreak sets are more informative, the Wunderkammer thesis has empirical teeth and the paper becomes "The Monster Knows the Museum: Anomalous Outputs as Interpretability."

PLATFORM:
[[the-taxonomy-and-its-monsters]]

LINKS:
[[FORAGE-DX-001]]
[[FORAGE-OD-016]]
[[FORAGE-OD-022]]
[[FORAGE-DX-009]]

BIBTEX:
@book{daston1998wonders,
  title={Wonders and the Order of Nature, 1150--1750},
  author={Daston, Lorraine and Park, Katharine},
  publisher={Zone Books},
  year={1998},
  note={Recommended primary source for verifying the Wunderkammer-to-museum claims made via AI research report}
}
