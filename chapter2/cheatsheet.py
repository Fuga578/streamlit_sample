import streamlit as st


# アイコン
icon = "https://upload.wikimedia.org/wikipedia/commons/4/48/Markdown-mark.svg"

# ページ設定
st.set_page_config(
    page_title="Markdown Cheatsheet",
    page_icon=icon,
    layout="wide",
)

st.logo(icon, link="https://github.github.com/gfm/")
st.markdown("### Markdown チートシート")

left, right = st.columns(2)

# 画面左部
left.markdown("**:memo: テキスト書式**")
left.markdown("""
    要素 | :green[HTML] | 要素
    ---|---|---
    見出し | `<h1>~<h6>` | `## 見出し`
    太字 | `<strong>` | `**太字**`
    斜体 | `<em>` | `*斜体*`
    取り消し | `<strike>` | `~~取り消し~~`
    引用 | `<blockquote>` | `> 引用文`
    コード | `<code>` | ``
    区切り線 | `<hr>` | `---`
    改行 | `<br>` | `  （半角スペース2つ）`
    Esc |  | `\\`
""")

# 画面右部
with right:
    st.markdown("**:material/format_list_bulleted: リスト**")
    st.markdown("""
        要素 | :green-background[HTML] | 用法
        ---|---|---
        順序なし | `<ul> <li>` | `- `
        順序あり | `<ol> <li>` | `1. `
    """)

    with st.expander("**リンク**", icon="🔗"):
        st.markdown("""
            要素 | HTML | 用法
            ---|---|---
            リンク | `<a href=...>` | `[文字列](url)`
            画像 | `<img scr=...>` | `[代替テキスト](url)`
        """)

with right.expander("**表**", icon=":material/table:", expanded=True):
    st.markdown("""```
        ヘッダ1 | ヘッダ2 | ヘッダ3
        ---|---|---
        (1, 1) | (1, 2) | (1, 3)
        (2, 1) | (2, 2) | (2, 3)
        (3, 1) | (3, 2) | (3, 3)
    ```""")

# st.markdown("""
#     - aaa
#     - bbb
#     1. aaa
#     2. aaa
#     2. aaa
# """)
