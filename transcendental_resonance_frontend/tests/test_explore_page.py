# STRICTLY A SOCIAL MEDIA PLATFORM
# Intellectual Property & Artistic Inspiration
# Legal & Ethical Safeguards

import pytest
pytest.importorskip("nicegui")
pytestmark = pytest.mark.requires_nicegui

# STRICTLY A SOCIAL MEDIA PLATFORM
# Intellectual Property & Artistic Inspiration
# Legal & Ethical Safeguards
import inspect
try:
    from pages.explore_page import explore_page
except ImportError:  # pragma: no cover - legacy pages removed
    pytest.skip("nicegui pages not available", allow_module_level=True)


def test_explore_page_is_async():
    assert inspect.iscoroutinefunction(explore_page)  # nosec B101


def test_explore_page_uses_trending_endpoint():
    src = inspect.getsource(explore_page)
    assert "/vibenodes/trending" in src  # nosec B101
