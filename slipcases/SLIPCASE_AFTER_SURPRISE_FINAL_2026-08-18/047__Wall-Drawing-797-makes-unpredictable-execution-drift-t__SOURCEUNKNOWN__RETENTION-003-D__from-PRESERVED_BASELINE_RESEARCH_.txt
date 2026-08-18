ZETTEL

ID:
RETENTION-003-D

TITLE:
Wall Drawing 797 makes unpredictable execution drift the content of a deterministic instruction.

SOURCE:
Sol LeWitt — Wall Drawing 797 — October 1995 — primary instruction and installation record preserved by MASS MoCA.

PASSAGE:
[PARAPHRASE]
A first draftsman makes an irregular line. A second attempts to copy that line without touching it; a third copies the second; a fourth copies the third. The cycle continues downward, with small differences accumulating through repeated human copying.

RESEARCH OBJECT:
THE RULE CAN BE FIXED WHILE THE TRAJECTORY IS UNPREDICTABLE.

LOCAL MOVE:
RETENTION-003 emphasizes decisions frozen upstream.

Wall Drawing 797 freezes the algorithm while making executor-specific deviation the mechanism that generates the final form.

SOURCE TERMS:
copy
irregular line
previous draftsman
without touching
repetition
unpredictable
altered

WHAT BECAME STRANGE:
LeWitt need not predict the visible output.

He specifies a process designed to magnify deviations he cannot predict.

The unplanned differences are not failures of execution.

They are what the instruction makes visible.

QUESTION:
Can unpredictability itself be an authored property of a generative process?

DEEPER QUESTION:
What is the difference between an accident outside a work’s rules and variation deliberately made consequential by those rules?

MECHANISM:
initial line L₀

then recursively:

draftsman_i observes L_i
→ attempts copy
→ produces L_{i+1}

with:

    L_{i+1} ≠ L_i

through unavoidable execution difference.

Repeated iteration amplifies variation.

FORMAL SHIFT:
<FIXED RULE>
+
<IMPERFECT REPLICATION>
→ [ITERATION]
→ <EMERGENT UNPREDICTED FORM>

SOURCE FORMALISM:
The primary instruction specifies serial copying from the immediately preceding line.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

    L_{t+1} = Copy(L_t, ε_t)

where:

    ε_t

represents executor-specific deviation.

The artist controls the recurrence relation more strongly than the realized sequence:

    {L_0,L_1,...,L_n}.

TENSION:
Calling ε “noise” may misdescribe skilled embodied differences that are meaningful contributions of particular draftsmen.

MISSING:
Whether LeWitt regarded executor differences as noise, interpretation, performance, or contribution in his own terminology.

BOUNDARY:
LACK OF OUTPUT PREDICTION does not imply LACK OF CONTROL OVER THE PROCESS THAT MAKES OUTPUT VARIATION POSSIBLE.

CITATION TRAIL:
[[RETENTION-003]]
→ stored procedural decisions
→ Wall Drawing 797
→ fixed recurrence produces unpredictable realization
→ separate process control from trajectory control.

TEST:
Run a digital simulation with:

A.
perfect copying

B.
small random perturbations

C.
human copying.

Hold the recurrence rule constant.

Compare which features emerge only when the executor contributes non-identical replication.

PLATFORM:
[[class-is-not-a-path]]

LINKS:
[[RETENTION-003]]
[[wall-drawing-797]]
[[process-control]]
[[trajectory-control]]
[[iterated-drift]]

BIBTEX:
NONE
