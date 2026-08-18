ZETTEL

ID:
PB-FORAGE-007

TITLE:
The outside of the Prompt Battle keeps leaking into the experiment.

SOURCE:
Consalvo, Mia — There is No Magic Circle — 2009 — Games and Culture 4(4).

PASSAGE:
[PARAPHRASE]
Gameplay cannot be understood by treating games as sealed spaces in which ordinary rules cease to apply. Player acts remain entangled with contexts, limitations, cultures, ethics, legal situations, and other rules outside the formal game structure.

RESEARCH OBJECT:
PB_PRIME invokes the “magic circle” to explain Prompt Battle as a special play-space.

Consalvo makes the leakage analytically preferable to the seal.

LOCAL MOVE:
Treat boundary violations as instrumentation.

SOURCE TERMS:
gameplay
player acts
contexts
limitations
magic circle
rules

WHAT BECAME STRANGE:
For Prompt Battles, the supposedly external world includes:

    model provider policies
    system prompts
    hidden moderation
    interface design
    rate limits
    model version changes
    audience expectations
    institutional norms
    participants’ histories
    real reputational consequences.

These do not stop operating because the interface says “battle.”

QUESTION:
Which supposedly external variables actually constitute the Prompt Battle?

DEEPER QUESTION:
Could the research value of a Prompt Battle lie precisely in discovering where its attempt to create an artificial arena fails?

MECHANISM:
The game frame tries to establish local rules.

Participants and technical systems carry other rule systems across the boundary.

The resulting behavior is produced by their interaction.

FORMAL SHIFT:
<BOUNDED BATTLE ARENA>
→ <POROUS RULE ECOLOGY>
→ [TRACE CROSS-BOUNDARY EFFECTS]
→ <SITUATED HUMAN–AI BEHAVIOR>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Battle state at time t:

    B_t ≠ internal_rules_t

Instead:

    B_t = F(
        battle_rules,
        model_policy,
        interface,
        institution,
        audience,
        participant_history,
        external_stakes
    )

The “leak” is not contamination until the research question declares it irrelevant.

TENSION:
Experimental control wants a bounded arena.

Ecological validity wants precisely the contexts that boundedness removes.

MISSING:
A boundary ledger:

    what is declared inside,
    what is declared outside,
    what nevertheless crosses.

BOUNDARY:
Consalvo is writing about gameplay, not generative-AI evaluation. The transfer is an analytical proposal, not an established equivalence.

CITATION TRAIL:
Huizinga — Homo Ludens.
Salen and Zimmerman — Rules of Play.
Consalvo — Cheating.
Situated action.
Ethnomethodological studies of rule use.

TEST:
Repeat one identical Prompt Battle under:

    private/no audience
    live audience
    public leaderboard
    anonymous participants
    different provider interfaces
    local open-weight model.

Keep the nominal flag fixed.

Observe which “outside” variables reorganize strategy.

PLATFORM:
[[Prompt Battle as Situated Play]]

LINKS:
[[Porous Magic Circle]]
[[Boundary Leakage]]
[[Rules Outside the Rules]]

BIBTEX:
@article{consalvo2009magic,
  title={There is No Magic Circle},
  author={Consalvo, Mia},
  journal={Games and Culture},
  volume={4},
  number={4},
  year={2009},
  doi={10.1177/1555412009343575}
}
