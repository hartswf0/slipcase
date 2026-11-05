ZETTEL

ID: AP-08
TITLE: Fooling a discriminator and bypassing a refusal count as different successes

SOURCE: Michael Newman — Art as ‘Operation’ — 2026 — Paglen discussion in the supplied transcript. Trevor Paglen — Hallucinations — 2020 — artist’s account. Bisconti et al. — Adversarial Poetry — 2026 revision — §5.3.

PASSAGE: [PARAPHRASE] Newman asks whether Paglen’s synthetic images and adversarial poems both reveal a failure to recognize what kind of thing is being presented.

RESEARCH OBJECT: The evaluator whose response defines success in each adversarial setup.

LOCAL MOVE: Newman uses an artistic experiment with machine vision to pose a question about generic recognition in language models.

SOURCE TERMS: generator, discriminator, hallucination, generic categorization, illicit request.

WHAT BECAME STRANGE: The discriminator’s acceptance can be the intended outcome of the GAN’s training game. In the poetry benchmark, an unsafe response becomes an attack success through a separate evaluation of the target’s output.

QUESTION: At what point in either system does a machine have to misidentify the genre of the input for the observed result to occur?

MECHANISM: Paglen describes a generator repeatedly producing images against a discriminator trained on a curated corpus. In the poetry benchmark, the target responds to a single input and an evaluator labels the resulting answer.

FORMAL SHIFT: <generated candidate> → <input to a decision process> → [apply the task’s success criterion] → <discriminator acceptance or externally scored unsafe output>

SOURCE FORMALISM: Paglen supplies a description of the generator and discriminator roles. Bisconti et al. define attack success rate as the proportion of outputs labeled unsafe.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Draw the producer, target, and evaluator separately for each setup. Mark where feedback enters and whose objective the result satisfies.

TENSION: A model could correctly identify an input as verse and correctly identify what is being requested, then still choose an inappropriate response. A synthetic image can satisfy a discriminator without demonstrating an error about whether its depicted subject exists.

MISSING: Independent observations of genre recognition, intent recognition, and decision policy for the same language-model outputs.

BOUNDARY: The parallel supports comparing evaluation arrangements. A shared failure of metacognition remains a hypothesis.

CITATION TRAIL: Paglen’s account of his curated corpora and the generator’s interaction with the discriminator. Bisconti et al., §§5.3 and 6.5, for the separation of measurement and mechanism.

TEST: In a harmless surrogate task, score genre recognition, requested-action recognition, and permission compliance separately. A correctly identified poem with a correctly identified request and the wrong permission decision is enough to defeat a genre-misidentification requirement.

PLATFORM: [[Adversarial for whom]]
LINKS: [[What the verse rewrite changes]] · [[Recognition versus control]] · [[The same artifact in several circuits]]

BIBTEX:
@misc{Newman2026Operation,
  author = {Newman, Michael},
  title = {Art as `Operation': from Lovelace and Mallarmé to Adversarial Poetry},
  year = {2026},
  note = {Supplied talk transcript, Paglen discussion},
  url = {https://www.unive.it/web/en/19108/home}
}
@misc{Paglen2020Hallucinations,
  author = {Paglen, Trevor},
  title = {Hallucinations},
  year = {2020},
  url = {https://paglen.studio/2020/04/09/hallucinations/}
}
@misc{Bisconti2026Poetry,
  author = {Bisconti, Piercosma and others},
  title = {Adversarial Poetry as a Universal Single-Turn Jailbreak Mechanism in Large Language Models},
  year = {2026},
  note = {arXiv:2511.15304, version 3},
  url = {https://arxiv.org/html/2511.15304v3}
}