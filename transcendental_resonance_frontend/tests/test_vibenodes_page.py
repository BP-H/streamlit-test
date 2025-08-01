# STRICTLY A SOCIAL MEDIA PLATFORM
# Intellectual Property & Artistic Inspiration
# Legal & Ethical Safeguards

import pytest
pytest.importorskip("nicegui")
pytestmark = pytest.mark.requires_nicegui

import inspect
try:
    from pages.vibenodes_page import vibenodes_page
except ImportError:  # pragma: no cover - legacy pages removed
    pytest.skip("nicegui pages not available", allow_module_level=True)

def test_vibenodes_page_is_async():
    assert inspect.iscoroutinefunction(vibenodes_page)

def test_vibenodes_page_has_search_widgets():
    src = inspect.getsource(vibenodes_page)
    assert "ui.input('Search'" in src
    assert "ui.select(['name', 'date', 'trending']" in src
