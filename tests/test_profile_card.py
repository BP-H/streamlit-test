import types
import sys
from pathlib import Path
import pytest
pytest.importorskip("streamlit")
pytestmark = pytest.mark.requires_streamlit

root = Path(__file__).resolve().parents[1]
if str(root) not in sys.path:
    sys.path.insert(0, str(root))

import profile_card


def test_render_profile_card_includes_env_badge(monkeypatch):
    captured = {}
    dummy_st = types.SimpleNamespace(markdown=lambda html, **k: captured.setdefault('html', html))
    monkeypatch.setattr(profile_card, 'st', dummy_st)
    monkeypatch.setenv('APP_ENV', 'production')
    profile_card.render_profile_card('User', 'avatar.png')
    assert '🚀 Production' in captured.get('html', '')
