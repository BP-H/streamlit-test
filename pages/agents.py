"""Fallback Agents page used when the full module is missing."""

import streamlit as st


def render() -> None:
    """Display a minimal placeholder for the agents page."""
    st.header("Agents")
    st.info("Agents module could not be loaded.")


def main() -> None:
    """Entry point for Streamlit."""
    render()


if __name__ == "__main__":  # pragma: no cover - manual invocation
    main()
