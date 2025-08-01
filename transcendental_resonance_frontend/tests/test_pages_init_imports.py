# STRICTLY A SOCIAL MEDIA PLATFORM
# Intellectual Property & Artistic Inspiration
# Legal & Ethical Safeguards

import pytest
pytest.importorskip("nicegui")
pytestmark = pytest.mark.requires_nicegui

import inspect
try:
    from pages import register_page, network_page
except ImportError:  # pragma: no cover - legacy pages removed
    pytest.skip("nicegui pages not available", allow_module_level=True)


def test_register_page_importable():
    assert inspect.iscoroutinefunction(register_page)


def test_network_page_importable():
    assert inspect.iscoroutinefunction(network_page)
