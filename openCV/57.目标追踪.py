import cv2
import numpy as np

# 创建追踪器
trackers = cv2.legacy.MultiTracker_create()
cap = cv2.VideoCapture("../img/video.mp4")

while True:
    flag, frame = cap.read()
    if flag:
        success, boxes = trackers.update(frame)
        for box in boxes:
            box = box.astype(np.uint8)
            cv2.rectangle(frame, box[:2], (box[0] + box[2], box[1] + box[3]), (0, 0, 255), 2)
        key = cv2.waitKey(25)
        cv2.imshow("frame", frame)
        if key == 13:
            roi = cv2.selectROI("frame", frame, showCrosshair=True, fromCenter=False)
            # roi是(x,y,w,h)
            print(roi)
            tracker = cv2.legacy.TrackerKCF_create()
            trackers.add(tracker, frame, roi)
        elif key >= 0:
            cv2.destroyAllWindows()
            break

cap.release()
