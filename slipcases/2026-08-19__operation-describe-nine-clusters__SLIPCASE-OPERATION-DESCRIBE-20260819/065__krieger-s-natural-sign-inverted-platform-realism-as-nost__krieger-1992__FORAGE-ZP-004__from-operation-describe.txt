ZETTEL

ID: FORAGE-ZP-004

TITLE: Krieger's natural sign inverted: platform realism as "nostalgia for the natural sign"

SOURCE: Z-Port/final-draft-v4.md ("The Shield and the Natural Sign"); Z-Port/portugal-version.md ("The shield and the natural sign"); Z-Port/deep-research-report (14).md (Thick prompting bin)

PASSAGE: [QUOTE] "As Krieger put it, the verbal description would become a 'natural sign,' as a picture was assumed to be. He added: 'The narrow, literal doctrine of ekphrasis would seem to require this primitive notion of the pictorial as the naively representational.'(Krieger, 12, n12)" (final-draft-v4.md) [QUOTE] "The images have a generic or 'average' character (Hintze et al, 2026). They are in a literal sense averages, as they are interpolations from the numerical values assigned to the images on which the model was trained. Steyerl (2023) calls them 'mean' images. Meyer further notes that the images are nostalgic in a postmodern way, expressive not of a longing for the past but for a sense of pastness." (final-draft-v4.md) [QUOTE] "Generative AI produces images of images, not the natural sign. We could say that what AI shows is a nostalgia for the natural sign." (final-draft-v4.md)

RESEARCH OBJECT: An inversion of Krieger's "illusion of the natural sign": ekphrastic hope wished the word could become a naively representational picture; generative platforms appear to grant this wish (photorealistic output on demand), but what they actually deliver is a statistical average of prior pictures — "mean images" (Steyerl), "platform realism" (Meyer). The natural sign returns only as an aesthetic of pastness. Grounded by an actual experiment: prompting Gemini 3 Flash with the entire Iliad 18.478–608 in Greek ("Create the shield described below. Make the image as faithful and detailed as possible") produced a bronze shield in default painterly-photographic realism; the vineyard scene (18.561–572) alone produced "a style reminiscent of an illustrated children's book of the mid-twentieth century... an illustration of a child's version of the Bible."

LOCAL MOVE: Use Krieger's dismissal ("naive," "primitive") against itself: the naive doctrine of pictorial realism, far from dead, is the default aesthetic regime of the platforms — so the theory of the natural sign becomes empirically testable for the first time, and fails in a specific way (averageness, not naturalness).

SOURCE TERMS: natural sign; illusion of the natural sign; ekphrastic hope; platform realism (Meyer); mean images (Steyerl); postmodern nostalgia / sense of pastness; images of images

WHAT BECAME STRANGE: Realism itself — the style that claimed to be unmediated — is revealed as the most heavily mediated output class, an interpolation of museum photography, Bible illustration, and movie iconography; the model's "faithfulness" to Homer's Greek is faithfulness to our visual culture's memory of antiquity.

QUESTION: Is "nostalgia for the natural sign" a property of the models (training-data composition) or of the users (prompting for faithfulness invites realism defaults)?

DEEPER QUESTION: If the natural sign was always an illusion sustained by pictorial convention, does a system that manufactures the illusion industrially finally prove Krieger right — or does executability (the word really does produce the picture) mean the sign is now "natural" in a new, operational sense that Krieger's semiotics cannot classify?

MECHANISM: Interpolation: outputs are literal numerical averages over training images; culturally weighted associations (ancient world → children's-Bible illustration style) dominate when the prompt does not constrain style; platforms default to "a small range of popular styles depending on the subject matter."

FORMAL SHIFT: The word/image sign relation becomes a statistics problem: resemblance is replaced by expectation (the mean of a distribution), so critique shifts from semiotics to distribution analysis.

SOURCE FORMALISM: Krieger 1992, p.12 n.12 (as cited in v4); Meyer's platform-realism dimensions table in the E research file (Legibility / Plausibility / Familiarity).

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Output ≈ E[image | prompt, training distribution D, platform policy P]. "Natural sign" claim = output tracks world W; actual: output tracks D, and D tracks prior images of images of W. Nostalgia-for-natural-sign = the systematic bias of E[·] toward historically sedimented realism styles.

TENSION: READING A: the Gemini experiment shows operative ekphrasis succeeding — the model "had no trouble with the Greek" and rendered the scenes. READING B: it shows operative ekphrasis failing constitutively — what appeared was the platform's memory of illustrated antiquity, not Homer's world; success at the image level is failure at the world level. The same experiment is evidence for both.

MISSING: The figures themselves (Fig 1, Fig 2) are referenced but not present in the text corpus; the Hintze et al. 2026 citation is not in any reference list and needs verification; no draft quantifies "averageness."

BOUNDARY: Claims are about image-output aesthetics of 2024–2026 commercial platforms (OpenAI GPT Image, Midjourney, Gemini); the natural-sign analysis is not extended to world-model outputs anywhere in the drafts.

CITATION TRAIL: Krieger 1992 (Ekphrasis: The Illusion of the Natural Sign, p.12 n.12) → Mitchell 1994 (ekphrastic hope) → Meyer 2025 ("Platform Realism") → Steyerl 2023 ("mean images") → Hintze et al. 2026 (unverified) → the authors' Gemini 3 Flash test with Iliad 18.478–608 in Greek.

TEST: Replicate the experiment: prompt several models with Iliad 18.478–608 in Greek and in translation, with and without style constraints; code output styles; the "nostalgia" claim predicts convergence on a narrow band of realist/illustrational styles absent constraints.

PLATFORM: Gemini 3 Flash (documented test); OpenAI GPT Image; Midjourney (compared for detail-execution vs cinematic effects in v4).

LINKS: [[FORAGE-ZP-003]], [[FORAGE-ZP-005]], [[FORAGE-ZP-006]], [[FORAGE-ZP-007]]

BIBTEX: @book{krieger1992ekphrasis, author = {Krieger, Murray}, title = {Ekphrasis: The Illusion of the Natural Sign}, publisher = {Johns Hopkins University Press}, address = {Baltimore}, year = {1992}}
