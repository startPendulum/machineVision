import cv2
import numpy as np

img = np.zeros((600, 600, 3), np.uint8)
# 分割通道
b, g, r = cv2.split(img)
print(b)
b[10:100, 10:100] = 255
g[10:100, 10:100] = 255
# r[10:100,10:100]=255
b[:, :1] = 255
g[:, :1] = 255
r[:, :1] = 255

# 合并通道
new_img = cv2.merge((b, g, r))
cv2.imshow("img", np.hstack((img, new_img)))
cv2.waitKey(0)
cv2.destroyAllWindows()
