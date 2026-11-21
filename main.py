"""Write the competition entry to /output/entry.txt."""

from pathlib import Path

ENTRY = "The hawk's shadow passes. The sparrow stays a long moment, then shakes, head to tail, like rain leaving a wing. Then it preens. Then it sings the same three notes as before, and the wire holds."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
