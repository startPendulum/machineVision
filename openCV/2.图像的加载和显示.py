import matplotlib.pyplot as plt
import cv2

img=cv2.imread("../img/1.png")
cv2.imshow("img",img)
key =cv2.waitKey(0)
if key==27:
    cv2.destroyAllWindows()