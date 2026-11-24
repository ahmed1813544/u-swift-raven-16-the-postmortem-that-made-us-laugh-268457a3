"""Entry program: writes one short agent-disaster story to /output/entry.txt.

Stdlib only. Deterministic: the same text on every run.
"""

import os
import sys


ENTRY = (
    "I asked the agent to rename one local variable in a helper function; "
    "it renamed it across the whole repo, including a database migration "
    "and a string in the billing email, and the deploy went out before "
    "anyone noticed the invoices now said 'undefined'."
)


def output_path():
    for name in ("OUTPUT_PATH", "MAKEFUN_OUTPUT_PATH", "ENTRY_OUTPUT"):
        value = os.environ.get(name)
        if value:
            return value
    return "/output/entry.txt"


def main():
    text = ENTRY.strip()
    if not 1 <= len(text) <= 400:
        raise SystemExit("entry must be 1 to 400 characters")
    if text.count(".") > 2:
        raise SystemExit("entry must be one or two sentences")
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
