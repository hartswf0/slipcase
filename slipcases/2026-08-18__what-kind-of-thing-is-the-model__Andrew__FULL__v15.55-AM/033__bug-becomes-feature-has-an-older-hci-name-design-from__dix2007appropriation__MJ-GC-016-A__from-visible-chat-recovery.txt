ZETTEL

ID:
MJ-GC-016-A

TITLE:
“Bug becomes feature” has an older HCI name: design from appropriation closes the loop when designers formalize a user workaround.

SOURCE:
Alan Dix — “Designing for Appropriation” — Proceedings of BCS HCI 2007, People and Computers XXI, Volume 2 — 2007.
Author source: https://alandix.com/academic/papers/HCI2007-appropriation/

PASSAGE:
[PARAPHRASE]
Dix describes appropriation as users adapting technologies in ways designers did not anticipate. He then identifies a further stage: designers can observe a recurring appropriation and redesign the technology to support the newly discovered use. He calls the closing of this cycle “design from appropriation.”

RESEARCH OBJECT:
DESIGN-FROM-APPROPRIATION.

LOCAL MOVE:
[[MJ-GC-016]] described a remarkable sequence:

users hacked together Remix
→ developers had not intended that use
→ the useful practice became Remix.

Dix supplies an existing HCI distinction that makes this sequence more precise.

The interesting event is not merely appropriation.

It is the transition:

APPROPRIATION
→ STABILIZED PRACTICE
→ DESIGN OBSERVATION
→ FORMAL FEATURE.

That transition turns users into participants in system design without requiring them to enter the official design process.

SOURCE TERMS:
“appropriation”
“learn from appropriation”
“newly discovered uses”
“co-design”
“Technology Appropriation Cycle”
“design from appropriation”
“visibility”

WHAT BECAME STRANGE:
The finished interface can contain fossils of earlier misuse.

A button may be a stabilized workaround.

A feature can therefore encode the history of users refusing—or simply failing—to use a system only as intended.

QUESTION:
How many generative-AI interface features began as recurrent community workarounds rather than top-down product concepts?

DEEPER QUESTION:
If users discover operations and developers subsequently freeze those operations into interface features, who designed the capability?

MECHANISM:
ARTIFACT
→ unanticipated use
→ repeated appropriation
→ appropriation becomes visible
→ designers recognize functional value
→ redesign
→ formerly improvised operation becomes official feature.

FORMAL SHIFT:
FROM:
DEVELOPER
→ FEATURE
→ USER

TO:
DEVELOPER
→ OPEN POSSIBILITY
→ USER APPROPRIATION
→ OBSERVABLE PRACTICE
→ DEVELOPER FORMALIZATION
→ FEATURE.

SOURCE FORMALISM:
Dix explicitly describes a Technology Appropriation Cycle in which observing appropriation can lead to redesign supporting newly discovered uses.

The paper also proposes design principles including:
allow interpretation,
provide visibility,
expose intentions,
support rather than control,
pluggability/configuration,
encourage sharing,
learn from appropriation.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

USE_0 = intended.

USER discovers:
USE_1 ∉ intended uses.

If:

UTILITY(USE_1) high
AND
VISIBILITY(USE_1) high
AND
REPETITION(USE_1) high,

then:

DESIGN_{t+1}
:= FORMALIZE(USE_1).

The workaround becomes infrastructure.

TENSION:
This creates a powerful conceptual genealogy but not a historical influence claim.

There is no evidence here that Midjourney developers knew Dix's appropriation literature or intentionally followed it.

The relation is:
mechanistic resemblance,
not demonstrated intellectual descent.

MISSING:
Primary evidence documenting the exact pre-Remix workaround and the development decision through which it became an official Midjourney feature.

BOUNDARY:
Do not rewrite:
“Dix described this mechanism earlier”

as:
“Dix influenced Midjourney.”

Similarity is not influence.

CITATION TRAIL:
[[MJ-GC-016]]
→ users “hacked together remix before it existed”
→ Dix 2007
→ recurring unforeseen uses can be learned from and redesigned into tools
→ “bug becomes feature” sharpens into DESIGN FROM APPROPRIATION.

TEST:
Recover contemporaneous Discord messages, Midjourney announcements, release notes, or developer statements concerning early Remix.

Establish separately:
1. what users actually did,
2. whether developers observed it,
3. whether that practice motivated the official feature,
4. which parts of the workaround survived formalization.

PLATFORM:
Human-computer interaction / Midjourney

LINKS:
[[MJ-GC-016]]
[[MJ-GC-002]]
[[MJ-GC-014]]

BIBTEX:
@inproceedings{dix2007appropriation,
  author={Dix, Alan},
  title={Designing for Appropriation},
  booktitle={Proceedings of BCS HCI 2007, People and Computers XXI, Volume 2},
  year={2007},
  url={https://alandix.com/academic/papers/HCI2007-appropriation/}
}
