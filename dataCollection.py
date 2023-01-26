import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
capture = cv2.VideoCapture(0)
detect = HandDetector(maxHands=1)
space = 30
while True:
    result, img = capture.read()
    hands, img = detect.findHands(img)
    if hands:
        x, y, w, h = hands[0]['bbox']
        crop = img[y-space:y+h+space, x-space:x+w+space]
        cv2.imshow("crop", crop)
    # white=np.zeros()
    # cv2.imshow("White screen",white)


    cv2.imshow("image", img)
    cv2.waitKey(1)

