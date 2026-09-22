ZETTEL

ID:
20260921-put-that-there-effective-accuracy-includes-repairability

TITLE:
Bolt’s System Could Become More Useful Without Making the Speech Recognizer More Accurate

SOURCE:
Richard A. Bolt, Chris Schmandt, and Eric Hulteen — Put-That-There: Voice and Gesture at the Graphics Interface — 1982 project description; continuing the 1980 Put-That-There work. ([www-prod.media.mit.edu](https://www-prod.media.mit.edu/publications/put-that-there-voice-and-gesture-at-the-graphics-interface/?utm_source=chatgpt.com))

PASSAGE:
[PARAPHRASE] The project explicitly assumes that speech recognition will not be perfectly accurate and seeks greater “effective accuracy” through redundant channels, syntactic and semantic analysis, context-sensitive interpretation, early feedback, and easy voice correction.

RESEARCH OBJECT:
System-level interaction accuracy that can improve while component recognition accuracy remains unchanged.

LOCAL MOVE:
The project relocates the engineering target from preventing every recognition error to making errors visible early and cheap to repair.

SOURCE TERMS:
effective accuracy
recognition errors
feedback
corrected
redundant input channels
context-sensitive interpretation

WHAT BECAME STRANGE:
A better prompt interface need not make the model understand the first instruction more often. It can instead alter when errors become visible and how far their consequences propagate before correction.

QUESTION:
Should prompt-system quality be measured partly by error detection latency and repair distance rather than only first-pass task success?

DEEPER QUESTION:
Can an interaction system with a less accurate model outperform a more accurate model because it externalizes misunderstandings earlier and supports cheaper correction?

MECHANISM:
fallible recognizer
→ provisional interpretation
→ redundant evidence + feedback
→ mismatch noticed early
→ correction issued
→ intended action recovered.

FORMAL SHIFT:
<MODEL ACCURACY>
→ <MODEL ACCURACY + ERROR VISIBILITY + REPAIR COST>
→ [INTERACT]
→ <EFFECTIVE ACCURACY>

SOURCE FORMALISM:
The project explicitly names redundant input channels, syntactic and semantic analysis, context-sensitive interpretation, early feedback, and easy correction as methods for increasing effective accuracy. ([www-prod.media.mit.edu](https://www-prod.media.mit.edu/publications/put-that-there-voice-and-gesture-at-the-graphics-interface/?utm_source=chatgpt.com))

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
effective_accuracy
≈
task_success_after_repair
/
(interaction_cost + propagated_error_cost)

TENSION:
Frequent confirmation and feedback can improve recoverability while increasing cognitive load and reducing fluent use.

MISSING:
A measurement protocol balancing first-pass accuracy, repair latency, correction effort, and interruption burden.

BOUNDARY:
Bolt’s claim concerns a tightly designed multimodal graphical interface, not unconstrained language-model systems.

CITATION TRAIL:
[[20260921-put-that-there-feedback-turns-misreference-into-repairable-event]]
→ Put-That-There’s “effective accuracy”
→ interpretation feedback becomes an alternative to pure model improvement.

TEST:
Compare two builders: stronger model with opaque execution versus weaker model with explicit reference/action previews and one-tap repair. Measure completed-task correctness and total correction cost.

PLATFORM:
[[practice-before-procedure]]

LINKS:
[[20260921-put-that-there-feedback-turns-misreference-into-repairable-event]]
[[effective-accuracy]]
[[repairability]]
[[feedback]]

BIBTEX:
@article{bolt1982put,
  author = {Bolt, Richard A. and Schmandt, Chris and Hulteen, Eric A.},
  title = {Put-That-There: Voice and Gesture at the Graphics Interface},
  year = {1982},
  note = {Architecture Machine Group, Massachusetts Institute of Technology}
}
