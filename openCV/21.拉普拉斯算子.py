import cv2
import numpy as np

img = cv2.resize(cv2.imread("../img/people1.jpg"), (450, 600))
# 拉普拉斯算子对有噪声的图片效果不好，其余效果最好
new_img = cv2.Laplacian(img, -1, ksize=3)
cv2.imshow("img", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
