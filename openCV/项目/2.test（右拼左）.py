import cv2
import numpy as np

# left = cv2.resize(cv2.imread("../../img/left.png"), (610, 482))
# right = cv2.resize(cv2.imread("../../img/right.png"), (610, 482))
left = cv2.imread("../../img/left.png")
right = cv2.imread("../../img/right.png")

sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(left, None)
kp2, des2 = sift.detectAndCompute(right, None)

bf = cv2.BFMatcher()
# 寻找两张图片匹配的特征点
matches = bf.knnMatch(des1, des2, 2)
good_matches = []
for m, n in matches:
    if m.distance <= 0.7 * n.distance:
        good_matches.append(m)
matches_img = cv2.drawMatchesKnn(left, kp1, right, kp2, [good_matches], None)
cv2.imshow("match_img", matches_img)

if len(good_matches) >= 4:
    # 得到特征点
    src_points = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    dst_points = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

    # 计算单应性矩阵
    H, _ = cv2.findHomography(src_points, dst_points, cv2.RANSAC, 5)
else:
    print("合格特征点不足")
    exit()

# 获取原始图像的高和宽
h1, w1 = left.shape[:2]
h2, w2 = right.shape[:2]

# 原始图像的四个顶点坐标
left_points = np.float32([[0, 0], [0, h1 - 1], [w1 - 1, h1 - 1], [w1 - 1, 0]]).reshape(-1, 1, 2)
right_points = np.float32([[0, 0], [0, h2 - 1], [w2 - 1, h2 - 1], [w2 - 1, 0]]).reshape(-1, 1, 2)

# 根据H计算出right四个角变换之后的坐标
left_transform = cv2.perspectiveTransform(left_points, H)

# 转换后的左底点和右底点
[left_trans_rightBottom, left_trans_h] = np.int32(left_transform.max(axis=0).ravel())
[left_trans_leftBottom, _] = np.int32(left_transform.min(axis=0).ravel())

left_points = np.concatenate((left_points, left_transform), axis=0)

[x_min, y_min] = np.int32(left_points.min(axis=0).ravel() - 1)
[x_max, y_max] = np.int32(left_points.max(axis=0).ravel() + 1)

# 平移矩阵
M = np.float32([
    [1, 0, w1 - 1 - left_trans_leftBottom - 1 - left_trans_rightBottom - 1],
    [0, 1, 0],
    [0, 0, 1]
])
# 对right平移后进行透视变换，得到的图像是匹配的图像，为了使全部图像显示出来，需要先对原图像进行平移
new_right = cv2.warpPerspective(right, M.dot(H), (int(w1 - left_trans_leftBottom), h1))
print(left_trans_h)
new_right[0:h1, 0:w1] = left
cv2.imshow("new_right", new_right)
# cv2.imshow("left", left)
# cv2.imshow("right", right)
# cv2.imshow("new_left", new_left)
cv2.waitKey(0)
cv2.destroyAllWindows()
