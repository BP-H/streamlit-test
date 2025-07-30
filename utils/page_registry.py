# STRICTLY A SOCIAL MEDIA PLATFORM
# Intellectual Property & Artistic Inspiration
# Legal & Ethical Safeguards
"""Utility helpers for managing Streamlit page modules."""

from __future__ import annotations

from pathlib import Path
import os
import streamlit as st

# Root directory of the repository
ROOT_DIR = Path(__file__).resolve().parents[1]
# Default location for Streamlit page modules
PAGES_DIR = ROOT_DIR / "transcendental_resonance_frontend" / "pages"


def ensure_pages(pages: dict[str, str], pages_dir: Path) -> None:
    """Ensure placeholder page modules exist for each slug.

    Parameters
    ----------
    pages:
        Mapping of display labels to page slugs.
    pages_dir:
        Directory where page modules are stored.
    """
    pages_dir.mkdir(parents=True, exist_ok=True)

    for slug in pages.values():
        file_path = pages_dir / f"{slug}.py"
        if not file_path.exists():
            file_path.write_text(
                "import streamlit as st\n\n"
                "def main():\n"
                "    st.write('Placeholder')\n"
            )
            if hasattr(st, "warning"):
                st.warning(f"Created placeholder page: {file_path.name}")
            else:  # pragma: no cover - tests use simple objects
                print(f"Created placeholder page: {file_path.name}")


def discover_pages(pages_dir: Path | None = None) -> dict[str, str]:
    """Return a mapping of page labels to slugs discovered in ``pages_dir``."""
    if pages_dir is None:
        pages_dir = PAGES_DIR

    found: dict[str, str] = {}
    if pages_dir.exists():
        for f in pages_dir.glob("*.py"):
            slug = f.stem
            label = slug.replace("_", " ").title()
            found[label] = slug
    return found


__all__ = ["ROOT_DIR", "PAGES_DIR", "ensure_pages", "discover_pages"]
