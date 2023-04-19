import cv2
import numpy as np

img = cv2.resize(cv2.imread("../img/people1.jpg"), (450, 600))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.ones((11, 11), np.uint8)
new_img = cv2.erode(img, kernel, iterations=1)

cv2.imshow("img", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
