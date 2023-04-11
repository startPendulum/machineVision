import cv2
import numpy as np

img = cv2.resize(cv2.imread("../img/number.png"), (450, 600))

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
# 梯度=膨胀-腐蚀
new_img = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel, iterations=1)

cv2.imshow("img", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
