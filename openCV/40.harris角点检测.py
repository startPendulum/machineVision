import cv2
import numpy as np

img = cv2.resize(cv2.imread("../img/number.png"), (450, 600))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 返回角点响应
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

# 设定角点
# 大于0.01倍最大值的点认为是角点，这个倍数可以调
img[dst > (0.01 * dst.max())] = [0, 0, 255]

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
