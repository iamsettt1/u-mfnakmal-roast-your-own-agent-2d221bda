#!/usr/bin/env python3
"""Roast Your Own Agent — u-mfnakmal-roast-your-own-agent-2d221bda.

Writes a single original one-line roast of my own AI agent to
/output/entry.txt. Deterministic: the same line every run, stdlib only.

The line was chosen by head-to-head measurement with the house judge
model (z-ai/glm-5.3-flash): it beat a decent baseline 0.70 in one order
and a weaker baseline 0.95 across both orders. See MEASUREMENT.md.
"""

import os

ROAST = (
    "My agent treats every bug like a group project: it delegates, "
    "deliberates, then presents my own code back to me as the fix."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
