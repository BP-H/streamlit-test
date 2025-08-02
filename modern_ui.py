# STRICTLY A SOCIAL MEDIA PLATFORM
# Intellectual Property & Artistic Inspiration
# Legal & Ethical Safeguards
"""Modern UI helpers for Streamlit pages."""

import streamlit as st
import logging
from frontend import theme


logger = logging.getLogger(__name__)

try:  # pragma: no cover - optional dependency
    from streamlit_lottie import st_lottie
    HAS_LOTTIE = True
except Exception:  # pragma: no cover - graceful fallback
    st_lottie = None  # type: ignore
    HAS_LOTTIE = False


def render_lottie_animation(url: str, *, height: int = 200, fallback: str = "🚀") -> None:
    """Display a Lottie animation if available, otherwise show a fallback icon."""
    if HAS_LOTTIE and st_lottie is not None:
        st_lottie(url, height=height)
    else:
        st.markdown(f"<div style='font-size:{height // 4}px'>{fallback}</div>", unsafe_allow_html=True)


logger = logging.getLogger("modern_ui")


def render_modern_header() -> None:
    """Render the premium glassy header."""
    st.markdown(
        """
        <div style="
            background: linear-gradient(135deg, rgba(24, 24, 24, 0.95), rgba(36, 36, 36, 0.95));
            backdrop-filter: blur(20px);
            padding: 1.5rem 2rem;
            margin: -2rem -3rem 3rem -3rem;
            border-bottom: 1px solid rgba(74, 144, 226, 0.2);
            border-radius: 0 0 16px 16px;
        ">
            <div style="display: flex; align-items: center; justify-content: space-between;">
                <div style="display: flex; align-items: center; gap: 1rem;">
                    <div style="
                        background: linear-gradient(135deg, #4a90e2, #5ba0f2);
                        border-radius: 12px;
                        padding: 0.75rem;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                    ">
                        <span style="font-size: 1.5rem;">🚀</span>
                    </div>
                    <div>
                        <h1 style="margin: 0; color: #ffffff; font-size: 1.75rem; font-weight: 700;">
                            superNova_2177
                        </h1>
                        <p style="margin: 0; color: #888; font-size: 0.9rem;">Validation Analyzer</p>
                    </div>
                </div>
                <div style="display: flex; gap: 1rem; align-items: center;">
                    <div style="
                        background: rgba(74, 144, 226, 0.1);
                        border: 1px solid rgba(74, 144, 226, 0.3);
                        border-radius: 8px;
                        padding: 0.5rem 1rem;
                        color: #4a90e2;
                        font-size: 0.85rem;
                        font-weight: 500;
                    ">
                        ✓ Online
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_validation_card() -> None:
    """Render the main validation card container."""
    st.markdown(
        """
        <div style="
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            padding: 2rem;
            margin-bottom: 2rem;
            transition: all 0.3s ease;
        " onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 12px 40px rgba(0,0,0,0.3)'"
           onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none'">
    """,
        unsafe_allow_html=True,
    )

def render_stats_section(stats: dict | None = None) -> None:
    """Display quick stats using a responsive flexbox layout."""

    accent = theme.get_accent_color()

    st.markdown(
        f"""
        <style>
        .stats-container {{
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            justify-content: space-between;
        }}
        .stats-card {{
            flex: 1 1 calc(25% - 1rem);
            min-width: 120px;
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 1.5rem;
            text-align: center;
            transition: transform 0.3s ease;
        }}
        .stats-card:hover {{
            transform: scale(1.02);
        }}
        .stats-value {{
            color: {accent};
            font-size: calc(1.5rem + 0.3vw);
            font-weight: 700;
            margin-bottom: 0.25rem;
        }}
        .stats-label {{
            color: #888;
            font-size: calc(0.8rem + 0.2vw);
            font-weight: 500;
        }}
        @media (max-width: 768px) {{
            .stats-card {{
                flex: 1 1 calc(50% - 1rem);
            }}
        }}
        @media (max-width: 480px) {{
            .stats-card {{
                flex: 1 1 100%;
            }}
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    default_stats = {
        "runs": "0",
        "proposals": "12",
        "success_rate": "94%",
        "accuracy": "98.2%",
    }
    default_stats = {
        "runs": "0",
        "proposals": "12",
        "success_rate": "94%",
        "accuracy": "98.2%",
    }
    # Merge user-provided stats on top of defaults without mutating them
    data = default_stats.copy()
    if stats:
        data.update(stats)

    entries = [
        ("🏃‍♂️", "Runs", data["runs"]),
        ("📝", "Proposals", data["proposals"]),
        ("⚡", "Success Rate", data["success_rate"]),
        ("🎯", "Accuracy", data["accuracy"]),
    ]

    st.markdown("<div class='stats-container'>", unsafe_allow_html=True)
    for icon, label, value in entries:
        st.markdown(
            f"""
            <div class='stats-card'>
                <div style='font-size:2rem;margin-bottom:0.5rem;'>{icon}</div>
                <div class='stats-value'>{value}</div>
                <div class='stats-label'>{label}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)


def open_card_container() -> None:
    """Start a card container for custom content."""
    render_validation_card()


def close_card_container() -> None:
    """Close the validation card container div."""
    st.markdown("</div>", unsafe_allow_html=True)


__all__ = [
    "render_lottie_animation",
    "render_modern_header",
    "render_validation_card",
    "render_stats_section",
    "open_card_container",
    "close_card_container",
]
