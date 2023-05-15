import cv2
import numpy as np


class App:
    mouse_down = False
    start_x = 0
    start_y = 0
    rect_w = 0
    rect_h = 0
    draw_img = []

    def __init__(self, image):
        self.image = image

    def run(self):

        img = cv2.imread(self.image)
        img = cv2.resize(img, (500, 700))
        self.img = img
        self.draw_img = self.img
        cv2.namedWindow("img")

        # 绑定鼠标事件
        cv2.setMouseCallback("img", self.mouseEvent)
        while True:

            cv2.imshow("img", self.draw_img)
            key = cv2.waitKey(1)
            if key == 13:
                print(1)
                rect = (self.start_x, self.start_y, self.rect_w, self.rect_h)
                mask = np.zeros(self.img.shape[:2], dtype=np.uint8)
                cv2.grabCut(self.img, mask, rect, None, None, 2, cv2.GC_INIT_WITH_RECT)
                mask = np.where(((mask == 1) | (mask == 3)), 255, 0).astype(np.uint8)
                result = cv2.bitwise_and(self.img, self.img, mask=mask)
                cv2.imshow("img", result)
                cv2.waitKey(0)
                break
            elif key > 0:
                break
        cv2.destroyAllWindows()

    def mouseEvent(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.start_x = x
            self.start_y = y
            self.mouse_down = True
        elif event == cv2.EVENT_LBUTTONUP:
            self.mouse_down = False
            self.rect_w = abs(x - self.start_x)
            self.rect_h = abs(y - self.start_y)
        elif event == cv2.EVENT_MOUSEMOVE:
            if self.mouse_down:
                self.draw_img = self.img.copy()
                cv2.rectangle(self.draw_img, (self.start_x, self.start_y), (x, y), (0, 0, 255), 2)


if __name__ == "__main__":
    app = App("../img/people1.jpg")
    app.run()
