# STRICTLY A SOCIAL MEDIA PLATFORM
# Intellectual Property & Artistic Inspiration
# Legal & Ethical Safeguards
"""Unified messages and chat center."""

import streamlit as st
from modern_ui import inject_modern_styles
from streamlit_helpers import safe_container
from video_chat_router import router as video_chat_router

inject_modern_styles()

SAMPLE_MESSAGES: dict[str, list[dict[str, str]]] = {
    "Alice": [{"sender": "Alice", "text": "Hi there!"}],
    "Bob": [{"sender": "Bob", "text": "Hello!"}],
}


def _init_state() -> None:
    if "messages" not in st.session_state:
        st.session_state["messages"] = {
            user: msgs.copy() for user, msgs in SAMPLE_MESSAGES.items()
        }
    if "active_chat" not in st.session_state:
        st.session_state["active_chat"] = next(iter(SAMPLE_MESSAGES))

def _render_conversation_list(users: list[str]) -> None:
    """Display list of conversations and update active selection."""
    active = st.session_state.get("active_chat", users[0] if users else "")
    selected = st.radio("Conversations", users, index=users.index(active)) if users else ""
    st.session_state["active_chat"] = selected


def _render_chat_panel(user: str) -> None:
    """Render chat history and input controls for ``user``."""
    msgs = st.session_state["messages"].setdefault(user, [])
    for msg in msgs:
        st.write(f"{msg['sender']}: {msg['text']}")

    txt = st.text_input("Message", key="msg_input")
    send_col, video_col, upload_col = st.columns(3)

    if send_col.button("Send") and txt:
        msgs.append({"sender": "You", "text": txt})
        st.session_state.msg_input = ""
        st.experimental_rerun()

    if video_col.button("Start Video Call"):
        st.toast("Video call integration pending")
        _ = video_chat_router

    if upload_col.button("Upload Media"):
        st.toast("Upload feature pending")


def main(main_container=None) -> None:
    if main_container is None:
        main_container = st
    _init_state()
    container_ctx = safe_container(main_container)
    with container_ctx:
        st.subheader("✉️ Messages")
        users = list(st.session_state["messages"].keys())
        if not users:
            st.info("No conversations yet")
            return
        left_col, right_col = st.columns([1, 3])
        with left_col:
            _render_conversation_list(users)
        with right_col:
            _render_chat_panel(st.session_state["active_chat"])


def render() -> None:
    main()


if __name__ == "__main__":
    main()
