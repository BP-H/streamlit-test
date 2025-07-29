"""Governance and voting page."""
from voting_ui import render_voting_tab
import streamlit as st

def main(main_container=None) -> None:
    if main_container is None:
        main_container = st
    with main_container:
        render_voting_tab(main_container=main_container)
