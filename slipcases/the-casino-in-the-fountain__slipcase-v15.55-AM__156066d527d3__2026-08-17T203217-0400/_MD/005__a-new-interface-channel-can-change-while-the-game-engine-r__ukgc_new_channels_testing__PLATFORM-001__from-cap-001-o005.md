ZETTEL

ID: PLATFORM-001

TITLE:
A new interface channel can change while the game engine remains the same.

SOURCE:
UK Gambling Commission — Testing Strategy for Compliance with Remote Gambling and Software Technical Standards — Procedure for Testing — updated 2024.

SOURCE URL:
https://www.gamblingcommission.gov.uk/strategy/testing-strategy-for-compliance-with-remote-gambling-and-software-technical/3-procedure-for-testing

PASSAGE:
[PARAPHRASE] When an existing game is ported to a new channel, testing may concern the interface and display while unchanged backend game functionality need not be retested.

RESEARCH OBJECT:
The regulator distinguishes a game's channel from its backend game logic strongly enough that one can change without necessarily changing the other.

LOCAL MOVE:
The testing regime uses selective retesting to encode an architectural distinction between presentation and game-engine behavior.

SOURCE TERMS:
channel
game client
user interface
player display
backend game design
functionality
HTML5
native mobile app
retesting

WHAT BECAME STRANGE:
Moving a game from one platform to another does not necessarily mean translating the game itself. Sometimes only the apparatus through which the game becomes perceptible and actionable changes.

QUESTION:
What exactly crosses platforms when software is “ported”?

DEEPER QUESTION:
When interface, execution, and semantics can change independently, which layer deserves to be called the program?

MECHANISM:
<EXISTING GAME ENGINE>
→ attach new client/channel
→ [TEST UI + PLAYER DISPLAY]
→ <NEW PLATFORM ACCESS>

while:

<BACKEND LOGIC>
→ unchanged
→ [REUSE PRIOR TEST EVIDENCE]
→ <NO FULL RETEST>

FORMAL SHIFT:
<PLATFORM CHANGE>
→ <CHANNEL CHANGE | ENGINE CHANGE>
→ [CLASSIFY SCOPE OF CHANGE]
→ <SELECT TEST OBLIGATION>

SOURCE FORMALISM:
The testing strategy explicitly distinguishes:
- intended channels,
- HTML5/native mobile clients,
- interface/player-display tests,
- backend game design/functionality,
- conditions under which backend retesting is unnecessary.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

PROGRAM :=
ENGINE × CHANNEL

PORT(P, C₁ → C₂)

If ENGINE₁ = ENGINE₂:
    RETEST := CHANNEL_DELTA
else:
    RETEST := CHANNEL_DELTA + ENGINE_DELTA

TENSION:
The uploaded article proposes lack of mobile availability as evidence that a developer may have used “obsolete development technology.” fileciteturn0file0L32-L42 The testing framework shows that channel support is a separable architectural dimension and cannot by itself identify the condition of backend game logic.

MISSING:
Neither source supplies enough evidence to infer the engineering quality of a particular developer from platform availability alone.

BOUNDARY:
Separable testing does not mean platform changes are trivial. It means regulators recognize cases where presentation changes while game behavior does not.

CITATION TRAIL:
UKGC testing strategy — new channels.
Historical Flash-to-HTML5 casino migrations.
Software portability and separation-of-concerns literature.
Research on whether interface changes alter gambling behavior despite unchanged underlying probabilities.

TEST:
Take one game released as both HTML5 and native mobile clients. Compare backend requests, state transitions, probabilities, timing, interaction design, and regulatory test reports to determine exactly what survived the port.

PLATFORM:
[[What travels when software crosses media?]]

LINKS:
[[Channel is not engine]]
[[Porting as selective transformation]]
[[Interfaces can change without changing semantics]]

BIBTEX:
@misc{ukgc_new_channels_testing,
  author       = {{UK Gambling Commission}},
  title        = {Testing Strategy for Compliance with Remote Gambling and Software Technical Standards: Procedure for Testing},
  year         = {2024},
  url          = {https://www.gamblingcommission.gov.uk/strategy/testing-strategy-for-compliance-with-remote-gambling-and-software-technical/3-procedure-for-testing},
  note         = {Updated 13 September 2024; accessed 2026-08-17}
}