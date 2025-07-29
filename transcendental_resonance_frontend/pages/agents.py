"""Agent insights page."""
from agent_ui import render_agent_insights_tab
import streamlit as st

def main(main_container=None) -> None:
    if main_container is None:
        main_container = st
    with main_container:
        render_agent_insights_tab(main_container=main_container)
