# STRICTLY A SOCIAL MEDIA PLATFORM
# Intellectual Property & Artistic Inspiration
# Legal & Ethical Safeguards
"""Responsive layout utilities."""

from __future__ import annotations

import streamlit as st


def center_container() -> None:
    """Wrap content in a centered container."""
    st.write("<div class='container'>", unsafe_allow_html=True)
