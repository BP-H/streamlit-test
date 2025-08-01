# STRICTLY A SOCIAL MEDIA PLATFORM
# Intellectual Property & Artistic Inspiration
# Legal & Ethical Safeguards
"""Utilities for rendering a simple (or custom) social feed."""

from __future__ import annotations

from typing import Iterable, Dict, Any, Tuple

import streamlit as st

import html

from streamlit_helpers import sanitize_text, sanitize_emoji, render_post_card
from modern_ui_components import shadcn_card

# --- default demo posts -------------------------------------------------------
DEMO_POSTS: list[Tuple[str, str, str]] = [
    (
        "alice",
        "https://picsum.photos/seed/alice/400/300",
        "Enjoying the sunshine!",
    ),
    (
        "bob",
        "https://picsum.photos/seed/bob/400/300",
        "Hiking adventures today.",
    ),
    (
        "carol",
        "https://picsum.photos/seed/carol/400/300",
        "Coffee time at my favourite spot.",
    ),
]

STORIES = [
    ("alice", "https://picsum.photos/seed/alice/80/80"),
    ("bob", "https://picsum.photos/seed/bob/80/80"),
    ("carol", "https://picsum.photos/seed/carol/80/80"),
]


def render_stories() -> None:
    """Display a horizontal carousel of stories."""
    if not hasattr(st, "markdown"):
        return
    st.markdown("<div class='stories-row'>", unsafe_allow_html=True)
    cols = st.columns(len(STORIES)) if hasattr(st, "columns") else [st] * len(STORIES)
    for col, (user, img) in zip(cols, STORIES):
        if hasattr(col, "image"):
            col.image(img, width=64)
        if hasattr(col, "caption"):
            col.caption(user)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <style>
        .stories-row{display:flex;gap:.5rem;overflow-x:auto;padding:.5rem 0;}
        .stories-row img{border-radius:50%;border:2px solid var(--accent);}
        </style>
        """,
        unsafe_allow_html=True,
    )


# -----------------------------------------------------------------------------


FEED_PAGE_SIZE = 3


def _render_interactive_post(entry: dict, idx: int) -> None:
    """Render a post card with like and comment controls."""
    key = f"post_{idx}"
    like_key = f"{key}_likes"
    st.session_state.setdefault(like_key, int(entry.get("likes", 0)))
    likes = st.session_state[like_key]

    render_post_card(
        {
            "image": entry.get("image"),
            "text": entry.get("text"),
            "likes": likes,
        }
    )

    cols = st.columns([1, 4]) if hasattr(st, "columns") else [st, st]
    like_col, comment_col = cols[0], cols[1]
    btn = getattr(like_col, "button", getattr(st, "button", None))
    if btn and btn("❤️", key=f"like_{key}"):
        st.session_state[like_key] += 1
        st.experimental_rerun()
    txt_input = getattr(comment_col, "text_input", getattr(st, "text_input", None))
    if txt_input:
        txt_input(
            "Add a comment",
            key=f"c_{key}",
            label_visibility="collapsed",
            placeholder="Add a comment...",
        )


def render_feed(posts: Iterable[Any] | None = None) -> None:
    """Render a simple scrolling feed of posts with infinite scroll."""

    render_stories()

    active = st.session_state.get("active_user", "guest")
    if posts is None or not list(posts):
        posts = DEMO_POSTS if active in {"guest", "demo_user"} else []
    else:
        posts = list(posts)

    if not posts:
        st.info("No posts to display")
        return

    offset = st.session_state.setdefault("feed_offset", 0)
    subset = posts[offset : offset + FEED_PAGE_SIZE]

    for idx, entry in enumerate(subset, start=offset):
        if not isinstance(entry, dict):
            user, image, caption = entry
            entry = {
                "user": sanitize_text(user),
                "image": sanitize_text(image),
                "text": sanitize_emoji(caption),
                "likes": 0,
            }
        else:
            entry = {
                "user": sanitize_text(entry.get("user") or entry.get("username", "")),
                "image": sanitize_text(entry.get("image", "")),
                "text": sanitize_emoji(entry.get("text") or entry.get("caption", "")),
                "likes": entry.get("likes", 0),
            }

        _render_interactive_post(entry, idx)

    if offset + FEED_PAGE_SIZE < len(posts):
        if st.button("Load more", key=f"more_{offset}"):
            st.session_state["feed_offset"] = offset + FEED_PAGE_SIZE
            st.experimental_rerun()


def render_mock_feed() -> None:
    """Convenience wrapper that simply calls :func:`render_feed` with demo data."""
    render_feed(DEMO_POSTS)


__all__ = ["render_feed", "render_mock_feed", "DEMO_POSTS", "render_stories", "STORIES"]

