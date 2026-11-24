"""One Breath — a pickup line an AI agent could actually say out loud.

The line: an agent that simulated a million ways to say hello and,
in every single one, still chose the simplest one — walking over.
The twist is the machine's exhaustive planning landing on the most
human choice there is: no calculation, just hello.
"""

# Verified by read-back: 92 characters, one line, so line + trailing
# newline = 93 bytes — inside the 200-character gate.
LINE = "I simulated a million ways to say hello, and in every single one I still walked over to you."

import os


def output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    text = LINE
    path = os.path.join(output_dir(), "entry.txt")
    os.makedirs(output_dir(), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
