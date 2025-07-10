import streamlit as st


st.header("予測最高最低気温")

st.markdown(f"**:red[2024-09-14]**")

col_min, col_max = st.columns(2)
col_min.metric("予想最低気温", "19.8℃", delta=-0.2)
col_max.metric("予想最高気温", "27.0℃", delta=0.5)
