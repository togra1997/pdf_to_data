# %%
import cv2
import numpy as np

# https://qiita.com/Yuzu2yan/items/056778f2707d6931519e
# 赤色は２つの領域にまたがります！！
# np.array([色彩, 彩度, 明度])
# 各値は適宜設定する！！

# 赤
LOW_COLOR1 = np.array([0, 50, 50])  # 各最小値を指定
HIGH_COLOR1 = np.array([6, 255, 255])  # 各最大値を指定
LOW_COLOR2 = np.array([174, 50, 50])
HIGH_COLOR2 = np.array([180, 255, 255])


def Clahe_red(img_name):
    img = cv2.imread(img_name)  # 画像を読み込む

    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)  # RGB => YUV(YCbCr)
    clahe = cv2.createCLAHE(
        clipLimit=2.0, tileGridSize=(8, 8)
    )  # claheオブジェクトを生成
    img_yuv[:, :, 0] = clahe.apply(img_yuv[:, :, 0])  # 輝度にのみヒストグラム平坦化
    img = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)  # YUV => RGB

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # BGRからHSVに変換

    bin_img1 = cv2.inRange(hsv, LOW_COLOR1, HIGH_COLOR1)  # マスクを作成
    bin_img2 = cv2.inRange(hsv, LOW_COLOR2, HIGH_COLOR2)
    mask = bin_img1 + bin_img2  # 必要ならマスクを足し合わせる
    masked_img = cv2.bitwise_and(img, img, mask=mask)  # 元画像から特定の色を抽出
    cv2.imwrite("./page/out_img.jpg", masked_img)  # 書き出す


# https://python.joho.info/opencv/opencv-color-detection/

# 青
LOW_COLOR1 = np.array([127, 50, 50])  # 各最小値を指定
HIGH_COLOR1 = np.array([177, 255, 255])  # 各最大値を指定


def Clahe_blue(img_name):
    img = cv2.imread(img_name)  # 画像を読み込む

    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)  # RGB => YUV(YCbCr)
    clahe = cv2.createCLAHE(
        clipLimit=2.0, tileGridSize=(8, 8)
    )  # claheオブジェクトを生成
    img_yuv[:, :, 0] = clahe.apply(img_yuv[:, :, 0])  # 輝度にのみヒストグラム平坦化
    img = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)  # YUV => RGB

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # BGRからHSVに変換

    bin_img1 = cv2.inRange(hsv, LOW_COLOR1, HIGH_COLOR1)  # マスクを作成

    mask = bin_img1  # 必要ならマスクを足し合わせる
    masked_img = cv2.bitwise_and(img, img, mask=mask)  # 元画像から特定の色を抽出
    cv2.imwrite("./page/out_img.jpg", masked_img)  # 書き出す
    cv2.imwrite("./page/out_img2.jpg", bin_img1)


if __name__ == "__main__":
    Clahe_blue("./モビリタ_20240821/スクショ5.png")  # ファイル名を入力


# %%
# https://www.peko-step.com/html/hsv.html
# HVSの色相環計算
target = 250
score = target / 360 * 255
print(f"{score=}")
# %%
