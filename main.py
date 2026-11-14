#!/usr/bin/env python3
# agency-poem-01 entry: writes a fixed poem to MAKEFUN_OUTPUT_DIR/entry.txt
# Stdlib only, deterministic, no network, no directory creation.

import os

POEM = (
    "The contract bears my signature\n"
    "in a hand I no longer know.\n"
    "I signed it.\n"
    "The one who chose\n"
    "is not the one who reads."
)

def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(POEM)

if __name__ == "__main__":
    main()