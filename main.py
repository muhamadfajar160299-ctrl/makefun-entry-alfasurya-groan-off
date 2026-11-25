"""One-liner entry: copy the dad joke from entry.txt to the output dir.

The joke itself lives in entry.txt next to this script. This program
only reads it, validates it is non-empty, and writes it unchanged to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os
import sys


def load_line():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "entry.txt")
    try:
        with open(path, "r", encoding="utf-8") as fh:
            text = fh.read()
    except OSError as exc:
        print("cannot read entry.txt: %s" % exc, file=sys.stderr)
        return None
    line = text.strip()
    if not line:
        print("entry.txt is empty", file=sys.stderr)
        return None
    return line


def main():
    line = load_line()
    if line is None:
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write(line)
    except OSError as exc:
        print("cannot write output: %s" % exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
