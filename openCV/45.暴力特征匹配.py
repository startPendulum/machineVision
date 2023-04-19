import cv2
import numpy as np

# 特征匹配旨在不同图片中寻找同一个物体的特征

img1 = cv2.resize(cv2.imread("../img/people1.jpg"), (450, 600))
img2 = cv2.resize(cv2.imread("../img/people2.jpg"), (450, 600))
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()
kp1, description1 = sift.detectAndCompute(gray1, None)
kp2, description2 = sift.detectAndCompute(gray2, None)

# 创建暴力匹配对象
bf = cv2.BFMatcher(cv2.NORM_L2)
# 进行匹配
match = bf.match(description1, description2)
result = cv2.drawMatches(img1, kp1, img2, kp2, match, None)

# knnMatch
knn_match = bf.knnMatch(description1, description2, 2)
knn_result = cv2.drawMatchesKnn(img1, kp1, img2, kp2, knn_match, None)

# 对knnMatch的结果进行距离筛选
good_match = []
for m, n in knn_match:
    # 设定阈值，距离小于对方距离的0.7倍，认为是好的匹配点
    if m.distance < 0.75 * n.distance:
        good_match.append(m)

knn_result = cv2.drawMatches(img1, kp1, img2, kp2, good_match, None)
cv2.imshow("img", result)
cv2.imshow("img_knn", knn_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
