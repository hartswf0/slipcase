ZETTEL

ID:
CBX-004-TRANSPARENCY-ATTACK-SURFACE

TITLE:
A Gatekeeper Card can make governance more transparent by making the governor more targetable.

SOURCE:
Hartsoe — Centaur Box Experiment: Aligning Freedom, Practicing Persuasion, and Crafting Synthetic Gatekeepers — supplied manuscript — “Transparent Gatekeepers”; Mitchell et al. — Model Cards for Model Reporting — 2019.

PASSAGE:
[PARAPHRASE]
The Centaur manuscript proposes “Gatekeeper Cards,” inspired by Model Cards, to expose developer worldviews and motivations. Elsewhere the same project proposes using modeled biases, motivations, and constraints to improve persuasive interventions.

RESEARCH OBJECT:
Transparency and exploitability can be produced by the same representation.

LOCAL MOVE:
The Gatekeeper Card transfers the documentation gesture from a technical artifact to a human decision-maker.

SOURCE TERMS:
Gatekeeper Cards
Model Cards
worldviews
motivations
transparency
operant profiles
human architectures

WHAT BECAME STRANGE:
Model Cards document characteristics of models so others can evaluate their use. Gatekeeper Cards would document characteristics of people inside an architecture explicitly interested in learning how to influence them.

QUESTION:
When does governance transparency become adversarial reconnaissance?

DEEPER QUESTION:
Can we disclose enough about a decision process to make power accountable without disclosing enough about particular people to make their decisions easier to manipulate?

MECHANISM:
Governance disclosure
→ structured human representation
→ extraction of stable features
→ targeting
→ optimized intervention.

FORMAL SHIFT:
<HUMAN GOVERNANCE CONTEXT>
→ <GATEKEEPER CARD>
→ [PROFILE / TARGET]
→ <PERSUASION POLICY>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Transparency utility = accountability gain − exploitation gain.

A Gatekeeper Card is governance-positive only if its marginal accountability value exceeds the targeting capacity it creates.

TENSION:
The manuscript simultaneously values “transparency not only in systems, but in humans” and treats knowledge of gatekeeper psychology as leverage.

MISSING:
A disclosure boundary separating institutionally relevant rationales from psychologically exploitable personal information.

BOUNDARY:
Nothing in the supplied manuscript demonstrates that Gatekeeper Cards will actually increase manipulation. The opening is that the proposed artifact has two mechanically opposed uses that require separate evaluation.

CITATION TRAIL:
Mitchell et al. 2019, Model Cards.
Documentation research on Datasheets and system cards.
Security research on information disclosure and attack surfaces.
Mental privacy and cognitive liberty literature.

TEST:
Give one red team access to a Gatekeeper Card and another only public role/institution information. Measure improvement in predicting or changing decisions. Separately test whether auditors gain governance-relevant understanding from the same added fields.

PLATFORM:
[[Transparent Gatekeepers]]

LINKS:
[[Transparency Can Leak Leverage]]
[[Human Model Cards]]
[[Accountability Without Psychographic Exposure]]

BIBTEX:
@inproceedings{mitchell2019model,
  title={Model Cards for Model Reporting},
  author={Mitchell, Margaret and Wu, Simone and Zaldivar, Andrew and Barnes, Parker and Vasserman, Lucy and Hutchinson, Ben and Spitzer, Elena and Raji, Inioluwa Deborah and Gebru, Timnit},
  booktitle={Proceedings of the Conference on Fairness, Accountability, and Transparency},
  pages={220--229},
  year={2019},
  doi={10.1145/3287560.3287596}
}

@misc{hartsoe_centaurbox_expanded,
  author={Hartsoe, Watson},
  title={Centaur Box Experiment: Aligning Freedom, Practicing Persuasion, and Crafting Synthetic Gatekeepers},
  note={Supplied manuscript; publication year not verified from supplied file}
}
