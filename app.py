import streamlit as st

st.set_page_config(
    page_title="Yerevan Utility Outages",
    page_icon="🔌",
    layout="centered",
)

st.title("🔌 Yerevan Utility Outages")

st.info(
    """
    This project has moved to a new home!

    **[Visit the new dashboard →](https://yerevanoutage.com/)**

    For source code and development, see:
    **[github.com/selfadjoint/yerevan-outage-dashboard](https://github.com/selfadjoint/yerevan-outage-dashboard)**
    """
)

st.markdown(
    """
    <meta http-equiv="refresh" content="3;url=https://yerevanoutage.com/" />
    Redirecting in 3 seconds...
    """,
    unsafe_allow_html=True,
)
