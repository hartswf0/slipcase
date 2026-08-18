ZETTEL

ID:
PROMPT-ONTOLOGY-002

TITLE:
Prompt research risks reviving the planning-model error: the available instruction is mistaken for the course of action.

SOURCE:
Lucy A. Suchman — “Plans and Situated Actions: The Problem of Human-Machine Communication” — Cambridge University Press — 1987 — SOURCE URL: https://www.cambridge.org/core/books/humanmachine-reconfigurations/9D53E602BA9BB5209271460F92D00EFE

PASSAGE:
[PARAPHRASE] Suchman’s critique distinguishes plans from situated action. Plans are consequential resources but do not determine the detailed course of situated conduct; retrospective accounts can make action appear to conform to a plan while suppressing the contingent work by which the action was actually produced.

RESEARCH OBJECT:
PROMPT AS PLAN / EXECUTION AS SITUATED ACTION.

The relation is not an identity claim. It is a diagnostic analogy that exposes a recurring representational mistake: substituting an instruction available to the analyst for the event whose production the instruction only partly organizes.

LOCAL MOVE:
Move from CONTEXT AS MISSING INFORMATION to SITUATION AS CONSTITUTIVE OF OPERATIVE MEANING.

SOURCE TERMS:
plans
situated actions
planning model
human-machine communication
situatedness
resources for action

WHAT BECAME STRANGE:
HCI may be rebuilding a distinction it previously learned to distrust. The prompt is visible before execution and legible afterward, making it unusually easy to reconstruct behavior as “following the prompt.”

QUESTION:
Is “prompt following” sometimes a retrospective reconstruction analogous to treating situated action as the execution of a plan?

DEEPER QUESTION:
What would prompt scholarship look like if the prompt were treated as a resource within situated execution rather than the script that determines it?

MECHANISM:
The written instruction supplies orientation and constraints. Runtime contingencies, model state, surrounding materials, and interaction reorganize what happens. Retrospective comparison of prompt and output can erase those contingencies by reading the result back into the instruction.

FORMAL SHIFT:
FROM:
PROMPT → EXECUTION

TO:
PROMPT ∈ RESOURCES-FOR-EXECUTION
and
EXECUTION emerges from situated relations not exhausted by PROMPT.

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

If A is observed action and P is a prior plan/instruction, then correspondence(A,P) does not establish determination(A|P).

Applied to prompting:
correspondence(output,prompt) ≠ located causal mechanism.

TENSION:
Prompts differ from human plans because generative models are explicitly engineered to condition behavior on input tokens. The analogy cannot erase genuine computational conditioning. Its force is narrower: conditioning does not establish that the visible inscription is the complete or stable causal unit.

MISSING:
Empirical work that separates prospective instruction, runtime assembly, internal state changes, and retrospective attribution in actual prompt systems.

BOUNDARY:
Suchman studied human-machine interaction and situated human action, not contemporary LLM prompting. This is a conceptual crossing, not a historical claim of influence.

CITATION TRAIL:
[[PROMPT-ONTOLOGY-001]]
→ prompt stabilized as an analyzable inscription
→ Suchman’s plan/action distinction
→ prompt as resource rather than determining script
→ causal reconstruction becomes the object of inquiry.

TEST:
For a prompt experiment, record not only the initial text and final output but every runtime material available to the system. Ask which post-hoc explanations of the output remain possible if the original prompt is hidden from analysts. Compare those accounts with the explanation produced when the prompt is visible.

PLATFORM:
HCI; situated action; prompt research as conceptual application.

LINKS:
[[PROMPT-ONTOLOGY-001]] [[DEFAULT-IMAGES-CHI26-B-1]]

BIBTEX:
@book{Suchman1987Plans,
  author={Suchman, Lucy A.},
  title={Plans and Situated Actions: The Problem of Human-Machine Communication},
  publisher={Cambridge University Press},
  year={1987}
}
