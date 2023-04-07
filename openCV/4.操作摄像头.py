import cv2
# 打开摄像头
cap=cv2.VideoCapture(0)

while True:
    # 读取一帧
    ret, img = cap.read()
    cv2.imshow("img", img)
    key=cv2.waitKey(1000//20)
    if key==27:
        cv2.destroyAllWindows()
        cap.release()
        break