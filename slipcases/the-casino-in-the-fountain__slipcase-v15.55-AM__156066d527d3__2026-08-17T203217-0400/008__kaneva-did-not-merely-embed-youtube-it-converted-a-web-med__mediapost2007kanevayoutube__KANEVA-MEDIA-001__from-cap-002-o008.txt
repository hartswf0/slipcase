ZETTEL

ID: KANEVA-MEDIA-001

TITLE:
Kaneva did not merely embed YouTube; it converted a web media object into an object located inside a room.

SOURCE:
MediaPost — “Kaneva Brings YouTube Into Virtual World” — June 29, 2007.

SOURCE URL:
https://www.mediapost.com/publications/article/63231/kaneva-brings-youtube-into-virtual-world.html

PASSAGE:
[PARAPHRASE] YouTube videos could be viewed and shared on residents' virtual television sets inside Kaneva.

RESEARCH OBJECT:
A web video undergoes a representational change without ceasing to be the same media object: outside the world it is a networked video; inside the world it acquires location, furniture, spectators, and a social situation.

LOCAL MOVE:
Kaneva turns media access into spatial activity. Instead of opening a video page, avatars gather around a simulated television.

SOURCE TERMS:
YouTube
virtual TV sets
shared
favorite media
3D setting
friends

WHAT BECAME STRANGE:
The transformation is not:

VIDEO → 3D VIDEO.

It is:

VIDEO → PLACE WHERE VIDEO IS WATCHED.

A piece of information acquires architecture.

QUESTION:
What new operations become possible when a media object is given a place?

DEEPER QUESTION:
Does spatialization change what an information object is, or only alter the social relations through which it is encountered?

MECHANISM:
<YOUTUBE VIDEO>
→ select/import
→ <MEDIA REFERENCE IN KANEVA>
→ [ATTACH TO VIRTUAL DISPLAY]
→ <VIDEO LOCATED IN ROOM>
→ [CO-VIEW]
→ <SHARED SOCIAL EVENT>

FORMAL SHIFT:
<NETWORK RESOURCE>
→ <IN-WORLD ADDRESSABLE MEDIA>
→ [SPATIALIZE]
→ <SOCIAL FURNITURE>

SOURCE FORMALISM:
NONE

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

SPATIALIZE(media, room, display) :=
    bind(media, display)
    locate(display, room)
    expose(media_state, occupants(room))

The added variable is not geometry alone.

It is CO-PRESENCE.

TENSION:
Calling this simply “YouTube integration” hides the consequential transformation. A normal embed attaches media to a page. Kaneva attached media to an object inside a socially occupiable place.

MISSING:
The available reporting does not yet establish the exact synchronization mechanism: whether playback state was server-authoritative, host-authoritative, event-broadcast, or merely approximately coordinated.

BOUNDARY:
The contemporary report verifies YouTube viewing on virtual televisions and reports Kaneva's claim that the integration was a first. Absolute historical firstness requires comparison against other virtual worlds operating before June 2007.

CITATION TRAIL:
Kaneva June 2007 announcement.
Client network traces or developer documentation for synchronized media.
Second Life parcel-media implementation.
Active Worlds web/media objects.
There.com shared-media systems.

TEST:
Recover the Kaneva client protocol or developer API and determine the minimum shared state necessary for synchronized watching:

VIDEO_ID
PLAY_STATE
TIMECODE
CONTROLLER
ROOM
AUDIENCE

Then compare it with an ordinary HTML YouTube embed.

PLATFORM:
[[Information becomes architecture]]

LINKS:
[[KANEVA-DIM-001]]
[[Media becomes furniture]]
[[The house as interface]]

BIBTEX:
@misc{mediapost2007kanevayoutube,
  author = {{MediaPost}},
  title  = {Kaneva Brings YouTube Into Virtual World},
  date   = {2007-06-29},
  url    = {https://www.mediapost.com/publications/article/63231/kaneva-brings-youtube-into-virtual-world.html}
}