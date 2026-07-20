import streamlit as st

st.set_page_config(page_title="Redirecting...", page_icon="🔌")

st.markdown(
    """
    <meta http-equiv="refresh" content="0;url=https://yerevanoutage.com/" />
    """,
    unsafe_allow_html=True,
)

st.write("Redirecting to yerevanoutage.com...")
