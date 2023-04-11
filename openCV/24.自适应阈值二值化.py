import cv2
import numpy as np

img = cv2.resize(cv2.imread("../img/book.jpg"), (450, 600))

# 二值化操作是对灰度图像进行操作
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 自适应阈值二值化只会返回一个值，是二值化的图片
new_img = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 411, 0)

cv2.imshow("img", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
