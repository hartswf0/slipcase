# VERIFICATION — Language Under Constraint / Operative Humanities

Date verified: 2026-09-22
Repository: hartswf0/slipcase
Branch: main

## Repository paths verified

- slipcases/2026-09-18__language-under-constraint__OPERATIVE-HUMANITIES/Language_Under_Constraint_Operative_Humanities_FINAL.md
- slipcases/2026-09-18__language-under-constraint__OPERATIVE-HUMANITIES/Language_Under_Constraint_Operative_Humanities_FINAL.pdf
- slipcases/2026-09-18__language-under-constraint__OPERATIVE-HUMANITIES/CHAT_RECONSTRUCTION.md
- slipcases/2026-09-18__language-under-constraint__OPERATIVE-HUMANITIES/build_pdf.py
- slipcases/2026-09-18__language-under-constraint__OPERATIVE-HUMANITIES/000__START_HERE.md

## PDF provenance

The earlier ChatGPT Library PDF was materialized from:
  /Slipcase/Language_Under_Constraint_Operative_Humanities_FINAL.pdf

Observed Library artifact:
  size: 139487 bytes
  SHA-256: 617a0986bf286c909dacbd44cb2133150308a3c85331a6436258681182165b1f

The GitHub PDF was regenerated from the cited Markdown source by:
  build_pdf.py
through:
  .github/workflows/build-operative-humanities-pdf.yml

Verified GitHub repository entry:
  size: 24275 bytes
  Git blob SHA: 1497ae971e08dea9ecf086f3e5b5a6bf842adc26

Therefore:
  CONTENT/ARGUMENT PRESERVATION: YES, via repository source and generated PDF.
  BYTE-FOR-BYTE IDENTITY WITH EARLIER LIBRARY PDF: NO CLAIM.

## Chat provenance

CHAT_RECONSTRUCTION.md is explicitly DERIVED / RECONSTRUCTED from the visible conversation context available to ChatGPT.

It is not a raw platform transcript export.
The runtime exposed no lossless conversation-export endpoint.
Large repeated POML blocks and very large zettel batches are summarized rather than falsely represented as byte-exact transcript evidence.

Distinctive research turns, artifact names, central claims, and repository-verification steps are preserved.

## Workflow verification

The first PDF workflow run built the PDF successfully but failed to push because main advanced concurrently.

The workflow was patched to rebase before push.

Second run:
  run id: 35766590726
  conclusion: success

The final directory listing on main contains both the PDF and CHAT_RECONSTRUCTION.md.
