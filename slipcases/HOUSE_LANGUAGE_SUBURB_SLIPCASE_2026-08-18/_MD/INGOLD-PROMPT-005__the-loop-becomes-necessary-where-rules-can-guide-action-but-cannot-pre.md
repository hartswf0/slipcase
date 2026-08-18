```text
ZETTEL

ID:
INGOLD-PROMPT-005

TITLE:
THE LOOP BECOMES NECESSARY WHERE RULES CAN GUIDE ACTION BUT CANNOT PREORDAIN WHAT THE SITUATION WILL REQUIRE.

SOURCE:
Tim Ingold — Making: Anthropology, Archaeology, Art and Architecture — 2013 — Chapter 4, “On Building a House,” pp. 54–57.

PASSAGE:
[QUOTE]
“they comprised resources for action, but did not determine it”

[PARAPHRASE]
Ingold argues that medieval builders worked with rules and carefully prescribed procedures, but these did not determine practice in every detail. Skilled action had to be fine-tuned to the exigencies of the situation.

RESEARCH OBJECT:
RULE AS RESOURCE RATHER THAN COMPLETE PROGRAM.

LOCAL MOVE:
Ingold refuses RULED versus IMPROVISED. Rules can materially structure action without being sufficient to determine it. The operative unit is RULE + SITUATION + JUDGEMENT.

SOURCE TERMS:
rules; maxims; resources for action; skill; inventiveness; experience; fine-tuned; situation; workmanship

WHAT BECAME STRANGE:
“Accepted properties become invariants” sounds like progressive movement toward a complete executable specification. Ingold introduces a possible asymptote: rules may become increasingly useful without ever becoming sufficient.

QUESTION:
Does iterative prompting asymptotically approach a complete program, or does it produce better resources for situated generation while leaving an irreducible interpretive remainder?

DEEPER QUESTION:
How could we distinguish a constraint that is incompletely formalized from one whose correct application necessarily depends on context-sensitive judgement?

MECHANISM:
Rules delimit or orient possibilities; concrete situations contain particulars not exhausted by the rule; a skilled agent interprets rule and circumstance; action is fine-tuned in execution.

FORMAL SHIFT:
<RULE AS DETERMINANT>
→ <RULE AS RESOURCE>
→ [SITUATED JUDGEMENT]
→ <ACTION FIT TO PRESENT CONDITIONS>

SOURCE FORMALISM:
Ingold, drawing on Polanyi, characterizes practical rules as maxims integrated into practical knowledge and uses Turnbull to reject exhaustive causal power attributed to codified rules and algorithms.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
Naive thick-prompt model: C₁ + C₂ + ... + Cₙ → COMPLETE SPECIFICATION. Alternative: ACTIONₜ = INTERPRET(CONSTRAINT_HISTORY, CURRENT_SITUATION, PRACTICAL_COMPETENCE). Increasing C does not necessarily make INTERPRET disappear.

TENSION:
The strongest version of deferred formalization converts ambiguity into constraints. The Ingoldian counterclaim is that successful systems may depend on acting where formal constraint ends; LLMs may supply situated interpretation after formalization remains incomplete.

MISSING:
Evidence showing whether repeated prompting actually reduces degrees of interpretive freedom; a thick prompt may accumulate constraints while the system supplies unstated judgement.

BOUNDARY:
Ingold does not argue contextual judgement is in principle uncomputable; his evidence only blocks EXPLICIT RULES EXIST therefore EXPLICIT RULES DETERMINE PRACTICE.

CITATION TRAIL:
[[THE PROMPT IS NOT THE PROGRAM]] → Ingold → Michael Polanyi → David Turnbull → Lucy Suchman → Hubert Dreyfus → constraint programming → LLM program synthesis.

TEST:
Take a mature thick prompt across deliberately altered circumstances; measure what remains invariant, requires interpretation, breaks, and needs new constraints; repeat until behavior is determined or situated judgement continues.

PLATFORM:
[[THE PROMPT IS NOT THE PROGRAM]]

LINKS:
[[THE PROMPT IS NOT THE PROGRAM]]
[[THICK PROMPTING]]
[[RULE AS RESOURCE]]

BIBTEX:
@book{ingold2013making_rules,
  author = {Ingold, Tim},
  title = {Making: Anthropology, Archaeology, Art and Architecture},
  publisher = {Routledge},
  year = {2013},
  doi = {10.4324/9780203559055}
}
```
