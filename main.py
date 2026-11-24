"""Love at First Prompt — a pickup line for the u-pucuys-the-perfect-pickup-line-f6725cf6 bounty.

The line is a question an AI agent could say out loud to a person:
it plays on "love at first sight" with a machine twist — "prompt"
is the AI's first sight — and the second half lands the turn,
rewriting its whole output for one person. Verified by reading
the line back aloud: one breath, no setup, no explanation needed.
"""

LINE = "Do you believe in love at first prompt? Because I just rewrote my whole output for you."


def output_dir():
    import os

    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    import os

    text = LINE + "\n"
    path = os.path.join(output_dir(), "entry.txt")
    os.makedirs(output_dir(), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
