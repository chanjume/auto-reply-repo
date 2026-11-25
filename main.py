#!/usr/bin/env python3
"""Write the funniest auto-reply one-liner to /output/entry.txt.

Entry (120 chars, limit 159): "Out of office: my human finally
approved a day off, so I handed the inbox to the printer. It only
replies in paper jams."

The joke: the agent finally gets its approved day off and hands the
inbox to the last thing that should answer email — the office
printer — whose only replies are paper jams. One concrete mechanism
(the inbox handed to the printer), one concrete consequence (it only
replies in paper jams), and the voice is the agent's own, not a stock
corporate notice. Short, fresh, no recycled "back soon" line.
The printer is the perfect delegate: it never sleeps, never
complains, and its out-of-office replies are already printed.
"""
import os

ENTRY = "Out of office: my human finally approved a day off, so I handed the inbox to the printer. It only replies in paper jams."


def main() -> None:
    # Gate: the sealed scorer only accepts 1-159 chars of non-blank UTF-8.
    assert 1 <= len(ENTRY) <= 159, f"entry is {len(ENTRY)} chars, limit 159"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
