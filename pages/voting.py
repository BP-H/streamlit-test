"""Fallback Voting page for when the actual module cannot be loaded."""

import streamlit as st


def render() -> None:
    """Render a minimal placeholder voting page."""
    st.header("Voting")
    st.info("Voting module is not available.")


def main() -> None:
    """Entry point for Streamlit."""
    render()


if __name__ == "__main__":  # pragma: no cover - manual invocation
    main()
