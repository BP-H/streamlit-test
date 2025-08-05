"""Adapters for optional backend integrations used by the UI."""

from __future__ import annotations

from typing import Any, Dict
import logging

try:  # Import backend lazily so tests can patch it easily
    import superNova_2177
except Exception:  # pragma: no cover - if backend unavailable
    superNova_2177 = None  # type: ignore

logger = logging.getLogger(__name__)


_STUB_STATUS: Dict[str, Any] = {
    "status": "offline",
    "timestamp": "N/A",
    "metrics": {},
    "mission": "stub",
    "db": "unavailable",
}


def system_status_adapter(use_backend: bool) -> Dict[str, Any]:
    """Return system status information.

    When ``use_backend`` is ``True`` this function attempts to delegate to
    :func:`superNova_2177.get_system_status`. If that call fails for any reason
    a stub dictionary is returned instead. When ``use_backend`` is ``False`` the
    stub dictionary is returned without attempting any backend calls.
    """

    if not use_backend:
        return _STUB_STATUS.copy()

    if superNova_2177 is None:
        return _STUB_STATUS.copy()

    try:
        return superNova_2177.get_system_status()  # type: ignore[attr-defined]
    except Exception as exc:  # pragma: no cover - protective fallback
        logger.debug("Backend status check failed: %s", exc)
        return _STUB_STATUS.copy()
