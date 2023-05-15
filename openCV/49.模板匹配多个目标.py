import cv2
import numpy as np

word = cv2.imread("../img/word.png")
n = cv2.imread("../img/n.png")

word_gray = cv2.cvtColor(word, cv2.COLOR_BGR2GRAY)
n_gray = cv2.cvtColor(n, cv2.COLOR_BGR2GRAY)

res = cv2.matchTemplate(word_gray, n_gray, cv2.TM_CCOEFF_NORMED)

# 准确率
loc=np.argwhere(res>0.8)
for point in loc:
    cv2.rectangle(word,(point[1],point[0]),(point[1]+n.shape[1],point[0]+n.shape[0]),(0,0,255),2)

cv2.imshow("img", word)
cv2.waitKey(0)
cv2.destroyAllWindows()
