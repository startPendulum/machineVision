import cv2
import numpy as np


img1=cv2.imread("../img/4.png")

img2=cv2.imread("../img/left.png")
# img2=cv2.resize(cv2.imread("../img/left.png"),(300,300))

cv2.imshow("left",img2)

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()

kp1, des1 = sift.detectAndCompute(gray1, None)
kp2, des2 = sift.detectAndCompute(gray2, None)

# 创建特征匹配器
index_param = dict(algorithm=1, trees=5)
search_param = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_param, search_param)
matches = flann.knnMatch(des1, des2, 2)
# print(matches[0].queryIdx, matches[0].trainIdx)
good_matches = []
for m, n in matches:
    if m.distance <= 0.75 * n.distance:
        good_matches.append(m)

# 找到特征点，计算单应性矩阵要求最少4个点
if len(good_matches) >= 4:
    src_points = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    dst_points = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

    # 根据匹配的特征点计算单应性矩阵
    H, _mask = cv2.findHomography(src_points, dst_points, cv2.RANSAC, 5)

    # 通过单应性矩阵计算计算小图在大图中的对应位置
    h, w = img2.shape[:2]
    pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)

    # 对向量进行透视变换
    dst = cv2.perspectiveTransform(pts, H)
    # 画出dts
    cv2.polylines(img1, [np.int32(dst)], True, (0, 0, 255), 2)
else:
    print("特征点不足")

cv2.imshow("img", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
