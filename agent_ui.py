# STRICTLY A SOCIAL MEDIA PLATFORM
# Intellectual Property & Artistic Inspiration
# Legal & Ethical Safeguards
import json
from pathlib import Path
from datetime import datetime
from typing import cast

import streamlit as st
from streamlit_helpers import (
    inject_global_styles,
    theme_selector,
    safe_container,
    BOX_CSS,  # ✅ Use imported version
    header,
)
from ui_utils import load_rfc_entries, summarize_text
from voting_ui import (
    render_proposals_tab,
    render_governance_tab,
    render_agent_ops_tab,
    render_logs_tab,
)

from ui_utils import load_rfc_entries, summarize_text



def render_agent_insights_tab(main_container=None) -> None:
    """Display diary, RFC summaries and internal notes."""
    if main_container is None:
        main_container = st

    inject_global_styles()
    theme_selector("Theme", key_suffix="agent_insights")
    container_ctx = safe_container(main_container)
    with container_ctx:
        st.markdown(BOX_CSS + "<div class='tab-box'>", unsafe_allow_html=True)
        header("Virtual Diary")
        with st.expander("📘 Notes", expanded=False):
            diary_note = st.text_input("Add note")
            rfc_input = st.text_input("Referenced RFC IDs (comma separated)")
            if st.button("Append Note"):
                entry = {
                    "timestamp": datetime.utcnow().isoformat(timespec="seconds"),
                    "note": diary_note,
                }
                rfc_ids = [r.strip() for r in rfc_input.split(",") if r.strip()]
                if rfc_ids:
                    entry["rfc_ids"] = rfc_ids
                st.session_state.setdefault("diary", []).append(entry)
        for entry in st.session_state.get("diary", []):
            note = entry.get("note", "")
            rfc_list = entry.get("rfc_ids")
            extra = f" (RFCs: {', '.join(rfc_list)})" if rfc_list else ""
            with st.container():
                st.markdown(f"**{entry['timestamp']}**: {note}{extra}")
        if st.download_button(
            "Export Diary as Markdown",
            "\n".join(
                [
                    f"* {e['timestamp']}: {e.get('note', '')}"
                    + (
                        f" (RFCs: {', '.join(e['rfc_ids'])})"
                        if e.get("rfc_ids")
                        else ""
                    )
                    for e in st.session_state.get("diary", [])
                ]
            ),
            file_name="diary.md",
        ):
            pass
        st.download_button(
            "Export Diary as JSON",
            json.dumps(st.session_state.get("diary", []), indent=2),
            file_name="diary.json",
        )

        header("RFCs and Agent Insights")
        with st.container():
            with st.expander("Proposed RFCs", expanded=False):
                rfc_dir = Path("rfcs")
                filter_text = st.text_input("Filter RFCs")
                preview_all = st.toggle("Preview full text")

            rfc_entries, rfc_index = load_rfc_entries(rfc_dir)

            diary_mentions: dict[str, list[int]] = {
                str(e["id"]): [] for e in rfc_entries
            }
            for i, entry in enumerate(st.session_state.get("diary", [])):
                note_lower = entry.get("note", "").lower()
                ids = {e.strip().lower() for e in entry.get("rfc_ids", []) if e}
                for rfc in rfc_entries:
                    rid = str(rfc["id"]).lower()
                    if (
                        rid in note_lower
                        or rid.replace("-", " ") in note_lower
                        or rid in ids
                    ):
                        diary_mentions.setdefault(str(rfc["id"]), []).append(i)
                        continue
                    keywords = {
                        w.strip(".,()[]{}:").lower()
                        for w in str(rfc["summary"]).split()
                        if len(w) > 4
                    }
                    if any(k in note_lower for k in keywords):
                        diary_mentions.setdefault(str(rfc["id"]), []).append(i)

            for rfc in rfc_entries:
                if (
                    filter_text
                    and filter_text.lower() not in rfc["summary"].lower()
                    and filter_text.lower() not in rfc["id"].lower()
                ):
                    continue
                mentions = diary_mentions.get(str(rfc["id"]), [])
                heading = f"<mark>{rfc['id']}</mark>" if mentions else rfc["id"]
                st.markdown(f"### {heading}", unsafe_allow_html=True)
                st.write(summarize_text(str(rfc["summary"])))
                if mentions:
                    links = ", ".join(
                        [f"[entry {idx + 1}](#diary-{idx})" for idx in mentions]
                    )
                    st.markdown(f"Referenced in: {links}", unsafe_allow_html=True)
                st.markdown(f"[Read RFC]({cast(Path, rfc['path']).as_posix()})")
                if preview_all or st.toggle("Show details", key=f"show_{rfc['id']}"):
                    st.markdown(rfc["text"], unsafe_allow_html=True)

        header("Protocols")
        with st.container():
            with st.expander("Repository Protocols", expanded=False):
                proto_dir = Path("protocols")
                files = sorted([p for p in proto_dir.glob("*.py") if p.is_file()])
                for file in files:
                    st.markdown(f"- [{file.name}]({file.as_posix()})")

        notes_path = Path("AgentNotes.md")
        if notes_path.exists():
            notes_content = notes_path.read_text()
        else:
            notes_content = "No notes found."

        with st.container():
            with st.expander("Agent’s Internal Thoughts"):
                st.markdown(notes_content)

        if st.session_state.get("governance_view"):
            tabs = st.tabs(
                [
                    "Proposal Hub",
                    "Governance",
                    "Agent Ops",
                    "Logs",
                ]
            )
            render_proposals_tab(main_container=tabs[0])
            render_governance_tab(main_container=tabs[1])
            render_agent_ops_tab(main_container=tabs[2])
            render_logs_tab(main_container=tabs[3])
        else:
            st.info("Enable Governance View in the sidebar to see governance features.")
        st.markdown("</div>", unsafe_allow_html=True)
