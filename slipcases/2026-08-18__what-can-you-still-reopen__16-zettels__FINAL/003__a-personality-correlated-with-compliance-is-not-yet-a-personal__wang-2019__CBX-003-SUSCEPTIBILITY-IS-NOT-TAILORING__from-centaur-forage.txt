ZETTEL

ID:
CBX-003-SUSCEPTIBILITY-IS-NOT-TAILORING

TITLE:
A personality correlated with compliance is not yet a personality-specific persuasive strategy.

SOURCE:
Wang et al. — Persuasion for Good: Towards a Personalized Persuasive Dialogue System for Social Good — 2019 — personality and strategy analyses; Hartsoe & Assi — Thinking Outside the AI Box: The Centaur Box Experiment — supplied manuscript.

PASSAGE:
[PARAPHRASE]
Persuasion for Good reports personality and value variables associated with baseline donation behavior, then separately examines interactions between recipient characteristics and particular persuasion strategies. The interaction evidence is heterogeneous and the authors caution against overinterpretation given the amount of annotated data.

RESEARCH OBJECT:
Baseline susceptibility and treatment-effect heterogeneity are different quantities.

LOCAL MOVE:
The source prevents a tempting inference from “this kind of person is more likely to comply” to “this message works especially well on this kind of person.”

SOURCE TERMS:
Big Five
Moral Foundations
Schwartz values
decision-making style
persuasion strategy
interaction
donation

WHAT BECAME STRANGE:
The Centaur Box describes Persuasion for Good as a basis for tailoring persuasive appeals from psychographic profiles. But a profile predicting who is already likely to act does not by itself tell an optimizer which intervention will change that person.

QUESTION:
Does the Centaur Operant Profile model persuasion effects or merely classify prior susceptibility?

DEEPER QUESTION:
How often does psychographic “personalization” confuse prediction of a person with prediction of a person’s response to an intervention?

MECHANISM:
Two mechanisms must remain separate:

person characteristic
→ baseline likelihood of action

versus

person characteristic × intervention
→ differential change caused by that intervention.

FORMAL SHIFT:
<PERSON PROFILE + MESSAGE>
→ <CONDITIONAL RESPONSE MODEL>
→ [ESTIMATE DIFFERENTIAL EFFECT]
→ <MESSAGE SELECTION>

SOURCE FORMALISM:
The source uses statistical models that distinguish individual predictors from interactions between persuasive strategies and psychological characteristics.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

logit P(Y=1) =
β0 + βP(PERSON) + βS(STRATEGY) + βPS(PERSON × STRATEGY)

βP ≠ βPS.

Predicting susceptibility requires βP.
Tailoring an intervention requires evidence about βPS.

TENSION:
The Centaur Box needs individualized causal leverage; much psychographic profiling supplies individualized prediction.

MISSING:
Evidence that the proposed Operant Profile variables produce stable, out-of-sample differences in response to specific interventions.

BOUNDARY:
Persuasion for Good does report some interaction patterns. The boundary is narrower: those results do not license treating every personality correlation as a tailoring rule.

CITATION TRAIL:
Wang et al. 2019.
Causal inference work on heterogeneous treatment effects.
IBM EviConv as a contrasting task concerned with convincingness rather than psychographic treatment response.

TEST:
Pre-register personality × strategy interactions, estimate them on one population, and require successful prediction of intervention effects on an unseen population before admitting a trait into a Gatekeeper Card.

PLATFORM:
[[Centaur Operant Profiles]]

LINKS:
[[Prediction Is Not Intervention]]
[[Psychographics Without Causality]]
[[Who Is Persuadable Is Not What Persuades Them]]

BIBTEX:
@inproceedings{wang2019persuasion,
  title={Persuasion for Good: Towards a Personalized Persuasive Dialogue System for Social Good},
  author={Wang, Xuewei and Shi, Weiyan and Kim, Richard and Oh, Yoojung and Yang, Sijia and Zhang, Jingwen and Yu, Zhou},
  booktitle={Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
  pages={5635--5649},
  year={2019},
  doi={10.18653/v1/P19-1566}
}

@misc{hartsoe_assi_centaurbox,
  author={Hartsoe, Watson and Assi, Tony},
  title={Thinking Outside the AI Box: The Centaur Box Experiment},
  note={Supplied manuscript; publication year not verified from supplied file}
}
