import inspect
import pytest
pytest.importorskip("nicegui")

from pages.music_page import music_page


def test_music_page_is_async():
    assert inspect.iscoroutinefunction(music_page)
