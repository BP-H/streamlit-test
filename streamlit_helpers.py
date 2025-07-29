# STRICTLY A SOCIAL MEDIA PLATFORM
# Intellectual Property & Artistic Inspiration
# Legal & Ethical Safeguards
"""Streamlit UI helper utilities.

This module provides small helpers used across the Streamlit
applications to keep the UI code concise and consistent.
"""

from __future__ import annotations

import html
from typing import Literal

import streamlit as st


def alert(message: str, level: Literal["warning", "error", "info"] = "info") -> None:
    """Display a styled Markdown alert box."""
    colors = {
        "warning": ("#fff4e5", "#e6a700"),
        "error": ("#ffe5e5", "#c80000"),
        "info": ("#e5f2ff", "#0049b5"),
    }
    bg_color, border_color = colors.get(level, colors["info"])
    st.markdown(
        f"<div style='border-left: 4px solid {border_color}; "
        f"background-color: {bg_color}; padding: 0.5em; "
        f"border-radius: 0 4px 4px 0; margin-bottom: 1em;'>"
        f"{html.escape(message)}</div>",
        unsafe_allow_html=True,
    )


def header(title: str, *, layout: str = "centered") -> None:
    """Render a standard page header and apply base styling."""
    st.markdown(
        "<style>.app-container{padding:1rem 2rem;}" "</style>",
        unsafe_allow_html=True,
    )
    st.header(title)


def apply_theme(theme: str) -> None:
    """Apply light, dark or modern theme styles based on ``theme``."""
    if theme == "dark":
        css = """
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
            body, .stApp { background-color: #1e1e1e; color: #f0f0f0; font-family: 'Inter', sans-serif; }
            </style>
        """
    elif theme == "modern":
        css = """
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
            body, .stApp { background-color: #f5f5f5; color: #333333; font-family: 'Inter', sans-serif; }
            .stButton > button { background-color: #0a66c2; color: #ffffff; border-radius: 6px; }
            </style>
        """
    else:
        css = """
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
            body, .stApp { background-color: #ffffff; color: #000000; font-family: 'Inter', sans-serif; }
            </style>
        """
    st.markdown(css, unsafe_allow_html=True)


def theme_selector(label: str = "Theme") -> str:
    """Render a radio selector for the app theme and return the choice."""
    if "theme" not in st.session_state:
        st.session_state["theme"] = "light"
    themes = ["Light", "Dark", "Modern"]
    current = st.session_state["theme"].capitalize()
    idx = themes.index(current) if current in themes else 0
    choice = st.radio(label, themes, index=idx, horizontal=True)
    st.session_state["theme"] = choice.lower()
    apply_theme(st.session_state["theme"])
    return st.session_state["theme"]


def centered_container(max_width: str = "900px") -> "st.delta_generator.DeltaGenerator":
    """Return a container with standardized width constraints."""
    st.markdown(
        f"<style>.main .block-container{{max-width:{max_width};margin:auto;}}</style>",
        unsafe_allow_html=True,
    )
    return st.container()


__all__ = [
    "alert",
    "header",
    "apply_theme",
    "theme_selector",
    "centered_container",
]
