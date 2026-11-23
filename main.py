#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes a single dad joke to /output/entry.txt.
"""

import os

JOKE = "My dad calls himself a couch potato, but Mom says he's the real remote control in this house — because he's always pushing her buttons."
OUTPUT_PATH = "/output/entry.txt"


def validate_joke(text):
    """A showdown entry must be one non-blank joke of 1-200 characters."""
    if not isinstance(text, str) or not text.strip():
        raise ValueError("joke must be a non-blank string")
    if not 1 <= len(text) <= 200:
        raise ValueError("joke must be 1-200 characters, got %d" % len(text))
    return text


def write_entry(text, path):
    """Validate the joke, then write it to path."""
    checked = validate_joke(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(checked)
    return len(checked)


def main():
    written = write_entry(JOKE, OUTPUT_PATH)
    print("Wrote %d characters to %s" % (written, OUTPUT_PATH))


if __name__ == "__main__":
    main()
