import cv2
import numpy as np

img = cv2.imread("../img/book.jpg")

src = np.float32([[700, 100], [2400, 200], [1100, 3000], [3000, 2920]])
dst = np.float32([[0, 0], [2400, 0], [0, 3000], [2400, 3000]])
h, w, ch = img.shape
# 获取变换矩阵
# 需要原来四个点坐标和对应变化后的坐标
M = cv2.getPerspectiveTransform(src, dst)
# 做透视变换
new_img = cv2.warpPerspective(img, M, (2400,3000))
new_img=cv2.resize(new_img,(600,700))
cv2.imshow("new_img", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
