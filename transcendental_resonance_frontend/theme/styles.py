"""Reusable CSS snippets for Transcendental Resonance frontend."""

from __future__ import annotations

import streamlit as st

# Styles for the horizontal story carousel and post layout
STORY_CSS = """
<style>
.story-strip{display:flex;overflow-x:auto;gap:0.5rem;padding:0.5rem;margin-bottom:1rem;}
.story-item{flex:0 0 auto;text-align:center;font-size:0.8rem;color:var(--text-muted);}
.story-item img{border-radius:50%;border:2px solid var(--accent);}
.post-card{background:var(--card);padding:0.5rem 0;border-radius:12px;margin-bottom:1rem;box-shadow:0 1px 2px rgba(0,0,0,0.05);}
.post-header{display:flex;align-items:center;gap:0.5rem;padding:0 0.5rem;margin-bottom:0.5rem;}
.post-header img{border-radius:50%;width:40px;height:40px;}
.post-caption{padding:0.25rem 0.5rem;}
</style>
"""

# Styles for Font Awesome based reactions
REACTION_CSS = """
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
<style>
.reaction-btn{background:transparent;border:none;font-size:1.1rem;cursor:pointer;margin-right:0.25rem;transition:transform 0.1s ease;}
.reaction-btn:active{transform:scale(1.2);}
</style>
"""

def inject_feed_styles() -> None:
    """Inject story and reaction styles once per session."""
    if st.session_state.get("_feed_styles_injected"):
        return
    st.markdown(STORY_CSS + REACTION_CSS, unsafe_allow_html=True)
    st.session_state["_feed_styles_injected"] = True
