from __future__ import annotations

import os
from pathlib import Path
from typing import Mapping


def ensure_pages(pages: Mapping[str, str], pages_dir: os.PathLike[str]) -> None:
    """Ensure a module exists for each slug in ``pages``."""
    dir_path = Path(pages_dir)
    dir_path.mkdir(parents=True, exist_ok=True)

    for slug in pages.values():
        file_path = dir_path / f"{slug}.py"
        if not file_path.exists():
            file_path.write_text(
                "# Auto-generated placeholder\n"
                "import streamlit as st\n\n"
                f"def main():\n    st.info('Placeholder page: {slug}')\n"
            )

