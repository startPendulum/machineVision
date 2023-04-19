# 速度最快，可以实时检测，准确率最差

import cv2
import numpy

img = cv2.resize(cv2.imread("../img/number.png"), (450, 600))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 创建cv2对象
orb = cv2.ORB_create()

# 进行检测
kp = orb.detect(gray)

# 计算描述子
kp, des = orb.compute(img, kp)
cv2.drawKeypoints(gray, kp, img, (0, 0, 255))

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
