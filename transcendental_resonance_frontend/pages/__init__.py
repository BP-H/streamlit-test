"""Unified page modules for the Transcendental Resonance frontend."""

from __future__ import annotations

__all__ = [
    # Streamlit modules
    "validation",
    "voting",
    "agents",
    "resonance_music",
    "chat",
    "feed",
    "social",
    "profile",
    "messages",
    "messages_center",
    "video_chat",
    # NiceGUI modules formerly under ``src.pages``
    "ai_assist_page",
    "debug_panel_page",
    "events_page",
    "explore_page",
    "feed_page",
    "forks_page",
    "groups_page",
    "login_page",
    "messages_page",
    "moderation_dashboard_page",
    "moderation_page",
    "music_page",
    "network_analysis_page",
    "notifications_page",
    "profile_page",
    "proposals_page",
    "recommendations_page",
    "status_page",
    "system_insights_page",
    "upload_page",
    "validator_graph_page",
    "vibenodes_page",
    "video_chat_page",
    "register_page",
    "network_page",
]

_module_map = {
    "register_page": "login_page",
    "network_page": "network_analysis_page",
}


def __getattr__(name: str):
    """Dynamically import page modules on access."""
    if name in __all__ or name in _module_map:
        module_name = _module_map.get(name, name)
        module = __import__(f"{__name__}.{module_name}", fromlist=[name])
        return getattr(module, name)
    raise AttributeError(name)
