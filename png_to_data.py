# %%
import cv2
import numpy as np

# 画像の読み込み
img = cv2.imread("./モビリタ_20240821/スクショ6.png")
print(type(img))


# %%
# グレースケール化
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 二値化(閾値100を超えた画素を255にする。
ret2, img_otsu = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU)
ret2

# %%


cv2.imwrite(img=img_otsu, filename="./page/test2.png")

# %%

# 輪郭線抽出
contours, hierarchy = cv2.findContours(img_otsu, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 全て白の画像を作成
img_blank = np.ones_like(img) * 255
# 輪郭だけを描画（黒色で描画）
img_contour_only = cv2.drawContours(img_blank, contours, -1, (0, 0, 0), 3)
# # 描画
# plt.imshow(cv2.cvtColor(img_contour_only, cv2.COLOR_BGR2RGB))
# plt.show()
cv2.imwrite(img=img_contour_only, filename="./page/test3.png")

# %%
