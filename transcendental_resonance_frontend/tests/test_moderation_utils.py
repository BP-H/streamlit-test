from moderation_utils import Vaccine, get_flagged_items, FLAGGED_QUEUE

class DummyConfig:
    VAX_PATTERNS = {"block": ["spam"]}

def test_scan_logs_flagged_items():
    FLAGGED_QUEUE.clear()
    v = Vaccine(DummyConfig())
    assert v.scan("clean text")
    assert get_flagged_items() == []
    assert not v.scan("this is spam")
    items = get_flagged_items()
    assert items and items[0]["reason"]
