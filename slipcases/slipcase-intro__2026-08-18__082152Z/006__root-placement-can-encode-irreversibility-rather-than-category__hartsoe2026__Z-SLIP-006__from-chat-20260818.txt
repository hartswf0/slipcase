ZETTEL

ID:
Z-SLIP-006

TITLE:
Root placement can encode irreversibility rather than category

SOURCE:
Watson Hartsoe — SLIPCASE — 2026 — “Repository”

PASSAGE:
[PARAPHRASE]
SLIPCASE keeps irreplaceable research objects at the checkpoint root while placing reproducible derivatives in underscore-prefixed directories: “Root holds what you would grieve. Underscore folders hold what you would regenerate.”

RESEARCH OBJECT:
Filesystem topology can distinguish primary intellectual events from reproducible views without imposing a topical hierarchy.

LOCAL MOVE:
The folder system stops answering “what kind of thing is this?” and starts answering “what would be lost if this vanished?”

SOURCE TERMS:
root
underscore folders
regenerate
zettel
derived artifact

WHAT BECAME STRANGE:
A filesystem hierarchy can encode reversibility rather than ontology.

QUESTION:
Would organizing artifacts by recoverability produce more durable research repositories than organizing them by document type or topic?

DEEPER QUESTION:
Is irreversibility a more fundamental archival property than category?

MECHANISM:
Objects whose loss destroys unique intellectual history receive privileged placement; objects derivable from them are segregated as disposable views.

FORMAL SHIFT:
<heterogeneous files>
→ <recoverability classes>
→ [PLACE BY LOSS CONSEQUENCE]
→ <filesystem expressing preservation priority>

SOURCE FORMALISM:
root = what you would grieve
underscore folder = what you would regenerate

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

PLACEMENT(x) =
ROOT       if recovery_cost(x) includes irrecoverable intellectual loss
DERIVED    if x = f(preserved_objects)

TENSION:
Some supposedly derived artifacts contain editorial decisions that cannot actually be regenerated without reproducing the original model state or prompt context.

MISSING:
A test for whether an artifact is genuinely derivable rather than merely reproducible in rough form.

BOUNDARY:
Filesystem placement communicates preservation priority but does not itself guarantee recoverability.

CITATION TRAIL:
Content-addressable storage; build systems; source/derived distinctions in scientific computing; archival appraisal.

TEST:
Delete every underscore directory from a mature checkpoint and rebuild it using only root objects and retained compiler instructions. Diff the results.

PLATFORM:
[[filesystem as epistemic architecture]]

LINKS:
[[irreversibility]]
[[derived artifact]]
[[build system]]
[[research source of truth]]

BIBTEX:
@misc{hartsoe2026slipcase,
  author = {Hartsoe, Watson},
  title = {SLIPCASE: A Research Checkpoint Compiler},
  year = {2026},
  note = {Working specification}
}
