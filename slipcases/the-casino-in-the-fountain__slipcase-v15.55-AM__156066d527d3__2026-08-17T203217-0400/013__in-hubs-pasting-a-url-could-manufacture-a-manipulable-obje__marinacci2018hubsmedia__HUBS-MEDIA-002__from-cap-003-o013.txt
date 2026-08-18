ZETTEL

ID:
HUBS-MEDIA-002

TITLE:
In Hubs, pasting a URL could manufacture a manipulable object.

SOURCE:
Josh Marinacci — “Share your favorite images and videos in VR with Mozilla Hubs” — Mozilla Hacks — 2018.

SOURCE URL:
https://hacks.mozilla.org/2018/08/share-your-favorite-images-and-videos-in-vr-with-mozilla-hubs/

PASSAGE:
[QUOTE] “Anything you share becomes a virtual object that everyone can interact with.”

RESEARCH OBJECT:
Hubs contains an unusually literal translation pipeline:

WEB ADDRESS
→ media retrieval
→ validation/cache
→ spatial object
→ embodied manipulation.

A URL does not merely summon representation onto a screen. It becomes material available to spatial action.

LOCAL MOVE:
Mozilla extends the web's embedding mechanism into object construction.

SOURCE TERMS:
URL
media
virtual object
interact
import
cached
move
throw
resize
play
pause

WHAT BECAME STRANGE:
The transformation from 2D web to 3D world is not principally a graphics transformation.

It is an affordance transformation.

A video changes from something you WATCH into something you can PICK UP.

QUESTION:
What must be added to information before it can participate as matter?

DEEPER QUESTION:
Could a metaverse compiler be understood as a function that assigns physical verbs to informational objects?

MECHANISM:
<URL>
→ [FETCH]
→ <MEDIA>
→ [VALIDATE + CACHE]
→ <ROOM OBJECT>
→ [ASSIGN SPATIAL AFFORDANCES]
→ <MOVE / THROW / RESIZE / PLAY>

FORMAL SHIFT:
<RESOURCE>
→ <REPRESENTATION>
→ [MATERIALIZE]
→ <THING>

SOURCE FORMALISM:
Mozilla documents special URL handling for images, audio, video, GLB models, Sketchfab, Giphy, Imgur, Google Poly, and YouTube.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

MATERIALIZE(url) :=
    media = resolve(url)
    safe_media = validate(media)
    obj = instantiate(safe_media)
    obj.affordances += {
        position,
        rotation,
        scale,
        grab,
        throw
    }

TENSION:
Kaneva spatialized YouTube by binding video to a virtual television.

Hubs generalizes the operation: heterogeneous web resources can themselves become movable room objects.

MISSING:
Which properties survive import?

Authorship?
Provenance?
Permalink?
Comments?
Metadata?
Licensing?
Update state?

BOUNDARY:
Hubs did not turn the whole originating webpage into a spatial object. Its server extracted or fetched supported media representations.

CITATION TRAIL:
Mozilla Hubs media resolver
GLTF
Open Graph
oEmbed
Kaneva synchronized YouTube
media-on-a-prim in Second Life

TEST:
For each supported source type, construct:

SOURCE OBJECT
→ RETAINED PROPERTIES
→ LOST PROPERTIES
→ ADDED SPATIAL PROPERTIES.

Ask whether MATERIALIZE is copying, embedding, translating, or creating a new object.

PLATFORM:
[[Information becomes matter by acquiring verbs]]

LINKS:
[[KANEVA-MEDIA-001]]
[[Affordance compilation]]
[[URL-to-object]]

BIBTEX:
@misc{marinacci2018hubsmedia,
  author = {Marinacci, Josh},
  title = {Share your favorite images and videos in VR with Mozilla Hubs},
  year = {2018},
  publisher = {Mozilla Hacks},
  url = {https://hacks.mozilla.org/2018/08/share-your-favorite-images-and-videos-in-vr-with-mozilla-hubs/}
}