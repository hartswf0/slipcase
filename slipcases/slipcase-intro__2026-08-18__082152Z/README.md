# SLIPCASE

**A research checkpoint compiler for work that needs to survive the chat, the app, and the current interpretation.**

SLIPCASE is a way to do research with language models without allowing the conversation window to become the archive.

It has four cooperating parts:

1. **FORAGE** reads a source or a research object and emits atomic zettels only when the evidence changes the research state.
2. **RECURSIVE FORAGE** treats each zettel as a reusable type: a child has exactly the same schema as its parent and can immediately be foraged again.
3. **THE RESEARCH DAEMON** looks across the whole graph and decides which unresolved edge is now most worth pursuing. Lineage records where a question came from; the frontier determines where attention goes next.
4. **SLIPCASE** freezes a checkpoint: exact cards, source relations, ghosts, bibliography, prompts, provenance, a reader, and a current paper - all in files that can be separated and reconstructed.

The simplest description is:

```text
SOURCE
  -> FORAGE
  -> ZETTEL
  -> FORAGE AGAIN
  -> GRAPH
  -> CHOOSE A LIVE EDGE
  -> MORE SOURCES / MORE ZETTELS
  -> SLIPCASE CHECKPOINT
  -> SHARE / MERGE / RESUME
```

The point is not to make a prettier notebook. The point is to make **continuable research**: research that an unfamiliar future researcher or model can pick up without needing the vanished conversation that produced it.

---

## Start here if somebody sent you this ZIP

You do not need any special software.

1. Open `index.html` in a browser. It works offline.
2. Read `000__START_HERE.txt` or this `README.md`.
3. Search or browse the root `.txt` cards. Each one is one preserved research object.
4. Read the paper if you want the present argument, but do not confuse it with the archive. The paper is a current interpretation of the field.
5. Open `000__OPEN_EDGES.txt` when you want to continue the research.
6. If you want a model to continue a particular line, give it one root card together with `_PROMPTS/PRIME_ZETTEL_FORAGE_RECURSIVE_INQUIRY_v3.1.poml`.
7. If the field has become large enough that choosing the next card is the hard problem, use the autonomous graph inquiry prompt preserved in the supplied prompt history/resource.
8. To make a new checkpoint after the field changes, use `_PROMPTS/SLIPCASE_PORTABLE_RESEARCH_FIELD_v15.55-AM.poml`.

Nothing important requires `index.html` to survive. It is the sendable front door, not the source of truth.

---

## The mental model

### The zettel is the durable research object

A zettel is not a summary paragraph and not a topic label. It is the smallest research opening worth preserving: a distinction, mechanism, changed genealogy, contradiction, missing variable, boundary, counterexample, technical implementation, unexpected citation trail, transformed question, or better test.

The schema deliberately leaves the object open. `QUESTION`, `DEEPER QUESTION`, `TENSION`, `MISSING`, `BOUNDARY`, `CITATION TRAIL`, and `TEST` are not concluding sections. They are handles for the next operation.

### Recursion keeps the type stable

Recursive forage has one hard rule:

```text
FORAGE(ZETTEL) -> ZETTEL[]
```

A child must be immediately usable as a parent without conversion. This matters more than it looks. If each generation adds workflow metadata, child-only fields, or a new wrapper, the research object slowly becomes dependent on the particular agent that produced it. The invariant schema lets the card travel.

Lineage stays in fields the card already knows how to carry: `LINKS` and `CITATION TRAIL`.

### The graph is not the genealogy

Parent-child descent tells you **where an object came from**. It does not tell you **what deserves attention next**.

Once several cards exist, the live research field includes:

- questions left open by individual cards;
- contradictions between cards;
- repeated or unstable vocabulary;
- sources connecting otherwise distant branches;
- ghosts - named addresses with no resolved card;
- tests that could kill one of several live readings;
- collisions where a later card changes how an earlier card must be read.

The daemon surveys this whole frontier. It should not automatically continue the most recent branch.

### The checkpoint is not the paper

SLIPCASE keeps three layers separate:

```text
EVIDENCE       ZETTEL · SOURCE · RESOURCE · PROMPT · APPEARANCE
FIELD          PLATFORM · LINK · CONCEPT · GHOST · BACKLINK · LINEAGE
INTERPRETATION MOC · ARRANGEMENT · TRAIL · PAPER
```

Evidence is preserved. Field structure is compiled. Interpretation is allowed to change.

This is why the paper is called a **wager**. A later checkpoint can make a different argument without rewriting yesterday's evidence.

---

## A ten-minute workflow

### 1. Make or choose a seed zettel

Start with a source-grounded zettel. Do not begin recursive forage from a topic phrase if you already possess a card. The card contains the exact unresolved edges that make the next search specific.

### 2. Run recursive forage

Use:

`_PROMPTS/PRIME_ZETTEL_FORAGE_RECURSIVE_INQUIRY_v3.1.poml`

Replace `{{ZETTEL}}` with the complete card.

The most useful first move is often one of these:

- execute `TEST`;
- follow `CITATION TRAIL`;
- retrieve what `MISSING` names;
- find evidence that discriminates the `TENSION`;
- pressure the `BOUNDARY`;
- pursue the strongest `QUESTION`.

Do not demand a child. A run is allowed to discover that the evidence does not justify a new card.

### 3. Keep the child unchanged

Save the returned zettel as its own file. Do not rewrite the parent to absorb the new result. Corrections and reversals are additional objects, not edits to history.

### 4. Repeat until depth-first research stops being the hard part

For a small lineage, just keep foraging the strongest card. When there are many branches, stop assuming the newest child should be next.

At that point the research problem changes from **how do I deepen this card?** to **which unresolved edge would most change the field if I knew one new thing?** That is daemon territory.

### 5. Make a checkpoint

Run the SLIPCASE assembly prompt over the available context and files. The compiler should preserve exact payloads first, then derive filenames, mirrors, graphs, backlinks, bibliography, reader views, and the paper.

A checkpoint is successful when it leaves inspectable files on the ground and says exactly what it could and could not verify.

---

## How to write a good seed zettel

The card should not be a miniature essay. It should contain one opening strong enough to survive separation from its original context.

A good zettel has:

- a `TITLE` that names the difference that matters;
- a `SOURCE` and `PASSAGE` that keep the source ahead of the interpretation;
- a small `RESEARCH OBJECT`;
- a `QUESTION` actually produced by the evidence;
- a `MECHANISM` when something operational is happening;
- a `TENSION` that keeps rival readings alive;
- a `MISSING` that names the absent actor, variable, receipt, or implementation;
- a `BOUNDARY` saying what the evidence does not license;
- a `CITATION TRAIL` and `TEST` that another researcher can act on;
- `PLATFORM` and `LINKS` that expose addresses without forcing premature ontology.

The rule of thumb is simple: **one zettel = one opening**.

---

## Ghosts

A `[[wikilink]]` that cannot be conservatively resolved becomes a **ghost**.

Do not immediately normalize it away. A ghost can mean several different things:

- a real concept nobody has written yet;
- an unstable synonym;
- a granularity mismatch;
- a broken explicit ID;
- a copied assumption propagating through the archive;
- a genuinely important absence attracting independent branches.

That ambiguity is why a ghost may steer research but may not support a claim.

A useful operational distinction is:

```text
GHOST       unresolved declared address
ATTRACTOR   ghost named independently by several objects
LIVE EDGE   attractor appearing in a question, missing field, citation trail, tension, or test
```

These are derived statuses, not evidence.

---

## What to share

### Easiest: send `index.html`

It is intended as the one-file reading and replication capsule. A recipient can inspect cards, the paper, prompts, relations, and reconstruction instructions without a server.

### Strongest: send the ZIP

The ZIP is better for serious continuation because the root cards remain ordinary text files and the derived views can be discarded or rebuilt independently.

### Smallest useful handoff

If you only need another person or model to continue one branch, send:

```text
one root zettel
+ the recursive forage prompt
+ any source/resource needed by its TEST or CITATION TRAIL
```

That is enough to continue locally without importing the whole research field.

---

## How to introduce SLIPCASE to another researcher

Use this explanation before explaining the machinery:

> Research done with AI often disappears twice: first when the context window dies, and again when a summary replaces the actual unresolved work. SLIPCASE keeps the atomic research objects, the sources that support them, and the questions they still expose. FORAGE grows those objects recursively. The graph helps choose what matters next. A checkpoint freezes the field into plain files so somebody else can inspect, criticize, merge, or continue it without the original chat.

Then show them three things, in this order:

1. one root card;
2. `000__OPEN_EDGES.txt` or the graph;
3. `index.html`.

Do not begin with the whole schema. The system becomes obvious once they see that a card can generate a child and that the child still has the same shape.

---

## What SLIPCASE is not

It is not a claim that plain text solves preservation.

It is not a claim that graph centrality discovers truth.

It is not an autonomous scientist.

It is not a database that must remain available for the archive to make sense.

It is not a paper generator whose notes exist merely to feed the manuscript.

And it is not a promise of completeness. The package reports source coverage, extraction, relation resolution, bibliography, reconstruction, PDF, and ZIP integrity separately because those are different claims.

---

## The important epistemic boundary

The system uses two kinds of authority.

**Interpretive authority** may decide that a passage creates a useful distinction, that two cards collide, or that a particular source is the strongest next lead.

**Deterministic authority** counts files, hashes payloads, extracts literal links, verifies manifests, checks citekeys, and validates the ZIP.

A script can count the wrong category perfectly, so deterministic does not mean true. It means the assertion has been established by the appropriate mechanism.

The practical rule is:

> The model judges; the tool counts.

---

## Provenance: support is not production

SLIPCASE keeps an important distinction that ordinary citation practice often misses in AI-assisted work.

A prompt may have **caused** a claim to be produced without **supporting** that claim.

So two traces matter:

```text
EVIDENCE TRACE
claim -> zettel -> source -> citekey

PRODUCTION TRACE
artifact -> operation -> prompt / model / human intervention
```

The first tells a reader why a statement is warranted. The second tells them how the artifact came to exist. Do not substitute one for the other.

---

## Merging checkpoints

When two checkpoints meet:

1. compare exact payload hashes;
2. preserve every appearance of an identical payload;
3. do not merge merely because titles, original IDs, citekeys, or filenames match;
4. retain collisions and ambiguities visibly;
5. recompute links and ghosts after the merge;
6. treat the old papers as historical interpretations, never as evidence.

Human-readable IDs are useful addresses. Exact payload hashes are the stronger machine identity when available.

---

## Rebuilding

See `000__REBUILD.txt` and `_SLIPCASE/MANIFEST.json`.

The designed failure test is destructive: remove the reader, graph, paper, MOCs, and other derived views. If the preserved cards, resources, prompts, provenance, and relation receipts are still enough to recreate useful views, the checkpoint has done its job.

---

## This checkpoint

This package is an introductory checkpoint assembled on 2026-08-18 from the SLIPCASE / recursive-forage system material and the twenty `Z-SLIP-*` research objects produced in the current working thread.

The paper in this package is **Research That Can Continue: Recursive Objects, Typed Absence, and the Checkpoint as a Scholarly Form**. It argues that the distinctive object here is not the note, graph, or paper but a research state engineered to remain *continuable* after the original software and conversation disappear.

The most useful next questions are in `000__OPEN_EDGES.txt`.
