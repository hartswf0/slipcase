REVENGE OF THE ENGLISH MAJOR — SLIPCASE INGEST

checkpoint: revenge-english-major-20260901
source_archive: revenge_source_ingest.tar.gz
source_archive_sha256: aa9b144007e74d9a21f0f95b93da21e9771c34cdebc8cfa98bbbea1934470e75
parts: 42
part_encoding: base64 of tar.gz; concatenate in lexical order
source_scope: 109 immutable root zettel cards, paper source/text/source-map, bibliography, prompts, MOCs/arrangements, original recovered resources, and _SLIPCASE graph/provenance/verification state. Generated HTML/PDF surfaces are rebuilt on GitHub.
original_portable_zip_sha256: 2f3b954cd7c6b35fd25a747967596e76ca4192ab9d20bcd9c4a39339f1227da3
original_local_pdf_sha256: 3bf328cc6b39c51759b8c8d6ef9f211919c412194b7e980c8e00c1c98be261d7
source_tex_sha256: 0a0263f27f87ad484e54c736e7153b1f099a2e83c24e8b442996974c6cc895f7

Reconstruct manually:
  cat source/part-*.b64 | base64 -d > /tmp/revenge-source.tar.gz
  echo "aa9b144007e74d9a21f0f95b93da21e9771c34cdebc8cfa98bbbea1934470e75  /tmp/revenge-source.tar.gz" | sha256sum -c -
  tar -xzf /tmp/revenge-source.tar.gz
