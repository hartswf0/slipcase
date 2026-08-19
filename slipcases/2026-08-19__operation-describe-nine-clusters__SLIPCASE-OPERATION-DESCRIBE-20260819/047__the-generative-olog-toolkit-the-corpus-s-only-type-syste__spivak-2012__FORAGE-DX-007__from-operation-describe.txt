ZETTEL

ID:
FORAGE-DX-007

TITLE:
THE GENERATIVE OLOG TOOLKIT: THE CORPUS'S ONLY TYPE SYSTEM FOR PROMPTS, WITH A DEFINED Δ, A ΔΔ, AND A COMPUTABLE VISCOSITY — AND IT EXISTS ONLY IN THIS ONE DOCUMENT

SOURCE:
drive-download deep-research corpus — "The Epistemic Crisis of Description in Generative Systems" §§1.1–3.1 — 2026; invoking David Spivak & Robert Kent, "Ologs: A Categorical Framework for Knowledge Representation" (PLoS ONE, 2012), Gregory Bateson, and Sem-DPO

PASSAGE:
[QUOTE]
"The 'Type System' defined in the GOT specification (Scene, Description, Prompt, Frame) is a meta-Olog: a category of categories designed to govern the generation of semantic worlds."

[QUOTE]
"ΔΔ(p, tweakA, tweakB) → compare(Δ(p, tweakA), Δ(p, tweakB))"

[QUOTE]
"viscosity(p:Prompt) -> number := measure_closure_pressure( run(p) )"

[QUOTE]
"Low Viscosity (Thin): 'The boy winked.' ... High Viscosity (Thick): 'The boy's wink was a conspiratorial fissure in the rigid discipline of the classroom, a semiotic rebellion acknowledged only by the back row.' This text is dense. It resists being moved to a different context (e.g., a romantic dinner). It is 'sticky' with social meaning."

RESEARCH OBJECT:
A worked formal apparatus the rest of the archive keeps reaching for and never builds:
1. Prompt as constructor of a temporary Olog (a schema the model populates with instances) — grounded in a real published formalism (Spivak/Kent) with real constraints (singular indefinite noun phrases; commutative diagrams as facts).
2. Frame as functor: ∂frame(p,k,v) maps the invariant event-olog into a style domain ("experiment happened" → "Methodology Section" under Scientific-Paper; → "Scandal" under Lab-Gossip) — Spivak's "safe data migration" repurposed as *meaning migration across styles*.
3. Δ and ΔΔ operators: first- and second-order comparison of steering strategies — ΔΔ is Bateson's Learning II rendered as an API.
4. Viscosity given an operational definition at last: resistance to context transplantation ("it resists being moved to a romantic dinner").

LOCAL MOVE:
The paper replaces "prompt alchemy" with category theory: every tweak becomes a typed morphism, every fact a commutative diagram, every style change a functor. It is the only document in either corpus that gives the Geertzian wink a formal metric — Geertz's own example ("the boy winked") is the paper's low-viscosity case.

SOURCE TERMS:
olog
generative olog toolkit (GOT)
singular indefinite noun phrase
commutative diagram
functor / safe data migration
∂frame(p,k,v)
Δ / ΔΔ operator
Metric.salience / Metric.option_space / Metric.legibility
closure pressure
ostranenie

WHAT BECAME STRANGE:
Viscosity, which circulates through the whole archive as an atmospheric metaphor (latent viscosity, worldtext viscosity, platform mean), here gets a decision procedure: **transplant the text into a foreign context and measure how much it resists.** "Sticky with social meaning" = high cost of recontextualization. That is measurable with embeddings today (perplexity or fit degradation of the passage under context swap).

And ΔΔ answers a question the archive's own framework raised and dropped: not "did the description change the output" but "which of two descriptions changed it *better*, and along which axis, with which side effects." The archive's ΔG is a detector; ΔΔ is a comparator — and steering requires comparators.

QUESTION:
Can viscosity-as-transplant-resistance be computed reliably (perplexity delta under context swap), and does it track the thick/thin judgments the archive makes by hand?

DEEPER QUESTION:
If the prompt defines a schema (olog) and the model populates instances, then prompt failure divides into schema error (wrong types/relations) and instance error (right schema, wrong filler) — a two-way fault taxonomy that would reorganize every failure list in the archive. Does the distinction survive contact with real logs?

MECHANISM:
<PROMPT>
→ [PARSE AS TEMPORARY OLOG: objects + aspects + declared path-equivalences]
→ model populates instances
→ [COMMUTATIVE DIAGRAMS = CONSISTENCY CHECKS: two declared-equal paths must agree]
→ disagreement = detected incoherence, BEFORE any human reads the output

This is the mechanical version of the worldtext's "same-worldness audit": path-equivalence checking as automated continuity testing.

FORMAL SHIFT:
<PROMPT AS STRING>
→ <PROMPT AS SCHEMA (OLOG)>
→ [FUNCTORIAL STYLE MIGRATION + PATH-EQUIVALENCE CHECKS]
→ <TYPED, COMPARABLE, LINTABLE GENERATION>

SOURCE FORMALISM:
Type System {Scene, Description, Prompt, Frame}; operators Δ(p, tweak), ΔΔ(p, tweakA, tweakB), ∂frame(p, k, v); metrics {salience, option_space, legibility}; viscosity(p) := measure_closure_pressure(run(p)). All quoted or paraphrased from the document; none implemented.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

viscosity, computably:

  visc(x) = E_c'[ misfit(x | c') ] − misfit(x | c)

where c is the passage's home context, c' random transplant contexts, and misfit = perplexity under a reference model. Thin text: misfit barely rises when transplanted. Thick text: misfit spikes.

ΔΔ, computably: embed outputs; Δ(p, tweak) is a displacement vector; ΔΔ compares two displacement vectors by angle (same direction?) and by side-effect components (projections onto unintended axes).

TENSION:
READING A: GOT is the archive's missing formal chapter — the categorical machinery makes thick description computable and the lint automatic.
READING B: ologs formalize what can be typed, and Geertz's whole point is that the wink's meaning is *not* typeable in advance — the conspiratorial fissure is thick precisely because its schema is discovered in interpretation, not declared before it. On this reading GOT is thin description with better notation, and its success would refute the Geertzian premise it claims to implement.

That tension — can thickness survive typing? — is itself the best paper here.

MISSING:
The GOT specification document itself. The paper cites "the GOT specification" as though it exists elsewhere; nothing named GOT appears in the repo (PROGRAMS/*.json is adjacent but different machinery). Either it exists outside the repo or the deep-research model confabulated a specification — determine which before building on it.

BOUNDARY:
Spivak/Kent ologs are real and verifiable. Everything specifically "GOT" is single-sourced to this AI-generated document; treat the toolkit as a design proposal, not prior work.

CITATION TRAIL:
Spivak & Kent — "Ologs: A Categorical Framework for Knowledge Representation" — PLoS ONE 7(1), 2012 — verify the noun-phrase and commutative-diagram rules.
Sem-DPO (cited in-text for semantic drift) — [UNVERIFIED], locate.
worldtext/syntheses/worldtext-formal-engine.md — the repo's own typed engine; diff GOT's type system against its 7 node types / 9 edge types.
FORAGE-DX-006 (the two compilers — GOT would be the type system of the second).

TEST:
Implement visc() as perplexity-delta-under-transplant. Run it on the paper's own two examples (the winked/conspiratorial-fissure pair) and on 20 prompt pairs the archive already classifies as thick/thin by hand.

Agreement validates the first computable metric of thickness. Disagreement is better: it locates exactly where thickness exceeds what typing can capture — the READING B result.

PLATFORM:
[[typing-thickness]]

LINKS:
[[FORAGE-DX-006]]
[[FORAGE-DX-002]]
[[FORAGE-OD-020]]
[[FORAGE-OD-001]]

BIBTEX:
@article{spivak2012ologs,
  title={Ologs: A Categorical Framework for Knowledge Representation},
  author={Spivak, David I. and Kent, Robert E.},
  journal={PLoS ONE},
  volume={7},
  number={1},
  pages={e24274},
  year={2012}
}
