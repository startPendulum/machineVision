import cv2
import numpy as np

# 中值滤波对均匀的噪声处理效果比较好
img = cv2.resize(cv2.imread("../img/zaodian.jpg"), (600, 600))

new_img = cv2.medianBlur(img, 5)
cv2.imshow("new_img", np.hstack((img, new_img)))
cv2.waitKey(0)
cv2.destroyAllWindows()