import streamlit as st
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
if str(root) not in sys.path:
    sys.path.insert(0, str(root))

from transcendental_resonance_frontend.pages import validation


def test_validation_main_runs(monkeypatch):
    called = {}
    def dummy_render_validation_ui(*, main_container):
        called['container'] = main_container
    monkeypatch.setattr(validation, 'render_validation_ui', dummy_render_validation_ui)
    validation.main(main_container=st)
    assert called['container'] is st
