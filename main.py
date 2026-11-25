"""Roast Your Fridge: one line, written to /output/entry.txt.

The line roasts the fridge as a museum of long-expired sauces:
three beats (curated / raided / charging admission), one concrete
detail (sauces that expired during the Obama administration)."""

import os

LINE = (
    "My fridge is a museum of sauces that expired during the Obama "
    "administration \u2014 curated by no one, raided at 2 a.m., and still "
    "charging admission in smells."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
