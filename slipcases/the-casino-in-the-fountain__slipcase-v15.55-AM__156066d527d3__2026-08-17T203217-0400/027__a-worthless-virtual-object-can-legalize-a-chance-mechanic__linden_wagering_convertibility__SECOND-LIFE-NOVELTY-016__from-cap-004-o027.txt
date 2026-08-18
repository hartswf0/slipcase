ZETTEL

ID:
SECOND-LIFE-NOVELTY-016

TITLE:
A worthless virtual object can legalize a chance mechanic by failing to become money.

SOURCE:
Linden Lab — Policy Regarding Wagering in Second Life — current official policy.

PASSAGE:
[PARAPHRASE] Linden Lab says a free-entry activity will likely be permitted, and similarly treats payouts involving novelty objects that cannot readily be converted into Linden dollars, real currency, or value as likely permissible.

RESEARCH OBJECT:
The virtual object's crucial property is not its texture, rarity, beauty, size, or 3D form.

It is its EXIT CAPACITY.

A reward can cease to trigger the same policy concern when it cannot readily traverse:

OBJECT
→ LINDEN DOLLARS
→ MONEY / VALUE.

LOCAL MOVE:
Linden Lab classifies an in-world object's significance partly by convertibility.

SOURCE TERMS:
payout
objects
novelty objects
converted
Linden dollars
real-world currency
value
consideration

WHAT BECAME STRANGE:
The legal/policy ontology of an object depends upon where it can go next.

A golden dragon and a useless pebble may look equally substantial in-world.

Their regulatory difference can reside entirely in an invisible exchange edge.

QUESTION:
Is value a property of an object or a path out of the world?

DEEPER QUESTION:
Should virtual-object ontology include its permitted transformations rather than merely its attributes?

MECHANISM:
<CHANCE>
→ <OBJECT>

PATH A:
<OBJECT>
-X→ <MONEY>
→ likely lower wagering concern under this policy

PATH B:
<OBJECT>
→ [CONVERT]
→ <L$ / REAL VALUE>
→ wagering concern increases

FORMAL SHIFT:
<VIRTUAL OBJECT AS THING>
→ <VIRTUAL OBJECT AS NODE IN EXCHANGE GRAPH>
→ [TEST REACHABILITY]
→ <VALUE STATUS>

SOURCE FORMALISM:
Linden Lab explicitly distinguishes novelty objects that cannot readily be converted into Linden dollars, real-world currency, or value.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

VALUE(o) :=
REACHABLE(
    o,
    {LINDEN_DOLLAR, REAL_CURRENCY, EXCHANGEABLE_VALUE}
)

The surprising variable is not:

PRICE(o)

but:

PATH_EXISTS(o → money).

TENSION:
Minecraft similarly permits server currencies only when they cannot be cashed out or transferred across servers.

The “failed” currency—the currency that cannot travel—may be precisely the compliant one.

MISSING:
How “readily converted” is operationally determined when unofficial markets, gifting, account sales, or off-platform exchanges exist.

BOUNDARY:
This is Linden Lab policy language, not a universal legal definition of gambling or value.

CITATION TRAIL:
[[LOOTBOX-BORDER-008]]
→ money or money's worth
→ Second Life novelty objects
→ value as graph reachability

[[MINECRAFT-MONEY-007]]
→ non-convertible server currency
→ economic membranes

TEST:
Construct identical random rewards with four exchange graphs:

A. no transfer
B. player-to-player transfer
C. Linden-dollar resale
D. external cash market

Hold the object itself constant.

Observe which classification changes are produced solely by adding edges.

PLATFORM:
[[Value is an exit route]]

LINKS:
[[LOOTBOX-BORDER-008]]
[[MINECRAFT-MONEY-007]]

BIBTEX:
@misc{linden_wagering_convertibility,
  author = {{Linden Lab}},
  title = {Policy Regarding Wagering in Second Life},
  url = {https://wiki.secondlife.com/wiki/Linden_Lab_Official:Policy_Regarding_Wagering_in_Second_Life},
  note = {Accessed 2026-08-17}
}