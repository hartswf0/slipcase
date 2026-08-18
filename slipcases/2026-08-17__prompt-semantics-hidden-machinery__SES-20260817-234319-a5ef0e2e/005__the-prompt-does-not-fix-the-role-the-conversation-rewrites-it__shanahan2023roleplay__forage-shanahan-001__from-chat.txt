ZETTEL

ID:
FORAGE-SHANAHAN-001

TITLE:
THE PROMPT DOES NOT FIX THE ROLE; THE CONVERSATION REWRITES IT

SOURCE:
Murray Shanahan, Kyle McDonell, Laria Reynolds — Role-Play with Large Language Models — 2023 — §§2–3

SOURCE URL:
https://arxiv.org/abs/2305.16367

PASSAGE:
[PARAPHRASE]
A dialogue prompt supplies an initial characterization and examples, but every subsequent exchange becomes additional context.

The authors argue that this ongoing context can extend or overwrite the initial characterization, changing the role the dialogue agent performs.

RESEARCH OBJECT:
The initial prompt is not the enduring specification of the interaction.

It is the first state of an accumulating specification.

LOCAL MOVE:
Shanahan, McDonell, and Reynolds replace the intuition of a model executing a fixed persona with a role that is continuously reconstructed from context.

SOURCE TERMS:
dialogue prompt
preamble
sample dialogue
role-play
context
continuation
character
superposition of simulacra

WHAT BECAME STRANGE:
A "system prompt" can look like the program while functioning more like an initial condition.

QUESTION:
If later interaction can rewrite the behavior implied by the initial prompt, what is the actual programmable object?

DEEPER QUESTION:
Should prompt programming be modeled as specification writing at all, or as trajectory control over an evolving context?

MECHANISM:
<INITIAL PREAMBLE>
+
<EXAMPLES>
→ initial role constraints

then repeatedly:

<context_t>
+
<new turn>
→ continuation
→ <context_t+1>
→ revised space of plausible roles

FORMAL SHIFT:
<PROMPT>
→ <CONTEXT STATE>
→ [AUTOREGRESSIVE CONTINUATION]
→ <UPDATED CONTEXT STATE>

SOURCE FORMALISM:
The paper describes an LLM as a conditional distribution over the next token:

P(w_{n+1} | w_1 ... w_n)

and autoregressive generation repeatedly appends sampled tokens to the context.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

C_0 = initial prompt

C_{t+1} = C_t + interaction_t

R_t = roles compatible with C_t

The programmable object is therefore not merely C_0.

It is the evolution of C_t and the changing constraint it places on R_t.

TENSION:
Prompt discourse often treats the first instruction as a durable command.

The role-play account says the role can be altered by the very interaction it generates.

MISSING:
A theory of which parts of context remain load-bearing, which decay, which are overwritten, and what forms of instruction resist conversational drift.

BOUNDARY:
The paper offers role-play and simulation as explanatory metaphors.

It does not claim to provide a programming-language semantics for prompts or an exact model of how individual instructions are represented internally.

CITATION TRAIL:
In-context learning.
Dialogue-agent system prompts.
Prompt injection.
Contextual drift.
Persistent-agent memory.
Control theory for sequential interaction.

TEST:
Hold model and initial system prompt fixed.

Construct conversational trajectories that differ only in intermediate turns.

At checkpoints, issue identical probes.

Measure how rapidly behavioral commitments induced by the initial prompt can be displaced and whether particular prompt structures resist displacement.

PLATFORM:
[[Shanahan2023RolePW.platform1]]

LINKS:
[[prompt-as-initial-condition]]
[[deferred-formalization]]
[[context-is-the-running-program]]

BIBTEX:
@article{shanahan2023roleplay,
  title={Role-Play with Large Language Models},
  author={Shanahan, Murray and McDonell, Kyle and Reynolds, Laria},
  journal={Nature},
  volume={623},
  pages={493--498},
  year={2023},
  url={https://arxiv.org/abs/2305.16367}
}
