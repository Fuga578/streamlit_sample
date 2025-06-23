import streamlit as st


st.markdown("---")

cols = st.columns(
    [0.2, 0.5, 0.3],
    gap="large",
    vertical_alignment="center"
)
st.markdown("---")

numbers = ":blue[0]123456789" * 3
cols[0].markdown(numbers)
cols[1].markdown(numbers)
cols[2].markdown(numbers)
