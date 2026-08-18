ZETTEL

ID:
BGS-1884-22

TITLE:
Prompt craft is not speaking a language; it is reverse-engineering one that never published its grammar

SOURCE:
Shambibble — interview with Watson Hartsoe — October 22, 2022 — 47:03–57:24. fileciteturn3file0L47-L103

PASSAGE:
[PARAPHRASE]
Shambibble says users copy long prompts without knowing which pieces matter; his own explanations rely on repeated empirical tests and simple toy examples. He describes learning system behavior by reading papers, searching old Discord posts, talking to programmers, and testing analogies rather than by consulting a complete specification. fileciteturn3file0L49-L59 fileciteturn3file0L97-L103

RESEARCH OBJECT:
The user is not programming against a published semantics.

The user is inferring an unknown semantics from behavior.

LOCAL MOVE:
The source turns “prompt language” into an empirical object rather than a conventional language system.

SOURCE TERMS:
empirically
hunches
toy examples
reading papers
Discord history
secret sauce
figure out how stuff worked

WHAT BECAME STRANGE:
A normal programming language lets the programmer reason:

expression
→ specified semantics
→ execution.

Here the practitioner reasons:

expression
→ unknown transformation
→ output
→ hypothesis about semantics.

The direction of knowledge is reversed.

QUESTION:
Can an instruction count as authorial control when the user must discover what the instruction means by observing what the machine does?

DEEPER QUESTION:
Is prompt expertise better described as experimental control of an unknown instrument than as linguistic command?

MECHANISM:
unknown interpreter
→ issue probe
→ observe output
→ infer association
→ alter probe
→ compare
→ retain provisional rule

FORMAL SHIFT:
<WORDS>
→ <OPAQUE INTERPRETER>
→ [PROBE / OBSERVE / UPDATE HYPOTHESIS]
→ <PROVISIONAL CONTROL MODEL>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Conventional language:

meaning = SEMANTICS(expression)

Prompt craft:

hypothesis_t
→ experiment
→ output
→ update(hypothesis_t+1)

The practitioner learns a local empirical semantics.

TENSION:
[[BGS-1884-18]] proposed that authorship may depend on control semantics.

But if those semantics are neither stable nor known in advance, authorship may depend on a user’s empirical mastery of behavior rather than the formal meaning of the instruction.

MISSING:
A distinction between:

knowing what words mean,
knowing what a system tends to do with them,
and actually controlling the resulting expression.

BOUNDARY:
The source documents Midjourney practice in 2022. It does not establish that all generative systems lack explicit or inspectable control semantics.

CITATION TRAIL:
[[BGS-1884-18]]
[[BGS-1884-21]]
→ empirical prompt craft
→ black-box system identification
→ compare prompting with programming, instrument calibration, and experimental control

TEST:
Give users an undocumented generative control and allow only input-output experimentation.

Measure whether they can acquire reliable control without ever learning the mechanism.

Then compare that control with a formally specified interface producing the same outputs.

PLATFORM:
[[Empirical Semantics]]

LINKS:
[[BGS-1884-18]]
[[BGS-1884-21]]
[[Prompting Is Not Programming]]
[[Black-Box Craft]]
[[System Identification]]

BIBTEX:
@misc{HartsoeShambibble2022,
  author = {Hartsoe, Watson and Shambibble},
  title = {Interview on Midjourney Prompt Craft},
  year = {2022},
  month = {10},
  note = {Interview conducted October 22, 2022}
}
