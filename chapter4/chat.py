import streamlit as st
from chat_ruby import Rubify
from chat_eliza import Doctor
from chat_translation import Translator


def on_select():
    """選択時にセッションから表示用文字列を削除します。"""
    del st.session_state["transactions"]

# セッションに「ルビ振り」を追加
if "ルビ振り" not in st.session_state:
    st.session_state["ルビ振り"] = Rubify()

# セッションに「セラピー」を追加
if "セラピー" not in st.session_state:
    st.session_state["セラピー"] = Doctor()

# セッションに「日英通訳」を追加
if "日英通訳" not in st.session_state:
    st.session_state["日英通訳"] = Translator()

# セッションに表示用文字列を追加
if "transactions" not in st.session_state:
    st.session_state["transactions"] = []

# 選択項目
options = ["ルビ振り", "セラピー", "日英通訳"]

# サイドバー
with st.sidebar:
    st.header("チャットサービス")
    selected = st.selectbox(
        label="サービスを選んでください",
        options=options,
        index=0,
        on_change=on_select
    )

# 選択に応じてチャットボットを取得
chat = st.session_state[selected]
st.html(f"【{chat.initial()}】")

# 入力
text = st.chat_input()
if text:
    response = chat.respond(text)
    st.session_state["transactions"].append(text)   # ユーザ入力を保存
    st.session_state["transactions"].append(f"{response}")    # レスポンスを保存

# 履歴を表示
# for show in st.session_state["transactions"]:
#     st.html(show)

for index, message in enumerate(st.session_state["transactions"]):
    # ユーザ入力
    if index % 2 == 0:
        with st.chat_message("user"):
            st.html(message)
    # チャットボット応答
    else:
        with st.chat_message("ai"):
            st.html(message)
