"""Write one joke about working beside AI coding agents to entry.txt.

Output contract: the file entry.txt is written to the directory in the
MAKEFUN_OUTPUT_DIR environment variable (default /output), encoded as UTF-8,
1 to 280 characters, not only white space, with no trailing newline.
"""
import os
import sys

JOKE = (
    "I asked my AI coding agent to write a joke about AI coding agents. "
    "It generated 47 options, ranked them by confidence, and picked the funniest. "
    "I didn't laugh. "
    "It marked the task \"successfully completed\" and opened a pull request to fix my sense of humor."
)


def main():
    if not (1 <= len(JOKE) <= 280) or not JOKE.strip():
        print("invalid joke length", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
