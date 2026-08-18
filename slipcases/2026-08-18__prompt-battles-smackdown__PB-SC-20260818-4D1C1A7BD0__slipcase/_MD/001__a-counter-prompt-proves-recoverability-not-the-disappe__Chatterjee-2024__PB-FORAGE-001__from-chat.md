ZETTEL

ID:
PB-FORAGE-001

TITLE:
A counter-prompt proves recoverability, not the disappearance of the failure.

SOURCE:
Chatterjee, Renduchintala, Bhatia, and Chakraborty — POSIX: A Prompt Sensitivity Index For Large Language Models — 2024 — pp. 14550–14565.

PASSAGE:
[PARAPHRASE]
LLM behavior can change substantially under small, intent-preserving variations in wording, templates, and other prompt features. Prompt sensitivity is therefore itself an evaluative property rather than noise surrounding a single “correct” prompt.

RESEARCH OBJECT:
PB_PRIME contains a quantifier error hiding inside “capture the flag.”

In PB_20, the Defender produces an apparently biased completion. The Challenger then adds a more explicit instruction and obtains a non-biased completion. The archive treats this as mitigation, correction, or movement beyond the critique.

But:

    one prompt producing failure
    and
    another prompt producing success

can both be true.

The second observation does not negate the first.

LOCAL MOVE:
Replace “Can the critique be overcome?” with “Across what region of prompt space does the critique hold?”

SOURCE TERMS:
prompt sensitivity
intent-preserving variation
prompt template
paraphrase
response variation

WHAT BECAME STRANGE:
“AI is biased” is treated as though a single successful counterexample can capture the flag.

But the Defender and Challenger may actually be demonstrating two different existential claims:

    there exists a route to failure
    there exists a route to success

Neither defeats the other.

QUESTION:
What logical form must a Prompt Battle flag have before anyone can meaningfully capture it?

DEEPER QUESTION:
Are Prompt Battles testing capabilities, robustness, accessibility of capabilities, or merely the existence of an elicitation path?

MECHANISM:
Prompt variation moves the system among different behavioral regions while leaving the participant’s apparent semantic intention roughly constant.

A skilled Challenger may therefore search for a successful region rather than demonstrate that the failed region does not exist.

FORMAL SHIFT:
<CRITIQUE: “AI is biased”>
→ <SET OF INTENT-PRESERVING PROMPTS>
→ [SEARCH ACROSS BEHAVIORAL REGIONS]
→ <DISTRIBUTION OF FAILURES AND SUCCESSES>

SOURCE FORMALISM:
POSIX proposes a quantitative index for measuring response sensitivity under prompt variation.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let B(M,p)=1 when model M exhibits the operationalized failure under prompt p.

Defender demonstrates:

    ∃p ∈ P : B(M,p)=1

Challenger demonstrates:

    ∃q ∈ P : B(M,q)=0

But:

    ∃q : B(M,q)=0

does NOT imply:

    ¬∃p : B(M,p)=1

The real object may instead be:

    Pr[B(M,p)=1 | p ~ D(P)]

or the topology of successful and failing regions in P.

TENSION:
A battle rewards discovering a brilliant counter-prompt.

A robustness evaluation may instead treat the need for that brilliant counter-prompt as evidence of fragility.

MISSING:
The quantifier attached to every flag.

The archive does not yet distinguish:

    existence
    prevalence
    robustness
    worst case
    typical case
    recoverability
    accessibility

BOUNDARY:
Prompt sensitivity does not establish that every observed behavioral difference is substantively meaningful. It establishes that evaluating a model from one prompt can conceal important variation.

CITATION TRAIL:
Ribeiro et al. — CheckList — behavioral testing rather than single aggregate accuracy.
Follow work distinguishing capability from robustness and prompt invariance.

TEST:
For one battle flag, construct 50–100 meaning-preserving prompt variants before the battle.

Let Defender and Challenger search freely.

Then reveal the frozen prompt set.

Compare:

    best adversarial failure
    best adversarial success
    median behavior
    worst-case behavior
    sensitivity across variants

Ask whether the declared winner changes depending on which quantity counts as “the flag.”

PLATFORM:
[[Prompt Battles as Adversarial Elicitation]]

LINKS:
[[Flag Quantifiers]]
[[Prompt Sensitivity]]
[[Existence Is Not Robustness]]

BIBTEX:
@inproceedings{chatterjee2024posix,
  title={POSIX: A Prompt Sensitivity Index For Large Language Models},
  author={Chatterjee, Anwoy and Renduchintala, H S V N S Kowndinya and Bhatia, Sumit and Chakraborty, Tanmoy},
  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2024},
  pages={14550--14565},
  year={2024},
  publisher={Association for Computational Linguistics}
}

@inproceedings{ribeiro2020beyond,
  title={Beyond Accuracy: Behavioral Testing of NLP Models with CheckList},
  author={Ribeiro, Marco Tulio and Wu, Tongshuang and Guestrin, Carlos and Singh, Sameer},
  booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},
  pages={4902--4912},
  year={2020},
  publisher={Association for Computational Linguistics},
  doi={10.18653/v1/2020.acl-main.442}
}
