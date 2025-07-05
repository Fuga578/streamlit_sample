import pykakasi


class Rubify:
    """ルビ振りボットクラスです。"""

    def __init__(self):
        self.kks = pykakasi.kakasi()

    def initial(self) -> str:
        """最初のセリフを取得します。"""
        return "ぼくはルビふり<ruby>君<rt>くん</ruby>です。"
    
    def final(self) -> str:
        """最後のセリフを取得します。"""
        return "また<ruby>寄<rt>よ</ruby>ってくださいな。"
    
    def respond(self, text: str) -> str:
        """入力文に対して、ルビを振った文字列を返します。"""

        # ルビ振り結果を取得
        results = self.kks.convert(text)

        words = []
        for result in results:
            orig = result["orig"]
            yomi = result["hira"]
            kana = result["kana"]
            
            # 文字がひらがな・カタカナ読みと一致した場合、そのまま
            if orig == yomi or orig == kana:
                words.append(orig)
            # 一致しない場合、ルビ振り
            else:
                rubied = f"<ruby>{orig}<rt>{yomi}</ruby>"
                words.append(rubied)
        
        return "".join(words)


if __name__ == "__main__":

    rubify = Rubify()

    # 初期メッセージ
    print(rubify.initial())

    # ルビ振り
    while True:
        text = input("> ")
        if text.lower().startswith("quit"):
            break
        print(rubify.respond(text))

    # 終了メッセージ
    print(rubify.final())
