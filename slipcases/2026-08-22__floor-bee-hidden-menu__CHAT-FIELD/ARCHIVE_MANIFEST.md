# Archive manifest

## Complete binary master archive

`SLIPCASE_CHAT_2026-08-21_22__FLOOR_BEE_HIDDEN_MENU.zip`

- SHA-256: `24762bcd5fca0216d91ba19f869ce6abe03697fc1a2e00364c73f18036e70a83`
- Integrity: `unzip -t` passed with no errors.
- Scope: papers, PDFs, DOCX sources, Markdown, zettel packages, source maps, BibTeX, user-pasted source files, reconstructed chat, preserved branch transcript, figures, prior Slipcase ZIP snapshots, manifests, and checksums.

## GitHub-optimized binary archive

`SLIPCASE_CHAT_2026-08-21_22__FLOOR_BEE_HIDDEN_MENU_REPO.zip`

- SHA-256: `776d394aaafc0a39c2c062107f78babd369f9db212d217cd11fd8e4ffa502cde`
- Integrity: `unzip -t` passed with no errors.
- Scope: 128 files, with render-verification derivatives reduced relative to the master archive.

## Semantic text archive

`hidden_menu_semantic_field.tar.xz`

- SHA-256: `9927a64568ca31cdc948fabc11959768251388c81b4f8c2f1f9669e5f08a5b2a`
- Scope: 115 text-like files (`.md`, `.txt`, `.bib`, `.json`, `.html`, `.jsonl`) from the field.

## Repository representation

The active GitHub connector can create and update UTF-8 repository files, but it does not expose a direct local-binary-file upload operation. For that reason, this repository field commits the human-readable semantic record directly: reconstructed chat lineage, the complete final paper as ordered Markdown sections, source map, and BibTeX. The complete binary master ZIP remains the canonical downloadable session artifact and is identified above by checksum.

A staging branch named `chat-field-floor-bee-hidden-menu-20260822` was used for an experimental encoded-archive transfer. It is not the canonical field and should not be treated as the completed archive. `main` is authoritative.

## Conversation fidelity

`CHAT/CHAT_RECONSTRUCTION.md` is a reconstruction of the visible research lineage, not a platform-native verbatim ChatGPT export. The binary master ZIP additionally preserves the high-fidelity imported branch transcript and user-provided pasted source files recovered from the conversation.
