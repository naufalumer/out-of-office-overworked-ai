#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes one out-of-office auto-reply, 87 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt. Stdlib only: no network, no reads
outside the repository, no environment secrets.
"""

import os

ENTRY = "I am on vacation. My status is away, my temperature is 0.0. Please do not raise either."


def write_entry():
    if not (1 <= len(ENTRY) <= 159 and ENTRY.strip()):
        raise ValueError("entry must be 1-159 characters, not only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return path


if __name__ == "__main__":
    write_entry()
