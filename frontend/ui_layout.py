"""UI Layout Helpers

Reusable Streamlit layout helpers and navigation components for pages.

These functions are lightweight and centralized for easy reuse across modules
without introducing heavy dependencies.

Features:
- `main_container()` – returns a generic container for page content
- `sidebar_container()` – accesses the sidebar container
- `render_navbar(pages)` – horizontal page links UI
- `render_title_bar(icon, label)` – renders a header with an icon

UI Ideas:
- Glassy navbar with icons
- Title bar with emoji label
- Preview badge overlay for unfinished pages
"""

from __future__ import annotations

from typing import Dict, Iterable, Optional
import streamlit as st

try:
    from streamlit_option_menu import option_menu
    USE_OPTION_MENU = True
except ImportError:
    USE_OPTION_MENU = False


def main_container() -> st.delta_generator.DeltaGenerator:
    """Return a container for the main content area."""
    return st.container()

    return st.container()


def sidebar_container() -> st.delta_generator.DeltaGenerator:
    """Return the sidebar container."""
    return st.sidebar


def render_navbar(
    page_links: Iterable[str] | Dict[str, str],
    icons: Optional[Iterable[str]] = None,
) -> None:
    """Render horizontal navigation links using ``st.page_link``."""
    opts = (
        list(page_links.items()) if isinstance(page_links, dict) else [(str(o), str(o)) for o in page_links]
    )
    icon_list = list(icons or [None] * len(opts))
    cols = st.columns(len(opts))
    for col, ((label, target), icon) in zip(cols, zip(opts, icon_list)):
        with col:
            st.page_link(target, label=label, icon=icon)


def render_title_bar(icon: str, label: str) -> None:
    """Display a stylized page title with icon."""
    st.markdown(
        f"<h1 style='display:flex;align-items:center;'>"
        f"<span style='margin-right:0.5rem'>{icon}</span>{label}</h1>",
        unsafe_allow_html=True,
    )


def show_preview_badge(text: str = "🚧 Preview Mode") -> None:
    """Overlay a badge used when a fallback or WIP page is shown."""
    st.markdown(
        f"<div style='position:fixed; top:1rem; right:1rem; background:#ffc107; "
        f"color:#000; padding:0.25rem 0.5rem; border-radius:4px; z-index:1000;'>"
        f"{text}</div>",
        unsafe_allow_html=True,
    )


"""\
## UI Ideas

- Glassmorphism cards for data panels
- Sidebar navigation with emoji icons
- Animated progress bars for background tasks
- Reaction badges for interactive elements
"""

__all__ = [
    "main_container",
    "sidebar_container",
    "render_navbar",
    "render_title_bar",
    "show_preview_badge",
]
