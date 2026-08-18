ZETTEL

ID:
PROMPT-PRACTICE-TALKBACK-006

TITLE:
THE OUTPUT IS NOT THE ANSWER; IT IS THE MATERIAL THAT TELLS YOU WHAT YOU WERE ACTUALLY ASKING.

SOURCE:
Donald A. Schön — “Designing as Reflective Conversation with the Materials of a Design Situation” — Research in Engineering Design 3, 1992, pp. 131–147.

SOURCE URL:
https://doi.org/10.1007/BF01580516

PASSAGE:
[QUOTE]
“reflective conversation with the materials of a design situation”

RESEARCH OBJECT:
ARTIFACT-AS-INTERLOCUTOR.

A generated artifact does not merely satisfy or violate a prior specification.

It can change what the specification becomes.

LOCAL MOVE:
[[SON-IEC-005-A]] made predetermined objectives potentially deceptive.

[[SON-IEC-005-C]] showed that even retained history can become an attractor.

Schön supplies an older design lineage in which making proceeds through moves whose consequences cause the practitioner to SEE the situation differently.

This places pressure on any claim that artifact-driven correction is itself historically new.

The novelty must lie elsewhere.

SOURCE TERMS:
reflective conversation
materials
design situation
design intention
knowing-in-action
designing

WHAT BECAME STRANGE:
There are at least two different correction loops.

ERROR CORRECTION:

I knew what I wanted.
The artifact failed.
I correct the artifact.

SPECIFICATION DISCOVERY:

I thought I knew what I wanted.
The artifact showed me a distinction I had not represented.
I change what “wanted” means.

The second loop cannot be described adequately as convergence toward a fixed target.

QUESTION:
How can prompt histories distinguish ERROR CORRECTION from SPECIFICATION DISCOVERY?

DEEPER QUESTION:
If the artifact can change the evaluator's criteria, what object is actually converging during iterative prompting?

MECHANISM:
A practitioner makes a move.

The transformed situation presents consequences.

Some consequence is surprising or salient.

The practitioner reframes the situation.

A subsequent move is made under the changed framing.

Prompt generation creates an unusually rapid computational version of this sequence:

DESCRIPTION
→ GENERATION
→ PERCEPTION
→ REFRAMING
→ DESCRIPTION'.

FORMAL SHIFT:
FROM:

SPEC S
→ ARTIFACT A
→ compare A to S
→ improve A toward S

TO:

S_t
→ generate A_t
→ encounter consequence C_t
→ reinterpret S_t
→ S_t+1
→ generate again.

The specification itself becomes stateful.

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

S_t = current specification
A_t = G(S_t)
J_t = evaluation(A_t | S_t)

Ordinary optimization assumes:

S_t = S₀
for all t.

Reflective specification allows:

S_t+1 =
REFRAME(S_t, A_t, J_t).

Then:

ΔS ≠ 0

is not specification error.

It is part of the process.

TENSION:
Reflective design long predates generative AI.

Therefore:

artifact reveals requirement

cannot by itself establish novelty for contemporary prompting.

A stronger novelty candidate is the combination:

NATURAL-LANGUAGE DESCRIPTION
+
IMMEDIATE COMPUTATIONAL EXECUTION
+
HIGH-FIDELITY ARTIFACT
+
RAPID REFORMULATION
+
PRESERVABLE GENEALOGY.

MISSING:
A quantitative or operational distinction between:

correction
reframing
preference drift
mere indecision.

Evidence that generated artifacts reveal previously unrepresented variables at a rate or scale different from earlier sketch/prototype practices.

BOUNDARY:
Schön studies professional designing.

The source does not describe LLM prompting or software synthesis.

Its role is genealogical opposition: it removes “artifact talks back” as an easy novelty claim.

CITATION TRAIL:
[[SON-IEC-005-A]]
→ fixed objective may mislead search

[[SON-IEC-005-C]]
→ prior context can constrain exploration

→ Schön
→ design situation talks back through consequences
→ evaluator reframes
→ prompt loop must model SPECIFICATION CHANGE, not only output correction

TEST:
Code every correction in a real prompt genealogy as one of:

A. OUTPUT ERROR:
criterion existed before generation.

B. SPECIFICATION DISCOVERY:
criterion first became articulable after seeing generation.

C. PREFERENCE CHANGE:
criterion existed but changed.

D. MODEL COMPENSATION:
criterion is introduced only to counter model behavior.

Measure the distribution.

If B is common and consequential, the genealogy contains genuine deferred specification rather than simple iterative optimization.

PLATFORM:
Research in Engineering Design

LINKS:
[[SON-IEC-005-A]]
[[SON-IEC-005-C]]

BIBTEX:
@article{schon1992designing,
  author = {Donald A. Sch{\"o}n},
  title = {Designing as Reflective Conversation with the Materials of a Design Situation},
  journal = {Research in Engineering Design},
  volume = {3},
  pages = {131--147},
  year = {1992},
  doi = {10.1007/BF01580516},
  url = {https://doi.org/10.1007/BF01580516}
}
