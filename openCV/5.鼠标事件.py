import cv2
import numpy as np


def mouseCallback(event, x, y, flags, userdata):
    print(event, x, y, flags, userdata)


cv2.namedWindow("mouse", cv2.WINDOW_NORMAL)
cv2.setMouseCallback("mouse", mouseCallback, "123")
img = np.zeros((360, 360, 3), np.uint8)
while True:
    cv2.imshow("mouse", img)
    key = cv2.waitKey(1000 // 20)
    if key == 27:
        cv2.destroyAllWindows()
        break
