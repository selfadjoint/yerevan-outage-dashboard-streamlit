import streamlit as st

st.set_page_config(page_title="Redirecting", page_icon="plug", layout="centered")

st.markdown(
    '<meta http-equiv="refresh" content="0;url=https://yerevanoutage.com/" />',
    unsafe_allow_html=True,
)

st.markdown("""
<script>
if (window.location.hostname !== 'yerevanoutage.com') {
    window.location.href = 'https://yerevanoutage.com/';
}
</script>
""", unsafe_allow_html=True)

st.info("Redirecting to yerevanoutage.com...")
