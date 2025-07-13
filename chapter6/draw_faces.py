from pathlib import PurePath
import cv2


# 画像ファイルパス
PARENT = PurePath(__file__).parent
SMILY = PARENT / "data/smily-240.png"

# バウンディングボックス設定
RECT_COLOR = (255, 0, 0)    # （BGR）
RECT_LINE = 3


def draw_rectangles(img: any, rectangles: list[tuple]) -> any:
    """画像にバウンディングボックスを描画します。
    
    Args:
        img (any): 画像
        rectangles (list[tuple]): バウンディングボックス座標[（xmin, ymin, xmax, ymax）, ...]

    Returns:
        any: バウンディングボックスを描画した画像
    """
    ret_img = img.copy()

    for rect in rectangles:
        xmin, ymin, xmax, ymax = rect
        cv2.rectangle(ret_img, (xmin, ymin), (xmax, ymax), RECT_COLOR, RECT_LINE)

    return ret_img


def draw_smilys(img: any, rectangles: list[tuple]) -> any:
    """画像のバウンディングボックス座標にスマイル画像を描画します。
    
    Args:
        img (any): 画像
        rectangles (list[tuple]): バウンディングボックス座標[（xmin, ymin, xmax, ymax）, ...]

    Returns:
        any: スマイル画像描画した画像
    """
    ret_img = img.copy()
    smily = cv2.imread(SMILY)

    for rect in rectangles:
        xmin, ymin, xmax, ymax = rect

        # リサイズ
        smily_resized = cv2.resize(smily, (xmax - xmin, ymax - ymin))
        
        # 描画（ndarrayの要素を変換）
        ret_img [ymin:ymax, xmin:xmax] = smily_resized

    return ret_img