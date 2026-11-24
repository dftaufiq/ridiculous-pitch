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
    # Guard the entry contract: the pitch must be one non-empty sentence
    # within the 200-character limit the bounty brief implies. Fail loudly
    # before writing anything so a bad pitch never reaches /output.
    if not 1 <= len(PITCH) <= 200:
        raise ValueError(
            f"PITCH must be 1-200 characters, got {len(PITCH)}"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
