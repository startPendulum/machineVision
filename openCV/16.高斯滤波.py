import cv2
import numpy as np

# 高斯滤波使卷积核变得符合高斯分布，即越中间的数越大
# 高斯滤波适合处理有白色噪点的图像，去噪
img = cv2.resize(cv2.imread("../img/zaodian.jpg"), (600, 600))
new_img = cv2.GaussianBlur(img, (5, 5), 100)
cv2.imshow("GaussianBlur", np.hstack((img, new_img)))
cv2.waitKey(0)
cv2.destroyAllWindows()
