ZETTEL

ID:
LAW-SHAM-20260817-07

TITLE:
2026-08-17 — The specification is a glossary, but the prompt has no stable skilled reader.

SOURCE:
U.S. Patent and Trademark Office, MPEP §§ 2111–2111.01, current edition consulted 2026-08-17; Shambibble interview transcript, 2022-10-22, 04:01–04:29 and 48:53–51:32.

SOURCE URL:
https://www.uspto.gov/web/offices/pac/mpep/s2111.html
[LOCAL UPLOAD — MJ_Interview 3.wh_shambibble_otter_ai.pdf]

PASSAGE:
[PARAPHRASE — USPTO]
Claim terms ordinarily receive their plain meaning to a person of ordinary skill in the art, read in light of the specification; an applicant may clearly define a term specially in the specification.

[QUOTE — SHAMBIBBLE]
“it will show you which words got run together and which words got split.”

RESEARCH OBJECT:
THE MISSING INTERPRETIVE COMMUNITY.

LOCAL MOVE:
Patent interpretation can ask how a skilled artisan would read a claim because patent law supplies an imagined interpretive community anchored in a technical field, specification, and prosecution record.

Prompt language lacks an equivalent stable reader. The same sentence may be tokenized differently, interpreted differently across models, altered by hidden system instructions, and routed through different tools. Shambibble predicted that some lexical prompt craft might disappear as natural-language understanding improved; this prediction makes the identity of the “reader” even more unstable.

SOURCE TERMS:
“person of ordinary skill in the art”
“plain meaning”
“specification”
“glossary”
“tokenized”
“model version”

WHAT BECAME STRANGE:
Patent law externalizes an answer to “meaning for whom?” Prompt engineering often does not. It speaks of prompt clarity without naming the interpreter whose clarity is at issue.

QUESTION:
Who is the relevant reader of a prompt?

DEEPER QUESTION:
Is prompt meaning indexed to a model/version/runtime in the way patent meaning is indexed to a skilled artisan and intrinsic record—and if so, can a prompt ever be considered clear independent of its execution environment?

MECHANISM:
Prompt text P is interpreted relative to runtime R = {model, version, system instructions, tokenizer, tools, schemas, conversation state}. Change R and the same P may acquire a different operational meaning.

FORMAL SHIFT:
PROMPT MEANING = f(TEXT)

becomes

PROMPT MEANING = f(TEXT, INTERPRETER, CONTEXT, RUNTIME)

SOURCE FORMALISM:
MPEP claim interpretation ties ordinary meaning to a skilled artisan and the specification; special definitions must be made clear.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

The prompt analogue of intrinsic evidence may include: system instructions, user context, tool contracts, schemas, examples, defined terms, and preserved amendment history.

TENSION:
Unlike a legal skilled artisan, an AI model is not a normative community member and does not possess a stable publicly contestable interpretive practice. Treating model behavior as “meaning” risks naturalizing implementation accidents.

MISSING:
A defensible theory of prompt meaning that separates normative user intent, textual affordance, empirical model behavior, and runtime contract.

BOUNDARY:
Patent claim interpretation supplies a normative skilled-reader construct. A model/runtime is not that construct; the analogy identifies a missing variable rather than filling it.

CITATION TRAIL:
[[MJ-2022-003]]
→ tokens differ from words
→ patent “skilled reader” doctrine
→ prompt clarity becomes interpreter-indexed
→ missing object: person/model of ordinary skill in prompt art

TEST:
Run identical prompts across model versions and runtime configurations. Separate semantic judgments by human readers from observed execution. Identify which ambiguities are text-intrinsic and which are interpreter-specific.

PLATFORM:
Patent claim interpretation
Prompt semantics
LLM runtimes

LINKS:
[[MJ-2022-003]]
[[MJ-2022-010]]
[[SHOT-20260817-02]]

BIBTEX:
@misc{uspto211101,
 author={{U.S. Patent and Trademark Office}},
 title={MPEP §§ 2111–2111.01: Claim Interpretation and Plain Meaning},
 url={https://www.uspto.gov/web/offices/pac/mpep/s2111.html}
}
@misc{shambibble2022interview,
  title={MJ Interview 3.wh_shambibble},
  year={2022},
  month={10},
  note={Interview transcript, October 22, 2022, 1:26:03; automated transcript}
}
