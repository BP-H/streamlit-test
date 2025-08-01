"""Fallback Validation page for when the real module is unavailable."""

import streamlit as st


def render() -> None:
    """Render a very small placeholder validation page."""
    st.header("Validation")
    st.info("Validation module is not installed.")


def main() -> None:
    """Entry point used by Streamlit."""
    render()


if __name__ == "__main__":  # pragma: no cover - manual invocation
    main()
