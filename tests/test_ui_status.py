import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import ui_adapters  # noqa: E402
from ui_adapters import system_status_adapter, _STUB_STATUS  # noqa: E402


def test_returns_stub_when_disabled(monkeypatch):
    def fail_backend():
        raise AssertionError("backend should not be called")

    monkeypatch.setattr(
        ui_adapters.superNova_2177, "get_system_status", fail_backend, raising=False
    )
    result = system_status_adapter(False)
    assert result == _STUB_STATUS


def test_delegates_when_enabled(monkeypatch):
    expected = {"status": "online"}

    monkeypatch.setattr(
        ui_adapters.superNova_2177, "get_system_status", lambda: expected, raising=False
    )
    result = system_status_adapter(True)
    assert result is expected


def test_backend_error_returns_stub(monkeypatch):
    def raise_error():
        raise RuntimeError("boom")

    monkeypatch.setattr(
        ui_adapters.superNova_2177, "get_system_status", raise_error, raising=False
    )
    result = system_status_adapter(True)
    assert result == _STUB_STATUS
