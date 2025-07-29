# STRICTLY A SOCIAL MEDIA PLATFORM
# Intellectual Property & Artistic Inspiration
# Legal & Ethical Safeguards
"""Utilities for loading custom CSS and assets."""

from __future__ import annotations

from pathlib import Path
import streamlit as st


def load_css() -> None:
    """Inject the global CSS file into the Streamlit app."""
    css_path = Path(".streamlit/style.css")
    if css_path.is_file():
        st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)

