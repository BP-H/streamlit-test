# RFC_V5_1_INIT
"""Moderation helper stubs."""

from typing import Any, Deque, Dict, List
from collections import deque
from datetime import datetime
import re


def check_profanity(text: str) -> bool:
    """Return True if profanity detected (stub)."""
    banned = {"badword"}
    words = set(text.lower().split())
    return not banned.isdisjoint(words)


def has_active_consent(user: Any = None) -> bool:
    """Placeholder consent check."""
    return True


FLAGGED_QUEUE: Deque[Dict[str, str]] = deque(maxlen=100)


def log_flagged_content(text: str, reason: str) -> None:
    """Add a flagged item to the global queue."""
    FLAGGED_QUEUE.appendleft(
        {"text": text, "reason": reason, "timestamp": datetime.utcnow().isoformat()}
    )


def get_flagged_items() -> List[Dict[str, str]]:
    """Return the list of currently flagged items."""
    return list(FLAGGED_QUEUE)


def remove_flagged_item(item: Dict[str, str]) -> None:
    """Remove ``item`` from the queue if present."""
    try:
        FLAGGED_QUEUE.remove(item)
    except ValueError:
        pass


class Vaccine:
    """Simple text vaccine using regex-based filtering."""

    def __init__(self, config: Any):
        """Compile patterns from ``config.VAX_PATTERNS['block']``."""
        block = config.VAX_PATTERNS.get("block", [])
        self.patterns = [re.compile(p, re.IGNORECASE) for p in block]

    def scan(self, text: str) -> bool:
        """Return ``True`` if content passes vaccine checks."""
        lower = text.lower()
        for pat in self.patterns:
            if pat.search(lower):
                log_flagged_content(text, "pattern match")
                return False
        if check_profanity(text):
            log_flagged_content(text, "profanity detected")
            return False
        return True
