import cv2
import numpy as np

img1 = cv2.imread("../img/1.png")
img2 = cv2.imread("../img/3.png")
# 融合的图片要相同大小
new_img1 = img1[200:600, 200:600]
new_img2 = img2[200:600, 200:600]
# 融合图片
new_img = cv2.addWeighted(new_img1, 0.5, new_img2, 0.5, 0)
cv2.imshow("new_img", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
