ZETTEL

ID:
SON-IEC-005-B

TITLE:
AN IMAGE CAN HAVE ANCESTORS IT DOES NOT RESEMBLE: Picbreeder turns creativity from authorship into genealogy.

SOURCE:
Jimmy Secretan, Nicholas Beato, David B. D’Ambrosio, Adelein Rodriguez, Adam Campbell & Kenneth O. Stanley — “Picbreeder: Evolving Pictures Collaboratively Online” — CHI 2008, pp. 1759–1768.
SOURCE URL: https://doi.org/10.1145/1357054.1357328
AUTHOR REPOSITORY RECORD: https://stars.library.ucf.edu/scopus2000/9481/

PASSAGE:
[QUOTE]
Picbreeder gives users “the ability to continue evolving others’ images.”

RESEARCH OBJECT:
COLLABORATIVE PHYLOGENY replaces the isolated creative artifact with an ancestral tree.

LOCAL MOVE:
[[SON-IEC-005-A]] made the stepping stone more important than resemblance to a target.

Picbreeder makes the stepping stone social.

A user does not merely continue their own optimization sequence.

They can publish an intermediate form that another person recognizes as interesting, branches, mutates, and carries somewhere the original discoverer never imagined.

The creative unit therefore expands from:

PROMPT
or
IMAGE

to:

BRANCHABLE LINEAGE.

SOURCE TERMS:
collaboratively evolve
selection
generation
branching
publish
community
NEAT
interactive evolutionary computation

WHAT BECAME STRANGE:
A creator can produce an indispensable part of an eventual artifact without:

imagining the artifact
recognizing the artifact
working toward the artifact
or ever seeing the artifact.

The contribution is not a piece of the final picture.

It is a position in possibility-space from which another search becomes possible.

This creates a form of authorship in which ancestry matters even when resemblance disappears.

QUESTION:
What would prompt culture look like if prompts and generations were treated as branchable phylogenies rather than isolated works or secret recipes?

DEEPER QUESTION:
Can a creative contribution consist primarily in discovering a stepping stone whose significance is visible only through descendants created by strangers?

MECHANISM:
Picbreeder users:

encounter an image
→ select it
→ evolve variants
→ select among descendants
→ publish a promising result

Another user can then:

discover published result
→ branch from it
→ continue a new evolutionary lineage

The archive therefore stores not merely finished images but points from which future search can resume.

FORMAL SHIFT:
FROM:

AUTHOR
→ ARTIFACT

TO:

USER_A
→ artifact_a
→ USER_B branches
→ artifact_b
→ USER_C branches
→ artifact_c
→ ...

The resulting artifact has a phylogeny rather than a single creative trajectory.

SOURCE FORMALISM:
[PARAPHRASE]

Picbreeder combines interactive evolutionary selection with publication and branching.

Users select appealing images to generate a new generation, publish selected images to the community, and can initiate later evolutionary sessions from images published by other users.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

ZETTEL / PROMPT / IMAGE AS NODE:

node_i = {
  artifact_i,
  ancestry_i,
  mutations_i
}

BRANCH(node_i, user_j)
→ node_k

VALUE(node_i)

cannot be measured solely from artifact_i.

A second quantity is required:

DESCENDANT_GENERATIVITY(node_i)

=
the diversity and significance of futures made reachable by branching from node_i.

TENSION:
Midjourney remix culture superficially resembles Picbreeder branching, but ordinary prompt remixing does not automatically preserve a formal genotype, mutation operator, or complete ancestry.

The deeper similarity may lie in social search rather than evolutionary computation.

Likewise, public ancestry can support collective discovery while conflicting directly with the parent paper’s treatment of prompts as trade secrets and competitive assets.

MISSING:
Complete historical branching data from early Midjourney prompt communities.

Cases where a famous style or prompt family descended from an apparently minor public generation.

Methods for distinguishing:

copying
remixing
branching
independent convergence
shared model bias

A measure of descendant generativity.

BOUNDARY:
Picbreeder was deliberately engineered as a collaborative interactive evolutionary system.

Midjourney was not.

The Picbreeder genealogy therefore supplies a technical counterexample and possible design model, not evidence of direct historical influence.

CITATION TRAIL:
[[SON-IEC-005]]
→ interactive human evaluation
→ [[SON-IEC-005-A]]
→ stepping stones may not resemble goals
→ Picbreeder
→ stepping stones become public and branchable
→ creative value migrates from final artifact to ancestral possibility

TEST:
Take a corpus with complete remix or generation ancestry.

For every node calculate:

number of descendants
maximum descendant depth
number of distinct users who branch from it
semantic distance between ancestor and descendants
quality of best descendant

Then test whether visually unimpressive or low-rated nodes sometimes exhibit high DESCENDANT_GENERATIVITY.

If so, artifact quality and evolutionary value are empirically distinct properties.

PLATFORM:
CHI / ACM

LINKS:
[[SON-IEC-005]]
[[SON-IEC-005-A]]

BIBTEX:
@inproceedings{secretan2008picbreeder,
  author = {Jimmy Secretan and Nicholas Beato and David B. D'Ambrosio and Adelein Rodriguez and Adam Campbell and Kenneth O. Stanley},
  title = {Picbreeder: Evolving Pictures Collaboratively Online},
  booktitle = {Proceedings of the SIGCHI Conference on Human Factors in Computing Systems},
  pages = {1759--1768},
  year = {2008},
  doi = {10.1145/1357054.1357328},
  url = {https://doi.org/10.1145/1357054.1357328}
}
