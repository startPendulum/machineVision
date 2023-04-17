import cv2
import numpy as np

img = cv2.resize(cv2.imread("../img/number.png"), (450, 600))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 创建sift对象
sift = cv2.xfeatures2d.SIFT_create()
# 检测角点
kp = sift.detect(gray)

# 绘制关键点
cv2.drawKeypoints(gray, kp, img, (0, 0, 255))

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
