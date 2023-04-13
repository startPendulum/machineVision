import cv2
import numpy as np

img = cv2.resize(cv2.imread("../img/number.png"), (450, 600))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
contours, index = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

img_copy = img.copy()
# 画出轮廓
cv2.drawContours(img_copy, contours, -1, (0, 0, 255), thickness=2)
# 使用多边形逼近，近似轮廓
approx = cv2.approxPolyDP(contours[3], 20, closed=True)
# drawContours使用的是三维轮廓数组
cv2.drawContours(img_copy, [approx], -1, (0, 255, 0), thickness=1)

# 计算凸包
hull = cv2.convexHull(contours[3])
cv2.drawContours(img_copy, [hull], -1, (255, 0, 0), thickness=2)

cv2.imshow("img_copy", img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()
