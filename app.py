import streamlit as st

st.set_page_config(page_title="Redirecting...", page_icon="🔌")

# Redirect using both meta refresh and JavaScript for maximum compatibility
redirect_html = """
<meta http-equiv="refresh" content="0;url=https://yerevanoutage.com/" />
<script>
window.location.href = "https://yerevanoutage.com/";
</script>
"""

st.markdown(redirect_html, unsafe_allow_html=True)
st.write("Redirecting to yerevanoutage.com...")
