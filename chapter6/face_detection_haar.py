from pathlib import PurePath
import cv2


PARENT = PurePath(__file__).parent
HAAR_FILE = PARENT / 'data/haarcascade_frontalcatface.xml'


def prepare_model():
    """Haar特徴検出モデルを取得します。（猫の正面画像用）"""
    cascade = cv2.CascadeClassifier(str(HAAR_FILE))
    return cascade


def detect(net, img, thresh=None):
    """Haar特徴検出モデルを用いて画像を解析し、バウンディングボックス座標を取得します。"""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.equalizeHist(gray, gray)    # コントラスト調整
    
    # 検出
    objects = net.detectMultiScale(gray)

    rectangles = []
    for rect in objects:
        x1, y1, w, h = rect
        rectangles.append((x1, y1, x1+w, y1+h))
        
    return rectangles
