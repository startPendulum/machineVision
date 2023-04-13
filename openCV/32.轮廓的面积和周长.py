import cv2
import numpy as np

img = cv2.resize(cv2.imread("../img/number.png"), (450, 600))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
contours, index = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
    # 计算轮廓面积
    area = cv2.contourArea(c)
    print("area:", area)

    # 计算轮廓周长
    perimeter = cv2.arcLength(c, closed=True)
    print("perimeter:", perimeter)
