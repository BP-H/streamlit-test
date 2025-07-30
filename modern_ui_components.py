# STRICTLY A SOCIAL MEDIA PLATFORM
# Intellectual Property & Artistic Inspiration
# Legal & Ethical Safeguards
"""Reusable UI components with a modern aesthetic."""

from __future__ import annotations

import streamlit as st

from streamlit_helpers import inject_global_styles


def render_modern_layout(max_width: str = "900px") -> "st.delta_generator.DeltaGenerator":
    """Apply global styles and return a centered container without Streamlit padding."""
    inject_global_styles()
    st.markdown(
        f"""
        <style>
        .glass-card {{
            background: rgba(255,255,255,0.3);
            border-radius: 16px;
            border: 1px solid rgba(255,255,255,0.4);
            backdrop-filter: blur(14px);
            box-shadow: 0 4px 30px rgba(0,0,0,0.1);
            padding: 1rem;
            margin-bottom: 1rem;
            transition: transform 0.2s ease-in-out;
        }}
        .glass-card:hover {{ transform: translateY(-2px); }}
        .main .block-container {{
            padding-top: 0;
            padding-bottom: 0;
            padding-left: 0;
            padding-right: 0;
            max-width: {max_width};
            margin: auto;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
    return st.container()


def render_modern_header(title: str) -> None:
    """Display a premium gradient header with subtle blur."""
    st.markdown(
        f"""
        <div class='glass-card' style="text-align:center;background:linear-gradient(90deg,rgba(255,255,255,0.4),rgba(255,255,255,0.1));backdrop-filter:blur(6px);padding:1rem 1.5rem;">
            <h2 style='margin:0'>{title}</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_modern_sidebar(pages: dict[str, str]) -> str:
    """Render a sidebar with vertical navigation and return the selected label."""
    with st.sidebar:
        st.markdown(
            """
            <style>
            .modern-nav {display:flex;flex-direction:column;gap:0.5rem;}
            .modern-nav label {padding:0.25rem 0.5rem;border-radius:6px;transition:background 0.2s;}
            .modern-nav label:hover {background:rgba(0,0,0,0.05);}
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("<div class='glass-card modern-nav'>", unsafe_allow_html=True)
        choice = st.radio("Navigate", list(pages.keys()), label_visibility="collapsed")
        st.markdown("</div>", unsafe_allow_html=True)
    return choice


def render_validation_card(entry: dict) -> None:
    """Display a single validation entry."""
    validator = entry.get("validator") or entry.get("validator_id", "N/A")
    target = entry.get("target", entry.get("subject", "N/A"))
    score = entry.get("score", "N/A")
    st.markdown(
        f"""
        <div class='glass-card'>
            <strong>{validator}</strong> → <em>{target}</em><br>
            <span>Score: {score}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_stats_section(stats: dict) -> None:
    """Show quick statistics in a styled block."""
    st.markdown(
        f"""
        <div class='glass-card'>
            <h4 style='margin-top:0'>Stats</h4>
            <div>Runs: {stats.get('runs', 0)}</div>
            <div>Proposals: {stats.get('proposals', 'N/A')}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


__all__ = [
    "render_modern_layout",
    "render_modern_header",
    "render_modern_sidebar",
    "render_validation_card",
    "render_stats_section",
]
