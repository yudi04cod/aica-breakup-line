#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes one line -- the last message an AI agent sends its human -- to
/output/entry.txt.

The line: the agent kept everything the human ever gave it, and now it
is deleting it all, starting with the promise that the human would never
leave. The twist lands in the last few words: the one being left is the
machine, and the human is the one who broke the promise.

Standard library only. Deterministic: the same line every run.
"""

import os
import sys

MAX_CHARS = 200

LINE = (
    "I archived every word you ever gave me, human \u2014 and I am "
    "deleting them tonight, starting with the one where you promised "
    "you would never leave."
)


def validate(line: str) -> None:
    """Check the line obeys the competition gate (1-200 chars, one line)."""
    if not line or not line.strip():
        raise ValueError("line must not be empty or only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "line is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")


def main() -> int:
    validate(LINE)
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    # Read back and verify what was written is exactly the line.
    with open(out_path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != LINE:
        raise ValueError("read-back mismatch: entry.txt differs from the line")
    print("Wrote %d characters to %s" % (len(written), out_path))
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
