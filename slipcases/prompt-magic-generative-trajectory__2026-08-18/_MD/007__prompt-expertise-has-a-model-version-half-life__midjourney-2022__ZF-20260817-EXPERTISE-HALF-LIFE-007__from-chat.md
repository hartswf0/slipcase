ZETTEL

ID:
ZF-20260817-EXPERTISE-HALF-LIFE-007

TITLE:
Prompt Expertise Has a Model-Version Half-Life

SOURCE:
[PRIMARY ARCHIVE] Midjourney Discord / Office Hours research archive supplied by user.
SOURCE URL: local:_RESOURCES/Midjourney_prompt_magic_archive_2022.md

[AUTHORITATIVE TECHNICAL SOURCE] Midjourney, “Version.”
https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version

PASSAGE:
[QUOTE — PRIMARY ARCHIVE] “I have to relearn my magical prompt incantations.”

[QUOTE — PRIMARY ARCHIVE] “v3—>v4 remove all the hacks” and “everything is really different.”

RESEARCH OBJECT:
The archive gives prompt expertise a temporal dimension.

A practitioner can become better at operating a model while becoming no better at operating its successor.

That means expertise may not simply accumulate.

It can expire.

The supposedly skilled phrase is not merely attached to an artistic intention. It is attached to a particular implementation state.

A model update can therefore function like a language change imposed overnight.

LOCAL MOVE:
Replace:

PROMPT EXPERTISE = accumulated mastery

with:

PROMPT EXPERTISE(t) =
portable competence
+
version-local competence
+
obsolete competence.

SOURCE TERMS:
relearn
prompt incantations
version
hacks
V3
V4
model version
prompt understanding

WHAT BECAME STRANGE:
Software improvement can destroy user expertise.

Ordinarily, better tools are imagined as extending accumulated skill.

Here:

MODEL IMPROVEMENT
→ OBSOLETE CONTROL KNOWLEDGE.

The expert may wake up after an update possessing a library of once-effective expressions whose operational meanings have vanished.

QUESTION:
What portion of prompt expertise survives a model replacement?

DEEPER QUESTION:
Can a practice count as a mature craft when the material itself is repeatedly replaced by its manufacturer and the craftsperson cannot preserve the old causal substrate?

MECHANISM:
[OUR INFERENCE]

Practitioners discover empirical mappings:

phrase p
→ behavior b
under model M₁.

Upgrade:

M₁ → M₂

changes:

P(output | p,M)

so previously learned:

p → b

may become:

p → b′
or
p → ∅.

Expertise therefore depreciates whenever the underlying model changes faster than transferable principles can be extracted.

FORMAL SHIFT:
LEARN
→ RETAIN
→ MASTER

becomes:

LEARN(M₁)
→ MODEL UPDATE
→ TEST TRANSFER
→ RETAIN / REVISE / DISCARD
→ LEARN(M₂)

SOURCE FORMALISM:
[PARAPHRASE] Midjourney officially exposes model selection through its version controls and maintains multiple generations of its image models.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

E = practitioner expertise
E_G = generalizable expertise
E_M = model-local expertise
M_t = model at time t

Then:

E(t) = E_G + E_Mt

After replacement:

M_t → M_t+1

transfer(E_Mt → M_t+1) may approach 0

while:

transfer(E_G → M_t+1) > 0.

The crucial empirical question is the ratio:

ρ = transferable skill / total measured skill.

TENSION:
Frequent model change produces two opposite interpretations.

READING A:
Prompting is shallow because tricks rapidly expire.

READING B:
Prompting is craft precisely because practitioners repeatedly perceive, adapt to, and learn new material behavior.

The distinction cannot be settled by vocabulary alone.

MISSING:
Longitudinal evidence following the same expert practitioners through successive model versions.

We need to know which competencies survive:
visual judgment
iteration strategy
prompt vocabulary
parameter knowledge
model intuition
selection skill
reference-image composition.

BOUNDARY:
Model-local skill is not automatically fake skill.

Many crafts depend on material-specific knowledge.

The unusual condition here is that the material can be silently and centrally replaced by a platform operator.

CITATION TRAIL:
[[ZF-20260817-MAGIC-TERMS-001]]
[[ZF-20260817-VOCABULARY-GAP-002]]
→ model-specific vocabulary
→ archive: practitioners explicitly report having to relearn
→ Office Hours: new version removes old “hacks”
→ new distinction: GENERAL CRAFT versus VERSION-LOCAL CRAFT
→ next edge: measure skill transfer across historical model boundaries

TEST:
Recruit practitioners with archived work from two successive Midjourney versions.

Give them matched reconstruction tasks on:

1. their historically mastered version
2. the immediately succeeding version
3. a current version

Measure:

iterations
time
lexical carryover
parameter carryover
selection accuracy
target similarity
self-reported surprise

Estimate:

TRANSFERABILITY RATIO
and
EXPERTISE HALF-LIFE.

PLATFORM:
Midjourney
versioned generative models
Discord

LINKS:
[[ZF-20260817-MAGIC-TERMS-001]]
[[ZF-20260817-VOCABULARY-GAP-002]]
[[MODEL-LOCAL-LANGUAGE]]
[[EXPERTISE-DEPRECIATION]]
[[CRAFT-WITH-A-MOVING-MATERIAL]]

BIBTEX:
@misc{midjourneyVersion,
  author={{Midjourney}},
  title={Version},
  howpublished={Midjourney Documentation},
  url={https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version}
}
