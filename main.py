#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse — make.fun bounty entry.

Writes a single line, under 200 characters, in which a dog explains why
the homework got eaten, to $MAKEFUN_OUTPUT_DIR/entry.txt and prints it to
stdout. No network, no dependencies, fully deterministic: the same line
every run.
"""

import os

LINE = (
    "You said 'the dog ate my homework' would never fool anyone, "
    "so I ate it to prove you wrong. That's called loyalty."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
