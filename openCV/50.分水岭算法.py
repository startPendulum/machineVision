import cv2
import numpy as np

coin = cv2.resize(cv2.imread("../img/coin.jpg"), (700, 700))
coin_gray = cv2.cvtColor(coin, cv2.COLOR_BGR2GRAY)
coin_gray = cv2.medianBlur(coin_gray, 9)
_, coin_thresh = cv2.threshold(coin_gray, 200, 255, cv2.THRESH_BINARY_INV)
kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
kernel3 = cv2.getStructuringElement(cv2.MORPH_RECT, (50, 50))

# 开运算去噪
coin_open = cv2.morphologyEx(coin_thresh, cv2.MORPH_CLOSE, kernel1, iterations=6)

# 确定背景
background = cv2.dilate(coin_open, kernel1, iterations=5)

# 算出每个像素距背景的距离
distance = cv2.distanceTransform(coin_open, cv2.DIST_L2, 5)

# 归一化，使距离按照0-1缩放，可以得到一张距离灰度图
cv2.normalize(distance, distance, 0, 1.0, cv2.NORM_MINMAX)

# 确定前景,即把距离灰度图二值化
_, front = cv2.threshold(distance, 0.8 * distance.max(), 255, cv2.THRESH_BINARY)

# 求出未知区域，分水岭算法中未知区域即轮廓
# 保证front和background数值是同一类型
front = np.uint8(front)
unknown = cv2.subtract(background, front)

# 求连通域，用0标记背景，用大于0的整数标记前景，为分水岭算法做准备,返回每个像素的值和每个像素的标记
# connectedComponents要求输入的图片是8位的单通道图片，即单通道的0到255的图片
_, markers = cv2.connectedComponents(front)

# 分水岭算法中用0标记不确定区域,1是背景,大于1是前景,需要对标记进行处理
markers += 1

# 从markers中筛选出未知区域
markers[unknown == 255] = 0

# watershed返回的markers做了修改,未知区域(边界)变为-1
markers = cv2.watershed(coin, markers)
print(markers.min(), markers.max())
coin[markers == -1] = (0, 0, 255)

# 单独标记出前景q
coin[markers > 1] = (0, 255, 0)

# 抠图，mask要扣的地方赋值255，其他位置赋0
mask = markers.copy()
print(coin.shape,mask.shape)
mask=np.uint8(mask)
mask[mask > 1] = 255
mask[mask != 255] = 0
result = cv2.bitwise_and(coin, coin, mask=mask)

cv2.imshow("coin", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
