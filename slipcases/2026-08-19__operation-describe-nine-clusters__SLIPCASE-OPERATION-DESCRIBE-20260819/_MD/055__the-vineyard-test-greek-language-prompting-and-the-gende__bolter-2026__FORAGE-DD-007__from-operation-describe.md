ZETTEL

ID: FORAGE-DD-007

TITLE: The vineyard test: Greek-language prompting and the gendered divergence of platform defaults

SOURCE: 00_PLIMSOLL-LINE/portugal-draft.md (§ The shield and the natural sign, Figs. 1–5 experiment); earlier single-model version in Dry-Dock/BULKHEAD-05_shield-natural-sign.md; Homeric source text in Dry-Dock/HOLD copy/a-source.md (Buckley translation, Il. 18.561–572)

PASSAGE: [QUOTE] "Our prompt was: 'Create the shield described below. Make the image as faithful and detailed as possible', and we included in the prompt the entire Homeric passage (Book 18, lines 478–608) in the original Greek. The model had no trouble with the Greek." [QUOTE] "Gemini produced a representation in linear perspective and a style reminiscent of an illustrated children's book of the mid-twentieth century. It looks like an illustration of a child's version of the Bible." [QUOTE] "It is interesting that ChatGPT chose to represent only young women with the exception of lyre-playing young man, although the text specifies individuals of both sexes. The figures in the Gemini version are boys and girls, whereas the ChatGPT version gives us significantly older female figures. The style in ChatGPT does not recall an illustration from a child's Bible, but perhaps the academic neoclassism of the nineteenth century." [QUOTE from the Homeric source being tested, Buckley trans.] "Young virgins and youths, of tender minds, carried the sweet fruit in woven baskets. In the midst of them a boy played pleasantly on a shrill lyre, and sung the beautiful Linus song with a slender voice."

RESEARCH OBJECT: A small but genuine empirical protocol: (1) prompting with the untranslated ancient Greek of Il. 18 as the entire prompt body — testing whether operative ekphrasis works across a 2,700-year language gap; (2) a controlled cross-platform comparison of one scene (the vineyard, 18.561–572) revealing that models diverge in gender and age rendering AGAINST the explicit text ("the text specifies individuals of both sexes"), and diverge in period-style attractors (mid-century children's Bible vs. nineteenth-century academic neoclassicism).

LOCAL MOVE: Use Homer as a bias probe: because the source text's content is philologically fixed, every deviation in the output is attributable to the platform's archive, not to prompt ambiguity — the ekphrastic classic becomes a calibrated instrument for measuring platform defaults.

SOURCE TERMS: faithful and detailed (the prompt formula); logic of immersion; linear perspective; iteration as "the most common method of thickening a prompt"; platform realism.

WHAT BECAME STRANGE: Fidelity failure is demographically patterned: the models do not fail randomly against the Greek — they fail toward culturally sedimented casting conventions (women harvesting, a single male musician), i.e., the archive rewrites Homer's social world in its own image.

QUESTION: Which layer produced the gender substitution — the Greek-to-latent encoding, the image prior for "vineyard harvest," or a platform-level aesthetic filter?

DEEPER QUESTION: When a model "has no trouble with the Greek" but silently mis-genders the scene, is that a translation error or a worldmaking decision — and does the difference matter once images become worlds one can enter?

MECHANISM: Full Homeric passage in Greek → multimodal encoding → whole-shield render (bronze object, scenes embossed); scene-level prompt → immersive render in the platform's period-style attractor; ChatGPT required a second corrective prompt ("Make the scene in a realistic style using linear perspective. That is, take us into the scene.") which "maintained almost exactly the same composition, but with a more painterly style" — composition is stickier than style under iteration.

FORMAL SHIFT: From evaluating outputs by beauty or plausibility to evaluating them by philological fidelity — a ground-truth text turns aesthetics into measurement.

SOURCE FORMALISM: The two-prompt protocol (whole shield vs. single scene; Greek passage as payload); Figs. 1–5 as the evidence series.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Fidelity vector F(output) over checkable text facts (entity counts, genders, ages, objects, actions from Il. 18.561–572); bias(platform) = systematic component of 1−F across runs; style attractor = modal art-historical period label assigned by independent raters.

TENSION: READING A (the draft's framing): the experiment illustrates platform realism — a stylistic finding. READING B (latent in the data, never stated): the gender substitution is an affordance-politics finding of exactly the kind SYNTH-03 theorizes ("women outside ceremony" as what the grammar renders unthinkable) — yet the draft never connects its own empirical observation to Watson's political argument, and the political section that could have received it was cut.

MISSING: Run counts, seeds, dates, and the images themselves; a translation-control condition (same passage in English) to separate language effects from scene priors; the connection to SYNTH-03's bias framework.

BOUNDARY: Two platforms, one scene, single-digit runs — an anecdotal protocol the paper itself calls "a test," not a study.

CITATION TRAIL: Homer, Iliad 18.478–608 (Buckley 1851 trans. in HOLD copy/a-source.md; Greek text used in prompts) → Meyer 2025 → Steyerl 2023 → Hintze et al. 2026.

TEST: Preregistered replication: n runs per platform per condition (Greek vs. English), code outputs for gender/age/count fidelity; the draft's claim predicts stable platform-specific demographic signatures.

PLATFORM: Gemini 3 Flash Image; ChatGPT Images 2.0.

LINKS: [[FORAGE-DD-006]] [[FORAGE-DD-013]] [[FORAGE-DD-002]] [[FORAGE-DD-011]]

BIBTEX: @unpublished{bolter2026portugal, author={Hartsoe, Watson and Bolter, Jay David}, title={From Imagetext to Worldtext: Generative AI as Operative Ekphrasis}, note={Draft, OPERATION-DESCRIBE repository, Dry-Dock/00\_PLIMSOLL-LINE/portugal-draft.md}, year={2026}}
