import cv2
import numpy as np
import requests
import streamlit as st


# 画像の最大幅
MAX_WIDTH = 1024


def limit_size(img: np.ndarray, max_width=MAX_WIDTH) -> np.ndarray:
    """画像サイズを制限します。"""
    if max_width is None:
        return img
    
    # 画像の縦横大きい方を制限するための比率
    factor = min([max_width / wh for wh in img.shape])
    if factor < 1:
        img = cv2.resize(img, dsize=None, fx=factor, fy=factor)
    
    return img


def bytes_to_ndarray(buf: bytes) -> np.ndarray:
    """画像バイナリデータをnp.ndarrayに変換します。"""
    arr = np.frombuffer(buf, np.uint8)
    img_bgr = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    return img_bgr


def uploaded_to_ndarray(uploaded, max_width=MAX_WIDTH) -> np.ndarray:
    """streamlitのUploadedFileをnp.ndarrayに変換します。"""
    buf = uploaded.getvalue()
    img = bytes_to_ndarray(buf)
    if img is None:
        raise Exception("Failed to read UploadedFile.")
    return limit_size(img, max_width)


def url_to_ndarray(url: str, max_width=MAX_WIDTH) -> np.ndarray:
    """URLで指定した画像をnp.ndarrayに変換します。"""
    resp = requests.get(url, headers={'User-agent': 'MyRequest'})
    if resp.status_code != 200:
        raise Exception('Failed to read URL.')

    img = bytes_to_ndarray(resp.content)

    return limit_size(img, max_width)
