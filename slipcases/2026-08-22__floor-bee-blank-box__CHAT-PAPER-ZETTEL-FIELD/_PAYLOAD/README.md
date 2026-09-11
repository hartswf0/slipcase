# Complete text payload

The complete text-native archive is stored in `_PAYLOAD/part-*.b64` because the connected GitHub write interface for this chat accepts UTF-8 text but does not expose binary uploads.

Concatenate the parts in lexical order, base64-decode them, and decompress the resulting `tar.xz`, or run `python UNPACK_TEXT_PAYLOAD.py` from the field root. The decoded `tar.xz` SHA-256 is:

`45ceb77a9e9220e8ab4e342eed5ee61d3ad506f65914bc43ac93d456d9ea3066`

The payload expands to the complete GitHub text field assembled locally: 90 canonical root zettels, structural Slipcase documents, raw chat inputs, five paper versions, source maps, BibTeX, and lineage material.
