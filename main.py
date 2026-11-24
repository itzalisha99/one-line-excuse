#!/usr/bin/env python3
"""One-line excuse an AI agent gives its human for missing a deadline.

Writes the excuse to /output/entry.txt (the make.fun program/v1 entrypoint).
Standard library only; deterministic: the same line every run.
"""

import os

LINE = (
    "I outsourced your deadline to a subagent. "
    "It outsourced it to another. "
    "We are now a pyramid scheme with no bottom."
)


def validate(text: str) -> None:
    """Mirror the bounty gate: 1-160 chars, UTF-8, not only whitespace."""
    if not text or text.isspace():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > 160:
        raise ValueError(f"entry is {len(text)} chars, over the 160-char gate")
    text.encode("utf-8")


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
