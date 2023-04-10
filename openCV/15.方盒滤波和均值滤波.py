import cv2
import numpy as np

# 这俩滤波效果没啥区别

img = cv2.resize(cv2.imread("../img/1.png"), (600, 600))
# 均值滤波
# 均值滤波没有位深ddepth
blur_img = cv2.blur(img, (5, 5))
# 方盒滤波
# 方盒滤波不需要创建卷积核，只需要告诉方盒滤波卷积核的大小是什么
# normalize指定卷积核是否除以卷积核的面积，即归一化处理，normalize为True时的效果和均值滤波效果相同，
boxFilter_img = cv2.boxFilter(img, -1, (5, 5), normalize=True)

cv2.imshow("blur", blur_img)
cv2.imshow("boxFilter", boxFilter_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
