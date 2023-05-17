import cv2
import cv2.dnn
import numpy as np

img = cv2.imread("../img/coin.jpg")
img = cv2.resize(img, (500, 700))

# 读入模型
net = cv2.dnn.readNetFromCaffe()

# 把图片变成tensor
blob = cv2.dnn.blobFromImage(img)

# 把图片给网络
net.setInput(blob)

# 预测
net.forward()
