ZETTEL

ID:
FIELD-20260817-01

TITLE:
The minimal reproducible prompt is a receipt for an execution event, not a string.

SOURCE:
MULTISOURCE — Mahdavi Goloujeh, Sullivan & Magerko 2024; Bolin/OpenAI 2026; Midjourney Version docs 2026. SOURCE URLs: https://doi.org/10.1145/3613905.3650947 ; https://openai.com/index/unrolling-the-codex-agent-loop/ ; https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version

PASSAGE:
[OUR INFERENCE] The string is one field in a larger execution event. Social ancestry, assembled runtime context, model/version, parameters, and lineage can change while the visible words remain identical.

RESEARCH OBJECT:
The field converges on a new reproducibility unit: a PROMPT RECEIPT. It is not a transcript of everything. It is an addressable record of enough execution conditions and lineage to say what ran, where it ran, what it could see, what it produced, and what evidence motivated the next change.

LOCAL MOVE:
Replace PROMPT PRESERVATION with EXECUTION-RECEIPT PRESERVATION.

SOURCE TERMS:
social construction; prompt history; effective prompt; version; execution environment; provenance; reproducibility

WHAT BECAME STRANGE:
Two identical prompt strings can be different research objects because they inherit different social histories, hidden context assemblies, model versions, tools, and tests. Conversely, two different strings can be instances of the same higher-level specification.

QUESTION:
What is the smallest receipt that lets another researcher materially reconstruct a prompt execution without pretending inaccessible hidden state is known?

DEEPER QUESTION:
Should prompt scholarship cite execution events rather than strings, in the way experimental work cites apparatus and conditions rather than only instructions?

MECHANISM:
VISIBLE INPUT + INSTRUCTION REFERENCES + HISTORY REFERENCES + TOOL SCHEMAS + MODEL/VERSION + EXPOSED PARAMETERS + TIMESTAMP + OUTPUT + LINEAGE + EVALUATION → reconstructable execution event.

FORMAL SHIFT:
PROMPT_IDENTITY=TEXT becomes EXECUTION_EVENT_IDENTITY=RECEIPT(TEXT, CONTEXT_REFS, ENVIRONMENT, MODEL, PARAMETERS, OUTPUT, LINEAGE, EVALUATION).

SOURCE FORMALISM:
Mahdavi et al. provide social circulation/lineage; Bolin describes assembled agent context beyond verbatim user input; Midjourney documents version-dependent execution. “Prompt receipt” is not source terminology.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
RECEIPT r={visible_input, instruction_set_ref, history_ref, tool_schema_ref, environment_ref, model_version, exposed_params, platform, timestamp, output_ref, lineage_refs, evaluation}. Sufficiency is relative to a reconstruction goal.

TENSION:
Richer receipts increase reproducibility and provenance while also increasing privacy, security, and proprietary-context exposure. A complete receipt may be neither possible nor desirable.

MISSING:
Empirical ablation determining which receipt fields materially change reconstruction accuracy for different prompt tasks.

BOUNDARY:
PROMPT RECEIPT is compiler synthesis. It should not be attributed to any source and must remain explicitly provisional.

CITATION TRAIL:
[[WWP-20260817-01]] → effective prompt exceeds visible words → [[WWP-20260817-09]] → preserved text can drift across versions → [[SCGAI-003]] / [[SCGAI-008]] → lineage and provenance → prompt receipt.

TEST:
Reconstruction ablation: give independent agents progressively richer bundles—string only; string+model; +params; +history; +tools; +lineage; +tests—and measure ability to reproduce behavior and explain changes.

PLATFORM:
Cross-platform generative AI / prompt archives / agent systems

LINKS:
[[WWP-20260817-01]]
[[WWP-20260817-09]]
[[SCGAI-003]]
[[SCGAI-008]]

BIBTEX:
@inproceedings{mahdavigoloujeh2024social, author={Mahdavi Goloujeh, Atefeh and Sullivan, Anne and Magerko, Brian}, title={The Social Construction of Generative AI Prompts}, year={2024}, doi={10.1145/3613905.3650947}}
@misc{bolin2026codexloop, author={Bolin, Michael}, title={Unrolling the Codex Agent Loop}, organization={OpenAI}, year={2026}, url={https://openai.com/index/unrolling-the-codex-agent-loop/}}
@misc{midjourney_version, author={{Midjourney}}, title={Version}, year={2026}, url={https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version}}
