import streamlit as st
from typing import List, Dict

try:
    from db_models import SessionLocal, SystemState
except Exception:  # pragma: no cover - optional dependency
    SessionLocal = None  # type: ignore
    SystemState = None  # type: ignore

# Keys reused from milestone_cli for consistency
KEY_SEASONAL = "seasonal_active"
KEY_QUEST = "quest_active"


def _get_flag(key: str) -> bool:
    """Return SystemState boolean flag value."""
    if SessionLocal is None or SystemState is None:
        return False
    db = SessionLocal()
    try:
        state = db.query(SystemState).filter(SystemState.key == key).first()
        return bool(state and state.value == "1")
    finally:
        db.close()


def _set_flag(key: str, value: bool) -> None:
    """Set a SystemState boolean flag."""
    if SessionLocal is None or SystemState is None:
        return
    db = SessionLocal()
    try:
        state = db.query(SystemState).filter(SystemState.key == key).first()
        val = "1" if value else "0"
        if state:
            state.value = val
        else:
            db.add(SystemState(key=key, value=val))
        db.commit()
    finally:
        db.close()


# Dummy quest data until backend expansion
Quest = Dict[str, any]


def _dummy_quests() -> List[Quest]:
    """Return placeholder quest definitions."""
    return [
        {
            "id": "q1",
            "name": "Harmonizer Welcome",
            "description": "Engage with the community to earn starter badges.",
            "toggleable": True,
            "state_key": KEY_QUEST,
            "milestones": [
                {"title": "Create an account", "progress": 1, "target": 1},
                {"title": "Follow 3 users", "progress": 2, "target": 3},
                {"title": "Post your first update", "progress": 0, "target": 1},
            ],
        },
        {
            "id": "q2",
            "name": "Seasonal Scholar",
            "description": "Complete learning modules during the seasonal event.",
            "toggleable": False,
            "state_key": KEY_SEASONAL,
            "milestones": [
                {"title": "Finish module 1", "progress": 1, "target": 1},
                {"title": "Finish module 2", "progress": 0, "target": 1},
                {"title": "Finish module 3", "progress": 0, "target": 1},
            ],
        },
    ]


def _quest_progress(quest: Quest) -> float:
    """Return completion ratio for a quest."""
    milestones = quest.get("milestones", [])
    if not milestones:
        return 0.0
    completed = sum(1 for m in milestones if m.get("progress", 0) >= m.get("target", 1))
    return completed / len(milestones)


def render_seasonal_quests_tab() -> None:
    """Display seasonal quest progress with toggle controls."""
    st.subheader("Seasonal Quests")
    quests = _dummy_quests()
    for q in quests:
        st.markdown(f"### {q['name']}")
        st.write(q.get("description", ""))
        if q.get("toggleable"):
            active = _get_flag(q.get("state_key", ""))
            new_val = st.checkbox("Active", value=active, key=f"toggle_{q['id']}")
            if new_val != active:
                _set_flag(q.get("state_key", ""), new_val)
        progress = _quest_progress(q)
        st.progress(progress)
        with st.expander("Milestones"):
            for i, m in enumerate(q.get("milestones", [])):
                done = m.get("progress", 0) >= m.get("target", 1)
                label = f"{m['title']} ({m.get('progress',0)}/{m.get('target',1)})"
                st.checkbox(label, value=done, disabled=True, key=f"{q['id']}_{i}")





