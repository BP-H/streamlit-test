import types
import sys
from pathlib import Path

import pytest

pytest.importorskip("streamlit")
pytestmark = pytest.mark.requires_streamlit

root = Path(__file__).resolve().parents[1]
if str(root) not in sys.path:
    sys.path.insert(0, str(root))

import frontend.theme as theme


def test_apply_theme_and_accent_color(monkeypatch):
    calls = []

    def dummy_markdown(css, **kwargs):
        calls.append(css)

    dummy_st = types.SimpleNamespace(markdown=dummy_markdown, session_state={})
    monkeypatch.setattr(theme, "st", dummy_st)

    theme.apply_theme("light")
    assert dummy_st.session_state["_theme"] == "light"
    assert theme.get_accent_color() == theme.LIGHT_THEME.accent
    theme.apply_theme("dark")
    assert dummy_st.session_state["_theme"] == "dark"
    assert theme.get_accent_color() == theme.DARK_THEME.accent
    assert len(calls) == 2


def test_inject_modern_styles_idempotent(monkeypatch):
    calls = []

    def dummy_markdown(css, **kwargs):
        calls.append(css)

    dummy_st = types.SimpleNamespace(markdown=dummy_markdown, session_state={})
    monkeypatch.setattr(theme, "st", dummy_st)

    theme.inject_modern_styles("light")
    theme.inject_modern_styles("dark")

    # one extra CSS block should appear only once
    extra_calls = [c for c in calls if "Glassmorphic cards" in c]
    assert len(extra_calls) == 1

