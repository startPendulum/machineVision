import cv2
import numpy as np

img = cv2.resize(cv2.imread("../img/number.png"), (450, 600))

# 开运算=腐蚀+膨胀
# 开运算可以去除图形外部的噪声
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
open_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel,iterations=1)
# 闭运算=膨胀+腐蚀
# 闭运算可以去除图形内部的噪声
close_img=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel,iterations=1)

cv2.imshow("open_img", open_img)
cv2.imshow("close_img", close_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
