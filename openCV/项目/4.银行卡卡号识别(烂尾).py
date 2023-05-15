import cv2
import numpy as np

card = cv2.imread("../../img/card.jpg")
number = cv2.imread("../../img/numbers.png")

_, card_thresh = cv2.threshold(cv2.cvtColor(card, cv2.COLOR_BGR2GRAY), 100, 200, cv2.THRESH_BINARY)
_, number_thresh = cv2.threshold(cv2.cvtColor(number, cv2.COLOR_BGR2GRAY), 100, 200, cv2.THRESH_BINARY)
card_gray=cv2.cvtColor(card,cv2.COLOR_BGR2GRAY)
number_gray=cv2.cvtColor(number,cv2.COLOR_BGR2GRAY)

# 找出数字的轮廓
contours, index = cv2.findContours(number_thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(number,contours,-1,(0,0,255),2)

# 查找最小外接矩形
temp_min_rect = []
for contour in contours:
    min_rect = cv2.minAreaRect(contour)
    if min_rect[1][0] >= 25 and min_rect[1][0] <= 100 and min_rect[1][1] >= 25 and min_rect[1][1] <= 100:
        points = cv2.boxPoints(min_rect)
        points = np.round(points).astype("int")
        temp_min_rect.append(points)

temp_min_rect=sorted(temp_min_rect, key=lambda rect: rect[0][0], reverse=False)
# print(temp_min_rect)
# print(temp_min_rect)

# cv2.drawContours(number, temp_min_rect, 1, (0, 0, 255), 2)
for temp in temp_min_rect:
    print(temp)
    print(number_gray.shape)
    print(temp[2][1],temp[0][1],temp[0][0],temp[2][0])
    res=cv2.matchTemplate(card_gray,number_gray[temp[2][1]:temp[0][1],temp[0][0]:temp[2][0]],cv2.TM_CCOEFF_NORMED)



cv2.imshow("card", card)
cv2.waitKey(0)
cv2.destroyAllWindows()
