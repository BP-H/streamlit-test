import streamlit as st
from streamlit_helpers import inject_global_styles

inject_global_styles()

st.markdown("<div class='card'>", unsafe_allow_html=True)
st.title("It Works!")
st.markdown("</div>", unsafe_allow_html=True)
