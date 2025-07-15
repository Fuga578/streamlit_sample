import cv2
from pathlib import PurePath


# caffe物体検出モデル
PARENT = PurePath(__file__).parent
PROTO_TEXT = PARENT / "data/deploy.prototxt"    # モデル構造
WEIGHT = PARENT / 'data/res10_300x300_ssd_iter_140000_fp16.caffemodel'  # 重みファイル
PROB_THRESH = 0.3   # 確信度閾値


def prepare_model():
    """caffe物体検出モデルを取得します。"""
    net = cv2.dnn.readNet(WEIGHT, PROTO_TEXT, "Caffe")
    return net


def detect(net: any, img: any, thresh: float = PROB_THRESH) -> list[tuple]:
    """指定の物体検出モデルで画像を解析し、バウンディングボックス座標を取得します。
    
    Args:
        net (any): モデル
        img (any): 画像
        thresh (float): 確信度閾値
    
    Returns:
        list[tuple]: バウンディングボックス座標（xmin, ymin, xmax, ymax）
    """

    # モデルの構造に合う形式に画像変換
    blob = cv2.dnn.blobFromImage(img, size=(300, 300), mean=(104, 177, 123))

    # 画像をモデルに読み込ませる
    net.setInput(blob)

    # 予測
    # shape = [1, 1, N, 7] -> [バッチサイズ, 検出結果セット数, 検出数, 検出項目]
    # [N, 7] -> [[固定値0, クラスラベル(faceの1のみ)], 確信度, xmin比率, ymin比率, xmax比率, ymax比率]
    pred = net.forward()

    # バウンディングボックス取得
    rectangles = []
    for i in range(pred.shape[2]):
        conf = pred[0, 0, i, 2] # 確信度抽出
        if conf > thresh:   # 閾値超えのみ保存
            xmin = int(pred[0, 0, i, 3] * img.shape[1])
            ymin = int(pred[0, 0, i, 4] * img.shape[0])
            xmax = int(pred[0, 0, i, 5] * img.shape[1])
            ymax = int(pred[0, 0, i, 6] * img.shape[0])

            rectangles.append((xmin, ymin, xmax, ymax))

    return rectangles
