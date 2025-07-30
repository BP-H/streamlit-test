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


def safe_apply_theme(theme: str) -> None:
    """Apply theme with error handling."""
    try:
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
                .stApp {
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
                .stApp {
                    background-color: var(--background);
                    color: var(--text-color);
                    font-family: var(--font-family);
                }
                </style>
            """
        st.markdown(css, unsafe_allow_html=True)
    except Exception as e:
        st.warning(f"Theme application failed: {e}")


def apply_theme(theme: str) -> None:
    """Apply theme with fallback."""
    safe_apply_theme(theme)


def inject_global_styles() -> None:
    """Inject custom CSS styling for containers, cards and buttons."""
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Poppins:wght@400;600&display=swap');
        body, .stApp {
            background-color: var(--background, #F0F2F6);
            color: var(--text-color, #333333);
            font-family: var(--font-family, 'Poppins', sans-serif);
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
        h1, h2, h3, h4, h5, h6 {
            font-weight: 600;
            margin: 0 0 0.5rem 0;
        }
        p {
            line-height: 1.6;
            margin-bottom: 0.75rem;
        }
        .stButton>button {
            border-radius: 6px;
            background: linear-gradient(90deg, var(--primary-color, #0A84FF), #2F70FF);
            color: var(--text-color, #FFFFFF);
            transition: background 0.3s ease-in-out, transform 0.2s ease-in-out;
            padding: 0.4rem 1rem;
            font-weight: 600;
            border: none;
        }
        .stButton>button:hover {
            transform: scale(1.02);
            filter: brightness(1.1);
        }
        a {
            transition: color 0.2s ease-in-out;
        }
        a:hover {
            color: var(--primary-color, #0A84FF);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def theme_selector(label: str = "Theme", *, key_suffix: str | None = None) -> str:
    """Modern theme selector with visual toggle.

    Parameters
    ----------
    label
        Visible label for the selectbox.
    key_suffix
        Optional unique suffix appended to the widget key. If omitted, "default"
        will be used. The key format becomes ``"theme_selector_{key_suffix}_{id(st)}"``.
    """

    if key_suffix is None:
        key_suffix = "default"

    if "theme" not in st.session_state:
        st.session_state["theme"] = "dark"

    unique_key = f"theme_selector_{key_suffix}_{id(st)}"

    try:
        col1, col2 = st.columns([4, 1])
        with col2:
            current_theme = st.session_state.get("theme", "dark")

            theme_choice = st.selectbox(
                label,
                ["Light", "Dark", "Codex"],
                index=1 if current_theme == "dark" else (2 if current_theme == "codex" else 0),
                key=unique_key,
            )

            st.session_state["theme"] = theme_choice.lower()

        apply_theme(st.session_state["theme"])
        return st.session_state["theme"]
    except Exception as e:
        st.warning(f"Theme selector error: {e}")
        return "dark"


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
