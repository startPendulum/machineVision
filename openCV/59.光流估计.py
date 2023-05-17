import cv2
import numpy as np

video = cv2.VideoCapture("../img/video.mp4")

flag, last_frame = video.read()
last_frame_gray = cv2.cvtColor(last_frame, cv2.COLOR_BGR2GRAY)
feature_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7)

# 角点检测
last_points = cv2.goodFeaturesToTrack(last_frame_gray, mask=None, **feature_params)
while flag:
    flag, frame = video.read()
    if not flag:
        break
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 光流估计
    next_points, status, err = cv2.calcOpticalFlowPyrLK(last_frame_gray, frame_gray, last_points, None)
    next_points = next_points[status == 1].astype("int")
    good_last_points = last_points[status == 1].astype("int")
    last_frame = frame
    last_frame_gray = cv2.cvtColor(last_frame, cv2.COLOR_BGR2GRAY)
    for (p1, p2) in zip(good_last_points, next_points):
        frame=cv2.line(frame, p1, p2, (0, 0, 255))
        print(p1,p2)
    cv2.imshow("frame", frame)
    key = cv2.waitKey(25)
    if key > 0:
        cv2.destroyAllWindows()
        break
