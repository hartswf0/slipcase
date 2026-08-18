ZETTEL

ID:
BGS-1884-14

TITLE:
Iteration can be search without authorship when every revision merely rerolls the generator

SOURCE:
U.S. Copyright Office — Copyright and Artificial Intelligence, Part 2: Copyrightability — 2025.

PASSAGE:
[PARAPHRASE]
The Office rejects the proposition that repeated prompt revision automatically establishes authorship. Where each submission causes the system to generate another output without materially increasing human control, iteration functions like repeatedly rerolling a stochastic process; acceptance of the resulting interpretation is not the same as authorship of its expression.

RESEARCH OBJECT:
Iteration itself is not a creative unit.

The question is whether an iteration modifies the work or merely initiates another independent search through outputs.

LOCAL MOVE:
The Office separates labor-intensive iterative prompting from iterative expressive determination.

SOURCE TERMS:
revising
resubmitting
re-rolling
select
control
acceptance
interpretation
authorship

WHAT BECAME STRANGE:
A workflow can contain hundreds of intentional decisions and still fail to accumulate authorship.

The count of interventions is therefore nearly meaningless.

100 operations that repeatedly reset the generative relation may establish less authorship than one operation that directly changes a surviving expressive feature.

QUESTION:
What must persist from one iteration to the next for iteration to become construction rather than repeated audition?

DEEPER QUESTION:
Is persistence—not prompting—the hidden variable that turns generative search into making?

MECHANISM:
RESETTING ITERATION:
prompt₁ → output₁
prompt₂ → output₂
prompt₃ → output₃

Each output largely replaces the prior state.

CONSTRUCTIVE ITERATION:
state₁
→ human transformation
→ state₂
→ human transformation
→ state₃

Earlier determinations survive and constrain later states.

FORMAL SHIFT:
<ITERATIVE WORKFLOW>
→ <ASK WHAT SURVIVES>
→ [REROLL OR STATEFUL TRANSFORMATION]
→ <SEARCH OR CONSTRUCTION>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

REROLL:
S₀ --p₁→ W₁
S₀ --p₂→ W₂
S₀ --p₃→ W₃

BUILD:
W₁ --h₁→ W₂ --h₂→ W₃

Candidate authorship variable:

PERSISTENCE(
human-determined expressive state
across transformations
)

TENSION:
Modern generative interfaces increasingly support image conditioning, inpainting, masking, reference images, latent reuse, editing, compositing, and other operations that may preserve parts of prior states.

The Office’s “reroll” description may therefore describe one interface architecture rather than generative AI as a medium.

MISSING:
A doctrinal vocabulary for distinguishing stochastic resampling from stateful generative editing.

BOUNDARY:
The Office expressly makes its prompting conclusion dependent on how current generally available systems operate and allows that technological changes providing greater expressive control could change the analysis.

CITATION TRAIL:
[[BGS-1884-08]]
→ Copyright Office Part 2
→ repeated prompting as reroll
→ inspect state persistence across generative interfaces

TEST:
Record a creation session as a state-transition graph rather than a prompt transcript.

For every human operation ask:

Did the previous expressive state survive?
What exactly changed?
Could the human identify the surviving feature before the next operation?

PLATFORM:
[[Prompting Is Not the Unit]]

LINKS:
[[BGS-1884-08]]
[[Production Receipts]]
[[Stateful Authorship]]
[[Generative Search]]

BIBTEX:
@techreport{USCOAI2_2025,
  title = {Copyright and Artificial Intelligence, Part 2: Copyrightability},
  institution = {U.S. Copyright Office},
  year = {2025}
}
