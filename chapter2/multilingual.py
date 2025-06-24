import streamlit as st
from acceptlang import parse_accept_lang_header


# 言語ごとのメッセージ
_MESSAGES = {
    "ja": "日本語 Strealit",
    "en": "英語 Strealit",
    "es": "スペイン語 Strealit",
    "cn": "中国語 Streamlit",
    "unknown": "不明 Streamlit"
}

def find_language(accept_language_parsed):
    for lang in accept_language_parsed:
        if lang.name in _MESSAGES:
            return lang.name
    return "unknown"

# URLのクエリから"lang"の項目を取得（未指定の場合はNone）
lang = getattr(st.query_params, "lang", None)

# クエリから"lang"項目が取得できない場合
# Accept-Languageリクエストヘッダから優先度が高い言語を抽出
if lang not in _MESSAGES:
    accept_language_value = st.context.headers["accept-language"]
    accept_language_parsed = parse_accept_lang_header(accept_language_value)
    st.write(accept_language_parsed)
    lang = find_language(accept_language_parsed)

st.markdown(f"## {_MESSAGES[lang]} :green[{lang}]")

st.write("`st.query_params`:")
st.write(st.query_params)
st.write("`st.context.headers`:")
st.write(st.context.headers)
