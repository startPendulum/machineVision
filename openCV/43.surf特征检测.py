# 已申请专利，需要低版本才能使用
# 速度快点，准确率居中
import cv2
import numpy as np


img=cv2.resize(cv2.imread("../img/number.png"),(450,600))
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 创建surf对象
surf=cv2.xfeatures2d.SURF_create()

# 返回列表，里面是keypoint对象
kp=surf.detect(gray)
# 计算描述子
kp,des=surf.compute(gray,kp)

# 一步计算
kp,des=surf.detectAndCompute(img,None)

cv2.drawKeypoints(gray,kp,img,(0,0,255))