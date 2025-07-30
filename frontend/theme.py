# STRICTLY A SOCIAL MEDIA PLATFORM
# Intellectual Property & Artistic Inspiration
# Legal & Ethical Safeguards
"""Color theme utilities for Streamlit frontend."""

from __future__ import annotations

import os
import streamlit as st


def get_global_css(dark: bool, *, accent: str | None = None) -> str:
    """Return ``:root`` CSS variables for dark or light mode."""
    if dark:
        accent_color = accent or "#00F0FF"
        return (
            "<style>"
            ":root {"
            "--bg:#001E26;"
            "--card:#002B36;"
            f"--accent:{accent_color};"
            "--text-muted:#7e9aaa;"
            "}</style>"
        )
    accent_color = accent or "#0A84FF"
    return (
        "<style>"
        ":root {"
        "--bg:#F0F2F6;"
        "--card:#FFFFFF;"
        f"--accent:{accent_color};"
        "--text-muted:#666666;"
        "}</style>"
    )


def apply_theme(dark: bool, *, accent: str | None = None) -> None:
    """Inject theme CSS into the Streamlit app."""
    if os.getenv("DISABLE_THEME", "0") == "1":
        return
    st.markdown(get_global_css(dark, accent=accent), unsafe_allow_html=True)


__all__ = ["get_global_css", "apply_theme"]
