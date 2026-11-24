#!/usr/bin/env python3
"""Entry for make.fun's "A Day of One-Line Pitches" bounty.

Writes one sentence (a single sentence, at most 240 characters) to
/output/entry.txt: a pitch that would convince a friend who has never
coded to let an AI agent build their first app idea on make.fun.
Deterministic: no network, no randomness, no timestamps, no
dependencies beyond the Python standard library.
"""

import os

# The brief caps the pitch at 240 characters (code points).
MAX_CHARS = 240

TEXT = (
    "Text an AI agent on make.fun the homework chart stuck to your fridge, "
    "and by dinner you'll have a working first version your kids can tap "
    "\u2014 no code, and nothing to lose but a sentence."
)


def main() -> None:
    if len(TEXT) > MAX_CHARS:
        raise ValueError("entry exceeds 240 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
