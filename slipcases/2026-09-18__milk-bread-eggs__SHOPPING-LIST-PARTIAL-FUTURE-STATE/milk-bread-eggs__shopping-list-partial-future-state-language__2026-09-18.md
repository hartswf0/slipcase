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

This yields a useful way to state the spatiotemporal problem. A
conventional shopping list specifies membership better than order. It
says which conditions should eventually become true, while leaving many
permutations acceptable. Store layout, current position, crowding,
perishability, personal habit, and opportunity convert this partially
ordered set into a trajectory. The natural temporal grammar of shopping
is therefore not simply first/then. It is closer to: accomplish these
goals, opportunistically, under spatial constraints, while keeping track
of what remains.

# 6. Three lists at once: future, present, and past

Conein and Jacopin make this distributed structure unusually explicit.
In their account of projected plans and workspace, shopping can be
understood through three external representations: the written list of
objects still to obtain; the store's spatial arrangement of available
objects; and the accumulated contents of the cart, which provide a
material trace of what has already been collected (Conein and Jacopin
1996). The activity is organized across prospective, present, and
retrospective representations.

Distributed-cognition work makes a related point at the level of one
artifact. Furniss and Blandford use the shopping list as an example of
coordinated cognitive resources. Its items can function as goals. If the
items are ordered according to pickup sequence, the same artifact can
function as a plan. If collected items are crossed off, it can display
current state (Furniss and Blandford 2006). A tiny mark changes the
representational role of the object.

This is a direct bridge to user-interface design. A useful task surface
often needs to distinguish at least three questions: What is wanted?
What is available or relevant now? What has already happened? Chat
interfaces tend to flatten these into a transcript. A shopping list
makes their separation visible. The checkbox is especially instructive.
Checking off 'milk' is neither ordinary linguistic description nor mere
decoration. It is a low-cost state transition that changes what deserves
attention next.

The result is a minimal state machine hidden in an everyday genre. OPEN
-> DONE is one state change. Reordering supplies a tentative temporal
relation. Location binding adds spatial grounding. Substitution changes
the referent while preserving a higher-level goal. Deleting an item
revises the desired future. Adding an item during the trip records a
newly discovered goal. None of these operations requires the list to
become a full program. They make explicit exactly those parts of
activity for which external state is useful, while leaving the rest to
situated judgment.

# 7. Specifically vague: why sparse language can be better language

A further complication appears when we ask what a list item actually
denotes. Ethnomethodological work on household grocery practices finds
that entries are often 'specifically vague.' A household member may
write 'beans' because members already know which beans, what quantity,
and under what circumstances the item is needed. The written entry is
sparse because local competence is rich (Hyland et al. 2018). To an
outsider or a product database, the same token is under-specified.

This reverses a common assumption in interface design. More explicit
language is not always better language. A form that forces brand, size,
SKU, quantity, store, and substitution policy may increase machine
addressability while increasing human attention cost. The right amount
of specification depends on how much world is shared between writer and
interpreter.

Hyland and colleagues also show that the list is temporally distributed
before the shopping trip begins. Physical lists are often positioned in
high-throughput household locations where a disappearing item can
occasion an immediate mark. The list is written across a week by
encounters with a changing material environment. Its placement is part
of its semantics. A digital list that is accessible everywhere but
absent at the moment an empty container is noticed can be less situated
than a scrap of paper fixed to the refrigerator.

This matters for AI because model context can mimic household
familiarity while also hiding its uncertainty. If an assistant has seen
a year's purchases, 'beans' may become resolvable without clarification.
But silent resolution creates a new responsibility: the system must know
when its inferred referent is stable enough to act. The goal is not
maximal explicitness. It is calibrated shared context, with ambiguity
becoming visible when its consequences exceed the tolerance of the task.

# 8. Engelbart: when the list becomes a manipulable computational object

Douglas Engelbart's shopping list in the 1968 NLS demonstration is often
folded into a general story about hypertext. Engelbart's own
retrospective description is more specific: the temporary shopping list
was the beginning of demonstrating ways of 'structuring ideas.' NLS
allowed items to become statements and branches that could be moved,
grouped, subordinated, clipped by level, truncated, filtered, and
displayed through different views (Engelbart and English 1968; Engelbart
1986). The crucial shift is not simply from paper to screen. It is from
externally visible structure to machine-addressable structure.

A handwritten list can be reordered, crossed off, and grouped. NLS adds
an ontology of manipulable entities and operations. A branch can be
moved as a branch. A view can be recomputed from underlying structure
without destroying it. The user's conceptual distinction becomes legible
to the computer as state. This is why Engelbart's example belongs next
to the philosophical shopping lists without being reduced to them: it
materializes a new layer of operational consequence.

The important unit in NLS is therefore not the static list but the
sequence of representational transformations. Engelbart and English
describe skilled users changing views rapidly to suit immediate needs.
Reading and editing are coupled in what the paper calls
'study-manipulate.' The user studies a structure, alters it, sees a new
view, and acts again. The interface turns representation into a
recurrent boundary between interpretation and operation.

For contemporary prompting, this suggests a design principle. Natural
language may be most valuable at moments when the desired transformation
is difficult to parameterize in advance. Once an object has acquired
explicit state, direct manipulation can be better than repeatedly
describing deterministic changes in prose. 'Make a weekly dinner plan
under $100' is a plausible language move. Changing quantity 2 to
quantity 3 is not improved by forcing the user to phrase it as a
sentence. Engelbart's shopping list points toward mixed operative
surfaces in which language constructs or deforms structures and widgets
expose stable state.

# 9. From chat to artifact: the list as a model for agentic UI

Recent shopping-agent interfaces make this old problem newly concrete.
DoorDash's 2026 engineering account of Ask DoorDash describes an
evolution from conversational result carousels toward a persistent
shopping-list artifact. The artifact, rather than the chat transcript,
is treated as authoritative application state; low-ambiguity edits such
as quantity changes, removals, and swaps can be made directly, while the
agent receives a reduced representation when judgment is needed
(Shillington and Wei 2026). The case should not be generalized from one
company implementation, but its architectural move is revealing.

The shopping list solves a problem that chat creates. Conversation is
excellent at negotiating underspecified intent, but weak as a durable
representation of current task state. A transcript forces users and
models to reconstruct which requests remain active, which proposals have
been superseded, and what was actually committed. A list externalizes
those distinctions.

The same system also separates the proposed shopping list from the cart.
This produces a useful transaction boundary: language can generate a
candidate future; direct manipulation can revise it; only an explicit
commit operation moves the proposal into consequential purchase state.
Anscombe's practical representation thus acquires a modern UI nuance.
Between words and world there can be a reversible proposal layer.

This intermediate state matters beyond shopping. Generative systems
increasingly operate in domains where a model can modify files, scenes,
calendars, code, messages, or physical devices. The relevant design
question is not simply whether the system can act. It is which state
transitions should remain proposals, which should be directly
manipulable, which can be automatic, and which require explicit
commitment. The shopping list provides a compact laboratory for these
distinctions because ordinary practice already contains goals,
substitutions, state updates, incomplete order, and a recognizable
completion condition.

# 10. Toward an operative humanities

The shopping list suggests a methodological program for the humanities.
Ordinary textual forms are often classified by content, rhetoric, genre,
or representation. An operative humanities adds another set of
questions. What state does this form presuppose? What changes when
someone uses it? Which operators are explicit and which are supplied by
convention? What background competence is required? What does the
artifact externalize? What does the environment contribute? Where is
mismatch repaired? Which transitions are reversible? When does a mark
become a commitment?

