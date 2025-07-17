import time
import whisper


def prepare_model(size: str = "base") -> any:
    """テキスト起こしモデル（whisper）を取得します。"""
    model = whisper.load_model(size)
    return model


def transcibe(model: any, audio_file: str, lang: str) -> str:
    """音声ファイルを読み込み、テキスト起こし結果を取得します。"""
    result = model.transcribe(audio_file, fp16=False, language=lang)
    return result["text"]


def performance():
    """モデルの性能を評価します。"""
    start_time = time.perf_counter()

    def get_stats(text: str, lang: str):
        """性能取得処理"""
        end_time = time.perf_counter()
        duration = end_time - start_time
        
        # 英語
        if lang == "en":
            wps = len(text.split()) / duration
            unit = "words/s"
        # 日本語
        else:
            wps = len(text) / duration
            unit = "文字/s"

        return {
            "duration": duration,
            "wps": wps,
            "unit": unit
        }
    
    return get_stats
    
