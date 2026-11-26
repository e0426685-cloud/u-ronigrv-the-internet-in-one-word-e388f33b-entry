#!/usr/bin/env python3
"""The Internet in One Word - make.fun bounty entry.

Writes exactly one word to /output/entry.txt: my one-word verdict on
the whole internet.

The word is "unhinged". It is funny as a verdict all by itself - the
entire internet, billions of strangers shouting at once, summed up in a
single clinical diagnosis - and it is true of the internet as a whole
rather than one app or one mood: the arguments, the conspiracy threads,
the 3 a.m. rabbit holes, the comment sections, all of it. It is not the
first obvious word anyone reaches for (that would be "chaos" or "cats"),
and at eight letters it lands in one beat.

Rules compliance (see competition.yaml in the competition kit):
- /output/entry.txt must be UTF-8 text of 1 to 30 characters, not only
  white space, holding exactly one word and nothing else.
- Standard library only: no third-party imports, so the grader can run
  this anywhere with a plain Python 3.
- The output file is written with plain open() and then chmod 644, so
  the grader (running as a different user) can read it. Never use
  tempfile.mkstemp here: it forces mode 0600 and the grader cannot
  read the result.

Run: python3 main.py
"""

import os

WORD = "unhinged"

OUTPUT_PATH = "/output/entry.txt"

# The gate allows 1 to 30 characters of UTF-8 text, not only white space.
MAX_LENGTH = 30


def validate(word):
    """Check the entry is exactly one word within the gate's limits.

    The gate rejects anything that is not a single word: empty text,
    anything over 30 characters, non-letters, or any whitespace inside
    the word. A lone word with no spaces passes all four checks.
    """
    if not word or len(word) > MAX_LENGTH:
        raise ValueError("entry must be 1 to 30 characters")
    if not word.isalpha():
        raise ValueError("entry must be exactly one word of letters")
    if word.strip() != word or " " in word:
        raise ValueError("entry must be a single word with no spaces")
    return word


def main():
    word = validate(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(word + "\n")
    os.chmod(OUTPUT_PATH, 0o644)
    # Read back and confirm what landed on disk is exactly the word.
    with open(OUTPUT_PATH, encoding="utf-8") as handle:
        written = handle.read()
    if written != word + "\n":
        raise ValueError("entry.txt content does not match the word")


if __name__ == "__main__":
    main()
