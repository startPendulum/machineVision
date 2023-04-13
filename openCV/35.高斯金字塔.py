import cv2
import numpy as np

img = cv2.imread("../img/number.png")

# 高斯金字塔向下采样会使图像缩小1/4，横向缩小1/2，纵向缩小1/2
# 高斯金字塔取样不可逆
img_down = cv2.pyrDown(img)

# 高斯金字塔项上采样使图像扩大四倍，缺失像素用0填充
img_up = cv2.pyrUp(img)

cv2.imshow("img", img)
cv2.imshow("img_down", img_down)
cv2.imshow("img_up", img_up)
cv2.waitKey(0)
cv2.destroyAllWindows()
