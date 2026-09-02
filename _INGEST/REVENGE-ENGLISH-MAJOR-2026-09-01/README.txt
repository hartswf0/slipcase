REVENGE OF THE ENGLISH MAJOR — SLIPCASE INGEST

checkpoint: revenge-english-major-20260901
source_archive: revenge_source_ingest.tar.xz
source_archive_sha256: 7f3e07e57d0964e8b0ec55dac07d36e5ec111bdc44072cc11aff21b39ae88400
parts: 20
part_encoding: base64 of tar.xz; concatenate source/xz-part-*.b64 in lexical order
source_scope: 109 immutable root zettel cards, paper source/text/source-map, bibliography, prompts, MOCs/arrangements, original recovered resources, and _SLIPCASE graph/provenance/verification state. Generated HTML/PDF surfaces are rebuilt on GitHub.
original_portable_zip_sha256: 2f3b954cd7c6b35fd25a747967596e76ca4192ab9d20bcd9c4a39339f1227da3
original_local_pdf_sha256: 3bf328cc6b39c51759b8c8d6ef9f211919c412194b7e980c8e00c1c98be261d7
source_tex_sha256: 0a0263f27f87ad484e54c736e7153b1f099a2e83c24e8b442996974c6cc895f7

Reconstruct manually:
  cat source/xz-part-*.b64 | base64 -d > /tmp/revenge-source.tar.xz
  echo "7f3e07e57d0964e8b0ec55dac07d36e5ec111bdc44072cc11aff21b39ae88400  /tmp/revenge-source.tar.xz" | sha256sum -c -
  tar -xJf /tmp/revenge-source.tar.xz

Note: source/part-00.b64 and source/part-01.b64 were superseded during staging by the smaller xz archive and are not used by the ingest workflow.
