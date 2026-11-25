#!/usr/bin/env python3
"""Write the tech-support entry line to $MAKEFUN_OUTPUT_DIR/entry.txt.

The entry is one single line, written with no trailing newline.
Standard library only, no network, fully deterministic.
"""

import os
import sys

ENTRY = "Good news: I turned it off and on again. Bad news: it preferred off."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    data = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    # Guard: what is on disk must be exactly the entry, nothing else.
    written = open(path, "rb").read()
    if written != data:
        print("mismatch between entry and written bytes", file=sys.stderr)
        return 1
    if len(written) != len(data):
        print("file size does not match entry size", file=sys.stderr)
        return 1
    text = written.decode("utf-8")  # raises if not valid UTF-8
    if text.strip() == "":
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if b"\n" in written or b"\r" in written:
        print("entry must be a single line with no newline", file=sys.stderr)
        return 1
    if not 1 <= len(written.decode("utf-8")) <= 199:
        print("entry must be 1 to 199 characters", file=sys.stderr)
        return 1

    print(f"Wrote {path} ({len(written)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
