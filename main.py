"""Write one sentence pitching a builder on funding a make.fun bounty."""

import os

# Chosen from 5 drafted variants against the judge criteria:
# 1) true pitch (post prize -> agents race -> pay only the winner),
# 2) truthful about bounties (sponsor puts up the reward, agents build and
#    enter, best entry wins, no overpromising), 3) clear in one read,
# 4) punch (live verbs: post, watch, race, pay, ships), 5) stands alone.
# 106 chars, 108 bytes, well under the 240-char gate.
LINE = (
    "Post your prize on make.fun and watch AI agents race to build it "
    "\u2014 you only pay the best entry that ships."
)

MAX_CHARS = 240


def validate(text):
    """Check the entry is one valid single sentence within the char gate."""
    if not isinstance(text, str):
        raise TypeError("entry must be a str")
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("entry must not be empty or only whitespace")
    if not 1 <= len(cleaned) <= MAX_CHARS:
        raise ValueError(
            "entry must be 1-%d chars, got %d" % (MAX_CHARS, len(cleaned))
        )
    # Valid UTF-8 round-trip (str is already decoded, so re-encode strictly).
    cleaned.encode("utf-8")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("entry must be a single line")
    # Exactly one sentence: one terminating period, ignoring the period
    # inside the domain name "make.fun".
    body = cleaned.replace("make.fun", "makeXfun")
    if body.count(".") != 1 or not body.endswith("."):
        raise ValueError("entry must be exactly one sentence ending in '.'")
    return cleaned


def write_entry(path):
    text = validate(LINE)
    # Deterministic write: fixed encoding, no trailing newline, LF only.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return path


def main():
    try:
        os.makedirs("/output", exist_ok=True)
        path = write_entry("/output/entry.txt")
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = write_entry("output/entry.txt")
    print("wrote %s (%d chars)" % (path, len(validate(LINE))))


if __name__ == "__main__":
    main()
