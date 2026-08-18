ZETTEL

ID:
CALLSHOT-FIELD-015

TITLE:
A “PROMPT” CAN NOW BE PACKAGED AS A REUSABLE SKILL CONTAINING INSTRUCTIONS, EXAMPLES, RESOURCES, AND CODE.

SOURCE:
OpenAI Help Center, “Skills in ChatGPT,” current documentation accessed 2026-08-17. SOURCE URL: https://help.openai.com/en/articles/20001066

PASSAGE:
[QUOTE]
“A skill can include instructions, examples, and code.”

RESEARCH OBJECT:
REPEATED PROMPT PRACTICE IS BEING REIFIED INTO PORTABLE PROCEDURAL OBJECTS.

LOCAL MOVE:
OpenAI describes Skills as reusable, shareable workflows that can include instructions, examples, supporting resources, code, and repeatable steps, and can be selected automatically when useful.

SOURCE TERMS:
“Skills” · “reusable” · “shareable” · “instructions” · “examples” · “code” · “steps”

WHAT BECAME STRANGE:
A prompt can acquire descendants, dependencies, resources, and procedural memory. Craft knowledge begins to have a package boundary.

QUESTION:
At what point does a refined prompt stop being a prompt and become a procedure?

DEEPER QUESTION:
Is the operative unit of natural-language programming the reusable workflow package rather than the sentence that invoked it?

MECHANISM:
REPEATED TASK → PROMPT → FAILURE → CORRECTION → STABILIZED PRACTICE → PACKAGE AS SKILL → REUSE / SHARE.

FORMAL SHIFT:
PROMPT STRING → VERSIONABLE PROCEDURAL OBJECT.

SOURCE FORMALISM:
[PARAPHRASE]
OpenAI describes Skills as workflows that can bundle instructions, examples, code, resources, and repeatable steps for consistent future use.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
SKILL={trigger_description, procedure, examples, resources, optional_code, constraints, checks}.

TENSION:
Packaging preserves validated craft and obsolete superstition with equal fidelity unless provenance and tests travel with the skill.

MISSING:
Versioned provenance that distinguishes documented invariant, experiment, convention, workaround, and unverified technique inside a skill.

BOUNDARY:
A skill remains interpreted by an agent and is not equivalent to a deterministic program.

CITATION TRAIL:
[[CALLSHOT-20260817-04]] → prompt principle becomes skill package → [[MJ-JOSHUA-018]] principle sharing gains an executable container.

TEST:
Compare a monolithic final prompt, prose playbook, and packaged skill across new users/models/tasks. Measure transfer, drift, failure recovery, and detectability of an intentionally obsolete rule.

PLATFORM:
ChatGPT · Codex · Skills

LINKS:
[[CALLSHOT-20260817-04]] [[MJ-JOSHUA-018]] [[CALLSHOT-FIELD-013]]

BIBTEX:
@misc{OpenAISkills2026, author={{OpenAI}}, title={Skills in ChatGPT}, year={2026}, url={https://help.openai.com/en/articles/20001066}}
