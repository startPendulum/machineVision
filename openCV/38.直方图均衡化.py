import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.resize(cv2.imread("../img/1.png"), (450, 600))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 变黑
img_dark = gray - 40

# 变亮
img_light = gray + 40

gray_hist = cv2.calcHist([gray], [0], None, [256], [0, 255])
dark_hist = cv2.calcHist([img_dark], [0], None, [256], [0, 255])
light_hist = cv2.calcHist([img_light], [0], None, [256], [0, 255])
plt.plot(gray_hist, label="gray")
plt.plot(dark_hist, label="dark")
plt.plot(light_hist, label="light")
plt.legend()
plt.show()

# 进行均衡化处理
dark_equ = cv2.equalizeHist(img_dark)
light_equ = cv2.equalizeHist(img_light)
dark_equ_hist = cv2.calcHist([dark_equ], [0], None, [256], [0, 255])
light_equ_hist = cv2.calcHist([light_equ], [0], None, [256], [0, 255])
plt.plot(dark_equ_hist, label="dark")
plt.plot(light_equ_hist, label="light")
plt.legend()
plt.show()

cv2.imshow("img", np.hstack((gray, dark_equ, light_equ)))
cv2.waitKey(0)
cv2.destroyAllWindows()
