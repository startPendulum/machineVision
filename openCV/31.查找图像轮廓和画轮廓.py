import cv2
import numpy as np

img = cv2.resize(cv2.imread("../img/people1.jpg"), (450, 600))

# 先变成黑白通道图片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 二值化,返回阈值和二值化的图
thresh, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
# 查找轮廓，findContours返回轮廓和层级
# contours是list,里面存放ndarray，每个ndarray表示一个轮廓
contours, index = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(index)

# 绘制轮廓会直接修改原图，如果想保持原图不变，建议copy一份
img_copy = img.copy()
cv2.drawContours(img_copy, contours, -1, (0, 0, 255), 2)

cv2.imshow("img_copy", img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()
