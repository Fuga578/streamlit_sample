import streamlit as st
from face_detection import prepare_model, detect
from stylize import stylize
from draw_faces import draw_rectangles, draw_smilys
from to_ndarray import uploaded_to_ndarray, url_to_ndarray


# 画像アップロード項目
OPTIONS = {
    'camera': {
        'name': 'カメラ',
        'text': 'スナップショットを撮ってください。',
        'icon': ':material/photo_camera:',
        'image': False,
        'input': lambda: st.camera_input(label='ダミー', label_visibility='hidden'),
        'process': uploaded_to_ndarray
    },
    'url': {
        'name': 'URL',
        'text': '画像への URL を入力してください。',
        'icon': ':material/photo_library:',
        'image': True,
        'input': lambda: st.text_input('ダミー', label_visibility='hidden',
                    value=None, placeholder='Enter URL for an image.'),
        'process': url_to_ndarray
    }
}

@st.cache_resource
def get_model() -> any:
    """顔検出モデルを取得します。"""
    model = prepare_model()
    return model


st.header("カメラ映像処理")

# カメラ or URL ラジオボタン
im = st.radio(
    label="ダミー",
    label_visibility="hidden",
    options=OPTIONS.keys(),
    horizontal=True
)

# 選択項目取得
options = OPTIONS[im]

# タブ
camera, face, anime = st.tabs([options["name"], "顔検出", "アニメ絵"])

# 画像アップロード
with camera:
    snapshot = options["input"]()

# 画像がアップロードされていない場合、メッセージ表示
if snapshot is None:
    face.info(body=options["text"], icon=options["icon"])
    anime.info(body=options["text"], icon=options["icon"])

# 画像がアップロードされた場合、処理実行
else:
    # 変換画像取得
    img = options["process"](snapshot, max_width=1024)
    
    # 画像表示
    if options["image"]:
        camera.image(snapshot)

    # 顔検出
    with face:
        over = st.radio("顔領域の位置", options=["スマイリー", "矩形"], horizontal=True)
        model = get_model()
        rectangles = detect(model, img)

        if over == "矩形":
            faces = draw_rectangles(img, rectangles)
        else:
            faces = draw_smilys(img, rectangles)
        
        st.image(faces, channels="BGR")
        st.caption(f"顔検出(`{len(rectangles)}`個発見)")

    # アニメ絵
    with anime:
        stylized = stylize(img)
        st.image(stylized, caption="アニメ絵化", channels="BGR")
