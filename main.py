"""Midnight Fridge Roast entry.

Writes a single one-line roast, spoken by a hungry person at the door
of a smart fridge that refuses to open after midnight, to
/output/entry.txt.
"""

import os

TEXT = "You're a fridge, not a bouncer — it's 12:01, stop checking IDs like that leftover cake is in VIP."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
