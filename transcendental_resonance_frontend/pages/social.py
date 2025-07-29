"""Friends & Followers page."""
from social_tabs import render_social_tab
import streamlit as st

def main(main_container=None) -> None:
    if main_container is None:
        main_container = st
    with main_container:
        render_social_tab(main_container=main_container)
