from PIL import Image, ImageFilter
import streamlit as st
from save import st_render


st.header(":rainbow[ポスタリゼーション]")

# 色数の入力欄
colors = st.number_input(
    label="色数",
    min_value=2,
    max_value=256,
    value=256,
    step=1,
    key="image_colors"
)

# 画像がアップロードされている場合
if "image_upload" in st.session_state:
    img = st.session_state.image_upload
    
    # 最頻値フィルタ
    mode_filter = ImageFilter.ModeFilter(size=7)

    # フィルタ画像
    filtered = img.filter(mode_filter)

    # ポスタリゼーション画像
    poster = filtered.quantize(colors=colors)
    poster.filename = img.filename
    st.image(poster)

    st_render(poster)
