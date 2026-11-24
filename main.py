"""Write one bizarre-but-real startup pitch to /output/entry.txt.

The pitch is a single sentence (134 characters): it names the odd thing
being sold (grief counseling for people dumped by their AI chatbot), who
pays (the dumped), and why it holds together (heartbreak is heartbreak
even when the ex was a language model). Deterministic: same bytes every run.
"""

import os

PITCH = (
    "We sell grief counseling to people dumped by their AI chatbot, "
    "because heartbreak is heartbreak even when the ex was a language model."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
