#!/usr/bin/env python3
"""Copy the finished front page into the grader's output folder.

The image is drawn by build_image.py and stored next to this file as
entry.png. This program does nothing clever on purpose: it copies those
bytes to $MAKEFUN_OUTPUT_DIR/entry.png so both runs agree exactly.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> int:
    source = os.path.join(HERE, "entry.png")
    with open(source, "rb") as handle:
        magic = handle.read(8)
    if magic != b"\x89PNG\r\n\x1a\n":
        print(f"error: {source} is not a PNG file", file=sys.stderr)
        return 1
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.png")
    shutil.copyfile(source, target)
    size = os.path.getsize(target)
    print(f"copied {source} -> {target} ({size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
