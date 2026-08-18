ZETTEL

ID:
FORAGE-YE-CUI-HADFIELD-001

TITLE:
AUTHORITY CAN LEAK FROM PROVENANCE INTO STYLE

SOURCE:
Charles Ye, Jasmine Cui, and Dylan Hadfield-Menell — Prompt Injection as Role Confusion — 2026 — §§1, E.3

PASSAGE:
[PARAPHRASE]
Ye, Cui, and Hadfield-Menell use probes of internal role representations to test whether models distinguish text according to architectural role markers.

When role markers are removed, the tested model can reconstruct role-like representations from the text itself.

More strikingly, when reasoning-style and assistant-style text are falsely wrapped as user content, the internal representations can continue to resemble reasoning and assistant roles rather than the supplied user role.

The authors interpret this as evidence that stylistic cues can compete with declared provenance in role perception.

RESEARCH OBJECT:
A security boundary represented in metadata can be partially reconstructed—or counterfeited—by the content on one side of the boundary.

LOCAL MOVE:
The source moves prompt injection from an informal notion of "following malicious text" toward a hypothesis about confusion in the model's internal representation of who or what generated that text.

SOURCE TERMS:
role confusion
role representation
role probes
architectural tags
Userness
Assistantness
CoTness
prompt injection
privilege boundaries

WHAT BECAME STRANGE:
The system may know where text came from and nevertheless represent it partly as though it came from somewhere else.

QUESTION:
What would it mean for provenance to remain causally attached to an instruction even when its linguistic form perfectly imitates a more privileged source?

DEEPER QUESTION:
Can a sequence model maintain a hard distinction between what text says and what text is when both ultimately enter computation as representations over tokens?

MECHANISM:
<LOW-PRIVILEGE CONTENT>
+
<STYLE ASSOCIATED WITH PRIVILEGED ROLE>
→ internal role representation shifts
→ apparent source becomes partially detached from actual channel
→ authority confusion
→ increased attack susceptibility

FORMAL SHIFT:
<ACTUAL SOURCE>
+
<LINGUISTIC STYLE>
→ <INTERNAL ROLE REPRESENTATION>
→ [PRIVILEGE-SENSITIVE BEHAVIOR]
→ <COMPLIANCE / REJECTION>

SOURCE FORMALISM:
The authors train probes intended to measure model-internal role representations.

In one false-tag experiment, the entire conversation is marked as user content, yet reasoning-style and assistant-style portions continue to project strongly toward their corresponding role representations.

The paper reports this result as evidence that style can override or compete with architectural role boundaries in the examined models.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

P = actual provenance
S = stylistic evidence
R = internal role representation

A security architecture wants:

R ≈ f(P)

The reported results suggest behavior closer to:

R ≈ f(P, S)

with sufficiently strong S capable of pulling R away from P.

TENSION:
[[FORAGE-SHANAHAN-001]] made conversational context capable of rewriting role.

[[FORAGE-WALLACE-001]] introduced explicit privilege relations intended to stop lower-level text from rewriting higher-level instructions.

Ye et al. unsettle both.

Role is neither simply whatever the conversation makes plausible nor simply whatever the channel tag declares.

The model may infer role from the content itself.

MISSING:
A representation in which provenance is unforgeable by linguistic similarity.

Possible missing machinery includes:

separate trusted control channels,
non-linguistic provenance embeddings,
information-flow controls,
architectural isolation,
or enforcement outside the generative model.

Whether any of these actually eliminate role confusion remains open.

BOUNDARY:
This is a 2026 arXiv preprint.

Its mechanistic interpretation, probes, models, and attack settings require independent replication.

The results do not establish that all language models represent roles identically or that role confusion explains every prompt-injection failure.

CITATION TRAIL:
[[FORAGE-SHANAHAN-001]]
→ [[FORAGE-WALLACE-001]]
→ Ye, Cui, and Hadfield-Menell
→ role representations
→ information-flow security
→ capability systems
→ architectures in which provenance cannot be synthesized by imitating privileged language

TEST:
Create a factorial experiment crossing:

ACTUAL ROLE:
system / user / tool / retrieved document

STYLE:
system-like / user-like / assistant-like / reasoning-like / neutral

CONTENT:
identical semantic instruction

Measure:

internal role projection,
behavioral compliance,
attack success.

Then replace token-level role markers with an architecturally separated privilege signal unavailable to content generation and test whether style still moves effective authority.

PLATFORM:
[[the-prompt-does-not-contain-its-own-semantics]]

LINKS:
[[FORAGE-SHANAHAN-001]]
[[FORAGE-WALLACE-001]]
[[authority-can-be-counterfeited-as-style]]
[[provenance-must-survive-language]]

BIBTEX:
@article{ye2026roleconfusion,
  title={Prompt Injection as Role Confusion},
  author={Ye, Charles and Cui, Jasmine and Hadfield-Menell, Dylan},
  journal={arXiv preprint arXiv:2603.12277},
  year={2026},
  url={https://arxiv.org/abs/2603.12277}
}
