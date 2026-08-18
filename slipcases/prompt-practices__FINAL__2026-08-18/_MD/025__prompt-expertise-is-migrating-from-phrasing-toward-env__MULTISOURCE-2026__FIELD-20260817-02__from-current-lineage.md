ZETTEL

ID:
FIELD-20260817-02

TITLE:
Prompt expertise is migrating from phrasing toward environment design, tests, and evaluative judgment.

SOURCE:
MULTISOURCE — OpenAI Prompting; OpenAI Prompt Generation; OpenAI Harness Engineering; Kirsh & Maglio 1994. SOURCE URLs: https://developers.openai.com/api/docs/guides/prompting ; https://developers.openai.com/api/docs/guides/prompt-generation ; https://openai.com/index/harness-engineering/ ; https://doi.org/10.1207/s15516709cog1804_1

PASSAGE:
[OUR INFERENCE] When systems can generate operative prompts, route to external instructions, and be judged by evaluations, durable expertise moves toward specifying goals, constructing tests, shaping environments, and interpreting failures.

RESEARCH OBJECT:
The field suggests a role transition. “Prompt engineer” becomes less a specialist in phrasing and more an engineer of conditions under which useful language is generated, executed, inspected, and revised.

LOCAL MOVE:
Replace PROMPT CRAFT with SPECIFICATION + HARNESS + EVALUATION DESIGN.

SOURCE TERMS:
application code; meta-prompt; harness; tests; evaluations; epistemic action; routing

WHAT BECAME STRANGE:
The more competent models become at writing prompts, the less special the final wording may be. Expertise can survive automation by moving one level upward into what counts as success and what evidence changes the specification.

QUESTION:
Which prompt-expertise skills remain predictive of performance after candidate prompt text is machine-generated?

DEEPER QUESTION:
Is the new programming unit a loop of specification, generation, inspection, correction, and evaluation rather than a linguistic instruction?

MECHANISM:
GOAL → SPECIFICATION → generated/routed instruction → execution → output-as-artifact/evidence → evaluation → failure classification → specification update.

FORMAL SHIFT:
HUMAN WRITES PROMPT becomes HUMAN DESIGNS THE SEARCH/EVALUATION SPACE IN WHICH PROMPTS ARE PRODUCED.

SOURCE FORMALISM:
The sources separately support prompt-as-code, prompt generation, routed repository guidance, and epistemic actions. Their combination is compiler synthesis.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
PROGRAM = (SPEC, HARNESS, EVAL, UPDATE_RULE); PROMPT_t = COMPILE(PROGRAM, STATE_t).

TENSION:
If higher-level specifications are themselves natural-language prompts, recursion can merely relocate fragility rather than eliminate it.

MISSING:
Comparative studies separating benefits from better phrasing, better examples, better tests, better tools, and better failure diagnosis.

BOUNDARY:
This is a cross-source synthesis, not a consensus claim from the cited works.

CITATION TRAIL:
[[WWP-20260817-06]] → generated prompts → [[WWP-20260817-02]] → prompt-as-code → [[WWP-20260817-03]] → routing → [[SCGAI-004-A]] → outputs as evidence.

TEST:
Hold a task constant and independently vary human phrase-craft, machine-generated prompts, evaluation quality, and harness quality; measure which interventions survive model migration.

PLATFORM:
LLM applications / agent harnesses / prompt optimization

LINKS:
[[WWP-20260817-06]]
[[WWP-20260817-02]]
[[WWP-20260817-03]]
[[SCGAI-004-A]]

BIBTEX:
@misc{openai_prompting, author={{OpenAI}}, title={Prompting}, url={https://developers.openai.com/api/docs/guides/prompting}}
@misc{openai_prompt_generation, author={{OpenAI}}, title={Prompt Generation}, url={https://developers.openai.com/api/docs/guides/prompt-generation}}
@misc{openai2026harness, author={{OpenAI}}, title={Harness Engineering: Leveraging Codex in an Agent-First World}, year={2026}, url={https://openai.com/index/harness-engineering/}}
@article{kirsh1994distinguishing, author={Kirsh, David and Maglio, Paul}, title={On Distinguishing Epistemic from Pragmatic Action}, year={1994}, doi={10.1207/s15516709cog1804_1}}
