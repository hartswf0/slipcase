```text
ZETTEL

ID:
HOUSE-COMP-006

TITLE:
APT GIVES LANGUAGE STATEMENTS MACHINING SEMANTICS: PROGRAM TEXT CAN TERMINATE IN PHYSICAL TOOL MOTION.

SOURCE:
Bradford M. Smith — Guidelines for Exchangeable APT Data Packages: APT Part Programmer’s Manual — National Bureau of Standards — 1980.

PASSAGE:
[QUOTE]
“It defines the machining function which will result from the use of each statement.”

RESEARCH OBJECT:
A FORMAL SEMANTICS WHOSE OUTPUT IS MACHINE ACTION.

LOCAL MOVE:
APT documentation treats a programming statement as having defined machining consequences; processors and postprocessors translate the language into machine-specific control.

SOURCE TERMS:
APT; part program; language statement; syntax; semantics; machining function; postprocessor; machine tool

WHAT BECAME STRANGE:
Here “language changes matter” requires almost no metaphor. The statement does not cut metal, but its defined semantics enter a technical chain that produces machine motion.

QUESTION:
Is numerical-control programming the historical point at which “description becomes construction” becomes an engineering fact rather than a philosophical metaphor?

DEEPER QUESTION:
What distinguishes an architectural specification interpreted by a builder from an APT statement interpreted by a postprocessor?

MECHANISM:
APT statements specify machining intentions; processor and postprocessor translate them into instructions usable by numerical-control equipment; the controller produces machine actions.

FORMAL SHIFT:
<DESIRED MACHINED FORM>
→ <APT STATEMENTS>
→ [PROCESS + POSTPROCESS]
→ <MACHINE FUNCTION / TOOL MOTION>

SOURCE FORMALISM:
APT language syntax; modifiers; scalar values; defined machining functions; postprocessor semantics.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
SOURCE CODE → PROCESSOR → MACHINE-SPECIFIC CODE → ACTUATOR MOTION → MATERIAL REMOVAL → PART.

TENSION:
APT makes language materially operative by radically constraining what can be said: natural language gains flexibility by tolerating ambiguity; machine language gains reliability by excluding it.

MISSING:
Assembly; whole-building sequencing; material handling; joining; site variation; perception; recovery from unexpected conditions.

BOUNDARY:
APT controls numerical machine tools; it does not design architectural objects, understand ordinary language, or construct complete buildings.

CITATION TRAIL:
APT history; numerical control; G-code / RS-274; CAD/CAM; STEP-NC; robotic fabrication; additive manufacturing; construction robotics.

TEST:
Encode one fabrication instruction as ordinary English, architectural specification, APT/G-code, and robot control; compare allowable ambiguity at each layer.

PLATFORM:
[[THE HOUSE THAT WORDS BUILT]]

LINKS:
[[HOUSE-COMP-000]]
[[LANGUAGE TO MATTER]]
[[THE LAST INTERPRETER BEFORE MATTER]]

BIBTEX:
@techreport{smith1980apt, author={Smith, Bradford M.}, title={Guidelines for Exchangeable APT Data Packages: APT Part Programmer's Manual}, institution={National Bureau of Standards}, number={NBSIR 80-2073.2}, year={1980}}
```
