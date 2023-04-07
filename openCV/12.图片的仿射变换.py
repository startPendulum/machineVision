import cv2
import numpy as np

img = cv2.resize(cv2.imread("../img/1.png"), (500, 500))
h, w, ch = img.shape
# M是仿射变换的矩阵
# 平移
M = np.float32([
    [1, 0, 200],
    [0, 1, 100]
])
# dsize是输出图片大小，先宽度后高度，opencv中都是这样
new_img1 = cv2.warpAffine(img, M, dsize=(w, h))
cv2.imshow("affine", new_img1)

# 旋转
# 获取变换矩阵
# cv2.getRotationMatrix2D(旋转中心，旋转角度，缩放)
M_rotate = cv2.getRotationMatrix2D((100, 100), 60, 2)
new_img2 = cv2.warpAffine(img, M_rotate, dsize=(w, h))
cv2.imshow("rotate", new_img2)

# 通过三点确定变换矩阵，需要原始图片的三个点坐标和变换之后的三个对应坐标
src = np.float32([
    [200, 100],
    [300, 100],
    [200, 300]
])
dst = np.float32([
    [100, 150],
    [360, 200],
    [280, 120]
])
M2 = cv2.getAffineTransform(src, dst)
new_img3 = cv2.warpAffine(img, M2, (w, h))
cv2.imshow("rotate2", new_img3)


cv2.waitKey(0)
cv2.destroyAllWindows()
