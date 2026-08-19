ZETTEL

ID:
FORAGE-OD-031

TITLE:
ON A HOSTED API THE DESCRIPTION UNDER TEST IS NEVER ALONE, AND THE COMPETING DESCRIPTION IS THE ONE THE RESEARCHER CANNOT SEE

SOURCE:
Watson Hartsoe — PAPERS/operation-describe-label-01.md §3 "Causality: Holding the Input Constant" and §4 "Evidence: Logged State Transitions" — 2026

PASSAGE:
[QUOTE]
§3:
"Causality is proven by holding the input constant and varying only the description."

[QUOTE]
§4:
"The data is empirical, public (GitHub), or experimentally generated (LLM API logs)."

RESEARCH OBJECT:
"Holding the input constant" is not achievable on a hosted model. The researcher controls the tool schema and the user turn. The provider controls a system prefix, a tool-use policy, safety instructions, and a serving configuration — all of which are operative descriptions with higher precedence, undocumented content, and unannounced revisions.

The archive's cleanest case runs on an input the archive cannot see.

LOCAL MOVE:
The causality argument is imported from experimental design, where "hold constant" means the experimenter controls the held variables. Here the held variables are held by a third party.

SOURCE TERMS:
holding the input constant
identical prompts
identical inputs
API logs
counterfactual
baseline state

WHAT BECAME STRANGE:
The archive's political chapter asks "who controls the descriptions that route action" and answers: platform architects, developers, administrators.

Its method chapter then treats the platform's own descriptions as though they were absent. The party named as most powerful in Chapter 5 is the party assumed away in Chapter 1.

QUESTION:
What fraction of the observed route in a hosted tool-calling experiment is attributable to the provider's prefix rather than to the researcher's schema?

DEEPER QUESTION:
If the answer is unknowable, is any hosted-API experiment admissible as evidence for a claim about *which* description routed — as opposed to the weaker claim that some description did?

MECHANISM:
<PROVIDER SYSTEM PREFIX>      ← invisible, higher precedence, version-dependent
<PROVIDER TOOL-USE POLICY>    ← invisible
<RESEARCHER'S TOOL SCHEMA>    ← the variable under study
<USER TURN>                   ← controlled
→ [ALL FOUR CONCATENATED INTO ONE CONTEXT]
→ route
→ <RESEARCHER ATTRIBUTES THE ROUTE TO THE ONE SEGMENT THEY WROTE>

The prefix also occupies the primacy position in context, which is where position effects are strongest (FORAGE-OD-008). The invisible description sits in the most operative location.

FORMAL SHIFT:
<CONTEXT>
→ <FOUR-PART CONCATENATION, ONE PART OBSERVED>
→ [ATTRIBUTION TO THE OBSERVED PART]
→ <OVERSTATED SCHEMA EFFECT>

SOURCE FORMALISM:
NONE. The archive states no assumptions about the serving stack.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

  route = f(prefix_v, policy_v, schema, user)

with v a provider version the researcher does not choose and cannot pin beyond a string.

Two consequences:
1. ΔG estimated by varying `schema` is conditional on prefix_v. Report it as ΔG | v, never as ΔG.
2. Replication across v is not replication. It is a different experiment.

Remedies, in order of strength:
  (a) open-weights local models — full control of every token, at the cost of frontier capability
  (b) version pinning plus explicit reporting of v, with re-runs on each v change
  (c) prefix probing — attempt to elicit or bound the prefix's content, and report what could not be determined

Only (a) makes "hold the input constant" literally true. The archive should say so, and should say what it gives up by choosing (b).

TENSION:
READING A: the prefix is a constant within a version, so it cannot confound a within-version comparison, and the design is sound.
READING B: it cannot confound the *comparison*, but it can and does bound the *effect size* and its transportability — a schema description competing against an aggressive prefix has a smaller ceiling than one competing against a permissive one. So the measured ΔG is a property of the pair, not of the description.

Reading A is technically right about internal validity and wrong about what the archive wants to claim.

MISSING:
Any version-pinning statement in the archive. Any local open-weights arm. Any acknowledgement that the primary case's stimulus is partly unobservable.

BOUNDARY:
This does not invalidate within-version comparisons. It invalidates the presentation of their results as properties of descriptions in general.

CITATION TRAIL:
Provider documentation on system-prompt precedence and tool-use policy.
Reproducibility literature on closed-model research.
FORAGE-OD-008 (position: the prefix holds the primacy slot), FORAGE-OD-011 (the absent third party).

TEST:
Run the same schema comparison on (a) a hosted frontier model and (b) a local open-weights model of comparable size, and report both effect sizes.

If the ratio differs substantially, the hosted result is a joint property of schema and prefix, and every number in the primary case needs a version subscript.

PLATFORM:
[[the-unseen-prefix]]

LINKS:
[[FORAGE-OD-008]]
[[FORAGE-OD-011]]
[[FORAGE-OD-003]]

BIBTEX:
@unpublished{hartsoe2026diligenceanswers,
  author = {Hartsoe, Watson},
  title = {Due-Diligence Answers: Operative Description},
  note = {OPERATION DESCRIBE archive, PAPERS/operation-describe-label-01.md},
  year = {2026}
}
