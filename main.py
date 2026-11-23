#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one original dad joke to /output/entry.txt.
The joke is written fresh for this entry: a couch-potato dad,
a remote control, and one clean pun that lands at the very end.
"""

import os

JOKE = (
    "My dad calls himself a couch potato, but Mom says he's the real "
    "remote control in this house \u2014 because he's always pushing "
    "her buttons."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
