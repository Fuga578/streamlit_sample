from pathlib import PurePath
from Eliza import eliza


# データセットファイルパス
FILE = PurePath(__file__).parent / "./Eliza/doctor.txt"


class Doctor:
    """イライザを利用したドクタークラスです。
    
    Args:
        file (str): データセットファイルパス

    Attributes:
        doctor (eliza.Eliza): イライザ
    """

    def __init__(self, file: str = FILE):
        self.doctor = eliza.Eliza()
        self.doctor.load(file)

    def initial(self) -> str:
        """起動時のメッセージを取得します。"""
        return self.doctor.initial()
    
    def respond(self, text: str) -> str:
        """質問に対して返答を行います。"""
        return self.doctor.respond(text)
    
    def final(self) -> str:
        """終了時のメッセージを取得します。"""
        return self.doctor.final()


if __name__ == "__main__":
    doctor = Doctor()
    print(doctor.initial())

    while True:
        text = input("> ")
        if text.lower().startswith("quit"):
            break
        print(doctor.respond(text))

    print(doctor.final())
