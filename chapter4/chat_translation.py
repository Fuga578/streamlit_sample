from transformers import pipeline


# 翻訳モデル
MODEL = "Mitsua/elan-mt-bt-ja-en"


class Translator:
    """翻訳クラスです。
    
    Args:
        model (any): 翻訳モデル
    """

    def __init__(self, model: any = MODEL):
        self.pipe = pipeline("translation", model=model)

    def initial(self) -> str:
        """起動時のメッセージを取得します。"""
        return "MITUNA です。日英翻訳します。"
    
    def respond(self, text: str) -> str:
        """入力に対する応答を戻します。"""
        results = self.pipe(text, max_length=100, src_lang="ja", tgt_lang="en")
        return results[0]["translation_text"]
    
    def final(self) -> str:
        """終了時のメッセージを取得します。"""
        return "また寄ってね"
    

if __name__ == "__main__":
    translator = Translator()
    print(translator.initial())

    while True:
        text = input('> ')
        if text.lower().startswith('quit'):
            break
        print(translator.respond(text))

    print(translator.final())
