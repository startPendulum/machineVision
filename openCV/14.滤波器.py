import cv2
import numpy as np

img = cv2.resize(cv2.imread("../img/1.png"), (600, 600))

# 设置卷积核
# 模糊
# kernel = np.ones([5, 5]) / 25
# 锐化
# kernel = np.float32([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
# 突出轮廓
kernel = np.float32([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
new_img = cv2.filter2D(img, -1, kernel)
cv2.imshow("filter2d", np.hstack((img, new_img)))
cv2.waitKey(0)
cv2.destroyAllWindows()
