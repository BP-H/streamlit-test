import streamlit as st


def main() -> None:
    try:
        from transcendental_resonance_frontend.pages.voting import main as real_main
        real_main()
    except Exception:
        st.info("Voting page placeholder")


def render() -> None:
    main()


if __name__ == "__main__":
    main()
