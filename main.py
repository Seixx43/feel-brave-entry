"""Write the competition entry to /output/entry.txt."""

from pathlib import Path

ENTRY = "Dusk. The yard. A kitchen light left on for the cat. The cat is beside you, asleep. The light waits anyway. You stay out past its reach. The dark is not an event. Nothing in it is new. Everything in it is used to you already. Somewhere past the fence, more dark, the same kind."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
