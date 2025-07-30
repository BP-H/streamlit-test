# STRICTLY A SOCIAL MEDIA PLATFORM
# Intellectual Property & Artistic Inspiration
# Legal & Ethical Safeguards
"""Simple helper for translating text between languages."""

from __future__ import annotations

from googletrans import Translator

translator = Translator()


def translate_text(text: str, target_lang: str, source_lang: str | None = None) -> str:
    """Return ``text`` translated to ``target_lang`` using Google Translate.

    If translation fails, return the original text.
    """
    try:
        result = translator.translate(text, dest=target_lang, src=source_lang)
        return result.text
    except Exception:
        return text
