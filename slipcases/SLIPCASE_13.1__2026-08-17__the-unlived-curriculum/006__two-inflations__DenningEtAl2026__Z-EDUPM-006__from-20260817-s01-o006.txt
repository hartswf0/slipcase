ZETTEL

ID:
Z-EDUPM-006

TITLE:
“GRADE INFLATION” IS NOT ONE OPERATION: RAISING EVERYONE’S GRADES AND MOVING STUDENTS ACROSS THE FAILING THRESHOLD CAN HAVE OPPOSITE LONG-RUN EFFECTS.

SOURCE:
Jeffrey T. Denning, Rachel L. Nesbit, Nolan G. Pope, and Merrill Warnick — Easy A’s, Less Pay: The Long-Term Effects of Grade Inflation — 2026 — NBER Working Paper 34952.

SOURCE URL:
https://www.nber.org/papers/w34952

PASSAGE:
[PARAPHRASE] The authors construct two distinct teacher-level measures: average-grade inflation and a propensity to award passing grades. Higher average-grade inflation is associated with worse later test scores, graduation, postsecondary enrollment, and earnings; greater passing-grade inflation reduces retention in grade and increases high-school graduation, with limited long-run effects.

RESEARCH OBJECT:
“Grade inflation” decomposes into at least two mechanisms whose consequences need not point in the same direction.

LOCAL MOVE:
The paper refuses a single scalar notion of leniency.

It separates:
raising the overall grade distribution
from
changing outcomes near the pass/fail threshold.

SOURCE TERMS:
average grade inflation
passing grade inflation
teacher value-added
test scores
high school graduation
college enrollment
earnings
grading practices

WHAT BECAME STRANGE:
A blanket claim that grade inflation “corrupts the price signal” loses the exact place where grading policy acts.

An extra five points everywhere and converting an F into a D are both “leniency,” but they perform different institutional operations.

QUESTION:
Which part of the grade distribution is actually changing when a university says its standards have weakened?

DEEPER QUESTION:
Could attempts to “restore rigor” accidentally destroy beneficial threshold leniency while doing little about broad compression at the top?

MECHANISM:
MEAN INFLATION:
easier grades across distribution
→ changed effort/information
→ later outcomes

PASSING INFLATION:
threshold crossing near failure
→ avoids retention / earns credit
→ changed persistence
→ later outcomes

FORMAL SHIFT:
<GRADE LENIENCY>
→ [DECOMPOSE]
→ <DISTRIBUTIONAL SHIFT>
   OR
   <THRESHOLD SHIFT>
→ <DIFFERENT BEHAVIORAL CONSEQUENCES>

SOURCE FORMALISM:
The authors construct and validate two teacher-level measures:
1. average grade inflation;
2. propensity to give a passing grade.

They distinguish both from teacher value-added and estimate their associations/effects on later outcomes using linked administrative records.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

GRADE_INFLATION ≠ scalar

GRADE_INFLATION :=
{
  SHIFT_MEAN,
  CROSS_THRESHOLD,
  COMPRESS_TOP,
  ALTER_VARIANCE,
  ...
}

Different operators should not inherit one moral or causal interpretation.

TENSION:
The initial “market manipulation” analogy implies that increasing grades uniformly corrupts information.

This source suggests the consequences depend on exactly how the grading function changes.

MISSING:
Direct evidence that the same decomposition produces the same effects in universities.

BOUNDARY:
The study analyzes high-school teachers and explicitly leaves open whether the findings generalize to college grading.

It therefore cannot be used as direct evidence about university grade inflation.

CITATION TRAIL:
Gans & Kominers — informativeness and strategic manipulation of grading systems.
Butcher et al. — anti-grade-inflation policy at Wellesley.
Boleslavsky & Cotton — grading standards and education quality.
College-level studies of transcript informativeness.

TEST:
For university transcript data, decompose historical grade changes into:

mean shift,
pass/fail threshold shift,
upper-tail compression,
variance change.

Test each separately against:
subsequent-course performance,
major persistence,
graduate admissions,
and labor-market outcomes.

PLATFORM:
[[THE UNIVERSITY AS SIGNALING SYSTEM]]

LINKS:
[[Grade Inflation Is Not One Operation]]
[[Threshold Mercy Versus Signal Compression]]
[[Distributional Grading Mechanics]]

BIBTEX:
@techreport{denning2026easya,
  author      = {Denning, Jeffrey T. and Nesbit, Rachel L. and Pope, Nolan G. and Warnick, Merrill},
  title       = {Easy A's, Less Pay: The Long-Term Effects of Grade Inflation},
  institution = {National Bureau of Economic Research},
  type        = {Working Paper},
  number      = {34952},
  year        = {2026},
  doi         = {10.3386/w34952},
  url         = {https://www.nber.org/papers/w34952}
}