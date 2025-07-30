from __future__ import annotations

"""Simple overlay component to surface fatal errors."""

try:
    from nicegui import ui
except Exception:  # pragma: no cover - optional dependency
    ui = None  # type: ignore


class ErrorOverlay:
    """Display an overlay with an error message."""

    def __init__(self) -> None:
        if ui is not None:
            self._dialog = ui.dialog().props("persistent")
            with self._dialog:
                with ui.card():
                    self._label = ui.label("Error")
                    ui.button("Close", on_click=self.hide)
        else:  # pragma: no cover - lightweight fallback
            self._dialog = None
            self._label = None

    def show(self, message: str) -> None:
        if ui is None or self._dialog is None:
            print(f"ERROR: {message}")
            return
        self._label.text = message
        if not self._dialog.open:
            self._dialog.open()

    def hide(self) -> None:
        if ui is not None and self._dialog and self._dialog.open:
            self._dialog.close()


__all__ = ["ErrorOverlay"]
