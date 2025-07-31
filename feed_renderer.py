# STRICTLY A SOCIAL MEDIA PLATFORM
# Intellectual Property & Artistic Inspiration
# Legal & Ethical Safeguards
"""Simple renderer for a social feed."""

from __future__ import annotations

from typing import Iterable, Dict, Any, List
from dataclasses import dataclass
import random

import streamlit as st

from streamlit_helpers import render_post_card


@dataclass
class Post:
    """Simple post structure for demo feeds."""

    username: str
    image: str
    caption: str
    reactions: Dict[str, int]


def generate_demo_posts() -> List[Dict[str, Any]]:
    """Return a few placeholder posts with random reactions."""
    users = ["Alice", "Bob", "Carol"]
    demo: List[Dict[str, Any]] = []
    for idx, user in enumerate(users, start=1):
        demo.append(
            {
                "username": user,
                "image": f"https://placehold.co/600x400?text=Post+{idx}",
                "text": f"Demo caption {idx}",
                "likes": random.randint(1, 9),
            }
        )
    return demo


def render_feed(posts: Iterable[Dict[str, Any]] | None = None) -> None:
    """Render each post using :func:`render_post_card`."""
    if posts is None:
        posts = generate_demo_posts()

    posts = list(posts)
    if not posts:
        st.info("No posts to display")
        return

    for post in posts:
        render_post_card(post)

__all__ = ["render_feed", "generate_demo_posts", "Post"]

