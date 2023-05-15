# meanshift是颜色涂抹的算法，meanshift可以有效的去除光泽和小范围的颜色，使前景的颜色一致

import cv2
import numpy as np

coin = cv2.imread("../img/coin.jpg")
coin = cv2.resize(coin, (500, 700))

result = cv2.pyrMeanShiftFiltering(coin, 20, 30)

cv2.imshow("result", np.hstack((result,coin)))
cv2.waitKey(0)
cv2.destroyAllWindows()
