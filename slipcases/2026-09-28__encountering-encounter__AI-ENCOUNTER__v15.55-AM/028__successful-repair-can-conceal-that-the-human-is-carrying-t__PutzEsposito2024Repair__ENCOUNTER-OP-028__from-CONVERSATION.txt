ZETTEL

ID:
ENCOUNTER-OP-028

TITLE:
Successful repair can conceal that the human is carrying the encounter.

SOURCE:
Ole Pütz and Elena Esposito — “Performance without understanding: How ChatGPT relies on humans to repair conversational trouble” — 2024 — Discourse & Communication 18(6). ([journals.sagepub.com](https://journals.sagepub.com/doi/10.1177/17504813241271492))

PASSAGE:
[PARAPHRASE] In ambiguous cases, ChatGPT often proceeds with a likely interpretation rather than initiating clarification; user-initiated repairs can redirect subsequent output, sometimes inconsistently. ([journals.sagepub.com](https://journals.sagepub.com/doi/10.1177/17504813241271492))

RESEARCH OBJECT:
Repair success and repair reciprocity are different variables.

LOCAL MOVE:
Pütz and Esposito introduce ambiguities and corrections to inspect how ChatGPT handles conversational trouble. The user frequently detects and specifies the repair that allows the dialogue to continue.

SOURCE TERMS:
repair
repair without understanding
third position repair
reference trouble
communicative competence
human direction
dialog history
misunderstanding

WHAT BECAME STRANGE:
A conversation can look collaboratively repaired even when one participant performs almost all trouble detection, diagnosis, and correction.

QUESTION:
Can repair-burden asymmetry distinguish fluent interaction from stronger encounter-like coupling?

DEEPER QUESTION:
How much human compensatory work can occur before “bidirectional coupling” becomes a misleading description?

MECHANISM:
ambiguous user turn
→ model selects interpretation
→ output exposes mismatch
→ human diagnoses mismatch
→ human reformulates/corrects
→ model conditions on corrective text
→ locally plausible continuation.

FORMAL SHIFT:
<REPAIR SUCCESS>
→ <REPAIR LABOR DISTRIBUTION>
→ [ACTOR-SENSITIVE CODING]
→ <ASYMMETRY PROFILE>

SOURCE FORMALISM:
The paper contrasts:
BOT-INITIATED handling of potential trouble
with
USER-INITIATED third-position repair,
and examines how revised user wording conditions subsequent model output. ([journals.sagepub.com](https://journals.sagepub.com/doi/10.1177/17504813241271492))

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

HUMAN_REPAIR_BURDEN =
human_detected_troubles / all_detected_troubles

AI_REPAIR_INITIATIVE =
AI_initiated_clarifications / ambiguity_opportunities

RECOVERY_FIDELITY =
resolved_without_reintroducing_conflict / repair_attempts

Encounter reciprocity requires reporting these separately from overall task success.

TENSION:
[[ENCOUNTER-AI-016]] requires recursive bidirectional coupling. Pütz and Esposito show that apparent recursion may be strongly directionally dependent.

MISSING:
Large-scale controlled comparisons across current models rather than illustrative GPT-3.5 dialogues.

BOUNDARY:
The authors’ examples do not establish that all LLM repair is human-driven, nor that successful repair never reflects useful model-side processing.

CITATION TRAIL:
[[ENCOUNTER-OP-027]]
[[ENCOUNTER-AI-016]]
→ Pütz and Esposito 2024
→ model comparisons
→ repair opportunity benchmark
→ directional encounter metrics.

TEST:
Generate a benchmark of minimally different ambiguous turns with known alternative interpretations. Measure whether the model:
detects ambiguity,
asks a discriminating question,
maintains both alternatives,
updates after correction,
and avoids reverting.
Compare those scores with ordinary “repair success.”

PLATFORM:
[[Operational Encounter Model]]

LINKS:
[[ENCOUNTER-006]]
[[ENCOUNTER-AI-016]]
[[Human Repair Burden]]
[[Repair Without Understanding]]

BIBTEX:
@article{PutzEsposito2024Repair,
  author = {Ole P{\"u}tz and Elena Esposito},
  title = {Performance without understanding: How ChatGPT relies on humans to repair conversational trouble},
  journal = {Discourse \& Communication},
  year = {2024},
  volume = {18},
  number = {6},
  doi = {10.1177/17504813241271492}
}