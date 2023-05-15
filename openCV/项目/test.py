import cv2
import numpy
import numpy as np

img = cv2.resize(cv2.imread("../../img/jianli3.png"), (700, 900))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray=cv2.copyMakeBorder(gray,50,50,50,50,cv2.BORDER_CONSTANT,value=255)
# gray=cv2.resize(gray,(gray.shape[0]*2,gray.shape[1]*2))

# thresh, binary = cv2.threshold(gray, 0, 200, cv2.THRESH_BINARY)

# 卷积核
kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
kernel3 = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
kernel_x = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 1))
kernel_y = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 15))

# 闭运算和开运算，去除条条框框
open_img = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel1, iterations=1)
close_img = cv2.morphologyEx(open_img, cv2.MORPH_CLOSE, kernel1, iterations=1)

# 进行腐蚀操作，扩大文字所在方块面积
erode_img = cv2.erode(close_img, kernel_x, iterations=1)
# erode_img = cv2.erode(close_img, kernel1, iterations=3)


# erode_img = cv2.erode(erode_img, kernel_y, iterations=20)
# erode_img = cv2.erode(erode_img, kernel1, iterations=5)


# 图像二值化
# thresh = cv2.adaptiveThreshold(gray, 200, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 0)
binary, thresh = cv2.threshold(erode_img, 0, 255, cv2.THRESH_OTSU)

# 再腐蚀，扩大文字方块
# kernel4 = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 20))
# erode_img = cv2.erode(thresh, kernel4, iterations=3)

# 腐蚀过度，使文字面积过大，膨胀减小文字面积
# dilate_img = cv2.dilate(erode_img, kernel3, iterations=1)

# 寻找轮廓
contours, index = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# print(contours)

# 寻找轮廓
rect = ()
for contour in contours:
    min_rect = cv2.minAreaRect(contour)
    # print(min_rect)
    if min_rect[1][1] >= 500:
        # temp=((min_rect[0][0]-50 or 10,min_rect[0][1]-50 or 10),min_rect[1],min_rect[2])
        points = cv2.boxPoints(min_rect)
        points = np.round(points).astype("int")
        cv2.drawContours(gray, [points], -1, (0, 0, 255))
        # break

# 做垂直投影，寻找水平分界点
(h, w) = thresh.shape
# 水平黑色像素个数
row_num = np.zeros(w)
for row_index in range(h):
    for col_index in range(w):
        if (thresh[row_index][col_index] == 0):
            row_num[col_index] += 1
min_loc = np.argwhere(row_num == min(row_num))
min_loc = min_loc.flatten()

min_loc_index=int(min_loc.shape[0]/2)
print(min_loc)
cv2.line(img, (min_loc[min_loc_index], 0), (min_loc[min_loc_index], h), (0, 0, 255))

cv2.imshow("thresh", thresh)
cv2.imshow("img_copy", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
