import inspect
from pages.moderation_page import moderation_page

def test_moderation_page_is_async():
    assert inspect.iscoroutinefunction(moderation_page)
