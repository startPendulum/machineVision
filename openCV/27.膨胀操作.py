import cv2
import numpy as np

img = cv2.resize(cv2.imread("../img/number.png"), (450, 600))

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
new_img = cv2.dilate(img, kernel, iterations=1)

cv2.imshow("img", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
