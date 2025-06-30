import streamlit as st
from aozora_download import get_aozora_text, parse_text_into_sentences
from word_cloud import get_tokens, get_pos_ids, get_wordcloud
from sentiment import get_model, get_sentiment, SENTIMENTS


@st.cache_data
def retrieve_aozora(url: str) -> str:
    """青空文庫の文章を抽出します。
    
    Args:
        url (str): 青空文庫のzipファイルURL または zipファイルパス
    
    Returns:
        str:    テキスト

    Notes:
        cache_dataで、セッション（ブラウザ）単位でキャッシュを保持します。
    """
    print(f'Retrieving Aozora: {url}.')
    return get_aozora_text(url)


@st.cache_data
def process_tokens(text: str) -> list[tuple[str, str]]:
    """文章からトークン一覧を作成します。
    
    Args:
        text (str): 文章
    
    Returns:
        list[tuple[str, str]]: トークン一覧（単語, 品詞）

    Notes:
        cache_dataで、セッション（ブラウザ）単位でキャッシュを保持します。
    """
    print(f'Generating tokens from the text.')
    return get_tokens(text)


@st.cache_data
def prepare_pos_ids() -> list[str]:
    """品詞リストを取得します。

    Returns:
        list[str]: 品詞リスト
    
    Notes:
        cache_dataで、セッション（ブラウザ）単位でキャッシュを保持します。
        （cache_resourceの方が適している）
    """
    print(f'Retriving POS_IDs.')
    return get_pos_ids()


@st.cache_resource
def prepare_sentiment_model() -> any:
    """感情分析用モデルを取得します。

    Returns:
        any: モデル
    
    Notes:
        cache_resourceにより、サーバ単位でキャッシュを保持します。
    """
    print(f'Preparing the model.')
    return get_model()


# タブ
tab_text, tab_wc, tab_sentiment = st.tabs(["テキスト", "ワードクラウド", "感情分析"])

# テキストタブ
with tab_text:
    # URL入力欄
    aozora_url = st.text_input("**青空文庫 Zipファイル URL**", value=None)

# ワードクラウドタブ
with tab_wc:
    # 品詞 複数選択項目
    pos_ids = prepare_pos_ids()
    pos_list = st.multiselect("品詞", pos_ids, default="名詞")

# 感情分析タブ
with tab_sentiment:
    trace_on = st.checkbox("文単位の感情", value=False)
    graph = st.empty()
    with graph:
        bar = st.progress(value=0.0, text='計算中')

# URL入力があった場合
if aozora_url is not None:

    # テキスト取得
    try:
        text = retrieve_aozora(aozora_url)
    except Exception as e:
        st.error(
            f'`{aozora_url}`が取得できない、あるいはそのZipが正しく解凍できませんでした。',
            icon=':material/network_locked:')
        st.exception(e)
        st.stop()
    
    # 取得したテキストを表示
    with tab_text:
        print(text)
        st.markdown(text.replace('\n', '\n\n'))

    # ワードクラウド画像を表示
    with tab_wc:
        tokens = process_tokens(text)
        img = get_wordcloud(tokens, pos_list)
        st.image(img, width=800)

    # 感情解析結果表示
    with tab_sentiment:
        pipe = prepare_sentiment_model()
        sentences = parse_text_into_sentences(text)
        sentiments = {key: 0 for key in SENTIMENTS}

        for idx, sentence in enumerate(sentences):
            emotion = get_sentiment(pipe, sentence)
            bar.progress(value=idx/len(sentences), text='計算中')
            sentiments[emotion] = sentiments[emotion] + 1

            if trace_on is True:
                st.markdown(f'{sentence} ==> {emotion}')

        graph.bar_chart(sentiments)
