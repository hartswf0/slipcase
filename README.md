# SLIPCASE — Portable Research Field & Prompt Operator

<p align="center">
  <img src="slipcase.png" alt="SLIPCASE: Portable Research Field" width="680"/>
</p>

<p align="center">
  <strong>Preserve &middot; Relate &middot; Return</strong><br>
  <em>A self-contained, mobile-first research console, zettel lines inspector, slipcard flipper, PDF reader, and prompt operator across 41 field slipcases.</em>
</p>

---

## Overview

**SLIPCASE** is an offline-capable, zero-dependency research desk and portable capsule designed for mobile devices and desktop environments. It unifies five core research faculties into a single fast, responsive interface (`index.html`):

1. **[LINES] Zettel Lines Inspector**: Complete atomic breakdown of all **1,552 zettel cards** into structured, selectable field rows (`QUESTION`, `DEEPER QUESTION`, `PASSAGE`, `RESEARCH OBJECT`, `LOCAL MOVE`, `MECHANISM`, `FORMAL SHIFT`, `BIBTEX`, etc.) with multi-line selection, continuous reading stack, and clipboard export.
2. **[FLIPPER] Tactile Card Deck**: Touch-swipe enabled card deck flipper with formatted/raw source toggles, core question callouts, and one-tap payload export.
3. **[PDFS] Research PDF Library & Dual Reader**: Curated library of **129 primary research PDFs** (compiled papers and source scans) with instant search, category filtering, embedded preview, and direct fullscreen tab breakouts (`&nearr;`).
4. **[MAPS] Case Inspector & Structural Field Maps**: Instant inspection of derived structural documents (`000__START_HERE.txt`, `000__MAP.txt`, `000__BIBLIOGRAPHY.txt` / `.bib`, `000__LINEAGE.txt`, `000__OPEN_EDGES.txt`, `000__MAKING_HISTORY.txt`).
5. **[PROMPTS] Prompt Operator Console**: The complete **Cool Radio** suite of 8 structured POML research instruments (`FORAGE 3.0`, `FORAGE 3.1`, `FORAGE 4.0`, `SLIPCASE 9.0`, `SLIPCASE 13.1`, `SLIPCASE 15.0`, `SLIPCASE 15.55-AM`, and `OPERATIONAL PRAGMATIST`) with one-tap copy-and-advance and `.poml` downloads.


**HEAD layer:** 41 canonical HEAD ZETTELs, one per field, mapped to all 129 PDFs in `heads-pdf-map.html` / `.json` / `.txt`.
---

## Architecture & Layout

```
+------------------------------------------------------------------------+
|                        SLIPCASE RESEARCH DESK                          |
+-----------------+------------------+-----------------+-----------------+
| [LINES]         | [FLIPPER]        | [PDFS]          | [MAPS] & PROMPT |
| Structured Rows | Tactile Card     | 129 Curated     | Structural Maps |
| Multi-Select    | Raw / Parsed     | Dual-Engine     | 8 POML Tools    |
| Stack Reader    | Touch Swipe      | Direct Open     | 41 Workspaces   |
+-----------------+------------------+-----------------+-----------------+
```

### 1. Zettel Lines Inspector
- **Field-by-Field Breakdown**: Inspect cards by atomic epistemological fields.
- **Filter Chips**: Filter by `ALL`, `QUESTIONS`, `PASSAGES`, `OBJECTS`, `MECHANISMS`, `FORMALISMS`, `TYPES`, `SOURCES`, or use the extended modal sheet for any field.
- **Multi-Line Selection**: Tap any row to select. Long-press, right-click, or tap the zettel header to select the entire card.
- **Reading Stack Sheet**: Slide-up continuous reading flow for all selected lines with one-tap clipboard copy (`&orarr;`).

### 2. Tactile Card Deck Flipper
- **Workspace Navigation**: Switch between all 41 slipcases or browse global decks.
- **Mobile Touch Swipe**: Swipe left/right on touchscreens to flip cards naturally.
- **Raw / Parsed Mode**: Toggle between typography and exact monospace `.txt` source.
- **Direct Export**: One-tap card copy or download as standalone `.txt` file.

### 3. Mobile PDF Library & Reader
- **129 Research PDFs**: Access compiled working papers, preprints, and archival scans.
- **Category Filter**: Filter between *Compiled Papers* and *Source / Archival Scans*.
- **Dual-Engine Reading**: Embedded preview modal plus direct `OPEN PDF &nearr;` links guaranteed to work in all desktop and mobile sandboxes.

### 4. Case Inspector & Structural Maps
- Inspect derived structural documents for each slipcase:
  - `000__START_HERE.txt` (Overview & checkpoint state)
  - `000__MAP.txt` (Complete textual relationship graph)
  - `000__BIBLIOGRAPHY.txt` / `.bib` (Compiled citations and citekeys)
  - `000__LINEAGE.txt` (Inquiry descent paths)
  - `000__OPEN_EDGES.txt` (Unresolved frontier questions)
  - `000__MAKING_HISTORY.txt` / `000__RETURN_PATH.txt`

### 5. Prompt Operator (Cool Radio Suite)
- **8 POML Research Instruments**:
  - `01 FORAGE 3.0` (Inquiry + Opposition &mdash; atomic zettel generation)
  - `02 FORAGE 3.1` (Recursive Inquiry &mdash; live-edge following)
  - `03 FORAGE 4.0` (Autonomous Graph Inquiry &mdash; expected epistemic gain steering)
  - `04 SLIPCASE 9.0` (The Compact Compiler &mdash; flat deck, graph, bib, reader, paper)
  - `05 SLIPCASE 13.1` (Lineage-Aware Compiler &mdash; descent laws & provenance)
  - `06 SLIPCASE 15.0` (The Ancient Master &mdash; 12 field operations)
  - `07 SLIPCASE 15.55-AM` (Portable Research Field &mdash; take-a-real-stab checkpointing)
  - `08 OPERATIONAL PRAGMATIST` (Wittgenstein Editor &mdash; control-surface overhaul)
- **One-Tap Copy & Advance**: Tap once to copy the prompt to clipboard and auto-advance to the next instrument.
- **Keyboard Shortcuts**: `ArrowLeft` / `ArrowRight` to step through instruments.

---

## 41 Included Slipcases

| # | Workspace / Case | Slips | PDFs | Field Docs |
|---|---|---:|---:|---:|
| 01 | `2026-08-17__prompt-semantics-hidden-machinery__SES-20260817-234319-a5ef0e2e` | 20 | 1 | 10 |
| 02 | `2026-08-17__slipcase__mycelium-sole-field__v15.55-AM (1)` | 16 | 3 | 11 |
| 03 | `2026-08-17__the-shop-makes-the-prompt__SLIPCASE-20260817-AIACS-01` | 46 | 11 | 11 |
| 04 | `2026-08-18__martina-deferred-specification__FINAL-SLIPCASE` | 48 | 2 | 13 |
| 05 | `2026-08-18__prompt-battles-smackdown__PB-SC-20260818-4D1C1A7BD0__slipcase` | 29 | 4 | 11 |
| 06 | `2026-08-18__what-can-you-still-reopen__16-zettels__FINAL` | 22 | 4 | 11 |
| 07 | `2026-08-18__what-kind-of-thing-is-the-model__Andrew__FULL__v15.55-AM` | 70 | 1 | 10 |
| 08 | `2026-08-19__operation-describe-nine-clusters__SLIPCASE-OPERATION-DESCRIBE-20260819` | 175 | 0 | 12 |
| 09 | `2026-08-21__when-meaning-gets-to-work__CULTUREOS-20260821-1443` | 1 | 0 | 10 |
| 10 | `2026-08-22__floor-bee-blank-box__CHAT-PAPER-ZETTEL-FIELD` | 1 | 0 | 1 |
| 11 | `2026-08-22__floor-bee-hidden-menu__CHAT-FIELD` | 2 | 1 | 0 |
| 12 | `2026-08-22__look-down-say-the-strange-thing__ALL-ZETTELS__CHAT-FIELD` | 40 | 0 | 10 |
| 13 | `2026-09-01__the-model-is-training-you__MODEL-TRAINING-YOU-2026-09-01` | 1 | 1 | 3 |
| 14 | `2026-09-01__the-prompt-is-already-disappearing__DHH-LEX__v15.55-AM` | 14 | 0 | 8 |
| 15 | `2026-09-13__chance-and-consequences__NOLAN-HOMER__SLIPCASE` | 21 | 2 | 12 |
| 16 | `2026-09-15__steering-not-specifying__PROMPTING-METIS__v15.55-AM` | 21 | 1 | 10 |
| 17 | `2026-09-18__milk-bread-eggs__SHOPPING-LIST-PARTIAL-FUTURE-STATE` | 1 | 0 | 3 |
| 18 | `FINAL_SLIPCASE__Mastery_Without_Sovereignty__ALL_ZETTELS__2026-08-18` | 39 | 4 | 12 |
| 19 | `HOUSE_LANGUAGE_SUBURB_SLIPCASE_2026-08-18` | 48 | 2 | 10 |
| 20 | `SLIPCASE_13.1__2026-08-17__the-unlived-curriculum` | 24 | 6 | 11 |
| 21 | `SLIPCASE_AFTER_SURPRISE_FINAL_2026-08-18` | 157 | 4 | 10 |
| 22 | `SLIPCASE_DEEP_LINEAGE_2026-08-18` | 121 | 13 | 10 |
| 23 | `SLIPCASE__PROMOTION_FIELD__2026-08-18__74d74484bfdd` | 30 | 1 | 10 |
| 24 | `SLIPCASE__theory-lag__20260818T030003-0400` | 32 | 2 | 14 |
| 25 | `THE_HUT__FINAL_FIELD__2026-08-18` | 2 | 1 | 1 |
| 26 | `YELMO_FINAL__all-zettels-and-paper` | 25 | 3 | 10 |
| 27 | `black-mountain-structured-openness__SCF-20260818-BMC-004__v15.55-AM__FINAL` | 28 | 3 | 10 |
| 28 | `house-language__FULL-FINAL__2026-08-18` | 39 | 4 | 12 |
| 29 | `house_language_many_mansions_2026-08-18` | 62 | 1 | 10 |
| 30 | `how_is_this_gonna_be_screwed_up_20260817` | 6 | 1 | 0 |
| 31 | `primitive_construction_slipcase_20260818` | 16 | 1 | 10 |
| 32 | `prompt-forward-slipcase-2026-08-18` | 95 | 1 | 10 |
| 33 | `prompt-magic-generative-trajectory__2026-08-18` | 27 | 1 | 10 |
| 34 | `prompt-practices__FINAL__2026-08-18` | 32 | 3 | 12 |
| 35 | `safe-relational-freedom-field__2026-08-18__a5ef0e2e` | 50 | 8 | 11 |
| 36 | `slipcase-intro__2026-08-18__082152Z` | 25 | 1 | 10 |
| 37 | `slipcase_final_20260818` | 46 | 8 | 11 |
| 38 | `slipcase_noise_of_sculptors_2026-08-17_2254` | 38 | 20 | 11 |
| 39 | `slipcase_ontology_build` | 1 | 4 | 0 |
| 40 | `the-casino-in-the-fountain__slipcase-v15.55-AM__156066d527d3__2026-08-17T203217-0400` | 38 | 2 | 10 |
| 41 | `the-prompt-keeps-disappearing__FINAL-SLIPCASE-15.55-AM__2026-08-18` | 43 | 4 | 12 |
| **Total** | **41 Field Slipcases** | **1,552 Slips** | **129 PDFs** | **373 Docs** |

---

## Getting Started

### Direct Browser Opening
Simply double-click or open `index.html` in Safari, Chrome, Firefox, or any mobile browser:
```bash
open index.html
```

### Local Web Server (Recommended for Mobile Device Testing)
To test on mobile devices over Wi-Fi:
```bash
python3 -m http.server 8000
```
Then visit `http://<your-local-ip>:8000` from your phone or tablet.

---

## Rebuilding & Compiling

To re-index slipcases or update the embedded database:
```bash
python3 build_index_html.py
```
This inspects all workspace directories, parses cards and PDFs, validates payload integrity, and outputs the single-file `index.html` and `slipcases.json`.

---

## Station ID & Public File

```
COOL RADIO · Watson Hartsoe with Claude & Gemini · Atlanta · SLIPCASE Master · 2026-08-18
```

- **Origin**: 31 research workspaces compiled under SLIPCASE 15.55-AM / Ancient Master specifications.
- **Zero External Dependencies**: Embedded dataset, vanilla CSS, vanilla JS, zero tracking, 100% offline.
