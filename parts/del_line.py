# 余計な線を消す

import cv2
import numpy as np

img = cv2.imread("./モビリタ_20240821/スクショ5.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ksize = 7
# 中央値フィルタ
img_mask = cv2.medianBlur(gray, ksize)
# 二値化(閾値100を超えた画素を255にする。
ret2, img_otsu = cv2.threshold(img_mask, 0, 255, cv2.THRESH_OTSU)
gray2 = cv2.bitwise_not(gray)
lines = cv2.HoughLinesP(
    gray2, rho=1, theta=np.pi / 360, threshold=80, minLineLength=500, maxLineGap=5
)

for line in lines:
    x1, y1, x2, y2 = line[0]

    # 赤線を引く
    red_line_img = cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
    cv2.imwrite("calendar_mod3.png", red_line_img)
