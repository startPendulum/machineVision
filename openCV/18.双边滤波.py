import cv2
import numpy as np

# 双边滤波可以起到美颜的效果
img = cv2.resize(cv2.imread("../img/people.jpg"),(450,600))
new_img = cv2.bilateralFilter(img, 12, sigmaColor=40, sigmaSpace=70)
cv2.imshow("bilateralFilter", np.hstack((img, new_img)))
cv2.waitKey(0)
cv2.destroyAllWindows()
