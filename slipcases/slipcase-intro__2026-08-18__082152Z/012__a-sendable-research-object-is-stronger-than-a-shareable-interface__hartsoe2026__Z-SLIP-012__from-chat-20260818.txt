ZETTEL

ID:
Z-SLIP-012

TITLE:
A sendable research object is stronger than a shareable interface

SOURCE:
Watson Hartsoe — SLIPCASE — 2026 — “One file you can send”

PASSAGE:
[PARAPHRASE]
The checkpoint’s index.html embeds payloads, bibliography, graph, supporting files, PDF, and reconstruction instructions and requires no server, CDN, or network request.

RESEARCH OBJECT:
Portability becomes stronger when an artifact contains not merely a view of research but enough material to reconstruct the research environment that produced the view.

LOCAL MOVE:
SLIPCASE moves from “offline reader” toward self-describing checkpoint.

SOURCE TERMS:
one file you can send
embed
no server
no CDN
no network request
rebuild
replicate

WHAT BECAME STRANGE:
A webpage can function less like a publication and more like a portable research seed.

QUESTION:
What is the smallest self-contained artifact from which a research field can be reconstructed after its original tooling disappears?

DEEPER QUESTION:
Could scholarship be distributed as self-describing checkpoints rather than references to remotely maintained platforms?

MECHANISM:
Primary payloads and reconstruction instructions are embedded inside a universally openable container; derived interfaces can then be recreated from the carried evidence.

FORMAL SHIFT:
<platform-dependent research environment>
→ <self-contained checkpoint>
→ [TRANSFER + RECONSTRUCT]
→ <new local research environment>

SOURCE FORMALISM:
index.html carries:
payloads
bibliography
graph
supporting files
PDF
rebuild instructions

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

PORTABILITY =
OFFLINE_OPENABLE
∧ SELF_DESCRIBING
∧ PRIMARY_PAYLOAD_PRESENT
∧ RECONSTRUCTION_INSTRUCTIONS_PRESENT

TENSION:
Embedding everything in one file creates a new monolith and may make inspection, diffing, incremental update, or archival preservation worse.

MISSING:
A separation between “single-file transmission object” and “canonical storage form.”

BOUNDARY:
Self-containment improves transfer independence but does not guarantee future browser compatibility or executable reconstruction.

CITATION TRAIL:
BagIt; RO-Crate; WARC; single-file web archives; reproducible research compendia; self-extracting archives.

TEST:
Air-gap a checkpoint, remove the original repository, and ask another researcher to reconstruct every mechanically derivable artifact using only the transmitted file.

PLATFORM:
[[self-describing research checkpoint]]

LINKS:
[[portable research field]]
[[single-file transmission]]
[[reconstruction state]]
[[software-independent scholarship]]

BIBTEX:
@misc{hartsoe2026slipcase,
  author = {Hartsoe, Watson},
  title = {SLIPCASE: A Research Checkpoint Compiler},
  year = {2026},
  note = {Working specification}
}
