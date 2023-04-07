import cv2
import numpy as np

img1 = cv2.imread("../img/1.png")[100:700, 100:700]
img2 = cv2.imread("../img/3.png")[100:700, 100:700]

# 非操作 相当于255-图片每个像素值
img1_not = cv2.bitwise_not(img1)
cv2.imshow("img1_not", np.hstack((img1, img1_not)))

# 与操作 相当于每个图片对应像素相与 与后的值比两个值都小一点
img1 = img1[200:600, 200:600]
img2 = img2[200:600, 200:600]
img_and = cv2.bitwise_and(img1, img2)
cv2.imshow("img_and", np.hstack((img1, img2, img_and)))

# 或操作 相当于每个图片对应像素相或 或后的值比两个值都大一点
img_or = cv2.bitwise_or(img1, img2)
cv2.imshow("img_or", np.hstack((img1, img2, img_or)))

# 异或操作 相当于每个图片对应像素相异或 异或后的值比两个值都小很多
img_xor = cv2.bitwise_xor(img1, img2)
cv2.imshow("img_xor", np.hstack((img1, img2, img_xor)))

cv2.waitKey(0)
cv2.destroyAllWindows()
