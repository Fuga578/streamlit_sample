import streamlit as st


# コードの実行と、コードの画面表示を同時に実行
# with st.echo(code_location="above"):
with st.echo(code_location="below"):
    st.title(":red[風船アニメーション]")
    st.balloons()
