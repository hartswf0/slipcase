ZETTEL

ID: OD-08

TITLE: A procedural first pass can lose authority during visual refinement

SOURCE: Bolter and Hartsoe — Operative Ekphrasis: From Imagetext to Worldtext — §6 — the Shield of Achilles workflow using B-flix, ABC-Flix, and a vision model. Newman — Art as ‘Operation’ — 2026 — LeWitt discussion of conception and realization.

PASSAGE: [PARAPHRASE] The paper describes sending passages from the Shield to a language model that emits B-flix commands, rendering them into an animated contact sheet, and giving that sheet and the Homeric text to a vision model for refinement.

RESEARCH OBJECT: What survives as a binding constraint across a transition from executable marks to a generated image sequence.

LOCAL MOVE: Operation Describe makes the relation among text, executable notation, and image unusually concrete. The second model receives both the original text and the render, which opens a question about which source controls a disputed detail.

SOURCE TERMS: B-flix, `PNT`, `LIN`, `REC`, animated contact sheet, refinement, control signal.

WHAT BECAME STRANGE: The same feature can be enforced by code in the contact sheet and merely suggested by pixels in the next pass. The workflow may preserve its look while losing its ability to constrain later states.

QUESTION: When the poem and the procedural render pull in different directions, which one can require the next operator to preserve a relation?

MECHANISM: The language model proposes a representation. The renderer executes it. The vision model interprets a visual result alongside the source text. A reviewing operator must decide what survives, unless that requirement is represented and checked by another part of the system.

FORMAL SHIFT: <Homeric passage> → <B-flix commands> → [render into a reference and reinterpret] → <refined sequence whose procedural fidelity can be tested>

SOURCE FORMALISM: The paper documents the command examples, rendering step, and feedback of the contact sheet with the original passage. Section 6 supplies no preservation check for the second pass.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Assign one invariant at three levels: visible object identity, temporal order, and later consequence. For the trial scene, keep the same pair of disputants, preserve the elders’ successive turns, and keep the case unresolved until an authorized decision. Compare visual refinement with a variant that also supplies those conditions as explicit state.

TENSION: The contact sheet can function as a compositional reference or as evidence of rules the next stage should preserve. LeWitt’s distinction between authorized interpretation and violation makes the difference consequential.

MISSING: Paired intermediate and refined outputs with enough trace information to show what the second pass preserved, changed, or invented.

BOUNDARY: The paper establishes the reported workflow. Procedural continuity through the second pass remains to be demonstrated for a specific sequence.

CITATION TRAIL: [[AP-02]] and [[AP-05]] → Operation Describe §6 → the B-flix source, raw ABC-Flix contact sheet, and corresponding refined sequence for the same Homeric zone.

TEST: Inspect one matched pair. Choose a relation with a visible consequence, such as whose turn follows whose. Mark the first stage where that relation can change without producing an error. Then repeat with an explicit check at that stage.

PLATFORM: [[Where the operator changes hands]]

LINKS: [[AP-02]] · [[AP-05]] · [[OD-02]] · [[OD-03]] · [[OD-09]]

BIBTEX:
@misc{BolterHartsoe2026Operative,
  author = {Bolter, Jay David and Hartsoe, Watson},
  title = {Operative Ekphrasis: From Imagetext to Worldtext},
  year = {2026},
  note = {Section 6, Shield of Achilles and B-flix workflow},
  url = {https://hartswf0.github.io/operation-describe/Dry-Dock/FINAL_SHIPWORTHY.html}
}
@misc{Newman2026Operation,
  author = {Newman, Michael},
  title = {Art as `Operation': from Lovelace and Mallarmé to Adversarial Poetry},
  year = {2026},
  note = {Supplied talk transcript, LeWitt discussion. URL identifies the program},
  url = {https://www.unive.it/web/en/19108/home}
}