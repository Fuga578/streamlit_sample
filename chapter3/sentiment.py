from transformers import pipeline


# 感情分析モデル
MODEL = 'Mizuiro-sakura/luke-japanese-large-sentiment-analysis-wrime'

# 感情の種類
SENTIMENTS = '喜び、悲しみ、期待、驚き、怒り、恐れ、嫌悪、信頼'.split('、')


def get_model(model: any = MODEL) -> any:
    """hugging faceからモデルを取得します。
    
    Args:
        model (any): モデル名
    
    Returns:
        any: モデル
    """

    model = pipeline("sentiment-analysis", model=model)
    return model


def get_sentiment(model: any, sentence: str) -> str:
    """指定の文の感情を取得します。
    
    Args:
        model (any):    感情分析モデル
        sentence(str):  文
    
    Retunrs:
        str: 感情
    """

    results = model(sentence)   # results: [{'label': 'LABEL_0', 'score': 0.9317873120307922}]
    label_number = int(results[0]["label"][-1:])
    return SENTIMENTS[label_number]


if __name__ == "__main__":
    import sys
    from aozora_download import get_aozora_text, parse_text_into_sentences

    # 文章取得
    url = sys.argv[1]
    text = get_aozora_text(url)
    sentences = parse_text_into_sentences(text)

    # モデル取得
    model = get_model()

    # 感情取得
    emotions = [get_sentiment(model, sentence) for sentence in sentences]

    # {感情: カウント数}の辞書作成
    stats = {e: emotions.count(e) for e in SENTIMENTS}
    print(stats)

    

