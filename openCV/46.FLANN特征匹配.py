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

# 创建FLANN特征匹配对象,需要搜索算法字典和搜索参数字典
index_params=dict(algorithm=1,tree=5)
search_params=dict(checks=50)
flann=cv2.FlannBasedMatcher(index_params,search_params)

# 进行检测
matches=flann.match(description1,description2)

result=cv2.drawMatches(img1,kp1,img2,kp2,matches,None)

cv2.imshow("img",result)
cv2.waitKey(0)
cv2.destroyAllWindows()