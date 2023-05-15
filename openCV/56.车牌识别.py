# opencv模型检测出车牌，tesseract提取车牌号，tesseract需要另安装，还需安装pytesseract
# 中文识别效果不好

import cv2
import numpy as np
import pytesseract

chepai = cv2.imread("../img/chepai.jpg")
chepai = cv2.resize(chepai, (500, 400))
chepai_gray = cv2.cvtColor(chepai, cv2.COLOR_BGR2GRAY)

# 创建级联器
identifier = cv2.CascadeClassifier("../venv/Lib/site-packages/cv2/data/haarcascade_russian_plate_number.xml")

# 识别车牌
plates = identifier.detectMultiScale(chepai)
for plate in plates:
    # 每个车牌是[x,y,w,h]
    print(plate)
    (x, y, w, h) = plate
    cv2.rectangle(chepai, plate[:2], (plate[0] + plate[2], plate[1] + plate[3]), (0, 0, 255), 2)
    roi = chepai_gray[y:y + h, x:x + w]

    # 二值化
    _, roi_thresh = cv2.threshold(roi, 0, 255, cv2.THRESH_OTSU)

    # ocr识别，图片不用非得二值化
    result = pytesseract.image_to_string(roi_thresh, lang="chi_sim+eng", config="--psm 8 --oem 3")
    print(result)

cv2.imshow("chepai", roi_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
