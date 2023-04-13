import cv2
import numpy as np

img = cv2.resize(cv2.imread("../img/number.png"), (450, 600))
# 拉普拉斯金字塔 新图像=原图像-pyrUp(pyrDown(img))

new_img = img - cv2.pyrUp(cv2.pyrDown(img))

cv2.imshow("new_img", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
