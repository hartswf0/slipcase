ZETTEL

ID:
FORAGE-OD-020

TITLE:
THE SLIPCASE CORPUS AND THE OPERATION DESCRIBE CORPUS RECORD THE SAME MISSING MECHANISM AND NEITHER KNOWS THE OTHER DID

SOURCE:
SLIPCASE — Portable Research Field — 1,244 zettels across 30 cases — 2026-08-17 to 2026-08-18 (https://hartswf0.github.io/slipcase/); read against OPERATION DESCRIBE — worldtext/atlas.md §QUESTIONS (34 registered open questions) — 2026-04-28

PASSAGE:
[QUOTE]
SLIPCASE FORAGE-SHANAHAN-001, MISSING:
"A theory of which parts of context remain load-bearing, which decay, which are overwritten, and what forms of instruction resist conversational drift."

[QUOTE]
OPERATION DESCRIBE atlas.md:
"[[question-worldtext-viscosity]] | Does a persistent worldtext develop its own viscosity, its own platform mean, its own twelve lighthouses?"

RESEARCH OBJECT:
Two archives by the same author, four months apart, in two vocabularies, name the same unresolved mechanism: what makes accumulated description resistant to change.

SLIPCASE calls it drift-resistance. OPERATION DESCRIBE calls it viscosity. Neither cites the other. Neither has a measure.

That the same gap surfaced independently twice is evidence that it is load-bearing rather than incidental.

LOCAL MOVE:
This is a collision, not a forage. Neither corpus is wrong. The finding is topological: two disconnected regions of one research programme are pressing on a single unnamed variable.

SOURCE TERMS:
load-bearing
decay
overwritten
resist conversational drift
viscosity
platform mean
attractor tokens
twelve lighthouses
same-worldness

WHAT BECAME STRANGE:
"Viscosity" in the OPERATION DESCRIBE archive is always a property of the *model's* training distribution — the resistance the prompt must overcome. It appears in seed-candidates-ch02, icids §6.2, and the framework's YAML theoretical_note ("a high-viscosity vector anchor").

The SLIPCASE gap is about the resistance of *accumulated context* — a property of the session, not the model.

So there are two viscosities, sharing one word, operating at different timescales, and the archive has never distinguished them. That is a terminological mutation inside a single research programme.

QUESTION:
Are model viscosity (resistance of the training prior) and context viscosity (resistance of accumulated instruction) the same mechanism at two timescales, or two mechanisms with one name?

DEEPER QUESTION:
If they are the same mechanism, then a long enough worldtext becomes indistinguishable from a fine-tune — and the archive's central object, the accumulated worldtext, would be a training artifact rather than a text.

MECHANISM:
Model viscosity:
<PROMPT> → competes against <TRAINING PRIOR> → [PRIOR PULLS TOWARD PLATFORM MEAN] → <GENERIC OUTPUT>

Context viscosity:
<NEW INSTRUCTION> → competes against <ACCUMULATED CONTEXT> → [ACCUMULATION PULLS TOWARD ESTABLISHED PATTERN] → <SESSION-SPECIFIC OUTPUT>

Same shape. Different substrate. Opposite implications for the operator: the first must be fought, the second is the thing the archive is trying to build.

FORMAL SHIFT:
<TWO RESISTANCES>
→ <ONE TERM>
→ [UNDIFFERENTIATED USE]
→ <A CLAIM ABOUT WORLDTEXT COHERENCE THAT MAY BE A CLAIM ABOUT PRIORS>

SOURCE FORMALISM:
NONE in either corpus. Viscosity is used metaphorically throughout; no paper in the archive supplies a unit, a measurement, or a range.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Separate them and give each a ratio:

  model viscosity     μ_M = ‖Δ prompt embedding‖ / ‖Δ output distribution‖   (holding context empty)
  context viscosity   μ_C = ‖Δ new instruction‖  / ‖Δ output distribution‖   (holding context long)

Then the archive's central practical claim becomes checkable:

  a worldtext "coheres" iff μ_C grows with accumulated context
  a worldtext "collapses to the platform mean" iff μ_M dominates μ_C

And the archive's own [[question-worldtext-viscosity]] — "does a persistent worldtext develop its own viscosity" — becomes the question of whether μ_C is increasing in context length.

TENSION:
READING A: one mechanism. Both are attention over tokens; context is just recent training. Then coherence and prior-collapse are the same phenomenon and the archive's hopes for worldtext are hopes for a longer prompt.
READING B: two mechanisms. Weights are gradient-shaped and cannot be overwritten in-session; context is attention-shaped and can. Then worldtext coherence is genuinely a different achievement from fine-tuning, and the archive's object survives.

Reading B is the archive's implicit position and it has never been argued.

MISSING:
Any citation between the two corpora. Any measurement of either viscosity. Any statement that there are two.

BOUNDARY:
This is an observation about two archives and one word. It does not establish that either viscosity exists as a stable quantity; that is precisely what the test would decide.

CITATION TRAIL:
SLIPCASE cases "prompt forward", "the prompt keeps disappearing", "what kind of thing is the model" — 205 zettels that likely bear on context viscosity and are not cited in OPERATION DESCRIBE.
worldtext/atlas.md [[question-worldtext-viscosity]], [[question-mud-as-resource]].
In-context learning as implicit gradient descent — the literature that would decide Reading A vs B.
FORAGE-OD-019.

TEST:
Measure μ_C at context lengths 0, 2k, 8k, 32k tokens using the same fixed instruction and the same output probe.

If μ_C rises with length, the worldtext accumulates resistance of its own and Reading B holds. If μ_C is flat and only μ_M matters, the archive's coherence claim reduces to prompt engineering and must be restated.

PLATFORM:
[[the-half-life-of-a-description]]

LINKS:
[[FORAGE-OD-019]]
[[FORAGE-OD-030]]
[[FORAGE-OD-024]]

BIBTEX:
@misc{hartsoe2026slipcase,
  author = {Hartsoe, Watson},
  title = {SLIPCASE — Portable Research Field},
  howpublished = {\url{https://hartswf0.github.io/slipcase/}},
  note = {1,244 zettels across 30 forage cases},
  year = {2026}
}
