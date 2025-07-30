import inspect
import pytest
pytest.importorskip("nicegui")

from pages.recommendations_page import recommendations_page


def test_recommendations_page_is_async():
    assert inspect.iscoroutinefunction(recommendations_page)
