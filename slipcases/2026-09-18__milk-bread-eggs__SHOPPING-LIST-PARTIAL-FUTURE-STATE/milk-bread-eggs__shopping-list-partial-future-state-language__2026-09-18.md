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

The later philosophical afterlife of the shopping list makes this even
clearer. Searle generalizes Anscombe's contrast into direction of fit as
part of a finite taxonomy of illocutionary acts (Searle 1975). Millikan
begins from the same example and proposes 'pushmi-pullyu'
representations that can simultaneously describe and direct (Millikan
1995). The history is useful because it reveals that practical language
cannot always be placed cleanly on one side of a representational
divide. A generative prompt such as 'a red house beside the river' can
describe a candidate world and direct a system to realize one at the
same time. The operative humanities needs to preserve this hybridity
rather than force every artifact into either description or command.

# 4. Suchman: the list says how shopping should turn out, not how shopping happens

Lucy Suchman's Plans and Situated Actions makes the shopping list an
explicit objection to treating plans as descriptions of action. Her user
of an expert-help system is placed in the shopper's position:
instructions can be consulted for what to do next, for deciding when
activity is complete, or for retrospectively explaining action. Yet, as
Suchman observes, the shopping list does not describe the practical
organization of shopping itself: finding objects, choosing aisles,
comparing brands, or handling the local circumstances that determine the
next move (Suchman 1987, 73). It says how the activity is to turn out.

This distinction is the center of the paper. A shopping list is
operational without being procedural. That combination is easily missed
because computing inherited strong models in which successful execution
means faithful traversal of an explicit instruction sequence. The
shopping case separates target from trajectory. It externalizes a set of
desired changes while leaving the route open.

The distinction can be written schematically. Let G be a set of goals
encoded by the list. Let W be the current world, including locations,
inventory, obstacles, prices, social conventions, and available
substitutions. Let S_t be the shopper's current state, including
position, acquired items, and remaining goals. A competent next action
is not a function of G alone. It depends on G, W, and S_t, and may alter
G itself. The operative loop is therefore not LIST -> EXECUTE. It is
LIST + WORLD + ACTOR -> LOCALLY RESOLVE -> ACT -> UPDATE -> REVISE.

This helps distinguish a shopping list from code without demoting it to
mere reminder. Suchman does not argue that plans are useless. She argues
against identifying the structure of the representation with the
structure of situated activity. That is precisely the mistake prompt
discourse risks when it treats a successful output as proof that a
natural-language prompt contained a complete program. The more capable
the interpreter, the less procedure the user needs to state. Apparent
linguistic executability can therefore increase because the interpreter
absorbs more of the missing work.

# 5. Goody and Lave: the list is spatiotemporal before it is digital

Jack Goody gives the shopping list a different operational character. In
his analysis of literacy and lists, the shopping list is more than a
record of needed objects: writing makes items visually separable and
rearrangeable. They can be grouped according to source of supply and
thereby used to construct a future schedule in space and time (Goody
1977). The order of marks on paper can anticipate the order of bodily
movement.

This is already a small form of spatial computation. Reordering does not
change the set of desired groceries. It changes the cost structure of
future action. Kirsh later develops a broader account of the intelligent
use of space, arguing that arrangements can simplify choice, simplify
perception, or simplify internal computation (Kirsh 1995). A list sorted
by aisle does cognitive work because it aligns an external
representation with the topology of the environment. The shopper no
longer has to repeatedly search the whole store for the next noun.

Jean Lave, Michael Murtaugh, and Olivia de la Rocha radicalize this
spatial account by describing the supermarket itself as something like
an 'ultimate grocery list': a materially ordered field of independently
obtainable objects. A particular shopping route emerges through
articulation between two structures, the shopper's purchase intentions
and the arrangement of the store (Lave, Murtaugh, and de la Rocha 1984).
The world is not a passive container in which the list executes. The
world's organization participates in determining sequence.

