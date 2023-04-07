import cv2


def callback(value):
    print(value)


cv2.namedWindow("color", cv2.WINDOW_NORMAL)
img = cv2.imread("../img/2.png",cv2.IMREAD_COLOR)
colorspaces = [
    cv2.COLOR_BGR2RGBA, cv2.COLOR_BGR2BGRA, cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2HSV, cv2.COLOR_BGR2YUV
]
cv2.createTrackbar("bar", "color", 0, 4, callback)
while True:
    index = cv2.getTrackbarPos("bar", "color")
    cvt_img = cv2.cvtColor(img, colorspaces[index])
    cv2.imshow("color", cvt_img)
    key = cv2.waitKey(1000//20)
    if key == 27:
        cv2.destroyAllWindows()
        break
