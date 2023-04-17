import cv2
import numpy as np

img = cv2.resize(cv2.imread("../img/number.png"), (450, 600))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, maxCorners=0, qualityLevel=0.01, minDistance=10)
corners = np.int32(corners)
for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 2, (0, 0, 255))
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
