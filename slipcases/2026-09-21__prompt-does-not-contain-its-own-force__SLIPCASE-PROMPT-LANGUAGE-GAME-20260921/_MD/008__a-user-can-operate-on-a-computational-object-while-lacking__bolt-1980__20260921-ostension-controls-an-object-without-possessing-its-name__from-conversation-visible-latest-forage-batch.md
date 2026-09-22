ZETTEL

ID:
20260921-ostension-controls-an-object-without-possessing-its-name

TITLE:
A User Can Operate on a Computational Object While Lacking the Vocabulary Needed to Describe It

SOURCE:
Richard A. Bolt — “‘Put-that-there’: Voice and gesture at the graphics interface” — 1980 — SIGGRAPH ’80. ([media.mit.edu](https://www.media.mit.edu/speech/papers/1980/bolt_SIGGRAPH80_put-that-there.pdf?utm_source=chatgpt.com))

PASSAGE:
[PARAPHRASE] Bolt’s multimodal design lets the user identify source and destination through pointing while speech supplies the operative relation. Deictic forms such as “that” and “there” can replace elaborate verbal descriptions of the selected item and location.

RESEARCH OBJECT:
Operational reference without descriptive possession of the object’s name or properties.

LOCAL MOVE:
The source separates the ability to pick out an entity from the ability to describe it propositionally.

SOURCE TERMS:
that
there
pointing
cursor
reference
move
gesture

WHAT BECAME STRANGE:
Control does not require a shared descriptive vocabulary for the controlled object. A user can know which thing they mean without knowing what the system calls it.

QUESTION:
How much prompting difficulty comes from forcing users to convert perceptual identification into verbal description before the machine can act?

DEEPER QUESTION:
When a world is directly addressable, should natural language describe relations and intentions while pointing, selection, and object identity carry reference?

MECHANISM:
world displays candidate objects
→ user perceptually identifies object
→ gesture binds referent
→ short linguistic operation supplies relation
→ executor applies relation to bound entity.

FORMAL SHIFT:
<DESCRIBE OBJECT TO IDENTIFY IT>
→ <OSTENSIVELY BIND OBJECT>
→ [STATE OPERATION]
→ <ACT WITHOUT NAMING>

SOURCE FORMALISM:
Bolt combines continuously sensed pointing with spoken deixis and action vocabulary. ([media.mit.edu](https://www.media.mit.edu/speech/papers/1980/bolt_SIGGRAPH80_put-that-there.pdf?utm_source=chatgpt.com))

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
prompt burden =
reference burden + relational burden + constraint burden

Direct selection can drive reference burden toward zero words.

TENSION:
Pointing works only when the intended entity is already perceptually or spatially available; many generative tasks concern entities that do not yet exist.

MISSING:
Interfaces that smoothly shift between ostension for existing things and description for not-yet-existing things.

BOUNDARY:
Bolt’s objects already exist on a visible screen. The result does not remove the need for descriptive language in constructive or hypothetical reference.

CITATION TRAIL:
[[20260921-put-that-there-lets-user-omit-the-object-name]]
→ deictic binding
→ control and naming separate into different competencies.

TEST:
Give users an unfamiliar 3D assembly with system-generated part names hidden. Compare text-only control against direct selection + short relational language for modification tasks.

PLATFORM:
[[prompt-stabilization]]

LINKS:
[[20260921-put-that-there-lets-user-omit-the-object-name]]
[[ostension]]
[[reference]]
[[direct-manipulation]]

BIBTEX:
@inproceedings{bolt1980put,
  author = {Bolt, Richard A.},
  title = {{``Put-that-there'': Voice and Gesture at the Graphics Interface}},
  booktitle = {Proceedings of SIGGRAPH 1980},
  year = {1980},
  pages = {262--270},
  publisher = {ACM},
  doi = {10.1145/800250.807503}
}
