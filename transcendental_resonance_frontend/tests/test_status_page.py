# STRICTLY A SOCIAL MEDIA PLATFORM
# Intellectual Property & Artistic Inspiration
# Legal & Ethical Safeguards

import pytest
pytest.importorskip("nicegui")
pytestmark = pytest.mark.requires_nicegui

import inspect
from transcendental_resonance_frontend.pages.status_page import status_page

def test_status_page_is_async():
    assert inspect.iscoroutinefunction(status_page)
