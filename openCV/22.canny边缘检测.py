import cv2
import numpy as np

img = cv2.resize(cv2.imread("../img/people1.jpg"), (450, 600))
# 需要指定最大值和最小值
new_img = cv2.Canny(img, 70, 150)
cv2.imshow("img", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
