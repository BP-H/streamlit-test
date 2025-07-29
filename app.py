# STRICTLY A SOCIAL MEDIA PLATFORM
# Intellectual Property & Artistic Inspiration
# Legal & Ethical Safeguards

import streamlit as st

st.set_page_config(page_title="Card Layout Demo")

st.markdown(
    """
    <style>
    body {
        background-color: #F0F2F6;
    }
    .card {
        background-color: #FFFFFF;
        padding: 1rem;
        border: 1px solid #E1E1E1;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("It Works!")

st.markdown('<div class="card">This is a card with custom styling.</div>', unsafe_allow_html=True)
