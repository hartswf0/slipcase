ZETTEL

ID:
HUBS-URL-001

TITLE:
Mozilla Hubs made the URL itself into a door to a 3D world.

SOURCE:
Sean White — “Enabling Social Experiences Using Mixed Reality and the Open Web” — Mozilla — 2018.

SOURCE URL:
https://blog.mozilla.org/en/mozilla/enabling-social-experiences-using-mixed-reality-and-the-open-web/

PASSAGE:
[QUOTE] “You can then share and access that room with a URL.”

RESEARCH OBJECT:
Hubs collapses a distinction that earlier virtual worlds usually preserve: the distinction between linking to information and entering a world.

The browser URL is not merely a page describing the room.

It addresses the room.

LOCAL MOVE:
Mozilla deliberately places immersive social space inside ordinary web addressing rather than behind a dedicated application, store installation, or headset platform.

SOURCE TERMS:
browser
web link
URL
room
web standards
WebVR
WebXR
desktop
mobile
Mixed Reality

WHAT BECAME STRANGE:
A hyperlink can become architectural circulation.

The web's ordinary operation:

CLICK LINK → OPEN DOCUMENT

becomes:

CLICK LINK → ENTER PLACE

QUESTION:
What changes when a URI identifies an inhabitable situation rather than a document?

DEEPER QUESTION:
Is the fundamental primitive of a browser-native metaverse not the WORLD but the ADDRESS?

MECHANISM:
<URL>
→ [RESOLVE]
→ <HUBS ROOM>
→ [RENDER ACCORDING TO AVAILABLE HARDWARE]
→ <DESKTOP | MOBILE | VR EXPERIENCE>

FORMAL SHIFT:
<WEB ADDRESS>
→ <ROOM ADDRESS>
→ [ENTER]
→ <CO-PRESENCE>

SOURCE FORMALISM:
Mozilla says Hubs uses web standards and progressively uses the hardware available to the participant.

OUR FORMALIZATION:
[OUR FORMALIZATION — NOT SOURCE SYNTAX]

URL : ADDRESS<PLACE>

GET(URL, DEVICE)
→ RENDER(ROOM_STATE, capabilities(DEVICE))

The representation changes.

The address does not.

TENSION:
Kaneva linked a 2D social site to a distinct 3D world. Hubs makes the browser itself capable of becoming the 3D world.

MISSING:
What precisely persists server-side independently of desktop, mobile, and headset renderings?

BOUNDARY:
The source establishes cross-device browser access. It does not establish that every device provides identical interaction, performance, or perceptual experience.

CITATION TRAIL:
WebVR
WebXR
A-Frame
Mozilla Hubs source
networked MUD URLs
Kaneva 2D/3D architecture

TEST:
Enter the same Hubs room URL from desktop, mobile, and VR.

Record:

ROOM ID
AVATAR ID
OBJECT STATE
MEDIA STATE
POSITION
PERMISSIONS
AVAILABLE ACTIONS

Separate what survives representation change from what changes with the client.

PLATFORM:
[[The world is not its rendering]]

LINKS:
[[KANEVA-DIM-001]]
[[KANEVA-WORLD-001]]
[[Addresses become architecture]]

BIBTEX:
@misc{white2018hubs,
  author = {White, Sean},
  title = {Enabling Social Experiences Using Mixed Reality and the Open Web},
  year = {2018},
  publisher = {Mozilla},
  url = {https://blog.mozilla.org/en/mozilla/enabling-social-experiences-using-mixed-reality-and-the-open-web/}
}