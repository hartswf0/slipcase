ZETTEL

ID:
RETENTION-005-N

TITLE:
In systems that rewrite prompts internally, the user may not be the author of the operative prompt the model actually receives.

SOURCE:
U.S. Copyright Office — Copyright and Artificial Intelligence, Part 2 — January 2025 — prompt analysis.

PASSAGE:
[PARAPHRASE]
The prompt visible to the user need not be identical to the representation that directly conditions the generator. An internal layer may rewrite or expand instructions before generation.

RESEARCH OBJECT:
THERE MAY BE TWO PROMPTS.

LOCAL MOVE:
Distinguish USER PROMPT from EFFECTIVE MACHINE PROMPT.

SOURCE TERMS:
modify
rewrite
prompt
human contribution
different form
control

WHAT BECAME STRANGE:
If generation is conditioned on p_eff rather than p_user, asking whether “the prompt caused the image” leaves unanswered WHICH prompt.

QUESTION:
Who authors the operative description when a system silently expands, sanitizes, translates, or rewrites the user’s prompt?

DEEPER QUESTION:
Is artistic control reduced by hidden rewriting even if the rewritten prompt realizes the user’s intention more faithfully?

MECHANISM:
p_user → rewriter R(policy,context) → p_eff → generator G → output y.

FORMAL SHIFT:
<HUMAN PROMPT> → [HIDDEN PROMPT COMPILER] → <OPERATIVE PROMPT> → [GENERATOR] → <OUTPUT>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
h → p_user; R → p_eff; G → y. AuthoredBy(p_user)=human while AuthoredBy(p_eff)=? and causal proximity may differ.

TENSION:
Compilers transform human source code without normally destroying programmer authorship; transformation alone cannot break attribution.

MISSING:
The property distinguishing authorship-preserving compilation from interpretive rewriting that injects new expressive choices.

BOUNDARY:
Literal proximity to the executable representation is not the same as authorship, but hidden prompt transformation belongs in the causal path.

CITATION TRAIL:
[[RETENTION-005]] → prompt intervention → internal rewriting → user-facing versus effective prompt → compare interpreter with compiler.

TEST:
Expose p_user, p_rewritten, and output. Give users approval/veto over p_rewritten and test feature-level control.

PLATFORM:
[[class-is-not-a-path]]

LINKS:
[[RETENTION-005]]
[[prompt-rewriting]]
[[effective-prompt]]
[[compiler-analogy]]
[[hidden-interpreter]]

BIBTEX:
NONE
