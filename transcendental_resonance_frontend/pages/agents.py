import streamlit as st

try:
    from agent_ui import render_agent_insights_tab
except Exception:  # pragma: no cover - optional dependency
    render_agent_insights_tab = None  # type: ignore


def main(main_container=None) -> None:
    """Display available agent tools or fallback stub."""
    if main_container is None:
        main_container = st

    try:
        st.title("🤖 Agents")
        if render_agent_insights_tab is not None:
            render_agent_insights_tab(main_container=main_container)
        else:
            st.warning("Agent logic coming soon...")
    except Exception as e:  # pragma: no cover - UI
        st.error(f"Agent page error: {e}")
        if st.button("Reset", key="agent_reset"):
            st.rerun()


def render() -> None:
    """Wrapper to keep page loading consistent."""
    main()


if __name__ == "__main__":
    main()
