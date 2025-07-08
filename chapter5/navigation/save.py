from io import BytesIO
from pathlib import PurePath
from PIL import Image, ImageFile


def get_extensions() -> list[str]:
    """Pillowで使用できる拡張子一覧を取得します。
    
    Returns:
        list[str]: 拡張子一覧
    """
    return list(Image.registered_extensions().keys())


def image_to_bytes(
    pil_image: ImageFile.ImageFile,
    extension: str = ".png"
) -> tuple[str, bytes]:
    """画像を指定拡張子に変更した（ファイル名, バイナリデータ）を取得します。"""
    
    filename = PurePath(pil_image.filename).with_suffix(extension).name
    buf = BytesIO()
    try:
        pil_image.save(buf, format=Image.registered_extensions()[extension])
        buf_bytes = buf.getvalue()
    except Exception as e:
        buf_bytes = None

    return (filename, buf_bytes)


def st_render(pil_image: ImageFile.ImageFile) -> None:
    """サイドバーに拡張子選択ラジオボタン、ダウンロードボタンを表示します。"""
    import streamlit as st

    # サイドバー
    with st.sidebar:
        st.divider()    # 水平線

        # ポップオーバー（開閉式コンテナ）
        with st.popover("画像フォーマットを選択"):
            # 扱える拡張子一覧を表示（ラジオボタン）
            extension = st.radio(
                label="変換先フォーマット",
                options=get_extensions(),
                index=None,
                horizontal=True
            )

        # 拡張子が選択されている場合
        if extension:
            filename, buffer = image_to_bytes(pil_image, extension)
            if buffer is None:
                st.error(f"{extension}への変換ができません。")
            else:
                st.download_button(
                    f'`{extension}` としてダウンロード（`{filename}`）',
                    buffer,
                    file_name=filename
                )
