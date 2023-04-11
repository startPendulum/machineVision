import cv2
import numpy as np

img = cv2.resize(cv2.imread("../img/number.png"), (450, 600))

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# 顶帽运算=原图-开运算，相当于获取到去除的噪声
tophat_img = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel, iterations=2)

# 黑帽运算=闭运算-原图
blackhat_img = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel, iterations=1)

cv2.imshow("tophat_img", tophat_img)
cv2.imshow("blackhat_img", blackhat_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
