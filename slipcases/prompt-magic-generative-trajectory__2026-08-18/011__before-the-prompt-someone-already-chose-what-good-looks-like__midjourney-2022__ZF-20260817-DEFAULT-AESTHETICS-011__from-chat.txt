ZETTEL

ID:
ZF-20260817-DEFAULT-AESTHETICS-011

TITLE:
Before the Prompt, Someone Already Chose What “Good” Looks Like

SOURCE:
[PRIMARY ARCHIVE] Midjourney Office Hours notes supplied by user.
SOURCE URL: local:_RESOURCES/Midjourney_prompt_magic_archive_2022.md

[AUTHORITATIVE TECHNICAL SOURCE] Midjourney, “Raw.”
https://docs.midjourney.com/hc/en-us/articles/32634113811853-Raw

PASSAGE:
[PRIMARY ARCHIVE]

“What should the aesthetics of the new version be?”

“Get a lot of data and have good defaults.”

The same section immediately raises “De-biasing of visual aesthetics.”

RESEARCH OBJECT:
Prompt theory usually begins too late.

It begins when the user types.

But before any user arrives, a model developer has already made aesthetic choices through:

training data
curation
objective functions
model architecture
fine-tuning
ranking
default parameters
safety systems
interface defaults.

The blank prompt box is therefore not aesthetically blank.

The model comes furnished.

LOCAL MOVE:
Replace:

USER PROMPT
→ MODEL
→ IMAGE

with:

DEVELOPER / DATA / TRAINING / DEFAULTS
→ AESTHETIC PRIOR
← USER PROMPT
→ IMAGE.

SOURCE TERMS:
aesthetics
good defaults
de-biasing
stylized defaults
creative touch
Raw
opinionated
model version

WHAT BECAME STRANGE:
The supposed neutrality of the empty interface disappears.

A user may believe that every visible aesthetic property of an output came either from:

THE PROMPT
or
THE DATA.

But the platform also has an aesthetic policy.

DEFAULT is an authored decision disguised as absence of decision.

QUESTION:
How much of what prompt users learn as “the model’s nature” is actually a deliberately engineered default aesthetic?

DEEPER QUESTION:
Who governs visual culture when a platform can alter the baseline aesthetic prior experienced by millions of users without changing a single word in their prompts?

MECHANISM:
DESIGNERS
→ choose training / tuning / defaults
→ produce model-level aesthetic tendencies
→ user prompts inside those tendencies
→ repeated outputs normalize those tendencies
→ practitioners adapt their vocabulary to them.

FORMAL SHIFT:
PROMPT = CREATIVE CONTROL

becomes:

PROMPT = LOCAL CONTROL
inside
PLATFORM-DEFINED AESTHETIC BOUNDARY CONDITIONS.

SOURCE FORMALISM:
[PARAPHRASE] Midjourney currently distinguishes Standard behavior, which adds model styling, from Raw behavior, which reduces that intervention.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

Let:

D = training data
θ = trained parameters
A = post-training aesthetic tuning
δ = interface defaults
p = user prompt

Then:

x ~ G(p | θ(D,A), δ)

The user controls p.

The platform controls much of:

θ
A
δ.

Therefore:

USER INTENT
operates inside
PLATFORM AESTHETIC GOVERNANCE.

TENSION:
“AI art is made by human artists” may be true while remaining radically incomplete.

There are multiple human agencies:

PROMPTER
MODEL DESIGNER
DATA CURATOR
RATER
INTERFACE DESIGNER
POLICY TEAM.

Calling only the final prompter “the human artist” can conceal upstream aesthetic decisions.

MISSING:
A method for experimentally separating:

prompt contribution
training-data association
default aesthetic
post-training preference tuning
user selection.

BOUNDARY:
Platform defaults do not determine every generated image.

They establish tendencies and priors against which user intervention operates.

CITATION TRAIL:
[[ZF-20260817-LANGUAGE-POINTS-INTO-DATA-005]]
[[ZF-20260817-PROMPT-NOT-COMMAND-004]]
→ training corpus gives language operative history
→ archive reveals explicit model-level aesthetic decision-making
→ Raw exposes default styling as removable rather than natural
→ next edge: aesthetic defaults as governance

TEST:
Take a fixed corpus of prompts.

Run them across:

1. Standard mode
2. Raw mode
3. adjacent model versions
4. identical seeds where technically supported

Have independent evaluators code recurring:

composition
lighting
beauty conventions
facial presentation
genre
color
camera position
cultural representation.

Estimate how much aesthetic variance is attributable to platform defaults without changing user language.

PLATFORM:
Midjourney
model defaults
Raw Mode
generative-image platforms

LINKS:
[[ZF-20260817-LANGUAGE-POINTS-INTO-DATA-005]]
[[ZF-20260817-PROMPT-NOT-COMMAND-004]]
[[DEFAULT-AS-GOVERNANCE]]
[[AESTHETIC-PRIOR]]
[[PLATFORM-AUTHORSHIP]]

BIBTEX:
@misc{midjourneyRawMode,
  author={{Midjourney}},
  title={Raw},
  howpublished={Midjourney Documentation},
  url={https://docs.midjourney.com/hc/en-us/articles/32634113811853-Raw}
}
