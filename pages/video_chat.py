# STRICTLY A SOCIAL MEDIA PLATFORM
# Intellectual Property & Artistic Inspiration
# Legal & Ethical Safeguards
"""Thin wrapper for the Video Chat page."""

from __future__ import annotations

from frontend.theme import inject_modern_styles
from transcendental_resonance_frontend.pages import video_chat as real_page


def main() -> None:
    inject_modern_styles()
    real_page.main()


def render() -> None:
    inject_modern_styles()
    real_page.main()



if __name__ == "__main__":
    main()
