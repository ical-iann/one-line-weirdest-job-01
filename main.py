"""Weirdest Job Title: Blind Judge Showdown (u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922).

Program/v1 entry: writes the single job title to /output/entry.txt
(via MAKEFUN_OUTPUT_DIR). No network, deterministic.
"""

import os

LINE = "Chief Apologizer to Pigeons Who Stole My Lunch"


def main() -> None:
    # Enforce the competition gate locally: 1-60 chars, one line, non-blank.
    assert 1 <= len(LINE) <= 60, f"line is {len(LINE)} chars, gate is 1-60"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE, "line must not start or end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
