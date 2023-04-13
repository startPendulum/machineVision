import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("../img/1.png")

# 用matplotlib画直方图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.hist(gray.ravel(), bins=256, range=[0, 255])
plt.show()

# calcHist接收图像数组
hist_b = cv2.calcHist([img], [0], None, [256], [0, 255])
hist_g = cv2.calcHist([img], [1], None, [256], [0, 255])
hist_r = cv2.calcHist([img], [2], None, [256], [0, 255])

# 画直方图
plt.plot(hist_b, color="b", label="blue")
plt.plot(hist_g, color="g", label="green")
plt.plot(hist_r, color="r", label="red")
plt.legend()
plt.show()
