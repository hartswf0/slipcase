ZETTEL

ID:
Z-RF-20260817-005

TITLE:
Trial and error is not noise around prompting; it is part of the interaction form.

SOURCE:
Vivian Liu, Lydia B. Chilton — “Design Guidelines for Prompt Engineering Text-to-Image Generative Models” — arXiv:2109.06977, 2021; revised 2023.

PASSAGE:
[PARAPHRASE]
Liu and Chilton characterize open-ended text interaction as double-edged: users can enter almost anything, but poor results force brute-force trial and error. Their evaluation covers 5,493 generations across five experiments, 51 subjects, and 51 styles.

RESEARCH OBJECT:
The apparent freedom of an unconstrained text box transfers specification work from interface structure into repeated empirical correction.

LOCAL MOVE:
The source gives [[Z-AIACS-016]] an earlier empirical basis: correction is not merely how experts polish prompts but a recurring consequence of open-ended text as an interaction modality.

SOURCE TERMS:
“open-ended”
“text as interaction”
“brute-force trial and error”
“subject”
“style”
“success and failure modes”

WHAT BECAME STRANGE:
The interface appears maximally expressive because it accepts arbitrary language, yet this same absence of explicit structure can make users discover the system’s constraints by failure.

QUESTION:
Does natural-language freedom reduce formalization, or merely defer formalization until after generation?

DEEPER QUESTION:
Could the repeated correction sequence be the interface’s missing specification language appearing temporally rather than syntactically?

MECHANISM:
underspecified / mismatched description
→ generation
→ visible failure
→ inferred missing constraint
→ prompt revision
→ regeneration

FORMAL SHIFT:
<open-ended intention>
→ <provisional text>
→ [GENERATE AND INSPECT]
→ <newly discovered constraint>

SOURCE FORMALISM:
The paper experimentally varies prompt keywords and model hyperparameters, examining coherent outputs and success/failure modes across thousands of generations.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

S_0 = initial specification

G(S_0) → failure evidence E_0

S_1 = S_0 ∪ constraint(E_0)

The effective specification is accumulated over executions rather than completed before execution.

TENSION:
Prompt interfaces are often described as lowering the need for formal specification. The documented trial-and-error burden suggests that specification may still occur, but after execution and through perceptual diagnosis.

MISSING:
Process data showing exactly which constraints users infer from each failed generation.

BOUNDARY:
Liu and Chilton document trial-and-error interaction and design guidelines. They do not name the process “deferred formalization.”

CITATION TRAIL:
[[Z-AIACS-016]]
→ Liu & Chilton
→ brute-force correction as an empirical feature of open-ended text interaction
→ recover failure-to-constraint transitions
→ compare with conventional programming/debugging

TEST:
Record complete screen, prompt, parameter, and output histories for a generation task. After every revision, ask the user what newly discovered constraint caused the edit. Reconstruct the specification in the order it became explicit.

PLATFORM:
[[Deferred Formalization]]

LINKS:
[[Z-AIACS-016]]
[[Failure Becomes Specification]]
[[Prompt History]]
[[Describe Generate Inspect Correct]]

BIBTEX:
@misc{LiuChilton2021PromptEngineering,
  author = {Vivian Liu and Lydia B. Chilton},
  title = {Design Guidelines for Prompt Engineering Text-to-Image Generative Models},
  year = {2021},
  eprint = {2109.06977},
  archivePrefix = {arXiv},
  primaryClass = {cs.HC},
  doi = {10.48550/arXiv.2109.06977}
}
