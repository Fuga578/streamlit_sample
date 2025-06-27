from pathlib import PurePath
from janome.tokenizer import Tokenizer
from wordcloud import WordCloud
import re


# 日本語フォントファイルパス
FONT_PATH = PurePath(__file__).parent / "data/ipaexm.ttf"

# IPA品詞ファイルパス
POS_ID_FILE = PurePath(__file__).parent / "data/pos-id.txt"

def get_tokens(text: str) -> list[tuple[str, str]]:
    """文章を単語（トークン）に分割します。
    
    Args:
        text (str): 文章
    
    list[tuple[str, str]]: トークン一覧（単語, 品詞）
    """
    
    sanitized = "".join(text.split())   # 空白除去
    
    tokenizer = Tokenizer()
    tokens = [(w.surface, w.part_of_speech) for w in tokenizer.tokenize(sanitized)]

    return tokens


def get_wordcloud(tokens: list[tuple[str, str]], pos_list: list[str]) -> "Image":
    """ワードクラウド画像を取得します。
    
    Args:
        tokens (list[tuple[str, str]]): トークン一覧（単語, 品詞）
        pos_list (list[str]):   検索する品詞のリスト
    
    Returns:
        Image: ワードクラウド画像
    """

    pos_joined = "|".join(pos_list) # 正規表現用の文字列作成 ["名詞", "動詞"] -> 名詞 | 動詞
    regexp = re.compile(f"^({pos_joined})")
    selected = [token[0] for token in tokens if regexp.search(token[1])]    # pos_listに該当するワードを抽出

    # {単語: カウント数}の辞書作成
    unique_words = list(set(selected))
    probs = {key: selected.count(key) for key in unique_words}

    # ワードクラウド画像作成
    word_cloud = WordCloud(
        font_path=FONT_PATH,
        background_color="lightgray",
        width=800,
        height=600,
        colormap="twilight",
    )
    img = word_cloud.fit_words(probs)

    return img.to_image()


def get_pos_ids(file: str = POS_ID_FILE) -> list[str]:
    """品詞リストを取得します。
    
    Args:
        file (str): 品詞ファイルパス
    
    Returns:
        list[str]: 品詞リスト
    """
    with open(file, encoding="utf-8") as fp:
        pos_ids = fp.readlines()
        pos_ids = [line.strip() for line in pos_ids]
    
    return pos_ids


if __name__ == "__main__":
    import sys
    from aozora_download import get_aozora_text
    from custom_timer import timer

    url = sys.argv[1]
    t = timer()
    text = get_aozora_text(url)
    tokens = get_tokens(text)
    img = get_wordcloud(tokens, ["名詞"])
    img.save("test.png")

    pos_ids = get_pos_ids()
    print(f"品詞リスト: {pos_ids}")
