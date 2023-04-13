import cv2
import numpy as np

img = cv2.resize(cv2.imread("../img/number.png"), (450, 600))
img_copy = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
contours, index = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 最小外接矩形函数返回矩形的起始坐标，长宽，旋转角度
min_rect = cv2.minAreaRect(contours[1])
print(min_rect)
# 计算旋转矩形的四个坐标点，运算后的坐标是浮点数，但是画出需要整数
box = cv2.boxPoints(min_rect)
box = np.round(box).astype("int")
print(box)

cv2.drawContours(img_copy, [box], -1, (0, 0, 255), thickness=2)

# 最大外接矩形
# 可以直接画矩形把外接矩形画出来
x, y, w, h = cv2.boundingRect(contours[3])
cv2.rectangle(img_copy, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

cv2.imshow("img_copy", img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()
