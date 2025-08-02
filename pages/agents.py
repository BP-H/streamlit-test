# STRICTLY A SOCIAL MEDIA PLATFORM
# Intellectual Property & Artistic Inspiration
# Legal & Ethical Safeguards
"""Thin wrapper for the Agents page."""

from frontend.theme import inject_modern_styles
from transcendental_resonance_frontend.pages import agents as real_page


def main() -> None:  # Streamlit runs this when the file is opened
    inject_modern_styles()
    real_page.main()


def render() -> None:  # keep legacy compatibility
    inject_modern_styles()
    real_page.main()


if __name__ == "__main__":  # manual execution

    main()
