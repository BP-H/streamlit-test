# STRICTLY A SOCIAL MEDIA PLATFORM
# Intellectual Property & Artistic Inspiration
# Legal & Ethical Safeguards
"""Messages page – delegates to the reusable chat UI."""

from __future__ import annotations

import streamlit as st
from frontend.light_theme import inject_light_theme
from transcendental_resonance_frontend.ui.chat_ui import render_chat_ui

inject_light_theme()


def main(main_container=None) -> None:
    """Render the chat interface inside the given container (or the page itself)."""
    render_chat_ui(main_container)


def render() -> None:  # for multipage apps that expect a `render` symbol
    main()


if __name__ == "__main__":
    main()
