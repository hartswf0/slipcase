ZETTEL

ID:
RETENTION-005-N-A

TITLE:
Prompt expansion is not a compiler in the ordinary semantics-preserving sense because it deliberately invents values for unspecified variables.

SOURCE:
Siddhartha Datta, Alexander Ku, Deepak Ramachandran, and Peter Anderson — “Prompt Expansion for Adaptive Text-to-Image Generation” — ACL 2024.

PASSAGE:
[PARAPHRASE]
Prompt Expansion takes a user query and generates expanded prompts optimized for appealing and diverse images, sampling aspects the user left uncommitted.

RESEARCH OBJECT:
AUTOMATIC PROMPT REWRITING CAN ADD CONTENT RATHER THAN MERELY TRANSLATE CONTENT.

LOCAL MOVE:
The compiler analogy breaks because the intermediary can choose values for unspecified artistic variables.

SOURCE TERMS:
prompt expansion
uncommitted aspects
diversity
aesthetic quality
user query
expanded prompt

WHAT BECAME STRANGE:
The effective prompt can contain commitments neither literal nor uniquely entailed by user input.

QUESTION:
Who or what is responsible for expressive commitments introduced during automatic prompt expansion?

DEEPER QUESTION:
At what point does helpful interpretation become co-design?

MECHANISM:
q → expansion model E → p1...pn with added style/detail/composition → G → outputs.

FORMAL SHIFT:
<SOURCE DESCRIPTION> → [SEMANTIC COMPLETION] → <MORE COMMITTED DESCRIPTION>

SOURCE FORMALISM:
Expanded textual prompts optimized for quality/diversity.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
C(p_eff)=C(p_user)∪C_added, C_added≠∅.

TENSION:
The user may implicitly delegate unspecified decisions.

MISSING:
A theory of DELEGATED EXPRESSIVE DISCRETION.

BOUNDARY:
Prompt expansion should not automatically be called compilation without a semantics-preservation criterion.

CITATION TRAIL:
[[RETENTION-005-N]] → hidden prompt → Prompt Expansion → uncommitted aspects become machine commitments.

TEST:
Classify every inserted phrase as entailed, paraphrase, default, inferred, aesthetic addition, or arbitrary completion; test causal output effect.

PLATFORM:
[[class-is-not-a-path]]

LINKS:
[[RETENTION-005-N]]
[[prompt-expansion]]
[[semantic-completion]]
[[delegated-discretion]]

BIBTEX:
NONE
