ZETTEL

ID: FORAGE-PT-038

TITLE: Repeated successful reference shortens the description, so thickness is a signature of unestablished reference rather than of good description

SOURCE: Referential communication research — Robert Krauss and Sidney Weinheimer on reference shortening over repeated trials (1960s); Herbert Clark and Deanna Wilkes-Gibbs, "Referring as a collaborative process", Cognition (1986), on conceptual pacts [UNVERIFIED pagination]; read against PROGRAMS/eos.json rendering loop

PASSAGE: [PARAPHRASE] In director-matcher tasks, participants describing the same hard-to-name figure repeatedly across trials converge on progressively shorter labels, and the abbreviated label works for the partner who helped establish it while failing for a new partner. [QUOTE] eos.json: "<drawing> [is] <descriptive_struggle_made_visible>"

RESEARCH OBJECT: An empirical relation between coordination and description length that inverts a working assumption. Elaborate description is what partners produce *before* a pact exists. Once it exists, a short label carries the same referential work. So descriptive thickness measures the absence of shared history, not the presence of care.

LOCAL MOVE: This child executes the parent's measurement instinct — convergence across renderers — in a paradigm that already ran it for sixty years, and finds the result runs against the corpus's valuation of thickness.

SOURCE TERMS: referential communication / director-matcher / conceptual pact / entrainment / reference shortening / new-partner cost

WHAT BECAME STRANGE: Thickness and success are inversely related over time. The corpus treats a rich constraint stack as a mark of skilled description; this paradigm treats it as a cost paid while a convention is missing. Both can be true only if thickness is indexed to the *history* between describer and receiver — which no measure in the corpus records.

QUESTION: Does prompt length required for a fixed output fall across repeated interaction with a system that retains the exchange, and rise again when the retained context is cleared?

DEEPER QUESTION: The new-partner cost is the sharp finding: an abbreviated label fails for someone who did not help build it. If prompts entrain to a model version, then a prompt is a pact with that version — and a model update is a partner substitution, which predicts exactly the brittleness practitioners report.

MECHANISM: <NOVEL REFERENT> -> [ELABORATE DESCRIPTION, HIGH COST] -> partner confirms -> [PACT FORMED] -> <SHORT LABEL SUFFICES> -> [NEW PARTNER] -> label fails -> <ELABORATION REQUIRED AGAIN>

FORMAL SHIFT: <DESCRIPTION LENGTH> -> <FUNCTION OF SHARED HISTORY> -> [PACT FORMATION] -> <COMPRESSION, WITH A NEW-PARTNER PENALTY>

SOURCE FORMALISM: The director-matcher paradigm and its trial-by-trial length measurements; no formal model quoted.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] length(t) = tokens needed at interaction t for fixed output fidelity. Pact formation predicts monotone decrease with t and a jump on partner change. Then thickness(D) is not a property of D but of the pair (D, history) — the same indexing the naming asymmetry requires, arrived at from psycholinguistics.

TENSION: READING A: pacts are genuine shared conventions and compression is evidence of successful coordination, so thick prompting is a startup cost to be minimised. READING B: compression discards content that mattered — the short label works only within a narrow range of tasks, and the pact buys efficiency by shrinking what can be said.

Discriminating evidence: after a pact forms, test the abbreviated label on a *variant* of the referent. If it fails where the elaborate description succeeded, compression lost information rather than encoding it.

MISSING: Verified pagination. Any application of the paradigm to human-model interaction with length as the dependent variable. Any measurement of the new-partner cost across model versions.

BOUNDARY: These are laboratory reference tasks with simple figures. Extending pact dynamics to open-ended generative prompting is an extrapolation, and the referents there are not fixed.

CITATION TRAIL: [[FORAGE-PT-011]] and [[FORAGE-PT-003]] -> Clark and Wilkes-Gibbs 1986 -> pacts and the new-partner cost -> next: the naming asymmetry in tool selection, where a legible name substitutes for a description — the same phenomenon in a different literature.

TEST: Fixed target output, repeated sessions with retained context, measure tokens to criterion per session. Then clear context, and separately change model version. Both should restore the startup cost; the model-version condition measures whether a prompt is a pact with a partner.

PLATFORM: [[thickness-is-indexed-to-history]]

LINKS: [[FORAGE-PT-003]] [[FORAGE-PT-011]] [[FORAGE-PT-051]] [[FORAGE-PT-053]]

BIBTEX: @article{clark1986referring, title={Referring as a collaborative process}, author={Clark, Herbert H. and Wilkes-Gibbs, Deanna}, journal={Cognition}, volume={22}, number={1}, year={1986}, note={[UNVERIFIED] pagination not verified in this forage}}
