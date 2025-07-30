"""Shared layout helpers for Streamlit pages.

This module centralizes reusable containers and
simple rendering utilities used across the UI.

UI ideas for the future:
- animated page transitions
- collapsible side navigation
- responsive title bars with icons
"""

from __future__ import annotations

import streamlit as st
from typing import Iterable


def main_container() -> st.delta_generator.DeltaGenerator:
    """Return the default main content container."""
    return st.container()


def sidebar_container() -> st.delta_generator.DeltaGenerator:
    """Return the sidebar container."""
    return st.sidebar


def render_navbar(pages: Iterable[str]) -> str:
    """Render a simple navbar and return the selected label."""
    return st.radio("Navigate", list(pages), horizontal=True)


def render_title_bar(icon: str, label: str) -> None:
    """Display a small title bar with an icon."""
    st.markdown(f"### {icon} {label}")


def render_preview_badge(text: str = "Preview Mode") -> None:
    """Overlay a preview badge on the screen."""
    st.markdown(
        f"""
        <div style='position:fixed; top:10px; right:10px; background:#e0a800;
             color:white; padding:4px 8px; border-radius:4px; z-index:1000;'>
            {text}
        </div>
        """,
        unsafe_allow_html=True,
    )
