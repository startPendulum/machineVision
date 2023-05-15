import cv2
import numpy as np

people = cv2.imread("../img/people2.jpg")
people = cv2.resize(people, (500, 700))
people_gray = cv2.cvtColor(people, cv2.COLOR_BGR2GRAY)

# 创建haar级联器
# m
face = cv2.CascadeClassifier("../venv/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml")

# 检测人脸
faces = face.detectMultiScale(people_gray)

for face in faces:
    # 每个face是[x,y,w,h]
    cv2.rectangle(people, face[:2], (face[0] + face[2], face[1] + face[3]), (0, 0, 255), 2)

cv2.imshow("people", people)
cv2.waitKey(0)
cv2.destroyAllWindows()
