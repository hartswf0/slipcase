ZETTEL

ID:
RETENTION-005-B

TITLE:
The more a prompt behaves like a program, the less copyright can monopolize the behavior it performs.

SOURCE:
17 U.S.C. § 102(b), which excludes ideas, procedures, processes, systems, and methods of operation from copyright protection. The Copyright Office report records a related warning from the Kernochan Center that extending prompt copyright across the multiplicity of outputs risks protecting a method of generating works.

PASSAGE:
[PARAPHRASE]
Copyright may protect the expressive form in which an operative procedure is written, but section 102(b) prevents that protection from becoming ownership of the procedure or method itself. The Office applies this concern specifically to attempts to extend rights in prompts across generated outputs.

RESEARCH OBJECT:
PROMPT-AS-ART and PROMPT-AS-PROGRAM PULL COPYRIGHT IN OPPOSITE DIRECTIONS.

LOCAL MOVE:
The project asks whether prompting becomes more program-like as words acquire reliable mechanical effects.

Copyright introduces an unexpected inversion:

the more important those effects become, the less the FUNCTIONAL relation itself is the sort of thing copyright protects.

SOURCE TERMS:
procedure
process
system
method of operation
prompt
expression
copyright

WHAT BECAME STRANGE:
Operativity may strengthen the case that prompting is a serious creative practice while weakening any claim that copyright in one prompt should control equivalent operative procedures.

QUESTION:
Could two prompts be legally noninfringing as texts while being operationally interchangeable inside a model?

DEEPER QUESTION:
Is the correct intellectual-property object for prompt craft:

THE SENTENCE,
THE METHOD,
THE RESULT,
THE CONTROL POLICY,
or none of these?

MECHANISM:
prompt text p
→ copyright may protect p's original expressive wording.

But:

functional behavior Φ(p)
→ may constitute a process/method
→ excluded from copyright protection as such.

FORMAL SHIFT:
<EXPRESSIVE PROMPT>
→ {
    <COPYRIGHTABLE FORM>,
    <UNPROTECTABLE FUNCTION>
  }

SOURCE FORMALISM:
Section 102(b) draws the statutory expression/function boundary.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Define behavioral equivalence under model M:

    p₁ ≈_M p₂

iff:

    Φ_M(p₁) ≈ Φ_M(p₂).

Copyright equivalence need not track:

    ≈_M.

Thus:

    textual difference
    ∧
    functional equivalence

is legally and technically coherent.

TENSION:
The fact that a prompt has functional effects does not strip copyright from its original expressive wording.

Computer programs themselves demonstrate that copyrightable expression can embody uncopyrightable methods.

MISSING:
Case law specifically applying §102(b) to prompt equivalence rather than conventional software or instructions.

BOUNDARY:
Copyright can protect HOW an operative description is expressed without protecting WHAT ITS OPERATIVE METHOD DOES.

CITATION TRAIL:
[[RETENTION-005]]
→ prompt as site of human intervention
→ prompt itself may be protected
→ §102(b)
→ functional consequences remain free
→ prompt becomes simultaneously artwork and method.

TEST:
Take one effective prompt P.

Generate twenty semantically and stylistically different paraphrases that reproduce its behavior.

Ask separately:

WHICH PARAPHRASES COPY PROTECTED EXPRESSION?

WHICH PARAPHRASES REPRODUCE THE SAME OPERATION?

The difference between those sets is the legal-operational boundary.

PLATFORM:
[[class-is-not-a-path]]

LINKS:
[[RETENTION-005]]
[[prompt-as-program]]
[[section-102b]]
[[expression-function]]
[[operative-description]]

BIBTEX:
@misc{USC17Section102,
  author = {{United States}},
  title  = {17 U.S.C. \S 102},
  year   = {1976}
}

@techreport{USCO2025Copyrightability,
  author      = {{U.S. Copyright Office}},
  title       = {Copyright and Artificial Intelligence, Part 2: Copyrightability},
  institution = {U.S. Copyright Office},
  year        = {2025}
}
