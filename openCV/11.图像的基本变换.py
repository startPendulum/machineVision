import cv2
import numpy as np

img1 = cv2.imread("../img/1.png")
img2 = cv2.imread("../img/3.png")

# 缩放 大小先宽度再高度
# 缩小
small_img1 = cv2.resize(img1, (600, 400))
cv2.imshow("smaller", small_img1)
# 放大
big_img11 = cv2.resize(img1, (1200, 800), interpolation=cv2.INTER_NEAREST)  # 效果最差
big_img12 = cv2.resize(img1, (1200, 800), interpolation=cv2.INTER_LINEAR)  # 默认，效果适中
big_img13 = cv2.resize(img1, (1200, 800), interpolation=cv2.INTER_CUBIC)  # 二次线性
big_img14 = cv2.resize(img1, (1200, 800), interpolation=cv2.INTER_AREA)  # 效果最好，计算时间最长
cv2.imshow("bigger1", big_img11)
cv2.imshow("bigger2", big_img12)
cv2.imshow("bigger3", big_img13)
cv2.imshow("bigger4", big_img14)
# 按x,y比例缩放
new_img1 = cv2.resize(img1, dsize=None, fx=0.2, fy=0.5)
cv2.imshow("xy", new_img1)

# 翻转
# flipCode=0上下翻转
flip_img11 = cv2.flip(small_img1, 0)
# flipCode>0左右翻转
flip_img12 = cv2.flip(small_img1, 1)
# flipCode<0上下左右翻转
flip_img13 = cv2.flip(small_img1, -1)
cv2.imshow("flip", np.hstack((small_img1, flip_img11, flip_img12, flip_img13)))

# 旋转
# cv2.ROTATE_90_CLOCKWISE 顺时针90度
# cv2.ROTATE_180 180度
# cv2.ROTATE_90_COUNTERCLOCKWISE 逆时针90度
rotate_img11 = cv2.rotate(small_img1, rotateCode=cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("rotate", rotate_img11)

cv2.waitKey(0)
cv2.destroyAllWindows()
