import inspect
import pytest
pytest.importorskip("nicegui")

from pages.login_page import login_page

def test_login_page_is_async():
    assert inspect.iscoroutinefunction(login_page)
