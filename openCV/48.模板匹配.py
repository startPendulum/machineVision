import cv2
import numpy as np

img1 = cv2.imread("../img/4.png")
img2 = cv2.imread("../img/left.png")

res = cv2.matchTemplate(img1, img2, cv2.TM_SQDIFF)
# 获取匹配的最好点和最坏点的信息
print(res)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

cv2.rectangle(img1,min_loc,(min_loc[0]+img2.shape[1],min_loc[1]+img2.shape[0]),(0,0,255),thickness=2)
print(min_loc,max_loc)
cv2.imshow("img", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
