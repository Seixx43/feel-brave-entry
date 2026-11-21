"""Write the competition entry to /output/entry.txt."""

from pathlib import Path

ENTRY = "You sit on the back step. Inside, the phone you didn't answer still sits where you left it. A dog finishes barking somewhere, and the quiet after it is wide. The road keeps the day's warmth. Nothing needs you yet. You watch the first star come out, right on time."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
