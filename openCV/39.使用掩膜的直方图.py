import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.resize(cv2.imread("../img/1.png"), (450, 600))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

mask = np.zeros(gray.shape, np.uint8)

mask[200:400, 100:300] = 255

# gray和gray做与运算，结果再和mask做与运算
new_img = cv2.bitwise_and(gray, gray, mask=mask)

hist = cv2.calcHist([gray], [0], None, [256], [0, 255])
mask_hist = cv2.calcHist([gray], [0], mask, [256], [0, 255])
print(mask_hist.shape,mask.shape)
plt.plot(hist, label='origin')
plt.plot(mask_hist, label='mask')
plt.legend()
plt.show()

cv2.imshow("new_img", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
