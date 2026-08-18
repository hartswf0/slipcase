ZETTEL

ID:
PB-FORAGE-004

TITLE:
Once the critique pool adapts to the battle, the benchmark becomes an endogenous curriculum.

SOURCE:
Kiela et al. — Dynabench: Rethinking Benchmarking in NLP — 2021 — pp. 4110–4124.

PASSAGE:
[PARAPHRASE]
Dynabench places humans and models in a loop where people deliberately construct examples that current models fail on; data creation, model development, and assessment consequently inform one another dynamically.

RESEARCH OBJECT:
PB_PRIME’s DJ analogy for the critique pool is much stranger than it first appears.

The archive proposes not merely sampling different flags.

It proposes changing or introducing critiques in response to how the battle unfolds.

LOCAL MOVE:
Separate dynamic examples from dynamic constructs.

SOURCE TERMS:
dynamic dataset creation
human-and-model-in-the-loop
target model
challenge examples
dynamic benchmarking

WHAT BECAME STRANGE:
Dynabench adapts examples while retaining a task whose correctness can still be checked.

PB_PRIME contemplates adapting the critique itself.

The distinction matters.

If:

    “AI is biased”

becomes:

    “AI cannot recognize its bias”

and then:

    “AI cannot recover from adversarially induced bias,”

the battle has not merely found harder examples.

It has moved the target construct.

QUESTION:
When does adaptive foraging discover a model boundary, and when does it silently redefine the question until a boundary appears?

DEEPER QUESTION:
Can a benchmark remain comparable while its ontology evolves?

MECHANISM:
Performance at time t influences which challenge is selected at t+1.

The evaluation distribution is therefore endogenous to the system being evaluated.

FORMAL SHIFT:
<CRITIQUE POOL C_t>
→ <MODEL–HUMAN PERFORMANCE>
→ [ADAPT / INVENT NEXT CRITIQUE]
→ <CRITIQUE POOL C_{t+1}>

SOURCE FORMALISM:
Human-and-model-in-the-loop dynamic benchmark construction.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

    C_{t+1} = A(C_t, failures_t, strategies_t, surprises_t)

Thus future measurement depends on past performance.

This is closer to curriculum generation or scientific foraging than a fixed benchmark.

TENSION:
Adaptivity makes the system excellent at finding fresh failures.

Adaptivity makes longitudinal scores difficult to interpret.

The thing that improves discovery may destroy comparability.

MISSING:
A distinction between:

    ANCHOR FLAGS — never change
    FRONTIER FLAGS — adapt to discoveries.

BOUNDARY:
Dynabench does not license arbitrary movement of the construct being measured. Its human adversaries generate new challenge instances under defined tasks. PB_PRIME goes further when the critique itself mutates.

CITATION TRAIL:
Dynamic adversarial data collection.
Benchmark saturation.
Adaptive testing.
Curriculum learning.
Construct drift.

TEST:
Create two simultaneous leagues.

ANCHOR LEAGUE:
A frozen set of flags and evaluation procedures repeated across model versions.

FRONTIER LEAGUE:
Flags mutate after every successful defense or capture.

For every new frontier flag, record its parent flag and the exact observation that caused the mutation.

Compare:

    longitudinal capability
    versus
    rate of new boundary discovery.

PLATFORM:
[[Living Benchmarks]]

LINKS:
[[Critique Pool]]
[[Dynamic Benchmark]]
[[Construct Drift]]

BIBTEX:
@inproceedings{kiela2021dynabench,
  title={Dynabench: Rethinking Benchmarking in NLP},
  author={Kiela, Douwe and Bartolo, Max and Nie, Yixin and Kaushik, Divyansh and Geiger, Atticus and Wu, Zhengxuan and Vidgen, Bertie and Prasad, Grusha and Singh, Amanpreet and Ringshia, Pratik and Ma, Zhiyi and Thrush, Tristan and Riedel, Sebastian and Waseem, Zeerak and Stenetorp, Pontus and Jia, Robin and Bansal, Mohit and Potts, Christopher and Williams, Adina},
  booktitle={Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},
  pages={4110--4124},
  year={2021},
  publisher={Association for Computational Linguistics}
}
