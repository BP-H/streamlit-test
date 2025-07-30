# STRICTLY A SOCIAL MEDIA PLATFORM
# Intellectual Property & Artistic Inspiration
# Legal & Ethical Safeguards
"""Modern UI helpers for Streamlit pages."""

import streamlit as st


def inject_premium_styles() -> None:
    """Inject global CSS for modern look and feel."""
    st.markdown(
        """
        <style>
        :root {
            --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            --color-primary: #4a90e2;
            --color-accent: #5ba0f2;
            --radius-base: 12px;
            --shadow-base: 0 4px 15px rgba(74, 144, 226, 0.4);
        }
        html, body, p, span, div {
            font-family: var(--font-sans) !important;
            line-height: 1.6 !important;
        }
        .main .block-container {
            padding-top: 2rem;
            padding-left: 3rem;
            padding-right: 3rem;
            max-width: 1200px;
        }
        h1, h2, h3, h4, h5, h6 {
            font-family: var(--font-sans) !important;
            font-weight: 600 !important;
            line-height: 1.3 !important;
            margin-bottom: 1rem !important;
        }
        .stButton > button {
            background: linear-gradient(135deg, var(--color-primary) 0%, var(--color-accent) 100%) !important;
            border: none !important;
            border-radius: var(--radius-base) !important;
            color: white !important;
            font-weight: 600 !important;
            padding: 0.75rem 2rem !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            box-shadow: var(--shadow-base) !important;
            font-size: 0.95rem !important;
            height: auto !important;
        }
        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 25px rgba(74, 144, 226, 0.6) !important;
            background: linear-gradient(135deg, var(--color-accent) 0%, #6bb0ff 100%) !important;
        }
        /* Modern scrollbar styling */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        ::-webkit-scrollbar-track {
            background: rgba(255, 255, 255, 0.05);
            border-radius: var(--radius-base);
        }
        ::-webkit-scrollbar-thumb {
            background: var(--color-primary);
            border-radius: var(--radius-base);
        }
        ::-webkit-scrollbar-thumb:hover {
            background: var(--color-accent);
        }
        /* Active navigation item styling */
        a.nav-link.active {
            background: var(--color-primary) !important;
            color: #fff !important;
            border-radius: var(--radius-base) !important;
            box-shadow: var(--shadow-base) !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


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
                        <h1 style="margin: 0; color: #ffffff; font-size: 2rem; font-weight: 700; font-family: var(--font-sans);">
                            superNova_2177
                        </h1>
                        <p style="margin: 0; color: #888; font-size: 0.9rem;">Validation Analyzer</p>
                    </div>
                </div>
                <div style="display: flex; gap: 1.5rem; align-items: center;">
                    <nav style="display: flex; gap: 1rem;">
                        <a class="nav-link active" href="#" style="text-decoration:none; padding:0.25rem 0.5rem; color:#fff;">Home</a>
                        <a class="nav-link" href="#" style="text-decoration:none; padding:0.25rem 0.5rem; color:#bbb;">Stats</a>
                    </nav>
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


def render_stats_section() -> None:
    """Display quick stats in four columns."""
    col1, col2, col3, col4 = st.columns(4)
    stats = [
        ("🏃‍♂️", "Runs", "0", "#4a90e2"),
        ("📝", "Proposals", "12", "#10b981"),
        ("⚡", "Success Rate", "94%", "#f59e0b"),
        ("🎯", "Accuracy", "98.2%", "#8b5cf6"),
    ]
    for col, (icon, label, value, color) in zip([col1, col2, col3, col4], stats):
        with col:
            st.markdown(
                f"""
                <div style="
                    background: rgba(255, 255, 255, 0.03);
                    backdrop-filter: blur(15px);
                    border: 1px solid rgba(255, 255, 255, 0.1);
                    border-radius: 12px;
                    padding: 1.5rem;
                    text-align: center;
                    transition: all 0.3s ease;
                " onmouseover="this.style.transform='scale(1.02)'"
                   onmouseout="this.style.transform='scale(1)'">
                    <div style="font-size: 2rem; margin-bottom: 0.5rem;">{icon}</div>
                    <div style="color: {color}; font-size: 1.75rem; font-weight: 700; margin-bottom: 0.25rem;">
                        {value}
                    </div>
                    <div style="color: #888; font-size: 0.85rem; font-weight: 500;">
                        {label}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def open_card_container() -> None:
    """Start a card container for custom content."""
    render_validation_card()


def close_card_container() -> None:
    """Close the validation card container div."""
    st.markdown("</div>", unsafe_allow_html=True)


__all__ = [
    "inject_premium_styles",
    "render_modern_header",
    "render_validation_card",
    "render_stats_section",
    "open_card_container",
    "close_card_container",
]
