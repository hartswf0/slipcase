ZETTEL

ID: FORAGE-ZP-007

TITLE: The loop is the operative unit; the image is feedback, not product

SOURCE: Z-Port/final-draft-v2.md §2; Z-Port/final-draft-v3.md §2 (adds the Midjourney v6 example); Z-Port/A-TEST/a-1.md §I (same example with prompt syntax); Z-Port/worldtext-after-ekphrasis.md §1; Z-Port/final-assembled-draft.md §2 (adds Oppenlaender, PromptMagician, Simonen citations)

PASSAGE: [QUOTE] "The operative unit is therefore not the single prompt. The operative unit is the loop." (final-draft-v2.md §2) [QUOTE] "The image is not the product. The image is feedback. Thick prompting names this unfinished condition: ekphrasis after the image has become feedback." (final-draft-v2.md §2) [QUOTE] "A user inputs a thin prompt: 'A Homeric shield.' The system does not return a neutral historical artifact. Guided by its probabilistic training distribution, it defaults to heavily weighted video-game concept art styles — glowing edges, Unreal Engine lighting, fantasy iconography. The user reads this misinterpretation and iterates a thick prompt, applying negative constraints to sculpt the latent space (`--no unreal engine, fantasy, glowing`) alongside positive structural logic (`concentric rings, agricultural labor, ocean rim, style raw`). The first image was not a failure. It was evidence revealing the model's biases." (final-draft-v3.md §2) [QUOTE] "There is no perfect prompt. There is only a better handle on the machine." (Draft F, quoted in draft-f-analysis.md #13)

RESEARCH OBJECT: The unit-of-analysis claim for generative media: not prompt, not image, but the cycle write → generate → read the misinterpretation → revise → regenerate. Corollary ontological shift: the generated image is demoted from artwork to diagnostic signal ("It tells the user what the model heard, what the model ignored, and what the model already assumes" — a-1.md). Empirically anchored in HCI literature (final-assembled: Oppenlaender's "co-creative ecosystem"; PromptMagician's "diagnostic cycle"; Simonen et al.: default images recur across unrelated inputs — "The archive always goes first").

LOCAL MOVE: Relocate ekphrasis from the finished artifact to the conditions of generation, which lets the paper link the prompting loop back to progymnasmata performance (delivery, audience response) against Cleanth Brooks's "well-wrought urn" model of the completed poem.

SOURCE TERMS: the loop; image as feedback; misinterpretation; negative constraints; sculpting the latent space; performance score; "no final perfect prompt"; diagnostic return; generation gate (v4: "one-way opaque: the prompter sees input and output but never the path between them")

WHAT BECAME STRANGE: Failure changes valence: the wrong image is the most informative event in the cycle — the system's biases are only visible when it misreads you, so error becomes the primary epistemic instrument for mapping a platform.

QUESTION: Is the loop genuinely dialogic (the model "answers back") or is that anthropomorphism for repeated sampling — what distinguishes iterative negotiation from brute-force rerolling?

DEEPER QUESTION: If the image is feedback, what is the actual product of prompting? Candidate answers latent in the drafts: a calibrated user (who has learned the platform), a refined prompt-artifact (score/JSON/metaprompt), or a relation ("The prompter trains a relation with the model"). The choice determines what ekphrasis now produces.

MECHANISM: Each output exposes "another mismatch between user intention and model tendency" (v2); negative prompting subtracts probability mass from default regions; iteration converges not on truth but on "the next useful version" (b-1.md).

FORMAL SHIFT: From one-shot function application (image = G(prompt)) to a closed-loop control system in which the user is the error-correcting controller — v4 makes this explicit: the prompt "functions less as a command than as a control signal (cf. Wiener 1948)."

SOURCE FORMALISM: The a-1/v3 Midjourney v6 protocol with literal parameter syntax (`--no unreal engine, fantasy, glowing`; `style raw`); d-1/image-is-not-end's schema: "write prompt → receive output → inspect failure → revise constraint → regenerate → compare → thicken → repeat".

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Prompting as feedback control: p_{t+1} = p_t + f(intent − read(G(p_t))), where read() is the user's diagnosis of the output and f translates mismatch into constraint edits; convergence criterion is pragmatic ("useful"), not fixed-point.

TENSION: READING A: the loop empowers — thick iteration gives the user "a better handle on the machine"; promptcraft is skill. READING B (via platform realism): the loop domesticates — each iteration teaches the user the platform's grammar, so what converges is the user's expectation toward the archive; the feedback trains the human. Both readings fit the same protocol.

MISSING: The "documented interaction" with Midjourney v6 has no actual documentation (no images, no session log) — v3 presents it as "Consider a documented interaction," a hypothetical wearing empirical clothes; guardian-grade C5 concerns apply. No count of iterations, no failure cases where thickening does not help.

BOUNDARY: Applies to interactive prompting interfaces with fast regeneration; the drafts note metaprompting extends the loop to prompts-that-write-prompts (Zhang, Yuan & Yao 2025; Zhao et al 2024; Ceurstemont 2025).

CITATION TRAIL: Quintilian Inst. Or. 6.2 (generation begins in the orator's imagination) → Brooks (well-wrought urn, via Keats criticism) → Brosch 2018a (ekphrasis as performance) → Liu & Chilton 2023 → Oppenlaender 2022–2024 → Lin et al. 2024 (PromptMagician) → Simonen et al. 2025 → Zhang, Yuan & Yao 2025.

TEST: The Simonen-cited claim is testable: sample thin prompts across unrelated subjects and check for recurring default compositions; then verify that structured negative constraints reduce recurrence more than added adjectives do.

PLATFORM: Midjourney v6 (named example, with --no and style raw parameters); general text-to-image platforms; PromptMagician as tooling evidence.

LINKS: [[FORAGE-ZP-006]], [[FORAGE-ZP-004]], [[FORAGE-ZP-011]], [[FORAGE-ZP-013]]

BIBTEX: @unpublished{hartsoe_bolter_v3_2026, author = {Hartsoe, Watson and Bolter, Jay David}, title = {From Imagetext to Worldtext: Generative AI as Operative Ekphrasis (final-draft-v3)}, note = {Unpublished draft, OPERATION-DESCRIBE/Z-Port/final-draft-v3.md, \S2}, year = {2026}}
