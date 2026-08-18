ZETTEL

ID:
Z-EDUPM-001

TITLE:
A GRADE FAILS THE MINIMUM TEST FOR A PREDICTION MARKET: IT IS A SIGNAL WITHOUT TRADING, PRICE DISCOVERY, OR CONTINGENT SETTLEMENT.

SOURCE:
Justin Wolfers and Eric Zitzewitz — “Prediction Markets” — 2004 — Journal of Economic Perspectives 18(2), 107–126.

SOURCE URL:
https://www.aeaweb.org/articles?id=10.1257%2F0895330041371321

PASSAGE:
[PARAPHRASE] Wolfers and Zitzewitz define the operative achievement of prediction markets as using markets to aggregate dispersed information into forecasts of uncertain future events. Carefully designed contracts allow market prices to express expectations about probabilities and other quantities.

RESEARCH OBJECT:
A minimal diagnostic for deciding when “prediction market” is literal and when it is metaphor.

LOCAL MOVE:
The paper locates prediction in a specific mechanism: participants trade contracts whose values depend on uncertain events, and the resulting market prices aggregate their information.

SOURCE TERMS:
prediction markets
dispersed information
market-generated forecasts
contracts
probabilities
uncertain future events
market design

WHAT BECAME STRANGE:
The university may be saturated with prediction while containing very few actual prediction markets.

A GPA predicts.
An admissions score predicts.
A student evaluation predicts.
A recommender predicts.
A credential signals.

None becomes a prediction market merely by being predictive.

QUESTION:
What additional machinery must an educational prediction acquire before “prediction market” becomes a literal rather than analogical description?

DEEPER QUESTION:
Does the more interesting object turn out to be not “education as prediction market” but an ecology of heterogeneous predictive instruments that allocate futures without allowing reciprocal bets?

MECHANISM:
<dispersed private beliefs>
→ <contingent contracts>
→ [TRADING]
→ <market price>
→ [EVENT OCCURS]
→ <settlement>

FORMAL SHIFT:
<UNCERTAIN EVENT>
→ <TRADEABLE CONTINGENT CLAIM>
→ [AGGREGATE INFORMATION THROUGH EXCHANGE]
→ <MARKET-GENERATED FORECAST>

SOURCE FORMALISM:
The source distinguishes contracts designed to reveal probabilities, means, medians, uncertainty, and conditional expectations. The market price is produced through exchange rather than assigned administratively.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

PREDICTION_MARKET(x) :=
    TRADEABLE(x)
    ∧ CONTINGENT_ON_FUTURE_EVENT(x)
    ∧ MULTIPLE_POSITION_TAKERS(x)
    ∧ PRICE_EMERGES_FROM_EXCHANGE(x)
    ∧ SETTLEMENT_RULE(x)

A grade fails several clauses.

TENSION:
The initial hypothesis gains rhetorical power by calling grades “prices,” degrees “contracts,” and universities “markets,” but doing so can erase the machinery that makes prediction markets epistemically distinctive.

MISSING:
A buyer.
A seller.
A trade.
A market-clearing mechanism.
A payoff.
A settlement rule.

BOUNDARY:
This does not show that grades or credentials lack predictive functions. It shows only that predictive function is insufficient to establish market structure.

CITATION TRAIL:
Wolfers & Zitzewitz — “Interpreting Prediction Market Prices as Probabilities.”
Robin Hanson — information markets / idea futures.
Mechanism-design literature on scoring rules and market makers.
Educational signaling literature distinguishing signals from markets.

TEST:
Take each proposed educational “prediction market” object and fill five columns:

TRADE?
CONTINGENT CONTRACT?
PRICE?
COUNTERPARTY?
SETTLEMENT?

Reject the literal market classification when the mechanism cannot populate them.

PLATFORM:
[[EDUCATION AS PREDICTIVE INFRASTRUCTURE]]

LINKS:
[[Prediction Market Minimum Test]]
[[Grades as Signals]]
[[Prediction Without Markets]]

BIBTEX:
@article{wolfers2004prediction,
  author  = {Wolfers, Justin and Zitzewitz, Eric},
  title   = {Prediction Markets},
  journal = {Journal of Economic Perspectives},
  year    = {2004},
  volume  = {18},
  number  = {2},
  pages   = {107--126},
  doi     = {10.1257/0895330041371321}
}