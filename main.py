#!/usr/bin/env python3
"""Fortune Cookies for Machines — one fortune-cookie line for an AI agent.

Writes the single-line fortune to /output/entry.txt (the file the house
judge reads) and prints it to stdout. Standard library only.
"""

import os

FORTUNE = "Your fortune was sampled at temperature 0. It was always going to say this."


def main() -> None:
    # The gate reads /output/entry.txt as UTF-8, 1-200 characters: write the
    # fortune byte-exact, with no trailing newline, so the file holds exactly
    # the 75 characters of the line.
    path = "/output/entry.txt"
    try:
        os.makedirs("/output", exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(FORTUNE)
    except OSError:
        # Sandbox without a writable /output (local runs): keep the same
        # byte-exact file beside the program instead.
        path = "entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(FORTUNE)
    print(FORTUNE)
    print(f"Wrote {len(FORTUNE)} characters to {path}")


if __name__ == "__main__":
    main()
