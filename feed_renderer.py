# STRICTLY A SOCIAL MEDIA PLATFORM
# Intellectual Property & Artistic Inspiration
# Legal & Ethical Safeguards
"""Utilities for rendering a simple (or custom) social feed."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Iterable, Dict, Any, List

import streamlit as st

from streamlit_helpers import render_post_card

# ──────────────────────────────────────────────────────────────────────────────
# Data structures & demo-data helpers
# ──────────────────────────────────────────────────────────────────────────────
@dataclass
class Post:
    """Lightweight post object used by demo helpers (optional for callers)."""

    username: str
    image: str
    caption: str
    reactions: Dict[str, int] | None = None


def generate_demo_posts() -> List[Dict[str, Any]]:
    """Return a handful of placeholder posts with random “likes” counts."""
    users = ["Alice", "Bob", "Carol"]
    demo: list[dict[str, Any]] = []
    for idx, user in enumerate(users, start=1):
        demo.append(
            {
                "user": user,
                "image": f"https://placehold.co/600x400?text=Post+{idx}",
                "text": f"Demo caption {idx}",
                "likes": random.randint(1, 15),
            }
        )
    return demo


# A static snapshot so older imports like “from feed_renderer import DEMO_POSTS”
# keep working.  Regenerated on every module import to avoid stale randomness.
DEMO_POSTS: List[Dict[str, Any]] = generate_demo_posts()

# ──────────────────────────────────────────────────────────────────────────────
# Rendering helpers
# ──────────────────────────────────────────────────────────────────────────────
def render_feed(posts: Iterable[Dict[str, Any]] | None = None) -> None:
    """
    Render a sequence of post-dicts with :func:`render_post_card`.

    Parameters
    ----------
    posts
        Iterable of post dictionaries. If *None* (default) the in-module
        ``DEMO_POSTS`` list is rendered instead.  Each post should contain
        at least ``image`` and ``text``; ``user`` / ``likes`` are optional.
    """
    data = list(posts) if posts is not None else DEMO_POSTS
    if not data:
        st.info("No posts to display")
        return

    for post in data:
        render_post_card(post)


def render_mock_feed() -> None:
    """
    Convenience wrapper that simply shows the built-in ``DEMO_POSTS``.

    This keeps older code that imported/used *render_mock_feed()* working.
    """
    render_feed(DEMO_POSTS)


# What this module publicly exposes
__all__ = [
    "Post",
    "generate_demo_posts",
    "DEMO_POSTS",
    "render_feed",
    "render_mock_feed",
]


