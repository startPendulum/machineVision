import cv2
import numpy as np

people = cv2.imread("../img/people2.jpg")
people = cv2.resize(people, (500, 700))

# 要处理的区域x,y,w,h
rect = (100, 100, 300, 450)

# 处理结果放入mask
mask = np.zeros(people.shape[:2], dtype=np.uint8)
cv2.grabCut(people, mask, rect, None, None, 2, cv2.GC_INIT_WITH_RECT)

# mask中0是背景，1前景，2可能的背景，3可能的前景
mask = np.where(((mask == 1) | (mask == 3)), 255, 0).astype(np.uint8)
result = cv2.bitwise_and(people, people, mask=mask)

cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
