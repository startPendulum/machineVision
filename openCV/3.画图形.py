import cv2
import numpy as np
bg=np.zeros((600,600,3),np.uint8)
cv2.line(bg,(0,0),(600,600),(255,255,255),5)
cv2.imshow("board",bg)
key=cv2.waitKey(0)
if key==27:
    cv2.destroyAllWindows()
