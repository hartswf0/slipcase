ZETTEL

ID:
Z-SLIP-008

TITLE:
Disclosure becomes more informative when its unit is the production chain

SOURCE:
Watson Hartsoe — SLIPCASE — 2026 — “Disclosure is an identification, not a label”

PASSAGE:
[PARAPHRASE]
SLIPCASE distinguishes a short recurring public identification from a fuller public file describing who acted, what was verbatim, where consequential control entered, what was verified, and what remains unchecked.

RESEARCH OBJECT:
AI disclosure may become more epistemically useful when it identifies consequential transformations in a production chain rather than assigning a binary AI/human label to the final artifact.

LOCAL MOVE:
The specification borrows the broadcast station-identification model to separate lightweight attribution from detailed provenance.

SOURCE TERMS:
identification
public file
chain
consequential control
verbatim
verified
thinness

WHAT BECAME STRANGE:
“Was AI used?” may be the wrong unit of disclosure because the answer contains almost no information about authorship, verification, or control.

QUESTION:
What events in a mixed human-model production chain are consequential enough to require explicit disclosure?

DEEPER QUESTION:
Can authorship become an event log rather than a categorical property of the artifact?

MECHANISM:
Short-form identification points to a fuller provenance record; the detailed record attributes operations and verification states across the chain.

FORMAL SHIFT:
<binary artifact label>
→ <production-chain provenance>
→ [IDENTIFY CONSEQUENTIAL TRANSFORMATIONS]
→ <inspectable authorship history>

SOURCE FORMALISM:
who
origin
where consequential control entered
what is verbatim
what a human verified
what nobody checked

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

ARTIFACT_AUTHORSHIP :=
ordered set of consequential interventions
+ verification events
+ preserved source contributions

TENSION:
A highly detailed provenance chain may still hide the significance of individual interventions behind exhaustive procedural logging.

MISSING:
A principled definition of consequential control.

BOUNDARY:
Production-chain disclosure may improve transparency without resolving normative disputes over credit, responsibility, or authorship.

CITATION TRAIL:
Provenance standards; contributorship taxonomies; documentary editing; broadcast station identification; software commit history.

TEST:
Show readers a binary AI label and a chain-style public file for the same artifact. Test which supports more accurate judgments about control, verification, and responsibility.

PLATFORM:
[[chain-level disclosure]]

LINKS:
[[consequential control]]
[[authorship event log]]
[[public file]]
[[thin provenance]]

BIBTEX:
@misc{hartsoe2026slipcase,
  author = {Hartsoe, Watson},
  title = {SLIPCASE: A Research Checkpoint Compiler},
  year = {2026},
  note = {Working specification}
}
