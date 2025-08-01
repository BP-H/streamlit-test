# STRICTLY A SOCIAL MEDIA PLATFORM
# Intellectual Property & Artistic Inspiration
# Legal & Ethical Safeguards

import importlib
import streamlit as st


def main() -> None:
    """Render the Voting page or a simple placeholder."""
    try:
        mod = importlib.import_module(
            "transcendental_resonance_frontend.pages.voting"
        )
        mod.main()
    except Exception:
        st.info("Voting page not available.")


def render() -> None:
    """Streamlit multipage entrypoint."""
    main()


if __name__ == "__main__":  # pragma: no cover - manual execution
    main()
