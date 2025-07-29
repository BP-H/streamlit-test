import asyncio
import json
import streamlit as st
from streamlit_helpers import alert

_TAB_CSS = """
<style>
.tab-box {
    padding: 1rem;
    border-radius: 8px;
    border: 1px solid #e0e0e0;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    margin-bottom: 1rem;
}
</style>
"""

try:
    from frontend_bridge import dispatch_route
except Exception:  # pragma: no cover - optional dependency
    dispatch_route = None  # type: ignore


def _run_async(coro):
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        return asyncio.run(coro)
    else:
        if loop.is_running():
            return asyncio.run_coroutine_threadsafe(coro, loop).result()
        return loop.run_until_complete(coro)


def render_proposals_tab() -> None:
    """Display proposal creation, listing and voting controls."""
    if dispatch_route is None:
        alert(
            "Governance routes not enabled—enable them in config.",
            "warning",
        )
        return
    st.markdown(_TAB_CSS, unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="tab-box">', unsafe_allow_html=True)
        if st.button("Refresh Proposals"):
            try:
                res = _run_async(dispatch_route("list_proposals", {}))
                st.session_state["proposals_cache"] = res.get("proposals", [])
            except Exception as exc:
                alert(f"Failed to load proposals: {exc}", "error")

        proposals = st.session_state.get("proposals_cache", [])
        if proposals:
            simple = [
                {
                    "id": p.get("id"),
                    "title": p.get("title"),
                    "status": p.get("status"),
                    "deadline": p.get("voting_deadline"),
                }
                for p in proposals
            ]
            st.table(simple)

        col1, col2 = st.columns(2)
        with col1.form("create_proposal_form"):
            st.write("Create Proposal")
            title = st.text_input("Title")
            description = st.text_area("Description")
            author_id = st.number_input("Author ID", value=1, step=1)
            group_id = st.text_input("Group ID")
            voting_deadline = st.date_input("Voting Deadline")
            submitted = st.form_submit_button("Create")
        if submitted:
            payload = {
                "title": title,
                "description": description,
                "author_id": int(author_id),
                "group_id": group_id or None,
                "voting_deadline": voting_deadline.isoformat(),
            }
            try:
                res = _run_async(dispatch_route("create_proposal", payload))
                alert(f"Proposal {res.get('proposal_id')} created", "info")
            except Exception as exc:
                alert(f"Create failed: {exc}", "error")

        with col2.form("vote_proposal_form"):
            st.write("Vote on Proposal")
            ids = [p.get("id") for p in proposals]
            prop_id = (
                st.selectbox("Proposal", ids)
                if ids
                else st.number_input("Proposal ID", value=1, step=1)
            )
            harmonizer_id = st.number_input(
                "Harmonizer ID", value=1, step=1, key="harmonizer_id_vote"
            )
            vote_choice = st.selectbox("Vote", ["yes", "no", "abstain"])
            vote_sub = st.form_submit_button("Submit Vote")
        if vote_sub:
            payload = {
                "proposal_id": prop_id,
                "harmonizer_id": int(harmonizer_id),
                "vote": vote_choice,
            }
            try:
                res = _run_async(dispatch_route("vote_proposal", payload))
                alert(f"Vote recorded id {res.get('vote_id')}", "info")
            except Exception as exc:
                alert(f"Vote failed: {exc}", "error")
        st.markdown('</div>', unsafe_allow_html=True)
def render_governance_tab() -> None:
    """Display generic vote registry operations."""
    if dispatch_route is None:
        alert(
            "Governance routes not enabled—enable them in config.",
            "warning",
        )
        return
    st.markdown(_TAB_CSS, unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="tab-box">', unsafe_allow_html=True)
        if st.button("Refresh Votes"):
            try:
                res = _run_async(dispatch_route("load_votes", {}))
                st.session_state["votes_cache"] = res.get("votes", [])
            except Exception as exc:
                alert(f"Failed to load votes: {exc}", "error")

        votes = st.session_state.get("votes_cache", [])
        col1, col2 = st.columns(2)
        with col1:
            if votes:
                st.table(votes)
        with col2.form("record_vote_form"):
            st.write("Record Vote")
            species = st.selectbox("Species", ["human", "ai", "company"])
            extra_json = st.text_input("Extra Fields (JSON)", value="{}")
            submit = st.form_submit_button("Record")
        if submit:
            try:
                extra = json.loads(extra_json or "{}")
            except Exception as exc:
                alert(f"Invalid JSON: {exc}", "error")
            else:
                payload = {"species": species, **extra}
                try:
                    _run_async(dispatch_route("record_vote", payload))
                    alert("Vote recorded", "info")
                except Exception as exc:
                    alert(f"Record failed: {exc}", "error")
        st.markdown('</div>', unsafe_allow_html=True)
def render_agent_ops_tab() -> None:
    """Expose protocol agent management routes."""
    if dispatch_route is None:
        alert(
            "Governance routes not enabled—enable them in config.",
            "warning",
        )
        return
    st.markdown(_TAB_CSS, unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="tab-box">', unsafe_allow_html=True)
        if st.button("Reload Agent List"):
            try:
                res = _run_async(dispatch_route("list_agents", {}))
                st.session_state["agent_list"] = res.get("agents", [])
            except Exception as exc:
                alert(f"Load failed: {exc}", "error")

        agents = st.session_state.get("agent_list", [])
        col1, col2 = st.columns(2)
        with col1:
            st.write("Available Agents", agents)
            if st.button("Step Agents"):
                try:
                    res = _run_async(dispatch_route("step_agents", {}))
                    st.json(res)
                except Exception as exc:
                    alert(f"Step failed: {exc}", "error")
        with col2.form("launch_agents_form"):
            launch_sel = st.multiselect("Agents to launch", agents)
            llm_backend = st.selectbox(
                "LLM Backend", ["", "dummy", "GPT-4o", "Claude-3", "Gemini"]
            )
            provider = st.text_input("Provider")
            api_key = st.text_input("API Key", type="password")
            launch = st.form_submit_button("Launch Agents")
        if launch:
            payload = {
                "agents": launch_sel,
                "llm_backend": llm_backend or None,
                "provider": provider,
                "api_key": api_key,
            }
            try:
                res = _run_async(dispatch_route("launch_agents", payload))
                st.json(res)
            except Exception as exc:
                alert(f"Launch failed: {exc}", "error")
        st.markdown('</div>', unsafe_allow_html=True)
def render_logs_tab() -> None:
    """Provide simple audit trace explanation."""
    if dispatch_route is None:
        alert(
            "Governance routes not enabled—enable them in config.",
            "warning",
        )
        return
    st.markdown(_TAB_CSS, unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="tab-box">', unsafe_allow_html=True)
        trace_text = st.text_area("Audit Trace JSON", value="{}", height=200)
        if st.button("Explain Trace"):
            try:
                trace = json.loads(trace_text or "{}")
            except Exception as exc:
                alert(f"Invalid JSON: {exc}", "error")
            else:
                try:
                    res = _run_async(dispatch_route("explain_audit", {"trace": trace}))
                    st.text_area("Explanation", value=res, height=150)
                except Exception as exc:
                    alert(f"Explain failed: {exc}", "error")
        st.markdown('</div>', unsafe_allow_html=True)
def render_voting_tab() -> None:
    """High level tab combining proposal and vote management."""
    st.markdown(_TAB_CSS, unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="tab-box">', unsafe_allow_html=True)
        sub1, sub2, sub3, sub4 = st.tabs([
            "Proposal Hub",
            "Governance",
            "Agent Ops",
            "Logs",
        ])
        with sub1:
            render_proposals_tab()
        with sub2:
            render_governance_tab()
        with sub3:
            render_agent_ops_tab()
        with sub4:
            render_logs_tab()
        st.markdown('</div>', unsafe_allow_html=True)
