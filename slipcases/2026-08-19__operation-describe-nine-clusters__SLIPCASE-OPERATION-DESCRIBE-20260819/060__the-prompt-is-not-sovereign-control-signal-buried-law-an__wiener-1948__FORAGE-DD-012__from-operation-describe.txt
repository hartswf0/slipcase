ZETTEL

ID: FORAGE-DD-012

TITLE: The prompt is not sovereign: control signal, buried law, and the constitution of the worldtext

SOURCE: Dry-Dock/BULKHEAD-06_shield-as-worldtext.md (Part B, closing paragraphs); Dry-Dock/watson-shield-as-worldtext.md (Blacksmith typescript); KEEL BLOCKS/SYNTH-02_shield-as-world-model.md; KEEL BLOCKS/deep-research-report (17).md (initialization-vector argument)

PASSAGE: [QUOTE] "System prompt and user prompt together form the constitution of the worldtext. A system prompt is a buried law; the user prompt is only the visible petition. The prompt functions not as a sovereign command but as a control signal (cf. Wiener 1948) — one regulatory input among many, collaborating with training data, safety filters, physics engines, and procedural rules. Worldtext names this hanging-together." [QUOTE, Jay's parallel in portugal-draft] "Even if the user or player provides only a short verbal prompt ... the generator depends on elaborate unseen system prompts that provide context to guide and constrain the model." [PARAPHRASE] SYNTH-02 adds the reclassification: "The prompt is therefore better theorized as initialization than as artwork ... the prompt is the initialization vector. The initial image is not the terminal object. It is a readout of how the world has been parameterized before it is entered." watson-conclusion.md records the later demotion of "initialization vector" as "jargon with no argumentative payoff."

RESEARCH OBJECT: A political theory of the prompt in three figures: (1) cybernetic — the prompt as one control signal among many regulatory inputs (Wiener), demoting user intention from authorship to regulation; (2) juridical — system prompt as buried law vs. user prompt as visible petition, importing constitutional structure (hidden higher-order norms governing visible speech acts) into interface analysis; (3) computational — prompt as initialization vector parameterizing a process rather than specifying a product. "Worldtext" is then defined not as a text-plus-world but as the HANGING-TOGETHER of all regulatory inputs.

LOCAL MOVE: Break the folk model of prompting (user commands, machine obeys) by enumerating the co-signatories of every generation — training data, safety filters, physics engines, procedural rules, system prompts — and giving the ensemble a constitutional name.

SOURCE TERMS: control signal (Wiener 1948); sovereign command; buried law / visible petition; constitution of the worldtext; system prompt; initialization vector; factory settings, "no outside-model" (Bajohr, via SYNTH-01/03); hanging-together.

WHAT BECAME STRANGE: The user's prompt — the only part of the apparatus the user writes — turns out to be the LEAST powerful input in the constitution: a petition addressed to laws the petitioner cannot read.

QUESTION: If the system prompt is a buried law, what is the analog of judicial review — who can inspect, contest, or amend it?

DEEPER QUESTION: Does calling the ensemble a "constitution" imply that generated worlds have a politics of legitimacy — that some worldtexts are constitutionally illegitimate because their buried laws cannot be petitioned against — and is that a metaphor or an actionable critical standard?

MECHANISM: Generation = f(user prompt, system prompt, weights, filters, physics, procedure); the user controls one argument; platform-side inputs are unseen and non-negotiable; hence output attribution to the user prompt alone is systematically wrong; the first image is a "readout" of the full parameterization.

FORMAL SHIFT: From speech-act model (prompt as imperative) to control-theory model (prompt as one input to a regulated plant) and juridical model (prompt as petition under constitution).

SOURCE FORMALISM: Wiener's cybernetic control signal; the constitutional metaphor (buried law / visible petition); the initialization-vector metaphor from cryptography (deep-research-report 17 / Ekphrasis-to-Worldtext keel block).

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Output o = G(u; s, w, phi) with u user prompt, s system prompt, w weights, phi filters/engines. Sovereignty index of u = sensitivity of o to u relative to total sensitivity across (u, s, w, phi). The section's claim: index(u) << 1, and s, w, phi are unobservable to the petitioner — a constitution without publication.

TENSION: READING A (Watson): the multi-input structure is a political scandal requiring constitutional vocabulary — power hides in the buried law. READING B (Jay, portugal-draft): the same fact is a neutral engineering observation — system prompts "guide and constrain the model," full stop. The final draft keeps B's sentence and cuts A's entire framework (control signal, constitution, buried law all gone).

MISSING: The dropped aphorism chain is recorded in watson-shield-as-worldtext.md, including a cut distinction with real content: "In the probabilistic path, text navigates a latent space; in the hybrid path, text legislates a rule system. Only the hybrid path recovers the original force of 'operative': the word specifies not appearance but behavior" — the sharpest statement of what "operative" means anywhere in the corpus, present only in the Blacksmith typescript.

BOUNDARY: The constitutional metaphor presumes proprietary platforms; open-weight local models with user-authored system prompts collapse the buried-law/petition distinction.

CITATION TRAIL: Wiener 1948 (Cybernetics) → Bajohr 2024 ("factory settings," "no outside-model") → Chun 2011 ("operation is never innocent," via watson-shield-as-worldtext.md and SEED-02) → Ha & Schmidhuber 2018.

TEST: Sensitivity experiment: vary user prompt vs. system prompt on an open pipeline and measure output variance attributable to each; the claim predicts system-side dominance for world-level properties (physics, permissible actions) and user-side influence confined to surface content.

PLATFORM: Proprietary generative platforms (OpenAI, Gemini, Midjourney); world generators (Genie, Marble) with "elaborate unseen system prompts."

LINKS: [[FORAGE-DD-010]] [[FORAGE-DD-013]] [[FORAGE-DD-001]] [[FORAGE-DD-009]]

BIBTEX: @book{wiener1948cybernetics, author={Wiener, Norbert}, title={Cybernetics: Or Control and Communication in the Animal and the Machine}, publisher={MIT Press}, year={1948}}
