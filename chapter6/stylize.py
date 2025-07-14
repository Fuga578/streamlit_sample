import cv2


def stylize(img_bgr, sigma_s=60, sigma_r=0.45) -> any:
    """画像をスタイライゼーション（アニメ絵化）します。
    
    Args:
        img_bgr (any): BGR画像
        sigma_s (int): スタイライゼーション度合い
        sigma_r (float): 輪郭のキープ度合い
    """
    stylized = cv2.stylization(img_bgr, sigma_s=sigma_s, sigma_r=sigma_r)
    return stylized
