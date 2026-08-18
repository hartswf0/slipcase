ZETTEL

ID:
RETENTION-005-A

TITLE:
A prompt can itself be a copyrighted work even when the image it generates is not.

SOURCE:
U.S. Copyright Office — Copyright and Artificial Intelligence, Part 2: Copyrightability — January 2025 — §II.D, “Prompts.” The Office expressly separates the possible copyrightability of sufficiently creative prompt text from the copyright status of the resulting output.

PASSAGE:
[PARAPHRASE]
The Office records that sufficiently original prompt language may itself qualify for copyright protection while emphasizing that this does not establish authorship of what the generative system subsequently produces.

RESEARCH OBJECT:
THE PROMPT AND THE OUTPUT CAN BE TWO DIFFERENT COPYRIGHT OBJECTS.

LOCAL MOVE:
RETENTION-005 focused on human authorship entering after generation through selection, arrangement, or modification.

This source opens the opposite end of the path:

human authorship may already exist BEFORE generation inside the prompt itself.

SOURCE TERMS:
prompt
original expression
copyrightability
output
human authorship
instructions

WHAT BECAME STRANGE:
A legal system can say simultaneously:

YOU AUTHORED THESE WORDS

and:

YOU DID NOT AUTHOR WHAT THOSE WORDS CAUSED THE MACHINE TO PRODUCE.

The operative description can be protected as expression while its consequence remains outside that protection.

QUESTION:
If an artist writes a highly original prompt as a literary object, what relation—if any—should copyright recognize between the protected prompt and its generated visual consequence?

DEEPER QUESTION:
Can one inscription possess two legally separable identities:

PROMPT-AS-EXPRESSION

and

PROMPT-AS-OPERATOR?

MECHANISM:
human writes prompt p

→ p may contain copyrightable literary expression

then:

p
→ generative system M
→ output y

but copyright in p does not automatically propagate through M into y.

FORMAL SHIFT:
<PROMPT AS COPYRIGHTABLE TEXT>
→ [GENERATIVE INTERPRETATION]
→ <SEPARATE OUTPUT AUTHORSHIP QUESTION>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Split:

    P_text = literal expressive form of prompt

from:

    Φ_M(P_text)
      = behavior induced when M interprets that prompt.

Copyright may attach to:

    P_text

without attaching to:

    Φ_M(P_text)

or to a sampled:

    y ~ Φ_M(P_text).

TENSION:
A highly expressive prompt may contain elements that remain perceptible in the output, and the Office separately recognizes protection for human-authored expressive inputs that survive into a resulting work.

MISSING:
A case involving a genuinely copyrightable prompt whose distinctive literal expression is demonstrably perceptible in a generated output.

BOUNDARY:
PROMPT AUTHORSHIP and OUTPUT AUTHORSHIP must not be collapsed.

The prompt may be an authored work even where it fails as evidence of authorship over generated pixels.

CITATION TRAIL:
[[RETENTION-005]]
→ prompt as upstream intervention
→ USCO separates prompt copyright from output copyright
→ one inscription acquires two legal roles
→ investigate expression versus operation.

TEST:
Create three prompts:

A. literal original prose P₁
B. close paraphrase P₂
C. terse functional equivalent P₃.

Hold model, seed, and generation settings fixed.

Compare:

TEXTUAL COPYRIGHT SIMILARITY
versus
GENERATIVE BEHAVIORAL SIMILARITY.

If these relations diverge, prompt-expression and prompt-operation require separate analysis.

PLATFORM:
[[class-is-not-a-path]]

LINKS:
[[RETENTION-005]]
[[prompt-as-work]]
[[prompt-as-operator]]
[[expression-vs-operation]]
[[copyright]]

BIBTEX:
@techreport{USCO2025Copyrightability,
  author      = {{U.S. Copyright Office}},
  title       = {Copyright and Artificial Intelligence, Part 2: Copyrightability},
  institution = {U.S. Copyright Office},
  year        = {2025},
  month       = {January}
}
