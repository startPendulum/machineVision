import cv2
import numpy as np

cap = cv2.VideoCapture("../../img/video.mp4")
# 创建背景
mog = cv2.createBackgroundSubtractorMOG2()
# 获取卷积核
kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))

while True:
    flag, frame = cap.read()
    if flag:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 把原始帧灰度，然后去噪

        thresh, binary1 = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
        mask = mog.apply(binary1)

        blur = cv2.GaussianBlur(mask, (3, 3), 5)
        median_blur = cv2.medianBlur(blur, 5)
        # 开运算降噪
        open = cv2.morphologyEx(median_blur, cv2.MORPH_OPEN, kernel1, iterations=3)


        # 闭运算消除内部块
        close = cv2.morphologyEx(open, cv2.MORPH_CLOSE, kernel2, iterations=3)
        thresh, binary = cv2.threshold(close, 50, 255, cv2.THRESH_BINARY)

        # 寻找轮廓
        contours, index = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if w >= 30 and h >= 30:
                cv2.rectangle(frame, (int(x), int(y)), (int(x + w), int(y + h)), color=(0, 0, 255), thickness=2)
        cv2.imshow("cap", frame)
    key = cv2.waitKey(1000 // 40)
    if key == 27:
        cap.release()
        cv2.destroyAllWindows()
        break
