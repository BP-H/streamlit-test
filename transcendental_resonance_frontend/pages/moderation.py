"""Moderation dashboard wrapper for Streamlit."""
from pages.moderation_page import moderation_page as _moderation_page
import asyncio

def main() -> None:
    asyncio.run(_moderation_page())
