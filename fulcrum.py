"""Fulcrum Landing Page Generator

This script copies the current landing page HTML (`fulcrum_landing.html`) to
`fulcrum_landing.generated.html`.

Source of truth: `fulcrum_landing.html` (the page you edit directly).
"""

from __future__ import annotations

from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    html_path = here / "fulcrum_landing.html"
    if not html_path.exists():
        raise FileNotFoundError(f"Expected {html_path} to exist.")

    out_path = here / "fulcrum_landing.generated.html"
    out_path.write_text(html_path.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"Generated: {out_path}")

if __name__ == "__main__":
    main()
