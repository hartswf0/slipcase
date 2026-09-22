ZETTEL

ID:
20260921-clever-hans-word-reading-goes-from-all-correct-to-none

TITLE:
Hans’s “Reading” Fell from 100 Percent to Zero When the Questioner Lost Positional Knowledge

SOURCE:
Oskar Pfungst — Clever Hans (The Horse of Mr. von Osten) — 1911 English translation — experimental tests, pp. 36–38. ([gutenberg.org](https://www.gutenberg.org/cache/epub/33936/pg33936-images.html?utm_source=chatgpt.com))

PASSAGE:
[PARAPHRASE] Pfungst arranged placards carrying words such as “Hans” and “Stall.” In fourteen trials where the questioner knew the position of the requested word, Hans was correct in every case. In twelve trials where the questioner could see the word but did not know its position in the row, Hans produced no correct responses. ([gutenberg.org](https://www.gutenberg.org/cache/epub/33936/pg33936-images.html?utm_source=chatgpt.com))

RESEARCH OBJECT:
Removing one item of evaluator knowledge destroying apparently perfect performance while preserving the nominal stimulus class.

LOCAL MOVE:
The experiment holds the apparent “reading” task in place while manipulating whether a human in the loop knows the correct spatial answer.

SOURCE TERMS:
placards
word
procedure with knowledge
procedure without knowledge
questioner
position
correct responses

WHAT BECAME STRANGE:
Hans can still see the placards in both conditions. The decisive missing information exists in another mind. The effective task input therefore includes knowledge state distributed across the experimental arrangement.

QUESTION:
What AI capabilities currently appear to belong to the evaluated model but disappear when task-relevant state is removed from surrounding components?

DEEPER QUESTION:
Can capability attribution be experimentally decomposed by systematically varying who or what in the total evaluation system possesses the answer-relevant information?

MECHANISM:
questioner knows correct location
→ involuntary bodily cue covaries with target
→ horse perceives cue
→ perfect apparent reading.

Questioner lacks target position
→ cue cannot encode correct stopping/location relation
→ performance collapses.

FORMAL SHIFT:
<SUBJECT HAS CAPABILITY>
→ <ARRANGEMENT PRODUCES PERFORMANCE>
→ [REMOVE KNOWLEDGE FROM ONE COMPONENT]
→ <LOCATE DEPENDENCY>

SOURCE FORMALISM:
Pfungst explicitly contrasts “procedure with knowledge” and “procedure without knowledge” across controlled trials. ([gutenberg.org](https://www.gutenberg.org/cache/epub/33936/pg33936-images.html?utm_source=chatgpt.com))

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
capability attribution requires interventions over:
knowledge(model),
knowledge(wrapper),
knowledge(grader),
knowledge(human),
knowledge(environment).

TENSION:
A modern model can contain target-relevant knowledge internally from training even when every runtime evaluator is blinded.

MISSING:
Evaluation designs using genuinely post-training secrets or freshly generated target states so prior model exposure can be excluded.

BOUNDARY:
Hans exploited perceptible human cues. The result cannot be generalized to AI without identifying an actual information path.

CITATION TRAIL:
[[20260921-clever-hans-knowledge-condition-collapses-from-98-to-8]]
→ Pfungst’s word-placard trial
→ the stronger 100%-to-0 case isolates evaluator positional knowledge.

TEST:
Generate a novel hidden spatial arrangement after model training. Run conditions where wrapper, grader, human proctor, or no pre-commit component knows the target mapping. Compare performance while preserving the visible task.

PLATFORM:
[[evaluation-as-language-game]]

LINKS:
[[20260921-clever-hans-knowledge-condition-collapses-from-98-to-8]]
[[Clever-Hans]]
[[distributed-knowledge]]
[[capability-attribution]]

BIBTEX:
@book{pfungst1911clever,
  author = {Pfungst, Oskar},
  title = {Clever Hans (The Horse of Mr. von Osten): A Contribution to Experimental Animal and Human Psychology},
  translator = {Rahn, Carl L.},
  year = {1911},
  publisher = {Henry Holt and Company},
  address = {New York}
}
