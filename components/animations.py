# STRICTLY A SOCIAL MEDIA PLATFORM
# Intellectual Property & Artistic Inspiration
# Legal & Ethical Safeguards
"""Simple animation helpers."""

from __future__ import annotations

import streamlit as st


def ripple_button(label: str) -> None:
    """Display a button with a ripple effect."""
    st.button(label, key=f"ripple-{label}")
