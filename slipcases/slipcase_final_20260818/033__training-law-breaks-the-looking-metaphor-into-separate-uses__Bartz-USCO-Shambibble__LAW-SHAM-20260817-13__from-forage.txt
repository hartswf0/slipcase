ZETTEL

ID:
LAW-SHAM-20260817-13

TITLE:
2026-08-17 — Training law breaks the “looking” metaphor into separate legally consequential uses.

SOURCE:
Shambibble interview transcript, 2022-10-22, copyright discussion; Bartz v. Anthropic PBC, No. 24-cv-05417-WHA, Order on Fair Use (N.D. Cal. June 23, 2025); U.S. Copyright Office, Copyright and Artificial Intelligence, Part 3: Generative AI Training, pre-publication version, May 2025.

SOURCE URL:
[LOCAL UPLOAD — MJ_Interview 3.wh_shambibble_otter_ai.pdf]
https://cases.justia.com/federal/district-courts/california/candce/3%3A2024cv05417/434709/231/0.pdf
https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-3-Generative-AI-Training-Report-Pre-Publication-Version.pdf

PASSAGE:
[PARAPHRASE — SHAMBIBBLE]
Shambibble presents one counterargument to training infringement: extending copyright to prohibit learning from publicly viewable images can begin to resemble extending copyright from copying to looking.

[PARAPHRASE — BARTZ]
The district court separately analyzed copies used to train specific LLMs, print-to-digital library copies, and pirated library copies; it held the training use fair on the summary-judgment record while refusing to collapse pirated library acquisition into that training use.

RESEARCH OBJECT:
PIPELINE-SPECIFIC COPYRIGHT ANALYSIS.

LOCAL MOVE:
[[SHAM-20260817-08]] preserved Shambibble’s refusal to pretend copyright was settled. His “looking” analogy is useful because it names one intuition about learning, but later doctrine pressures its hidden collapse. A training pipeline can involve acquisition, reproduction, storage, selection into data mixes, training, retention, and outputs. Each stage can present a different legal use and a different market question.

The striking later development is not that a court simply validated or rejected Shambibble’s analogy. It is that the legal analysis became more granular than the analogy.

SOURCE TERMS:
“training copies”
“central library”
“pirated copies”
“fair use”
“licensing”
“training”
“looking”

WHAT BECAME STRANGE:
The metaphor “AI learns like a person” can be simultaneously illuminating about transformation and useless about the copies required to build the learning system.

QUESTION:
At which stages of a generative-model pipeline should copyright attach distinct legal significance?

DEEPER QUESTION:
Can a law of AI training remain coherent if it evaluates “learning” as one act rather than decomposing acquisition, copying, retention, model training, retrieval, and output generation?

MECHANISM:
Acquire source material. Create or retain copies. Select data for a model. Train model. Retain or discard source copies. Generate outputs. Copyright analysis can change at each stage because purpose, amount, market effect, authorization, and ongoing possession differ.

FORMAL SHIFT:
WORK
→ MODEL LEARNS
→ OUTPUT

becomes

WORK
→ ACQUISITION
→ COPY / STORAGE
→ DATA SELECTION
→ TRAINING USE
→ RETENTION / OTHER USES
→ OUTPUT

SOURCE FORMALISM:
Bartz expressly separates training copies, purchased print-to-digital library copies, and pirated central-library copies. The Copyright Office Part 3 separately analyzes fair use, competition, market effects, and licensing for AI training.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

LEGAL(training_system) = Σ legal_analysis(stage_i)

where the legality or fair-use status of one stage does not automatically legalize another.

TENSION:
Bartz is one federal district-court order and not a universal rule for all training systems or sources. The later class settlement concerned piracy claims and does not convert the training-use holding into nationwide settled doctrine. The Copyright Office’s Part 3 remains a policy report, not binding case law.

MISSING:
Appellate doctrine and cross-modal cases capable of distinguishing training on books, images, music, audiovisual works, and data acquired under different factual conditions.

BOUNDARY:
This zettel does not give legal advice or claim that generative-AI training is categorically fair use or categorically infringing.

CITATION TRAIL:
[[SHAM-20260817-08]]
→ copyright as unsettled
→ “looking” counterargument
→ Bartz separates training use from pirated library acquisition
→ USCO Part 3 separates fair use from licensing policy
→ training becomes a pipeline of legally distinct acts

TEST:
For any proposed training system, build a stage-by-stage copyright ledger recording source, acquisition method, copy created, retention, training role, downstream access, and output behavior. Compare the legal analysis with a single undifferentiated statement that “the model learned from the work.”

PLATFORM:
U.S. copyright law
Generative AI training
AI datasets

LINKS:
[[SHAM-20260817-08]]
[[LAW-SHAM-20260817-12]]
[[LAW-SHAM-20260817-08]]

BIBTEX:
@misc{bartz2025fairuse,
  author={{United States District Court for the Northern District of California}},
  title={Bartz v. Anthropic PBC, Order on Fair Use},
  year={2025},
  month={6},
  day={23},
  url={https://cases.justia.com/federal/district-courts/california/candce/3%3A2024cv05417/434709/231/0.pdf}
}
@report{usco2025part3,
  author={{U.S. Copyright Office}},
  title={Copyright and Artificial Intelligence, Part 3: Generative AI Training},
  year={2025},
  month={5},
  note={Pre-publication version},
  url={https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-3-Generative-AI-Training-Report-Pre-Publication-Version.pdf}
}
@misc{shambibble2022interview,
  title={MJ Interview 3.wh_shambibble},
  year={2022},
  month={10},
  note={Interview transcript, October 22, 2022, 1:26:03; automated transcript}
}
