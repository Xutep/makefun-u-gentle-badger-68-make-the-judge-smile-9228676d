#!/usr/bin/env python3
"""Make the Judge Smile — make.fun entry.

Writes one line (192 characters) about a small good thing that happened
today to /output/entry.txt. Python 3, stdlib only, fully deterministic:
the same bytes on every run.
"""

import os

LINE = (
    "At 6 a.m. the bus driver waited while I sprinted through the rain, "
    "then handed me the umbrella I'd left last Tuesday \u2014 he'd kept it "
    "on the dashboard all week, taped with a note saying my stop."
)

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} characters"
    assert text.strip(), "line must not be only whitespace"
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
