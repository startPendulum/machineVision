import cv2
import numpy as np

cap = cv2.VideoCapture("../../img/video.mp4")
# cap = cv2.VideoCapture(0)
# 创建背景
mog = cv2.createBackgroundSubtractorMOG2()
# 获取卷积核
kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (6, 6))

while True:
    flag, frame = cap.read()

    if flag:
        # 把原始帧灰度话，然后去噪
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 5)

        # 在图像中应用背景，自动去除背景
        mask = mog.apply(blur)

        # # 腐蚀去噪
        # erode = cv2.erode(mask, kernel1)
        #
        # # 膨胀还原图像
        # dialte = cv2.dilate(erode, kernel1, iterations=1)

        # 开运算降噪
        open = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel1, iterations=2)

        # 闭运算消除内部块
        close = cv2.morphologyEx(open, cv2.MORPH_CLOSE, kernel2, iterations=3)
        thresh, binary = cv2.threshold(close, 100, 255, cv2.THRESH_BINARY)

        # 寻找轮廓
        contours, index = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if w >= 40 and h >= 40:
                cv2.rectangle(frame, (int(x), int(y)), (int(x + w), int(y + h)), color=(0, 0, 255), thickness=2)
        cv2.line(frame, (0, 450), (1000, 450), (0, 255, 0), thickness=2)
        # if y//2<=450 or y//2>=450
        cv2.imshow("cap", frame)
    key = cv2.waitKey(1000 // 40)
    if key == 27:
        cap.release()
        cv2.destroyAllWindows()
        break
