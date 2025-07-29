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


def alert(
    message: str,
    level: Literal["warning", "error", "info"] = "info",
    *,
    show_icon: bool = True,
) -> None:
    """Display a minimally intrusive alert box."""
    icons = {"warning": "\u26A0", "error": "\u274C", "info": "\u2139"}
    colors = {
        "warning": ("#fff7e6", "#f0ad4e"),
        "error": ("#fdecea", "#f44336"),
        "info": ("#e8f4fd", "#1e88e5"),
    }
    bg_color, border_color = colors.get(level, colors["info"])
    icon_html = f"<span class='icon'>{icons.get(level, '')}</span>" if show_icon else ""
    st.markdown(
        f"<div class='custom-alert' style='border-left:4px solid {border_color};"
        f"background-color:{bg_color};padding:0.5em;border-radius:4px;"
        f"margin-bottom:1em;display:flex;align-items:center;gap:0.5rem;'>"
        f"{icon_html}{html.escape(message)}</div>",
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
    """Apply light or dark theme styles based on ``theme``."""
    if theme == "dark":
        css = """
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Iosevka:wght@400;700&display=swap');
            :root {
                --background: #181818;
                --secondary-bg: #242424;
                --text-color: #e8e6e3;
                --primary-color: #4a90e2;
                --font-family: 'Iosevka', monospace;
            }
            body, .stApp {
                background-color: var(--background);
                color: var(--text-color);
                font-family: var(--font-family);
            }
            a { color: var(--primary-color); }

            </style>
        """
    else:
        css = """
            <style>
            :root {
                --background: #F0F2F6;
                --secondary-bg: #FFFFFF;
                --text-color: #333333;
                --primary-color: #0A84FF;
                --font-family: 'Inter', sans-serif;
            }
            body, .stApp {
                background-color: var(--background);
                color: var(--text-color);
                font-family: var(--font-family);
            }

            </style>
        """
    st.markdown(css, unsafe_allow_html=True)


def inject_global_styles() -> None:
    """Inject custom CSS styling for containers, cards and buttons."""
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
        body, .stApp {
            background-color: var(--background, #F0F2F6);
            color: var(--text-color, #333333);
            font-family: var(--font-family, 'Inter', sans-serif);
        }
        .custom-container {
            padding: 1rem;
            border-radius: 8px;
            border: 1px solid rgba(0,0,0,0.05);
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 1rem;
            background-color: var(--secondary-bg, #FFFFFF);
        }
        .card {
            background-color: var(--secondary-bg, #FFFFFF);
            padding: 1rem;
            border: 1px solid rgba(0,0,0,0.1);
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 1rem;
        }
        .stButton>button {
            border-radius: 6px;
            background: linear-gradient(90deg, var(--primary-color, #0A84FF), #2F70FF);
            color: var(--text-color, #FFFFFF);
            transition: filter 0.2s ease-in-out;
        }
        .stButton>button:hover {
            filter: brightness(1.1);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def theme_selector(label: str = "Theme") -> str:
    """Render a theme selector and return the chosen theme."""
    if "theme" not in st.session_state:
        st.session_state["theme"] = "dark"

    options = ["Light", "Dark", "Codex"]
    current = st.session_state["theme"].capitalize()
    idx = options.index(current) if current in options else 0

    cols = st.columns([4, 1])
    with cols[0]:
        choice = st.selectbox(label, options, index=idx)

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
    "inject_global_styles",
]
