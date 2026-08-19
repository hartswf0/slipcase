ZETTEL

ID:
FORAGE-OD-024

TITLE:
THE ONE ROUTING SYSTEM WITH COMPLETE LOGS, NO IRB, AND NO PLATFORM GATEKEEPER IS THE ARCHIVE ITSELF

SOURCE:
OPERATION DESCRIBE repository — COSMIC_LAW.md (mtime 2026-04-13), PROGRAMS/CLAUDE.md (mtime 2026-04-27), git history 2026-04-20 to 2026-06-04, worldtext/chronicle.md (730 lines); against PAPERS/operation-describe-label-00.md §4 "Evidence Questions" and §12 "Scope Questions"

PASSAGE:
[QUOTE]
label-00 §4:
"Can I get access to the data? If I cannot get access, what is my backup? Can I actually study moderation routing, or am I relying on public documentation and hypothetical workflows?"

[QUOTE]
label-00 §12:
"Can I finish this with available data?"

RESEARCH OBJECT:
The archive's most serious practical risk is data access. Its answer (label-01 §4) is to fall back on public GitHub data and simulated moderation pipelines.

There is a third option it has not considered: a routing system where the descriptions are authored, versioned, and timestamped; the operator is available for introspection; the actions are commits; the outcomes are files; and nobody's consent is required.

The repository is a complete, ethically unproblematic instance of the phenomenon under study.

LOCAL MOVE:
COSMIC_LAW.md is not documentation. Read against the archive's own definition, it is a stack of operative descriptions: §10 "Anti-Patterns (Forbidden)", §11 "Governing Imperatives", §6 "Ingest Protocol" with eleven numbered steps that determine what gets written next.

PROGRAMS/CLAUDE.md goes further: eight numbered "CONSTITUTIONAL LAWS" declared "inviolable," each with a stated failure condition.

SOURCE TERMS:
COSMIC_LAW
governing imperatives
anti-patterns (forbidden)
ingest protocol
constitutional laws
inviolable
the operator governs
Explanation Gate

WHAT BECAME STRANGE:
The archive spent twenty numbered sections asking who controls the categories that route action, and the answer for its own primary evidence base is: the author, three months ago, in a file they may not have reread.

The dissertation about descriptions that route labor is being written by descriptions that route the author's labor. That is not a curiosity. It is the only case in the portfolio where the researcher has access to the describer's intentions *and* the complete action log.

QUESTION:
What does the archive's own routing analysis find when applied to the archive — which laws routed, which did not, and what distinguishes them?

DEEPER QUESTION:
If a research programme's governing documents can be shown to route its output, does that make the programme's findings *more* credible (the method works) or *less* (the findings were routed into existence)? The archive cannot have it both ways, and choosing is a genuine contribution.

MECHANISM:
<LAW WRITTEN IN COSMIC_LAW.md OR CLAUDE.md>
→ read by the author (or by a model acting for the author)
→ constrains what counts as an admissible next object
→ [COMMIT]
→ new files, new atlas rows, new chronicle entries
→ [FEEDBACK: worldtext/chronicle.md records the change]
→ next law revised

This is the prompt-output-revision loop the archive theorizes, running on the archive, with a durable log.

FORMAL SHIFT:
<GOVERNING DOCUMENT>
→ <ADMISSIBILITY CONSTRAINT>
→ [COMMIT]
→ <ARCHIVE STATE CHANGE>
→ <CHRONICLE ENTRY>

SOURCE FORMALISM:
COSMIC_LAW §2 supplies a nine-level scale law; §6 an eleven-step ingest protocol; §8 a twelve-item lint checklist. PROGRAMS/CLAUDE.md supplies eight laws, a twelve-step Naurian Loop, and an eight-item registration gate.

This is more explicit procedural machinery than any of the archive's three external cases provide.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Treat each numbered law as a description D_k with an issue date τ_k and a stated route R_k.

For each, compute:
  compliance_k  = fraction of post-τ_k objects satisfying R_k
  ΔG_k          = compliance_k − compliance before τ_k
  cost_k        = tokens/effort required to comply

Then classify:
  operative        : ΔG_k > 0
  dead letter      : ΔG_k ≈ 0, cost low        (nobody bothered)
  broken dependency: ΔG_k ≈ 0, cost high       (compliance would break something — see FORAGE-OD-023)
  performative     : ΔG_k ≈ 0, never checkable (see FORAGE-OD-025)

Four categories, from one repository, with dates. The archive currently has zero measured instances of any of them.

TENSION:
READING A: this is autoethnography and will be read as self-indulgence by a committee that wants platform-scale evidence.
READING B: it is the only case where every due-diligence question in label-00 can actually be answered — operator, authority, error, feedback, counterfactual, access, ethics — and refusing it because it is small is refusing the one case that is complete.

The strongest position is probably neither: use it as the *method-validation* case. Demonstrate the routing analysis works where everything is observable, then apply the validated instrument to GitHub where it is not.

MISSING:
Author-side data the git log cannot supply: which laws were reread, when, and whether the author was aware of them at the moment of writing. That is recoverable prospectively with a two-line logging habit, and not recoverable retrospectively.

BOUNDARY:
n = 1. The author is the researcher. No generalization to other operators is licensed. What is licensed is method validation and the discovery of failure categories.

CITATION TRAIL:
COSMIC_LAW.md §§6, 8, 10, 11.
PROGRAMS/CLAUDE.md LAWS 1–8 and the Registration Gate.
worldtext/chronicle.md — 730 lines of the archive's own feedback record, unanalyzed.
Second-order cybernetics: the observer inside the system — PAPERS/cyber-00.md §4.
FORAGE-OD-013, FORAGE-OD-023, FORAGE-OD-025, FORAGE-OD-027.

TEST:
Take the eight CONSTITUTIONAL LAWS in PROGRAMS/CLAUDE.md. For each, find the objects in /PROGRAMS/ created after 2026-04-27 and check compliance.

LAW 5 ("every theory must state what it cannot do") is checkable by grep for a Residual Human Theory section. LAW 3 (>80% overlap must merge) is not checkable at all. That asymmetry, measured across eight laws, is the finding.

PLATFORM:
[[the-repository-as-its-own-case]]

LINKS:
[[FORAGE-OD-023]]
[[FORAGE-OD-025]]
[[FORAGE-OD-013]]
[[FORAGE-OD-027]]
[[FORAGE-OD-018]]

BIBTEX:
@unpublished{hartsoe2026cosmiclaw,
  author = {Hartsoe, Watson},
  title = {COSMIC\_LAW — Operating Schema for OPERATION DESCRIBE},
  note = {OPERATION DESCRIBE archive, COSMIC\_LAW.md, version 1.0.0, compiled 2026-04-13},
  year = {2026}
}
