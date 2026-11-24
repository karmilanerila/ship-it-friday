#!/usr/bin/env python3
"""Ship It Friday entry: emit one original commit-message joke.

Writes a single line to entry.txt in MAKEFUN_OUTPUT_DIR (or the
current directory). Stdlib only, fully deterministic.
"""

import os

LINE = (
    "fix: ship it Friday 4:59pm, tests pass on my machine, "
    "prod is just a rumor, rollback plan is vibes and one prayer"
)


def main() -> None:
    # Exactly one line, no trailing newline: the brief asks for one line.
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as fh:
        fh.write(LINE.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
