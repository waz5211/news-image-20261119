#!/usr/bin/env python3
"""Entrypoint for news-image-20261119 (Python 3 standard library only).

Copies the entry.png beside this file to the output directory:
``$MAKEFUN_OUTPUT_DIR/entry.png`` (default ``/output/entry.png``).
Deterministic: a plain file copy, no timestamps or randomness.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, DST)
print(f"copied {SRC} -> {DST}")
