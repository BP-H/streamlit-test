# STRICTLY A SOCIAL MEDIA PLATFORM
# Intellectual Property & Artistic Inspiration
# Legal & Ethical Safeguards
"""Validation analysis page."""

import streamlit as st
from ui import render_validation_ui


def main(main_container=None) -> None:
    """Render the validation UI within ``main_container``."""
    if main_container is None or main_container is st:
        # ``st`` is not a context manager, so call directly
        render_validation_ui()
    else:
        # When provided a container use it as a context manager
        with main_container:
            render_validation_ui()


def render() -> None:
    """Wrapper to keep page loading consistent."""
    main()
