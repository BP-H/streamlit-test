# STRICTLY A SOCIAL MEDIA PLATFORM
# Intellectual Property & Artistic Inspiration
# Legal & Ethical Safeguards
"""Validation analysis page."""

import importlib
import streamlit as st
import frontend.theme
from modern_ui import apply_modern_styles


from streamlit_helpers import safe_container, theme_toggle

# --------------------------------------------------------------------
# Dynamic loader with graceful degradation
# --------------------------------------------------------------------
def _fallback_validation_ui(*_a, **_k):
    st.warning("Validation UI unavailable")

def _load_render_ui():
    """Try to import ui.render_validation_ui, else return a stub."""
    try:
        mod = importlib.import_module("ui")
        return getattr(mod, "render_validation_ui", _fallback_validation_ui)
    except Exception:  # pragma: no cover
        return _fallback_validation_ui

render_validation_ui = _load_render_ui()

# Inject modern global styles (safe when running in classic Streamlit)
frontend.theme.set_theme("light")
apply_modern_styles()


# --------------------------------------------------------------------
# Page decorator (works even if Streamlit’s multipage API absent)
# --------------------------------------------------------------------
def _page_decorator(func):
    if hasattr(st, "experimental_page"):
        return st.experimental_page("Validation")(func)
    return func

# --------------------------------------------------------------------
# Main entry point
# --------------------------------------------------------------------
@_page_decorator
def main(main_container=None) -> None:
    """Render the validation UI inside a safe container."""
    frontend.theme.apply_theme("light")
    frontend.theme.inject_global_styles()

    if main_container is None:
        main_container = st
    theme_toggle("Dark Mode", key_suffix="validation")

    global render_validation_ui
    # Reload if we initially fell back but the real module may now exist
    if render_validation_ui is _fallback_validation_ui:
        render_validation_ui = _load_render_ui()

    container_ctx = safe_container(main_container)

    try:
        with container_ctx:
            render_validation_ui(main_container=main_container)
    except AttributeError:
        # If safe_container gave an unexpected object, fall back
        render_validation_ui(main_container=main_container)

def render() -> None:
    """Alias used by other modules/pages."""
    main()
