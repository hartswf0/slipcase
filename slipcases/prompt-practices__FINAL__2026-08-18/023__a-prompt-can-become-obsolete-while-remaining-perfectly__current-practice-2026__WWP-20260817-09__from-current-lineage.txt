ZETTEL

ID:
WWP-20260817-09

TITLE:
A prompt can become obsolete while remaining perfectly preserved.

SOURCE:
Midjourney — “Version” — Official Documentation — https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version — accessed 2026-08-17

PASSAGE:
[QUOTE] “V8.2 released as the default version on July 24, 2026.”

RESEARCH OBJECT:
The same text can be executed against materially different generative systems across short spans of time. Preserved words do not preserve the operative environment.

LOCAL MOVE:
Replace PROMPT ARCHIVING with PROMPT + EXECUTION ENVIRONMENT ARCHIVING.

SOURCE TERMS:
Version; V8.1; V8.2; default version; prompt adherence; Personalization; parameters; compatibility

WHAT BECAME STRANGE:
A perfect textual archive can fail to preserve the work. The linguistic artifact remains stable while its execution semantics drift beneath it.

QUESTION:
What metadata is required before an archived prompt can legitimately be called reproducible?

DEEPER QUESTION:
Are prompts more like recipes or like specimens whose behavior depends on an environment that must also be preserved?

MECHANISM:
PROMPT P + MODEL M1 + SETTINGS S1 → distribution D1; later same P + M2 + S2 → D2.

FORMAL SHIFT:
PROMPT IDENTITY=TEXT becomes EXECUTION IDENTITY={TEXT, MODEL_VERSION, PARAMETERS, PERSONALIZATION, REFERENCES, DATE, TOOLCHAIN}.

SOURCE FORMALISM:
Midjourney exposes explicit model-version selection and documents changing defaults/compatibility across versions.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
PROMPT FOSSIL=P preserved while ENV(P)_original no longer exists; resurrection requires P + sufficiently reconstructed ENV(P).

TENSION:
Declared version labels may not capture hidden changes in infrastructure, moderation, personalization, preprocessing, or sampling.

MISSING:
The smallest “execution capsule” sufficient to rerun an old prompt practice with meaningful fidelity.

BOUNDARY:
Midjourney explicitly exposes model versions; other platforms may version/update differently.

CITATION TRAIL:
[[SCGAI-004-B]] → adaptive folk theorization → prompt fossils → current version turnover → execution-environment preservation.

TEST:
Run prompts documented under an earlier version across that and later versions while holding exposed parameters constant; measure technique survival.

PLATFORM:
Midjourney / versioned generative models

LINKS:
[[SCGAI-004-B]]

BIBTEX:
@misc{midjourney_version, author={{Midjourney}}, title={Version}, howpublished={Midjourney Documentation}, url={https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version}, note={Accessed 2026-08-17}}
