"""Proxy package for Streamlit/NiceGUI pages."""

from __future__ import annotations

import importlib

_mapping = {
    "register_page": "transcendental_resonance_frontend.pages.login_page",
    "network_page": "transcendental_resonance_frontend.pages.network_analysis_page",
}


def __getattr__(name: str):
    if name in _mapping:
        mod = importlib.import_module(_mapping[name])
        return getattr(mod, name)
    raise AttributeError(name)
