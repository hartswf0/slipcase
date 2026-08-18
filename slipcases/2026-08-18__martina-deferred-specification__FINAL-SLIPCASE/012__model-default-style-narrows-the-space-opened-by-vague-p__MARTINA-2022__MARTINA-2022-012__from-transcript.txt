ZETTEL

ID:
MARTINA-2022-012

TITLE:
Model default style narrows the space opened by vague prompts

SOURCE:
Martina interview with Watson Hartsoe, October 10, 2022. Unpublished transcript.

SOURCE URL:
NONE (private local source; preserved under _RESOURCES/PINK_MJ_Interview1.wh_Martina.pages and _RESOURCES/martina_transcript.txt)

PASSAGE:
[QUOTE]
But at least you were able to spend your money on DALLE I tried. But none of my, like, none of my cards were accepted. And I don't know why. Like, I don't know, maybe they have some issue with Spanish cards or whatever. Maybe it's something that I don't know. But I wanted to but creadits and I couldn't. So this is why I was like, okay, then Midjourney is my best friend now. Which I also prefer, because I really like the style of Midjourney. But speaking of the style of Midjourney, I always feel like I always get like very similar results, even my prompts... they're not that related, but it kind of most of the time goes to a very similar style. And I think I get bored of that. I don't know if it's still like that. Because as I told you, I took a break. Like I haven't used it in a month. Maybe because of that. Because I was like it's not that great. You know,

RESEARCH OBJECT:
[OUR INFERENCE]
UNDERSPECIFICATION DOES NOT PRESERVE NEUTRAL OPENNESS.

LOCAL MOVE:
Martina likes Midjourney's style but becomes bored because unrelated prompts repeatedly drift toward similar results.

SOURCE TERMS:
"very similar results"; "similar style"; "get bored"

WHAT BECAME STRANGE:
Leaving style open can produce convergence on a platform/model aesthetic rather than wide exploration.

QUESTION:
When the user leaves a dimension unspecified, does the system preserve uncertainty or collapse it into a learned/default regularity?

DEEPER QUESTION:
Can default aesthetics silently become design decisions when users mistake system regularity for their own preference?

MECHANISM:
Omitted variable is resolved by conditional model behavior, interface settings, sampling, and training regularities rather than remaining undefined.

FORMAL SHIFT:
OMISSION != OPEN POSSIBILITY; omission can invoke DEFAULT DISTRIBUTION.

SOURCE FORMALISM:
[PARAPHRASE]
Martina reports similar style across prompts that she considered unrelated.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]
If style not specified: output style ~ P_model(style | remaining prompt, defaults), not uniform freedom.

TENSION:
Observed similarity may reflect Martina's own recurring wording or selective memory as well as the model.

MISSING:
Controlled prompting across users and prompt families.

BOUNDARY:
The interview does not identify the technical source of similarity.

CITATION TRAIL:
Transcript 12:18 -> boredom with default style -> omission as non-neutral -> test model priors.

TEST:
Hold semantic content constant and vary only style specification; quantify visual clustering and compare across users, seeds, and model versions.

PLATFORM:
Midjourney; default aesthetic; model prior

LINKS:
[[MARTINA-2022-008]]
[[MARTINA-2022-016]]

BIBTEX:
@misc{martina2022midjourney,
  author = {Martina},
  title = {Interview on the Midjourney AI Art Community},
  howpublished = {Unpublished interview with Watson Hartsoe},
  year = {2022},
  note = {Interview conducted October 10, 2022}
}
