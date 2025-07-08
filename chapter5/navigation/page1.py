import streamlit as st
from PIL import Image
from save import st_render


def on_change() -> None:
    """アップロードされた画像ファイルをセッションに保存します。"""
    uploaded = st.session_state._image_upload
    if uploaded is not None:
        img = Image.open(uploaded)
        img.filename = uploaded.name
        st.session_state.image_upload = img
    else:
        st.session_state.pop("image_upload", None)


st.header(":rainbow[元画像]")

# 画像アップローダー（key指定により、session_stateに自動保存）
st.file_uploader(
    "画像ファイルをアップロードしてください。",
    key="_image_upload",
    on_change=on_change
)

# 画像がアップロードされた場合、画面に表示
if "image_upload" in st.session_state:
    img = st.session_state.image_upload
    st.image(img)
    st_render(img)
