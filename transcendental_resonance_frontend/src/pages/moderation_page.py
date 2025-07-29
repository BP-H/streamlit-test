from __future__ import annotations

"""Moderation dashboard for reviewing flagged content."""

from nicegui import ui

from utils.api import api_call, TOKEN, listen_ws
from utils.layout import page_container, navigation_bar
from utils.styles import get_theme
from moderation_utils import get_flagged_items, remove_flagged_item
from .login_page import login_page


@ui.page('/moderation')
async def moderation_page() -> None:
    """Display queued flagged content for moderator review."""
    if not TOKEN:
        ui.open(login_page)
        return

    theme = get_theme()
    with page_container(theme):
        if TOKEN:
            navigation_bar()
        ui.label('Moderation').classes('text-2xl font-bold mb-4').style(
            f"color: {theme['accent']};"
        )

        items_container = ui.column().classes('w-full')

        async def refresh() -> None:
            items = get_flagged_items()
            items_container.clear()
            for item in items:
                with items_container:
                    with ui.card().classes('w-full mb-2').style('border: 1px solid #333; background: #1e1e1e;'):
                        ui.label(item['text']).classes('text-sm')
                        ui.label(item['reason']).classes('text-xs text-red-400 mb-2')
                        with ui.row():
                            ui.button('Approve', on_click=lambda it=item: ui.run_async(action('approve', it))).props('flat')
                            ui.button('Reject', on_click=lambda it=item: ui.run_async(action('reject', it))).props('flat')
                            ui.button('Censor', on_click=lambda it=item: ui.run_async(action('censor', it))).props('flat')
                            ui.button('Ban User', on_click=lambda it=item: ui.run_async(action('ban', it))).props('flat')

        async def action(name: str, item: dict) -> None:
            await api_call('POST', f'/moderation/{name}', {"text": item['text']})
            remove_flagged_item(item)
            await refresh()

        await refresh()
        ui.timer(5.0, lambda: ui.run_async(refresh()))

        async def handle_event(event: dict) -> None:
            if event.get('type') == 'flagged_content':
                await refresh()

        ws_task = listen_ws(handle_event)
        ui.context.client.on_disconnect(lambda: ws_task.cancel())
