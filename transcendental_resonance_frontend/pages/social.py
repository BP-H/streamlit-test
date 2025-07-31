# STRICTLY A SOCIAL MEDIA PLATFORM
# Intellectual Property & Artistic Inspiration
# Legal & Ethical Safeguards
"""Friends & Followers page."""

import streamlit as st
from frontend.light_theme import inject_light_theme
from modern_ui import inject_modern_styles
from social_tabs import render_social_tab
from streamlit_helpers import safe_container, render_mock_feed, theme_selector
from feed_renderer import render_feed
from frontend.ui_layout import render_top_bar

inject_light_theme()
inject_modern_styles()


def main(main_container=None) -> None:
    """Render the social page content within ``main_container``."""
    if main_container is None:
        main_container = st
    render_top_bar(key_prefix=st.session_state.get("active_page", ""))
    theme_selector("Theme", key_suffix="social")

    container_ctx = safe_container(main_container)
    with container_ctx:
        render_social_tab()
        st.divider()
        render_mock_feed()
        render_feed()


def render() -> None:
    """Wrapper to keep page loading consistent."""
    main()
