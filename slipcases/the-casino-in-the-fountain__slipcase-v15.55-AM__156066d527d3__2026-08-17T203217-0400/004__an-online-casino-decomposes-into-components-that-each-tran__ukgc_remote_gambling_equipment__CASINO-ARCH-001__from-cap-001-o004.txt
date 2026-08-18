ZETTEL

ID: CASINO-ARCH-001

TITLE:
An online casino decomposes into components that each transform a different kind of state.

SOURCE:
UK Gambling Commission — Remote Gambling Equipment — current guidance, accessed 2026-08-17.

SOURCE URL:
https://www.gamblingcommission.gov.uk/licensees-and-businesses/guide/remote-gambling-equipment

PASSAGE:
[PARAPHRASE] The Commission separately identifies customer management, settling, RNG, virtual-event control, back-office tools, security, and data components.

RESEARCH OBJECT:
The casino is not one program. It is an arrangement of components that generate numbers, map them to events, settle gambles, modify balances, maintain customer state, display results, and enforce access.

LOCAL MOVE:
The regulator decomposes an apparently singular application according to operational responsibilities and state transitions.

SOURCE TERMS:
component
customer management
settling
random number generator
virtual event control
back-office tools
security
customer account
event state

WHAT BECAME STRANGE:
What the player encounters as “a casino game” exists only because several machines with different authorities pass representations and state changes among one another.

QUESTION:
Where is the game?

DEEPER QUESTION:
If no single component contains the whole operative object, should software ontology begin from modules, messages, or transformations rather than applications?

MECHANISM:
<RNG>
→ random number

<RANDOM NUMBER + EVENT RULES>
→ virtual event result

<VIRTUAL EVENT RESULT + BET>
→ settling

<SETTLEMENT>
→ account balance change

<STATE>
→ client display

FORMAL SHIFT:
<CASINO AS APPLICATION>
→ <NETWORK OF SPECIALIZED COMPONENTS>
→ [PASS STATE + COMMANDS]
→ <GAMBLING EVENT>

SOURCE FORMALISM:
The source explicitly distinguishes software/data components by function, including RNG generation, virtual-event determination, settling, customer account management, and security.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

PLAYER
→ BET
→ EVENT_CONTROL
→ RNG
→ EVENT_CONTROL
→ SETTLEMENT
→ ACCOUNT_STATE
→ DISPLAY

The “game” is the successful traversal of this chain rather than a single executable object.

TENSION:
The uploaded mycelium.is source already notices that casinos may rely on separate developer platforms and separate payment-management systems. fileciteturn0file0L44-L54 The regulatory architecture makes the decomposition considerably finer-grained.

MISSING:
The guidance identifies components but does not imply that every operator deploys each component as a distinct physical server or software package.

BOUNDARY:
The component model is an operational/regulatory description, not necessarily the internal architecture of every commercial casino platform.

CITATION TRAIL:
UK Gambling Commission — Remote Gambling Equipment.
RTS 7 — Generation of Random Outcomes.
RTS requirements concerning interrupted gambling, security, and customer funds.
Software architecture literature on distributed transactions and state machines.

TEST:
Take one actual remote-gambling transaction and trace every state representation from wager submission through RNG request, event determination, settlement, account update, and client display.

PLATFORM:
[[A program can be a choreography of state transformations]]

LINKS:
[[RNG-002]]
[[Where is the program?]]
[[Interfaces between machines]]

BIBTEX:
@misc{ukgc_remote_gambling_equipment,
  author       = {{UK Gambling Commission}},
  title        = {Remote Gambling Equipment},
  url          = {https://www.gamblingcommission.gov.uk/licensees-and-businesses/guide/remote-gambling-equipment},
  note         = {Accessed 2026-08-17}
}