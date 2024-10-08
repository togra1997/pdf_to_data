from pathlib import Path

import cv2
import pandas as pd

X_DEFAULT = 250
Y_DEFAULT = 100


def png2data(path: Path):
    # データ読み込み
    img = cv2.imread(path)

    ksize = 3
    # 中央値フィルタ
    img_mask = cv2.medianBlur(img, ksize)

    # グレースケール化と2値化
    img_gray = cv2.cvtColor(img_mask, cv2.COLOR_BGR2GRAY)
    # 二値化(閾値100を超えた画素を255にする。
    ret2, img_otsu = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU)
    # cv2.imwrite(filename="./test.png", img=img_otsu)

    # 画像の大きさを作成
    Y, X, _ = img.shape

    img.shape

    columns = ["x", "y"]
    df = pd.DataFrame(columns=columns, index=[0])

    # 横軸の点群検出
    # https://kitakantech.com/opencv-cv2imread/
    # グレースケール値の参考
    for i, index in enumerate(img_otsu):
        for j, cell in enumerate(index):
            if 0 == cell:
                d = {"y": i, "x": j}
                dff = pd.DataFrame(d, index=[0])
                df = pd.concat([df, dff])

    df.reset_index(inplace=True)
    df = df[["x", "y"]]

    dff = df.groupby(["x"]).mean().reset_index()

    # dff["y"] = dff["y"]/
    dff["x"] = dff["x"] / X * X_DEFAULT
    dff["y"] = dff["y"] / Y * Y_DEFAULT

    dff.to_csv(f"./{path.stem}.csv", index=False)


if __name__ == "__main__":
    path = Path("./モビリタ_20240821/スクショ.png")
    png2data(path=path)
