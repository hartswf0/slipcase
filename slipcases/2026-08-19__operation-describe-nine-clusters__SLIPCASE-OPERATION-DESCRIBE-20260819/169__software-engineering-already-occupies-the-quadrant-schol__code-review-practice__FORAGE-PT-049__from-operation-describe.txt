ZETTEL

ID: FORAGE-PT-049

TITLE: Software engineering already occupies the quadrant scholarship left empty — it records the objection and its resolution together

SOURCE: Version control and code-review practice: commit history plus review threads in which an objection, the response, and the resulting change are all preserved and linked [no specific study claimed]; read against [[FORAGE-PT-022]]

PASSAGE: [PARAPHRASE] In ordinary code-review practice a reviewer records an objection against a specific line, the author replies or revises, and the thread, the revision and the final state are retained together in the project's history. [QUOTE] dse.json: "{ ... <public_criterion>, <correction>, <ethical_consequence> }" [QUOTE] memex.json: "judged by <path integrity>, not by <answer fluency>"

RESEARCH OBJECT: An existing institution satisfying both honesty criteria at once. Traceability is met — every change resolves to an author, a time and a diff. Struggle is met — the objection that prompted the change is preserved next to it, with the reasoning and the disagreement intact. The parent predicted the high-high quadrant would be nearly empty. It is populated, and not by scholarship.

LOCAL MOVE: This child falsifies the parent's emptiness prediction by locating the counterexample, and reads the counterexample for what scholarship would have to adopt.

SOURCE TERMS: commit history / diff / review thread / objection / resolution / blame

WHAT BECAME STRANGE: The discipline that produced the theory of untransferable understanding is also the one that built the best apparatus for recording answerability. Naur said the text is a residue and the theory lives in the team; the same field then developed a practice in which the *disagreements* about the text are retained. Those disagreements are the closest thing to an inscription of the shared theory, and Naur's own lineage never claimed them as such.

QUESTION: Does a preserved objection-and-resolution record let a newcomer reconstruct the theory better than the code plus prose documentation alone?

DEEPER QUESTION: If review threads carry reconstructive power, then the transferable residue is not the artifact or its explanation but the *record of what was rejected* — the negative space of the design. That is the same finding as constraint outperforming description, arrived at from a different direction.

MECHANISM: <PROPOSED CHANGE> -> [REVIEWER OBJECTS, CITING A CRITERION] -> [AUTHOR REVISES OR DEFENDS] -> [RESOLUTION RECORDED WITH THE DIFF] -> <ARTIFACT PLUS THE ARGUMENT THAT SHAPED IT, BOTH INSCRIBED>

FORMAL SHIFT: <FINISHED ARTIFACT> -> <ARTIFACT PLUS OBJECTION HISTORY> -> [READ THE REJECTED ALTERNATIVES] -> <DESIGN RATIONALE AS A PUBLIC OBJECT>

SOURCE FORMALISM: NONE — a practice, not a formalism. The data structures (commits, threads, diffs) are conventional and not quoted.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Score an artifact on S (share of changes carrying a recorded objection) and T (share of content resolving to an authored, timed change). Code review scores high on both. Scholarly monographs score high on T for citations and near zero on S. The gap is not a difference in rigour but in whether the medium retains rejection.

TENSION: READING A: code review genuinely occupies the quadrant and scholarship should adopt it — preserved objection is the missing apparatus. READING B: review threads record objections that were *raised*, which is a small and socially filtered subset of the objections that occurred; the author's own rejected attempts, made privately before submission, are absent — so the record captures interpersonal challenge, not descriptive struggle.

Reading B is strong: the struggle dse describes is largely pre-submission, and review begins after it.

MISSING: Any study of whether review threads aid reconstruction. Any comparison between objections raised in review and revisions made before review, which is where Reading B's missing mass would be.

BOUNDARY: This is an observation about a practice, not evidence that the practice transfers understanding. The reconstruction claim is exactly what the test would decide.

CITATION TRAIL: [[FORAGE-PT-022]] and [[FORAGE-PT-023]] -> code-review practice -> objection history as inscribed answerability -> next: design-rationale research, which attempted to capture rejected alternatives systematically and largely failed to be adopted — a cautionary precedent.

TEST: Two newcomers, one system. One receives code plus prose documentation; the other receives code plus the review history. Both attempt the same modification. Blind coherence scoring by a maintainer. If the review-history arm wins, rejection is the transferable residue.

PLATFORM: [[rejection-is-the-residue]]

LINKS: [[FORAGE-PT-016]] [[FORAGE-PT-022]] [[FORAGE-PT-023]] [[FORAGE-PT-053]]

BIBTEX: @misc{code_review_practice, title={Version control and code review as an objection-preserving record}, note={Practice description; no specific study claimed in this forage}, year={2026}}
