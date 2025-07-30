# STRICTLY A SOCIAL MEDIA PLATFORM
# Intellectual Property & Artistic Inspiration
# Legal & Ethical Safeguards
"""Utility helpers for managing Streamlit page modules."""

from __future__ import annotations

from pathlib import Path
import logging
import streamlit as st
from disclaimers import (
    STRICTLY_SOCIAL_MEDIA,
    INTELLECTUAL_PROPERTY_ARTISTIC_INSPIRATION,
    LEGAL_ETHICAL_SAFEGUARDS,
)

logger = logging.getLogger(__name__)
logger.propagate = False



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

    # Detect case-insensitive duplicates that may cause issues on some
    # filesystems (e.g. "Foo.py" vs "foo.py").
    existing_files: dict[str, Path] = {}
    for path in pages_dir.glob("*.py"):
        lower = path.name.lower()
        if lower in existing_files:
            logger.warning(
                "Duplicate page modules detected: %s and %s",
                existing_files[lower].name,
                path.name,
            )
        else:
            existing_files[lower] = path

    for slug in pages.values():
        slug_lower = slug.lower()
        file_path = pages_dir / f"{slug_lower}.py"
        if not file_path.exists():
            file_path.write_text(
                f"# {STRICTLY_SOCIAL_MEDIA}\n"
                f"# {INTELLECTUAL_PROPERTY_ARTISTIC_INSPIRATION}\n"
                f"# {LEGAL_ETHICAL_SAFEGUARDS}\n"
                "import streamlit as st\n\n"
                "def main() -> None:\n"
                "    st.write('Placeholder')\n"
            )
            logger.info("Created placeholder page module %s", file_path.name)

def get_pages_dir() -> Path:
    """Return the canonical directory for Streamlit page modules."""
    return Path(__file__).resolve().parents[2] / "pages"


__all__ = ["ensure_pages", "get_pages_dir"]

