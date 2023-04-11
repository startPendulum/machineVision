import cv2
import numpy as np

img = cv2.resize(cv2.imread("../img/people.jpg"), (450, 600))

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (10, 10))
new_img = cv2.erode(img, kernel, iterations=1)

cv2.imshow("img", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
