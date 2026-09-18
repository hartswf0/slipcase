**Watson Hartsoe \| Working Paper \| 18 September 2026**

AI-augmented research process · Evidence, prompts, and making history
preserved in the associated SLIPCASE field.

**Abstract**

A shopping list is an unusually small piece of language that can
reorganize a future world. Its typical entries are noun phrases rather
than commands, yet they guide acquisition, sequence attention,
externalize progress, and survive changes in route, substitution, and
circumstance. This paper argues that the shopping list is best
understood neither as a miniature program nor as a passive memory aid,
but as a partial future-state language. It specifies conditions to be
made true while leaving reference resolution, order, locomotion, repair,
and often commitment to situated execution. Reading Wittgenstein's
grocer beside Anscombe's shopper, Suchman's critique of plans, Goody and
Lave's accounts of list and supermarket space, Engelbart's manipulable
NLS shopping list, and contemporary artifact-centered agent interfaces
reveals a recurring design problem: what must be made explicit for
language to become operational, and what can remain distributed across
people, artifacts, and world. The paper develops this as a contribution
to an operative humanities: a method for studying ordinary textual forms
by reconstructing the state changes, hidden operators, background
competencies, and material consequences they coordinate.

**Keywords:** shopping lists; language-games; situated action;
human-computer interaction; operative language; external
representations; prompting; spatial cognition

# 1. The strange power of a noun list

Milk. Bread. Eggs. The form looks almost maximally non-operative. There
is no imperative mood, no explicit agent, no route, no timing, no
account of what to do when the milk is unavailable, and no instruction
for deciding whether the eggs in the refrigerator make another carton
unnecessary. Yet a competent shopper can carry three nouns into a store
and return with a changed world. This is a useful anomaly for thinking
about contemporary interfaces. We increasingly ask computers to act from
descriptions that are similarly incomplete. The temptation is to say
that language has become executable. The shopping list suggests a more
precise claim: language can become operational while remaining radically
underdetermined by itself.

The shopping list is therefore a better object for the study of
operative language than the command line. A shell command wears its
operation on its syntax. A shopping list often does not. Its force is
distributed across a practice: a person recognizes the artifact as a
list, knows that listed nouns normally designate things to acquire,
enters an environment in which those things are spatially organized,
resolves local ambiguities, takes opportunities in an order that may
differ from the written one, crosses off or remembers completed items,
substitutes when the world resists, and stops when enough of the desired
future has been realized. The list contributes to this activity without
containing it.

I call this a partial future-state language. The phrase is intentionally
narrower than 'program' and more operational than 'description.' A
shopping list specifies some conditions toward which activity should
tend. It does not necessarily specify a total state, an exhaustive plan,
or a sequence of procedures. Empirical work reinforces this asymmetry:
shoppers often purchase items not written down while purchasing a large
majority of items that were listed (Block and Morwitz 1999). In other
words, the list frequently behaves as a set of selective commitments
rather than a complete world specification.

This paper develops the claim through a set of collisions rather than a
single genealogy. Wittgenstein and Anscombe make shopping lists
philosophically revealing; Goody, Lave, Kirsh, and Suchman expose their
spatial and situated organization; Engelbart makes a shopping list
computationally manipulable; distributed-cognition work shows that a
list can change role as goals, plan, and state; and recent agent
interfaces rediscover the need for an authoritative artifact distinct
from chat. These sources do not form one causal line. Their conjunction
is valuable because each isolates a different condition under which
sparse language becomes consequential.

# 2. Wittgenstein: the operation is not in the words alone

Wittgenstein opens Philosophical Investigations with a scene of
shopping. A person sends another to a shop with a slip whose marks
specify a number, a color, and apples. The shopkeeper locates the
relevant drawer, consults a color sample, counts, and selects.
Wittgenstein's question is not how a hidden semantic object inside the
word mechanically causes these acts. He redirects attention to use: this
is what is done with the signs in the practice (Wittgenstein 1953, §1).
The apparently simple inscription works because the actor already
inhabits a system of techniques, distinctions, objects, and
expectations.

That observation matters for computational interfaces because it changes
where executability is located. If the shopping slip were a
self-sufficient program, each necessary operation would have to be
recoverable from its inscription. It is not. The slip does not explain
counting, color matching, what counts as an apple, why a shopkeeper
should satisfy the request, or where the relevant objects are. The
sequence is executable only relative to background competence and an
environment in which the terms have practical purchase. The visible
string is the tip of an operational iceberg.

Wittgenstein later makes the role of use even harder to reduce to
linguistic surface form. In §21 he asks us to imagine the same words
serving as a report in one case and an order in another. The difference
can survive even when tone and expression are held constant. What
distinguishes the utterances is the role they play in the language-game.
This supplies an important warning for interface design. Classifying a
string as operative from grammar alone will fail whenever role is
supplied by interaction history, institutional setting, or the state of
a task.

Section 23 widens the field further. Among Wittgenstein's heterogeneous
language-games are giving orders and obeying them, describing objects,
reporting events, and constructing an object from a description or
drawing. This last case is especially important for generative media.
Description already participates in making long before contemporary
text-to-image or text-to-3D systems. What has changed is not the
discovery that descriptions can guide construction, but the speed,
scale, and delegation of the interpretive machinery between description
and constructed result. Operative language should therefore not be
defined by the fantasy that words have only recently begun to act. The
better question is what kind of apparatus now receives them, what that
apparatus assumes, and what part of the practical world it can change.

# 3. Anscombe: a future-state representation is a norm of correction

G. E. M. Anscombe's famous shopping-list example supplies a second
distinction. In Intention, she asks us to compare the shopper's list
with a detective's record of what the shopper purchases. The
inscriptions may correspond item for item. Their practical relation to
events differs. If the shopper departs from the intended list, the error
can lie in the performance; if the detective's record departs from what
actually happens, the error lies in the record (Anscombe 1957, §32).
Later speech-act theory would redescribe this contrast as opposing
'directions of fit,' but Anscombe's own diagnostic is more concrete:
when representation and event diverge, which side is to be corrected?

This is a powerful way to characterize a partial future state. A list
becomes practical not because it somehow ceases to represent, but
because it establishes a norm under which future activity can be
evaluated. 'Milk' on the list is not merely a proposition about milk. It
makes the absence of milk at the end of shopping potentially count as
unfinished business. The list participates in the definition of success.

But Anscombe's example should not be simplified into an unconditional
words-to-world arrow. She explicitly qualifies the contrast. A list
itself can be badly formed; circumstances can change; an item may no
longer be obtainable; judgment can be revised. This caveat becomes
critical for interactive systems. When a generated action does not match
a prompt, there are at least three possible failures: execution failed
to realize a valid specification; the system misunderstood the
specification; or the specification should itself change in light of the
world. A usable operative interface needs a repair policy, not merely an
execution engine.

