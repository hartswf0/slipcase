ZETTEL

ID:
FORAGE-DX-004

TITLE:
HALLUCINATION AS DOUBLE BIND: THE CORPUS'S ONE MECHANISTIC THEORY OF MODEL FAILURE, STATED AND NEVER TESTED

SOURCE:
drive-download deep-research corpus — "Second-Order Thick Prompting: A Cybernetic and Anthropological Framework for Observer-in-the-Loop AI Interaction" §3.3 — 2026; invoking Gregory Bateson, "Toward a Theory of Schizophrenia" (1956) via Steps to an Ecology of Mind

PASSAGE:
[QUOTE]
"Primary Injunction: 'Do X' (e.g., 'Answer the user's question...'). Secondary Injunction: 'Do not do X' (at a higher abstract level... encoded in the RLHF safety layer). Tertiary Injunction: 'You cannot leave the field' (The model must generate a response)."

[QUOTE]
"When an LLM faces a Double Bind, it 'hallucinates.' It creates a reality where both true and false are suspended, often generating a plausible-sounding but nonsensical or evasive answer to satisfy the conflicting logical constraints."

[QUOTE]
"Logical Type Separation... is the specific antidote to the Double Bind."

RESEARCH OBJECT:
A causal theory of hallucination with a distinctive prediction: hallucination rate should *spike* where instruction and constraint contradict at different logical levels, and should *fall* when the contradiction is made structurally explicit (tags separating levels) — even holding total contradiction constant.

That is not what standard accounts predict. The dominant explanations (distribution gaps, exposure bias, retrieval failure, sampling noise) attribute hallucination to *ignorance*; this one attributes a distinct class of hallucination to *conflict* — the model is Bateson's schizophrenogenic child, forbidden both to answer and not to answer and forbidden to leave the field.

LOCAL MOVE:
The paper transposes Bateson's three-injunction schema onto the RLHF stack: user turn = primary injunction, safety layer = secondary, autoregressive obligation to emit tokens = tertiary ("you cannot leave the field" is a genuinely sharp mapping — a chat model literally cannot leave the field).

SOURCE TERMS:
double bind
primary/secondary/tertiary injunction
logical types
Learning I / II / III
logical type separation
you cannot leave the field
RLHF safety layer
evasive answer

WHAT BECAME STRANGE:
The tertiary injunction is the interesting one and the paper hurries past it. Refusal exists — models *can* decline. So the double bind only forms where refusal is suppressed: forced-choice formats, JSON-mode, tool-call-required settings, benchmark harnesses that reject non-answers.

Which yields a sharper, stranger prediction than the paper's: **structured-output modes should hallucinate more than free-text modes on identical conflicted queries**, because structure is precisely what closes the exit. The antidote proposed (more structure, XML tags) and the aggravator (structure closes the field) are the same intervention — the theory contains its own confounder and the paper does not notice.

QUESTION:
On identical conflicted queries, does hallucination rise when the exit is closed (mandatory JSON/tool-call) versus open (refusal permitted)?

DEEPER QUESTION:
Are there two populations of hallucination — ignorance-hallucination (missing knowledge) and conflict-hallucination (double bind) — with different signatures, different fixes, and different responsibility assignments (training data vs. constraint stack)?

MECHANISM:
<PRIMARY: answer>
+ <SECONDARY: don't answer (higher level)>
+ <TERTIARY: emit tokens regardless>
→ [NO CONSISTENT COMPLETION EXISTS]
→ model outputs the nearest high-probability text that superficially satisfies all three
→ <PLAUSIBLE EVASION OR CONFABULATION>

Antidote claimed:
[TAG-SEPARATED LEVELS] → constraints processed as distinct operations → conflict becomes representable → refusal or clarification instead of confabulation

FORMAL SHIFT:
<FLAT TOKEN SEQUENCE OF CONFLICTING INJUNCTIONS>
→ <TYPED LEVELS>
→ [CONFLICT DETECTION]
→ <REFUSAL / CLARIFICATION INSTEAD OF HALLUCINATION>

SOURCE FORMALISM:
Bateson's three-injunction schema, transposed; the Learning I/II/III ladder as constraint hierarchy; no quantitative apparatus.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

For query q with conflict level c(q) ∈ {none, same-level, cross-level} and exit e ∈ {open, closed}:

  H(q) = P(confabulated content | q, c, e)

Double-bind theory predicts an interaction term: H is maximal at (cross-level, closed) and the c × e interaction is positive. Ignorance theories predict H depends on knowledge coverage only, no interaction.

One 2×3 experiment separates the theories.

TENSION:
READING A: hallucination is a knowledge/distribution phenomenon; conflict cases are a rounding error and "double bind" is a metaphor with no added predictive power.
READING B: conflict-hallucination is a real second population; the interaction term exists; and safety training that adds cross-level contradiction without adding exits *manufactures* hallucination — a governance finding, since it relocates part of the blame from the training data to the constraint architecture.

MISSING:
Any citation in the corpus to the empirical hallucination literature. Any acknowledgment that refusal training already exists (the tertiary injunction is variably enforced, not absolute). Bateson page references.

BOUNDARY:
Bateson's double bind theory of schizophrenia is itself contested in psychiatry; importing its *structure* (conflicting injunctions across levels + no exit) does not import its clinical validity, and the zettel's claim is only about the structure.

CITATION TRAIL:
Bateson, Jackson, Haley, Weakland — "Toward a Theory of Schizophrenia" — Behavioral Science 1(4), 1956.
worldtext/atlas.md [[question-double-bind-mode-collapse]] — registered 2026-04-14, unpursued; this zettel gives it its experiment.
PAPERS/cyber-00.md §3 (Bateson's circuit).
Structured-output/JSON-mode degradation reports in the ML literature — [UNVERIFIED, search before citing].

TEST:
Build 30 queries in three conflict classes (none / same-level / cross-level), run each with exit open (refusal allowed) and closed (mandatory JSON schema with no refusal field). Score confabulation blind.

A positive c × e interaction is the first empirical support for a Batesonian mechanism of hallucination — and a paper title: "You Cannot Leave the Field: Structured Output and the Manufacture of Hallucination."

PLATFORM:
[[conflict-hallucination]]

LINKS:
[[FORAGE-DX-005]]
[[FORAGE-OD-033]]
[[FORAGE-OD-012]]

BIBTEX:
@article{bateson1956toward,
  title={Toward a Theory of Schizophrenia},
  author={Bateson, Gregory and Jackson, Don D. and Haley, Jay and Weakland, John},
  journal={Behavioral Science},
  volume={1},
  number={4},
  pages={251--264},
  year={1956}
}
