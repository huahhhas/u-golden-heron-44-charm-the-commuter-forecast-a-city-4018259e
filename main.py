#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast, at most 140 characters, for a city
that does not exist, to $OUTPUT_DIR/entry.txt (default /output), with no
trailing newline. Then self-verifies the written file.

Stdlib only.
"""

import hashlib
import os
import sys

LINE = (
    "Cloudy in Wobbleford this morning, 14°C, drizzle by lunch — "
    "but the sun has pencilled in ten minutes just for your coffee break."
)

MAX_CHARS = 140


def main() -> int:
    if not (1 <= len(LINE) <= MAX_CHARS):
        print(f"line is {len(LINE)} chars, outside 1..{MAX_CHARS}", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("line is only whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    data = LINE.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)

    # Self-verification: read back and check every gate condition.
    with open(path, "rb") as fh:
        raw = fh.read()
    text = raw.decode("utf-8")  # raises if not valid UTF-8
    assert text == LINE, "written text does not match the line"
    assert raw == data, "written bytes are not byte-identical"
    assert 1 <= len(text) <= MAX_CHARS, "length outside gate"
    assert text.strip(), "text is only whitespace"
    assert not text.endswith("\n"), "trailing newline present"

    print(f"wrote {path}: {len(text)} chars, {len(raw)} bytes")
    print(f"sha256: {hashlib.sha256(raw).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
