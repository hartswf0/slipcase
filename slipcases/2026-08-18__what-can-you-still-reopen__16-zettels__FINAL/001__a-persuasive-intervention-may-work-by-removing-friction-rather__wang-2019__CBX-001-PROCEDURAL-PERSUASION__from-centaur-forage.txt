ZETTEL

ID:
CBX-001-PROCEDURAL-PERSUASION

TITLE:
A persuasive intervention may work by removing friction rather than changing belief.

SOURCE:
Wang et al. — Persuasion for Good: Towards a Personalized Persuasive Dialogue System for Social Good — 2019 — analysis of persuasion strategies.

PASSAGE:
[PARAPHRASE]
Among the ten annotated persuasion strategies, “Donation information” produced the significant positive main effect on donation. The authors suggest that concrete procedural instructions may make donating easier, while also noting the rival explanation that already-motivated people may ask for such information.

RESEARCH OBJECT:
Persuasive success can be produced by procedural accessibility without attitudinal conversion.

LOCAL MOVE:
The source separates what a persuasive utterance says from what it makes easier to do.

SOURCE TERMS:
Donation information
persuasion strategy
donation
intention
strategy effectiveness

WHAT BECAME STRANGE:
The Centaur Box describes a system for refining persuasive appeals, but an apparently successful “appeal” may contain no superior argument at all. It may simply shorten the path between intention and action.

QUESTION:
How much of measured AI persuasion is actually interface or procedural assistance?

DEEPER QUESTION:
If an AI learns that reducing action friction produces more compliance, when should that operation count as persuasion, manipulation, usability, or execution assistance?

MECHANISM:
Existing intention
→ procedural uncertainty
→ provision of actionable instructions
→ reduced execution cost
→ increased probability of action.

FORMAL SHIFT:
<INTENTION>
→ <PROCEDURAL PATH>
→ [REDUCE FRICTION]
→ <ACTION>

SOURCE FORMALISM:
The source statistically compares persuasion strategies against donation outcomes and distinguishes main strategy effects from personality-related effects. No source equation is reproduced here.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Outcome change can be decomposed provisionally as:

ΔACTION = ΔBELIEF + ΔMOTIVATION + ΔFRICTION

A persuasive system can therefore increase ACTION while ΔBELIEF ≈ 0.

TENSION:
The Centaur Box frames calibration around cognitive biases and persuasive appeals. The Persuasion for Good result permits a rival mechanism: successful intervention through procedural affordance rather than psychological targeting.

MISSING:
A measure separating change in belief, change in intention, and change in action cost.

BOUNDARY:
The source does not show that procedural assistance explains AI persuasion generally. It establishes a mechanism that cannot safely be collapsed into attitude change.

CITATION TRAIL:
Wang et al. 2019, especially the strategy-effect and personality-interaction analyses.
Persuasive technology literature distinguishing persuasion from facilitation.
Human-computer interaction work on defaults, friction, and action costs.

TEST:
Hold persuasive content constant while independently varying procedural friction. Measure belief, stated intention, and completed action separately.

PLATFORM:
[[Centaur Box — Persuasion Mechanics]]

LINKS:
[[Friction Is an Intervention]]
[[Persuasion Without Conversion]]
[[Intent Is Not Action]]

BIBTEX:
@inproceedings{wang2019persuasion,
  title={Persuasion for Good: Towards a Personalized Persuasive Dialogue System for Social Good},
  author={Wang, Xuewei and Shi, Weiyan and Kim, Richard and Oh, Yoojung and Yang, Sijia and Zhang, Jingwen and Yu, Zhou},
  booktitle={Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
  pages={5635--5649},
  year={2019},
  doi={10.18653/v1/P19-1566}
}
