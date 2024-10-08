# %%
import cv2
import pandas as pd

# %%
# データ読み込み
img = cv2.imread("./モビリタ_20240821/スクショ.png")


ksize = 3
# 中央値フィルタ
img_mask = cv2.medianBlur(img, ksize)


# グレースケール化と2値化
img_gray = cv2.cvtColor(img_mask, cv2.COLOR_BGR2GRAY)
# 二値化(閾値100を超えた画素を255にする。
ret2, img_otsu = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU)

cv2.imwrite(filename="./test.png", img=img_otsu)



# %%
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

df.to_csv("./test.csv")

# %%
# データの可視化
import pandas as pd
import seaborn as sns

df = pd.read_csv("./test.csv")
# %%
df.reset_index(inplace=True)

# %%
df = df[["x", "y"]]
df

dff = df.groupby(["x"]).mean().reset_index()

# dff["y"] = dff["y"]/
dff["x"] = dff["x"] /  * 250

# %%
sns.scatterplot(data=dff, x="x", y="y")
# %%
print(len(img_gray))
# %%

dff.to_csv("test2.csv")

# %%
dff = dff.set_index("x")
# %%
dfff = dff.resample("s")
dfff
# %%
dff
# %%
