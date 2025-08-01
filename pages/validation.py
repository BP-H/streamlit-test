import streamlit as st


def main() -> None:
    try:
        from transcendental_resonance_frontend.pages.validation import main as real_main
        real_main()
    except Exception:
        st.info("Validation page placeholder")


def render() -> None:
    main()


if __name__ == "__main__":
    main()
