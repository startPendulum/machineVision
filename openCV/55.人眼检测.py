import cv2
import numpy as np

people = cv2.imread("../img/people1.jpg")
people = cv2.resize(people, (500, 700))
people_gray = cv2.cvtColor(people, cv2.COLOR_BGR2GRAY)

eye = cv2.CascadeClassifier("../venv/Lib/site-packages/cv2/data/haarcascade_eye_tree_eyeglasses.xml")
eyes = eye.detectMultiScale(people_gray)

for eye in eyes:
    # 每个eye是[x,y,w,h]
    print(eye)
    cv2.rectangle(people, eye[:2], (eye[0] + eye[2], eye[1] + eye[3]), (0, 0, 255), 2)

cv2.imshow("people",people)
cv2.waitKey(0)
cv2.destroyAllWindows()