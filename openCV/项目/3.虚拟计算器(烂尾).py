# 需要安装cvzone和mediapipe
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)

cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# 创建手部检测器
hand_detector = HandDetector(maxHands=1, detectionCon=0.8)

# 计算器格子宽高
width = 40
height = 50
box_start = (50, 100)
box_end = (50 + width * 4, 100 + height * 4)

while True:
    flag, frame = cap.read()

    # 翻转画面
    frame = cv2.flip(frame, 1)

    lastNum = 10
    if flag:

        # 检测手

        hand_points, frame = hand_detector.findHands(frame, flipType=False)

        # 画计算器

        cv2.rectangle(frame, box_start, box_end, (128, 128, 128), thickness=-1)
        cv2.rectangle(frame, box_start, box_end, (0, 0, 0))
        for y in range(3):
            for x in range(4):
                start_x = 50 + x * 40
                start_y = 150 + y * 50
                end_x = 50 + (x + 1) * 40
                end_y = 150 + (y + 1) * 50
                cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (0, 0, 0))
                if x != 3:
                    cv2.putText(frame, str(y * 3 + x + 1), (start_x + 5, start_y + 40), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                                1, (0, 0, 0))

        if hand_points:
            lmList = hand_points[0]["lmList"]
            length, _, img = hand_detector.findDistance(lmList[8][:2], lmList[16][:2], frame)
            if length < 40 and lmList[8][0] >= box_start[0] and lmList[8][0] <= box_end[0] and lmList[8][1] >= box_start[1] and lmList[8][1] <= box_end[1]:
                num = (lmList[8][1] - box_start[1] - 100) // height * 3 + (lmList[8][0] - box_start[0]) // width
            # print(lmList[8])
                if num != lastNum:
                    lastNum = num
            # print(num, lastNum)
            cv2.imshow("frame", frame)
            key = cv2.waitKey(1000 // 25)
            if key == 27:
                cap.release()
            cv2.destroyAllWindows()
            break
