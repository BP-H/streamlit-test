# STRICTLY A SOCIAL MEDIA PLATFORM
# Intellectual Property & Artistic Inspiration
# Legal & Ethical Safeguards

import pytest
pytest.importorskip("nicegui")
pytestmark = pytest.mark.requires_nicegui

import inspect
try:
    from pages.proposals_page import proposals_page
except ImportError:  # pragma: no cover - legacy pages removed
    pytest.skip("nicegui pages not available", allow_module_level=True)

def test_proposals_page_is_async():
    assert inspect.iscoroutinefunction(proposals_page)
