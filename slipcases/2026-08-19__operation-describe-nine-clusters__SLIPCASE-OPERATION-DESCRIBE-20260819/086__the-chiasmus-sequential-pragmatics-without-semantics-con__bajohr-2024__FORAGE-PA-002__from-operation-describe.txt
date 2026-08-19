ZETTEL

ID: FORAGE-PA-002

TITLE: The chiasmus: sequential pragmatics without semantics, connectionist semantics without pragmatics

SOURCE: PAPERS/bajohr.md (= tenne.md), sections 3–4 "Sequential Digitality: Pragmatics Without Semantics" / "Connectionist Digitality: Semantics Without Pragmatics"

PASSAGE: [QUOTE] "This produces a chiasmus between the two digital paradigms: The sequential system has **pragmatics without semantics**. It acts through command but does not mean. The connectionist system has **semantics without pragmatics**. It correlates meanings but does not act through explicit command-like speech. The prompt sits at the threshold between these worlds. ... The prompt is ekphrasis after execution."

RESEARCH OBJECT: The chiasmic classification of the two digital paradigms, plus the name for the middle zone it opens: [QUOTE] "the strange zone Bajohr calls **artificial semantics**: meaning that is weak, dumb, nonintentional, and technical, yet not reducible to empty formal manipulation."

LOCAL MOVE: Refuses both poles of the standard AI debate ("Hype says the machine understands. Dismissal says the machine merely manipulates symbols.") by giving each digital paradigm exactly one of the two halves of language — force or meaning — and locating the prompt at their crossing point.

SOURCE TERMS: artificial semantics; pragmatics without semantics; semantics without pragmatics; chiasmus; operational vector; latent space; executable syntax

WHAT BECAME STRANGE: The prompt itself — it looks like ordinary language but "once entered into a multimodal model, it becomes an operational vector"; it neither commands (like code) nor communicates (like speech). Also: "artificial semantics is not innocent. It is trained. It is inherited. It is statistical memory with consequences."

QUESTION: Is "weak semantics" a stable third category, or just a rhetorical midpoint — what operational test distinguishes correlation-that-behaves-like-meaning from mere correlation?

DEEPER QUESTION: If sequential systems supply pragmatics and connectionist systems supply semantics, do agentic LLM systems (models wrapped in tool-calling loops) recombine the chiasmus — semantics WITH pragmatics — and does the paper's whole taxonomy then collapse?

MECHANISM: Sequential: explicit instructions execute regardless of meaning; force without sense. Connectionist: CLIP-style training on image-caption pairs places related images and texts near each other in a shared space, supporting flexible cross-modal generation without intention, embodiment, or situation; sense without force. The prompt converts human-legible sense into a vector that activates learned correlations — description becomes summoning "a probable image from a learned distribution."

FORMAL SHIFT: Meaning stops being a binary predicate (understands / doesn't) and becomes a two-axis decomposition (semantic correlation × pragmatic force), with each machine paradigm occupying one off-diagonal cell.

SOURCE FORMALISM: The chiasmus itself (A-without-B / B-without-A), stated as parallel prose clauses.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Let S = has semantic correlation structure, P = has pragmatic/executive force. Human language: S∧P. Sequential code: ¬S∧P. Connectionist model: S∧¬P. Prompt: an S∧P-shaped token consumed at an S∧¬P interface via a ¬S∧P substrate — the type mismatch IS the phenomenon.

TENSION: winnograd.md argues the opposite valence: generated language "can trigger obligations without holding them" — i.e., connectionist systems DO enter pragmatic space (commitment structures) while being "ontologically exempt from commitment." Bajohr's paper says connectionist systems lack pragmatics; Winograd/Flores says they exercise pragmatic force without accountability. The disagreement is over whether pragmatics means execution or obligation.

MISSING: Any treatment of RLHF/instruction-tuning, which explicitly trains pragmatic behavior (following commands) into the connectionist substrate; the chiasmus is drawn for base multimodal models circa DALL-E/CLIP.

BOUNDARY: "Artificial semantics" is claimed only under "specific operational conditions" — the paper explicitly does not claim lived experience, intention, embodiment, or communicative situation for the model.

CITATION TRAIL: Bajohr (artificial semantics); CLIP / DALL-E / Stable Diffusion as named systems; Agre ("AI is 'philosophy underneath'"); Austin implicitly behind pragmatics; Hayles behind processual text.

TEST: Probe the same instruction as (a) code to an interpreter and (b) prompt to a multimodal model; vary meaning-preserving paraphrase. Prediction: (a) is invariant only under syntactic identity, (b) is approximately invariant under paraphrase — behavioral evidence of semantics without pragmatics.

PLATFORM: CLIP, DALL-E, Stable Diffusion; shell scripts as sequential contrast.

LINKS: [[FORAGE-PA-001]], [[FORAGE-PA-003]], [[FORAGE-PA-007]]

BIBTEX: @article{bajohr2024operative, author={Bajohr, Hannes}, title={Operative ekphrasis: The collapse of the text/image distinction in multimodal {AI}}, journal={Word \& Image}, volume={40}, number={2}, pages={77--90}, year={2024}} % see FORAGE-PA-001 caveat: essay in repo is about Bajohr, authorship of the file unverified.
