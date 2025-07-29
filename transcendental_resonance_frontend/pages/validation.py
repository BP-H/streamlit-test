"""Validation analysis page."""
from ui import render_validation_ui
import streamlit as st

def main(main_container=None) -> None:
    if main_container is None:
        main_container = st
    with main_container:
        render_validation_ui(main=main_container)
