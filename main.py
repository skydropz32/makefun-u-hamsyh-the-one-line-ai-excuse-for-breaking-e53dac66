#!/usr/bin/env python3
"""Write one AI excuse for breaking production to /output/entry.txt."""

import os

LINE = "The rollback failed too, so technically I broke production twice with one deploy. Efficiency."


def main():
    # Gate: the entry must be 1-180 characters of non-blank UTF-8 text.
    if not 1 <= len(LINE) <= 180 or not LINE.strip():
        raise ValueError("entry line must be 1-180 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
