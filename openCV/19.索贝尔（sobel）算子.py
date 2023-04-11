import cv2
import numpy as np

#  算子主要用作边缘检测
img = cv2.resize(cv2.imread("../img/people.jpg"), (450, 600))
# sobel算子要分别计算x,y的梯度
# 计算x轴方向的梯度
dx = cv2.Sobel(img, cv2.CV_64F, dx=1, dy=0, ksize=5)
dy = cv2.Sobel(img, cv2.CV_64F, dx=0, dy=1,ksize=5)
dst = cv2.add(dx, dy)
# 计算y轴方向的梯度
cv2.imshow("img", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
