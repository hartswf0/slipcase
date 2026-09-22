ZETTEL

ID:
20260921-bolt-medium-is-executed-without-being-said

TITLE:
“Create a Blue Square There” Also Creates “Medium,” Even Though Nobody Says Medium

SOURCE:
Richard A. Bolt — “‘Put-that-there’: Voice and gesture at the graphics interface” — 1980 — SIGGRAPH ’80, pp. 262–270. ([media.mit.edu](https://www.media.mit.edu/speech/papers/1980/bolt_SIGGRAPH80_put-that-there.pdf?utm_source=chatgpt.com))

PASSAGE:
[PARAPHRASE] Bolt’s example command is “Create a blue square there.” The location comes from the pointing cursor at the instant “there” is spoken. The square’s size is not linguistically specified at all: the system supplies its default value, “medium.” Color and shape, by contrast, have no defaults and must be supplied.

RESEARCH OBJECT:
One executed object whose parameters originate from three different places: spoken language, synchronized gesture, and an interface default.

LOCAL MOVE:
The source makes omission operationally heterogeneous. An omitted coordinate would leave the command without its intended destination, an omitted color or shape is disallowed, while an omitted size silently acquires a value.

SOURCE TERMS:
there
x,y cursor
medium
default size
color
shape
Create routine
parameter

WHAT BECAME STRANGE:
The final blue medium square looks like one unified response to one unified command, but “blue,” “square,” position, and size have four different provenance stories. Looking only at the sentence conceals which parts the user actually specified.

QUESTION:
Should correspondence between prompt and result be evaluated parameter by parameter according to who or what supplied each value?

DEEPER QUESTION:
Can a generated artifact be accompanied by a provenance map that distinguishes explicitly stated, gesturally supplied, contextually inferred, defaulted, retrieved, and autonomously chosen properties?

MECHANISM:
“blue”
→ speech supplies COLOR

“square”
→ speech supplies SHAPE

“there”
→ synchronizes pointer sampling
→ gesture supplies POSITION

SIZE absent
→ interface reads default
→ MEDIUM

all parameters
→ Create routine
→ object instantiated.

FORMAL SHIFT:
<ONE COMMAND → ONE OBJECT>
→ <MULTIPLE PARAMETER SOURCES → ONE OBJECT>
→ [ASSEMBLE ARGUMENTS]
→ <EXECUTED COMPOSITE SPECIFICATION>

SOURCE FORMALISM:
Bolt explicitly describes the complete utterance as a call to a Create routine with parameters, identifies the x,y cursor as the source of location, and states that medium is the default size.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
object.property_source =
{
  color: USER_LANGUAGE,
  shape: USER_LANGUAGE,
  position: USER_GESTURE,
  size: SYSTEM_DEFAULT
}

TENSION:
Modern generative models may not expose stable object properties or a deterministic parameter binding stage; a visual attribute may emerge jointly from many tokens and hidden model state.

MISSING:
A provenance representation for generated properties that are not clean arguments to an explicit constructor.

BOUNDARY:
Bolt’s system can identify parameter provenance because its graphical operations are deliberately structured. The case does not show that arbitrary model generations admit equally clean decomposition.

CITATION TRAIL:
[[20260921-there-is-a-timed-coordinate-sample]]
→ Bolt’s omitted-size example
→ synchronization is only one source of hidden specification; defaults are another.

TEST:
Instrument a world-building command so every resulting property is labeled EXPLICIT, POINTED, DEFAULTED, INFERRED, RETRIEVED, or MODEL-CHOSEN. Compare that map with what users believe they specified.

PLATFORM:
[[prompt-comparison]]

LINKS:
[[20260921-there-is-a-timed-coordinate-sample]]
[[parameter-provenance]]
[[default]]
[[put-that-there]]

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
