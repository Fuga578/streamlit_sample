import streamlit as st


icon = "https://upload.wikimedia.org/wikipedia/commons/4/48/Markdown-mark.svg"

# レイアウト設定
# layout = "centered"
layout = "wide"
st.set_page_config(
    layout=layout,
    page_title="layout sample",
    page_icon=icon
    # page_icon="🧊"
)

st.logo(
    image=icon,
    link="https://github.github.com/gfm/"
)

st.markdown(f"### {layout}")
numbers = ":blue[0]123456789" * 10
st.markdown(numbers)
