import cv2
import numpy as np

img = cv2.resize(cv2.imread("../img/book.jpg"), (450, 600))
# 先变成黑白通道图片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 二值化,返回阈值和二值化的图
thresh, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
# 查找轮廓，findContours返回轮廓和层级
# contours是list,里面存放ndarray，每个ndarray表示一个轮廓
result,contours=cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(result)