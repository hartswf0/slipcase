ZETTEL

ID:
PROMPT-GENRE-20260922-018

TITLE:
A richer game can make a thinner utterance sufficient

SOURCE:
Ludwig Wittgenstein, Philosophical Investigations, 4th ed., 1953/2009, §§2, 7. Richard A. Bolt, "Put-That-There: Voice and Gesture at the Graphics Interface," SIGGRAPH, 1980. Hartsoe synthesis.

SOURCE URL:
https://www.media.mit.edu/speech/papers/1980/bolt_SIGGRAPH80_put-that-there.pdf

PASSAGE:
[OUR SYNTHESIS]\nThe builder's 'Slab!' and Bolt's 'Put that there' both achieve economy because roles, referents, and allowable continuations live in the surrounding game.

RESEARCH OBJECT:
[OUR INFERENCE]\nTHICK PROMPTING IS COMPATIBLE WITH LESS TEXT.

LOCAL MOVE:
Prevent 'thick prompting' from becoming a recipe for prompt bloat.

SOURCE TERMS:
economy; shared state; deixis; game richness; prompt length

WHAT BECAME STRANGE:
A sophisticated interface can make the best prompt shorter by carrying context through state and gesture.

QUESTION:
What should the interface know so the user does not have to say it?

DEEPER QUESTION:
Can prompt quality improve while visible token count falls?

MECHANISM:
Persistent state, direct reference, enforced constraints, and feedback move context out of repeated prose.

FORMAL SHIFT:
RICHER_GAME -> LOWER_REQUIRED_LEXICAL_LOAD.

SOURCE FORMALISM:
[NO SOURCE FORMALISM]

OUR FORMALIZATION:
Thickness belongs to the interaction, not the string.

TENSION:
Hidden context can also make systems opaque and hard to reproduce.

MISSING:
Measures balancing linguistic economy against provenance and reconstructability.

BOUNDARY:
This is a cross-case synthesis; neither Wittgenstein nor Bolt makes this prompt-design claim.

CITATION TRAIL:
Slab! + Put That There -> thick interaction -> thin utterance.

TEST:
Compare task success, token count, and reconstructability across text-only versus stateful/deictic interfaces.

PLATFORM:
Prompt economy; HCI; thick prompting

LINKS:
[[PROMPT-GENRE-20260922-002]]
[[PROMPT-GENRE-20260922-005]]
[[PROMPT-GENRE-20260922-006]]
[[PROMPT-GENRE-20260922-017]]

BIBTEX:
@book{wittgenstein2009philosophical,
  author={Wittgenstein, Ludwig},
  title={Philosophical Investigations},
  edition={4},
  publisher={Wiley-Blackwell},
  year={2009}
}

@inproceedings{bolt1980put,
  author={Bolt, Richard A.},
  title={Put-That-There: Voice and Gesture at the Graphics Interface},
  booktitle={Proceedings of SIGGRAPH 1980},
  pages={262--270},
  year={1980}
}

@unpublished{hartsoe2026promptgenre,
  author={Hartsoe, Watson},
  title={The Prompt Is Not a Genre: Language Games, Operative Ekphrasis, and Worldtext},
  note={Working Paper},
  year={2026}
}
