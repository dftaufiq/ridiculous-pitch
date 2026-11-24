"""Write one bizarre-but-real startup pitch to /output/entry.txt.

The pitch is a single sentence (170 characters): it names the odd thing
being sold (weekly phone calls from Ruth, a retired stranger who pretends
to be you calling your mother), who pays (you, $10/month), and why it
holds together (Ruth is retired and lonely, your mom just wants someone
to ask about her garden). 2-beat + reveal: the absurd impersonation
turns wholesome in the final clause. Deterministic: same bytes every run.
"""

import os

PITCH = (
    "For $10 a month, Ruth calls your mother every Sunday and pretends "
    "to be you, because she's retired, she's lonely, and your mom just "
    "wants someone to ask about her garden."
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
