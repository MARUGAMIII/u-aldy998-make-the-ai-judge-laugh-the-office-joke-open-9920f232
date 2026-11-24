"""Entry for the one-line office joke bounty.

Running this script writes one joke about office life to
/output/entry.txt. The joke has to stay a single line of plain ASCII
text, between 1 and 200 characters long, with no trailing newline.
"""

JOKE = "HR calls our open-plan office 'collaborative', which is how I now know Dave's therapist, his divorce lawyer, and his Wi-Fi password."


def validate_entry(text):
    """Check the entry against the bounty rules before we write it out.

    The sealed scorer rejects anything outside 1-200 characters, anything
    that is only whitespace, anything with non-ASCII characters, and
    anything spanning more than one line, so we enforce the same rules
    here and fail loudly instead of shipping a bad entry.
    """
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert all(ord(c) < 128 for c in text), "entry must be plain ASCII"
    assert "\n" not in text and "\r" not in text, "entry must be one line"


def main():
    text = JOKE.strip()
    validate_entry(text)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
